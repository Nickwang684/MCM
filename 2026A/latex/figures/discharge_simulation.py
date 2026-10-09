#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCM 2026 Problem A - Battery Discharge Simulation Figures
基于不同初始状态和影响因素下的实验仿真与模型验证、不确定度量化

图1: 耗尽时间 vs 电池功耗 (不同初始电量)
图2: 耗尽时间 vs 环境温度 (不同初始电量)  
图3: 3D图 - 耗尽时间 vs 环境温度 vs 电池功耗

Author: MCM Team
Date: 2026
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp
import warnings
warnings.filterwarnings('ignore')
import gc

# Set publication-quality figure parameters
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.size'] = 11
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 13
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10
rcParams['legend.fontsize'] = 9
rcParams['figure.dpi'] = 150
rcParams['savefig.dpi'] = 150
rcParams['savefig.bbox'] = 'tight'
rcParams['axes.linewidth'] = 0.8
rcParams['grid.linewidth'] = 0.5

# Color palette for different initial SOC levels
COLORS = ['#2E86AB', '#A23B72', '#F18F01', '#4B8F8C', '#E94F37', '#7D8491', '#1B4965', '#5FA8D3']

# =============================================================================
# Battery Model Parameters
# =============================================================================
class BatteryParams:
    """Battery model parameters"""
    Q_nom = 3.0         # Nominal capacity [Ah]
    V_nom = 3.7         # Nominal voltage [V]
    R0 = 0.050          # Internal resistance [Ohm]
    R1 = 0.030          # RC pair 1 resistance [Ohm]
    R2 = 0.020          # RC pair 2 resistance [Ohm]
    C1 = 1000.0         # RC pair 1 capacitance [F]
    C2 = 25000.0        # RC pair 2 capacitance [F]
    
    # OCV Shepherd model
    E0 = 3.685
    K1 = 0.2156
    K2 = 0.0351
    K3 = -0.0175
    
    # Thermal parameters
    T_amb = 298.15      # Ambient temperature [K] = 25°C
    C_th = 100.0        # Thermal capacitance [J/K]
    R_th = 5.0          # Thermal resistance [K/W]
    
    SOH = 1.0           # State of Health
    
    # Power consumption (baseline)
    P_base = 0.150      # Base power [W]
    B = 0.5             # Screen brightness [0-1]
    U_cpu = 0.3         # CPU utilization [0-1]

def calculate_ocv(soc: float) -> float:
    """Calculate Open Circuit Voltage using Shepherd model"""
    soc = np.clip(soc, 0.001, 0.999)
    return BatteryParams.E0 + BatteryParams.K1 * soc + \
           BatteryParams.K2 * np.log(soc) + BatteryParams.K3 * np.log(1 - soc)

def calculate_power(brightness: float = 0.5, cpu_util: float = 0.3, T: float = 298.15) -> float:
    """
    Calculate total power consumption [W]
    
    Args:
        brightness: Screen brightness [0-1]
        cpu_util: CPU utilization [0-1]
        T: Battery temperature [K]
    """
    P_display = 0.050 + 0.800 * (brightness ** 1.8)
    P_cpu = 0.100 + 2.5 * (cpu_util ** 1.5)
    P_base = 0.150
    
    # Temperature correction factor (higher temp = slightly more efficient)
    T_factor = 1.0 + 0.002 * (298.15 - T)
    
    return (P_display + P_cpu + P_base) * T_factor

