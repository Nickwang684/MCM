from pypdf import PdfReader

def extract_sections(file_path):
    reader = PdfReader(file_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    
    # Extract Abstract (approx first 2000 chars)
    abstract = full_text[:2000]
    
    # Extract Sensitivity Analysis (find the header and take 2000 chars after)
    sens_idx = full_text.lower().find("sensitivity analysis")
    sensitivity = ""
    if sens_idx != -1:
        sensitivity = full_text[sens_idx:sens_idx+2000]
        
    # Extract Strengths (find header)
    str_idx = full_text.lower().find("strengths")
    strengths = ""
    if str_idx != -1:
        strengths = full_text[str_idx:str_idx+1000]
        
    return abstract, sensitivity, strengths

f1 = "/workspace/Nick_wangjincheng/mathmodel/2024/2400996.pdf"
abs1, sens1, str1 = extract_sections(f1)

print("=== ABSTRACT ===")
print(abs1[:500])
print("\n=== SENSITIVITY ===")
print(sens1[:500])
print("\n=== STRENGTHS ===")
print(str1[:500])
