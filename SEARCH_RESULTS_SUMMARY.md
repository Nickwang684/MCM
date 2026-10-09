# Search Results Summary: Overlay Plotting Patterns

## Task Completion Status ✅

**TASK**: Search codebase for validation plots that overlay actual vs predicted signals.
**STATUS**: ✅ COMPLETE - Found 4 primary files with overlay plotting patterns

---

## Files Found and Analyzed

### 1. **Model Comparison Module** (Primary - Validation Plots)
📁 **Path**: `D:\jingsai\shumo\MCM\2026A\model\compare\plot_results.py`
- **Focus**: Battery model validation with actual vs predicted overlay
- **Key Functions**:
  - `plot_ocv_scatter()` [Lines 30-47] - Scatter plot with reference line
  - `plot_lg_sample_trace()` [Lines 84-103] - Time series overlay comparison
- **Pattern**: Scatter + diagonal reference line for validation
- **Style**: `alpha=0.5` scatter, `linewidth=1` dashed reference line

### 2. **Time Series Comparison Module**
📁 **Path**: `D:\jingsai\shumo\MCM\2025A\test\plot_time_comparison.py`
- **Focus**: Short-term vs long-term wear patterns overlay
- **Key Functions**:
  - `plot_overlay_short_long()` [Lines 86-125] - Two signals with fill_between shading
- **Pattern**: `fill_between(alpha=0.25)` + `plot(linewidth=2.5)` per signal
- **Style**: Red (`#c0392b`, `#e74c3c`) for short-term, Blue (`#2980b9`, `#3498db`) for long-term
- **Feature**: Includes annotation box with ratio metrics

### 3. **Wear Model Analysis Module**
📁 **Path**: `D:\jingsai\shumo\MCM\2025A\test\plot_separate_figures.py`
- **Focus**: Multi-scenario wear profile overlay
- **Key Functions**:
  - `plot_overlay_comparison()` [Lines 148-176] - 4+ curves with different linestyles
- **Pattern**: Multiple signals differentiated by linestyle (`"-"` solid, `"--"` dashed)
- **Style**: Colors from palette + linestyle variation for clarity
- **Feature**: Peak values in legend labels

### 4. **Bayesian Analysis Module**
📁 **Path**: `D:\jingsai\shumo\MCM\2025A\test\plot_bayesian_model.py`
- **Focus**: Posterior distributions and scenario comparisons
- **Key Functions**:
  - `plot_scenario_comparison()` [Lines 78-117] - Fill_between with annotations
  - `plot_mcmc_posterior()` [Lines 120-204] - Posterior distributions
- **Pattern**: `fill_between` for uncertainty, text boxes for parameters
- **Style**: Semi-transparent fills, parameter annotations

---

## Key Patterns Identified

### Pattern 1: Scatter + Reference Line (Validation)
```python
# From: plot_results.py:30-47
plt.scatter(df["v_true"], df["v_pred"], s=6, alpha=0.5)
plt.plot([vmin, vmax], [vmin, vmax], color="#333333", linestyle="--", linewidth=1)
```
**Use for**: Measured vs Predicted comparison
**Alpha values**: Scatter `0.5`, Line `1` (opaque)

### Pattern 2: Overlay with Fill_Between
```python
# From: plot_time_comparison.py:99-105
ax.fill_between(x_grid, wear_short, alpha=0.25, color="#e74c3c")
ax.plot(x_grid, wear_short, color="#c0392b", linewidth=2.5, label="...")
ax.fill_between(x_grid, wear_long, alpha=0.25, color="#3498db")
ax.plot(x_grid, wear_long, color="#2980b9", linewidth=2.5, label="...")
```
**Use for**: Time series signal overlay
**Alpha values**: Fill `0.25`, Plot `default` (opaque)
**Line width**: `2.5` for visibility
**Colors**: Dark variant for main signal, light variant for fill

### Pattern 3: Multi-Signal with Linestyle Variation
```python
# From: plot_separate_figures.py:158-162
for dir_mode, form_mode, label, color, style in scenarios:
    wear = model.calculate_wear_profile(x_grid, N_total)
    ax.plot(x_grid, wear, label=f"{label} (Peak:{np.max(wear):.1f})", 
            color=color, linewidth=2.5, linestyle=style)
```
**Use for**: Multiple scenarios with legend identification
**Linestyles**: Solid `"-"`, Dashed `"--"`, Dash-dot `"-."`
**Label format**: Include peak/metric values in legend

