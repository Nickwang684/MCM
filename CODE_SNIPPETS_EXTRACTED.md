# Actual Code Snippets from Codebase

## 📍 Pattern 1: Scatter Validation Plot
**Source**: `D:\jingsai\shumo\MCM\2026A\model\compare\plot_results.py` (Lines 30-47)

```python
def plot_ocv_scatter() -> None:
    try:
        df = pd.read_csv(COMPARE / "ocv_points.csv")
    except Exception:
        return
    if df.empty:
        return
    plt.figure(figsize=(5, 5))
    plt.scatter(df["v_true"], df["v_pred"], s=6, alpha=0.5)
    vmin = float(min(df["v_true"].min(), df["v_pred"].min()))
    vmax = float(max(df["v_true"].max(), df["v_pred"].max()))
    plt.plot([vmin, vmax], [vmin, vmax], color="#333333", linestyle="--", linewidth=1)
    plt.title("OCV: measured vs predicted")
    plt.xlabel("Measured Voltage (V)")
    plt.ylabel("Predicted Voltage (V)")
    plt.tight_layout()
    plt.savefig(PLOTS / "ocv_scatter.png", dpi=150)
    plt.close()
```

**Key Points:**
- Square figure: `figsize=(5, 5)`
- Scatter: `s=6, alpha=0.5` (small, semi-transparent)
- Reference line: `color="#333333", linestyle="--", linewidth=1` (dark gray, dashed)
- Clean title format: "X: measured vs predicted"

---

## 📍 Pattern 2: Time Series Overlay with Fill
**Source**: `D:\jingsai\shumo\MCM\2025A\test\plot_time_comparison.py` (Lines 86-125)

```python
def plot_overlay_short_long():
    model = WearModel()
    model.set_direction_mode("bidirectional")
    model.set_formation_mode("mixed")
    
    width_cm = 200
    x_grid = np.linspace(0, width_cm, 200)
    
    wear_short, amp_short = generate_wear_profile_with_fatigue(model, x_grid, N_TOTAL, T_SHORT)
    wear_long, amp_long = generate_wear_profile_with_fatigue(model, x_grid, N_TOTAL, T_LONG)
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.fill_between(x_grid, wear_short, alpha=0.25, color="#e74c3c")
    ax.plot(x_grid, wear_short, color="#c0392b", linewidth=2.5, 
            label=f"Short-term T={T_SHORT}years (Peak:{np.max(wear_short):.1f}, Amplification:{amp_short:.2f})")
    
    ax.fill_between(x_grid, wear_long, alpha=0.25, color="#3498db")
    ax.plot(x_grid, wear_long, color="#2980b9", linewidth=2.5, 
            label=f"Long-term T={T_LONG}years (Peak:{np.max(wear_long):.1f}, Amplification:{amp_long:.2f})")
    
    ax.set_title(f"Short-term Intensive vs Long-term Sparse Wear Distribution Overlay (N={N_TOTAL:,})", 
                 fontsize=16, fontweight="bold")
    ax.set_xlabel("Stair Width Position (cm)", fontsize=12)
    ax.set_ylabel("Wear Depth (Relative Units)", fontsize=12)
    ax.set_xlim(0, width_cm)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.axvline(x=width_cm / 2, color="gray", linestyle="--", alpha=0.5)
    
    ratio = np.max(wear_short) / np.max(wear_long)
    ax.text(0.02, 0.98, f"Short/Long Wear Ratio: {ratio:.2f}x", transform=ax.transAxes,
            fontsize=12, fontweight="bold", color="#c0392b",
            verticalalignment="top", horizontalalignment="left",
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig(output_dir / "fig6_short_long_overlay.png", dpi=150)
    plt.close()
```

**Key Points:**
- Wide landscape figure: `figsize=(12, 7)`
- Each signal: `fill_between(alpha=0.25)` + `plot(linewidth=2.5)`
- Dark/light color pairs: `#c0392b`/`#e74c3c` (red), `#2980b9`/`#3498db` (blue)
- Label format: Include metric values with `.1f`, `.2f` formatting
- Annotation box: `ax.text()` with `bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7)`
- Grid: `alpha=0.3` for subtle guides
- Vertical reference line: `axvline(..., linestyle="--", alpha=0.5)`

---

## 📍 Pattern 3: Multi-Signal Overlay with Linestyles
**Source**: `D:\jingsai\shumo\MCM\2025A\test\plot_separate_figures.py` (Lines 148-176)

