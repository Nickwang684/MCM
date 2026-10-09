# MCM 2026A - BATTERY DATASET INVENTORY & VALIDATION MAPPING

**Analysis Date:** 2025-02-01  
**Total Data Files:** ~700+  
**Directory:** `D:/jingsai/shumo/MCM/2026A/dataset`

---

## 1. DATASET CATEGORIES & ORGANIZATION

### A. OPEN CIRCUIT VOLTAGE (OCV) VALIDATION

**Location:** `battery data/` (Chinese folder names)

```
battery data/
├─ 低电流开路电压 (Low Current OCV)
│  ├─ sample1/SP1_Initial capacity_10_16_2015/
│  │  └─ 10_16_2015_Initial capacity_SP20-1.xlsx (3.8M)
│  └─ sample2/SP3_Initial capacity_10_16_2015/
│     └─ 10_16_2015_Initial capacity_SP20-3.xls (4.0M)
│
└─ 增量电流开路电压 (Incremental Current OCV)
   ├─ sample1/SP1_Initial capacity_10_16_2015/
   │  └─ 10_16_2015_Initial capacity_SP20-1.xlsx (3.8M)
   └─ sample2/SP3_Initial capacity_10_16_2015/
      └─ 10_16_2015_Initial capacity_SP20-3.xls (4.0M)
```

| Property | Value |
|----------|-------|
| **Validation Use** | OCV characterization at different current protocols |
| **File Types** | XLS/XLSX (native spreadsheet format) |
| **Data Content** | Initial capacity tests, OCV curves vs. SOC |
| **Sample Count** | 2 samples × 2 current profiles = 4 files |
| **Total Size** | ~15.6 MB |
| **Priority** | HIGH |

---

### B. EQUIVALENT CIRCUIT MODEL (ECM) / THERMAL VALIDATION

**Location:** `LG 18650HG2 Li-ion Battery Data.../` (McMaster University Dataset)

#### Original Dataset Structure
```
LG_HG2_Original_Dataset_McMasterUniversity_Jan_2020/
├─ 0degC/       (Cold condition)
├─ -10degC/     (Very cold)
├─ -20degC/     (Extreme cold)
├─ 10degC/      (Cool)
├─ 25degC/      (Room temperature - BASELINE)
├─ 40degC/      (Warm/High temperature)
└─ n10degC/     (Additional temp point)
```

#### File Types & Test Patterns

| Test Pattern | Description | File Count |
|---|---|---|
| `Charge*.mat/csv` | Charging profiles (capacity fade tracking) | 16 per temp |
| `Dis_0p5C*.mat/csv` | Low discharge rate (0.5C) | 1-2 per temp |
| `Dis_2C*.mat/csv` | High discharge rate (2C) | 1-2 per temp |
| `C20DisCh*.mat/csv` | C/20 discharge (capacity reference) | 1 per temp |
| `HPPC*.mat/csv` | Hybrid Pulse Power Characterization | 1 per temp |
| `UDDS*.mat/csv` | Urban Dynamometer Driving Schedule | 1 per temp |
| `HWFET*.mat/csv` | Highway Federal Emission Test | 1 per temp |
| `LA92*.mat/csv` | LA92 driving cycle | 1 per temp |
| `US06*.mat/csv` | US06 aggressive driving cycle | 1 per temp |
| `Mixed*.mat/csv` | Mixed driving profiles | 2-8 per temp |
| `PausCycl*.mat/csv` | Cycling with pause periods | 1 per temp |

#### Sample Identification
- Samples identified as SP (e.g., SP549, SP567, SP576)
- Each battery cell tested at multiple temperatures
- Approximately 10+ different battery cells

#### Validation Applications

| Application | Relevance |
|---|---|
| **ECM Parameter Extraction** | Voltage response, current profiles |
| **Thermal Behavior** | Temperature effects on capacity, R, C |
| **Capacity Fade Aging** | Sequential charging shows degradation |
| **Dynamic Power Profiles** | HPPC for SOC estimation |
| **Real-World Driving Cycles** | UDDS, HWFET, LA92, US06 validation |

#### Coverage & Statistics

| Metric | Value |
|---|---|
| Temperature Range | -20°C to +40°C (7 conditions) |
| Multiple Samples | ~10+ different battery cells |
| Load Profile Diversity | Static, dynamic, cyclic, pause |
| Data Volumes | CSV 4KB-20MB range; MAT files 3KB-3.5MB |
| Total Files | ~400+ (MAT + CSV pairs) |
| Total Size | **~1.2 GB** |
| **Priority** | **CRITICAL** |

---

### C. THERMAL DYNAMICS VALIDATION (Extended Coverage)

