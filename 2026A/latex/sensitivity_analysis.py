#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCM 2026 Problem A - O-Award Level Sensitivity Analysis
Battery Discharge Model Sensitivity Analysis

This script generates publication-quality figures for sensitivity analysis:
1. Sobol indices horizontal bar chart (S1 and ST)
2. One-at-a-time (OAT) sensitivity curves (4-panel)
3. Scenario matrix heatmap (Temperature × Usage × SOH)
4. Morris screening μ* vs σ scatter plot
5. Interaction effects heatmap
6. Parameter perturbation spider/radar plot

Author: MCM Team
Date: 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import Patch
import seaborn as sns
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

# Set publication-quality figure parameters
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.size'] = 11
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 13
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10
rcParams['legend.fontsize'] = 10
rcParams['figure.dpi'] = 300
rcParams['savefig.dpi'] = 300
rcParams['savefig.bbox'] = 'tight'
rcParams['axes.linewidth'] = 0.8
rcParams['grid.linewidth'] = 0.5

# Color schemes
COLORS = {
    'primary': '#2E86AB',      # Blue
    'secondary': '#A23B72',    # Magenta
    'tertiary': '#F18F01',     # Orange
    'quaternary': '#4B8F8C',   # Teal
    'highlight': '#E94F37',    # Red
    'muted': '#7D8491',        # Gray
}

# =============================================================================
# Battery Model Parameters (Baseline)
# =============================================================================
class BatteryParams:
    """Battery model parameters"""
    # Electrical parameters
    Q_nom = 3.0         # Nominal capacity [Ah]
    V_nom = 3.7         # Nominal voltage [V]
    R0 = 0.050          # Internal resistance [Ohm]
    R1 = 0.030          # RC pair 1 resistance [Ohm]
    R2 = 0.020          # RC pair 2 resistance [Ohm]
    C1 = 1000.0         # RC pair 1 capacitance [F]
    C2 = 25000.0        # RC pair 2 capacitance [F]
    
    # OCV Shepherd model: OCV = E0 + K1*SOC + K2*ln(SOC) + K3*ln(1-SOC)
    E0 = 3.685          # Base voltage [V]
    K1 = 0.2156         # Linear coefficient
    K2 = 0.0351         # Log(SOC) coefficient
    K3 = -0.0175        # Log(1-SOC) coefficient
    
    # Thermal parameters
    T_amb = 298.15      # Ambient temperature [K]
    C_th = 100.0        # Thermal capacitance [J/K]
    R_th = 5.0          # Thermal resistance [K/W]
    
    # Degradation
    SOH = 1.0           # State of Health
    
    # Power consumption model
    P_base = 0.150      # Base power [W]
    B = 0.5             # Screen brightness [0-1]
    U_cpu = 0.3         # CPU utilization [0-1]
    P_net = 0.100       # Network power [W]
    GPS = 0.0           # GPS status [0-1]
    P_gps = 0.5         # GPS power when active [W]
    
    # Initial conditions
    SOC_0 = 1.0         # Initial SOC

def calculate_ocv(soc, params):
    """Calculate Open Circuit Voltage using Shepherd model"""
    soc = np.clip(soc, 0.001, 0.999)
    return params.E0 + params.K1 * soc + params.K2 * np.log(soc) + params.K3 * np.log(1 - soc)

def calculate_power_consumption(params):
    """Calculate total power consumption"""
    P_display = 0.050 + 0.800 * (params.B ** 1.8)  # Display power [W]
    P_cpu = 0.050 + 1.950 * (params.U_cpu ** 1.5)  # CPU power [W]
    P_total = params.P_base + P_display + P_cpu + params.P_net + params.GPS * params.P_gps
    return P_total