```python
def plot_overlay_comparison():
    fig, ax = plt.subplots(figsize=(12, 7))

    scenarios = [
        ("ascending_only", "single_file", "Ascending+Single", "#3498db", "-"),
        ("ascending_only", "side_by_side", "Ascending+Side-by-side", "#e67e22", "--"),
        ("descending_only", "single_file", "Descending+Single", "#e74c3c", "-"),
        ("descending_only", "side_by_side", "Descending+Side-by-side", "#9b59b6", "--"),
    ]

    for dir_mode, form_mode, label, color, style in scenarios:
        model.set_direction_mode(dir_mode)
        model.set_formation_mode(form_mode)
        wear = model.calculate_wear_profile(x_grid, N_total)
        ax.plot(x_grid, wear, label=f"{label} (Peak:{np.max(wear):.1f})", 
                color=color, linewidth=2.5, linestyle=style)

    ax.set_title("Four Extreme Wear Profiles Overlay (N=500k)", fontsize=16, fontweight="bold")
    ax.set_xlabel("Stair Width Position (cm)", fontsize=12)
    ax.set_ylabel("Wear Depth (Relative Units)", fontsize=12)
    ax.set_xlim(0, width_cm)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.axvline(x=width_cm / 2, color="gray", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(output_dir / "fig4_overlay_comparison.png", dpi=150)
    plt.close()
    print(f"Saved: {save_path}")
```

**Key Points:**
- Loop through scenarios with tuple unpacking: `(mode1, mode2, label, color, style)`
- Differentiate curves via linestyle: `linestyle="-"` (solid) vs `linestyle="--"` (dashed)
- Label includes metric: `f"{label} (Peak:{np.max(wear):.1f})"`
- Colors: `#3498db`, `#e67e22`, `#e74c3c`, `#9b59b6` (no need for fill_between here)

---

## 📍 Pattern 4: Stacked Subplots (Time Series)
**Source**: `D:\jingsai\shumo\MCM\2026A\model\compare\plot_results.py` (Lines 84-103)

```python
def plot_lg_sample_trace() -> None:
    try:
        df = pd.read_csv(COMPARE / "lg_sample_trace.csv")
    except Exception:
        return
    if df.empty:
        return
    _, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    axes[0].plot(df["t_s"], df["soc_true"], label="SOC true")
    axes[0].plot(df["t_s"], df["soc_pred"], label="SOC pred", alpha=0.8)
    axes[0].set_ylabel("SOC")
    axes[0].legend(loc="best")
    axes[1].plot(df["t_s"], df["v_true"], label="V true")
    axes[1].plot(df["t_s"], df["v_pred"], label="V pred", alpha=0.8)
    axes[1].set_ylabel("Voltage (V)")
    axes[1].set_xlabel("Time (s)")
    axes[1].legend(loc="best")
    plt.tight_layout()
    plt.savefig(PLOTS / "lg_sample_trace.png", dpi=150)
    plt.close()
```

**Key Points:**
- Stacked layout: `plt.subplots(2, 1, figsize=(9, 6), sharex=True)`
- Predicted curves: `alpha=0.8` (slightly transparent to show secondary nature)
- Simple labels: "true" vs "pred" suffixes
- Legend: `loc="best"` for automatic best placement
- No fill_between needed for time series in this pattern
- Grid not explicitly shown but inferred

---

## 📍 Pattern 5: With Fill_Between and Scenario Boxes
**Source**: `D:\jingsai\shumo\MCM\2025A\test\plot_separate_figures.py` (Lines 24-62)

```python
def plot_direction_comparison():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    model.set_formation_mode("single_file")
    model.set_direction_mode("ascending_only")
    wear_asc = model.calculate_wear_profile(x_grid, N_total)

    model.set_direction_mode("descending_only")
    wear_desc = model.calculate_wear_profile(x_grid, N_total)

    max_ylim = max(np.max(wear_asc), np.max(wear_desc)) * 1.1

    axes[0].fill_between(x_grid, wear_asc, alpha=0.3, color="#3498db")
    axes[0].plot(x_grid, wear_asc, color="#2980b9", linewidth=2)
    axes[0].set_title(f"Extreme Ascending\nPeak Wear: {np.max(wear_asc):.2f}", fontsize=14)
    axes[0].set_xlabel("Stair Width Position (cm)", fontsize=12)
    axes[0].set_ylabel("Wear Depth (Relative Units)", fontsize=12)
    axes[0].set_xlim(0, width_cm)
    axes[0].set_ylim(0, max_ylim)
    axes[0].grid(True, alpha=0.3)
    axes[0].axvline(x=width_cm / 2, color="gray", linestyle="--", alpha=0.5)

    axes[1].fill_between(x_grid, wear_desc, alpha=0.3, color="#e74c3c")
    axes[1].plot(x_grid, wear_desc, color="#c0392b", linewidth=2)
    axes[1].set_title(f"Extreme Descending\nPeak Wear: {np.max(wear_desc):.2f}", fontsize=14)
    axes[1].set_xlabel("Stair Width Position (cm)", fontsize=12)
    axes[1].set_ylabel("Wear Depth (Relative Units)", fontsize=12)
    axes[1].set_xlim(0, width_cm)
    axes[1].set_ylim(0, max_ylim)
    axes[1].grid(True, alpha=0.3)
    axes[1].axvline(x=width_cm / 2, color="gray", linestyle="--", alpha=0.5)

    fig.suptitle("Direction Mode Comparison (Fixed: Single-file, N=500k)", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(output_dir / "fig1_direction_comparison.png", dpi=150)
    plt.close()
```

