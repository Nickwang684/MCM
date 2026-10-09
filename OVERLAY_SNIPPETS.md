# Quick Reference: Code Snippets for Overlay Plots

## 1. QUICK COPY-PASTE SNIPPETS

### Pattern A: Simple Actual vs Predicted Overlay
```python
import matplotlib.pyplot as plt
import numpy as np

def plot_validation(actual, predicted, time, title, output_path):
    """Quick overlay plot template."""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Actual data (reference) - red
    ax.fill_between(time, actual, alpha=0.25, color="#c0392b")
    ax.plot(time, actual, color="#c0392b", linewidth=2.5, label="Actual")
    
    # Predicted data - blue
    ax.fill_between(time, predicted, alpha=0.25, color="#3498db")
    ax.plot(time, predicted, color="#3498db", linewidth=2.5, alpha=0.8, label="Predicted")
    
    ax.set_title(title, fontsize=16, fontweight="bold")
    ax.set_xlabel("Time", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
```

---

### Pattern B: Scatter Plot with Reference Line
```python
def plot_scatter_validation(true_values, pred_values, title, output_path):
    """Scatter plot with identity reference line."""
    plt.figure(figsize=(5, 5))
    plt.scatter(true_values, pred_values, s=6, alpha=0.5)
    
    # Reference line
    vmin = min(true_values.min(), pred_values.min())
    vmax = max(true_values.max(), pred_values.max())
    plt.plot([vmin, vmax], [vmin, vmax], color="#333333", linestyle="--", linewidth=1)
    
    plt.title(title)
    plt.xlabel("True Value")
    plt.ylabel("Predicted Value")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
```

---

### Pattern C: Multi-Signal Overlay with Legends
```python
def plot_multi_overlay(signals_dict, x_values, title, output_path):
    """Plot multiple signals with automatic color/style assignment."""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    colors = ["#c0392b", "#3498db", "#2ecc71", "#e67e22"]
    linestyles = ["-", "--", "-.", ":"]
    
    for idx, (label, signal) in enumerate(signals_dict.items()):
        color = colors[idx % len(colors)]
        style = linestyles[idx % len(linestyles)]
        
        ax.fill_between(x_values, signal, alpha=0.15, color=color)
        ax.plot(x_values, signal, color=color, linewidth=2.5, 
                label=f"{label} (Peak:{np.max(signal):.2f})", linestyle=style)
    
    ax.set_title(title, fontsize=16, fontweight="bold")
    ax.set_xlabel("Position/Time", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
```

---

### Pattern D: Stacked Subplots (Multiple Metrics)
```python
def plot_stacked_validation(df, output_path):
    """Plot multiple related metrics in stacked subplots."""
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    
    metrics = [("SOC", "soc_true", "soc_pred"),
               ("Voltage (V)", "v_true", "v_pred"),
               ("Temperature (°C)", "temp_true", "temp_pred")]
    
    for ax, (ylabel, true_col, pred_col) in zip(axes, metrics):
        ax.plot(df["time"], df[true_col], label="True", linewidth=2)
        ax.plot(df["time"], df[pred_col], label="Predicted", linewidth=2, alpha=0.8)
        ax.set_ylabel(ylabel, fontsize=11)
        ax.legend(loc="best", fontsize=10)
        ax.grid(True, alpha=0.3)
    
    axes[-1].set_xlabel("Time (s)", fontsize=12)
    fig.suptitle("Validation: Multi-Metric Comparison", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
```

---

### Pattern E: With Annotation Box (Statistics)
```python
def plot_with_stats(actual, predicted, time, title, output_path):
    """Overlay plot with error metrics in annotation box."""
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Calculate metrics
    mse = mean_squared_error(actual, predicted)
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mse)
    
    # Plot overlays
    ax.fill_between(time, actual, alpha=0.25, color="#c0392b")
    ax.plot(time, actual, color="#c0392b", linewidth=2.5, label="Actual")
    
    ax.fill_between(time, predicted, alpha=0.25, color="#3498db")
    ax.plot(time, predicted, color="#3498db", linewidth=2.5, alpha=0.8, label="Predicted")
    
    # Add statistics box
    stats_text = f"RMSE: {rmse:.4f}\nMAE: {mae:.4f}\nMSE: {mse:.6f}"
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            fontsize=11, verticalalignment="top",
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))
    
    ax.set_title(title, fontsize=16, fontweight="bold")
    ax.set_xlabel("Time (s)", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.legend(fontsize=11, loc="lower right")
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
```

---

## 2. COLOR PALETTE QUICK REFERENCE