def battery_model(t, y, params):
    """Battery state-space model ODEs"""
    SOC, V_RC1, V_RC2, T_cell = y
    
    # Calculate current from power demand
    P_load = calculate_power_consumption(params)
    V_terminal = calculate_ocv(SOC, params) - V_RC1 - V_RC2
    I_load = P_load / max(V_terminal, 2.5)
    
    # Effective parameters with SOH and temperature
    Q_eff = params.Q_nom * params.SOH
    T_factor = 1 + 0.01 * (T_cell - 298.15)  # Temperature effect on resistance
    R0_eff = params.R0 * T_factor
    
    # State equations
    dSOC_dt = -I_load / (Q_eff * 3600)
    dV_RC1_dt = (I_load * params.R1 - V_RC1) / (params.R1 * params.C1)
    dV_RC2_dt = (I_load * params.R2 - V_RC2) / (params.R2 * params.C2)
    
    # Thermal dynamics
    P_loss = I_load**2 * (R0_eff + params.R1 + params.R2)
    dT_dt = (P_loss - (T_cell - params.T_amb) / params.R_th) / params.C_th
    
    return [dSOC_dt, dV_RC1_dt, dV_RC2_dt, dT_dt]

def simulate_battery(params, SOC_cutoff=0.1, t_max=86400):
    """
    Simulate battery discharge and return time-to-empty
    
    Args:
        params: BatteryParams object
        SOC_cutoff: SOC threshold for empty [default: 0.1]
        t_max: Maximum simulation time [s]
    
    Returns:
        time_to_empty: Time until SOC reaches cutoff [hours]
    """
    y0 = [params.SOC_0, 0.0, 0.0, params.T_amb]
    
    def event_soc_low(t, y, params):
        return y[0] - SOC_cutoff
    event_soc_low.terminal = True
    event_soc_low.direction = -1
    
    try:
        sol = solve_ivp(
            lambda t, y: battery_model(t, y, params),
            [0, t_max],
            y0,
            method='RK45',
            events=lambda t, y: event_soc_low(t, y, params),
            max_step=60.0,
            rtol=1e-6,
            atol=1e-8
        )
        
        if sol.t_events[0].size > 0:
            time_to_empty = sol.t_events[0][0] / 3600  # Convert to hours
        else:
            time_to_empty = t_max / 3600
            
    except Exception as e:
        time_to_empty = t_max / 3600
    
    return time_to_empty

# =============================================================================
# Sensitivity Analysis Methods
# =============================================================================

# Parameter definitions for sensitivity analysis
PARAM_DEFINITIONS = {
    'B': {'name': 'Screen Brightness', 'symbol': 'B', 'min': 0.1, 'max': 1.0, 'baseline': 0.5, 'unit': ''},
    'U_cpu': {'name': 'CPU Utilization', 'symbol': r'$U_{CPU}$', 'min': 0.05, 'max': 0.95, 'baseline': 0.3, 'unit': ''},
    'P_net': {'name': 'Network Power', 'symbol': r'$P_{net}$', 'min': 0.05, 'max': 0.5, 'baseline': 0.1, 'unit': 'W'},
    'GPS': {'name': 'GPS Status', 'symbol': 'GPS', 'min': 0.0, 'max': 1.0, 'baseline': 0.0, 'unit': ''},
    'T_amb': {'name': 'Ambient Temp.', 'symbol': r'$T_{amb}$', 'min': 263.15, 'max': 318.15, 'baseline': 298.15, 'unit': 'K'},
    'SOC_0': {'name': 'Initial SOC', 'symbol': r'$SOC_0$', 'min': 0.2, 'max': 1.0, 'baseline': 1.0, 'unit': ''},
    'SOH': {'name': 'State of Health', 'symbol': 'SOH', 'min': 0.7, 'max': 1.0, 'baseline': 1.0, 'unit': ''},
    'Q_nom': {'name': 'Nominal Capacity', 'symbol': r'$Q_{nom}$', 'min': 2.5, 'max': 5.0, 'baseline': 3.0, 'unit': 'Ah'},
    'R0': {'name': 'Internal Resist.', 'symbol': r'$R_0$', 'min': 0.03, 'max': 0.15, 'baseline': 0.05, 'unit': r'$\Omega$'},
}

def set_param(params, param_name, value):
    """Set a parameter value on the params object"""
    setattr(params, param_name, value)

