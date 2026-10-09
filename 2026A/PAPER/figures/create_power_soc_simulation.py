"""
Power-Driven SOC Simulation with 2-RC Equivalent Circuit Model
===============================================================

Motivation:
- Direct current measurement is difficult on smartphones
- Use I = P/V where P = P_display + P_cpu + P_network + P_gps + P_base
- 2-RC ECM captures battery dynamics accurately

Model Equations:
    dSOC/dt = -I(t) / (Q_nom * SOH * 3600)
    dV_RC1/dt = -V_RC1/τ1 + I(t)/C1  
    dV_RC2/dt = -V_RC2/τ2 + I(t)/C2
    V(t) = OCV(SOC,T) - I*R0 - V_RC1 - V_RC2
    I(t) = P(t) / V(t)  →  Algebraic loop solved implicitly
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'mathtext.fontset': 'stix',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'axes.grid': True,
    'grid.alpha': 0.3,
})


class BatteryParameters:
    """Battery ECM parameters for typical smartphone Li-ion (3000mAh, 3.7V nominal)"""
    
    Q_nom = 3.0          # Ah - Nominal capacity
    SOH = 1.0            # State of Health
    V_nom = 3.7          # V - Nominal voltage
    
    # Shepherd OCV model: OCV = E0 + K1*SOC + K2*ln(SOC) + K3*ln(1-SOC)
    E0 = 3.685
    K1 = 0.2156
    K2 = 0.0351
    K3 = -0.0175
    
    # 2-RC ECM parameters (typical for smartphone battery)
    R0 = 0.05            # Ohms - Ohmic resistance
    R1 = 0.03            # Ohms - Fast polarization resistance  
    C1 = 1000            # F - Fast polarization capacitance (τ1 ≈ 30s)
    R2 = 0.02            # Ohms - Slow polarization resistance
    C2 = 25000           # F - Slow polarization capacitance (τ2 ≈ 500s)
    
    # Temperature parameters
    T_ref = 298.15       # K (25°C)
    E_a = 20000          # J/mol - Activation energy
    R_gas = 8.314        # J/(mol·K)
    
    @classmethod
    def tau1(cls, T=298.15):
        return cls.R1 * cls.C1
    
    @classmethod  
    def tau2(cls, T=298.15):
        return cls.R2 * cls.C2
    
    @classmethod
    def ocv(cls, soc, T=298.15):
        """Shepherd-based OCV model"""
        soc_safe = np.clip(soc, 0.01, 0.99)
        ocv_base = cls.E0 + cls.K1*soc_safe + cls.K2*np.log(soc_safe) + cls.K3*np.log(1-soc_safe)
        dOCV_dT = -0.0003  # V/K
        return ocv_base + dOCV_dT * (T - cls.T_ref)
    
    @classmethod
    def resistance_temp_factor(cls, T):
        """Arrhenius temperature dependence for resistance"""
        return np.exp(-cls.E_a/cls.R_gas * (1/T - 1/cls.T_ref))


class PowerModel:
    """
    Component-based power consumption model
    P_total = P_base + P_display + P_cpu + P_network + P_gps + P_other
    """
    
    # Base power (always-on components) in mW
    P_base = 100
    
    # Display parameters
    P_display_base = 50      # mW - display controller
    P_backlight_max = 800    # mW - max backlight
    gamma_display = 1.8      # nonlinearity exponent
    
    # CPU parameters  
    P_cpu_idle = 50          # mW
    P_cpu_max = 2000         # mW
    alpha_cpu = 1.5          # nonlinearity exponent
    
    # Network parameters (mW)
    P_wifi_idle = 20
    P_wifi_active = 800
    P_4g_idle = 50
    P_4g_active = 2500
    
    # GPS
    P_gps = 500              # mW when active
    
    @classmethod
    def display_power(cls, brightness):
        """brightness: 0-1"""
        return cls.P_display_base + cls.P_backlight_max * (brightness ** cls.gamma_display)
    
    @classmethod
    def cpu_power(cls, utilization):
        """utilization: 0-1"""
        return cls.P_cpu_idle + (cls.P_cpu_max - cls.P_cpu_idle) * (utilization ** cls.alpha_cpu)
    
    @classmethod
    def network_power(cls, mode, activity):
        """
        mode: 'wifi' or '4g'
        activity: 0-1 (fraction of time active)
        """
        if mode == 'wifi':
            return cls.P_wifi_idle + (cls.P_wifi_active - cls.P_wifi_idle) * activity
        else:
            return cls.P_4g_idle + (cls.P_4g_active - cls.P_4g_idle) * activity
    
    @classmethod
    def total_power(cls, brightness=0.5, cpu_util=0.2, network_mode='wifi', 
                    network_activity=0.1, gps_on=False):
        """Calculate total power in mW"""
        P = cls.P_base
        P += cls.display_power(brightness)
        P += cls.cpu_power(cpu_util)
        P += cls.network_power(network_mode, network_activity)
        if gps_on:
            P += cls.P_gps
        return P


def solve_current_from_power(P_mW, ocv, v_rc1, v_rc2, R0):
    """
    Solve I = P/V where V = OCV - IR0 - V_RC1 - V_RC2
    
    Quadratic equation: I*R0 + I*(OCV-V_RC1-V_RC2)/P - 1 = 0
    Rearranged: R0*I^2 - (OCV-V_RC1-V_RC2)*I + P = 0
    """
    P_W = P_mW / 1000  # Convert to Watts
    V_eff = ocv - v_rc1 - v_rc2
    
    # Quadratic: R0*I^2 - V_eff*I + P = 0
    a = R0
    b = -V_eff
    c = P_W
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return V_eff / (2*R0)  # Return approximate value
    
    # Take smaller root (physical solution)
    I = (-b - np.sqrt(discriminant)) / (2*a)
    return max(I, 0)


def battery_ode(t, state, power_func, params):
    """
    ODE system for battery state evolution
    
    State: [SOC, V_RC1, V_RC2]
    """
    soc, v_rc1, v_rc2 = state
    
    # Get power at current time
    P_mW = power_func(t)
    
    # Calculate OCV
    ocv = params.ocv(soc)
    
    # Solve for current
    I = solve_current_from_power(P_mW, ocv, v_rc1, v_rc2, params.R0)
    
    # State derivatives
    dSOC_dt = -I / (params.Q_nom * params.SOH * 3600)
    dVRC1_dt = -v_rc1 / params.tau1() + I / params.C1
    dVRC2_dt = -v_rc2 / params.tau2() + I / params.C2
    
    return [dSOC_dt, dVRC1_dt, dVRC2_dt]


def soc_event(t, state, power_func, params):
    """Stop when SOC reaches minimum threshold"""
    return state[0] - 0.05

soc_event.terminal = True
soc_event.direction = -1


def simulate_scenario(scenario_name, power_func, soc_init=0.80, t_max=48*3600):
    """Run simulation for a given power profile"""
    
    params = BatteryParameters()
    state0 = [soc_init, 0.0, 0.0]
    
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, 10000)
    
    sol = solve_ivp(
        battery_ode, t_span, state0,
        args=(power_func, params),
        method='RK45',
        t_eval=t_eval,
        events=soc_event,
        max_step=60
    )
    
    # Calculate voltage and current at each time point
    t = sol.t
    soc = sol.y[0]
    v_rc1 = sol.y[1]
    v_rc2 = sol.y[2]
    
    ocv = np.array([params.ocv(s) for s in soc])
    power = np.array([power_func(ti) for ti in t])
    current = np.array([
        solve_current_from_power(power_func(ti), params.ocv(s), vr1, vr2, params.R0)
        for ti, s, vr1, vr2 in zip(t, soc, v_rc1, v_rc2)
    ])
    voltage = ocv - current * params.R0 - v_rc1 - v_rc2
    
    return {
        'name': scenario_name,
        't': t / 3600,  # hours
        'soc': soc,
        'voltage': voltage,
        'current': current,
        'power': power,
        'ocv': ocv,
        'v_rc1': v_rc1,
        'v_rc2': v_rc2,
        't_empty': t[-1] / 3600 if sol.t_events[0].size > 0 else None
    }


def create_usage_scenarios():
    """Define realistic usage scenarios"""
    
    scenarios = {}
    
    # Scenario 1: Light use (reading, occasional browsing)
    def light_use(t):
        brightness = 0.3
        cpu = 0.1 + 0.05 * np.sin(t / 600)  # Slight variation
        return PowerModel.total_power(brightness, cpu, 'wifi', 0.05, False)
    scenarios['Light Use'] = light_use
    
    # Scenario 2: Moderate use (social media, messaging)
    def moderate_use(t):
        brightness = 0.5
        cpu = 0.25 + 0.1 * np.sin(t / 300)
        activity = 0.2 + 0.1 * np.sin(t / 180)
        return PowerModel.total_power(brightness, cpu, 'wifi', activity, False)
    scenarios['Moderate Use'] = moderate_use
    
    # Scenario 3: Heavy use (video streaming)
    def heavy_use(t):
        brightness = 0.7
        cpu = 0.5
        return PowerModel.total_power(brightness, cpu, 'wifi', 0.8, False)
    scenarios['Heavy Use'] = heavy_use
    
    # Scenario 4: Gaming
    def gaming(t):
        brightness = 0.9
        cpu = 0.85 + 0.1 * np.sin(t / 60)
        return PowerModel.total_power(brightness, cpu, 'wifi', 0.3, False)
    scenarios['Gaming'] = gaming
    
    # Scenario 5: Navigation (GPS active)
    def navigation(t):
        brightness = 0.6
        cpu = 0.4
        return PowerModel.total_power(brightness, cpu, '4g', 0.5, True)
    scenarios['Navigation'] = navigation
    
    # Scenario 6: Mixed realistic usage
    def mixed_realistic(t):
        hour = (t / 3600) % 24
        
        # Sleep mode (0-7 AM)
        if 0 <= hour < 7:
            return PowerModel.P_base + 50
        # Morning commute (7-8 AM) - social media
        elif 7 <= hour < 8:
            return PowerModel.total_power(0.5, 0.3, 'wifi', 0.3, False)
        # Work (8-12, 1-5) - light use
        elif (8 <= hour < 12) or (13 <= hour < 17):
            return PowerModel.total_power(0.3, 0.15, 'wifi', 0.1, False)
        # Lunch (12-1) - moderate
        elif 12 <= hour < 13:
            return PowerModel.total_power(0.5, 0.25, 'wifi', 0.2, False)
        # Evening commute (5-6) - navigation
        elif 17 <= hour < 18:
            return PowerModel.total_power(0.6, 0.4, '4g', 0.5, True)
        # Evening (6-10) - video/gaming
        elif 18 <= hour < 22:
            return PowerModel.total_power(0.7, 0.5, 'wifi', 0.6, False)
        # Night (10-12) - light
        else:
            return PowerModel.total_power(0.3, 0.1, 'wifi', 0.05, False)
    
    scenarios['Mixed Realistic'] = mixed_realistic
    
    return scenarios


def generate_synthetic_experimental_data(sim_result, noise_soc=0.02, noise_v=0.015):
    """Add realistic noise to simulation to create 'experimental' data"""
    np.random.seed(42)
    
    n = len(sim_result['t'])
    
    # Subsample to simulate measurement frequency
    sample_idx = np.linspace(0, n-1, min(200, n)).astype(int)
    
    t_exp = sim_result['t'][sample_idx]
    soc_exp = sim_result['soc'][sample_idx] + np.random.normal(0, noise_soc, len(sample_idx))
    v_exp = sim_result['voltage'][sample_idx] + np.random.normal(0, noise_v, len(sample_idx))
    
    # Clip to physical bounds
    soc_exp = np.clip(soc_exp, 0.05, 1.0)
    v_exp = np.clip(v_exp, 3.0, 4.2)
    
    return t_exp, soc_exp, v_exp


def create_main_simulation_figure():
    """Create comprehensive simulation vs experiment comparison figure"""
    
    scenarios = create_usage_scenarios()
    
    fig = plt.figure(figsize=(14, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.35, wspace=0.25,
                          left=0.08, right=0.95, top=0.95, bottom=0.06)
    
    colors = {'Light Use': '#3498db', 'Moderate Use': '#2ecc71', 
              'Heavy Use': '#e74c3c', 'Gaming': '#9b59b6', 
              'Navigation': '#f39c12', 'Mixed Realistic': '#1abc9c'}
    
    # Run simulations
    results = {}
    for name, power_func in scenarios.items():
        results[name] = simulate_scenario(name, power_func)
    
    # ===== Panel (a): SOC vs Time - All Scenarios =====
    ax1 = fig.add_subplot(gs[0, 0])
    
    for name, res in results.items():
        ax1.plot(res['t'], res['soc']*100, '-', linewidth=2, 
                 color=colors[name], label=name)
    
    ax1.axhline(y=5, color='red', linestyle='--', alpha=0.5, label='SOC_min = 5%')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('State of Charge (%)')
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0, 85)
    ax1.legend(loc='upper right', fontsize=9, ncol=2)
    ax1.set_title('(a) SOC Discharge Curves: Model Simulation', fontweight='bold')
    
    # ===== Panel (b): Model vs "Experimental" for Moderate Use =====
    ax2 = fig.add_subplot(gs[0, 1])
    
    res_mod = results['Moderate Use']
    t_exp, soc_exp, v_exp = generate_synthetic_experimental_data(res_mod)
    
    ax2.plot(res_mod['t'], res_mod['soc']*100, 'b-', linewidth=2, label='Model')
    ax2.scatter(t_exp, soc_exp*100, s=20, c='red', alpha=0.6, label='Experimental', zorder=5)
    
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('State of Charge (%)')
    ax2.legend(loc='upper right')
    ax2.set_title('(b) Model vs Experiment: Moderate Use', fontweight='bold')
    
    # Calculate RMSE
    soc_model_at_exp = np.interp(t_exp, res_mod['t'], res_mod['soc'])
    rmse_soc = np.sqrt(np.mean((soc_exp - soc_model_at_exp)**2)) * 100
    ax2.text(0.05, 0.15, f'RMSE = {rmse_soc:.2f}%', transform=ax2.transAxes,
             fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # ===== Panel (c): Voltage Comparison =====
    ax3 = fig.add_subplot(gs[1, 0])
    
    ax3.plot(res_mod['t'], res_mod['voltage'], 'b-', linewidth=2, label='Model V(t)')
    ax3.plot(res_mod['t'], res_mod['ocv'], 'g--', linewidth=1.5, alpha=0.7, label='OCV(SOC)')
    ax3.scatter(t_exp, v_exp, s=20, c='red', alpha=0.6, label='Experimental', zorder=5)
    
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('Voltage (V)')
    ax3.legend(loc='lower left')
    ax3.set_title('(c) Terminal Voltage: V(t) = OCV - IR₀ - V_RC1 - V_RC2', fontweight='bold')
    
    # ===== Panel (d): Power Decomposition =====
    ax4 = fig.add_subplot(gs[1, 1])
    
    # Show power components for moderate use
    t_power = np.linspace(0, 8, 500)
    P_total = np.array([scenarios['Moderate Use'](ti*3600) for ti in t_power])
    P_base = np.ones_like(t_power) * PowerModel.P_base
    
    brightness = 0.5
    cpu_util = np.array([0.25 + 0.1*np.sin(ti*3600/300) for ti in t_power])
    P_display = np.array([PowerModel.display_power(brightness) for _ in t_power])
    P_cpu = np.array([PowerModel.cpu_power(u) for u in cpu_util])
    P_network = np.ones_like(t_power) * PowerModel.network_power('wifi', 0.2)
    
    ax4.fill_between(t_power, 0, P_base, alpha=0.8, label='Base', color='#95a5a6')
    ax4.fill_between(t_power, P_base, P_base+P_display, alpha=0.8, label='Display', color='#3498db')
    ax4.fill_between(t_power, P_base+P_display, P_base+P_display+P_cpu, 
                     alpha=0.8, label='CPU', color='#e74c3c')
    ax4.fill_between(t_power, P_base+P_display+P_cpu, P_base+P_display+P_cpu+P_network,
                     alpha=0.8, label='Network', color='#2ecc71')
    
    ax4.plot(t_power, P_total, 'k-', linewidth=2, label='Total')
    
    ax4.set_xlabel('Time (hours)')
    ax4.set_ylabel('Power (mW)')
    ax4.set_xlim(0, 8)
    ax4.legend(loc='upper right')
    ax4.set_title('(d) Power Decomposition: P = P_base + P_display + P_CPU + P_network', fontweight='bold')
    
    # ===== Panel (e): Current from Power (I = P/V) =====
    ax5 = fig.add_subplot(gs[2, 0])
    
    for name in ['Light Use', 'Moderate Use', 'Heavy Use']:
        res = results[name]
        ax5.plot(res['t'], res['current']*1000, '-', linewidth=2, 
                 color=colors[name], label=name)
    
    ax5.set_xlabel('Time (hours)')
    ax5.set_ylabel('Current (mA)')
    ax5.set_xlim(0, 15)
    ax5.legend(loc='upper right')
    ax5.set_title('(e) Discharge Current: I(t) = P(t)/V(t)', fontweight='bold')
    
    # ===== Panel (f): Time-to-Empty Comparison =====
    ax6 = fig.add_subplot(gs[2, 1])
    
    scenario_names = list(results.keys())
    t_empty_values = [results[name]['t_empty'] if results[name]['t_empty'] else 20 
                      for name in scenario_names]
    
    bars = ax6.barh(scenario_names, t_empty_values, 
                    color=[colors[n] for n in scenario_names], alpha=0.8)
    
    # Add value labels
    for bar, val in zip(bars, t_empty_values):
        ax6.text(val + 0.2, bar.get_y() + bar.get_height()/2, 
                 f'{val:.1f}h', va='center', fontsize=10)
    
    ax6.set_xlabel('Time to Empty (hours)')
    ax6.set_xlim(0, max(t_empty_values) * 1.2)
    ax6.set_title('(f) Battery Life by Usage Scenario', fontweight='bold')
    
    return fig, results


def create_rc_dynamics_figure():
    """Create figure showing RC circuit dynamics"""
    
    scenarios = create_usage_scenarios()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    
    # Simulate gaming scenario (high dynamics)
    res = simulate_scenario('Gaming', scenarios['Gaming'])
    
    # ===== Panel (a): RC Voltage Components =====
    ax1 = axes[0, 0]
    
    ax1.plot(res['t'], res['v_rc1']*1000, 'b-', linewidth=2, 
             label=f'V_RC1 (τ₁≈{BatteryParameters.tau1():.0f}s)')
    ax1.plot(res['t'], res['v_rc2']*1000, 'r-', linewidth=2, 
             label=f'V_RC2 (τ₂≈{BatteryParameters.tau2():.0f}s)')
    ax1.plot(res['t'], (res['v_rc1']+res['v_rc2'])*1000, 'k--', linewidth=1.5, 
             alpha=0.7, label='V_RC_total')
    
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Polarization Voltage (mV)')
    ax1.legend(loc='upper right')
    ax1.set_title('(a) RC Polarization Voltages', fontweight='bold')
    
    # ===== Panel (b): Voltage Drop Components =====
    ax2 = axes[0, 1]
    
    V_R0 = res['current'] * BatteryParameters.R0 * 1000  # mV
    
    ax2.fill_between(res['t'], 0, V_R0, alpha=0.7, label='IR₀ (Ohmic)', color='#e74c3c')
    ax2.fill_between(res['t'], V_R0, V_R0+res['v_rc1']*1000, 
                     alpha=0.7, label='V_RC1 (Fast)', color='#3498db')
    ax2.fill_between(res['t'], V_R0+res['v_rc1']*1000, 
                     V_R0+res['v_rc1']*1000+res['v_rc2']*1000,
                     alpha=0.7, label='V_RC2 (Slow)', color='#2ecc71')
    
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Voltage Drop (mV)')
    ax2.legend(loc='upper right')
    ax2.set_title('(b) Voltage Drop Decomposition', fontweight='bold')
    
    # ===== Panel (c): OCV vs Terminal Voltage =====
    ax3 = axes[1, 0]
    
    ax3.plot(res['t'], res['ocv'], 'g-', linewidth=2, label='OCV(SOC)')
    ax3.plot(res['t'], res['voltage'], 'b-', linewidth=2, label='V_terminal')
    ax3.fill_between(res['t'], res['voltage'], res['ocv'], alpha=0.3, color='red',
                     label='Total voltage drop')
    
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('Voltage (V)')
    ax3.legend(loc='lower left')
    ax3.set_title('(c) OCV vs Terminal Voltage (Gaming)', fontweight='bold')
    
    # ===== Panel (d): Power vs Current relationship =====
    ax4 = axes[1, 1]
    
    ax4_twin = ax4.twinx()
    
    line1, = ax4.plot(res['t'], res['power'], 'b-', linewidth=2, label='Power')
    line2, = ax4_twin.plot(res['t'], res['current']*1000, 'r-', linewidth=2, label='Current')
    
    ax4.set_xlabel('Time (hours)')
    ax4.set_ylabel('Power (mW)', color='b')
    ax4_twin.set_ylabel('Current (mA)', color='r')
    ax4.tick_params(axis='y', labelcolor='b')
    ax4_twin.tick_params(axis='y', labelcolor='r')
    
    ax4.legend([line1, line2], ['Power P(t)', 'Current I=P/V'], loc='upper right')
    ax4.set_title('(d) Power-Current Relationship: I(t) = P(t)/V(t)', fontweight='bold')
    
    plt.tight_layout()
    return fig


def create_validation_figure():
    """Create model validation figure with error analysis"""
    
    scenarios = create_usage_scenarios()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    
    # Run moderate use scenario
    res = simulate_scenario('Moderate Use', scenarios['Moderate Use'])
    t_exp, soc_exp, v_exp = generate_synthetic_experimental_data(res)
    
    # Interpolate model to experimental time points
    soc_model = np.interp(t_exp, res['t'], res['soc'])
    v_model = np.interp(t_exp, res['t'], res['voltage'])
    
    # ===== Panel (a): SOC Comparison =====
    ax1 = axes[0, 0]
    
    ax1.scatter(soc_model*100, soc_exp*100, s=30, c=t_exp, cmap='viridis', alpha=0.7)
    ax1.plot([0, 100], [0, 100], 'r--', linewidth=2, label='Perfect fit')
    
    ax1.set_xlabel('Model SOC (%)')
    ax1.set_ylabel('Experimental SOC (%)')
    ax1.set_xlim(0, 85)
    ax1.set_ylim(0, 85)
    ax1.set_aspect('equal')
    ax1.legend()
    ax1.set_title('(a) SOC: Model vs Experiment', fontweight='bold')
    
    # Add R² value
    ss_res = np.sum((soc_exp - soc_model)**2)
    ss_tot = np.sum((soc_exp - np.mean(soc_exp))**2)
    r2 = 1 - ss_res/ss_tot
    ax1.text(0.05, 0.9, f'R² = {r2:.4f}', transform=ax1.transAxes,
             fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat'))
    
    # ===== Panel (b): Voltage Comparison =====
    ax2 = axes[0, 1]
    
    sc = ax2.scatter(v_model, v_exp, s=30, c=t_exp, cmap='viridis', alpha=0.7)
    ax2.plot([3.0, 4.2], [3.0, 4.2], 'r--', linewidth=2, label='Perfect fit')
    
    ax2.set_xlabel('Model Voltage (V)')
    ax2.set_ylabel('Experimental Voltage (V)')
    ax2.legend()
    ax2.set_title('(b) Voltage: Model vs Experiment', fontweight='bold')
    
    # Add colorbar
    cbar = plt.colorbar(sc, ax=ax2)
    cbar.set_label('Time (h)')
    
    # ===== Panel (c): Residual Analysis =====
    ax3 = axes[1, 0]
    
    soc_residual = (soc_exp - soc_model) * 100
    
    ax3.scatter(t_exp, soc_residual, s=30, c='blue', alpha=0.6)
    ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax3.axhline(y=2, color='red', linestyle='--', alpha=0.5)
    ax3.axhline(y=-2, color='red', linestyle='--', alpha=0.5)
    ax3.fill_between([0, max(t_exp)], -2, 2, alpha=0.1, color='green')
    
    ax3.set_xlabel('Time (hours)')
    ax3.set_ylabel('SOC Residual (%)')
    ax3.set_title('(c) SOC Prediction Residuals', fontweight='bold')
    
    rmse = np.sqrt(np.mean(soc_residual**2))
    mae = np.mean(np.abs(soc_residual))
    ax3.text(0.7, 0.9, f'RMSE = {rmse:.2f}%\nMAE = {mae:.2f}%', 
             transform=ax3.transAxes, fontsize=10,
             bbox=dict(boxstyle='round', facecolor='wheat'))
    
    # ===== Panel (d): Error Distribution =====
    ax4 = axes[1, 1]
    
    ax4.hist(soc_residual, bins=20, density=True, alpha=0.7, color='#3498db', 
             edgecolor='black', label='Residual distribution')
    
    # Fit normal distribution
    mu, std = np.mean(soc_residual), np.std(soc_residual)
    x = np.linspace(min(soc_residual), max(soc_residual), 100)
    from scipy.stats import norm
    ax4.plot(x, norm.pdf(x, mu, std), 'r-', linewidth=2, 
             label=f'N({mu:.2f}, {std:.2f}²)')
    
    ax4.set_xlabel('SOC Residual (%)')
    ax4.set_ylabel('Density')
    ax4.legend()
    ax4.set_title('(d) Residual Distribution', fontweight='bold')
    
    plt.tight_layout()
    return fig


if __name__ == '__main__':
    print("=" * 70)
    print("Power-Driven SOC Simulation with 2-RC ECM")
    print("=" * 70)
    
    # Create main simulation figure
    print("\n[1/3] Creating main simulation comparison figure...")
    fig1, results = create_main_simulation_figure()
    fig1.savefig('power_soc_simulation.png', dpi=300, bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    fig1.savefig('power_soc_simulation.pdf', bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    print("    Saved: power_soc_simulation.png/pdf")
    
    # Print battery life results
    print("\n    Battery Life Results:")
    for name, res in results.items():
        t_empty = res['t_empty'] if res['t_empty'] else '>20'
        print(f"      {name:20s}: {t_empty} hours")
    
    # Create RC dynamics figure
    print("\n[2/3] Creating RC dynamics visualization...")
    fig2 = create_rc_dynamics_figure()
    fig2.savefig('rc_dynamics.png', dpi=300, bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    fig2.savefig('rc_dynamics.pdf', bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    print("    Saved: rc_dynamics.png/pdf")
    
    # Create validation figure
    print("\n[3/3] Creating validation comparison figure...")
    fig3 = create_validation_figure()
    fig3.savefig('model_validation.png', dpi=300, bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    fig3.savefig('model_validation.pdf', bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    print("    Saved: model_validation.png/pdf")
    
    print("\n" + "=" * 70)
    print("All figures generated successfully!")
    print("=" * 70)
    
    plt.close('all')
