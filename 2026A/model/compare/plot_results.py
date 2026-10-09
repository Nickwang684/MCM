from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(r"D:\jingsai\shumo\MCM\2026A")
COMPARE = ROOT / "model" / "compare"
PLOTS = COMPARE / "plots"


def plot_ocv_metrics() -> None:
    try:
        df = pd.read_csv(COMPARE / "ocv_metrics.csv")
    except Exception:
        return
    if df.empty:
        return
    plt.figure(figsize=(8, 4))
    plt.plot(df["rmse_V"].to_numpy(), marker="o", linestyle="-")
    plt.title("OCV RMSE (V) by file")
    plt.xlabel("File index")
    plt.ylabel("RMSE (V)")
    plt.tight_layout()
    plt.savefig(PLOTS / "ocv_rmse.png", dpi=150)
    plt.close()


def plot_ocv_scatter() -> None:
    try:
        df = pd.read_csv(COMPARE / "ocv_points.csv")
    except Exception:
        return
    if df.empty:
        return
    plt.figure(figsize=(5, 5))
    plt.scatter(df["v_true"], df["v_pred"], s=6, alpha=0.5)
    vmin = float(min(df["v_true"].min(), df["v_pred"].min()))
    vmax = float(max(df["v_true"].max(), df["v_pred"].max()))
    plt.plot([vmin, vmax], [vmin, vmax], color="#333333", linestyle="--", linewidth=1)
    plt.title("OCV: measured vs predicted")
    plt.xlabel("Measured Voltage (V)")
    plt.ylabel("Predicted Voltage (V)")
    plt.tight_layout()
    plt.savefig(PLOTS / "ocv_scatter.png", dpi=150)
    plt.close()


def plot_ocv_curve_overlay() -> None:
    try:
        df = pd.read_csv(COMPARE / "ocv_points.csv")
    except Exception:
        return
    if df.empty:
        return
    bins = 50
    df = df.copy()
    df["soc_bin"] = pd.cut(df["soc"], bins=bins, labels=False, include_lowest=True)
    grouped = df.groupby("soc_bin", as_index=False).agg(
        soc=("soc", "mean"),
        v_true=("v_true", "mean"),
        v_pred=("v_pred", "mean"),
    )
    plt.figure(figsize=(6, 4))
    plt.plot(grouped["soc"], grouped["v_true"], label="Measured OCV")
    plt.plot(grouped["soc"], grouped["v_pred"], label="Predicted OCV", alpha=0.8)
    plt.title("OCV curve overlay")
    plt.xlabel("SOC")
    plt.ylabel("Voltage (V)")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(PLOTS / "ocv_curve_overlay.png", dpi=150)
    plt.close()


def plot_lg_soc_rmse() -> None:
    try:
        df = pd.read_csv(COMPARE / "lg_cycle_metrics.csv")
    except Exception:
        return
    if df.empty:
        return
    plt.figure(figsize=(8, 4))
    plt.plot(df["rmse_soc"].to_numpy(), marker="o", linestyle="-")
    plt.title("LG Cycle SOC RMSE")
    plt.xlabel("Cycle index")
    plt.ylabel("RMSE (SOC)")
    plt.tight_layout()
    plt.savefig(PLOTS / "lg_soc_rmse.png", dpi=150)
    plt.close()


def plot_lg_voltage_rmse() -> None:
    try:
        df = pd.read_csv(COMPARE / "lg_cycle_metrics.csv")
    except Exception:
        return
    if df.empty or "rmse_v" not in df.columns:
        return
    plt.figure(figsize=(8, 4))
    plt.plot(df["rmse_v"].to_numpy(), marker="o", linestyle="-")
    plt.title("LG Cycle Voltage RMSE")
    plt.xlabel("Cycle index")
    plt.ylabel("RMSE (V)")
    plt.tight_layout()
    plt.savefig(PLOTS / "lg_v_rmse.png", dpi=150)
    plt.close()


def plot_lg_sample_trace() -> None:
    try:
        df = pd.read_csv(COMPARE / "lg_sample_trace.csv")
    except Exception:
        return
    if df.empty:
        return
    has_temp = "temp_true_C" in df.columns and "temp_pred_C" in df.columns
    rows = 3 if has_temp else 2
    _, axes = plt.subplots(rows, 1, figsize=(9, 3 * rows), sharex=True)
    axes[0].plot(df["t_s"], df["soc_true"], label="SOC true")
    axes[0].plot(df["t_s"], df["soc_pred"], label="SOC pred", alpha=0.8)
    axes[0].set_ylabel("SOC")
    axes[0].legend(loc="best")
    axes[1].plot(df["t_s"], df["v_true"], label="V true")
    axes[1].plot(df["t_s"], df["v_pred"], label="V pred", alpha=0.8)
    axes[1].set_ylabel("Voltage (V)")
    axes[1].legend(loc="best")
    if has_temp:
        axes[2].plot(df["t_s"], df["temp_true_C"], label="Temp true")
        axes[2].plot(df["t_s"], df["temp_pred_C"], label="Temp pred", alpha=0.8)
        axes[2].set_ylabel("Temp (°C)")
        axes[2].legend(loc="best")
    axes[-1].set_xlabel("Time (s)")
    plt.tight_layout()
    plt.savefig(PLOTS / "lg_sample_trace.png", dpi=150)
    plt.close()


def plot_lg_temp_rmse() -> None:
    try:
        df = pd.read_csv(COMPARE / "lg_cycle_metrics.csv")
    except Exception:
        return
    if df.empty or "rmse_temp_C" not in df.columns:
        return
    temp = df["rmse_temp_C"].dropna()
    if temp.empty:
        return
    plt.figure(figsize=(8, 4))
    plt.plot(temp.to_numpy(), marker="o", linestyle="-")
    plt.title("LG Cycle Temperature RMSE")
    plt.xlabel("Cycle index")
    plt.ylabel("RMSE (°C)")
    plt.tight_layout()
    plt.savefig(PLOTS / "lg_temp_rmse.png", dpi=150)
    plt.close()


def plot_uncertainty_hist() -> None:
    try:
        df = pd.read_csv(COMPARE / "uncertainty_samples.csv")
    except Exception:
        return
    if df.empty:
        return
    plt.figure(figsize=(6, 4))
    plt.hist(df["t_empty_s"], bins=30, color="#4C78A8")
    plt.title("t_empty Monte Carlo samples")
    plt.xlabel("t_empty (s)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(PLOTS / "t_empty_hist.png", dpi=150)
    plt.close()


def plot_panasonic_eis_summary() -> None:
    try:
        df = pd.read_csv(COMPARE / "panasonic_eis_inventory.csv")
    except Exception:
        return
    if df.empty:
        return
    labels = ["has Zreal", "has Zimag"]
    counts = [int(df["has_zreal"].sum()), int(df["has_zimag"].sum())]
    plt.figure(figsize=(5, 4))
    plt.bar(labels, counts, color=["#59A14F", "#F28E2B"])
    plt.title("Panasonic EIS column availability")
    plt.ylabel("File count")
    plt.tight_layout()
    plt.savefig(PLOTS / "panasonic_eis_columns.png", dpi=150)
    plt.close()


def main() -> None:
    PLOTS.mkdir(exist_ok=True)
    plot_ocv_metrics()
    plot_ocv_scatter()
    plot_ocv_curve_overlay()
    plot_lg_soc_rmse()
    plot_lg_voltage_rmse()
    plot_lg_sample_trace()
    plot_lg_temp_rmse()
    plot_uncertainty_hist()
    plot_panasonic_eis_summary()


if __name__ == "__main__":
    main()