def run_sobol_analysis(n_samples=256):
    """
    Run Sobol sensitivity analysis using Saltelli sampling
    
    Returns:
        dict: Sobol indices S1, ST for each parameter
    """
    print("Running Sobol sensitivity analysis...")
    
    param_names = list(PARAM_DEFINITIONS.keys())
    n_params = len(param_names)
    
    # Generate Saltelli samples (simplified approach)
    N = n_samples
    
    # Base samples
    np.random.seed(42)
    A = np.random.random((N, n_params))
    B = np.random.random((N, n_params))
    
    # Scale samples to parameter ranges
    def scale_samples(samples):
        scaled = np.zeros_like(samples)
        for i, pname in enumerate(param_names):
            pdef = PARAM_DEFINITIONS[pname]
            scaled[:, i] = pdef['min'] + samples[:, i] * (pdef['max'] - pdef['min'])
        return scaled
    
    A_scaled = scale_samples(A)
    B_scaled = scale_samples(B)
    
    # Evaluate model at base samples
    def evaluate_samples(samples):
        results = []
        for row in samples:
            params = BatteryParams()
            for i, pname in enumerate(param_names):
                set_param(params, pname, row[i])
            tte = simulate_battery(params)
            results.append(tte)
        return np.array(results)
    
    print("  Evaluating base matrix A...")
    Y_A = evaluate_samples(A_scaled)
    print("  Evaluating base matrix B...")
    Y_B = evaluate_samples(B_scaled)
    
    # Calculate first-order and total-order indices
    S1 = {}
    ST = {}
    
    f0_sq = np.mean(Y_A) ** 2
    var_Y = np.var(np.concatenate([Y_A, Y_B]))
    
    for i, pname in enumerate(param_names):
        print(f"  Analyzing parameter: {pname}")
        
        # Create AB_i matrix (A with column i from B)
        AB_i = A_scaled.copy()
        AB_i[:, i] = B_scaled[:, i]
        Y_AB_i = evaluate_samples(AB_i)
        
        # First-order index: S1_i = V[E[Y|Xi]] / V[Y]
        # Approximation: S1 = (1/N) * sum(Y_B * (Y_AB - Y_A)) / Var(Y)
        S1[pname] = np.mean(Y_B * (Y_AB_i - Y_A)) / var_Y
        
        # Total-order index: ST_i = E[V[Y|X~i]] / V[Y]
        # Approximation: ST = (1/2N) * sum((Y_A - Y_AB)^2) / Var(Y)
        ST[pname] = 0.5 * np.mean((Y_A - Y_AB_i) ** 2) / var_Y
        
        # Clip to valid range
        S1[pname] = np.clip(S1[pname], 0, 1)
        ST[pname] = np.clip(ST[pname], 0, 1)
    
    return {'S1': S1, 'ST': ST, 'param_names': param_names}

def run_morris_screening(n_trajectories=20, n_levels=6):
    """
    Run Morris Elementary Effects screening
    
    Returns:
        dict: mu_star and sigma for each parameter
    """
    print("Running Morris screening analysis...")
    
    param_names = list(PARAM_DEFINITIONS.keys())
    n_params = len(param_names)
    
    delta = 1.0 / (n_levels - 1)
    
    elementary_effects = {pname: [] for pname in param_names}
    
    np.random.seed(123)
    
    for traj in range(n_trajectories):
        # Random starting point
        x = np.random.randint(0, n_levels, n_params) * delta
        
        # Random order of parameter perturbation
        order = np.random.permutation(n_params)
        
        # Evaluate at starting point
        params = BatteryParams()
        for i, pname in enumerate(param_names):
            pdef = PARAM_DEFINITIONS[pname]
            value = pdef['min'] + x[i] * (pdef['max'] - pdef['min'])
            set_param(params, pname, value)
        y_prev = simulate_battery(params)
        
        # Perturb each parameter
        for idx in order:
            pname = param_names[idx]
            pdef = PARAM_DEFINITIONS[pname]
            
            # Perturb
            if x[idx] < 0.5:
                x[idx] += delta
            else:
                x[idx] -= delta
            x[idx] = np.clip(x[idx], 0, 1)
            
            # Evaluate
            params = BatteryParams()
            for i, pn in enumerate(param_names):
                pd = PARAM_DEFINITIONS[pn]
                value = pd['min'] + x[i] * (pd['max'] - pd['min'])
                set_param(params, pn, value)
            y_new = simulate_battery(params)
            
            # Elementary effect
            EE = (y_new - y_prev) / delta
            elementary_effects[pname].append(EE)
            
            y_prev = y_new
    
    # Calculate mu_star and sigma
    mu_star = {}
    sigma = {}
    for pname in param_names:
        ees = np.array(elementary_effects[pname])
        mu_star[pname] = np.mean(np.abs(ees))
        sigma[pname] = np.std(ees)
    
    return {'mu_star': mu_star, 'sigma': sigma, 'param_names': param_names}

