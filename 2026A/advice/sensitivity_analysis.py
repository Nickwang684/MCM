"""
Sensitivity Analysis for Battery Life Prediction Model
Factors analyzed:
1. Power consumption (P)
2. Temperature (T)
3. CPU utilization (U_CPU)
4. Screen brightness (B)
5. Battery health/SOH
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from SALib.sample import saltelli
from SALib.analyze import sobol
import warnings
warnings.filterwarnings('ignore')

# Set up matplotlib for publication-quality figures
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

# ============================================================
# Battery Model Parameters
# ============================================================
Q_NOM = 3.0  # Ah - nominal capacity
V_NOM = 3.7  # V - nominal voltage
SOC_MIN = 0.05  # Minimum SOC (5%)
SOC_0 = 1.0  # Initial SOC (100%)
T_REF = 298.15  # K (25°C)

# Power model parameters
P_BASE = 0.3  # W - base power (always on)
P_DISPLAY_MAX = 1.5  # W - maximum display power
P_CPU_MAX = 3.0  # W - maximum CPU power
P_NETWORK = 0.5  # W - network power (average)
P_GPS = 0.3  # W - GPS power when active

# ============================================================
# Battery Life Model
# ============================================================
def compute_power(U_CPU, B, T):
    """
    Compute total power consumption
    
    Parameters:
    - U_CPU: CPU utilization [0, 1]
    - B: Screen brightness [0, 1]
    - T: Temperature in Kelvin
    """
    # Display power (OLED approximation)
    P_display = P_DISPLAY_MAX * B
    
    # CPU power (quadratic relationship with utilization)
    P_CPU = P_CPU_MAX * (0.2 + 0.8 * U_CPU**1.5)
    
    # Temperature effect on power (leakage current increases with T)
    T_celsius = T - 273.15
    temp_factor = 1.0 + 0.005 * max(0, T_celsius - 25)
    
    P_total = (P_BASE + P_display + P_CPU + P_NETWORK) * temp_factor
    return P_total

def temperature_correction(T):
    """Temperature correction factor for effective capacity"""
    T_celsius = T - 273.15
    if T_celsius < 25:
        return 1.0 - 0.008 * (25 - T_celsius)  # Capacity reduction at low T
    elif T_celsius > 40:
        return 1.0 - 0.003 * (T_celsius - 40)  # Slight reduction at high T
    return 1.0

def battery_life_model(params):
    """
    Main battery life prediction model
    
    Parameters (in order):
    - P_factor: Power consumption factor [0.5, 2.0] (multiplier)
    - T: Temperature [273, 318] K (0-45°C)
    - U_CPU: CPU utilization [0.1, 1.0]
    - B: Screen brightness [0.1, 1.0]
    - SOH: State of Health [0.7, 1.0]
    
    Returns:
    - t_empty: Time to empty in hours
    """
    P_factor, T, U_CPU, B, SOH = params
    
    # Compute power consumption
    P_base = compute_power(U_CPU, B, T)
    P = P_base * P_factor
    
    # Effective capacity with temperature and SOH correction
    f_T = temperature_correction(T)
    Q_eff = Q_NOM * SOH * f_T
    
    # Average voltage (simplified linear model)
    V_avg = V_NOM - 0.2 * (1 - SOH)  # Voltage drops with degradation
    
    # Time to empty
    energy_available = Q_eff * (SOC_0 - SOC_MIN) * V_avg  # Wh
    t_empty = energy_available / P  # hours
    
    return t_empty

def battery_life_model_vectorized(X):
    """Vectorized version for SALib"""
    return np.array([battery_life_model(x) for x in X])

# ============================================================
# Sobol Sensitivity Analysis
# ============================================================
def run_sobol_analysis(N=512):
    """
    Run Sobol sensitivity analysis
    
    Parameters:
    - N: Number of base samples (total evaluations = N*(2D+2))
    """
    # Define the problem
    problem = {
        'num_vars': 5,
        'names': ['Power Factor', 'Temperature', 'CPU Utilization', 
                  'Screen Brightness', 'Battery Health (SOH)'],
        'bounds': [
            [0.5, 2.0],      # Power factor
            [273.15, 318.15], # Temperature (0-45°C)
            [0.1, 1.0],      # CPU utilization
            [0.1, 1.0],      # Screen brightness
            [0.7, 1.0]       # SOH
        ]
    }
    
    # Generate samples using Saltelli's scheme
    print(f"Generating {N} base samples...")
    param_values = saltelli.sample(problem, N, calc_second_order=True)
    print(f"Total model evaluations: {len(param_values)}")
    
    # Run model
    print("Running model evaluations...")
    Y = battery_life_model_vectorized(param_values)
    
    # Analyze
    print("Computing Sobol indices...")
    Si = sobol.analyze(problem, Y, calc_second_order=True)
    
    return problem, Si, Y

# ============================================================
# One-at-a-Time (OAT) Analysis
# ============================================================
def run_oat_analysis(n_points=50):
    """
    Run One-at-a-Time sensitivity analysis
    """
    # Base values
    base = {
        'P_factor': 1.0,
        'T': 298.15,  # 25°C
        'U_CPU': 0.5,
        'B': 0.5,
        'SOH': 0.9
    }
    
    # Ranges for each parameter
    ranges = {
        'P_factor': np.linspace(0.5, 2.0, n_points),
        'T': np.linspace(273.15, 318.15, n_points),
        'U_CPU': np.linspace(0.1, 1.0, n_points),
        'B': np.linspace(0.1, 1.0, n_points),
        'SOH': np.linspace(0.7, 1.0, n_points)
    }
    
    # Labels for plotting
    labels = {
        'P_factor': 'Power Factor',
        'T': r'Temperature ($^\circ$C)',
        'U_CPU': 'CPU Utilization',
        'B': 'Screen Brightness',
        'SOH': 'Battery Health (SOH)'
    }
    
    results = {}
    
    for param_name, param_range in ranges.items():
        t_empty_values = []
        for val in param_range:
            params = [base['P_factor'], base['T'], base['U_CPU'], base['B'], base['SOH']]
            idx = list(base.keys()).index(param_name)
            params[idx] = val
            t_empty = battery_life_model(params)
            t_empty_values.append(t_empty)
        
        results[param_name] = {
            'values': param_range if param_name != 'T' else param_range - 273.15,
            't_empty': np.array(t_empty_values),
            'label': labels[param_name]
        }
    
    return results

# ============================================================
# Visualization Functions
# ============================================================
def plot_sobol_indices(problem, Si, save_path):
    """Create bar chart of Sobol indices"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    names = problem['names']
    S1 = Si['S1']
    ST = Si['ST']
    S1_conf = Si['S1_conf']
    ST_conf = Si['ST_conf']
    
    x = np.arange(len(names))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, S1, width, label=r'First-order $S_1$', 
                   color='#2ecc71', edgecolor='black', linewidth=0.5,
                   yerr=S1_conf, capsize=3)
    bars2 = ax.bar(x + width/2, ST, width, label=r'Total-order $S_T$', 
                   color='#3498db', edgecolor='black', linewidth=0.5,
                   yerr=ST_conf, capsize=3)
    
    ax.set_ylabel('Sensitivity Index')
    ax.set_title('Sobol Sensitivity Indices for Battery Life Prediction')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=15, ha='right')
    ax.legend(loc='upper right')
    ax.set_ylim(0, 1.0)
    ax.axhline(y=0.1, color='gray', linestyle='--', alpha=0.5, label='Threshold')
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar, val in zip(bars1, S1):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
                f'{val:.3f}', ha='center', va='bottom', fontsize=8)
    for bar, val in zip(bars2, ST):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
                f'{val:.3f}', ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.savefig(save_path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {save_path}")
    plt.close()

def plot_oat_analysis(oat_results, save_path):
    """Create OAT sensitivity plots"""
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    axes = axes.flatten()
    
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
    
    param_order = ['P_factor', 'T', 'U_CPU', 'B', 'SOH']
    
    for i, param_name in enumerate(param_order):
        ax = axes[i]
        data = oat_results[param_name]
        
        ax.plot(data['values'], data['t_empty'], color=colors[i], linewidth=2.5)
        ax.fill_between(data['values'], data['t_empty'] * 0.95, data['t_empty'] * 1.05,
                       color=colors[i], alpha=0.2)
        
        ax.set_xlabel(data['label'])
        ax.set_ylabel('Battery Life (hours)')
        ax.set_title(f'Effect of {data["label"]}')
        ax.grid(True, alpha=0.3)
        
        # Add sensitivity metric
        sensitivity = (data['t_empty'].max() - data['t_empty'].min()) / data['t_empty'].mean() * 100
        ax.text(0.95, 0.95, f'Range: {sensitivity:.1f}%', transform=ax.transAxes,
               ha='right', va='top', fontsize=9, 
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Use last subplot for summary
    ax = axes[5]
    sensitivities = []
    for param_name in param_order:
        data = oat_results[param_name]
        sens = (data['t_empty'].max() - data['t_empty'].min()) / data['t_empty'].mean() * 100
        sensitivities.append(sens)
    
    bars = ax.barh(range(len(param_order)), sensitivities, color=colors)
    ax.set_yticks(range(len(param_order)))
    ax.set_yticklabels([oat_results[p]['label'] for p in param_order])
    ax.set_xlabel('Relative Sensitivity (%)')
    ax.set_title('OAT Sensitivity Ranking')
    ax.grid(axis='x', alpha=0.3)
    
    for bar, val in zip(bars, sensitivities):
        ax.text(val + 1, bar.get_y() + bar.get_height()/2, f'{val:.1f}%',
               va='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.savefig(save_path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {save_path}")
    plt.close()

def plot_interaction_heatmap(Si, problem, save_path):
    """Create interaction heatmap from second-order indices"""
    fig, ax = plt.subplots(figsize=(8, 7))
    
    names = problem['names']
    short_names = ['Power', 'Temp', 'CPU', 'Brightness', 'SOH']
    n = len(names)
    
    # Create matrix
    S2_matrix = np.zeros((n, n))
    S2 = Si['S2']
    
    # Fill matrix (S2 is lower triangular in SALib)
    for i in range(n):
        for j in range(i+1, n):
            S2_matrix[i, j] = S2[i, j]
            S2_matrix[j, i] = S2[i, j]
    
    # Put S1 on diagonal
    for i in range(n):
        S2_matrix[i, i] = Si['S1'][i]
    
    im = ax.imshow(S2_matrix, cmap='YlOrRd', vmin=0, vmax=0.5)
    
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(short_names, rotation=45, ha='right')
    ax.set_yticklabels(short_names)
    
    # Add text annotations
    for i in range(n):
        for j in range(n):
            val = S2_matrix[i, j]
            color = 'white' if val > 0.25 else 'black'
            ax.text(j, i, f'{val:.3f}', ha='center', va='center', 
                   color=color, fontsize=9)
    
    ax.set_title('Sensitivity Indices: Diagonal = First-order, Off-diagonal = Interactions')
    
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Sensitivity Index')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.savefig(save_path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {save_path}")
    plt.close()

def plot_comprehensive_sensitivity(problem, Si, oat_results, save_path):
    """Create a comprehensive sensitivity analysis figure"""
    fig = plt.figure(figsize=(14, 10))
    
    # Layout: 2x2 grid
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.25)
    
    # ========== Subplot 1: Sobol Indices Bar Chart ==========
    ax1 = fig.add_subplot(gs[0, 0])
    
    names = ['Power', 'Temp', 'CPU', 'Brightness', 'SOH']
    S1 = Si['S1']
    ST = Si['ST']
    
    x = np.arange(len(names))
    width = 0.35
    
    ax1.bar(x - width/2, S1, width, label=r'$S_1$', color='#2ecc71', edgecolor='black', linewidth=0.5)
    ax1.bar(x + width/2, ST, width, label=r'$S_T$', color='#3498db', edgecolor='black', linewidth=0.5)
    
    ax1.set_ylabel('Sensitivity Index')
    ax1.set_title('(a) Sobol Sensitivity Indices')
    ax1.set_xticks(x)
    ax1.set_xticklabels(names)
    ax1.legend(loc='upper right')
    ax1.set_ylim(0, 0.8)
    ax1.grid(axis='y', alpha=0.3)
    
    # ========== Subplot 2: Tornado Chart ==========
    ax2 = fig.add_subplot(gs[0, 1])
    
    # Calculate impact range for each parameter
    param_order = ['P_factor', 'T', 'U_CPU', 'B', 'SOH']
    impacts = []
    for param_name in param_order:
        data = oat_results[param_name]
        low = data['t_empty'].min()
        high = data['t_empty'].max()
        impacts.append((low, high))
    
    base_value = battery_life_model([1.0, 298.15, 0.5, 0.5, 0.9])
    
    colors_low = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
    colors_high = ['#c0392b', '#2980b9', '#27ae60', '#d68910', '#8e44ad']
    
    y_pos = np.arange(len(param_order))
    
    for i, ((low, high), param_name) in enumerate(zip(impacts, param_order)):
        ax2.barh(i, low - base_value, left=base_value, color=colors_low[i], alpha=0.7, height=0.6)
        ax2.barh(i, high - base_value, left=base_value, color=colors_high[i], alpha=0.7, height=0.6)
    
    ax2.axvline(x=base_value, color='black', linestyle='-', linewidth=1.5)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([oat_results[p]['label'] for p in param_order])
    ax2.set_xlabel('Battery Life (hours)')
    ax2.set_title('(b) Tornado Diagram (Impact Range)')
    ax2.grid(axis='x', alpha=0.3)
    
    # ========== Subplot 3: OAT Curves ==========
    ax3 = fig.add_subplot(gs[1, 0])
    
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
    
    for i, param_name in enumerate(['P_factor', 'U_CPU', 'B', 'SOH']):
        data = oat_results[param_name]
        # Normalize x-axis to [0, 1]
        if param_name == 'P_factor':
            x_norm = (data['values'] - 0.5) / 1.5
        elif param_name == 'SOH':
            x_norm = (data['values'] - 0.7) / 0.3
        else:
            x_norm = (data['values'] - 0.1) / 0.9
        
        # Normalize y-axis
        t_norm = (data['t_empty'] - data['t_empty'].min()) / (data['t_empty'].max() - data['t_empty'].min())
        
        ax3.plot(x_norm, t_norm, color=colors[i], linewidth=2, label=data['label'])
    
    ax3.set_xlabel('Normalized Parameter Value')
    ax3.set_ylabel('Normalized Battery Life')
    ax3.set_title('(c) OAT Response Curves')
    ax3.legend(loc='upper right', fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    
    # ========== Subplot 4: Summary Table ==========
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    
    # Create summary table
    table_data = []
    headers = ['Factor', r'$S_1$', r'$S_T$', 'OAT Range (%)', 'Classification']
    
    for i, param_name in enumerate(param_order):
        data = oat_results[param_name]
        oat_range = (data['t_empty'].max() - data['t_empty'].min()) / data['t_empty'].mean() * 100
        
        if ST[i] > 0.3:
            classification = 'HIGH'
        elif ST[i] > 0.1:
            classification = 'MEDIUM'
        else:
            classification = 'LOW'
        
        table_data.append([names[i], f'{S1[i]:.3f}', f'{ST[i]:.3f}', f'{oat_range:.1f}%', classification])
    
    table = ax4.table(cellText=table_data, colLabels=headers,
                     loc='center', cellLoc='center',
                     colColours=['#f0f0f0']*5)
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)
    
    # Color code the classification column
    for i in range(len(param_order)):
        cell = table[(i+1, 4)]
        if table_data[i][4] == 'HIGH':
            cell.set_facecolor('#ffcccc')
        elif table_data[i][4] == 'MEDIUM':
            cell.set_facecolor('#ffffcc')
        else:
            cell.set_facecolor('#ccffcc')
    
    ax4.set_title('(d) Sensitivity Classification Summary', y=0.95)
    
    plt.suptitle('Comprehensive Sensitivity Analysis for Battery Life Prediction', 
                fontsize=14, fontweight='bold', y=1.02)
    
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.savefig(save_path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {save_path}")
    plt.close()

def plot_spider_chart(oat_results, save_path):
    """Create spider/radar chart for sensitivity comparison"""
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    param_order = ['P_factor', 'T', 'U_CPU', 'B', 'SOH']
    labels = ['Power\nFactor', 'Temperature', 'CPU\nUtilization', 'Screen\nBrightness', 'Battery\nHealth']
    
    # Calculate normalized sensitivities
    sensitivities = []
    for param_name in param_order:
        data = oat_results[param_name]
        sens = (data['t_empty'].max() - data['t_empty'].min()) / data['t_empty'].mean()
        sensitivities.append(sens)
    
    # Normalize to [0, 1]
    max_sens = max(sensitivities)
    sensitivities_norm = [s / max_sens for s in sensitivities]
    
    # Number of variables
    num_vars = len(labels)
    
    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Complete the loop
    sensitivities_norm += sensitivities_norm[:1]
    angles += angles[:1]
    
    # Plot
    ax.plot(angles, sensitivities_norm, 'o-', linewidth=2, color='#3498db')
    ax.fill(angles, sensitivities_norm, alpha=0.25, color='#3498db')
    
    # Set the labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=11)
    
    # Set y-axis
    ax.set_ylim(0, 1.1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(['25%', '50%', '75%', '100%'], size=9)
    
    ax.set_title('Relative Sensitivity of Battery Life Factors', size=13, y=1.08)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.savefig(save_path.replace('.png', '.pdf'), bbox_inches='tight')
    print(f"Saved: {save_path}")
    plt.close()

# ============================================================
# Main Execution
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Battery Life Sensitivity Analysis")
    print("=" * 60)
    
    # Output directory
    output_dir = "D:/jingsai/shumo/MCM/2026A/final/PAPER/figures/"
    
    # Run Sobol analysis
    print("\n[1/4] Running Sobol Sensitivity Analysis...")
    problem, Si, Y = run_sobol_analysis(N=512)
    
    # Print Sobol results
    print("\n" + "=" * 60)
    print("SOBOL SENSITIVITY INDICES")
    print("=" * 60)
    print(f"{'Parameter':<25} {'S1':>10} {'S1_conf':>10} {'ST':>10} {'ST_conf':>10}")
    print("-" * 65)
    for i, name in enumerate(problem['names']):
        print(f"{name:<25} {Si['S1'][i]:>10.4f} {Si['S1_conf'][i]:>10.4f} {Si['ST'][i]:>10.4f} {Si['ST_conf'][i]:>10.4f}")
    
    # Run OAT analysis
    print("\n[2/4] Running One-at-a-Time Analysis...")
    oat_results = run_oat_analysis(n_points=50)
    
    # Print OAT results
    print("\n" + "=" * 60)
    print("OAT SENSITIVITY RESULTS")
    print("=" * 60)
    for param_name, data in oat_results.items():
        t_min, t_max, t_mean = data['t_empty'].min(), data['t_empty'].max(), data['t_empty'].mean()
        range_pct = (t_max - t_min) / t_mean * 100
        print(f"{data['label']:<25}: {t_min:.2f} - {t_max:.2f} h (range: {range_pct:.1f}%)")
    
    # Generate figures
    print("\n[3/4] Generating Figures...")
    
    plot_sobol_indices(problem, Si, output_dir + "fig_sensitivity_sobol.png")
    plot_oat_analysis(oat_results, output_dir + "fig_sensitivity_oat.png")
    plot_interaction_heatmap(Si, problem, output_dir + "fig_sensitivity_interactions.png")
    plot_comprehensive_sensitivity(problem, Si, oat_results, output_dir + "fig_sensitivity_comprehensive.png")
    plot_spider_chart(oat_results, output_dir + "fig_sensitivity_spider.png")
    
    # Print summary for LaTeX table
    print("\n[4/4] Summary for LaTeX Table...")
    print("\n" + "=" * 60)
    print("LATEX TABLE DATA")
    print("=" * 60)
    
    print("\n% Copy this into your LaTeX document:")
    print("\\begin{tabular}{@{}clcccl@{}}")
    print("\\toprule")
    print("\\textbf{Rank} & \\textbf{Factor} & $\\mathbf{S_1}$ & $\\mathbf{S_T}$ & \\textbf{OAT Range} & \\textbf{Class} \\\\")
    print("\\midrule")
    
    # Sort by ST
    indices = np.argsort(Si['ST'])[::-1]
    param_order = ['P_factor', 'T', 'U_CPU', 'B', 'SOH']
    names_full = ['Power Factor ($P$)', 'Temperature ($T$)', 'CPU Utilization ($U_{CPU}$)', 
                  'Screen Brightness ($B$)', 'Battery Health (SOH)']
    
    for rank, i in enumerate(indices, 1):
        data = oat_results[param_order[i]]
        oat_range = (data['t_empty'].max() - data['t_empty'].min()) / data['t_empty'].mean() * 100
        
        if Si['ST'][i] > 0.3:
            cls = "HIGH"
        elif Si['ST'][i] > 0.1:
            cls = "MEDIUM"
        else:
            cls = "LOW"
        
        print(f"{rank} & {names_full[i]} & {Si['S1'][i]:.3f} & {Si['ST'][i]:.3f} & {oat_range:.1f}\\% & {cls} \\\\")
    
    print("\\bottomrule")
    print("\\end{tabular}")
    
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)