### Pattern 4: Stacked Subplots (Multiple Metrics)
```python
# From: plot_results.py:84-103
_, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
axes[0].plot(df["t_s"], df["soc_true"], label="SOC true")
axes[0].plot(df["t_s"], df["soc_pred"], label="SOC pred", alpha=0.8)
```
**Use for**: Multiple related validation metrics
**Alpha for predicted**: `0.8` (slightly transparent to show secondary)
**Layout**: `sharex=True` for aligned time axis

---

## Consistent Style Conventions Found

### 1. **Figure Sizes**
```
Square (5, 5)           → Scatter plots
Landscape (12, 7)       → Overlay comparisons  
Wide (14, 5)            → Side-by-side
Stacked 2x1 (9, 6)      → Time series subplots
Stacked 3x1 (12, 10)    → Multiple metrics
```

### 2. **Alpha Values**
```
Scatter points:         0.5   (semi-transparent for density)
Fill_between:           0.25  (very light background)
Predicted overlay:      0.8   (slightly transparent to show secondary)
Grid:                   0.3   (subtle guides)
Reference lines:        0.5   (visible but not dominant)
```

### 3. **Color Scheme** (Hex codes)
```
Dark Red:    #c0392b  → Actual/True/Primary signal
Light Red:   #e74c3c  → Fill for actual (background)
Dark Blue:   #2980b9  → Predicted/Secondary signal
Light Blue:  #3498db  → Fill for predicted (background)
Dark Gray:   #333333  → Reference lines, axis
Alternates:  #2ecc71 (Green), #e67e22 (Orange), #9b59b6 (Purple)
```

### 4. **Line Properties**
```
Main curves:        linewidth=2.5, solid "-"
Reference/Grid:     linewidth=1,   dashed "--"
Fill boundaries:    alpha=0.25 with matching color
```

### 5. **Font Sizes**
```
Title:      fontsize=16, fontweight="bold"
Axis labels: fontsize=12
Legend:     fontsize=11
Tick labels: fontsize=10
Annotations: fontsize=11-12
```

### 6. **Output Configuration**
```
DPI:        150 (consistent high quality)
Layout:     plt.tight_layout() (prevent overlap)
Directory:  results/ or plots/ subdirectory
Naming:     fig[N]_description.png (sequential)
Format:     PNG (raster, saves well)
```

---

## Usage Guidelines

### When to Use Each Pattern:

| Scenario | Pattern | File Reference | Figure Size |
|----------|---------|---|---|
| Measured vs Model Prediction | Scatter + Line | `plot_results.py:30-47` | (5, 5) |
| Battery SOC/Voltage over Time | Stacked Subplots | `plot_results.py:84-103` | (9, 6) |
| Wear Distribution (2 scenarios) | Fill_Between Overlay | `plot_time_comparison.py:86-125` | (12, 7) |
| Multi-scenario Comparison (4+) | Multi-line + Linestyle | `plot_separate_figures.py:148-176` | (12, 7) |
| Parameter Uncertainty | Fill with Annotation | `plot_time_comparison.py:116-119` | (12, 7) |

---

## Files Created (Reference Documents)

✅ **`OVERLAY_PLOTTING_REFERENCE.md`**
- Comprehensive guide with all patterns
- Code snippets for each use case
- Color palette reference
- Best practices checklist

✅ **`OVERLAY_SNIPPETS.md`**
- Copy-paste ready code templates
- 5 complete pattern functions
- Quick configuration dictionaries
- Validation checklist
- Common modifications

---

## Key Takeaways for New Overlay Plots

1. **Use established color scheme**: Dark variant for "actual", light for "predicted"
2. **Set correct alpha values**: Fill `0.25`, Scatter `0.5`, Predicted overlay `0.8`
3. **Line width**: `2.5` for main curves, `1` for references
4. **Figure size**: `(12, 7)` for standard overlays
5. **Include metrics**: Peak values, RMSE, or other stats in labels/annotations
6. **Grid and legend**: Always enable grid (`alpha=0.3`) and place legend (`loc="upper right"`)
7. **DPI and format**: Always save as `dpi=150` PNG to results folder

---

## Next Steps

Use the reference documents created to:
1. Copy appropriate pattern from `OVERLAY_SNIPPETS.md`
2. Modify data source and labels as needed
3. Verify against `OVERLAY_PLOTTING_REFERENCE.md` checklist
4. Save to `results/` or `plots/` directory with `fig[N]_name.png` format

All patterns follow existing codebase conventions and maintain consistency.
