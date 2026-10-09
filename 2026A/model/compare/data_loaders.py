"""Dataset loaders for LG/Panasonic/OCV sources."""
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TypeAlias, cast

import numpy as np
import numpy.typing as npt
import pandas as pd

FloatArray: TypeAlias = npt.NDArray[np.float64]
ObjectArray: TypeAlias = npt.NDArray[np.object_]


@dataclass
class BatterySeries:
    """Time-series container for battery measurements.

    Args:
        t_s: Time in seconds.
        voltage: Voltage array.
        current: Current array.
        temperature_C: Temperature in Celsius.
        capacity_Ah: Capacity in Ah.
        power_W: Power in Watts.
        meta: Metadata tags.
    """

    t_s: FloatArray
    voltage: FloatArray
    current: FloatArray
    temperature_C: FloatArray | None
    capacity_Ah: FloatArray | None
    power_W: FloatArray
    meta: dict[str, str]


def _find_header_line(path: Path, header_token: str = "Time Stamp") -> int:
    """Find the header line index in LG HG2 CSV files.

    Args:
        path: CSV file path.
        header_token: Header string indicating table start.

    Returns:
        Line index of the header row.

    Raises:
        ValueError: If the header token is not found.
    """
    with path.open("r", encoding="latin-1", errors="ignore") as f:
        for idx, line in enumerate(f):
            if line.strip().startswith(header_token):
                return idx
    raise ValueError(f"Header token '{header_token}' not found in {path}")


def _parse_time_to_seconds(
    series: pd.Series,
) -> FloatArray:
    """Parse HH:MM:SS(.ms) strings into seconds.

    Args:
        series: Pandas Series containing time strings.

    Returns:
        NumPy array of seconds.
    """
    # Accept formats like HH:MM:SS or HH:MM:SS.mmm
    values: ObjectArray = cast(
        ObjectArray, series.to_numpy(dtype=object)
    )

    def parse_one(val: str | float | object) -> float:
        if pd.isna(val):
            return np.nan
        s = str(val).strip()
        if not s:
            return np.nan
        parts = s.split(":")
        if len(parts) != 3:
            return np.nan
        h = float(parts[0])
        m = float(parts[1])
        sec = float(parts[2])
        return h * 3600 + m * 60 + sec

    return cast(FloatArray, np.array([parse_one(val) for val in values], dtype=np.float64))


def load_lg_csv(path: Path) -> BatterySeries:
    """Load LG HG2 CSV file with embedded metadata headers.

    Args:
        path: CSV file path.

    Returns:
        BatterySeries containing parsed measurements.

    Raises:
        ValueError: If a required header token is missing.
    """
    header_idx = _find_header_line(path, "Time Stamp")
    df: pd.DataFrame = pd.read_csv(
        path,
        skiprows=header_idx,
        encoding="latin-1",
        low_memory=False,
    )
    # Drop unit row if present
    if (
        df.iloc[0]
        .astype(str)
        .str.contains(r"\[V\]|\[A\]|\[C\]", regex=True)
        .any()
    ):
        df = df.iloc[1:].reset_index(drop=True)

    for col in df.columns:
        if col not in [
            "Time Stamp",
            "Step",
            "Status",
            "Prog Time",
            "Step Time",
            "Procedure",
        ]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "Step Time" in df.columns:
        t_s = _parse_time_to_seconds(df["Step Time"])
    elif "Prog Time" in df.columns:
        t_s = _parse_time_to_seconds(df["Prog Time"])
    else:
        t_s = np.arange(len(df), dtype=np.float64)

    if "Voltage" not in df.columns or "Current" not in df.columns:
        raise ValueError("LG file missing Voltage or Current columns")
    voltage: FloatArray = cast(FloatArray, df["Voltage"].to_numpy(dtype=np.float64))
    current: FloatArray = cast(FloatArray, df["Current"].to_numpy(dtype=np.float64))
    temperature_C: FloatArray | None
    if "Temperature" in df.columns:
        temperature_C = cast(FloatArray, df["Temperature"].to_numpy(dtype=np.float64))
    else:
        temperature_C = None

    capacity_Ah: FloatArray | None
    if "Capacity" in df.columns:
        capacity_Ah = cast(FloatArray, df["Capacity"].to_numpy(dtype=np.float64))
    else:
        capacity_Ah = None

    if "Power" in df.columns:
        power_W: FloatArray = cast(FloatArray, df["Power"].to_numpy(dtype=np.float64))
    else:
        power_W = voltage * current

    return BatterySeries(
        t_s=t_s,
        voltage=voltage,
        current=current,
        temperature_C=temperature_C,
        capacity_Ah=capacity_Ah,
        power_W=power_W,
        meta={"source": "LG_HG2"},
    )


