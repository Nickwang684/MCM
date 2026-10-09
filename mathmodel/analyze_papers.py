import os
from pypdf import PdfReader
import re

def analyze_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        # Read first 3 pages
        for i in range(min(3, len(reader.pages))):
            text += reader.pages[i].extract_text()
        
        # Normalize text
        text_norm = text.replace('\n', ' ').replace('  ', ' ')
        
        problem_type = "Unknown"
        # Strict regex for "Problem Chosen"
        if re.search(r"Problem\s*Chosen\s*[:]?\s*A", text_norm, re.IGNORECASE):
            problem_type = "A"
        elif re.search(r"Problem\s*Chosen\s*[:]?\s*C", text_norm, re.IGNORECASE):
            problem_type = "C"
        # Fallback inference
        elif "Wordle" in text_norm or "Tennis" in text_norm or "Momentum" in text_norm:
             problem_type = "C (Inferred)"
        elif "Lamprey" in text_norm or "Drought" in text_norm:
             problem_type = "A (Inferred)"
            
        return {
            "filename": os.path.basename(file_path),
            "type": problem_type,
            "snippet": text_norm[:200]
        }
    except Exception as e:
        return {"filename": os.path.basename(file_path), "error": str(e)}

base_dir = "/workspace/Nick_wangjincheng/mathmodel"
years = ["2021", "2022", "2023", "2024"]
results = []

for year in years:
    year_dir = os.path.join(base_dir, year)
    if os.path.exists(year_dir):
        for f in os.listdir(year_dir):
            if f.endswith(".pdf"):
                res = analyze_pdf(os.path.join(year_dir, f))
                if "C" in res['type']:
                    results.append(res)

print(f"Found {len(results)} Problem C papers.")
for r in results:
    print(f"{r['filename']} | Type: {r['type']}")
    print(f"Snippet: {r['snippet']}...")
    print("-" * 20)