**Location:** `wykht8y7tg-1/Panasonic 18650PF Data/`

**Cell Type:** Panasonic 18650PF (Different chemistry than LG)

#### Temperature Conditions
```
├─ -20degC Trise (temperature rise analysis)
├─ -20degC Trise with pause
├─ -10degC/ 
├─ 0degC/
├─ 10degC Trise
├─ 10degC Trise with pause
└─ 25degC/ (Room temperature baseline)
```

#### Test Types

| Test Type | Purpose | Files/Temp |
|---|---|---|
| **5 Pulse Test** | Impedance characterization | 1-3 |
| **Charges and Pauses** | Thermal effects during charging | Multiple |
| **Drive Cycles** | Dynamic thermal response | Multiple |
| **EIS** | Electrochemical Impedance Spectroscopy | 1 per temp |
| **1C Discharge Tests** | Discharge capacity vs. temperature | Multiple |

#### Validation Applications

| Application | Details |
|---|---|
| **Temperature Rise (Trise)** | Calculations for thermal models |
| **Impedance vs. Temperature** | Relationships for parameter scaling |
| **Thermal ECM Validation** | Confirm temperature-dependent R, C, OCV |
| **Cross-Cell Comparison** | Alternative cell chemistry validation |
| **Impedance Modeling** | Frequency-domain analysis (EIS) |

#### Statistics

| Metric | Value |
|---|---|
| File Types | MAT and CSV |
| Total Files | ~200+ |
| Total Size | **~800+ MB** |
| **Priority** | **HIGH** |

---

### D. POWER CONSUMPTION & DEVICE LEVEL VALIDATION

**Location:** Root dataset directory

#### Reference Documents

| File | Size | Content |
|---|---|---|
| `3Ws.pdf` | 503K | "Watts-When-Where" reference paper |
| `AndroWatts_Unpacking_the_Power_Consumption_of_Mobile_Devices_Components.pdf` | 511K | Mobile device power breakdown |

#### Validation Use
- Cross-validation against real device power data
- Component-level power model calibration
- Mobile-specific use case validation
- Validation topics: CPU, GPU, display, radio, sensor power models

#### Statistics

| Metric | Value |
|---|---|
| File Types | PDF (reference documents) |
| Total Size | ~1 MB |
| **Priority** | **LOW** |

---

### E. AGING & DEGRADATION DATASETS

**Distribution:** Distributed across temperature conditions in LG and Panasonic datasets

#### Key Files for Aging Analysis

| File Pattern | Description | Sample Count |
|---|---|---|
| `Charge1.csv` → `Charge16.csv` | Sequential charging revealing capacity loss | 16 per cell per temp |
| Multiple discharge tests at same condition | Comparison of performance degradation | Variable |

#### Validation Applications

| Application | Details |
|---|---|
| **Battery Aging Models** | Capacity fade quantification |
| **Degradation Rate Estimation** | Loss per cycle, per hour, per temperature |
| **Cycle-Life Prediction** | Validation of aging models |
| **Temperature Dependency** | Aging acceleration at elevated temps |

#### Data Quality

| Aspect | Value |
|---|---|
| Collection Span | 2015-2023 (implies multi-year studies) |
| Cycle Count | 16+ cycles per temperature condition |
| Temperature Range | Covers -20°C to +40°C acceleration testing |
| **Priority** | **MEDIUM** |

---

### F. ML/DEEP LEARNING PROJECT FILES (Reference Implementation)

**Location:** `LG-18650HG2-SOC-Estimation/` (Complete Git repository)

**Purpose:** SOC estimation pipeline with neural network implementation

#### Key Components

| Component | Purpose |
|---|---|
| `FNN_xEV_Li_ion_SOC_EstimatorScript_March_2020.mlx` (1.2M) | MATLAB/Simulink example with pre-trained FNN |
| `src/SOCEst/components/` | Modular pipeline components |
| `src/SOCEst/config/` | Configuration management |
| `src/SOCEst/constants/` | Shared constants |
| `src/SOCEst/entity/` | Data entity definitions |
| `src/SOCEst/pipeline/` | Training/evaluation pipelines |
| `src/SOCEst/utils/` | Utility functions |
| `config/` | Experiment configurations |
| `artifacts/` | Model outputs and evaluations |
| `mlruns/` | MLflow tracking (2+ experiments) |
| `templates/` | UI templates |

#### Validation Applications

| Application | Purpose |
|---|---|
| **Benchmarking** | Compare proprietary models against published approach |
| **Deep Learning Validation** | SOC estimation accuracy benchmarking |
| **Pipeline Reference** | Code structure and best practices |
| **Pre-trained Models** | Baseline for comparison studies |