def run_oat_analysis(perturbations=[-0.3, -0.1, -0.05, 0.0, 0.05, 0.1, 0.3]):
    """
    Run One-at-a-Time sensitivity analysis
    
    Returns:
        dict: Results for each parameter at each perturbation level
    """
    print("Running One-at-a-Time analysis...")
    
    # Key parameters for OAT
    oat_params = ['B', 'U_cpu', 'T_amb', 'SOH']
    
    # Get baseline
    baseline_params = BatteryParams()
    baseline_tte = simulate_battery(baseline_params)
    
    results = {'perturbations': perturbations, 'baseline': baseline_tte, 'params': {}}
    
    for pname in oat_params:
        print(f"  Analyzing parameter: {pname}")
        pdef = PARAM_DEFINITIONS[pname]
        baseline_value = pdef['baseline']
        
        tte_values = []
        for pert in perturbations:
            params = BatteryParams()
            new_value = baseline_value * (1 + pert)
            new_value = np.clip(new_value, pdef['min'], pdef['max'])
            set_param(params, pname, new_value)
            tte = simulate_battery(params)
            tte_values.append(tte)
        
        # Calculate sensitivity: % change in output / % change in input
        relative_changes = [(tte - baseline_tte) / baseline_tte * 100 for tte in tte_values]
        
        results['params'][pname] = {
            'tte': tte_values,
            'relative_change': relative_changes,
            'name': pdef['name']
        }
    
    return results

def run_scenario_analysis():
    """
    Run scenario matrix analysis for Temperature × Usage × SOH
    
    Returns:
        dict: 3D matrix of time-to-empty for different scenarios
    """
    print("Running scenario analysis...")
    
    # Define scenario levels
    temp_levels = {'Cold': 273.15, 'Normal': 298.15, 'Hot': 313.15}
    usage_levels = {'Light': (0.2, 0.1), 'Medium': (0.5, 0.3), 'Heavy': (0.9, 0.7)}  # (brightness, CPU)
    soh_levels = {'Degraded': 0.7, 'Moderate': 0.85, 'Fresh': 1.0}
    
    results = {}
    
    for temp_name, temp_val in temp_levels.items():
        results[temp_name] = {}
        for usage_name, (brightness, cpu) in usage_levels.items():
            results[temp_name][usage_name] = {}
            for soh_name, soh_val in soh_levels.items():
                params = BatteryParams()
                params.T_amb = temp_val
                params.B = brightness
                params.U_cpu = cpu
                params.SOH = soh_val
                
                tte = simulate_battery(params)
                results[temp_name][usage_name][soh_name] = tte
                print(f"  {temp_name}/{usage_name}/{soh_name}: {tte:.2f}h")
    
    return results

def run_interaction_analysis():
    """
    Calculate second-order interaction effects between key parameters
    
    Returns:
        dict: Interaction matrix
    """
    print("Running interaction analysis...")
    
    key_params = ['B', 'U_cpu', 'T_amb', 'SOH', 'Q_nom']
    n_params = len(key_params)
    
    baseline_params = BatteryParams()
    baseline_tte = simulate_battery(baseline_params)
    
    # Individual effects at +20%
    individual_effects = {}
    for pname in key_params:
        pdef = PARAM_DEFINITIONS[pname]
        params = BatteryParams()
        new_value = pdef['baseline'] * 1.2
        new_value = np.clip(new_value, pdef['min'], pdef['max'])
        set_param(params, pname, new_value)
        tte = simulate_battery(params)
        individual_effects[pname] = (tte - baseline_tte) / baseline_tte * 100
    
    # Interaction effects
    interaction_matrix = np.zeros((n_params, n_params))
    
    for i, pname1 in enumerate(key_params):
        for j, pname2 in enumerate(key_params):
            if i == j:
                interaction_matrix[i, j] = individual_effects[pname1]
            else:
                # Combined effect
                params = BatteryParams()
                pdef1 = PARAM_DEFINITIONS[pname1]
                pdef2 = PARAM_DEFINITIONS[pname2]
                
                new_val1 = np.clip(pdef1['baseline'] * 1.2, pdef1['min'], pdef1['max'])
                new_val2 = np.clip(pdef2['baseline'] * 1.2, pdef2['min'], pdef2['max'])
                
                set_param(params, pname1, new_val1)
                set_param(params, pname2, new_val2)
                
                tte = simulate_battery(params)
                combined_effect = (tte - baseline_tte) / baseline_tte * 100
                
                # Interaction = Combined - Sum of individual
                interaction_matrix[i, j] = combined_effect - individual_effects[pname1] - individual_effects[pname2]
    
    return {'matrix': interaction_matrix, 'params': key_params, 'individual': individual_effects}

