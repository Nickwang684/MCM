"""Run model validation and generate comparison artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from data_loaders import (
    compute_soc_from_capacity,
    list_lg_files,
    list_panasonic_files,
    load_lg_csv,
    load_ocv_excel,
)
from metrics import mae, max_error, rmse
from model_impl import BatteryParams, SmartphoneBatteryModel, monte_carlo_t_empty


ROOT = Path(r"D:\jingsai\shumo\MCM\2026A")
DATASET = ROOT / "dataset"
COMPARE = ROOT / "model" / "compare"


def ensure_dirs() -> None:
    """Ensure output directories exist.

    Returns:
        None. Creates output directories if missing.
    """
    COMPARE.mkdir(parents=True, exist_ok=True)
    (COMPARE / "plots").mkdir(exist_ok=True)


def summarize_dataset_inventory() -> pd.DataFrame:
    """Summarize local dataset inventory for reporting.

    Returns:
        DataFrame with dataset names, paths, and notes.
    """
    records: list[dict[str, str]] = []
    lg_root = DATASET / "LG 18650HG2 Li-ion Battery Data and Example Deep Neural Network xEV SOC Estimator Script"
    pan_root = DATASET / "wykht8y7tg-1" / "Panasonic 18650PF Data"
    ocv_root = DATASET / "battery data"
    records.append({"name": "LG HG2", "path": str(lg_root), "notes": "drive cycles, C/20, HPPC, temperatures"})
    records.append({"name": "Panasonic PF", "path": str(pan_root), "notes": "drive cycles, EIS, Trise"})
    records.append({"name": "OCV Excel", "path": str(ocv_root), "notes": "low-current & incremental OCV"})
    return pd.DataFrame(records)


def _find_ocv_columns(df: pd.DataFrame) -> tuple[str, str]:
    """Find voltage and capacity columns in OCV files.

    Args:
        df: OCV data DataFrame.

    Returns:
        Tuple of (voltage_column, capacity_column).

    Raises:
        ValueError: If required columns are missing.
    """
    voltage_col = None
    capacity_col = None
    for col in df.columns:
        col_lower = str(col).lower()
        if voltage_col is None and "voltage" in col_lower:
            voltage_col = col
        if capacity_col is None and "charge_capacity" in col_lower:
            capacity_col = col
    if voltage_col is None or capacity_col is None:
        raise ValueError("OCV file missing Voltage(V) or Charge_Capacity(Ah) column")
    return voltage_col, capacity_col


def validate_ocv(model: SmartphoneBatteryModel) -> pd.DataFrame:
    """Validate OCV-SOC relation using available OCV Excel files.

    Args:
        model: Battery model instance.

    Returns:
        DataFrame with per-file error metrics.
    """
    ocv_files = list((DATASET / "battery data").rglob("*.xls*"))
    rows: list[dict[str, float | str]] = []
    for f in ocv_files:
        try:
            df = load_ocv_excel(f)
            voltage_col, capacity_col = _find_ocv_columns(df)
            voltage = df[voltage_col].to_numpy(dtype=float)
            capacity = df[capacity_col].to_numpy(dtype=float)
            soc = compute_soc_from_capacity(capacity, model.params.Q_nom)
            v_pred = model.ocv(soc)
            rows.append(
                {
                    "file": str(f),
                    "rmse_V": rmse(voltage, v_pred),
                    "mae_V": mae(voltage, v_pred),
                    "max_err_V": max_error(voltage, v_pred),
                }
            )
        except (ValueError, KeyError, pd.errors.EmptyDataError):
            continue
    return pd.DataFrame(rows)


def validate_cycle(
    file_path: Path,
    model: SmartphoneBatteryModel,
    Q_nom: float,
) -> dict[str, float | str | None]:
    """Validate a single LG HG2 cycle file.

    Args:
        file_path: Path to LG HG2 CSV file.
        model: Battery model instance.
        Q_nom: Nominal capacity for SOC calculation.

    Returns:
        Dictionary of metrics and timing comparison.
    """
    data = load_lg_csv(file_path)
    if data.capacity_Ah is None:
        raise ValueError("Capacity is required to compute SOC for LG file")
    soc_true = compute_soc_from_capacity(data.capacity_Ah, Q_nom)
    power_mW = data.power_W * 1000.0

    def power_func(t: float) -> float:
        return float(np.interp(t, data.t_s, power_mW))

    sim = model.simulate(
        SOC_0=float(soc_true[0]),
        T_0=298.15,
        power_func=power_func,
        t_span=(0, float(data.t_s[-1])),
    )
    # Align predicted SOC to observed timestamps (rough)
    t_sim = sim["t"]
    soc_pred = np.interp(data.t_s, t_sim, sim["SOC"])
    v_pred = np.interp(data.t_s, t_sim, sim["V"])
    temp_rmse: float | None = None
    temp_mae: float | None = None
    if data.temperature_C is not None:
        temp_pred = np.interp(data.t_s, t_sim, sim["T"]) - 273.15
        temp_rmse = rmse(data.temperature_C, temp_pred)
        temp_mae = mae(data.temperature_C, temp_pred)
    t_empty = sim["t_empty"]
    t_empty_pred_s = float(t_empty) if t_empty is not None else None
    result = {
        "file": str(file_path),
        "rmse_soc": rmse(soc_true, soc_pred),
        "mae_soc": mae(soc_true, soc_pred),
        "rmse_v": rmse(data.voltage, v_pred),
        "mae_v": mae(data.voltage, v_pred),
        "rmse_temp_C": temp_rmse,
        "mae_temp_C": temp_mae,
        "t_empty_pred_s": t_empty_pred_s,
        "t_end_s": float(data.t_s[-1]),
    }
    return result


def list_lg_cycle_files() -> list[Path]:
    """List LG HG2 cycle files across standard drive profiles.

    Returns:
        List of matching LG HG2 CSV files.
    """
    lg_root = (
        DATASET
        / "LG 18650HG2 Li-ion Battery Data and Example Deep Neural Network xEV SOC Estimator Script"
        / "LG_HG2_Original_Dataset_McMasterUniversity_Jan_2020"
    )
    cycles: list[Path] = []
    patterns = [
        "*UDDS*.csv",
        "*HWFET*.csv",
        "*LA92*.csv",
        "*US06*.csv",
        "*C20DisCh*.csv",
        "*HPPC*.csv",
        "*Charge*.csv",
    ]
    for pattern in patterns:
        cycles.extend(list_lg_files(lg_root, pattern))
    return cycles


def validate_lg_cycles(
    model: SmartphoneBatteryModel,
    cycles: list[Path] | None = None,
) -> pd.DataFrame:
    """Validate a subset of LG HG2 cycles for runtime control.

    Args:
        model: Battery model instance.

    Returns:
        DataFrame of per-file SOC/voltage metrics.
    """
    if cycles is None:
        cycles = list_lg_cycle_files()
    # limit to reduce runtime for full dataset
    cycles = cycles[:30]
    rows: list[dict[str, float | str]] = []
    for f in cycles:
        try:
            rows.append(validate_cycle(f, model, model.params.Q_nom))
        except Exception:
            continue
    return pd.DataFrame(rows)


def validate_panasonic_eis() -> pd.DataFrame:
    """Inventory Panasonic EIS files and infer impedance column availability.

    Returns:
        DataFrame with file-level impedance column availability.
    """
    pan_root = DATASET / "wykht8y7tg-1" / "Panasonic 18650PF Data"
    eis_files = list_panasonic_files(pan_root, "*EIS*.csv")
    rows: list[dict[str, int | str | bool]] = []
    for f in eis_files[:20]:
        try:
            df = pd.read_csv(f, encoding="latin-1")
            cols = [c.lower() for c in df.columns]
            zreal = None
            zimag = None
            for idx, c in enumerate(cols):
                if "real" in c and ("z" in c or "ohm" in c):
                    zreal = df.columns[idx]
                if "imag" in c and ("z" in c or "ohm" in c):
                    zimag = df.columns[idx]
            rows.append(
                {
                    "file": str(f),
                    "rows": len(df),
                    "has_zreal": zreal is not None,
                    "has_zimag": zimag is not None,
                }
            )
        except Exception:
            continue
    return pd.DataFrame(rows)


def validate_uncertainty(model: SmartphoneBatteryModel) -> pd.DataFrame:
    """Generate Monte Carlo samples for t_empty uncertainty.

    Args:
        model: Battery model instance.

    Returns:
        DataFrame with sampled empty-time values in seconds.
    """
    samples = monte_carlo_t_empty(model, SOC_0=0.8, T=298.15, P_mW=1500, n=200)
    return pd.DataFrame({"t_empty_s": samples})


def build_ocv_points(
    model: SmartphoneBatteryModel,
    max_points_per_file: int = 400,
) -> pd.DataFrame:
    """Build OCV scatter points for measured vs predicted voltage.

    Args:
        model: Battery model instance.
        max_points_per_file: Maximum points sampled per file.

    Returns:
        DataFrame with measured/predicted OCV points.
    """
    ocv_files = list((DATASET / "battery data").rglob("*.xls*"))
    frames: list[pd.DataFrame] = []
    for f in ocv_files:
        try:
            df = load_ocv_excel(f)
            voltage_col, capacity_col = _find_ocv_columns(df)
            voltage = df[voltage_col].to_numpy(dtype=float)
            capacity = df[capacity_col].to_numpy(dtype=float)
            soc = compute_soc_from_capacity(capacity, model.params.Q_nom)
            v_pred = model.ocv(soc)
            if len(voltage) == 0:
                continue
            if len(voltage) > max_points_per_file:
                idx = np.linspace(0, len(voltage) - 1, max_points_per_file, dtype=int)
            else:
                idx = np.arange(len(voltage))
            frames.append(
                pd.DataFrame(
                    {
                        "file": str(f),
                        "soc": soc[idx],
                        "v_true": voltage[idx],
                        "v_pred": v_pred[idx],
                    }
                )
            )
        except (ValueError, KeyError, pd.errors.EmptyDataError):
            continue
    if frames:
        return pd.concat(frames, ignore_index=True)
    return pd.DataFrame(columns=["file", "soc", "v_true", "v_pred"])


def build_lg_sample_trace(
    model: SmartphoneBatteryModel,
    cycles: list[Path],
) -> pd.DataFrame:
    """Build a representative LG cycle trace with predictions.

    Args:
        model: Battery model instance.
        cycles: Candidate cycle file list.

    Returns:
        DataFrame with time, SOC, voltage, and optional temperature traces.
    """
    for file_path in cycles:
        try:
            data = load_lg_csv(file_path)
            if data.capacity_Ah is None:
                continue
            soc_true = compute_soc_from_capacity(data.capacity_Ah, model.params.Q_nom)
            power_mW = data.power_W * 1000.0

            def power_func(t: float) -> float:
                return float(np.interp(t, data.t_s, power_mW))

            sim = model.simulate(
                SOC_0=float(soc_true[0]),
                T_0=298.15,
                power_func=power_func,
                t_span=(0, float(data.t_s[-1])),
            )
            t_sim = sim["t"]
            soc_pred = np.interp(data.t_s, t_sim, sim["SOC"])
            v_pred = np.interp(data.t_s, t_sim, sim["V"])
            trace = pd.DataFrame(
                {
                    "file": str(file_path),
                    "t_s": data.t_s,
                    "soc_true": soc_true,
                    "soc_pred": soc_pred,
                    "v_true": data.voltage,
                    "v_pred": v_pred,
                }
            )
            if data.temperature_C is not None:
                temp_pred = np.interp(data.t_s, t_sim, sim["T"]) - 273.15
                trace["temp_true_C"] = data.temperature_C
                trace["temp_pred_C"] = temp_pred
            return trace
        except Exception:
            continue
    return pd.DataFrame()


def main() -> None:
    """Run validation pipeline and save outputs.

    Returns:
        None. Writes CSV/JSON outputs to the compare directory.
    """
    ensure_dirs()
    params = BatteryParams()
    model = SmartphoneBatteryModel(params)

    inventory = summarize_dataset_inventory()
    inventory.to_csv(COMPARE / "dataset_inventory.csv", index=False)

    ocv_metrics = validate_ocv(model)
    if ocv_metrics.empty:
        ocv_metrics = pd.DataFrame(columns=["file", "rmse_V", "mae_V", "max_err_V"])
    ocv_metrics.to_csv(COMPARE / "ocv_metrics.csv", index=False)

    cycles = list_lg_cycle_files()
    cycle_subset = cycles[:30]
    lg_metrics = validate_lg_cycles(model, cycle_subset)
    lg_metrics.to_csv(COMPARE / "lg_cycle_metrics.csv", index=False)

    pan_eis = validate_panasonic_eis()
    pan_eis.to_csv(COMPARE / "panasonic_eis_inventory.csv", index=False)

    uq_samples = validate_uncertainty(model)
    uq_samples.to_csv(COMPARE / "uncertainty_samples.csv", index=False)

    ocv_points = build_ocv_points(model)
    ocv_points.to_csv(COMPARE / "ocv_points.csv", index=False)

    lg_trace = build_lg_sample_trace(model, cycle_subset)
    lg_trace.to_csv(COMPARE / "lg_sample_trace.csv", index=False)

    rmse_v_mean = (
        float(lg_metrics["rmse_v"].mean()) if "rmse_v" in lg_metrics else None
    )
    rmse_temp_mean = (
        float(lg_metrics["rmse_temp_C"].mean()) if "rmse_temp_C" in lg_metrics else None
    )
    zreal_count = int(pan_eis["has_zreal"].sum()) if len(pan_eis) else 0
    zimag_count = int(pan_eis["has_zimag"].sum()) if len(pan_eis) else 0
    summary = {
        "ocv": {
            "count": int(len(ocv_metrics)),
            "rmse_V_mean": float(ocv_metrics["rmse_V"].mean()) if len(ocv_metrics) else None,
            "points": int(len(ocv_points)),
        },
        "lg_cycles": {
            "count": int(len(lg_metrics)),
            "rmse_soc_mean": float(lg_metrics["rmse_soc"].mean()) if len(lg_metrics) else None,
            "rmse_v_mean": rmse_v_mean,
            "rmse_temp_C_mean": rmse_temp_mean,
        },
        "panasonic_eis": {
            "count": int(len(pan_eis)),
            "has_zreal": zreal_count,
            "has_zimag": zimag_count,
        },
        "uncertainty": {
            "samples": int(len(uq_samples)),
        },
    }
    with open(COMPARE / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
