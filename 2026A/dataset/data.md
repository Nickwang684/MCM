# Data Sources Documentation

## MCM 2026 Problem A: Smartphone Battery Modeling

This document records all data sources used in our battery discharge modeling paper, including their origins, preprocessing steps, and specific applications in our models.

---

## 1. Battery Specifications

**Source:** Manufacturer datasheets for typical smartphone Li-ion cells (3.0–5.0 Ah capacity)

**Data Used:**
- Nominal capacity: 3.0 Ah (LG 18650HG2)
- Nominal voltage: 3.6–3.7 V
- Voltage range: 2.5 V – 4.2 V
- Maximum discharge current: 20 A continuous

**Application in Paper:**
- Model 1 (Section 3): State-space model parameter initialization
- Model 2 (Section 4): Energy-based time-to-empty calculation
- Sensitivity Analysis (Section 6): Parameter bounds for Sobol analysis

---

## 2. ECM Parameters (2-RC Equivalent Circuit Model)

**Source:** Electrochemical Impedance Spectroscopy (EIS) measurements from literature [Plett2015, Hu2012]

**Specific Datasets:**
1. **LG 18650HG2 HPPC Test Data**
   - Location: `dataset/LG 18650HG2 Li-ion Battery Data.../LG_HG2_Original_Dataset_McMasterUniversity_Jan_2020/`
   - Temperature folders: 25degC, 0degC, -10degC, -20degC, 40degC
   - Test files: `*_HPPC_*.mat` and `*_HPPC_*.csv`
   - DOI: https://data.mendeley.com/datasets/cp3473x7xv/3

2. **Panasonic 18650PF EIS Data**
   - Location: `dataset/wykht8y7tg-1/Panasonic 18650PF Data/*/EIS/`
   - Files: `3623_EIS*.csv` (frequency-domain impedance)
   - DOI: https://data.mendeley.com/datasets/wykht8y7tg.1

**Parameters Extracted:**

| Parameter | Value | Source | Method |
|-----------|-------|--------|--------|
| R₀ (25°C, 50% SOC) | 50 mΩ | LG HPPC | Instantaneous voltage drop |
| R₁ | 30 mΩ | LG HPPC | Double-exponential fitting |
| R₂ | 20 mΩ | LG HPPC | Double-exponential fitting |
| τ₁ = R₁C₁ | ~40 s | LG HPPC | Relaxation curve fitting |
| τ₂ = R₂C₂ | ~500 s | LG HPPC | Relaxation curve fitting |

**Data Preprocessing:**
1. Loaded raw HPPC test files with variable sampling rates
2. Identified current pulse start/end indices using derivative thresholding
3. Extracted instantaneous R₀ from voltage drop at pulse onset: `R₀ = ΔV_instant / ΔI`
4. Fitted double-exponential relaxation model: `V(t) = V_final - I × (R₁×exp(-t/τ₁) + R₂×exp(-t/τ₂))`
5. Applied Arrhenius temperature correction for multi-temperature data

**Application in Paper:**
- Model 1 (Section 3.2): 2-RC ECM parameterization
- Model 1 (Section 3.5): Temperature-dependent resistance (Arrhenius model)

---

## 3. OCV-SOC Characterization

**Source:** 
1. LG 18650HG2 C/20 discharge/charge tests [Kollmeyer2020]
2. Chinese OCV characterization data (low-current and incremental current tests)

**Specific Datasets:**
1. **LG C/20 Discharge**
   - Files: `*_C20DisCh_*.mat` in each temperature folder
   - Very slow discharge rate minimizing polarization effects

2. **Chinese OCV Data**
   - Location: `dataset/battery data/低电流开路电压/` (Low-current OCV)
   - Location: `dataset/battery data/增量电流开路电压/` (Incremental current OCV)
   - Files: `10_16_2015_Initial capacity_SP20-*.xlsx`

**Shepherd Model Parameters:**

| Parameter | Value | Unit | Description |
|-----------|-------|------|-------------|
| K₀ (E₀) | 3.685 | V | Base voltage |
| K₁ | 0.2156 | V | Linear SOC coefficient |
| K₂ | 0.0351 | V | ln(SOC) coefficient |
| K₃ | -0.0175 | V | ln(1-SOC) coefficient |
| ∂OCV/∂T | -0.3 | mV/K | Temperature coefficient |

