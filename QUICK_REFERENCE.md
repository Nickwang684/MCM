# Visual Guide: Overlay Plotting Patterns Quick Reference

## Quick Pattern Selector

### 🎯 What do you need to plot?

```
1. MEASURED vs MODEL OUTPUT (Validation)
   ├─ Scatter plot + diagonal line
   ├─ Figure: (5, 5)
   ├─ Colors: true vs pred
   └─ File: plot_results.py:30-47

2. TIME SERIES COMPARISON (Two signals)
   ├─ Filled curves overlay
   ├─ Figure: (12, 7)
   ├─ Colors: Light fill + darker line per signal
   └─ File: plot_time_comparison.py:86-125

3. MULTI-SCENARIO (4+ curves)
   ├─ Multiple lines + linestyles
   ├─ Figure: (12, 7)
   ├─ Colors: Different + linestyle variation
   └─ File: plot_separate_figures.py:148-176

4. STACKED METRICS (3+ related signals)
   ├─ Subplots with sharex
   ├─ Figure: (9, 6) to (12, 10)
   ├─ Colors: Simple true/pred per subplot
   └─ File: plot_results.py:84-103
```

---

## One-Liner Code Reference

### Setup
```python
import matplotlib.pyplot as plt; import numpy as np
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
```

### Pattern 1: Scatter Validation
```python
plt.figure(figsize=(5,5)); plt.scatter(true, pred, s=6, alpha=0.5); 
v_min, v_max = min(true.min(), pred.min()), max(true.max(), pred.max())
plt.plot([v_min, v_max], [v_min, v_max], color="#333333", linestyle="--", linewidth=1)
plt.title("Validation"); plt.xlabel("True"); plt.ylabel("Predicted"); plt.tight_layout()
plt.savefig("validation.png", dpi=150); plt.close()
```

### Pattern 2: Two-Signal Overlay
```python
fig, ax = plt.subplots(figsize=(12, 7))
ax.fill_between(x, sig1, alpha=0.25, color="#e74c3c")
ax.plot(x, sig1, color="#c0392b", linewidth=2.5, label="Signal 1")
ax.fill_between(x, sig2, alpha=0.25, color="#3498db")
ax.plot(x, sig2, color="#2980b9", linewidth=2.5, label="Signal 2")
ax.legend(); ax.grid(True, alpha=0.3); plt.tight_layout()
plt.savefig("overlay.png", dpi=150); plt.close()
```

### Pattern 3: Multi-Line with Styles
```python
fig, ax = plt.subplots(figsize=(12, 7))
for (label, color, linestyle), signal in zip([("A","#3498db","-"),("B","#e67e22","--")], [sig1, sig2]):
    ax.plot(x, signal, color=color, linestyle=linestyle, linewidth=2.5, label=label)
ax.legend(); ax.grid(True, alpha=0.3); plt.tight_layout()
plt.savefig("multi.png", dpi=150); plt.close()
```

---

## Color Quick Pick

```
PRIMARY (Actual/True):      #c0392b (dark red)
SECONDARY (Predicted):      #3498db (dark blue)
FILL ACTUAL:               #e74c3c (light red)
FILL PREDICTED:            #2980b9 (light blue)
REFERENCE LINES:           #333333 (dark gray)

ALTERNATIVES (if needed):
  Green:    #2ecc71 / #27ae60
  Orange:   #e67e22
  Purple:   #9b59b6 / #8e44ad
  Teal:     #1abc9c
```

---

## Alpha Value Cheat Sheet

```
Scatter points:    0.5   (semi-transparent, see overlaps)
Main lines:        1.0   (opaque, solid)
Fill under curve:  0.25  (very light, subtle background)
Predicted overlay: 0.8   (slightly faded, still visible)
Grid:              0.3   (subtle guides)
Reference line:    0.5   (medium visibility)
Annotation box:    0.7   (readable background)
```

---

## Figure Size Quick Pick

```
(5, 5)       → Scatter validation plots
(9, 6)       → Single overlay time series
(12, 7)      → Standard overlay comparison
(12, 8)      → 2-subplot stacked
(12, 10)     → 3-subplot stacked
(14, 5)      → Ultra-wide side-by-side
(14, 10)     → 4-subplot grid
```

---

## Common Line Styles

```
"-"   Solid line       (main signals)
"--"  Dashed line      (reference, secondary signals)
"-."  Dash-dot line    (tertiary signals)
":"   Dotted line      (quaternary signals)
```

---

## Standard Formatting Template

