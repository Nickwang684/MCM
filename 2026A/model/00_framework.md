# 智能手机电池耗电模型：完整框架

> 智能手机电池连续时间建模 - 综合框架
>
> **2026年MCM问题A：智能手机电池耗电建模**

---

## 目录

- [1. 模型架构总览](#1-模型架构总览)
- [2. 完整状态空间模型](#2-完整状态空间模型)
- [3. 参数汇总表](#3-参数汇总表)
- [4. 求解方法](#4-求解方法)
- [5. 完整Python实现](#5-完整python实现)
- [6. 典型应用场景](#6-典型应用场景)
- [7. 模型验证](#7-模型验证)
- [8. 模型限制与扩展](#8-模型限制与扩展)
- [9. 灵敏度分析（06模块）](#9-灵敏度分析06模块)
- [10. 不确定性量化（07模块）](#10-不确定性量化07模块)
- [11. 用户建议与系统优化（08模块）](#11-用户建议与系统优化08模块)
- [12. 文件结构总结](#12-文件结构总结)
- [13. MCM题目要求对照](#13-mcm题目要求对照)
- [14. 参考文献总结](#14-参考文献总结)

## 1. 模型架构总览

### 1.1 系统框图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          用户使用场景输入                                │
│    (屏幕亮度、CPU利用率、网络模式、GPS状态、传感器状态等)                  │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     功耗分解模型 (02_power_model)                        │
│                                                                         │
│   P_total(t) = P_display + P_CPU + P_GPU + P_network + P_sensors + ...  │
│                                                                         │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │ P_total(t)
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  ┌──────────────────┐      I(t) = P(t)/V(t)      ┌──────────────────┐  │
│  │                  │◄─────────────────────────►│                  │  │
│  │   功耗-电流转换   │                           │   电池模型(01)   │  │
│  │                  │         V(t)              │   SOC动力学      │  │
│  └──────────────────┘◄──────────────────────────│   二阶ECM        │  │
│                                                  │                  │  │
│                                                  └────────┬─────────┘  │
│                                                           │            │
└───────────────────────────────────────────────────────────┼────────────┘
                                                            │
                         ┌──────────────────────────────────┼──────────┐
                         │                                  │          │
                         ▼                                  ▼          │
          ┌──────────────────────────┐      ┌──────────────────────────┐
          │    热模型 (03_thermal)   │      │   老化模型 (04_aging)    │
          │                          │      │                          │
          │   dT/dt = (Q_gen-Q_loss) │      │  dSOH/dt = -(cal + cyc)  │
          │          / (m*Cp)        │      │                          │
          └────────────┬─────────────┘      └────────────┬─────────────┘
                       │                                  │
                       │ T(t), R(T), Q_eff(T)            │ SOH, R_growth
                       │                                  │
                       └──────────────────────────────────┘
                                       │
                                       ▼
          ┌────────────────────────────────────────────────────────────┐
          │                 预测模型 (05_prediction)                   │
          │                                                            │
          │   t_empty = ∫[SOC→SOC_min] Q_eff / I(SOC) dSOC            │
          │                                                            │
          └────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
                              ┌─────────────────┐
                              │  剩余时间预测    │
                              │  t_empty [h]    │
                              │  置信区间       │
                              └─────────────────┘
```

### 1.2 模型层次

| 层次 | 模型 | 时间尺度 | 核心输出 |
|------|------|----------|----------|
| **第1层** | 电池模型 | 秒-分钟 | SOC(t), V(t) |
| **第1层** | 功耗模型 | 秒 | P(t), I(t) |
| **第2层** | 热模型 | 分钟-小时 | T(t), R(T) |
| **第3层** | 老化模型 | 天-年 | SOH(t) |
| **第4层** | 预测模型 | 分钟-小时 | t_empty |

---

## 2. 完整状态空间模型

### 2.1 状态变量

$$\mathbf{x}(t) = \begin{bmatrix} SOC(t) \\ V_{RC1}(t) \\ V_{RC2}(t) \\ T(t) \\ SOH(t) \end{bmatrix}$$

### 2.2 连续时间微分方程组

$$\boxed{
\begin{aligned}
\frac{dSOC}{dt} &= -\frac{I(t)}{Q_{nom} \cdot SOH \cdot 3600} \\[8pt]
\frac{dV_{RC1}}{dt} &= -\frac{V_{RC1}}{\tau_1(T)} + \frac{I(t)}{C_1} \\[8pt]
\frac{dV_{RC2}}{dt} &= -\frac{V_{RC2}}{\tau_2(T)} + \frac{I(t)}{C_2} \\[8pt]
\frac{dT}{dt} &= \frac{I^2 R(T,SOC) - h_{eff}A(T-T_{amb})}{mC_p} \\[8pt]
\frac{dSOH}{dt} &= -\dot{SOH}_{cal}(T, SOC) - \dot{SOH}_{cyc}(I, T, SOC)
\end{aligned}
}$$

### 2.3 代数约束

**电压方程**：
$$V(t) = V_{OC}(SOC, T) - I(t) \cdot R_0(T, SOC) \cdot f_R(SOH) - V_{RC1}(t) - V_{RC2}(t)$$

**电流方程**（隐式）：
$$I(t) = \frac{P_{total}(t)}{V(t)}$$

**功率-电流显式解**（二次近似）：
$$I = \frac{(V_{OC}-V_{RC1}-V_{RC2}) - \sqrt{(V_{OC}-V_{RC1}-V_{RC2})^2 - 4R_0P}}{2R_0}$$

**OCV模型**（平滑组合）：
$$V_{OC}(SOC, T) = (1-w) V_{poly}(SOC) + w V_{log}(SOC) + \frac{\partial V_{OC}}{\partial T}(T - T_{ref})$$

---

## 3. 参数汇总表

### 3.1 电池基本参数

| 参数 | 符号 | 典型值 | 单位 | 来源 |
|------|------|--------|------|------|
| 标称容量 | $Q_{nom}$ | 3.0 | Ah | 规格书 |
| 标称电压 | $V_{nom}$ | 3.8 | V | 规格书 |
| 截止电压 | $V_{min}$ | 3.0 | V | 规格书 |
| 最大电压 | $V_{max}$ | 4.35 | V | 规格书 |
| 欧姆内阻 | $R_0$ | 80 | mΩ | 测量/文献 |
| RC1电阻 | $R_1$ | 20 | mΩ | 辨识 |
| RC1电容 | $C_1$ | 2000 | F | 辨识 |
| RC2电阻 | $R_2$ | 10 | mΩ | 辨识 |
| RC2电容 | $C_2$ | 50000 | F | 辨识 |

### 3.2 OCV-SOC参数

| 参数 | 值 | 单位 |
|------|------|------|
| $K_0$ | 3.685 | V |
| $K_1$ | 0.2156 | V |
| $K_2$ | 0.0351 | V |
| $K_3$ | -0.0175 | V |
| $\partial V_{OC}/\partial T$ | -0.3 | mV/K |

### 3.3 热参数

| 参数 | 符号 | 典型值 | 单位 |
|------|------|--------|------|
| 电池质量 | $m$ | 50 | g |
| 比热容 | $C_p$ | 1000 | J/(kg·K) |
| 换热系数 | $h$ | 10 | W/(m²·K) |
| 表面积 | $A$ | 60 | cm² |
| 内阻活化能 | $E_{a,R}$ | 25 | kJ/mol |
| 参考温度 | $T_{ref}$ | 298.15 | K |
| 环境修正 | $h_{eff}$ | 见03模型 | - |

### 3.4 老化参数

| 参数 | 符号 | 典型值 | 单位 |
|------|------|--------|------|
| 日历老化系数 | $k_{cal}$ | 0.02 | %/√day |
| 循环老化系数 | $k_{cyc}$ | 0.02 | %/cycle |
| 日历活化能 | $E_{a,cal}$ | 60 | kJ/mol |
| 循环活化能 | $E_{a,cyc}$ | 40 | kJ/mol |
| DOD指数 | $\gamma$ | 2.0 | - |
| C-rate指数 | $\alpha$ | 0.7 | - |
| 内阻增长系数 | $k_R$ | 2.0 | - |

### 3.5 功耗参数

详见 `02_power_model.md` 中的完整功耗参数表。

---

## 4. 求解方法

### 4.1 数值积分

**推荐求解器**：
- **Python**: `scipy.integrate.solve_ivp` (RK45/BDF)
- **MATLAB**: `ode45` / `ode15s`

**时间步长选择**：
- 快动态（RC）：$\Delta t_{max} = \tau_1/10 \approx 4s$
- 慢动态（热）：$\Delta t_{max} = \tau_{th}/10 \approx 80s$
- 老化：$\Delta t = 1$ day

**自适应步长**：让求解器自动选择步长

### 4.2 代数环求解

电压-电流-功率形成代数环，需要迭代求解：

```python
def solve_algebraic_loop(P_load, SOC, T, V_RC1, V_RC2, params, tol=1e-6, max_iter=10):
    """
    求解电流-电压代数环
    """
    V_OC = ocv_model(SOC, T, params)
    R_total = params['R0'] * temp_factor(T, params) + params['R1'] + params['R2']
    
    # 初始猜测
    V = V_OC - V_RC1 - V_RC2
    
    for _ in range(max_iter):
        I = P_load / V / 1000  # mW to W, then to A
        V_new = V_OC - I * R_total - V_RC1 - V_RC2
        
        if abs(V_new - V) < tol:
            break
        V = V_new
    
    return I, V
```

### 4.4 EKF状态估计（在线SOC）

为提高长期SOC估计稳定性，加入EKF：

$$\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (y_k - h(\hat{x}_{k|k-1}, u_k))$$

其中$y_k$为端电压测量，$K_k$为卡尔曼增益（详见01模型）。

### 4.3 多时间尺度处理

老化模型与电-热模型时间尺度相差5-6个数量级，采用分离求解：

```
短期仿真（秒-小时）:
    1. 假设SOH恒定
    2. 求解电池-热耦合ODE
    3. 累积循环计数和平均温度

长期仿真（天-年）:
    1. 每天/每周更新SOH
    2. 使用平均工况条件
    3. 老化ODE积分
```

---

## 5. 完整Python实现

### 5.1 统一模型类

```python
import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass
from typing import Callable, Tuple, Dict

@dataclass
class BatteryParams:
    """电池参数数据类"""
    # 容量和电压
    Q_nom: float = 3.0      # Ah
    V_nom: float = 3.8      # V
    V_min: float = 3.0      # V
    V_max: float = 4.35     # V
    SOC_min: float = 0.05   # -
    
    # ECM参数
    R0: float = 0.080       # Ω
    R1: float = 0.020       # Ω
    C1: float = 2000        # F
    R2: float = 0.010       # Ω
    C2: float = 50000       # F
    
    # OCV参数
    K0: float = 3.685       # V
    K1: float = 0.2156      # V
    K2: float = 0.0351      # V
    K3: float = -0.0175     # V
    
    # 热参数
    m: float = 0.050        # kg
    Cp: float = 1000        # J/(kg·K)
    h: float = 10           # W/(m²·K)
    A: float = 0.006        # m²
    Ea_R: float = 25000     # J/mol
    T_ref: float = 298.15   # K
    
    # 老化参数
    k_cal: float = 2e-6     # 1/√s
    k_cyc: float = 2e-5     # 1/Ah
    Ea_cal: float = 60000   # J/mol
    Ea_cyc: float = 40000   # J/mol
    gamma: float = 2.0      # DOD指数
    alpha: float = 0.7      # C-rate指数
    k_R: float = 2.0        # 内阻增长系数

R_GAS = 8.314  # J/(mol·K)

class SmartphoneBatteryModel:
    """智能手机电池连续时间模型"""
    
    def __init__(self, params: BatteryParams = None):
        self.params = params or BatteryParams()
    
    def ocv(self, SOC: float, T: float = 298.15) -> float:
        """开路电压模型"""
        p = self.params
        SOC = np.clip(SOC, 0.01, 0.99)
        V_OC = p.K0 + p.K1 * SOC + p.K2 * np.log(SOC) + p.K3 * np.log(1 - SOC)
        # 温度修正
        V_OC += -0.0003 * (T - p.T_ref)
        return V_OC
    
    def resistance(self, T: float, SOC: float, SOH: float = 1.0) -> float:
        """温度和SOH依赖的内阻"""
        p = self.params
        # 温度修正 (Arrhenius)
        R_T = p.R0 * np.exp(-p.Ea_R / R_GAS * (1/T - 1/p.T_ref))
        # SOH修正
        R_SOH = R_T * (1 + p.k_R * (1 - SOH))
        return R_SOH
    
    def power_to_current(self, P_mW: float, SOC: float, T: float, 
                         V_RC1: float, V_RC2: float, SOH: float) -> Tuple[float, float]:
        """功率转换为电流（迭代求解）"""
        V_OC = self.ocv(SOC, T)
        R_total = self.resistance(T, SOC, SOH)
        
        # 迭代求解
        V = V_OC - V_RC1 - V_RC2
        for _ in range(5):
            I = P_mW / V / 1000  # mW -> A
            V = V_OC - I * R_total - V_RC1 - V_RC2
        
        return I, V
    
    def battery_ode(self, t: float, x: np.ndarray, 
                    power_func: Callable, T_amb: float = 298.15) -> np.ndarray:
        """
        电池状态微分方程
        
        状态: x = [SOC, V_RC1, V_RC2, T]
        """
        SOC, V_RC1, V_RC2, T = x
        p = self.params
        
        # 假设SOH恒定（短期仿真）
        SOH = 1.0
        
        # 获取功率
        P_load = power_func(t)
        
        # 计算电流和电压
        I, V = self.power_to_current(P_load, SOC, T, V_RC1, V_RC2, SOH)
        
        # 有效容量
        Q_eff = p.Q_nom * SOH * 3600  # As
        
        # SOC动力学
        dSOC = -I / Q_eff
        
        # RC动力学
        R1_T = p.R1 * np.exp(-p.Ea_R / R_GAS * (1/T - 1/p.T_ref))
        R2_T = p.R2 * np.exp(-p.Ea_R / R_GAS * (1/T - 1/p.T_ref))
        tau1 = R1_T * p.C1
        tau2 = R2_T * p.C2
        
        dV_RC1 = -V_RC1 / tau1 + I / p.C1
        dV_RC2 = -V_RC2 / tau2 + I / p.C2
        
        # 热动力学
        R_total = self.resistance(T, SOC, SOH)
        Q_gen = I**2 * R_total
        Q_loss = p.h * p.A * (T - T_amb)
        dT = (Q_gen - Q_loss) / (p.m * p.Cp)
        
        return np.array([dSOC, dV_RC1, dV_RC2, dT])
    
    def simulate(self, SOC_0: float, T_0: float, 
                 power_func: Callable, t_span: Tuple[float, float],
                 T_amb: float = 298.15) -> Dict:
        """
        运行仿真
        
        参数:
            SOC_0: 初始SOC
            T_0: 初始温度 [K]
            power_func: 功率函数 P(t) [mW]
            t_span: 时间区间 (t_start, t_end) [s]
            T_amb: 环境温度 [K]
        
        返回:
            包含时间、状态、电压等的字典
        """
        # 初始状态
        x0 = [SOC_0, 0.0, 0.0, T_0]
        
        # 定义ODE
        def ode(t, x):
            return self.battery_ode(t, x, power_func, T_amb)
        
        # 终止条件
        def soc_event(t, x):
            return x[0] - self.params.SOC_min
        soc_event.terminal = True
        soc_event.direction = -1
        
        # 求解
        sol = solve_ivp(ode, t_span, x0, method='RK45', 
                        events=soc_event, max_step=10.0)
        
        # 计算电压轨迹
        V_trajectory = []
        I_trajectory = []
        for i in range(len(sol.t)):
            SOC, V_RC1, V_RC2, T = sol.y[:, i]
            P = power_func(sol.t[i])
            I, V = self.power_to_current(P, SOC, T, V_RC1, V_RC2, 1.0)
            V_trajectory.append(V)
            I_trajectory.append(I)
        
        return {
            't': sol.t,
            'SOC': sol.y[0],
            'V_RC1': sol.y[1],
            'V_RC2': sol.y[2],
            'T': sol.y[3],
            'V': np.array(V_trajectory),
            'I': np.array(I_trajectory),
            't_empty': sol.t[-1] if sol.t_events[0].size > 0 else None
        }
    
    def predict_empty_time(self, SOC_0: float, P_load_mW: float, 
                           SOH: float = 1.0, T: float = 298.15) -> float:
        """
        快速预测耗尽时间
        """
        p = self.params
        Q_eff = p.Q_nom * SOH
        usable_SOC = SOC_0 - p.SOC_min
        V_avg = self.ocv((SOC_0 + p.SOC_min) / 2, T)
        
        energy_Wh = Q_eff * usable_SOC * V_avg
        P_W = P_load_mW / 1000
        
        t_hours = energy_Wh / P_W
        return t_hours * 3600  # 返回秒


# 使用示例
if __name__ == "__main__":
    # 创建模型
    model = SmartphoneBatteryModel()
    
    # 定义功率函数 (社交媒体场景: 1500mW)
    def power_social(t):
        return 1500  # mW
    
    # 运行仿真
    results = model.simulate(
        SOC_0=0.8,
        T_0=298.15,
        power_func=power_social,
        t_span=(0, 10*3600),  # 最多10小时
        T_amb=298.15
    )
    
    # 输出结果
    print(f"仿真结束时间: {results['t'][-1]/3600:.2f} 小时")
    print(f"最终SOC: {results['SOC'][-1]*100:.1f}%")
    print(f"最终温度: {results['T'][-1]-273.15:.1f}°C")
    if results['t_empty']:
        print(f"电量耗尽时间: {results['t_empty']/3600:.2f} 小时")
    
    # 快速估算
    t_quick = model.predict_empty_time(0.8, 1500)
    print(f"快速估算耗尽时间: {t_quick/3600:.2f} 小时")
```

### 5.2 MATLAB实现框架

```matlab
function results = smartphone_battery_simulation(SOC_0, T_0, P_load, t_span, params)
    % 智能手机电池仿真
    %
    % 输入:
    %   SOC_0: 初始SOC
    %   T_0: 初始温度 [K]
    %   P_load: 功率 [mW] 或函数句柄
    %   t_span: 时间区间 [s]
    %   params: 参数结构体
    
    % 默认参数
    if nargin < 5
        params = default_params();
    end
    
    % 初始状态 [SOC, V_RC1, V_RC2, T]
    x0 = [SOC_0; 0; 0; T_0];
    
    % 事件函数（SOC到达最小值）
    options = odeset('Events', @(t,x) soc_event(t, x, params.SOC_min));
    
    % 求解ODE
    [t, x] = ode45(@(t,x) battery_ode(t, x, P_load, params), t_span, x0, options);
    
    % 计算电压
    V = zeros(size(t));
    I = zeros(size(t));
    for i = 1:length(t)
        [I(i), V(i)] = power_to_current(P_load, x(i,1), x(i,4), x(i,2), x(i,3), 1.0, params);
    end
    
    % 输出结果
    results.t = t;
    results.SOC = x(:,1);
    results.V_RC1 = x(:,2);
    results.V_RC2 = x(:,3);
    results.T = x(:,4);
    results.V = V;
    results.I = I;
    results.t_empty = t(end);
end

function dxdt = battery_ode(t, x, P_load, params)
    % 电池ODE
    SOC = x(1);
    V_RC1 = x(2);
    V_RC2 = x(3);
    T = x(4);
    
    SOH = 1.0;
    
    % 功率
    if isa(P_load, 'function_handle')
        P = P_load(t);
    else
        P = P_load;
    end
    
    % 电流
    [I, V] = power_to_current(P, SOC, T, V_RC1, V_RC2, SOH, params);
    
    % 有效容量
    Q_eff = params.Q_nom * SOH * 3600;
    
    % SOC动力学
    dSOC = -I / Q_eff;
    
    % RC动力学
    R1_T = params.R1 * exp(-params.Ea_R / 8.314 * (1/T - 1/params.T_ref));
    tau1 = R1_T * params.C1;
    tau2 = params.R2 * params.C2;
    
    dV_RC1 = -V_RC1 / tau1 + I / params.C1;
    dV_RC2 = -V_RC2 / tau2 + I / params.C2;
    
    % 热动力学
    R_total = params.R0 * exp(-params.Ea_R / 8.314 * (1/T - 1/params.T_ref));
    Q_gen = I^2 * R_total;
    Q_loss = params.h * params.A * (T - params.T_amb);
    dT = (Q_gen - Q_loss) / (params.m * params.Cp);
    
    dxdt = [dSOC; dV_RC1; dV_RC2; dT];
end

function [value, isterminal, direction] = soc_event(t, x, SOC_min)
    value = x(1) - SOC_min;
    isterminal = 1;
    direction = -1;
end

function params = default_params()
    params.Q_nom = 3.0;
    params.R0 = 0.08;
    params.R1 = 0.02;
    params.C1 = 2000;
    params.R2 = 0.01;
    params.C2 = 50000;
    params.K0 = 3.685;
    params.K1 = 0.2156;
    params.K2 = 0.0351;
    params.K3 = -0.0175;
    params.m = 0.05;
    params.Cp = 1000;
    params.h = 10;
    params.A = 0.006;
    params.Ea_R = 25000;
    params.T_ref = 298.15;
    params.T_amb = 298.15;
    params.SOC_min = 0.05;
end
```

---

## 6. 典型应用场景

### 6.1 场景1：续航时间预测

**问题**：从80% SOC开始，在社交媒体场景下，预测剩余续航时间。

**输入**：
- SOC_0 = 0.8
- P_load = 1500 mW
- T_amb = 25°C
- SOH = 0.95

**求解**：
```python
model = SmartphoneBatteryModel()
t_empty = model.predict_empty_time(0.8, 1500, 0.95, 298.15)
print(f"预计续航: {t_empty/3600:.1f} 小时")
# 输出: 预计续航: 5.4 小时
```

### 6.2 场景2：混合使用场景

**问题**：模拟一天的典型使用模式

**使用模式**：
```python
def daily_power_profile(t):
    """每日功率曲线 (t in seconds)"""
    hour = (t / 3600) % 24
    
    if hour < 7:  # 0-7: 充电后待机
        return 50
    elif hour < 9:  # 7-9: 通勤
        return 1200
    elif hour < 12:  # 9-12: 办公
        return 800
    elif hour < 13:  # 12-13: 午餐
        return 1500
    elif hour < 18:  # 13-18: 办公
        return 800
    elif hour < 20:  # 18-20: 通勤+社交
        return 1500
    else:  # 20-24: 娱乐
        return 2000
```

### 6.3 场景3：温度影响分析

**问题**：分析0°C vs 25°C对续航的影响

**方法**：
```python
# 25°C
t_25 = model.predict_empty_time(1.0, 1500, 1.0, 298.15)

# 0°C（需要考虑温度对容量和内阻的影响）
# 容量下降到85%，内阻增加到2.2倍
model_cold = SmartphoneBatteryModel()
model_cold.params.Q_nom *= 0.85
model_cold.params.R0 *= 2.2
t_0 = model_cold.predict_empty_time(1.0, 1500, 1.0, 273.15)

print(f"25°C续航: {t_25/3600:.1f} h")
print(f"0°C续航: {t_0/3600:.1f} h ({t_0/t_25*100:.0f}%)")
```

---

## 7. 模型验证

### 7.1 验证策略

| 级别 | 验证内容 | 数据来源 | 指标 |
|------|----------|----------|------|
| 单元 | OCV-SOC关系 | 实验室测量 | RMSE < 10mV |
| 单元 | 内阻-温度关系 | EIS测量 | RMSE < 10% |
| 集成 | 放电曲线 | 恒流放电 | 电压RMSE < 30mV |
| 系统 | 续航时间 | 实际使用 | MAPE < 10% |

### 7.2 推荐验证数据集

1. **NASA PCoE Battery Dataset**：18650电池老化数据
2. **CALCE Battery Dataset**：动态工况测试
3. **3W's UCSD Dataset**：智能手机功耗测量

---

## 8. 模型限制与扩展

### 8.1 当前模型限制

1. **集总参数热模型**：无法捕捉电池内部温度分布
2. **简化老化模型**：未考虑详细的电化学老化机制
3. **恒定环境假设**：未考虑动态环境温度
4. **平均功耗假设**：未考虑功耗的瞬态尖峰

### 8.2 可能扩展

1. **高保真热模型**：采用1D/2D热模型
2. **详细电化学模型**：采用SPM或P2D模型
3. **自适应参数估计**：在线辨识参数
4. **机器学习增强**：用ML修正模型误差

---

## 9. 灵敏度分析（06模块）

### 9.1 核心方法

采用**Sobol全局灵敏度分析**量化各参数对续航的影响：

$$S_i = \frac{V_i}{Var(Y)}, \quad S_{Ti} = \frac{E[Var(Y|\theta_{\sim i})]}{Var(Y)}$$

### 9.2 关键发现

| 排名 | 参数 | 总效应 $S_T$ | 类型 |
|------|------|-------------|------|
| 1 | 标称容量 $Q_{nom}$ | ~0.35 | 电池属性 |
| 2 | 初始SOC | ~0.25 | 初始状态 |
| 3 | 屏幕亮度 | ~0.15 | **用户可控** |
| 4 | CPU负载 | ~0.12 | 使用模式 |
| 5 | SOH | ~0.10 | 电池状态 |

**意外发现**：GPS和内阻的影响出人意料地小（$S_T < 0.05$）。

详见 `06_sensitivity_analysis.md`。

---

## 10. 不确定性量化（07模块）

### 10.1 核心方法

采用**Monte Carlo传播**量化预测不确定性：

$$p(Y) = \int p(Y|\theta) \cdot p(\theta) d\theta$$

### 10.2 典型结果

| 场景 | 均值 | 95% 置信区间 | 变异系数 |
|------|------|-------------|----------|
| 轻度使用 | 12.5h | [9.8, 15.2]h | 18% |
| 中度使用 | 5.7h | [4.5, 7.0]h | 19% |
| 重度使用 | 2.8h | [2.2, 3.5]h | 20% |

**环境因素**：湿度与气压会改变散热与有效容量（弱影响但可用于最差情景评估）。

### 10.3 模型表现边界

**表现良好**：室温(15-35°C)、中等负载(20-70%)、SOH>80%

**表现不佳**：极端低温(<0°C)、极高负载(>90%)、SOH<75%

详见 `07_uncertainty_quantification.md`。

---

## 11. 用户建议与系统优化（08模块）

### 11.1 用户行为建议（按效果排序）

| 排名 | 行为 | 续航提升 | 难度 |
|------|------|----------|------|
| 1 | 屏幕亮度100%→30% | **+82%** | 易 |
| 2 | 开启深色模式 | **+28%** | 易 |
| 3 | 关闭位置服务 | +18% | 易 |
| 4 | 5G→4G | +15% | 易 |
| 5 | 关闭后台刷新 | +12% | 易 |

### 11.2 OS级优化策略

1. **自适应省电模式**：渐进式限制策略
2. **智能任务调度**：低电量延迟非必要任务
3. **预测性功率管理**：学习使用模式

### 11.3 电池寿命保护

- **推荐充电范围**：20%-80%（年均容量损失减少50%）
- **避免边充边用**：减少高温老化
- **优先慢充**：减少循环老化

详见 `08_recommendations.md`。

---

## 12. 文件结构总结

```
D:\jingsai\shumo\MCM\2026A\model\
├── 00_framework.md               # 本文档 - 完整框架整合
├── 01_battery_model.md           # 基础电池模型（SOC动力学+二阶ECM）
├── 02_power_model.md             # 功耗分解模型（各组件功耗）
├── 03_thermal_model.md           # 温度耦合模型（产热散热）
├── 04_aging_model.md             # 老化模型（日历+循环）
├── 05_prediction_model.md        # 耗尽时间预测
├── 06_sensitivity_analysis.md    # 灵敏度分析（Sobol/Morris）
├── 07_uncertainty_quantification.md  # 不确定性量化（Monte Carlo）
├── 08_recommendations.md         # 用户建议与系统优化
├── validation_code.py            # 验证代码
├── validation_code_v2.py         # 完整验证代码（含06-08模块）
└── validation_results.md         # 验证报告
```

---

## 13. MCM题目要求对照

| 题目要求 | 对应模块 | 完成状态 |
|---------|---------|---------|
| 连续时间数学模型 | 01-05 | ✅ |
| SOC作为时间函数 | 01 | ✅ |
| 预测电量耗尽时间 | 05 | ✅ |
| 识别快速耗电因素 | 06 | ✅ |
| 影响出人意料地小的因素 | 06 | ✅ |
| 量化不确定性 | 07 | ✅ |
| 预测置信区间 | 07 | ✅ |
| 用户行为建议 | 08 | ✅ |
| OS省电策略 | 08 | ✅ |
| 电池老化影响 | 04, 08 | ✅ |
| 推广至其他设备 | 08 | ✅ |

---

## 14. 参考文献总结

### 核心文献（必读）

| 编号 | 主题 | 贡献 |
|------|------|------|
| 277 | 连续时间建模 | SOC动力学、ECM方程 |
| 278 | 手机功耗 | 组件功耗分解 |
| 279 | 温度参数 | Arrhenius关系 |
| 280 | 耗尽预测 | 预测算法 |
| 141 | 热模型 | Bernardi方程 |
| 238 | 老化模型 | 通用老化框架 |
| 191 | OCV模型 | OCV-SOC关系 |
| 178 | 功耗测量 | UCSD实测数据 |

### 补充文献

详见 `model1.md` 中的完整文献排序。

### 灵敏度与不确定性分析文献

| 编号 | 主题 | 贡献 |
|------|------|------|
| Saltelli (2008) | Sobol方法 | 全局灵敏度分析 |
| Morris (1991) | Morris筛选 | 快速参数筛选 |
| Smith (2013) | 不确定性量化 | UQ理论框架 |

---

*文档版本: v2.0*
*更新时间: 2026年1月31日*
*项目: 2026年MCM问题A - 智能手机电池耗电建模*
*新增模块: 06灵敏度分析、07不确定性量化、08用户建议*
