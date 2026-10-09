---
description: Perform data analysis and visualization
mode: agent
tools: ['read', 'edit', 'search', 'execute']
---

# Data Analysis and Visualization

Analyze the provided dataset and create comprehensive visualizations:

## Analysis Steps
1. **Data Loading**: Load and inspect the dataset
2. **Data Cleaning**: Handle missing values, outliers, duplicates
3. **Exploratory Analysis**: Summary statistics, distributions
4. **Correlation Analysis**: Identify relationships between variables
5. **Visualization**: Create informative plots

## Required Outputs
- Summary statistics table
- Distribution plots for key variables
- Correlation heatmap
- Time series plots (if applicable)
- Scatter plots with trend lines

## Visualization Standards
- Use `matplotlib` and `seaborn` for static plots
- Use `plotly` for interactive visualizations
- Include descriptive titles and axis labels
- Use colorblind-friendly palettes
- Export in both PNG (for preview) and PDF (for report)

## Code Template
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('colorblind')

# Load data
df = pd.read_csv('data.csv')

# Summary statistics
print(df.describe())

# Distribution plots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# ... plotting code

plt.tight_layout()
plt.savefig('analysis.pdf', dpi=300, bbox_inches='tight')
```