#### Statistics

| Metric | Value |
|---|---|
| Total Size | ~500+ MB (includes Python environment) |
| Architecture | Python-based ML pipeline with MLflow |
| Framework Evidence | References to PyTorch/TensorFlow patterns |
| **Priority** | **MEDIUM** |

---

## 2. VALIDATION MAPPING MATRIX

| MODEL COMPONENT | RELEVANT DATASETS | PRIORITY | NOTES |
|---|---|---|---|
| **OCV Modeling** | `battery data/` (OCV files) | HIGH | Direct OCV curves from initial capacity tests |
| | LG HG2 (Charge tests) | MEDIUM | Indirect inference via capacity |
| **Internal Resistance (R)** | LG HG2 (HPPC, Dis_2C) | HIGH | Pulse tests directly capture IR |
| | Panasonic (5 pulse) | MEDIUM | Alternative cell type validation |
| **Diffusion/Warburg** | LG HG2 (all discharge) | HIGH | Time-dependent voltage response |
| | Panasonic EIS | HIGH | Frequency-domain impedance data |
| **Temperature Effects** | LG HG2 (0/-10/-20/40°C) | **CRITICAL** | 7-temperature comprehensive coverage |
| | Panasonic (Trise tests) | **CRITICAL** | Explicit temperature rise data |
| **Capacity Degradation** | LG HG2 (Charge sequences) | HIGH | 16 charge cycles per temperature |
| | `battery data/` (2015 data) | MEDIUM | Historical baseline reference |
| **SOC Estimation (Dynamic)** | LG HG2 (UDDS/HWFET/LA92) | HIGH | Real-world driving cycles |
| | Panasonic (Drive cycles) | MEDIUM | Alternative cell validation |
| **Power Delivery** | LG HG2 (US06, LA92) | MEDIUM | Aggressive power profiles |
| | 3Ws.pdf / AndroWatts.pdf | LOW | Device-level reference data |
| **Cycle Life Prediction** | LG HG2 (all charge seqs) | MEDIUM | Degradation tracking over cycles |
| | Panasonic (multi-tests) | MEDIUM | Alternative cell aging patterns |

---

## 3. RECOMMENDED VALIDATION SEQUENCE

### **PHASE 1 - OCV & Static Parameters**
**Use:** `battery data/` + LG HG2 Charge tests

- [ ] Extract OCV curves at different temperatures
- [ ] Validate OCV vs. SOC relationships
- [ ] Establish baseline capacity reference
- [ ] Compare low-current vs. incremental OCV protocols

### **PHASE 2 - Dynamic Response & ECM**
**Use:** LG HG2 HPPC + Discharge tests

- [ ] Extract internal resistance (R0, R1, C1 parameters)
- [ ] Validate voltage response to current steps
- [ ] Confirm diffusion/Warburg behavior
- [ ] Temperature scaling of R and C

### **PHASE 3 - Temperature Validation**
**Use:** LG HG2 all temperatures + Panasonic Trise

- [ ] Validate temperature effects on R, C, OCV
- [ ] Confirm thermal coupling in model
- [ ] Validate temperature-dependent parameters
- [ ] Establish thermal acceleration factors

### **PHASE 4 - Real-World Cycles**
**Use:** LG HG2 UDDS/HWFET/LA92/US06

- [ ] SOC estimation accuracy validation
- [ ] Power profile tracking
- [ ] Long-duration cycle validation
- [ ] Peak power delivery capability

### **PHASE 5 - Aging & Degradation**
**Use:** Charge sequences + historical data

- [ ] Capacity fade rate validation
- [ ] Long-term model predictions
- [ ] Aging acceleration at elevated temperatures
- [ ] Calendar vs. cycle aging separation

### **PHASE 6 - Cross-Cell Validation**
**Use:** Panasonic dataset

- [ ] Alternative chemistry validation
- [ ] Robustness confirmation
- [ ] Generalization demonstration
- [ ] Differences vs. LG cells

---

## 4. FILE STATISTICS SUMMARY

| Dataset Component | Files | Size | Format | Priority |
|---|---|---|---|---|
| **OCV Data** | 4 | 15.6 MB | XLS/XLSX | HIGH |
| **LG 18650HG2 (All)** | ~350 | 1.2 GB | MAT/CSV | **CRITICAL** |
| **Panasonic 18650PF** | ~200 | 800 MB | MAT/CSV | HIGH |
| **ML Reference** | ~50 | 500 MB | Python+MLflow | MEDIUM |
| **Technical References** | 2 | 1 MB | PDF | LOW |
| **TOTALS** | **~600+** | **2.5+ GB** | **Mixed** | **VARIED** |

