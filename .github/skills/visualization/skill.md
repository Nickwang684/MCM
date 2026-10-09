---
name: visualization
description: Data visualization toolkit for creating publication-quality figures and interactive plots. Use when asked to plot, visualize, graph, or create charts.
version: 1.0.0
---

# Visualization Skill

## When to Use This Skill
- Creating publication-quality figures
- Exploratory data visualization
- Interactive dashboards
- Geographic/spatial visualizations
- Network diagrams

## Recommended Libraries

| Library | Use Case |
|---------|----------|
| Matplotlib | Base plotting, customization |
| Seaborn | Statistical visualizations |
| Plotly | Interactive plots |
| Altair | Declarative visualization |
| NetworkX + Matplotlib | Graph/network visualization |

## Plot Templates

### Publication-Quality Setup
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for publications
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 11,
    'figure.figsize': (8, 6),
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

# Colorblind-friendly palette
colors = sns.color_palette('colorblind')
```

### Multi-Panel Figure
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Panel labels
for ax, label in zip(axes.flat, ['(a)', '(b)', '(c)', '(d)']):
    ax.text(-0.1, 1.05, label, transform=ax.transAxes, 
            fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('figure.pdf', dpi=300)
```

### 3D Surface Plot
```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
fig.colorbar(surf, shrink=0.5, aspect=5)
```

## Best Practices
1. Always include axis labels with units
2. Use vector formats (PDF, SVG) for publications
3. Choose appropriate color schemes
4. Add legends when multiple series exist
5. Consider colorblind accessibility
