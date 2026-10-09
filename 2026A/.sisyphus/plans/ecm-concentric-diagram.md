# Concentric 2‑RC ECM (“Electron Tunnel”) Figure (Matplotlib)

## TL;DR

Create a publication-quality **concentric/radial** ECM diagram showing the conceptual bridge **SOC → OCV(SOC) → terminal voltage V(t)** with layered drops (**R0**, **R1‖C1**, **R2‖C2**) and an outward **discharge current I(t)** arrow. Export **PNG (300 DPI)** + **PDF** to `D:\jingsai\shumo\MCM\2026A\PAPER\figures` as `ecm_concentric.png` and `ecm_concentric.pdf`.

**Estimated effort**: Short–Medium (mostly careful figure layout)

---

## Context

### Original Request
Novel/distinctive academic visualization of a Li‑ion battery **2‑RC equivalent circuit model**, not a conventional horizontal circuit, with explicit narrative from **SOC** (internal) to **OCV** to **measurable terminal voltage**.

### Confirmed Requirements
- Layout: **Concentric “Electron Tunnel”** radial visualization.
- Figure prominence: **double-column width** (~6–7 inches / 17–18 cm).
- White background; academic style.
- SOC core: **continuous color gradient** + **small colorbar** (red=empty → green/blue=full).
- Rings/layers (center → outside):
  1) SOC core
  2) OCV(SOC) ring
  3) **R2‖C2** ring (slow diffusion), **τ2 ≈ 500 s** (thicker)
  4) **R1‖C1** ring (fast), **τ1 ≈ 40 s** (thinner)
  5) **R0** outer shell (ohmic boundary)
  6) External **terminal measurement point** labeled **V(t)**
- Show discharge arrow **I(t), I>0** outward through layers.
- Put equation on-figure:
  - `V(t)=OCV(SOC)−I R₀−V_RC1−V_RC2`
- Output files:
  - `ecm_concentric.png` at **300 DPI**
  - `ecm_concentric.pdf`

### Local Style Conventions (from repo scan)
- Existing plots are Matplotlib-first; no central `.mplstyle` found.
- Common patterns: `tight_layout()` before saving; clean aesthetic; PNG outputs (often dpi ~150) in `model/compare/plots/`.
  - Reference: `model/compare/plot_results.py`.

---

## Work Objectives

### Core Objective
Produce a **single, self-explanatory concentric ECM figure** suitable for an academic paper that visually encodes internal state (SOC) and external observation (V(t)) via ECM elements.

### Concrete Deliverables
- One Python script that generates the diagram.
- Outputs written to:
  - `D:\jingsai\shumo\MCM\2026A\PAPER\figures\ecm_concentric.png`
  - `D:\jingsai\shumo\MCM\2026A\PAPER\figures\ecm_concentric.pdf`

### Must NOT Have (Guardrails)
- Do not draw a standard left-to-right circuit.
- Do not introduce additional ECM elements beyond R0 + two RC branches.
- Avoid overly decorative effects (textures, 3D shading) that reduce print clarity.
- No “manual verification by user” steps in acceptance criteria; keep verification agent-executable.

---

## Verification Strategy (Agent-Executable)

### Automated Verification Commands
The executor should be able to run:
1) Generate figure:
   - `python path\to\generate_ecm_concentric.py`