def load_panasonic_csv(path: Path) -> BatterySeries:
    """Load Panasonic PF CSV file.

    Args:
        path: CSV file path.

    Returns:
        BatterySeries containing parsed measurements.

    Raises:
        ValueError: If required numeric columns are missing.
    """
    df: pd.DataFrame = pd.read_csv(path, encoding="latin-1")
    for col in df.columns:
        if col not in ["TimeStamp", "Time"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "Time" in df.columns:
        t_s = df["Time"].to_numpy(dtype=np.float64)
    else:
        t_s = np.arange(len(df), dtype=np.float64)

    if "Voltage" not in df.columns or "Current" not in df.columns:
        raise ValueError("Panasonic file missing Voltage or Current columns")
    voltage: FloatArray = cast(FloatArray, df["Voltage"].to_numpy(dtype=np.float64))
    current: FloatArray = cast(FloatArray, df["Current"].to_numpy(dtype=np.float64))
    temperature_C: FloatArray | None
    if "Battery_Temp_degC" in df.columns:
        temperature_C = cast(
            FloatArray, df["Battery_Temp_degC"].to_numpy(dtype=np.float64)
        )
    elif "Temp" in df.columns:
        temperature_C = cast(FloatArray, df["Temp"].to_numpy(dtype=np.float64))
    else:
        temperature_C = None

    capacity_Ah: FloatArray | None
    if "Ah" in df.columns:
        capacity_Ah = cast(FloatArray, df["Ah"].to_numpy(dtype=np.float64))
    else:
        capacity_Ah = None

    if "Power" in df.columns:
        power_W: FloatArray = cast(FloatArray, df["Power"].to_numpy(dtype=np.float64))
    else:
        power_W = voltage * current

    return BatterySeries(
        t_s=t_s,
        voltage=voltage,
        current=current,
        temperature_C=temperature_C,
        capacity_Ah=capacity_Ah,
        power_W=power_W,
        meta={"source": "Panasonic"},
    )


def _select_ocv_sheet(xls: pd.ExcelFile) -> str:
    """Select the sheet that contains OCV measurement data.

    Args:
        xls: Parsed Excel file handle.

    Returns:
        Sheet name with voltage/current columns.
    """
    for sheet_name in xls.sheet_names:
        try:
            sample: pd.DataFrame = pd.read_excel(
                xls, sheet_name=sheet_name, nrows=1
            )
        except Exception:
            continue
        columns = [str(col).lower() for col in sample.columns]
        has_voltage = any("voltage" in col for col in columns)
        has_current = any("current" in col for col in columns)
        if has_voltage and has_current:
            return str(sheet_name)
    return str(xls.sheet_names[0])


def load_ocv_excel(path: Path) -> pd.DataFrame:
    """Load OCV Excel file, selecting the data sheet when needed.

    Args:
        path: Excel file path.

    Returns:
        DataFrame with OCV data.

    Raises:
        ValueError: If the Excel file cannot be parsed.
    """
    xls = pd.ExcelFile(path)
    sheet_name = _select_ocv_sheet(xls)
    return pd.read_excel(xls, sheet_name=sheet_name)


def compute_soc_from_capacity(
    capacity_Ah: FloatArray,
    Q_nom: float,
) -> FloatArray:
    """Compute SOC from capacity trace.

    Args:
        capacity_Ah: Capacity trace in Ah.
        Q_nom: Nominal capacity in Ah.

    Returns:
        SOC array in [0, 1] assuming discharge capacity increases with time.

    Raises:
        ValueError: If capacity data is missing.
    """
    cap = capacity_Ah.astype(float)
    cap = cap - np.nanmin(cap)
    soc = 1.0 - cap / Q_nom
    return np.clip(soc, 0.0, 1.0)


def list_lg_files(root: Path, pattern: str) -> list[Path]:
    """List LG files by glob pattern.

    Args:
        root: Root directory to search.
        pattern: Glob pattern (e.g., "*UDDS*.csv").

    Returns:
        Sorted list of matching file paths.
    """
    return sorted(root.rglob(pattern))


def list_panasonic_files(root: Path, pattern: str) -> list[Path]:
    """List Panasonic files by glob pattern.

    Args:
        root: Root directory to search.
        pattern: Glob pattern (e.g., "*EIS*.csv").

    Returns:
        Sorted list of matching file paths.
    """
    return sorted(root.rglob(pattern))