**Data Preprocessing:**
1. Loaded C/20 discharge data and calculated SOC from Ah integration: `SOC = 1 - Ah/Q_nom`
2. Clamped SOC to [0.001, 0.999] to avoid log singularities
3. Constructed design matrix: `X = [1, SOC, ln(SOC), ln(1-SOC)]`
4. Performed least-squares fit: `[K₀, K₁, K₂, K₃] = (X'X)⁻¹X'V_OC`
5. Validated RMSE = 4.2 mV vs. pure Nernst model (15.7 mV)

**Application in Paper:**
- Model 1 (Section 3.3): Shepherd OCV model derivation and validation
- Figure 4: OCV model comparison (Nernst vs. Shepherd)

---

## 4. Power Consumption Models

**Source:** Validated power models from UCSD's 3W dataset [Pathak2012] and component-level measurements

**Reference Literature:**
1. **3Ws Paper (Pathak et al., 2012)**
   - Location: `dataset/3Ws.pdf`
   - Fine-grained energy accounting methodology
   - Component power models for CPU, display, network, GPS

2. **AndroWatts Paper**
   - Location: `dataset/AndroWatts_Unpacking_the_Power_Consumption_of_Mobile_Devices_Components.pdf`
   - Display power vs. brightness characterization
   - OLED vs. LCD power comparison

**Power Model Parameters:**

| Component | Idle (mW) | Max (mW) | Model |
|-----------|-----------|----------|-------|
| Display (LCD) | 50 | 800 | P = 50 + 800×B^1.8 |
| CPU | 50 | 2000 | P = 50 + 1950×U^1.5 |
| WiFi | 20 | 800 | State-based |
| 4G LTE | 50 | 2500 | State-based |
| GPS | 0 | 500 | Binary on/off |
| Base (misc) | 100 | 100 | Constant |

**Data Preprocessing:**
1. Extracted empirical power curves from literature figures using digitization
2. Fitted nonlinear models to brightness-power and CPU-power relationships
3. Validated total power against reported device-level measurements
4. Normalized to 3.0 Ah battery for consistent runtime predictions

**Application in Paper:**
- Model 2 (Section 4.3): Component power breakdown
- Model 2 (Section 4.6): Usage scenario definitions (Table 4)
- Sensitivity Analysis (Section 6): Power parameter bounds

---

## 5. Aging and Degradation Data

**Source:** NASA PCoE battery dataset and CALCE accelerated aging experiments

**Specific Datasets:**
1. **NASA Battery Aging Dataset**
   - Location: `dataset/metadata.csv`
   - Batteries: B0045, B0047, B0048
   - URL: https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository
   - Contains: Capacity fade, impedance growth (Re, Rct) over 168+ cycles

2. **Oxford Battery Degradation Dataset**
   - Location: `dataset/Oxford_Battery_Degradation_Dataset_1.mat`
   - Long-term cycling with capacity measurements
   - SOH tracking under various conditions

**Key Aging Metrics Extracted:**

| Battery | Initial Capacity | End-of-Life Capacity | Cycles | Annual Loss Rate |
|---------|-----------------|---------------------|--------|------------------|
| B0045 | ~2.0 Ah | ~0.6 Ah (70% loss) | 168+ | High stress |
| B0047 | ~2.0 Ah | ~1.1 Ah (45% loss) | 184+ | Moderate stress |
| B0048 | ~2.0 Ah | ~1.2 Ah (40% loss) | 184+ | Moderate stress |

**Aging Model Parameters:**

| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| k_cal | 0.02 | %/√day | NASA data fit |
| k_cyc | 0.02 | %/cycle | CALCE literature |
| E_a,cal | 60 | kJ/mol | Arrhenius fit |
| γ (DOD exponent) | 2.0 | - | Literature [Wang2014] |
| k_R (resistance growth) | 2.0 | - | NASA impedance data |

**Data Preprocessing:**
1. Loaded metadata.csv and filtered by battery_id (B0045, B0047, B0048)
2. Extracted capacity fade curves: Capacity vs. cycle number
3. Fitted semi-empirical aging models: `dSOH/dt = -k_cal × exp(-Ea/RT) - k_cyc × DOD^γ × I`
4. Validated resistance growth correlation: 20% capacity loss → 40% R₀ increase
5. Extracted calendar aging stress factors from storage condition experiments

**Application in Paper:**
- Model 3 (Section 5): Battery aging and SOH dynamics
- Model 3 (Section 5.2-5.4): Calendar and cycle aging models
- Model 3 (Section 5.9): Resistance growth model
- Sensitivity Analysis (Section 6): SOH parameter bounds [0.7, 1.0]

