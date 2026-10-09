from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Tuple

import numpy as np
from scipy.integrate import solve_ivp

R_GAS = 8.314  # J/(mol·K)


@dataclass
class BatteryParams:
    # Capacity & voltage
    Q_nom: float = 3.0  # Ah
    V_nom: float = 3.8  # V
    V_min: float = 3.0  # V
    V_max: float = 4.35  # V
    SOC_min: float = 0.05

    # ECM params
    R0: float = 0.080  # ohm
    R1: float = 0.020
    C1: float = 2000.0
    R2: float = 0.010
    C2: float = 50000.0

    # OCV params (log blend baseline)
    K0: float = 3.685
    K1: float = 0.2156
    K2: float = 0.0351
    K3: float = -0.0175

    # Thermal params
    m: float = 0.050  # kg
    Cp: float = 1000.0  # J/(kg·K)
    h: float = 10.0  # W/(m²·K)
    A: float = 0.006  # m²
    Ea_R: float = 25000.0  # J/mol
    T_ref: float = 298.15  # K

    # Environmental correction
    k_T: float = 0.01  # K^-1
    k_H: float = 0.002  # %^-1
    gamma_P: float = 0.3
    H_ref: float = 50.0  # %
    P_ref: float = 101.325  # kPa

    # Aging params
    k_cal: float = 2e-6  # 1/√s
    k_cyc: float = 2e-5  # 1/Ah
    Ea_cal: float = 60000.0
    Ea_cyc: float = 40000.0
    gamma: float = 2.0
    alpha: float = 0.7
    k_R: float = 2.0
    beta: float = 1.5
    k_win: float = 2.0
    SOC_avg: float = 0.65
    SOC_ref: float = 0.5


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