### Coverage Metrics

| Metric | Value |
|---|---|
| **Temperature Range** | -20°C to +40°C (7 conditions) |
| **Sample Cells** | 15+ different battery cells |
| **Test Duration** | Collection dates span 2015-2023 |
| **Data Maturity** | Research-grade, peer-reviewed datasets |
| **Test Protocol Diversity** | 11+ different test types |

---

## 5. NOTES & RECOMMENDATIONS

### ✅ STRENGTHS

- ✓ **Comprehensive temperature range:** -20°C to +40°C covers extreme conditions
- ✓ **Multiple test protocols:** Static, dynamic, cyclic, pause-based tests
- ✓ **Multi-cell validation:** 10+ different battery samples for robustness
- ✓ **Long-term aging data:** Sequential charging reveals capacity fade
- ✓ **Real-world driving cycles:** UDDS, HWFET, LA92, US06 for SOC validation
- ✓ **Cross-cell chemistry:** Panasonic provides alternative cell validation
- ✓ **Dual data formats:** Both binary (MAT) and text (CSV) for flexible analysis
- ✓ **High-resolution EIS:** Panasonic includes frequency-domain impedance data

### ⚠️ CONSIDERATIONS

- ⚠ **OCV data limited:** Only 2 samples collected in 2015
- ⚠ **Cell chemistry variation:** LG and Panasonic use different chemistries
- ⚠ **Legacy file formats:** Some older XLS files may require conversion
- ⚠ **Different naming conventions:** Panasonic test naming differs from LG
- ⚠ **EIS complexity:** Frequency-domain analysis requires specialized tools
- ⚠ **File volume:** ~700 files may require efficient indexing

### 📋 RECOMMENDED PRIORITY ORDER FOR VALIDATION

1. **LG HG2 @ 25°C baseline** - All test types (room temperature reference)
2. **Temperature effects** - 0°C, 25°C, 40°C from LG (most relevant range)
3. **OCV characterization** - `battery data/` (static model foundation)
4. **Real-world driving cycles** - UDDS/HWFET/LA92 (practical validation)
5. **Extreme temperatures** - -20°C, +40°C (robustness testing)
6. **Panasonic cross-validation** - Alternative cell chemistry
7. **Aging degradation sequences** - Long-term model predictions

---

## 6. DATA ACCESS & FORMAT REFERENCE

### CSV Format (Text-Based)
- **Advantage:** Human-readable, Excel-compatible, easily imported to Python/MATLAB
- **Typical Structure:** Time, voltage, current, temperature columns
- **File Size Range:** 4 KB (short tests) to 20 MB (long drive cycles)

### MAT Format (MATLAB Binary)
- **Advantage:** Compact storage, preserves MATLAB structures, fast load times
- **Typical Structure:** Struct arrays with 'Data', 'meta' fields
- **File Size Range:** 3 KB to 3.5 MB
- **Conversion Tool:** Can be loaded in Python via `scipy.io.loadmat()`

### XLS/XLSX Format (Spreadsheets)
- **Advantage:** Excel-native, tabular layout, easy manual review
- **Note:** Older XLS may need conversion to XLSX for modern tools
- **Python Import:** `pandas.read_excel()`

---

## 7. SUGGESTED VALIDATION WORKFLOW CODE STRUCTURE

```python
# Pseudocode for validation workflow
class BatteryValidationSuite:
    
    def __init__(self):
        self.ocv_data = load_battery_data()  # Phase 1
        self.lg_thermal = load_lg_hg2()      # Phase 2-3
        self.panasonic = load_panasonic()    # Phase 3, 6
        
    def validate_ocv(self):
        """Phase 1: OCV model validation"""
        # Compare measured vs. predicted OCV curves
        pass
    
    def validate_ecm(self):
        """Phase 2: ECM parameter extraction"""
        # Extract R0, R1, C1, Rct from HPPC and pulse tests
        pass
    
    def validate_temperature(self):
        """Phase 3: Temperature effects"""
        # Validate temperature-dependent parameters
        pass
    
    def validate_soc(self):
        """Phase 4: SOC estimation accuracy"""
        # Kalman filter performance on driving cycles
        pass
    
    def validate_aging(self):
        """Phase 5: Degradation models"""
        # Capacity fade prediction vs. actual
        pass
    
    def cross_validate_cell_types(self):
        """Phase 6: Generalization"""
        # LG models on Panasonic data and vice versa
        pass
```

---

**Document Version:** 1.0  
**Last Updated:** 2025-02-01  
**Next Review:** After Phase 1 validation completion