---

## 6. Drive Cycle Validation Data

**Source:** LG 18650HG2 and Panasonic 18650PF drive cycle tests

**Specific Datasets:**
1. **LG 18650HG2 Drive Cycles**
   - Location: `dataset/LG 18650HG2.../25degC/`
   - Files: `*_UDDS_*.csv`, `*_HWFET_*.csv`, `*_LA92_*.csv`, `*_US06_*.csv`, `*_Mixed*.csv`
   - Dynamic load profiles representing realistic usage patterns

2. **Panasonic 18650PF Drive Cycles**
   - Location: `dataset/wykht8y7tg-1/Panasonic 18650PF Data/*/Drive cycles/`
   - Additional Neural Network (NN) custom high-dynamics cycle

**Validation Results:**

| Metric | Target | Achieved | Test Dataset |
|--------|--------|----------|--------------|
| SOC RMSE | <3% | 2.1% | LG Mixed cycles |
| Voltage RMSE | <30 mV | 18 mV | LG UDDS, HWFET |
| Temperature RMSE | <2°C | 1.3°C | Panasonic Trise |

**Data Preprocessing:**
1. Resampled variable-rate data to uniform 0.1s intervals
2. Calculated ground-truth SOC from Ah integration with Coulombic efficiency η = 0.998
3. Applied moving average filter to reduce measurement noise
4. Split into training (70%) and validation (30%) subsets
5. Generated residual plots to check for systematic bias

**Application in Paper:**
- Model 1 (Section 3.10): Model validation (Table 1)
- Model 2 (Section 4.2.2): Model validation figure

---

## 7. Sensitivity Analysis Parameters

**Source:** Derived from above datasets and literature bounds

**Parameter Ranges for Sobol Analysis:**

| Parameter | Symbol | Min | Max | Baseline | Unit |
|-----------|--------|-----|-----|----------|------|
| Screen Brightness | B | 0.1 | 1.0 | 0.5 | - |
| CPU Utilization | U_CPU | 0.05 | 0.95 | 0.30 | - |
| Network Power | P_net | 50 | 500 | 100 | mW |
| GPS Status | GPS | 0 | 1 | 0 | - |
| Ambient Temperature | T_amb | 263 | 318 | 298 | K |
| Initial SOC | SOC₀ | 0.2 | 1.0 | 1.0 | - |
| State of Health | SOH | 0.7 | 1.0 | 1.0 | - |
| Nominal Capacity | Q_nom | 2.5 | 5.0 | 3.0 | Ah |
| Internal Resistance | R₀ | 30 | 150 | 50 | mΩ |

**Application in Paper:**
- Sensitivity Analysis (Section 6): Full parameter sweep
- Sobol indices calculation (N=128 base samples, 2560 model evaluations)
- Morris screening validation (15 trajectories, 6 levels)

---

## Data Quality Notes

1. **LG 18650HG2 Dataset**: High-quality laboratory measurements with documented test protocols. Temperature accuracy ±1°C, voltage/current accuracy 0.1% of full scale.

2. **NASA Aging Data**: Well-characterized accelerated aging with controlled conditions. Capacity measurements taken after each full cycle.

3. **Power Consumption Data**: Validated against device-level measurements in published literature. Component isolation achieved through controlled experiments.

4. **Chinese OCV Data**: Local source with lower documentation quality. Cross-validated against LG C/20 data to ensure consistency.

---

## Citation Information

```bibtex
@misc{kollmeyer2020lg,
  author = {Kollmeyer, Phillip},
  title = {LG 18650HG2 Li-ion Battery Data},
  year = {2020},
  doi = {10.17632/cp3473x7xv.3}
}

@misc{kollmeyer2018panasonic,
  author = {Kollmeyer, Phillip},
  title = {Panasonic 18650PF Li-ion Battery Data},
  year = {2018},
  doi = {10.17632/wykht8y7tg.1}
}

@misc{nasa_battery,
  author = {Saha, B. and Goebel, K.},
  title = {Battery Data Set},
  year = {2007},
  publisher = {NASA Ames, Prognostics Data Repository}
}

@inproceedings{Pathak2012,
  author = {Pathak, Abhinav and Hu, Y. Charlie and Zhang, Ming},
  title = {Where is the Energy Spent Inside My App?},
  booktitle = {EuroSys},
  year = {2012}
}
```

---

*Document generated for MCM 2026 Problem A. All datasets used for academic research with proper attribution.*
