#!/usr/bin/env python3
"""
Novel Concentric ECM Visualization for MCM 2026 Problem A
Creates a radial "Electron Tunnel" representation of 2-RC Equivalent Circuit Model
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Wedge, FancyArrowPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects
from matplotlib import rcParams

# Configure for publication quality
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.linewidth'] = 1.2
rcParams['mathtext.fontset'] = 'cm'

def create_concentric_ecm():
    """Create the novel concentric ECM visualization"""
    
    fig, ax = plt.subplots(figsize=(8, 9), facecolor='white')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.7, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # ===== Color definitions =====
    soc_colors = ['#d62728', '#ff7f0e', '#ffbb33', '#98df8a', '#2ca02c']  # Red to Green
    soc_cmap = LinearSegmentedColormap.from_list('soc', soc_colors, N=256)
    
    ring_blue_dark = '#2c3e50'
    ring_blue_mid = '#3498db'
    ring_blue_light = '#85c1e9'
    ring_gray = '#7f8c8d'
    capacitor_color = '#e74c3c'
    resistor_color = '#f39c12'
    
    # ===== Ring radii (from center outward) =====
    r_soc = 0.25          # SOC core
    r_ocv = 0.38          # OCV ring
    r_rc2_inner = 0.42    # R2||C2 inner
    r_rc2_outer = 0.68    # R2||C2 outer (thick - slow dynamics)
    r_rc1_inner = 0.72    # R1||C1 inner
    r_rc1_outer = 0.90    # R1||C1 outer (thinner - fast dynamics)
    r_r0_inner = 0.94     # R0 inner
    r_r0_outer = 1.05     # R0 outer (thin shell)
    r_terminal = 1.20     # Terminal measurement point
    
    # ===== 1. SOC Core (gradient-filled circle) =====
    # Create gradient effect with multiple circles
    n_gradient = 50
    for i in range(n_gradient, 0, -1):
        ratio = i / n_gradient
        r = r_soc * ratio
        # SOC value for color (demonstrating 70% SOC)
        soc_demo = 0.7
        color = soc_cmap(soc_demo * ratio + (1-ratio) * 0.3)
        circle = Circle((0, 0), r, facecolor=color, edgecolor='none', zorder=10)
        ax.add_patch(circle)
    
    # SOC label in center
    ax.text(0, 0, r'$\mathbf{SOC}$', ha='center', va='center', fontsize=12, 
            fontweight='bold', color='white', zorder=15)
    
    # ===== 2. OCV Ring =====
    ocv_ring = Wedge((0, 0), r_ocv, 0, 360, width=r_ocv-r_soc-0.02,
                      facecolor='#1a5276', edgecolor='white', linewidth=1.5, zorder=8)
    ax.add_patch(ocv_ring)
    ax.text(0.32, 0.12, r'$V_{OC}$', ha='center', va='center', fontsize=10, 
            color='white', fontweight='bold', zorder=9)
    
    # ===== 3. R2||C2 Ring (Slow Diffusion - THICK) =====
    # Main ring
    rc2_ring = Wedge((0, 0), r_rc2_outer, 0, 360, width=r_rc2_outer-r_rc2_inner,
                      facecolor=ring_blue_light, edgecolor=ring_blue_dark, 
                      linewidth=1.5, alpha=0.8, zorder=6)
    ax.add_patch(rc2_ring)
    
    # Add visual elements for R and C (alternating segments)
    for angle in range(0, 360, 30):
        # Resistor segments (zigzag pattern approximation)
        if angle % 60 == 0:
            wedge = Wedge((0, 0), r_rc2_outer-0.02, angle, angle+25, 
                         width=0.18, facecolor=resistor_color, alpha=0.7, zorder=7)
            ax.add_patch(wedge)
        else:
            # Capacitor segments
            wedge = Wedge((0, 0), r_rc2_outer-0.02, angle, angle+25,
                         width=0.18, facecolor=capacitor_color, alpha=0.5, zorder=7)
            ax.add_patch(wedge)
    
    # R2||C2 labels
    ax.text(0.55, 0.55, r'$R_2$', ha='center', va='center', fontsize=10, 
            color=ring_blue_dark, fontweight='bold', zorder=9)
    ax.text(-0.55, 0.55, r'$C_2$', ha='center', va='center', fontsize=10,
            color=ring_blue_dark, fontweight='bold', zorder=9)
    ax.text(0.0, -0.55, r'$\tau_2 \approx 500s$', ha='center', va='center', 
            fontsize=9, color=ring_blue_dark, style='italic', zorder=9)
    
    # ===== 4. R1||C1 Ring (Fast Dynamics - THINNER) =====
    rc1_ring = Wedge((0, 0), r_rc1_outer, 0, 360, width=r_rc1_outer-r_rc1_inner,
                      facecolor=ring_blue_mid, edgecolor=ring_blue_dark,
                      linewidth=1.5, alpha=0.7, zorder=5)
    ax.add_patch(rc1_ring)
    
    # Visual elements for R1 and C1
    for angle in range(15, 360, 30):
        if angle % 60 == 15:
            wedge = Wedge((0, 0), r_rc1_outer-0.01, angle, angle+20,
                         width=0.12, facecolor=resistor_color, alpha=0.6, zorder=6)
            ax.add_patch(wedge)
        else:
            wedge = Wedge((0, 0), r_rc1_outer-0.01, angle, angle+20,
                         width=0.12, facecolor=capacitor_color, alpha=0.4, zorder=6)
            ax.add_patch(wedge)
    
    # R1||C1 labels
    ax.text(0.81, 0.25, r'$R_1$', ha='center', va='center', fontsize=10,
            color='white', fontweight='bold', zorder=9)
    ax.text(-0.81, 0.25, r'$C_1$', ha='center', va='center', fontsize=10,
            color='white', fontweight='bold', zorder=9)
    ax.text(0.81, -0.25, r'$\tau_1$', ha='center', va='center', fontsize=9,
            color='white', zorder=9)
    ax.text(-0.81, -0.25, r'$\approx 40s$', ha='center', va='center', fontsize=9,
            color='white', zorder=9)
    
    # ===== 5. R0 Outer Shell (Ohmic - THIN rigid boundary) =====
    r0_ring = Wedge((0, 0), r_r0_outer, 0, 360, width=r_r0_outer-r_r0_inner,
                     facecolor=ring_gray, edgecolor='#2c3e50', linewidth=2, zorder=4)
    ax.add_patch(r0_ring)
    
    # R0 label
    ax.text(1.0, 0.0, r'$R_0$', ha='center', va='center', fontsize=11,
            color='white', fontweight='bold', zorder=9)
    
    # ===== 6. Terminal Voltage Point =====
    # Measurement probe
    terminal_circle = Circle((r_terminal, 0), 0.08, facecolor='#27ae60', 
                              edgecolor='#1e8449', linewidth=2, zorder=10)
    ax.add_patch(terminal_circle)
    ax.text(r_terminal, 0, '+', ha='center', va='center', fontsize=14,
            color='white', fontweight='bold', zorder=11)
    
    # V(t) label with arrow
    ax.annotate(r'$V(t)$', xy=(r_terminal+0.1, 0), xytext=(r_terminal+0.35, 0.15),
                fontsize=12, fontweight='bold', color='#27ae60',
                arrowprops=dict(arrowstyle='->', color='#27ae60', lw=1.5))
    
    # Ground reference
    ground_y = -0.15
    ax.plot([r_terminal-0.08, r_terminal+0.08], [ground_y, ground_y], 
            color='#2c3e50', linewidth=2)
    ax.plot([r_terminal-0.05, r_terminal+0.05], [ground_y-0.03, ground_y-0.03],
            color='#2c3e50', linewidth=1.5)
    ax.plot([r_terminal-0.02, r_terminal+0.02], [ground_y-0.06, ground_y-0.06],
            color='#2c3e50', linewidth=1)
    
    # ===== 7. Current Flow Arrow =====
    # Radial arrow showing I(t) discharge direction
    arrow = FancyArrowPatch((0.35, 0.9), (0.85, 1.15),
                            arrowstyle='-|>', mutation_scale=20,
                            color='#8e44ad', linewidth=2.5, zorder=12)
    ax.add_patch(arrow)
    ax.text(0.55, 1.18, r'$I(t)$', ha='center', va='bottom', fontsize=12,
            color='#8e44ad', fontweight='bold')
    ax.text(0.82, 1.28, r'(discharge)', ha='center', va='bottom', fontsize=9,
            color='#8e44ad', style='italic')
    
    # ===== 8. Layer Labels (curved annotations) =====
    # Title for the visualization
    ax.text(0, 1.42, r'$\mathbf{Concentric\ ECM:\ SOC \rightarrow OCV \rightarrow V(t)}$',
            ha='center', va='center', fontsize=13, fontweight='bold', color='#2c3e50')
    ax.text(0, 1.28, r'Second-Order Equivalent Circuit Model (2-RC)',
            ha='center', va='center', fontsize=10, color='#7f8c8d')
    
    # ===== 9. Voltage Equation at Bottom =====
    eq_box = mpatches.FancyBboxPatch((-1.35, -1.55), 2.7, 0.35, 
                                      boxstyle="round,pad=0.02,rounding_size=0.05",
                                      facecolor='#ecf0f1', edgecolor='#2c3e50',
                                      linewidth=1.5, zorder=15)
    ax.add_patch(eq_box)
    ax.text(0, -1.38, r'$V(t) = V_{OC}(SOC) - I \cdot R_0 - V_{RC1} - V_{RC2}$',
            ha='center', va='center', fontsize=12, color='#2c3e50',
            fontweight='bold', zorder=16)
    
    # ===== 10. SOC Colorbar =====
    # Create a small colorbar on the left
    cbar_ax = fig.add_axes([0.08, 0.35, 0.025, 0.3])
    norm = plt.Normalize(0, 100)
    sm = plt.cm.ScalarMappable(cmap=soc_cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax)
    cbar.set_label('SOC (%)', fontsize=10)
    cbar.ax.tick_params(labelsize=8)
    
    # ===== 11. Legend for R and C =====
    legend_elements = [
        mpatches.Patch(facecolor=resistor_color, alpha=0.7, edgecolor='none',
                       label=r'Resistance ($R$)'),
        mpatches.Patch(facecolor=capacitor_color, alpha=0.5, edgecolor='none',
                       label=r'Capacitance ($C$)')
    ]
    ax.legend(handles=legend_elements, loc='lower left', 
              bbox_to_anchor=(-0.12, -0.08), fontsize=9, framealpha=0.9)
    
    # ===== 12. Annotation: "Bridge" concept =====
    # Show the conceptual bridge from internal to external
    ax.annotate('', xy=(0.18, -0.18), xytext=(-0.12, -0.35),
                arrowprops=dict(arrowstyle='->', color='#7f8c8d', 
                               connectionstyle='arc3,rad=0.2', lw=1))
    ax.text(-0.35, -0.42, 'Internal\n(unmeasurable)', ha='center', va='top',
            fontsize=8, color='#7f8c8d', style='italic')
    
    ax.annotate('', xy=(1.12, 0), xytext=(1.35, 0.35),
                arrowprops=dict(arrowstyle='->', color='#27ae60',
                               connectionstyle='arc3,rad=-0.2', lw=1))
    ax.text(1.38, 0.42, 'External\n(measurable)', ha='center', va='bottom',
            fontsize=8, color='#27ae60', style='italic')
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    # Create the figure
    fig = create_concentric_ecm()
    
    # Save outputs
    output_dir = r"D:\jingsai\shumo\MCM\2026A\PAPER\figures"
    
    # Save PNG (300 DPI)
    png_path = f"{output_dir}/ecm_concentric.png"
    fig.savefig(png_path, dpi=300, facecolor='white', edgecolor='none',
                bbox_inches='tight', pad_inches=0.1)
    print(f"Saved: {png_path}")
    
    # Save PDF
    pdf_path = f"{output_dir}/ecm_concentric.pdf"
    fig.savefig(pdf_path, facecolor='white', edgecolor='none',
                bbox_inches='tight', pad_inches=0.1)
    print(f"Saved: {pdf_path}")
    
    plt.close()
    print("Done! Novel concentric ECM diagram created successfully.")
