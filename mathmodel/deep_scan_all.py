import os
import re
from pypdf import PdfReader
from collections import Counter

def analyze_paper(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        # Read first 2 pages for classification
        header_text = ""
        for i in range(min(2, len(reader.pages))):
            header_text += reader.pages[i].extract_text()
        
        # Determine Type
        is_c = False
        if re.search(r"Problem\s*[:]?\s*C", header_text, re.IGNORECASE) or \
           re.search(r"Problem\s*Chosen\s*[:]?\s*C", header_text, re.IGNORECASE):
            is_c = True
        
        # User instruction: If not C (and implicitly not others if we were checking), treat as A.
        # The user said "naming without A or C are A". 
        # So if it's explicitly C, it's C. Otherwise A.
        p_type = "C" if is_c else "A"

        # Read more content for deep analysis (first 10 pages)
        full_text = header_text
        for i in range(2, min(10, len(reader.pages))):
            full_text += reader.pages[i].extract_text()
        
        full_text_lower = full_text.lower()

        # Extract specific insights
        insights = {
            "type": p_type,
            "has_flowchart": "flowchart" in full_text_lower or "flow chart" in full_text_lower,
            "has_sensitivity": "sensitivity analysis" in full_text_lower,
            "has_stability": "stability" in full_text_lower and "equilibrium" in full_text_lower,
            "has_code": "appendix" in full_text_lower and ("code" in full_text_lower or "python" in full_text_lower or "matlab" in full_text_lower),
            "models": [],
            "algorithms": []
        }

        # Keywords for Models (A & C mixed list, we filter later)
        model_keywords = [
            ("differential equation", "DE"), ("pde", "PDE"), ("ode", "ODE"),
            ("logistic", "Logistic"), ("lotka-volterra", "Lotka-Volterra"),
            ("regression", "Regression"), ("random forest", "Random Forest"),
            ("xgboost", "XGBoost"), ("lstm", "LSTM"), ("arima", "ARIMA"),
            ("neural network", "Neural Net"), ("genetic algorithm", "GA"),
            ("simulated annealing", "SA"), ("entropy weight", "Entropy Weight"),
            ("topsis", "TOPSIS"), ("ahp", "AHP")
        ]

        for kw, name in model_keywords:
            if kw in full_text_lower:
                insights["models"].append(name)

        return insights

    except Exception as e:
        return None

base_dir = "/workspace/Nick_wangjincheng/mathmodel"
years = [str(y) for y in range(2006, 2025)]
stats = {"A": Counter(), "C": Counter()}
features = {"A": Counter(), "C": Counter()}

print("Deep scanning all papers (treating unknowns as A)...")

count = 0
for year in years:
    year_dir = os.path.join(base_dir, year)
    if os.path.exists(year_dir):
        files = [f for f in os.listdir(year_dir) if f.endswith(".pdf")]
        for f in files:
            res = analyze_paper(os.path.join(year_dir, f))
            if res:
                t = res["type"]
                stats[t].update(res["models"])
                if res["has_sensitivity"]: features[t]["Sensitivity"] += 1
                if res["has_stability"]: features[t]["Stability"] += 1
                if res["has_flowchart"]: features[t]["Flowchart"] += 1
                count += 1

print(f"Analyzed {count} papers.")
print("\n=== Problem A Insights ===")
print("Top Models:", stats["A"].most_common(10))
print("Key Features:", features["A"])

print("\n=== Problem C Insights ===")
print("Top Models:", stats["C"].most_common(10))
print("Key Features:", features["C"])
