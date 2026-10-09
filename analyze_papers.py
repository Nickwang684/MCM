
import os
import pypdf
import json
from collections import defaultdict

def sanitize_text(text):
    if not text:
        return ""
    # 过滤掉无法用utf-8编码的代理字符
    return text.encode('utf-8', 'ignore').decode('utf-8', 'ignore')

def analyze():
    root1 = r"D:\competition\MathModel\national\按36个模型整理的国内比赛论文"
    root2 = r"D:\competition\MathModel\national\参考"

    all_pdfs = []
    for r in [root1, root2]:
        for dp, _, fns in os.walk(r):
            for f in fns:
                if f.lower().endswith('.pdf'):
                    all_pdfs.append(os.path.join(dp, f))

    print(f"Total PDFs found: {len(all_pdfs)}")

    patterns = {
        "sensitivity": ["敏感性分析", "鲁棒性", "Robustness", "Sensitivity Analysis", "扰动"],
        "figure_specs": ["三线表", "残差", "流程图", "Fig.", "Table", "热力图", "分布图", "拟合曲"],
        "model_logic": ["假设", "Assumption", "符号说明", "Notations", "微分方程", "离散化", "求解器", "机理模型"],
        "evaluation": ["优点", "缺点", "评价", "推广", "展望"]
    }

    results = []
    for i, path in enumerate(all_pdfs):
        try:
            reader = pypdf.PdfReader(path)
            pages_to_read = list(range(min(len(reader.pages), 3))) + list(range(max(0, len(reader.pages)-5), len(reader.pages)))
            
            content = ""
            for p_idx in sorted(list(set(pages_to_read))):
                text_page = reader.pages[p_idx].extract_text() or ""
                content += sanitize_text(text_page)
            
            matches = {cat: [p for p in p_list if p in content] for cat, p_list in patterns.items()}
            
            results.append({
                "path": path,
                "model_category": os.path.basename(os.path.dirname(path)),
                "matches": matches,
                "summary_snippet": content[:500].replace("\n", " ")
            })
            
            if (i+1) % 100 == 0:
                print(f"Processed {i+1}/{len(all_pdfs)}...")
        except Exception as e:
            continue

    with open("detailed_paper_analysis.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Analysis complete and saved successfully.")

if __name__ == "__main__":
    analyze()
