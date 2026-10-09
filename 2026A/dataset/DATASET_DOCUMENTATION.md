# Battery Dataset Documentation

## MCM 2026 Problem A: Smartphone Battery Modeling

**Document Version:** 1.0  
**Last Updated:** Session Date  
**Purpose:** Comprehensive documentation of all datasets used for battery SOC estimation and power modeling

---

## Table of Contents

1. [Overview](#1-overview)
2. [Data Sources Summary](#2-data-sources-summary)
3. [LG 18650HG2 Dataset](#3-lg-18650hg2-dataset)
4. [Panasonic 18650PF Dataset](#4-panasonic-18650pf-dataset)
5. [NASA Battery Aging Dataset](#5-nasa-battery-aging-dataset)
6. [Chinese OCV Characterization Data](#6-chinese-ocv-characterization-data)
7. [Oxford Battery Degradation Dataset](#7-oxford-battery-degradation-dataset)
8. [Reference Literature](#8-reference-literature)
9. [Data Preprocessing Pipeline](#9-data-preprocessing-pipeline)
10. [Usage in Paper Models](#10-usage-in-paper-models)
11. [Academic Citations](#11-academic-citations)

---

## 1. Overview

This document describes all datasets collected and utilized for the MCM 2026 Problem A solution, which focuses on:

- **State of Charge (SOC) Estimation** using Equivalent Circuit Models (ECM)
- **Open Circuit Voltage (OCV)** characterization across temperature ranges
- **Power consumption modeling** for smartphone applications
- **Battery degradation** and capacity fade analysis

### Dataset Directory Structure

```
D:\jingsai\shumo\MCM\2026A\dataset\
├── battery data/                          # Chinese OCV characterization
│   ├── 低电流开路电压/                    # Low-current OCV tests
│   └── 增量电流开路电压/                  # Incremental current OCV tests
├── LG 18650HG2 Li-ion Battery Data.../    # Primary ECM training data
│   ├── LG_HG2_Original_Dataset_McMasterUniversity_Jan_2020/
│   └── LG_HG2_Prepared_Dataset_McMasterUniversity_Jan_2020/
├── LG-18650HG2-SOC-Estimation/            # ML reference implementation
├── wykht8y7tg-1/Panasonic 18650PF Data/   # EIS and drive cycle data
├── metadata.csv                           # NASA battery aging metadata
├── Oxford_Battery_Degradation_Dataset_1.mat  # Degradation cycles
├── 3Ws.pdf                                # Power consumption literature
├── AndroWatts_*.pdf                       # Mobile power analysis
└── s41586-020-1994-5.pdf                  # Nature battery research
```

---

## 2. Data Sources Summary

| Dataset | Origin | Cell Type | Capacity | Temp Range | Primary Use |
|---------|--------|-----------|----------|------------|-------------|
| LG 18650HG2 | McMaster University | Li-ion NMC | 3.0 Ah | -20°C to 40°C | ECM parameter identification |
| Panasonic 18650PF | UW-Madison | Li-ion | 2.9 Ah | -20°C to 25°C | EIS validation, drive cycles |
| NASA B0045/B0047/B0048 | NASA Ames | Li-ion | 2.0 Ah | 24°C | Aging/degradation modeling |
| Chinese OCV Data | Local source | Li-ion | - | Room temp | OCV curve characterization |
| Oxford Degradation | Oxford University | Li-ion | - | Various | Capacity fade analysis |

---

## 3. LG 18650HG2 Dataset

### 3.1 Source Information

- **Institution:** McMaster University, Hamilton, Ontario, Canada
- **Principal Investigator:** Dr. Phillip Kollmeyer (phillip.kollmeyer@gmail.com)
- **Publication Date:** January 2020
- **DOI:** https://data.mendeley.com/datasets/cp3473x7xv/3

### 3.2 Cell Specifications

| Parameter | Value |
|-----------|-------|
| Manufacturer | LG Chem |
| Model | 18650HG2 |
| Chemistry | Li-ion NMC |
| Nominal Capacity | 3.0 Ah |
| Nominal Voltage | 3.6 V |
| Voltage Range | 2.5 V - 4.2 V |
| Max Discharge | 20 A continuous |

### 3.3 Test Equipment

- **Thermal Chamber:** 8 cu.ft. environmental chamber
- **Battery Tester:** Digatron Firing Circuits Universal Battery Tester
  - 75 A, 5 V channel
  - Voltage/current accuracy: 0.1% of full scale
- **Temperature Sensor:** AD592 (±1°C accuracy)

### 3.4 Directory Structure

```
LG_HG2_Original_Dataset_McMasterUniversity_Jan_2020/
├── 40degC/          # 40°C ambient tests
├── 25degC/          # 25°C ambient tests (reference temperature)
├── 10degC/          # 10°C ambient tests
├── 0degC/           # 0°C ambient tests
├── n10degC/         # -10°C ambient tests
├── n20degC/         # -20°C ambient tests
├── Readme file - Description of Experimental Tests.txt
├── Plot_results.m
└── Technical Information and Experimental Test Results for LG 18650HG2.pdf
```

### 3.5 Test Protocol

1. **HPPC Test (Hybrid Pulse Power Characterization)**
   - Discharge rates: 1C, 2C, 4C, 6C
   - Charge rates: 0.5C, 1C, 1.5C, 2C
   - SOC levels: 100%, 95%, 90%, 80%, 70%, ..., 20%, 15%, 10%, 5%, 2.5%, 0%
   - Used for: R₀, R₁, R₂, τ₁, τ₂ parameter extraction

2. **C/20 Discharge and Charge**
   - Very slow rate for accurate OCV-SOC curve
   - Minimal polarization effects

3. **Constant Current Discharge Tests**
   - 0.5C, 1C, 2C discharge rates
   - Capacity characterization

4. **Drive Cycle Tests**
   - UDDS (Urban Dynamometer Driving Schedule)
   - HWFET (Highway Fuel Economy Test)
   - LA92 (California Unified Cycle)
   - US06 (Supplemental Federal Test Procedure)
   - Mixed cycles (Mix1-Mix8): Random combinations

### 3.6 Data Columns

| Column | Description | Units |
|--------|-------------|-------|
| Time | Elapsed time since test start | seconds |
| TimeStamp | Absolute timestamp | MM/DD/YYYY HH:MM:SS |
| Voltage | Cell terminal voltage | V |
| Current | Cell current (positive = discharge) | A |
| Ah | Accumulated amp-hours | Ah |
| Wh | Accumulated watt-hours | Wh |
| Power | Instantaneous power | W |
| Battery_Temp_degC | Cell case temperature | °C |

### 3.7 File Naming Convention

```
{date}_{time} {test_id}_{test_type}_{temperature}.csv
Example: 11-07-18_10.49 557_Cap_1C_40degC_LGHG2.csv
```

### 3.8 Sample Statistics

- **Files per temperature folder:** ~50-60 files
- **Total files:** ~350 CSV files
- **Typical file size:** 1-10 MB
- **Rows per drive cycle file:** ~90,000 (0.1s sampling)
- **Sampling rate:** 0.1s for drive cycles, variable for charges/pauses

---

## 4. Panasonic 18650PF Dataset

### 4.1 Source Information

- **Institution:** University of Wisconsin-Madison
- **Principal Investigator:** Dr. Phillip Kollmeyer
- **DOI:** https://data.mendeley.com/datasets/wykht8y7tg/1

### 4.2 Cell Specifications

| Parameter | Value |
|-----------|-------|
| Manufacturer | Panasonic |
| Model | NCR18650PF |
| Chemistry | Li-ion |
| Nominal Capacity | 2.9 Ah |
| Voltage Range | 2.5 V - 4.2 V |

### 4.3 Directory Structure

```
wykht8y7tg-1/Panasonic 18650PF Data/
├── 25degC/                    # Reference temperature
│   ├── EIS/                   # Electrochemical Impedance Spectroscopy
│   ├── Drive Cycles/          # Dynamic load profiles
│   ├── Charges and Pauses/    # Charge characterization
│   └── 5 pulse test/          # HPPC-style pulse tests
├── 10degC/
├── 0degC/
├── -10degC/
├── -20degC/
├── 10degC Trise/              # Temperature rise tests
├── 10degC Trise with pause/
├── -20degC Trise/
├── -20degC Trise with pause/
├── Readme file - desc of tests performed.txt
└── Plot_results.m
```

### 4.4 Test Protocol

1. **EIS Tests (Electrochemical Impedance Spectroscopy)**
   - Frequency range: 1 mHz to 100 kHz
   - SOC levels: 100%, 95%, 90%, 80%, ..., 5%, 0%
   - Used for: Frequency-domain impedance characterization

2. **Five-Pulse HPPC Test**
   - Discharge rates: 0.5C, 1C, 2C, 4C, 6C
   - SOC levels: Same as EIS

3. **Drive Cycles**
   - Cycle 1-4: Random mix of standard cycles
   - US06, HWFET, UDDS, LA92
   - Neural Network (NN): Custom high-dynamics cycle
   - Power profile: Ford F150 truck with 35 kWh pack, scaled to single cell

4. **Temperature Rise Tests**
   - Starting temperature: -20°C or 10°C
   - Chamber allowed to drift, battery heats during use
   - Tests model behavior during thermal transients

### 4.5 Data Columns

| Column | Description | Units |
|--------|-------------|-------|
| TimeStamp | Absolute timestamp | MM/DD/YYYY HH:MM:SS |
| Voltage | Cell terminal voltage | V |
| Current | Cell current | A |
| Ah | Accumulated amp-hours | Ah |
| Wh | Accumulated watt-hours | Wh |
| Power | Instantaneous power | W |
| Battery_Temp_degC | Cell case temperature | °C |
| Time | Elapsed time | seconds |
| Chamber_Temp_degC | Ambient chamber temperature | °C |

### 4.6 EIS Data Format

EIS files contain frequency-domain data:
- **File naming:** `{test_id}_EIS{sequence}.csv`
- **Columns:** Frequency (Hz), Real Impedance (Ω), Imaginary Impedance (Ω)
- **Files per temperature:** ~12-15 EIS measurements

---

## 5. NASA Battery Aging Dataset

### 5.1 Source Information

- **Institution:** NASA Ames Research Center, Prognostics Center of Excellence
- **Dataset:** Battery Data Set
- **URL:** https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository

### 5.2 Cells Included

| Battery ID | Initial Capacity | End-of-Life Capacity | Cycles |
|------------|------------------|---------------------|--------|
| B0045 | ~2.0 Ah | ~0.6 Ah | 168+ |
| B0047 | ~2.0 Ah | ~1.1 Ah | 184+ |
| B0048 | ~2.0 Ah | ~1.2 Ah | 184+ |

### 5.3 Metadata Structure (metadata.csv)

| Column | Description |
|--------|-------------|
| type | Test type: charge, discharge, impedance |
| start_time | Test start timestamp |
| ambient_temperature | Ambient temperature (°C) |
| battery_id | Battery identifier (B0045, B0047, B0048) |
| test_id | Sequential test number |
| uid | Unique identifier |
| filename | Associated data file |
| Capacity | Measured discharge capacity (Ah) |
| Re | Electrolyte resistance (Ω) |
| Rct | Charge transfer resistance (Ω) |

### 5.4 Test Protocol

- **Charge:** Constant current to 4.2V, constant voltage to 20mA
- **Discharge:** Constant current at 2A to 2.7V
- **Impedance:** EIS at multiple frequencies
- **Ambient Temperature:** 24°C (room temperature)

### 5.5 Usage in Paper

- **Capacity fade modeling:** Track capacity vs. cycle number
- **Impedance growth:** Monitor Re, Rct evolution with aging
- **End-of-life prediction:** Define 70% or 80% capacity threshold

---

## 6. Chinese OCV Characterization Data

### 6.1 Directory Structure

```
battery data/
├── 低电流开路电压/           # Low-current OCV (quasi-equilibrium)
│   ├── sample1/
│   │   └── SP1_Initial capacity_10_16_2015/
│   └── sample2/
│       └── SP3_Initial capacity_10_16_2015/
└── 增量电流开路电压/         # Incremental current OCV
    ├── sample1/
    └── sample2/
```

### 6.2 Test Description

1. **低电流开路电压 (Low-Current OCV)**
   - Very low C-rate discharge/charge (~C/50 or lower)
   - Minimizes polarization effects
   - Provides near-equilibrium OCV-SOC relationship

2. **增量电流开路电压 (Incremental Current OCV)**
   - Small current steps with rest periods
   - Captures OCV at discrete SOC points
   - Useful for piecewise OCV model fitting

### 6.3 Usage in Paper

- **Shepherd OCV model fitting:** `OCV = E₀ + K₁·SOC + K₂·ln(SOC) + K₃·ln(1-SOC)`
- **Temperature coefficient extraction** (if multi-temperature data available)
- **Validation of Nernst-based models**

---

## 7. Oxford Battery Degradation Dataset

### 7.1 Source Information

- **File:** `Oxford_Battery_Degradation_Dataset_1.mat`
- **Format:** MATLAB .mat file
- **Institution:** Oxford University

### 7.2 Content

- Long-term cycling data with capacity measurements
- Degradation under various cycling conditions
- State of Health (SOH) tracking

### 7.3 Usage in Paper

- **SOH estimation models**
- **Capacity fade curve fitting**
- **Lifetime prediction algorithms**

---

## 8. Reference Literature

### 8.1 Included Papers

| File | Title/Description | Relevance |
|------|-------------------|-----------|
| `3Ws.pdf` | Power consumption analysis | Component power modeling |
| `AndroWatts_*.pdf` | Mobile device power unpacking | Display, CPU, network power |
| `s41586-020-1994-5.pdf` | Nature battery research | Advanced battery chemistry |

### 8.2 SOC Estimation Reference Code

```
LG-18650HG2-SOC-Estimation/
├── src/SOCEst/           # Python ML pipeline
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   └── model_evaluation.py
├── artifacts/            # Trained models, scalers
├── config/              # YAML configuration files
└── README.md            # Project documentation
```

**Reference Implementation Features:**
- Bayesian Optimization for hyperparameter tuning
- LSTM neural networks for sequence modeling
- Data normalization and padding
- MLflow integration for experiment tracking

---

## 9. Data Preprocessing Pipeline

### 9.1 LG 18650HG2 Preprocessing

```python
# Pseudocode for data preprocessing
def preprocess_lg_data(raw_csv_path):
    # 1. Load CSV with appropriate encoding
    df = pd.read_csv(raw_csv_path, skiprows=header_rows)
    
    # 2. Parse timestamp column
    df['DateTime'] = pd.to_datetime(df['TimeStamp'])
    
    # 3. Calculate SOC from Ah counter
    # Assuming Ah counter reset at full charge
    df['SOC'] = 1.0 - (df['Ah'] / nominal_capacity)
    
    # 4. Handle variable sampling rate
    df = df.resample('100ms').interpolate()
    
    # 5. Remove outliers and invalid readings
    df = df[(df['Voltage'] >= 2.5) & (df['Voltage'] <= 4.2)]
    
    return df
```

### 9.2 HPPC Parameter Extraction

```python
def extract_ecm_parameters(hppc_data, soc_level):
    """
    Extract 2-RC ECM parameters from pulse response.
    
    Parameters identified:
    - R0: Instantaneous resistance (V_drop / I_step)
    - R1, tau1: First RC pair (fast dynamics, ~1-10s)
    - R2, tau2: Second RC pair (slow dynamics, ~10-100s)
    """
    # Find pulse start/end indices
    pulse_start = find_current_step(hppc_data)
    
    # Calculate R0 from instantaneous voltage drop
    R0 = delta_V_instant / delta_I
    
    # Fit exponential relaxation for R1, R2, tau1, tau2
    # V(t) = V_final - I * (R1*exp(-t/tau1) + R2*exp(-t/tau2))
    params = curve_fit(double_exp_model, t_relax, V_relax)
    
    return R0, R1, tau1, R2, tau2
```

### 9.3 OCV-SOC Curve Fitting

```python
def fit_shepherd_ocv(soc_data, ocv_data):
    """
    Fit Shepherd OCV model: OCV = E0 + K1*SOC + K2*ln(SOC) + K3*ln(1-SOC)
    
    Avoids singularities by clamping SOC to [0.001, 0.999]
    """
    soc_clamped = np.clip(soc_data, 0.001, 0.999)
    
    # Design matrix
    X = np.column_stack([
        np.ones_like(soc_clamped),      # E0
        soc_clamped,                     # K1
        np.log(soc_clamped),             # K2
        np.log(1 - soc_clamped)          # K3
    ])
    
    # Least squares fit
    coeffs, residuals, rank, s = np.linalg.lstsq(X, ocv_data, rcond=None)
    
    return {'E0': coeffs[0], 'K1': coeffs[1], 'K2': coeffs[2], 'K3': coeffs[3]}
```

---

## 10. Usage in Paper Models

### 10.1 Model 1: SOC Dynamics (2-RC ECM)

**Primary Data Source:** LG 18650HG2 HPPC tests

| Parameter | Source | Temperature Dependence |
|-----------|--------|----------------------|
| R₀(SOC, T) | HPPC pulse response | Arrhenius model |
| R₁(SOC, T) | Exponential fit to relaxation | Lookup table |
| R₂(SOC, T) | Exponential fit to relaxation | Lookup table |
| τ₁(T) | Time constant extraction | Temperature-dependent |
| τ₂(T) | Time constant extraction | Temperature-dependent |
| OCV(SOC) | C/20 discharge curve | Shepherd model |

### 10.2 Model 2: Time-to-Empty Prediction

**Primary Data Source:** LG 18650HG2 drive cycles + power literature

| Component | Data Source |
|-----------|-------------|
| Power profiles | Drive cycle current × voltage |
| Component power | AndroWatts paper, 3Ws paper |
| Usage patterns | Simulated user behavior models |

### 10.3 Model 3: Battery Health (SOH)

**Primary Data Source:** NASA aging data + Oxford degradation

| Metric | Data Source | Method |
|--------|-------------|--------|
| Capacity fade | NASA B0045/B0047/B0048 | Cycle counting |
| Resistance growth | NASA impedance data | Re, Rct tracking |
| Calendar aging | Literature + modeling | Arrhenius extrapolation |

---

## 11. Academic Citations

### 11.1 LG 18650HG2 Dataset

```bibtex
@misc{kollmeyer2020lg,
  author = {Kollmeyer, Phillip},
  title = {LG 18650HG2 Li-ion Battery Data and Example Deep Neural Network 
           xEV SOC Estimator Script},
  year = {2020},
  publisher = {Mendeley Data},
  doi = {10.17632/cp3473x7xv.3},
  url = {https://data.mendeley.com/datasets/cp3473x7xv/3}
}
```

### 11.2 Panasonic 18650PF Dataset

```bibtex
@misc{kollmeyer2018panasonic,
  author = {Kollmeyer, Phillip},
  title = {Panasonic 18650PF Li-ion Battery Data},
  year = {2018},
  publisher = {Mendeley Data},
  doi = {10.17632/wykht8y7tg.1},
  url = {https://data.mendeley.com/datasets/wykht8y7tg/1}
}
```

### 11.3 NASA Battery Dataset

```bibtex
@misc{nasa_battery,
  author = {Saha, B. and Goebel, K.},
  title = {Battery Data Set},
  year = {2007},
  publisher = {NASA Ames Research Center, Prognostics Data Repository},
  url = {https://www.nasa.gov/content/prognostics-center-of-excellence-data-set-repository}
}
```

### 11.4 SOC Estimation Reference

```bibtex
@misc{sohal2023soc,
  author = {Sohal, Harpreetsingh and Eleftheriadis, Panagiotis},
  title = {LG-18650HG2-SOC-Estimation: Bayesian Optimization and Neural Network 
           for Battery State of Charge Estimation},
  year = {2023},
  publisher = {GitHub},
  url = {https://github.com/...}
}
```

---

## Appendix A: Quick Reference Card

### File Count Summary

| Dataset | CSV Files | Total Size | Temp Points |
|---------|-----------|------------|-------------|
| LG HG2 Original | ~350 | ~2 GB | 6 |
| LG HG2 Prepared | ~100 | ~500 MB | 6 |
| Panasonic 18650PF | ~200 | ~1 GB | 5 |
| NASA (metadata) | 1 | 50 KB | 1 |
| Chinese OCV | ~10 | ~5 MB | 1 |

### Key Parameters (25°C Reference)

| Parameter | LG HG2 | Panasonic PF |
|-----------|--------|--------------|
| Capacity | 3.0 Ah | 2.9 Ah |
| R₀ (50% SOC) | ~25 mΩ | ~30 mΩ |
| V_max | 4.2 V | 4.2 V |
| V_min | 2.5 V | 2.5 V |

---

*Document generated for MCM 2026 Problem A solution. All datasets are used for academic research purposes with proper attribution.*
