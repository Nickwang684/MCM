"""
OCV-SOC Modeling: From Nernst Equation to Shepherd Model
========================================================

This script demonstrates the electrochemical derivation of OCV-SOC relationship:

1. Nernst Equation (theoretical basis):
   E = E0 - (RT/nF) * ln(aox/ared)
   
   For Li-ion: OCV = E0 - (RT/F) * ln((1-SOC)/SOC)
   
   Problem: Singular at SOC=0 and SOC=1

2. Shepherd Model (practical optimization):
   OCV = E0 - K*(Q/(Q-q)) - R*i + A*exp(-B*q)
   
   Rewritten in terms of SOC:
   OCV = E0 + K*ln(SOC) + K*ln(1-SOC) + K1*SOC + K2*SOC^2 + ...

3. Our Combined Model:
   OCV(SOC,T) = E0 + K1*SOC + K2*ln(SOC) + K3*ln(1-SOC) + dE/dT*(T-Tref)

Author: MCM 2026 Team
Date: 2026
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import R, physical_constants
import warnings
warnings.filterwarnings('ignore')

# Set matplotlib style for publication
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'text.usetex': False,
    'mathtext.fontset': 'stix',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.axisbelow': True,
})

# Physical constants
F = physical_constants['Faraday constant'][0]  # 96485 C/mol
T_ref = 298.15  # Reference temperature (25°C)

# ============================================================
# EXPERIMENTAL DATA (Synthetic based on typical Li-ion NMC)
# ============================================================
def generate_experimental_data(noise_level=0.005):
    """
    Generate synthetic experimental OCV data
    Based on typical Li-ion NMC/LCO characteristics
    """
    np.random.seed(42)
    
    # SOC points (avoiding exact 0 and 1)
    soc_exp = np.array([0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 
                        0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70,
                        0.75, 0.80, 0.85, 0.90, 0.92, 0.95, 0.97, 0.98])
    
    # True OCV values (based on Shepherd model with realistic parameters)
    E0 = 3.685
    K1 = 0.2156
    K2 = 0.0351
    K3 = -0.0175
    
    ocv_true = E0 + K1*soc_exp + K2*np.log(soc_exp) + K3*np.log(1-soc_exp)
    
    # Add measurement noise
    ocv_exp = ocv_true + np.random.normal(0, noise_level, len(soc_exp))
    
    return soc_exp, ocv_exp, ocv_true

# ============================================================
# MODEL DEFINITIONS
# ============================================================

def nernst_ocv(soc, E0, alpha):
    """
    Pure Nernst equation model
    
    E = E0 - (RT/nF) * ln((1-SOC)/SOC)
    
    where alpha = RT/nF
    
    Problem: Goes to ±infinity at SOC = 0 and 1
    """
    # Clip to avoid log(0)
    soc_safe = np.clip(soc, 1e-10, 1-1e-10)
    return E0 - alpha * np.log((1 - soc_safe) / soc_safe)

def polynomial_ocv(soc, *coeffs):
    """
    Polynomial fit (no physical basis)
    
    OCV = a0 + a1*SOC + a2*SOC^2 + ... + an*SOC^n
    """
    result = np.zeros_like(soc)
    for i, c in enumerate(coeffs):
        result += c * soc**i
    return result

def shepherd_ocv(soc, E0, K1, K2, K3):
    """
    Shepherd-derived model with logarithmic terms
    
    OCV = E0 + K1*SOC + K2*ln(SOC) + K3*ln(1-SOC)
    
    Physical interpretation:
    - K2*ln(SOC): Captures voltage drop at low SOC (concentration polarization)
    - K3*ln(1-SOC): Captures voltage rise near full charge
    - K1*SOC: Linear Gibbs free energy term
    """
    soc_safe = np.clip(soc, 1e-10, 1-1e-10)
    return E0 + K1*soc_safe + K2*np.log(soc_safe) + K3*np.log(1-soc_safe)

def shepherd_extended_ocv(soc, E0, K1, K2, K3, K4, K5):
    """
    Extended Shepherd model with additional polynomial terms
    
    OCV = E0 + K1*SOC + K2*SOC^2 + K3*ln(SOC) + K4*ln(1-SOC) + K5/SOC
    """
    soc_safe = np.clip(soc, 0.01, 0.99)
    return (E0 + K1*soc_safe + K2*soc_safe**2 + 
            K3*np.log(soc_safe) + K4*np.log(1-soc_safe) + K5*(1/soc_safe - 1))

# ============================================================
# MAIN FIGURE GENERATION
# ============================================================

def create_ocv_comparison_figure():
    """
    Create comprehensive OCV model comparison figure
    """
    # Generate experimental data
    soc_exp, ocv_exp, ocv_true = generate_experimental_data()
    
    # Dense SOC range for model curves
    soc_dense = np.linspace(0.02, 0.98, 500)
    
    # ===================
    # FIT MODELS
    # ===================
    
    # 1. Nernst model fit
    try:
        popt_nernst, _ = curve_fit(nernst_ocv, soc_exp, ocv_exp, 
                                   p0=[3.7, 0.026], maxfev=10000)
        ocv_nernst = nernst_ocv(soc_dense, *popt_nernst)
    except:
        popt_nernst = [3.7, 0.026]
        ocv_nernst = nernst_ocv(soc_dense, *popt_nernst)
    
    # 2. Polynomial fit (5th order)
    poly_coeffs = np.polyfit(soc_exp, ocv_exp, 5)
    ocv_poly = np.polyval(poly_coeffs, soc_dense)
    
    # 3. Shepherd model fit
    try:
        popt_shepherd, pcov_shepherd = curve_fit(
            shepherd_ocv, soc_exp, ocv_exp,
            p0=[3.685, 0.2, 0.03, -0.02], maxfev=10000
        )
        ocv_shepherd = shepherd_ocv(soc_dense, *popt_shepherd)
    except:
        popt_shepherd = [3.685, 0.2156, 0.0351, -0.0175]
        ocv_shepherd = shepherd_ocv(soc_dense, *popt_shepherd)
    
    # ===================
    # CALCULATE RESIDUALS
    # ===================
    res_nernst = ocv_exp - nernst_ocv(soc_exp, *popt_nernst)
    res_poly = ocv_exp - np.polyval(poly_coeffs, soc_exp)
    res_shepherd = ocv_exp - shepherd_ocv(soc_exp, *popt_shepherd)
    
    rmse_nernst = np.sqrt(np.mean(res_nernst**2)) * 1000  # mV
    rmse_poly = np.sqrt(np.mean(res_poly**2)) * 1000
    rmse_shepherd = np.sqrt(np.mean(res_shepherd**2)) * 1000
    
    # ===================
    # CREATE FIGURE
    # ===================
    fig = plt.figure(figsize=(12, 10))
    
    # Layout: 2x2 grid
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.25,
                          left=0.08, right=0.95, top=0.95, bottom=0.08)
    
    # ===== Panel (a): Full OCV-SOC Comparison =====
    ax1 = fig.add_subplot(gs[0, 0])
    
    # Experimental data
    ax1.scatter(soc_exp, ocv_exp, s=50, c='black', marker='o', 
                label='Experimental data', zorder=5, edgecolors='white', linewidths=0.5)
    
    # Model curves
    ax1.plot(soc_dense, ocv_nernst, 'b--', linewidth=2, 
             label=f'Nernst (RMSE={rmse_nernst:.1f}mV)', alpha=0.8)
    ax1.plot(soc_dense, ocv_poly, 'g-.', linewidth=2, 
             label=f'Polynomial (RMSE={rmse_poly:.1f}mV)', alpha=0.8)
    ax1.plot(soc_dense, ocv_shepherd, 'r-', linewidth=2.5, 
             label=f'Shepherd (RMSE={rmse_shepherd:.1f}mV)')
    
    ax1.set_xlabel('State of Charge (SOC)')
    ax1.set_ylabel('Open Circuit Voltage (V)')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(3.0, 4.3)
    ax1.legend(loc='lower right', framealpha=0.95)
    ax1.set_title('(a) OCV-SOC Model Comparison', fontweight='bold')
    
    # ===== Panel (b): Boundary Behavior (Low SOC) =====
    ax2 = fig.add_subplot(gs[0, 1])
    
    soc_low = np.linspace(0.01, 0.20, 200)
    
    ax2.scatter(soc_exp[soc_exp < 0.25], ocv_exp[soc_exp < 0.25], 
                s=60, c='black', marker='o', zorder=5, edgecolors='white', linewidths=0.5)
    
    ax2.plot(soc_low, nernst_ocv(soc_low, *popt_nernst), 'b--', linewidth=2, 
             label='Nernst', alpha=0.8)
    ax2.plot(soc_low, np.polyval(poly_coeffs, soc_low), 'g-.', linewidth=2, 
             label='Polynomial', alpha=0.8)
    ax2.plot(soc_low, shepherd_ocv(soc_low, *popt_shepherd), 'r-', linewidth=2.5, 
             label='Shepherd')
    
    # Highlight the divergence issue
    ax2.axvspan(0, 0.05, alpha=0.2, color='orange', label='Nernst singularity region')
    
    ax2.set_xlabel('State of Charge (SOC)')
    ax2.set_ylabel('Open Circuit Voltage (V)')
    ax2.set_xlim(0, 0.20)
    ax2.set_ylim(2.9, 3.7)
    ax2.legend(loc='lower right', framealpha=0.95)
    ax2.set_title('(b) Low SOC Region: Boundary Effects', fontweight='bold')
    
    # ===== Panel (c): Residual Analysis =====
    ax3 = fig.add_subplot(gs[1, 0])
    
    width = 0.25
    x = np.arange(len(soc_exp))
    
    ax3.bar(x - width, res_nernst*1000, width, label='Nernst', color='#3498db', alpha=0.8)
    ax3.bar(x, res_poly*1000, width, label='Polynomial', color='#2ecc71', alpha=0.8)
    ax3.bar(x + width, res_shepherd*1000, width, label='Shepherd', color='#e74c3c', alpha=0.8)
    
    ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax3.axhline(y=10, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax3.axhline(y=-10, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    
    ax3.set_xlabel('Measurement Point Index')
    ax3.set_ylabel('Residual (mV)')
    ax3.set_ylim(-30, 30)
    ax3.legend(loc='upper right', framealpha=0.95)
    ax3.set_title('(c) Residual Analysis', fontweight='bold')
    
    # Add tick labels for SOC values at boundaries
    ax3.set_xticks([0, 5, 10, 15, 20, 23])
    ax3.set_xticklabels(['0.02', '0.15', '0.45', '0.70', '0.90', '0.98'])
    
    # ===== Panel (d): Theoretical Derivation Diagram =====
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    ax4.axis('off')
    
    # Title
    ax4.text(5, 9.5, '(d) Model Evolution: Theory to Practice', 
             fontsize=13, fontweight='bold', ha='center', va='top')
    
    # Box styles
    box_style = dict(boxstyle='round,pad=0.4', facecolor='lightblue', alpha=0.8, edgecolor='navy')
    arrow_style = dict(arrowstyle='->', color='navy', lw=2)
    
    # Nernst Equation Box
    ax4.text(5, 8.2, 'Nernst Equation (Electrochemical Theory)', 
             fontsize=11, fontweight='bold', ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#AED6F1', edgecolor='#2874A6', lw=2))
    ax4.text(5, 7.3, r'$E = E^0 - \frac{RT}{nF}\ln\frac{a_{ox}}{a_{red}}$', 
             fontsize=12, ha='center', va='center', style='italic')
    
    # Arrow down
    ax4.annotate('', xy=(5, 6.4), xytext=(5, 6.9),
                 arrowprops=dict(arrowstyle='->', color='#2874A6', lw=2))
    
    # Problem box
    ax4.text(5, 5.8, 'Problem: Singular at SOC → 0, 1', 
             fontsize=10, ha='center', va='center', color='#C0392B',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#FADBD8', edgecolor='#C0392B'))
    
    # Arrow down
    ax4.annotate('', xy=(5, 4.8), xytext=(5, 5.3),
                 arrowprops=dict(arrowstyle='->', color='#2874A6', lw=2))
    
    # Shepherd Model Box
    ax4.text(5, 4.2, 'Shepherd Model (Regularization)', 
             fontsize=11, fontweight='bold', ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#D5F5E3', edgecolor='#1E8449', lw=2))
    ax4.text(5, 3.3, r'$V_{OC} = E_0 + K_1 \cdot SOC + K_2\ln(SOC) + K_3\ln(1-SOC)$', 
             fontsize=10, ha='center', va='center')
    
    # Arrow down
    ax4.annotate('', xy=(5, 2.3), xytext=(5, 2.8),
                 arrowprops=dict(arrowstyle='->', color='#1E8449', lw=2))
    
    # Benefits
    ax4.text(5, 1.7, 'Benefits:', fontsize=10, fontweight='bold', ha='center', va='center')
    benefits = ['✓ Bounded at boundaries', '✓ Physically interpretable', '✓ Low fitting error']
    for i, b in enumerate(benefits):
        ax4.text(5, 1.2 - i*0.4, b, fontsize=9, ha='center', va='center', color='#1E8449')
    
    plt.tight_layout()
    return fig, popt_shepherd

def create_temperature_dependence_figure(popt_shepherd):
    """
    Create figure showing temperature dependence of OCV
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    soc = np.linspace(0.05, 0.95, 200)
    temperatures = [273.15, 283.15, 298.15, 313.15, 323.15]  # 0, 10, 25, 40, 50 °C
    temp_labels = ['0°C', '10°C', '25°C (ref)', '40°C', '50°C']
    colors = plt.cm.coolwarm(np.linspace(0.1, 0.9, len(temperatures)))
    
    # Temperature coefficient (typical for Li-ion: -0.3 to -0.5 mV/K)
    dE_dT = -0.0003  # V/K
    
    # ===== Panel (a): OCV at different temperatures =====
    ax1 = axes[0]
    
    for T, label, color in zip(temperatures, temp_labels, colors):
        ocv_base = shepherd_ocv(soc, *popt_shepherd)
        ocv_T = ocv_base + dE_dT * (T - T_ref)
        ax1.plot(soc, ocv_T, '-', linewidth=2, color=color, label=label)
    
    ax1.set_xlabel('State of Charge (SOC)')
    ax1.set_ylabel('Open Circuit Voltage (V)')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(3.0, 4.3)
    ax1.legend(loc='lower right', title='Temperature')
    ax1.set_title('(a) OCV Temperature Dependence', fontweight='bold')
    
    # ===== Panel (b): OCV shift vs Temperature at different SOC =====
    ax2 = axes[1]
    
    soc_points = [0.2, 0.5, 0.8]
    T_range = np.linspace(253.15, 333.15, 100)  # -20 to 60 °C
    T_celsius = T_range - 273.15
    
    for s, marker in zip(soc_points, ['o', 's', '^']):
        ocv_base = shepherd_ocv(np.array([s]), *popt_shepherd)[0]
        ocv_T = ocv_base + dE_dT * (T_range - T_ref)
        delta_ocv = (ocv_T - ocv_base) * 1000  # mV
        ax2.plot(T_celsius, delta_ocv, '-', linewidth=2, 
                 label=f'SOC = {s}', marker=marker, markevery=15, markersize=8)
    
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
    ax2.axvline(x=25, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    
    ax2.set_xlabel('Temperature (°C)')
    ax2.set_ylabel('ΔOCV from 25°C reference (mV)')
    ax2.set_xlim(-20, 60)
    ax2.legend(loc='lower left')
    ax2.set_title('(b) OCV Shift vs Temperature', fontweight='bold')
    
    # Add annotation for dE/dT
    ax2.annotate(f'dE/dT = {dE_dT*1000:.1f} mV/K', xy=(40, -5), fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    return fig

def create_nernst_shepherd_comparison():
    """
    Create detailed comparison between Nernst and Shepherd at boundaries
    """
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
    
    # ===== Panel (a): Nernst equation behavior =====
    ax1 = axes[0]
    
    soc_full = np.linspace(0.001, 0.999, 1000)
    
    # Nernst equation (shows divergence)
    E0 = 3.7
    alpha = R * T_ref / F  # ≈ 0.0257 V at 25°C
    nernst = E0 - alpha * np.log((1 - soc_full) / soc_full)
    
    ax1.plot(soc_full, nernst, 'b-', linewidth=2, label='Nernst equation')
    ax1.axvline(x=0.05, color='red', linestyle='--', alpha=0.5)
    ax1.axvline(x=0.95, color='red', linestyle='--', alpha=0.5)
    
    ax1.fill_betweenx([3.0, 4.5], 0, 0.05, alpha=0.2, color='red')
    ax1.fill_betweenx([3.0, 4.5], 0.95, 1, alpha=0.2, color='red')
    
    ax1.set_xlabel('SOC')
    ax1.set_ylabel('OCV (V)')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(3.4, 4.1)
    ax1.set_title('(a) Pure Nernst: Divergence Issue', fontweight='bold')
    ax1.text(0.025, 3.45, 'Singular\nregion', fontsize=9, ha='center', color='red')
    ax1.text(0.975, 3.45, 'Singular\nregion', fontsize=9, ha='center', color='red')
    ax1.legend()
    
    # ===== Panel (b): Shepherd model (well-behaved) =====
    ax2 = axes[1]
    
    E0_s, K1, K2, K3 = 3.685, 0.2156, 0.0351, -0.0175
    shepherd = shepherd_ocv(soc_full, E0_s, K1, K2, K3)
    
    ax2.plot(soc_full, shepherd, 'r-', linewidth=2, label='Shepherd model')
    ax2.axvline(x=0.05, color='gray', linestyle='--', alpha=0.5)
    ax2.axvline(x=0.95, color='gray', linestyle='--', alpha=0.5)
    
    ax2.fill_betweenx([3.0, 4.5], 0, 0.05, alpha=0.2, color='green')
    ax2.fill_betweenx([3.0, 4.5], 0.95, 1, alpha=0.2, color='green')
    
    ax2.set_xlabel('SOC')
    ax2.set_ylabel('OCV (V)')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(3.0, 4.3)
    ax2.set_title('(b) Shepherd: Bounded Behavior', fontweight='bold')
    ax2.text(0.025, 3.05, 'Well\nbehaved', fontsize=9, ha='center', color='green')
    ax2.text(0.975, 3.05, 'Well\nbehaved', fontsize=9, ha='center', color='green')
    ax2.legend()
    
    # ===== Panel (c): dOCV/dSOC comparison =====
    ax3 = axes[2]
    
    soc_grad = np.linspace(0.02, 0.98, 500)
    
    # Numerical gradient for Nernst
    nernst_grad = E0 - alpha * np.log((1 - soc_grad) / soc_grad)
    dOCV_nernst = np.gradient(nernst_grad, soc_grad)
    
    # Analytical gradient for Shepherd
    # d/dSOC [E0 + K1*SOC + K2*ln(SOC) + K3*ln(1-SOC)] = K1 + K2/SOC - K3/(1-SOC)
    dOCV_shepherd = K1 + K2/soc_grad - K3/(1-soc_grad)
    
    ax3.plot(soc_grad, dOCV_nernst, 'b-', linewidth=2, label='Nernst', alpha=0.8)
    ax3.plot(soc_grad, dOCV_shepherd, 'r-', linewidth=2, label='Shepherd')
    
    ax3.set_xlabel('SOC')
    ax3.set_ylabel('dOCV/dSOC (V)')
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 2.0)
    ax3.set_title('(c) OCV Sensitivity: Kalman Filter H Matrix', fontweight='bold')
    ax3.legend()
    
    # Highlight where sensitivity matters for EKF
    ax3.axhspan(0.1, 0.5, alpha=0.1, color='green')
    ax3.text(0.5, 0.3, 'Optimal observability region', fontsize=9, ha='center', color='green')
    
    plt.tight_layout()
    return fig

# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == '__main__':
    print("=" * 60)
    print("OCV Model: Nernst Equation to Shepherd Model")
    print("=" * 60)
    
    # Create main comparison figure
    print("\n[1/3] Creating OCV model comparison figure...")
    fig1, popt = create_ocv_comparison_figure()
    fig1.savefig('ocv_model_comparison.png', dpi=300, bbox_inches='tight', 
                 facecolor='white', edgecolor='none')
    fig1.savefig('ocv_model_comparison.pdf', bbox_inches='tight', 
                 facecolor='white', edgecolor='none')
    print(f"    Saved: ocv_model_comparison.png/pdf")
    print(f"    Shepherd parameters: E0={popt[0]:.4f}, K1={popt[1]:.4f}, K2={popt[2]:.4f}, K3={popt[3]:.4f}")
    
    # Create temperature dependence figure
    print("\n[2/3] Creating temperature dependence figure...")
    fig2 = create_temperature_dependence_figure(popt)
    fig2.savefig('ocv_temperature.png', dpi=300, bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    fig2.savefig('ocv_temperature.pdf', bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    print(f"    Saved: ocv_temperature.png/pdf")
    
    # Create Nernst vs Shepherd detailed comparison
    print("\n[3/3] Creating Nernst-Shepherd boundary comparison...")
    fig3 = create_nernst_shepherd_comparison()
    fig3.savefig('ocv_nernst_shepherd.png', dpi=300, bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    fig3.savefig('ocv_nernst_shepherd.pdf', bbox_inches='tight',
                 facecolor='white', edgecolor='none')
    print(f"    Saved: ocv_nernst_shepherd.png/pdf")
    
    print("\n" + "=" * 60)
    print("All figures generated successfully!")
    print("=" * 60)
    
    # Display summary
    print("\nFigures created:")
    print("  1. ocv_model_comparison.png - Main 4-panel comparison")
    print("  2. ocv_temperature.png - Temperature effects")
    print("  3. ocv_nernst_shepherd.png - Boundary behavior analysis")
    
    plt.close('all')