def simulate_discharge(soc_init: float, T_amb: float, power: float, 
                       soc_cutoff: float = 0.10) -> tuple:
    """
    Simulate battery discharge
    
    Args:
        soc_init: Initial state of charge [0-1]
        T_amb: Ambient temperature [K]
        power: Power consumption [W]
        soc_cutoff: SOC cutoff threshold
        
    Returns:
        (time_to_empty [hours], time_array, soc_array, power_array)
    """
    Q_eff = BatteryParams.Q_nom * BatteryParams.SOH * 3600  # [As]
    V_nom = BatteryParams.V_nom
    
    def battery_ode(t, y):
        soc, V_rc1, V_rc2, T = y
        
        if soc < soc_cutoff:
            return [0, 0, 0, 0]
        
        # Current from power
        V_oc = calculate_ocv(soc)
        V_terminal = V_oc - V_rc1 - V_rc2 - BatteryParams.R0 * (power / V_nom)
        I = power / max(V_terminal, 2.5)
        
        # State derivatives
        dSOC = -I / Q_eff
        dV_rc1 = (I * BatteryParams.R1 - V_rc1) / (BatteryParams.R1 * BatteryParams.C1)
        dV_rc2 = (I * BatteryParams.R2 - V_rc2) / (BatteryParams.R2 * BatteryParams.C2)
        
        # Thermal dynamics
        P_loss = I**2 * (BatteryParams.R0 + BatteryParams.R1 + BatteryParams.R2)
        dT = (P_loss - (T - T_amb) / BatteryParams.R_th) / BatteryParams.C_th
        
        return [dSOC, dV_rc1, dV_rc2, dT]
    
    # Initial conditions
    y0 = [soc_init, 0, 0, T_amb]
    
    # Time span (max 30 hours in seconds)
    t_span = (0, 30 * 3600)
    t_eval = np.linspace(0, 30 * 3600, 300)
    
    # Solve ODE
    sol = solve_ivp(battery_ode, t_span, y0, t_eval=t_eval, method='RK45')
    
    # Find time to empty
    soc_array = sol.y[0]
    time_array = sol.t / 3600  # Convert to hours
    
    # Find when SOC drops below cutoff
    idx = np.where(soc_array <= soc_cutoff)[0]
    if len(idx) > 0:
        t_empty = time_array[idx[0]]
    else:
        t_empty = time_array[-1]
    
    return t_empty, time_array, soc_array, np.full_like(time_array, power)


def generate_figure1():
    """
    图1: 耗尽时间 vs 电池功耗 (不同初始电量)
    横坐标: 耗尽时间 t [hours]
    纵坐标: 电池功耗 P [W]
    多条曲线: 不同初始SOC (20%, 40%, 60%, 80%, 100%)
    """
    print("Generating Figure 1: Discharge Time vs Power Consumption...")
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Initial SOC levels (step of 20%)
    soc_levels = [1.0, 0.8, 0.6, 0.4, 0.2]
    
    # Power consumption range
    power_range = np.linspace(0.5, 4.0, 20)  # 0.5W to 4.0W
    
    for i, soc_init in enumerate(soc_levels):
        t_empty_list = []
        
        for power in power_range:
            t_empty, _, _, _ = simulate_discharge(soc_init, 298.15, power)
            t_empty_list.append(t_empty)
        
        label = f'SOC$_0$ = {int(soc_init*100)}%'
        ax.plot(t_empty_list, power_range, color=COLORS[i], linewidth=2, 
                label=label, marker='o', markersize=3, markevery=5)
    
    ax.set_xlabel('Time to Empty, $t_{empty}$ [hours]')
    ax.set_ylabel('Power Consumption, $P$ [W]')
    ax.set_title('Battery Life vs Power Consumption at Different Initial SOC')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, None)
    ax.set_ylim(0.5, 4.0)
    
    # Add annotation
    ax.annotate('Light usage\n(browsing)', xy=(15, 0.8), fontsize=9, 
                ha='center', color='gray')
    ax.annotate('Heavy usage\n(gaming)', xy=(2, 3.5), fontsize=9, 
                ha='center', color='gray')
    
    plt.tight_layout()
    plt.savefig('fig1_discharge_power.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig1_discharge_power.pdf', bbox_inches='tight')
    plt.close()
    gc.collect()
    print("  -> Saved: fig1_discharge_power.png/pdf")


def generate_figure2():
    """
    图2: 耗尽时间 vs 环境温度 (不同初始电量)
    横坐标: 耗尽时间 t [hours]
    纵坐标: 环境温度 T [°C]
    多条曲线: 不同初始SOC (20%, 40%, 60%, 80%, 100%)
    """
    print("Generating Figure 2: Discharge Time vs Ambient Temperature...")
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Initial SOC levels
    soc_levels = [1.0, 0.8, 0.6, 0.4, 0.2]
    
    # Temperature range: -10°C to 45°C
    temp_range_C = np.linspace(-10, 45, 20)
    temp_range_K = temp_range_C + 273.15
    
    # Fixed power consumption (medium usage)
    power = 1.5  # W
    
    for i, soc_init in enumerate(soc_levels):
        t_empty_list = []
        
        for T_amb in temp_range_K:
            # Temperature affects power slightly
            power_eff = power * (1.0 + 0.003 * (298.15 - T_amb))
            t_empty, _, _, _ = simulate_discharge(soc_init, T_amb, power_eff)
            t_empty_list.append(t_empty)
        
        label = f'SOC$_0$ = {int(soc_init*100)}%'
        ax.plot(t_empty_list, temp_range_C, color=COLORS[i], linewidth=2, 
                label=label, marker='s', markersize=3, markevery=4)
    
    ax.set_xlabel('Time to Empty, $t_{empty}$ [hours]')
    ax.set_ylabel('Ambient Temperature, $T_{amb}$ [°C]')
    ax.set_title('Battery Life vs Ambient Temperature at Different Initial SOC')
    ax.legend(loc='upper right', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, None)
    
    # Add horizontal lines for reference temperatures
    ax.axhline(y=0, color='lightblue', linestyle='--', alpha=0.5, linewidth=1)
    ax.axhline(y=25, color='green', linestyle='--', alpha=0.5, linewidth=1)
    ax.axhline(y=40, color='orange', linestyle='--', alpha=0.5, linewidth=1)
    
    ax.text(0.5, 2, 'Freezing', fontsize=8, color='lightblue')
    ax.text(0.5, 27, 'Room temp', fontsize=8, color='green')
    ax.text(0.5, 42, 'Hot environment', fontsize=8, color='orange')
    
    plt.tight_layout()
    plt.savefig('fig2_discharge_temperature.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig2_discharge_temperature.pdf', bbox_inches='tight')
    plt.close()
    gc.collect()
    print("  -> Saved: fig2_discharge_temperature.png/pdf")