# =============================================================================
# Plotting Functions
# =============================================================================

def plot_sobol_indices(sobol_results, save_path='fig_sobol_indices.pdf'):
    """
    Create horizontal bar chart of Sobol indices
    """
    print("Creating Sobol indices bar chart...")
    
    S1 = sobol_results['S1']
    ST = sobol_results['ST']
    param_names = sobol_results['param_names']
    
    # Sort by total-order index
    sorted_params = sorted(param_names, key=lambda x: ST[x], reverse=True)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    y_pos = np.arange(len(sorted_params))
    bar_height = 0.35
    
    # Plot bars
    bars1 = ax.barh(y_pos + bar_height/2, [S1[p] for p in sorted_params], 
                    bar_height, label='First-order ($S_1$)', color=COLORS['primary'], alpha=0.8)
    bars2 = ax.barh(y_pos - bar_height/2, [ST[p] for p in sorted_params], 
                    bar_height, label='Total-order ($S_T$)', color=COLORS['secondary'], alpha=0.8)
    
    # Labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels([PARAM_DEFINITIONS[p]['name'] for p in sorted_params])
    ax.set_xlabel('Sobol Sensitivity Index')
    ax.set_title('Global Sensitivity Analysis: Sobol Indices')
    ax.legend(loc='lower right')
    
    # Add value labels on bars
    for bar, val in zip(bars1, [S1[p] for p in sorted_params]):
        if val > 0.02:
            ax.text(val + 0.01, bar.get_y() + bar.get_height()/2, 
                   f'{val:.3f}', va='center', fontsize=9)
    for bar, val in zip(bars2, [ST[p] for p in sorted_params]):
        if val > 0.02:
            ax.text(val + 0.01, bar.get_y() + bar.get_height()/2, 
                   f'{val:.3f}', va='center', fontsize=9)
    
    ax.set_xlim(0, max(max(ST.values()), max(S1.values())) * 1.25)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, format='pdf')
    plt.savefig(save_path.replace('.pdf', '.png'), format='png', dpi=300)
    plt.close()
    print(f"  Saved: {save_path}")