class SmartphoneBatteryModel:
    def __init__(self, params: BatteryParams | None = None):
        self.params = params or BatteryParams()

    def ocv(self, soc: np.ndarray | float, T: float = 298.15) -> np.ndarray:
        p = self.params
        soc = np.clip(soc, 0.01, 0.99)
        V_oc = p.K0 + p.K1 * soc + p.K2 * np.log(soc) + p.K3 * np.log(1 - soc)
        # Temperature correction
        V_oc = V_oc + -0.0003 * (T - p.T_ref)
        return V_oc

    def resistance(self, T: float, soc: float, soh: float = 1.0) -> float:
        p = self.params
        R_T = p.R0 * np.exp(-p.Ea_R / R_GAS * (1 / T - 1 / p.T_ref))
        R_SOH = R_T * (1 + p.k_R * (1 - soh))
        return R_SOH

    def power_to_current(self, P_mW: float, soc: float, T: float, V_RC1: float, V_RC2: float, soh: float) -> Tuple[float, float]:
        V_oc = self.ocv(soc, T)
        R_total = self.resistance(T, soc, soh)
        V = V_oc - V_RC1 - V_RC2
        for _ in range(8):
            I = P_mW / V / 1000.0
            V = V_oc - I * R_total - V_RC1 - V_RC2
        return I, V

    def battery_ode(self, t: float, x: np.ndarray, power_func: Callable[[float], float], T_amb: float = 298.15) -> np.ndarray:
        soc, V_RC1, V_RC2, T = x
        p = self.params
        soh = 1.0
        P_load = power_func(t)
        I, V = self.power_to_current(P_load, soc, T, V_RC1, V_RC2, soh)
        Q_eff = p.Q_nom * soh * 3600
        dSOC = -I / Q_eff
        R1_T = p.R1 * np.exp(-p.Ea_R / R_GAS * (1 / T - 1 / p.T_ref))
        R2_T = p.R2 * np.exp(-p.Ea_R / R_GAS * (1 / T - 1 / p.T_ref))
        tau1 = R1_T * p.C1
        tau2 = R2_T * p.C2
        dV_RC1 = -V_RC1 / tau1 + I / p.C1
        dV_RC2 = -V_RC2 / tau2 + I / p.C2
        R_total = self.resistance(T, soc, soh)
        Q_gen = I ** 2 * R_total - I * T * self.dVoc_dT(soc)
        Q_loss = self.h_eff(T_amb, 50.0, 101.325) * p.A * (T - T_amb)
        dT = (Q_gen - Q_loss) / (p.m * p.Cp)
        return np.array([dSOC, dV_RC1, dV_RC2, dT])

    def simulate(self, SOC_0: float, T_0: float, power_func: Callable[[float], float], t_span: Tuple[float, float], T_amb: float = 298.15) -> Dict[str, np.ndarray | float]:
        x0 = [SOC_0, 0.0, 0.0, T_0]

        def ode(t, x):
            return self.battery_ode(t, x, power_func, T_amb)

        def soc_event(t, x):
            return x[0] - self.params.SOC_min

        soc_event.terminal = True
        soc_event.direction = -1

        sol = solve_ivp(ode, t_span, x0, method="RK45", events=soc_event, max_step=10.0)
        V_traj = []
        I_traj = []
        for i in range(len(sol.t)):
            soc, V_RC1, V_RC2, T = sol.y[:, i]
            P = power_func(sol.t[i])
            I, V = self.power_to_current(P, soc, T, V_RC1, V_RC2, 1.0)
            V_traj.append(V)
            I_traj.append(I)

        return {
            "t": sol.t,
            "SOC": sol.y[0],
            "V_RC1": sol.y[1],
            "V_RC2": sol.y[2],
            "T": sol.y[3],
            "V": np.array(V_traj),
            "I": np.array(I_traj),
            "t_empty": sol.t[-1] if sol.t_events[0].size > 0 else None,
        }

    def predict_empty_time(self, SOC_0: float, P_load_mW: float, soh: float = 1.0, T: float = 298.15) -> float:
        p = self.params
        Q_eff = p.Q_nom * soh
        usable_soc = SOC_0 - p.SOC_min
        V_avg = float(self.ocv((SOC_0 + p.SOC_min) / 2, T))
        energy_Wh = Q_eff * usable_soc * V_avg
        P_W = P_load_mW / 1000.0
        t_hours = energy_Wh / P_W
        return t_hours * 3600

    def dVoc_dT(self, soc: float) -> float:
        a0, a1, a2 = 0.8, -1.5, 0.4
        return (a0 + a1 * soc + a2 * soc ** 2) * 1e-3

    def h_eff(self, T_amb: float, H: float, P_kPa: float) -> float:
        p = self.params
        f_T = 1 + p.k_T * (T_amb - p.T_ref)
        f_H = 1 - p.k_H * (H - p.H_ref)
        f_P = (P_kPa / p.P_ref) ** p.gamma_P
        return p.h * f_T * f_H * f_P


def aging_model_rate(t_s: float, soh: float, T: float, soc: float, current: float, params: BatteryParams) -> float:
    k_cal = params.k_cal * np.exp(-params.Ea_cal / (R_GAS * T))
    k_cyc = params.k_cyc * np.exp(-params.Ea_cyc / (R_GAS * T))
    f_soc = np.exp(params.beta * soc)
    t_eff = max(t_s, 1.0)
    dSOH_cal = -k_cal * f_soc / (2 * np.sqrt(t_eff))
    f_window = 1 + params.k_win * (params.SOC_avg - params.SOC_ref)
    dSOH_cyc = -k_cyc * f_window * abs(current) / (2 * params.Q_nom * max(soh, 1e-6) * 3600)
    return dSOH_cal + dSOH_cyc


def resistance_growth(soh: float, params: BatteryParams) -> float:
    return 1 + params.k_R * (1 - soh)


def monte_carlo_t_empty(model: SmartphoneBatteryModel, SOC_0: float, T: float, P_mW: float, n: int = 200, sigma_soc: float = 0.01, sigma_soh: float = 0.05) -> np.ndarray:
    rng = np.random.default_rng(42)
    t_samples = []
    for _ in range(n):
        soc = float(np.clip(SOC_0 + rng.normal(0, sigma_soc), 0.05, 0.99))
        soh = float(np.clip(1.0 + rng.normal(0, sigma_soh), 0.7, 1.0))
        t_samples.append(model.predict_empty_time(soc, P_mW, soh=soh, T=T))
    return np.array(t_samples)
