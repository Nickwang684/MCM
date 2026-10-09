# Draft: Concentric 2-RC ECM (“Electron Tunnel”) Figure

## Requirements (confirmed)
- Novel/distinctive academic visualization of a **2-RC ECM** (not a conventional horizontal circuit).
- Must show conceptual bridge: **SOC (internal) → OCV(SOC) → terminal voltage V(t)** (external measurable).
- Creative approach: **concentric/radial “Electron Tunnel”** layers.
- Components to visualize:
  - OCV(SOC) voltage source
  - R0 (ohmic)
  - R1 ‖ C1 (fast dynamics), **τ1 ≈ 40 s**
  - R2 ‖ C2 (slow dynamics), **τ2 ≈ 500 s**
  - Terminal voltage relationship: **V(t)=OCV(SOC)−I R0−V_RC1−V_RC2** (must appear on figure)
- Add **discharge current I>0** arrow labeled **I(t)** flowing outward through layers.
- Visual encoding:
  - SOC shown as **color gradient core** with **small colorbar** (continuous; red=empty to green/blue=full).
- Labels:
  - Include ring labels **R0, R1, C1, R2, C2** plus τ annotations on the RC rings.
- Background: **pure white**.
- Rendering: **matplotlib** with **LaTeX-like text** (prefer `rcParams['text.usetex']=True`; allow mathtext fallback).
- Output:
  - Save to: `D:\jingsai\shumo\MCM\2026A\PAPER\figures`
  - Files: `ecm_concentric.png` (300 DPI) and `ecm_concentric.pdf`.
- Figure size: **double-column** (~17–18 cm / 6–7 inches wide). Prominent “key figure”.

## Technical Decisions (current)
- Use matplotlib **patches** (Circle/Wedge/Arc) + **annotations** for arrows, labels, and equation block.
- Keep ring styling mostly grayscale (academic); use color primarily for SOC core + minimal accents.
- Add explicit outward-flow narrative: SOC → OCV ring → dynamic drops across RC rings + R0 → terminal measurement point.

## Research Findings
- Repo plotting conventions appear Matplotlib-based (no central `.mplstyle`). Existing plots often use `tight_layout()` and save PNGs (commonly ~150 DPI), with clean styling and limited grid usage.
  - Key reference mentioned by exploration: `model/compare/plot_results.py` (plot saving and aesthetic patterns).

## Scope Boundaries
- INCLUDE: One standalone ECM concentric diagram as PNG+PDF with labels, arrows, equation, τ annotations.
- EXCLUDE: Parameter identification, fitting, SOC estimation algorithm, time-series simulation plots, TikZ.

## Open Questions (none blocking for plan)
- Potential fallback if TeX is unavailable on target system (mathtext). Must be handled in implementation.