def plot_oat_sensitivity(oat_results, save_path='fig_oat_sensitivity.pdf'):
    """
    Create 4-panel OAT sensitivity curves
    """
    print("Creating OAT sensitivity curves...")
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()
    
    perturbations = np.array(oat_results['perturbations']) * 100  # Convert to percentage
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['tertiary'], COLORS['quaternary']]
    
    for idx, (pname, data) in enumerate(oat_results['params'].items()):
        ax = axes[idx]
        
        rel_changes = data['relative_change']
        
        ax.plot(perturbations, rel_changes, 'o-', color=colors[idx], 
                linewidth=2, markersize=8, markerfacecolor='white', markeredgewidth=2)
        
        ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
        
        ax.set_xlabel(f'Parameter Perturbation [%]')
        ax.set_ylabel('Change in Battery Life [%]')
        ax.set_title(f'{data["name"]}')
        ax.grid(True, alpha=0.3)
        
        # Add sensitivity coefficient text
        # Calculate local sensitivity at baseline
        if len(rel_changes) >= 5:
            local_sens = (rel_changes[4] - rel_changes[2]) / (perturbations[4] - perturbations[2])
            ax.text(0.95, 0.05, f'Local S = {local_sens:.2f}', 
                   transform=ax.transAxes, ha='right', va='bottom',
                   fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig(save_path, format='pdf')
    plt.savefig(save_path.replace('.pdf', '.png'), format='png', dpi=300)
    plt.close()
    print(f"  Saved: {save_path}")

def plot_scenario_heatmap(scenario_results, save_path='fig_scenario_heatmap.pdf'):
    """
    Create scenario comparison heatmap
    """
    print("Creating scenario heatmap...")
    
    # Create 3x3 matrix for each SOH level
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    
    temp_order = ['Cold', 'Normal', 'Hot']
    usage_order = ['Light', 'Medium', 'Heavy']
    soh_order = ['Fresh', 'Moderate', 'Degraded']
    
    for idx, soh_name in enumerate(soh_order):
        ax = axes[idx]
        
        # Build matrix
        matrix = np.zeros((3, 3))
        for i, temp in enumerate(temp_order):
            for j, usage in enumerate(usage_order):
                matrix[i, j] = scenario_results[temp][usage][soh_name]
        
        # Create heatmap
        sns.heatmap(matrix, ax=ax, annot=True, fmt='.1f', 
                   cmap='RdYlGn_r', center=matrix.mean(),
                   xticklabels=usage_order, yticklabels=temp_order,
                   cbar_kws={'label': 'Battery Life [h]'})
        
        ax.set_xlabel('Usage Pattern')
        ax.set_ylabel('Temperature')
        ax.set_title(f'SOH: {soh_name}\n({soh_order.index(soh_name)*-15+100}%)')
    
    plt.suptitle('Scenario Analysis: Battery Life Under Different Operating Conditions', 
                 fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, format='pdf')
    plt.savefig(save_path.replace('.pdf', '.png'), format='png', dpi=300)
    plt.close()
    print(f"  Saved: {save_path}")

def plot_morris_screening(morris_results, save_path='fig_morris_screening.pdf'):
    """
    Create Morris screening μ* vs σ scatter plot
    """
    print("Creating Morris screening plot...")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    mu_star = morris_results['mu_star']
    sigma = morris_results['sigma']
    param_names = morris_results['param_names']
    
    colors_list = plt.cm.tab10(np.linspace(0, 1, len(param_names)))
    
    for i, pname in enumerate(param_names):
        ax.scatter(mu_star[pname], sigma[pname], 
                  s=150, c=[colors_list[i]], alpha=0.7, edgecolors='black', linewidth=1)
        
        # Add label
        offset = (5, 5)
        ax.annotate(PARAM_DEFINITIONS[pname]['name'], 
                   (mu_star[pname], sigma[pname]),
                   xytext=offset, textcoords='offset points',
                   fontsize=9, ha='left')
    
    # Add reference lines
    max_mu = max(mu_star.values())
    ax.plot([0, max_mu*1.1], [0, max_mu*1.1], 'k--', alpha=0.3, label=r'$\sigma = \mu^*$ (nonlinear/interactive)')
    ax.plot([0, max_mu*1.1], [0, max_mu*0.55], 'k:', alpha=0.3, label=r'$\sigma = 0.5\mu^*$ (weakly nonlinear)')
    
    # Add regions
    ax.axhline(y=np.median(list(sigma.values())), color='gray', linestyle=':', alpha=0.3)
    ax.axvline(x=np.median(list(mu_star.values())), color='gray', linestyle=':', alpha=0.3)
    
    ax.set_xlabel(r'$\mu^*$ (Mean of Absolute Elementary Effects)')
    ax.set_ylabel(r'$\sigma$ (Standard Deviation of Elementary Effects)')
    ax.set_title('Morris Screening: Parameter Importance and Nonlinearity')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)
    
    # Set axis limits
    ax.set_xlim(0, max_mu * 1.15)
    ax.set_ylim(0, max(sigma.values()) * 1.15)
    
    plt.tight_layout()
    plt.savefig(save_path, format='pdf')
    plt.savefig(save_path.replace('.pdf', '.png'), format='png', dpi=300)
    plt.close()
    print(f"  Saved: {save_path}")