**Key Points:**
- Side-by-side layout: `plt.subplots(1, 2, figsize=(14, 5))`
- Each subplot: `fill_between(alpha=0.3)` + `plot(linewidth=2)` (note: alpha=0.3 here vs 0.25 for overlay)
- Synchronized y-axis: `max_ylim = max(...) * 1.1` then `set_ylim(0, max_ylim)` on both
- Title includes metric: `f"Extreme Ascending\nPeak Wear: {np.max(wear_asc):.2f}"`
- Super-title: `fig.suptitle(..., fontsize=16, fontweight="bold")`

---

## 📍 Pattern 6: Bayesian Posterior with Annotations
**Source**: `D:\jingsai\shumo\MCM\2025A\test\plot_bayesian_model.py` (Lines 92-109)

```python
def plot_scenario_comparison():
    model = BayesianWearModel()
    x_grid = np.linspace(0, 200, 100)
    
    scenarios = [
        ("New Staircase (50 years) + Low Traffic", 50, 100, UsageMode.BIDIRECTIONAL, FormationMode.SINGLE_FILE, '#3498db'),
        ("Medium-age Staircase (150 years) + Medium Traffic", 150, 500, UsageMode.BIDIRECTIONAL, FormationMode.MIXED, '#2ecc71'),
        ("Ancient Staircase (300 years) + High Traffic", 300, 2000, UsageMode.BIDIRECTIONAL, FormationMode.MIXED, '#e74c3c'),
        ("Ancient Staircase (300 years) + Low Traffic", 300, 100, UsageMode.ASCENDING_ONLY, FormationMode.SINGLE_FILE, '#9b59b6'),
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    for idx, (name, age, traffic, usage, formation, color) in enumerate(scenarios):
        activity = ActivityPattern(ActivityLevel.MEDIUM, formation, traffic)
        inputs = ModelInputs(age, usage, activity)
        wear_profile = model.predict_wear_profile(inputs, x_grid)
        
        axes[idx].fill_between(x_grid, wear_profile, alpha=0.3, color=color)
        axes[idx].plot(x_grid, wear_profile, color=color, linewidth=2)
        axes[idx].set_title(f'{name}\nPeak Wear: {np.max(wear_profile):.0f}', fontsize=12)
        axes[idx].set_xlabel('Stair Width Position (cm)', fontsize=10)
        axes[idx].set_ylabel('Wear Depth', fontsize=10)
        axes[idx].set_xlim(0, 200)
        axes[idx].axvline(x=100, color='gray', linestyle='--', alpha=0.5)
        axes[idx].grid(True, alpha=0.3)
        
        info_text = f'Age: {age} years\nDaily Traffic: {traffic}\nUsage: {usage.value}\nFormation: {formation.value}'
        axes[idx].text(0.02, 0.98, info_text, transform=axes[idx].transAxes,
                       fontsize=9, verticalalignment='top',
                       bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    fig.suptitle('Wear Profile Predictions for Different Scenarios', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_dir / "bayesian_scenario_comparison.png", dpi=150)
    plt.close()
```

**Key Points:**
- Grid layout: `plt.subplots(2, 2)` with `axes.flatten()` for loop
- Each subplot: `fill_between(alpha=0.3)` + `plot(linewidth=2)`
- Multi-line title: `f'{name}\nPeak Wear: {np.max(wear_profile):.0f}'` (note `.0f` for integers)
- Parameter annotation box: `axes[idx].text(..., bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))`
- Note: Single color per subplot (not overlaid curves)

---

## 📍 Key Matplotlib Config (All Files)
**Source**: Used consistently across all plotting files

```python
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Configuration (always at top)
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.unicode_minus"] = False

# Output directory
output_dir = Path(__file__).parent / "results"
output_dir.mkdir(parents=True, exist_ok=True)

# Typical file structure:
# - Import section
# - Matplotlib config
# - Output directory setup
# - Constants (if any)
# - Function definitions
# - if __name__ == "__main__": main execution
```

---

## 📊 Summary Table: Extract Key Pattern Differences

| Aspect | Scatter | Time Series | Multi-Scenario | Stacked Subplots |
|--------|---------|-------------|---|---|
| **Figure Size** | (5, 5) | (12, 7) | (12, 7) | (9, 6) |
| **Fill Alpha** | N/A | 0.25 | N/A | N/A |
| **Line Width** | N/A | 2.5 | 2.5 | default |
| **Scatter s=** | 6 | N/A | N/A | N/A |
| **Scatter alpha** | 0.5 | N/A | N/A | N/A |
| **Linestyle** | N/A | "-" (both) | "-" and "--" | default |
| **Predicted alpha** | N/A | default | default | 0.8 |
| **Grid** | implicit | yes (0.3) | yes (0.3) | implicit |
| **Legend** | N/A | yes | yes | yes (best) |
| **Reference line** | diagonal | vertical | vertical | N/A |
| **File Example** | plot_results.py:30 | plot_time_comparison.py:86 | plot_separate_figures.py:148 | plot_results.py:84 |

---

**These are actual, production-ready code snippets from your codebase.**
**Copy and modify for new overlay plots.**