def generate_figure3():
    """
    图3: 3D图 - 耗尽时间 vs 环境温度 vs 电池功耗
    X轴: 耗尽时间 t [hours]
    Y轴: 环境温度 T [°C]
    Z轴: 电池功耗 P [W]
    特定初始电量 (100% SOC)
    """
    print("Generating Figure 3: 3D Surface - Time vs Temperature vs Power...")
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Fixed initial SOC
    soc_init = 1.0
    
    # Create mesh grid
    temp_range_C = np.linspace(-10, 45, 15)
    temp_range_K = temp_range_C + 273.15
    power_range = np.linspace(0.5, 4.0, 15)
    
    T_mesh, P_mesh = np.meshgrid(temp_range_C, power_range)
    T_mesh_K, _ = np.meshgrid(temp_range_K, power_range)
    t_empty_mesh = np.zeros_like(T_mesh)
    
    # Calculate time to empty for each (T, P) combination
    for i in range(len(power_range)):
        for j in range(len(temp_range_C)):
            T_amb = temp_range_K[j]
            power = power_range[i]
            power_eff = power * (1.0 + 0.003 * (298.15 - T_amb))
            t_empty, _, _, _ = simulate_discharge(soc_init, T_amb, power_eff)
            t_empty_mesh[i, j] = t_empty
    
    # Create surface plot
    surf = ax.plot_surface(t_empty_mesh, T_mesh, P_mesh, 
                           cmap='viridis', alpha=0.8,
                           linewidth=0.2, edgecolor='gray',
                           antialiased=True)
    
    # Add contour projections
    ax.contour(t_empty_mesh, T_mesh, P_mesh, zdir='z', offset=0.5, 
               cmap='viridis', alpha=0.5, levels=10)
    ax.contour(t_empty_mesh, T_mesh, P_mesh, zdir='y', offset=45, 
               cmap='viridis', alpha=0.3, levels=10)
    
    ax.set_xlabel('\nTime to Empty, $t_{empty}$ [hours]', labelpad=10)
    ax.set_ylabel('\nAmbient Temperature, $T$ [°C]', labelpad=10)
    ax.set_zlabel('\nPower Consumption, $P$ [W]', labelpad=10)
    ax.set_title('3D Battery Discharge Simulation (SOC$_0$ = 100%)', pad=20)
    
    # Add colorbar
    cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.1)
    cbar.set_label('Time to Empty [hours]', rotation=270, labelpad=15)
    
    # Set viewing angle
    ax.view_init(elev=25, azim=135)
    
    plt.tight_layout()
    plt.savefig('fig3_3d_discharge.png', dpi=150, bbox_inches='tight')
    plt.savefig('fig3_3d_discharge.pdf', bbox_inches='tight')
    plt.close()
    gc.collect()
    print("  -> Saved: fig3_3d_discharge.png/pdf")


def main():
    """Generate all three figures"""
    print("=" * 60)
    print("Battery Discharge Simulation - Figure Generation")
    print("基于不同初始状态和影响因素下的实验仿真与模型验证")
    print("=" * 60)
    
    generate_figure1()
    generate_figure2()
    generate_figure3()
    
    print("=" * 60)
    print("All figures generated successfully!")
    print("Output files:")
    print("  - fig1_discharge_power.png/pdf")
    print("  - fig2_discharge_temperature.png/pdf")
    print("  - fig3_3d_discharge.png/pdf")
    print("=" * 60)


if __name__ == "__main__":
    main()