def plot_interaction_heatmap(interaction_results, save_path='fig_interaction_effects.pdf'):
    """
    Create interaction effects heatmap
    """
    print("Creating interaction effects heatmap...")
    
    fig, ax = plt.subplots(figsize=(8, 7))
    
    matrix = interaction_results['matrix']
    params = interaction_results['params']
    param_labels = [PARAM_DEFINITIONS[p]['name'] for p in params]
    
    # Create heatmap
    mask = np.eye(len(params), dtype=bool)
    sns.heatmap(matrix, ax=ax, annot=True, fmt='.1f',
               cmap='coolwarm', center=0,
               xticklabels=param_labels, yticklabels=param_labels,
               mask=mask, cbar_kws={'label': 'Interaction Effect [%]'},
               linewidths=0.5)
    
    # Add diagonal values separately (individual effects)
    for i in range(len(params)):
        ax.text(i + 0.5, i + 0.5, f'{matrix[i, i]:.1f}*', 
               ha='center', va='center', fontsize=10, fontweight='bold')
    
    ax.set_title('Parameter Interaction Effects\n(Diagonal: Individual Effects*, Off-diagonal: Synergy/Antagonism)')
    
    plt.tight_layout()
    plt.savefig(save_path, format='pdf')
    plt.savefig(save_path.replace('.pdf', '.png'), format='png', dpi=300)
    plt.close()
    print(f"  Saved: {save_path}")

