import os
import re
from pypdf import PdfReader
from collections import Counter

def extract_info(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        # Read first 2 pages for Abstract/Keywords and Problem ID
        header_text = ""
        for i in range(min(2, len(reader.pages))):
            header_text += reader.pages[i].extract_text()
        
        # Identify Problem A
        is_problem_a = False
        if re.search(r"Problem\s*[:]?\s*A", header_text, re.IGNORECASE) or \
           re.search(r"Problem\s*Chosen\s*[:]?\s*A", header_text, re.IGNORECASE):
            is_problem_a = True
        
        if not is_problem_a:
            return None

        # Read full text for deep analysis (limit to first 15 pages to save time/memory)
        full_text = header_text
        for i in range(2, min(15, len(reader.pages))):
            full_text += reader.pages[i].extract_text()
        
        full_text_lower = full_text.lower()

        # 1. Extract Keywords
        keywords = []
        kw_match = re.search(r"Key\s*words\s*[:](.*?)(?:\n\n|\n1|Introduction)", header_text, re.IGNORECASE | re.DOTALL)
        if kw_match:
            kws = kw_match.group(1).replace('\n', ' ').split(',')
            keywords = [k.strip().lower() for k in kws if len(k.strip()) > 2]

        # 2. Detect Models
        models = []
        if "differential equation" in full_text_lower: models.append("Differential Equations")
        if "partial differential" in full_text_lower or "pde" in full_text_lower: models.append("PDE")
        if "ordinary differential" in full_text_lower or "ode" in full_text_lower: models.append("ODE")
        if "lotka-volterra" in full_text_lower: models.append("Lotka-Volterra")
        if "heat equation" in full_text_lower: models.append("Heat Equation")
        if "navier-stokes" in full_text_lower: models.append("Navier-Stokes")
        if "cellular automata" in full_text_lower: models.append("Cellular Automata")
        if "agent-based" in full_text_lower or "abm" in full_text_lower: models.append("Agent-Based Model")
        if "network" in full_text_lower and "graph" in full_text_lower: models.append("Network Model")
        if "regression" in full_text_lower: models.append("Regression")
        if "machine learning" in full_text_lower or "neural network" in full_text_lower: models.append("Machine Learning")
        if "genetic algorithm" in full_text_lower: models.append("Genetic Algorithm")
        if "simulated annealing" in full_text_lower: models.append("Simulated Annealing")
        if "monte carlo" in full_text_lower: models.append("Monte Carlo")

        # 3. Detect Validation/Sensitivity
        validation = []
        if "sensitivity analysis" in full_text_lower: validation.append("Sensitivity Analysis")
        if "robustness" in full_text_lower: validation.append("Robustness Check")
        if "stability analysis" in full_text_lower: validation.append("Stability Analysis")
        if "error analysis" in full_text_lower: validation.append("Error Analysis")
        if "cross-validation" in full_text_lower: validation.append("Cross-Validation")

        return {
            "year": file_path.split('/')[-2],
            "keywords": keywords,
            "models": models,
            "validation": validation
        }

    except Exception as e:
        return None

base_dir = "/workspace/Nick_wangjincheng/mathmodel"
years = [str(y) for y in range(2015, 2025)] # Focus on last 10 years for modern trends
all_data = []

print("Scanning papers...")
for year in years:
    year_dir = os.path.join(base_dir, year)
    if os.path.exists(year_dir):
        files = [f for f in os.listdir(year_dir) if f.endswith(".pdf")]
        for f in files:
            res = extract_info(os.path.join(year_dir, f))
            if res:
                all_data.append(res)

# Aggregation
model_counts = Counter()
validation_counts = Counter()
keyword_counts = Counter()

for item in all_data:
    model_counts.update(item['models'])
    validation_counts.update(item['validation'])
    keyword_counts.update(item['keywords'])

print(f"\nAnalyzed {len(all_data)} Problem A papers from 2015-2024.")
print("\nTop Models Used:")
for m, c in model_counts.most_common(10):
    print(f"{m}: {c}")

print("\nTop Validation Methods:")
for m, c in validation_counts.most_common(10):
    print(f"{m}: {c}")

print("\nTop Keywords:")
for k, c in keyword_counts.most_common(15):
    print(f"{k}: {c}")