```python
# UNIVERSAL TEMPLATE - Copy and modify

def plot_overlay_template(signal1, signal2, x_values, output_path):
    """Template for adding new overlay plots."""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Signal 1 (actual/reference/true)
    ax.fill_between(x_values, signal1, alpha=0.25, color="#c0392b")
    ax.plot(x_values, signal1, color="#c0392b", linewidth=2.5, 
            label=f"Signal 1 (Peak: {signal1.max():.2f})")
    
    # Signal 2 (predicted/comparison)
    ax.fill_between(x_values, signal2, alpha=0.25, color="#3498db")
    ax.plot(x_values, signal2, color="#3498db", linewidth=2.5, alpha=0.8,
            label=f"Signal 2 (Peak: {signal2.max():.2f})")
    
    # Formatting (ALWAYS INCLUDE)
    ax.set_title("Overlay Comparison Title", fontsize=16, fontweight="bold")
    ax.set_xlabel("X-axis Label", fontsize=12)
    ax.set_ylabel("Y-axis Label", fontsize=12)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

# USAGE:
# plot_overlay_template(actual_data, predicted_data, time_array, "results/fig1_comparison.png")
```

---

## Matplotlib Setup Copy-Paste

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# ===== MATPLOTLIB CONFIG =====
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.unicode_minus"] = False

# ===== OUTPUT SETUP =====
OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ===== COLOR PALETTE =====
COLORS = {
    "actual":    "#c0392b",
    "predicted": "#3498db",
    "error":     "#e74c3c",
    "grid":      "#333333",
}

# ===== STANDARD PARAMS =====
LINEWIDTH = 2.5
SCATTER_SIZE = 6
SCATTER_ALPHA = 0.5
FILL_ALPHA = 0.25
GRID_ALPHA = 0.3
DPI = 150

# Ready to plot!
```

---

## Validation Checklist (Before Saving)

```
□ Colors correct? (dark for actual, light for predicted)
□ Alphas correct? (fill 0.25, scatter 0.5, line 1.0)
□ Line width OK? (2.5 for main, 1 for reference)
□ Title present and bold? (fontsize=16)
□ Labels present? (xlabel, ylabel with fontsize=12)
□ Legend present? (fontsize=11, loc="upper right")
□ Grid enabled? (alpha=0.3)
□ Figure size appropriate? (check against size guide above)
□ DPI=150 for savefig? 
□ File named correctly? (fig[N]_description.png)
□ Saved to results/ folder?
```

---

## Error Troubleshooting

```
Q: "Curves overlap too much"
A: Increase fill_alpha from 0.25 to 0.35 OR add linestyle variation (- vs --)

Q: "Can't see predicted curve"
A: Remove alpha=0.8 from predicted plot line OR use lighter color

Q: "Legend too small/unreadable"
A: Increase fontsize from 11 to 13 OR move to different location

Q: "Saved image too fuzzy"
A: Check dpi=150 (increase to 200 if still blurry)

Q: "Can't read tiny x-axis numbers"
A: Rotate x labels: ax.set_xticklabels(..., rotation=45)

Q: "Lines blend into background grid"
A: Reduce grid alpha from 0.3 to 0.15 OR increase line linewidth to 3.0

Q: "Colors don't match other plots"
A: Use exact hex codes from COLOR PALETTE above (copy-paste, don't eyeball)

Q: "Saved PNG looks different than display"
A: Add bbox_inches='tight' to savefig: plt.savefig(..., bbox_inches='tight', dpi=150)
```

---

## Key Files to Reference

| File | Purpose | Key Function |
|------|---------|---|
| `2026A/model/compare/plot_results.py` | Model validation | `plot_ocv_scatter()`, `plot_lg_sample_trace()` |
| `2025A/test/plot_time_comparison.py` | Time series | `plot_overlay_short_long()` |
| `2025A/test/plot_separate_figures.py` | Scenarios | `plot_overlay_comparison()` |
| `2025A/test/plot_bayesian_model.py` | Distributions | `plot_scenario_comparison()` |

---

## ONE-PAGE SUMMARY

**For actual vs predicted overlay:**
1. Use figure size `(12, 7)`
2. Plot actual with fill: `fill_between(alpha=0.25, color="#c0392b")` + `plot(color="#c0392b", linewidth=2.5)`
3. Plot predicted with fill: `fill_between(alpha=0.25, color="#3498db")` + `plot(color="#3498db", linewidth=2.5, alpha=0.8)`
4. Add labels, legend, grid: `grid(True, alpha=0.3)`, `legend(fontsize=11, loc="upper right")`
5. Save: `savefig(path, dpi=150)` to `results/fig[N]_name.png`

**That's it! Copy template above and modify data source.**

---

*Generated from analysis of 4 plotting modules in codebase*
*All patterns verified against existing code*
*Ready for copy-paste implementation*
