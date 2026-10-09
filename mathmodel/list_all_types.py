import os
from pypdf import PdfReader
import re

def analyze_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for i in range(min(1, len(reader.pages))):
            text += reader.pages[i].extract_text()
        
        text_norm = text.replace('\n', ' ').replace('  ', ' ')
        
        problem_type = "Unknown"
        if re.search(r"Problem\s*Chosen\s*[:]?\s*A", text_norm, re.IGNORECASE):
            problem_type = "A"
        elif re.search(r"Problem\s*Chosen\s*[:]?\s*B", text_norm, re.IGNORECASE):
            problem_type = "B"
        elif re.search(r"Problem\s*Chosen\s*[:]?\s*C", text_norm, re.IGNORECASE):
            problem_type = "C"
        elif re.search(r"Problem\s*Chosen\s*[:]?\s*D", text_norm, re.IGNORECASE):
            problem_type = "D"
        elif re.search(r"Problem\s*Chosen\s*[:]?\s*E", text_norm, re.IGNORECASE):
            problem_type = "E"
        elif re.search(r"Problem\s*Chosen\s*[:]?\s*F", text_norm, re.IGNORECASE):
            problem_type = "F"
            
        return f"{os.path.basename(file_path)}: {problem_type}"
    except:
        return f"{os.path.basename(file_path)}: Error"

base_dir = "/workspace/Nick_wangjincheng/mathmodel"
years = ["2019", "2020", "2021"]

for year in years:
    print(f"--- {year} ---")
    year_dir = os.path.join(base_dir, year)
    if os.path.exists(year_dir):
        files = [f for f in os.listdir(year_dir) if f.endswith(".pdf")]
        for f in files[:10]: # Limit to 10
            print(analyze_pdf(os.path.join(year_dir, f)))