2) Verify files exist and are non-trivial:
   - Check that both output files exist in `...\PAPER\figures\`
   - Check file sizes are reasonable (e.g., PNG > 100 KB; PDF > 20 KB)
3) Verify PNG dimensions / DPI via Pillow (script or one-liner):
   - `python -c "from PIL import Image; im=Image.open(r'D:\\...\\ecm_concentric.png'); print(im.size, im.info.get('dpi'))"`
   - Expect dpi tuple ~ (300, 300) (note: some pipelines store DPI differently; if absent, rely on exporter’s dpi parameter)

### Visual Sanity Checks (still automated)
- Produce an additional optional “evidence” raster (same as PNG) is the PNG itself. The executor can open it using an automated image read to confirm non-empty pixels (e.g., histogram not all-white):
  - `python -c "from PIL import Image; import numpy as np; im=np.array(Image.open(r'D:\\...\\ecm_concentric.png')); print(im.mean(), im.std())"`
  - Expect std > 0 (not all-white).

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Start Immediately; independent design decisions):
1. Define final composition spec (radii, ring order, label placements, canvas size)
2. Define typography + LaTeX fallback strategy (usetex vs mathtext)
3. Define SOC colormap (red→green/blue), colorbar placement

Wave 2 (After Wave 1):
4. Implement geometry primitives (rings/wedges/arcs; coordinate transforms)
5. Implement glyphs/labels (R0, R1, C1, R2, C2; τ annotations; equation block)
6. Implement narrative arrows (I(t) outward; radial “drop” arrows or minus labels)

Wave 3 (After Wave 2):
7. Final layout polish + export (PNG 300 DPI + PDF; tight bounding boxes)
8. Automated verification script/commands run + quick fix loop (label overlap, margins)

Critical Path: 1 → 4 → 7 → 8

### Dependency Matrix
| Task | Depends On | Can Parallelize With |
|------|------------|----------------------|
| 1 | None | 2, 3 |
| 2 | None | 1, 3 |
| 3 | None | 1, 2 |
| 4 | 1 | 5, 6 |
| 5 | 1,2 | 4, 6 |
| 6 | 1 | 4, 5 |
| 7 | 4,5,6 | 8 (partial) |
| 8 | 7 | None |

---

## TODOs (Exact Implementation Steps)

> Notes for executor:
> - Use `matplotlib.patches` heavily: `Circle`, `Wedge`, `Arc`, `FancyArrowPatch`.
> - Keep axis hidden; enforce equal aspect.
> - Reserve right margin for a small vertical colorbar.

### 1) Compose the concentric layout spec (radii, thickness, canvas)

**What to do**
- Choose a square-ish canvas appropriate for 6–7" width without circle distortion:
  - Recommended start: `figsize=(7.0, 6.5)` inches.
- Define radii (normalized in axis units) for:
  - SOC core radius `r_soc`
  - OCV ring outer radius `r_ocv`
  - R2‖C2 ring outer radius `r_rc2` (thicker)
  - R1‖C1 ring outer radius `r_rc1` (thinner)
  - R0 ring outer radius `r_r0` (outer shell)
- Define consistent ring gaps (small white gaps help readability).
- Decide the “terminal node” location (e.g., on the rightmost point of outer ring) and where to place equation text (top or bottom).

**Acceptance Criteria**
- A written layout table exists in the script (constants with comments).
- Layout leaves space for:
  - colorbar on right
  - equation block
  - external V(t) label

### 2) Typography and LaTeX fallback strategy

**What to do**
- Implement a robust text configuration:
  - Attempt `rcParams['text.usetex']=True`.
  - If TeX is not available at runtime, fallback to mathtext + serif font.
- Standardize font sizes for paper readability:
  - Ring labels ~10–12 pt
  - Equation ~11–12 pt
  - Small annotations ~9–10 pt

**Must NOT do**
- Do not make the figure dependent on TeX without a fallback; the script must still run.

**Acceptance Criteria**
- Script runs successfully on systems without TeX (fallback path tested).
- Math symbols render correctly: subscripts (R₀), τ, parallel symbol (‖ or `\parallel`).

### 3) SOC gradient core + colorbar

**What to do**
- Render a circular gradient “SOC core”:
  - Create a meshgrid in axis coordinates.
  - Compute normalized radial value (or a simple left-to-right gradient if preferred) and mask outside the SOC circle.
  - Display via `imshow` with alpha mask and a colormap mapping **empty→full**.
- Choose a colormap consistent with requirement:
  - Recommend a custom `LinearSegmentedColormap` from red → yellow → teal/blue.
- Add a small vertical colorbar on the right:
  - Label: `SOC` with endpoints `0` and `1` (or `0%` and `100%`).

**Acceptance Criteria**
- Colorbar appears and is readable at print size.
- Core is visibly graded, not flat.

### 4) Draw rings (OCV, R2‖C2, R1‖C1, R0) as clean annuli

**What to do**
- Use `Wedge` patches to create annuli (donut rings):
  - For each ring: draw a 360° wedge (or a nearly-full wedge with a small “gap” angle to avoid seam artifacts).
- Use subtle grayscale fills or white with outlined edges:
  - Keep SOC as the only strong color.
  - Use thicker linewidth for R0 boundary.

**Acceptance Criteria**
- All rings are concentric, evenly spaced, and visually distinct.
- Ring thickness communicates: R2‖C2 thicker than R1‖C1.

### 5) Place component labels and τ annotations on the rings

**What to do**
- Place text labels along rings (positioned at fixed angles like 120°, 240°):
  - OCV ring: `\mathrm{OCV}(\mathrm{SOC})`
  - R2‖C2 ring: `R_2 \parallel C_2` and `\tau_2\approx 500\,\mathrm{s}`
  - R1‖C1 ring: `R_1 \parallel C_1` and `\tau_1\approx 40\,\mathrm{s}`
  - R0 ring: `R_0`
- Optional: draw small minimalist glyphs (academic-safe) near labels:
  - Resistor: short zig-zag polyline
  - Capacitor: two short parallel lines
  - Keep them subtle; labels carry meaning.

**Acceptance Criteria**
- Labels do not overlap and remain legible when rasterized at 300 DPI.
- τ annotations are clearly associated with the correct ring.

### 6) Add the narrative: arrows for I(t) and voltage drop contributions

**What to do**
- Add a clear outward arrow passing through layers:
  - `I(t), I>0` (discharge) pointing from center outward (or from inner ring to outside).
- Add radial arrows/markers showing how voltage reduces moving outward:
  - Between OCV ring and terminal: annotate `-I R_0`, `-V_{RC1}`, `-V_{RC2}`.
  - Implementation options (choose one):
    1) Three short radial arrows at different angles with those labels, or
    2) A single outward arrow with stacked labels.

**Acceptance Criteria**
- Current direction is unambiguous.
- The “drop” terms are visibly tied to their corresponding layers.

### 7) Terminal measurement point and equation block

**What to do**
- Draw an external “measurement node” on the outside (e.g., small filled circle on right).
- Add a probe-like leader line to text `V(t)` to emphasize measurability.
- Add the equation on the figure (top or bottom):
  - `V(t)=OCV(SOC)−I R_0−V_{RC1}−V_{RC2}`
- Keep equation in a light bounding box (white fill, thin gray edge) if needed for contrast.

**Acceptance Criteria**
- The terminal node is visually distinct and clearly labeled.
- Equation is visible and not clipped.

### 8) Export: PNG 300 DPI + PDF (font embedding considerations)

**What to do**
- Save to exactly:
  - `D:\jingsai\shumo\MCM\2026A\PAPER\figures\ecm_concentric.png`
  - `D:\jingsai\shumo\MCM\2026A\PAPER\figures\ecm_concentric.pdf`
- Use:
  - `bbox_inches='tight'` (or a tuned `pad_inches`) to prevent clipping.
  - `dpi=300` for PNG.
- For PDF text consistency:
  - Prefer vector text (default). If using TeX, verify fonts are embedded (depends on environment).

**Acceptance Criteria (agent-executable)**
- After running the script, both files exist.
- PNG indicates ~300 DPI via Pillow `im.info.get('dpi')` when available.
- Files are non-trivial size; image is not blank (pixel std > 0).

---

## Recommended File/Path Conventions (for executor)

- Script location (recommended):
  - `D:\jingsai\shumo\MCM\2026A\PAPER\figures\generate_ecm_concentric.py`
- Outputs in same folder, matching requested names.

---

## Risk Register / Edge Cases

1) **TeX unavailable** → implement runtime fallback to mathtext.
2) **Label overlap / clipping** → reserve margins early; use `constrained_layout` or careful `bbox_inches='tight'` + padding.
3) **Colormap not matching “red→green/blue”** → define a custom segmented colormap explicitly by hex colors.
4) **Print legibility** → test at final size by ensuring minimum font sizes and sufficient contrast.

---

## Notes on Planning Constraints

- Metis review was intended but is not runnable in this environment (only `explore`/`librarian` agents available). The plan includes explicit edge cases/guardrails as a substitute.