def plot_spider_chart(oat_results, save_path='fig_spider_sensitivity.pdf'):
    """
    Create spider/radar chart for parameter sensitivity comparison
    """
    print("Creating spider/radar chart...")
    
    params_data = oat_results['params']
    param_names = list(params_data.keys())
    n_params = len(param_names)
    
    # Get sensitivity at ±30%
    sensitivities_neg = []
    sensitivities_pos = []
    
    for pname in param_names:
        rel_changes = params_data[pname]['relative_change']
        sensitivities_neg.append(abs(rel_changes[0]))  # -30%
        sensitivities_pos.append(abs(rel_changes[-1]))  # +30%
    
    # Create radar chart
    angles = np.linspace(0, 2 * np.pi, n_params, endpoint=False).tolist()
    
    # Close the polygon
    sensitivities_neg += sensitivities_neg[:1]
    sensitivities_pos += sensitivities_pos[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    ax.plot(angles, sensitivities_neg, 'o-', linewidth=2, label='-30% perturbation', color=COLORS['primary'])
    ax.fill(angles, sensitivities_neg, alpha=0.25, color=COLORS['primary'])
    
    ax.plot(angles, sensitivities_pos, 's-', linewidth=2, label='+30% perturbation', color=COLORS['secondary'])
    ax.fill(angles, sensitivities_pos, alpha=0.25, color=COLORS['secondary'])
    
    # Set labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([params_data[p]['name'] for p in param_names])
    
    ax.set_ylabel('|Change in Battery Life| [%]')
    ax.set_title('Parameter Sensitivity Comparison\n(Absolute Impact at ±30% Perturbation)', y=1.08)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
    
    plt.tight_layout()
    plt.savefig(save_path, format='pdf')
    plt.savefig(save_path.replace('.pdf', '.png'), format='png', dpi=300)
    plt.close()
    print(f"  Saved: {save_path}")

def generate_summary_table(sobol_results, morris_results, oat_results, scenario_results):
    """
    Generate summary statistics and save as text for LaTeX table
    """
    print("\n" + "="*60)
    print("SENSITIVITY ANALYSIS SUMMARY")
    print("="*60)
    
    # Baseline
    baseline_params = BatteryParams()
    baseline_tte = simulate_battery(baseline_params)
    print(f"\nBaseline Battery Life: {baseline_tte:.2f} hours")
    
    # Sobol ranking
    print("\n--- Sobol Sensitivity Ranking (by Total-order) ---")
    ST = sobol_results['ST']
    S1 = sobol_results['S1']
    sorted_params = sorted(ST.keys(), key=lambda x: ST[x], reverse=True)
    
    print(f"{'Rank':<5}{'Parameter':<20}{'S1':>10}{'ST':>10}{'Classification':<15}")
    print("-"*60)
    for i, pname in enumerate(sorted_params):
        if ST[pname] > 0.1:
            classification = "HIGH"
        elif ST[pname] > 0.03:
            classification = "MEDIUM"
        else:
            classification = "LOW"
        print(f"{i+1:<5}{PARAM_DEFINITIONS[pname]['name']:<20}{S1[pname]:>10.4f}{ST[pname]:>10.4f}{classification:<15}")
    
    # Scenario summary
    print("\n--- Scenario Analysis Summary ---")
    best_case = scenario_results['Normal']['Light']['Fresh']
    worst_case = scenario_results['Hot']['Heavy']['Degraded']
    base_case = scenario_results['Normal']['Medium']['Fresh']
    
    print(f"Best Case (Normal/Light/Fresh):   {best_case:.2f} hours (+{(best_case-baseline_tte)/baseline_tte*100:.1f}%)")
    print(f"Base Case (Normal/Medium/Fresh):  {base_case:.2f} hours (baseline)")
    print(f"Worst Case (Hot/Heavy/Degraded):  {worst_case:.2f} hours ({(worst_case-baseline_tte)/baseline_tte*100:.1f}%)")
    
    print("\n--- Key Findings ---")
    print(f"1. Battery life ranges from {worst_case:.1f}h (worst) to {best_case:.1f}h (best)")
    print(f"2. Ratio of best/worst scenarios: {best_case/worst_case:.1f}x")
    print(f"3. Most influential parameters: {', '.join([PARAM_DEFINITIONS[p]['name'] for p in sorted_params[:3]])}")
    print(f"4. Least influential parameters: {', '.join([PARAM_DEFINITIONS[p]['name'] for p in sorted_params[-2:]])}")
    
    # Save as CSV for LaTeX
    with open('sensitivity_summary.csv', 'w') as f:
        f.write("Parameter,S1,ST,mu_star,sigma,Classification\n")
        for pname in sorted_params:
            mu = morris_results['mu_star'][pname]
            sig = morris_results['sigma'][pname]
            if ST[pname] > 0.1:
                cls = "High"
            elif ST[pname] > 0.03:
                cls = "Medium"
            else:
                cls = "Low"
            f.write(f"{PARAM_DEFINITIONS[pname]['name']},{S1[pname]:.4f},{ST[pname]:.4f},{mu:.4f},{sig:.4f},{cls}\n")
    
    print("\n  Summary saved to: sensitivity_summary.csv")
    
    return {
        'baseline': baseline_tte,
        'best': best_case,
        'worst': worst_case,
        'ranking': sorted_params
    }

# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    print("="*60)
    print("MCM 2026 Problem A - Sensitivity Analysis")
    print("="*60)
    
    # Run all analyses
    print("\n[1/5] Running Sobol Sensitivity Analysis...")
    sobol_results = run_sobol_analysis(n_samples=128)
    
    print("\n[2/5] Running Morris Screening...")
    morris_results = run_morris_screening(n_trajectories=15)
    
    print("\n[3/5] Running One-at-a-Time Analysis...")
    oat_results = run_oat_analysis()
    
    print("\n[4/5] Running Scenario Analysis...")
    scenario_results = run_scenario_analysis()
    
    print("\n[5/5] Running Interaction Analysis...")
    interaction_results = run_interaction_analysis()
    
    # Generate all figures
    print("\n" + "="*60)
    print("Generating Publication-Quality Figures")
    print("="*60)
    
    plot_sobol_indices(sobol_results)
    plot_oat_sensitivity(oat_results)
    plot_scenario_heatmap(scenario_results)
    plot_morris_screening(morris_results)
    plot_interaction_heatmap(interaction_results)
    plot_spider_chart(oat_results)
    
    # Generate summary
    summary = generate_summary_table(sobol_results, morris_results, oat_results, scenario_results)
    
    print("\n" + "="*60)
    print("ALL ANALYSES COMPLETE")
    print("="*60)
    print("\nGenerated files:")
    print("  - fig_sobol_indices.pdf/png")
    print("  - fig_oat_sensitivity.pdf/png")
    print("  - fig_scenario_heatmap.pdf/png")
    print("  - fig_morris_screening.pdf/png")
    print("  - fig_interaction_effects.pdf/png")
    print("  - fig_spider_sensitivity.pdf/png")
    print("  - sensitivity_summary.csv")