```python
# Define at top of your plotting module
CODEBASE_COLORS = {
    "actual":    "#c0392b",    # Dark red for true/actual values
    "predicted": "#3498db",    # Dark blue for predicted values
    "error":     "#e74c3c",    # Light red for errors
    "reference": "#333333",    # Dark gray for reference lines
    "grid":      "#999999",    # Medium gray for grid
    "alt1":      "#2ecc71",    # Green (secondary)
    "alt2":      "#e67e22",    # Orange (tertiary)
    "alt3":      "#9b59b6",    # Purple (quaternary)
}

# Usage
ax.plot(x, y, color=CODEBASE_COLORS["actual"], linewidth=2.5)
```

---

## 3. STANDARD FIGURE CONFIGURATIONS

```python
# Standard imports for all plotting files
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Standard matplotlib config (add to top of each script)
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.unicode_minus"] = False

# Standard figure sizes
FIGURE_SIZES = {
    "scatter":    (5, 5),       # Square for scatter/validation
    "overlay":    (12, 7),      # Wide for overlay comparison
    "stacked_2":  (12, 8),      # Two stacked subplots
    "stacked_3":  (12, 10),     # Three stacked subplots
    "wide":       (14, 5),      # Ultra-wide for side-by-side
    "heatmap":    (14, 5),      # For 2D heatmaps
}

# Standard line/point styling
PLOT_STYLE = {
    "linewidth":           2.5,
    "reference_linewidth": 1,
    "scatter_size":        6,
    "scatter_alpha":       0.5,
    "fill_alpha":          0.25,
    "grid_alpha":          0.3,
    "reference_alpha":     0.5,
}

# Standard font sizes
FONT_SIZES = {
    "title":    16,
    "suptitle": 16,
    "label":    12,
    "legend":   11,
    "tick":     10,
    "text":     11,
}
```

---

## 4. VALIDATION CHECKLIST

Before saving a new overlay plot:

- [ ] **Colors**: Using dark variant for "actual/true", light variant for "predicted"?
- [ ] **Transparency**: Fill alpha is `0.25`? Scatter alpha is `0.5`?
- [ ] **Lines**: Main curves are `linewidth=2.5`? Reference lines are `linewidth=1`?
- [ ] **Figure size**: Using appropriate size from `FIGURE_SIZES`?
- [ ] **Labels**: Title, xlabel, ylabel all present and formatted?
- [ ] **Legend**: Present with meaningful labels including metric values?
- [ ] **Grid**: `grid(True, alpha=0.3)` applied?
- [ ] **DPI**: `savefig(..., dpi=150)` for high quality?
- [ ] **Output**: Saved to correct `results/` or `plots/` directory?
- [ ] **File naming**: Follows `fig[N]_description.png` convention?

---

## 5. COMMON MODIFICATIONS

### Change color scheme
```python
# Swap red/blue
ax.plot(x, y, color="#3498db", ...)  # Use blue for actual instead
ax.plot(x, pred, color="#c0392b", ...) # Use red for predicted instead
```

### Add more transparency to fill
```python
# From 0.25 to 0.15 for even subtler background
ax.fill_between(x, y, alpha=0.15, color="#c0392b")
```

### Add error band/uncertainty
```python
# Plot mean with confidence interval fill
ax.fill_between(x, lower_bound, upper_bound, alpha=0.25, color="#3498db")
ax.plot(x, mean, color="#3498db", linewidth=2.5, label="Mean")
```

### Adjust legend position
```python
# Options: "upper left", "upper right", "lower left", "lower right", "best"
ax.legend(fontsize=11, loc="lower left")  # Change from "upper right"
```

### Add reference lines
```python
# Vertical line
ax.axvline(x=center, color="gray", linestyle="--", alpha=0.5, linewidth=1)

# Horizontal line
ax.axhline(y=threshold, color="gray", linestyle="--", alpha=0.5, linewidth=1)

# Diagonal (for scatter plots)
ax.plot([vmin, vmax], [vmin, vmax], color="#333333", linestyle="--", linewidth=1)
```

---

## 6. FILE PATHS FOR REFERENCE

| Purpose | Path | Example Files |
|---------|------|---|
| Model validation | `2026A/model/compare/` | `plot_results.py` |
| Time series test | `2025A/test/` | `plot_time_comparison.py` |
| Wear model analysis | `2025A/test/` | `plot_separate_figures.py` |
| Bayesian analysis | `2025A/test/` | `plot_bayesian_model.py` |
| Output results | `results/` or `plots/` | `.png` files |

---

## 7. IMPORTS YOU'LL NEED

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sklearn.metrics import mean_squared_error, mean_absolute_error  # Optional
```

---

**Last Updated**: Analysis of codebase plotting patterns
**Files Analyzed**: 4 Python plotting scripts, 2 plotting modules
