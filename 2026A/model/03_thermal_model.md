# 温度耦合模型：热动力学与参数温度依赖

> 智能手机电池连续时间建模 - 第3部分
>
> **核心目标**：建立电池温度T(t)的微分方程，描述产热-散热平衡及参数温度依赖性

---

## 目录

- [1. 模型概述](#1-模型概述)
- [2. 热动力学方程](#2-热动力学方程)
  - [2.1 能量守恒基本方程](#21-能量守恒基本方程)
  - [2.2 Bernardi产热方程](#22-bernardi产热方程)
  - [2.3 熵变系数](#23-熵变系数)
  - [2.4 散热方程](#24-散热方程)
  - [2.5 环境因子对换热系数的影响](#25-环境因子对换热系数的影响)
- [3. 完整热模型](#3-完整热模型)
- [4. 参数温度依赖性](#4-参数温度依赖性)
- [5. 温度-Peukert耦合](#5-温度-peukert耦合)
- [6. 智能手机热环境特殊考虑](#6-智能手机热环境特殊考虑)
- [7. 完整热模型总结](#7-完整热模型总结)
- [8. 与其他子模型的接口](#8-与其他子模型的接口)
- [9. 数值实现](#9-数值实现)
- [10. 模型验证](#10-模型验证)
- [参考文献](#参考文献)

## 1. 模型概述

### 1.1 建模目标

将电池温度建模为时间的连续函数：

$$T(t): [0, \infty) \rightarrow \mathbb{R}^+$$

**输入**：
- 放电电流 $I(t)$ [A]
- 端电压 $V(t)$ [V]
- 环境温度 $T_{amb}(t)$ [K]
- SOC状态 $SOC(t)$ [-]

**输出**：
- 电池温度 $T(t)$ [K]
- 温度修正后的电池参数

### 1.2 热模型选择

采用**集总参数热模型(0D Lumped Model)**：

| 特性 | 集总模型(0D) | 分布参数(3D) |
|------|-------------|--------------|
| 计算复杂度 | O(1) | O(n³) |
| 参数数量 | 3-5 | 20+ |
| 空间分辨率 | 无（平均温度） | 有 |
| 适用性 | ✓ 智能手机小电池 | 大型电池包 |

**文献依据**：论文141（电化学-热耦合综述）、论文279（温度依赖参数）

---

## 2. 热动力学方程

### 2.1 能量守恒基本方程

$$\boxed{mC_p\frac{dT(t)}{dt} = \dot{Q}_{gen}(t) - \dot{Q}_{loss}(t)}$$

**符号定义**：

| 符号 | 含义 | 单位 | 典型值 |
|------|------|------|--------|
| $m$ | 电池质量 | kg | 0.040-0.060 |
| $C_p$ | 比热容 | J/(kg·K) | 800-1200 |
| $T(t)$ | 电池温度 | K | 273-333 |
| $\dot{Q}_{gen}$ | 产热速率 | W | 0-10 |
| $\dot{Q}_{loss}$ | 散热速率 | W | 0-5 |

### 2.2 Bernardi产热方程

电池产热由多项组成：

$$\boxed{\dot{Q}_{gen}(t) = \dot{Q}_{irr}(t) + \dot{Q}_{rev}(t)}$$

**不可逆热（焦耳热）**：
$$\dot{Q}_{irr}(t) = I(t)^2 \cdot R_{total}(T, SOC)$$

**可逆热（熵变热）**：
$$\dot{Q}_{rev}(t) = I(t) \cdot T(t) \cdot \frac{\partial V_{OC}}{\partial T}$$

**完整Bernardi方程**：
$$\dot{Q}_{gen} = I \cdot (V_{OC} - V) + I \cdot T \cdot \frac{\partial V_{OC}}{\partial T}$$

简化为：
$$\dot{Q}_{gen} = I^2 R_{total} - I \cdot T \cdot \frac{\partial V_{OC}}{\partial T}$$

### 2.3 熵变系数

OCV温度系数 $\frac{\partial V_{OC}}{\partial T}$ 随SOC变化：

| SOC | $\frac{\partial V_{OC}}{\partial T}$ [mV/K] | 说明 |
|-----|-------------------------------------------|------|
| 0.1 | +0.5 ~ +1.0 | 吸热(放电时冷却) |
| 0.3 | -0.1 ~ +0.2 | 近乎等温 |
| 0.5 | -0.2 ~ -0.1 | 轻微放热 |
| 0.7 | -0.3 ~ -0.2 | 放热 |
| 0.9 | -0.4 ~ -0.2 | 放热 |

**多项式拟合**：
$$\frac{\partial V_{OC}}{\partial T}(SOC) = a_0 + a_1 \cdot SOC + a_2 \cdot SOC^2$$

**NMC电池参数**：
- $a_0 = 0.8$ mV/K
- $a_1 = -1.5$ mV/K
- $a_2 = 0.4$ mV/K

### 2.4 散热方程

牛顿冷却定律：

$$\boxed{\dot{Q}_{loss}(t) = hA(T(t) - T_{amb}(t))}$$

其中：
- $h$：等效对流换热系数 [W/(m²·K)]
- $A$：散热表面积 [m²]

**智能手机电池散热参数**：

| 参数 | 符号 | 典型值 | 范围 | 单位 |
|------|------|--------|------|------|
| 换热系数 | $h$ | 10 | 5-20 | W/(m²·K) |
| 表面积 | $A$ | 0.006 | 0.004-0.01 | m² |
| 热阻 | $R_{th}=1/(hA)$ | 16.7 | 10-50 | K/W |
| 热时间常数 | $\tau_{th}$ | 500-1000 | - | s |

**热时间常数**：
$$\tau_{th} = \frac{mC_p}{hA}$$

### 2.5 环境因子对换热系数的影响

> **为什么要引入环境因子？**
>
> 题目要求考虑温度、湿度、气压等环境因素。它们影响自然对流与蒸发散热，
> 进而改变有效换热系数$h$，导致热模型偏差。[文献148]

采用经验修正：

$$h_{eff}(t) = h_0 \cdot f_T(T_{amb}) \cdot f_H(H) \cdot f_P(P)$$
\tag{2.5-1}

其中：

$$f_T(T_{amb}) = 1 + k_T(T_{amb}-T_{ref})$$
$$f_H(H) = 1 - k_H\,(H-H_{ref})$$
$$f_P(P) = \left(\frac{P}{P_{ref}}\right)^{\gamma}$$
\tag{2.5-2}

**建议参数**：

- $k_T=0.01\,\mathrm{K^{-1}}$（环境升温增强对流）
- $k_H=0.002\,\mathrm{\%^{-1}}$（湿度升高降低蒸发散热）
- $\gamma \approx 0.3$（气压升高增强对流）

将$h$替换为$h_{eff}$：

$$\dot{Q}_{loss}(t) = h_{eff}(t)A\,(T-T_{amb})$$
\tag{2.5-3}

> **注**：湿度影响在手机内部电池上较弱，但在高湿环境下外壳散热会减弱，可作为敏感性分析参数。

---

## 3. 完整热模型

### 3.1 微分方程

$$\boxed{\frac{dT(t)}{dt} = \frac{1}{mC_p}\left[I(t)^2 R_{total}(T, SOC) - I(t) \cdot T \cdot \frac{\partial V_{OC}}{\partial T} - h_{eff}(t)A(T - T_{amb})\right]}$$

### 3.2 简化形式

忽略可逆热（对于中等SOC区间）：

$$\frac{dT(t)}{dt} = \frac{I(t)^2 R_{total}}{mC_p} - \frac{T - T_{amb}}{\tau_{th}}$$

其中 $\tau_{th} = \frac{mC_p}{hA}$

### 3.3 稳态温升

在恒定电流下，稳态温度：

$$T_{ss} = T_{amb} + \frac{I^2 R_{total}}{hA}$$

**温升估算**：

| 放电电流 | 功耗(R=80mΩ) | 稳态温升 |
|----------|--------------|----------|
| 0.5 A | 0.02 W | ~0.3 K |
| 1.0 A | 0.08 W | ~1.3 K |
| 2.0 A | 0.32 W | ~5.3 K |
| 3.0 A | 0.72 W | ~12 K |

---

## 4. 参数温度依赖性

### 4.1 Arrhenius关系

电化学过程速率遵循Arrhenius定律：

$$k(T) = A \cdot \exp\left(-\frac{E_a}{RT}\right)$$

对于电池参数，表示为相对于参考温度的变化：

$$\boxed{\xi(T) = \xi_{ref} \cdot \exp\left[-\frac{E_a}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]}$$

### 4.2 内阻温度依赖

$$\boxed{R(T) = R_{ref} \cdot \exp\left[-\frac{E_{a,R}}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]}$$

**参数**：

| 参数 | 值 | 单位 |
|------|------|------|
| $R_{ref}$ | 80 | mΩ |
| $E_{a,R}$ | 20-30 | kJ/mol |
| $T_{ref}$ | 298.15 | K (25°C) |
| $R$ (气体常数) | 8.314 | J/(mol·K) |

**温度-内阻对照表**：

| 温度 [°C] | 温度 [K] | $R/R_{ref}$ | 内阻 [mΩ] |
|-----------|----------|-------------|-----------|
| -10 | 263 | 3.16 | 253 |
| 0 | 273 | 2.15 | 172 |
| 10 | 283 | 1.51 | 121 |
| 20 | 293 | 1.10 | 88 |
| 25 | 298 | 1.00 | 80 |
| 30 | 303 | 0.87 | 70 |
| 40 | 313 | 0.67 | 54 |
| 50 | 323 | 0.53 | 42 |

### 4.3 容量温度依赖

有效容量随温度变化：

$$\boxed{Q_{eff}(T) = Q_{nom} \cdot f_T(T)}$$

**温度修正因子**：

$$f_T(T) = 1 - k_{cap,low} \cdot \max(0, T_{low} - T) - k_{cap,high} \cdot \max(0, T - T_{high})$$

简化Arrhenius形式：
$$f_T(T) = \exp\left[-\frac{E_{a,Q}}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]$$

**温度-容量对照表**：

| 温度 [°C] | 相对容量 $Q/Q_{nom}$ |
|-----------|----------------------|
| -20 | 0.50-0.60 |
| -10 | 0.70-0.80 |
| 0 | 0.85-0.90 |
| 10 | 0.93-0.97 |
| 20 | 0.98-1.00 |
| 25 | 1.00 |
| 35 | 1.00-1.02 |
| 45 | 0.98-1.00 |

### 4.4 扩散系数温度依赖

固相扩散系数：

$$D_s(T) = D_{s,ref} \cdot \exp\left[-\frac{E_{a,D}}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]$$

**参数**：$E_{a,D} = 30-50$ kJ/mol

### 4.5 交换电流密度

$$i_0(T) = i_{0,ref} \cdot \exp\left[-\frac{E_{a,i}}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]$$

**参数**：$E_{a,i} = 40-80$ kJ/mol

---

## 5. 温度-Peukert耦合

### 5.1 温度扩展Peukert方程

Peukert指数随温度变化：

$$\boxed{n(T) = n_{ref} + k_n \cdot (T_{ref} - T)}$$

**参数**：
- $n_{ref} = 1.02$（25°C时锂电池）
- $k_n = 0.001$ K⁻¹

低温时Peukert效应增强（$n$增大），高倍率放电损失更大。

### 5.2 有效容量综合模型

$$Q_{eff}(I, T) = Q_{nom} \cdot SOH \cdot f_T(T) \cdot \left(\frac{I_{nom}}{I}\right)^{n(T)-1}$$

**文献依据**：论文122（Peukert温度依赖性JPS）

---

## 6. 智能手机热环境特殊考虑

### 6.1 外壳热阻

电池到环境的热传递经过手机外壳：

$$\frac{dT_{battery}}{dt} = \frac{1}{mC_p}\left[\dot{Q}_{gen} - \frac{T_{battery} - T_{case}}{R_{th,1}}\right]$$

$$\frac{dT_{case}}{dt} = \frac{1}{m_{case}C_{p,case}}\left[\frac{T_{battery} - T_{case}}{R_{th,1}} - \frac{T_{case} - T_{amb}}{R_{th,2}}\right]$$

简化为单节点时：
$$R_{th,total} = R_{th,1} + R_{th,2}$$

### 6.2 SoC产热贡献

手机中SoC(处理器)是主要热源，会加热电池：

$$\dot{Q}_{total} = \dot{Q}_{battery} + \eta_{coupling} \cdot P_{SoC}$$

其中 $\eta_{coupling} \approx 0.1-0.3$（热耦合系数）

### 6.3 使用场景热特性

| 场景 | 电池产热 [W] | SoC产热 [W] | 总热负荷 [W] | 预期温升 |
|------|--------------|-------------|--------------|----------|
| 待机 | 0.01 | 0.05 | 0.06 | < 1 K |
| 浏览 | 0.05 | 0.3 | 0.35 | 2-3 K |
| 视频 | 0.08 | 0.5 | 0.58 | 4-6 K |
| 游戏 | 0.3 | 2.0 | 2.3 | 15-25 K |
| 充电 | 1.5 | 0.1 | 1.6 | 10-15 K |

---

## 7. 完整热模型总结

### 7.1 微分方程组

$$\boxed{
\begin{aligned}
\frac{dT(t)}{dt} &= \frac{1}{mC_p}\left[I^2 R(T, SOC) - I \cdot T \cdot \frac{\partial V_{OC}}{\partial T}(SOC) - hA(T - T_{amb})\right] \\[10pt]
R(T) &= R_{ref} \cdot \exp\left[-\frac{E_{a,R}}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right] \\[10pt]
Q_{eff}(T) &= Q_{nom} \cdot SOH \cdot \exp\left[-\frac{E_{a,Q}}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]
\end{aligned}
}$$

### 7.2 参数汇总

**智能手机电池热参数**：

| 参数 | 符号 | 典型值 | 单位 |
|------|------|--------|------|
| 电池质量 | $m$ | 0.050 | kg |
| 比热容 | $C_p$ | 1000 | J/(kg·K) |
| 热容量 | $mC_p$ | 50 | J/K |
| 换热系数 | $h$ | 10 | W/(m²·K) |
| 表面积 | $A$ | 0.006 | m² |
| 热导 | $hA$ | 0.06 | W/K |
| 热时间常数 | $\tau_{th}$ | 833 | s (~14min) |
| 内阻活化能 | $E_{a,R}$ | 25 | kJ/mol |
| 容量活化能 | $E_{a,Q}$ | 15 | kJ/mol |
| 参考温度 | $T_{ref}$ | 298.15 | K (25°C) |

### 7.3 初始条件

$$T(0) = T_{amb}(0)$$

### 7.4 约束条件

$$T_{min} \leq T(t) \leq T_{max}$$

- $T_{min} = 273K$ (0°C)：低温保护
- $T_{max} = 333K$ (60°C)：高温保护

---

## 8. 与其他子模型的接口

| 接口 | 方向 | 变量 | 来源/去向 |
|------|------|------|-----------|
| 输入 | ← | $I(t)$ | 功耗模型(02) → 电池模型(01) |
| 输入 | ← | $V(t)$ | 电池模型(01) |
| 输入 | ← | $SOC(t)$ | 电池模型(01) |
| 输入 | ← | $P_{SoC}(t)$ | 功耗模型(02) |
| 输入 | ← | $T_{amb}(t)$ | 环境条件 |
| 输出 | → | $T(t)$ | 电池模型(01) |
| 输出 | → | $R(T)$ | 电池模型(01) |
| 输出 | → | $Q_{eff}(T)$ | 电池模型(01) |

---

## 9. 数值实现

### 9.1 Python实现

```python
import numpy as np

# 物理常数
R_gas = 8.314  # J/(mol·K)

def thermal_model(t, T, I, V, SOC, T_amb, params):
    """
    热模型微分方程
    
    输入:
        T: 电池温度 [K]
        I: 放电电流 [A]
        V: 端电压 [V]
        SOC: 荷电状态 [-]
        T_amb: 环境温度 [K]
        params: 热参数字典
    
    输出:
        dT/dt [K/s]
    """
    # 温度依赖内阻
    R_total = params['R_ref'] * np.exp(
        -params['Ea_R'] / R_gas * (1/T - 1/params['T_ref'])
    )
    
    # 熵变系数 dVoc/dT
    dVoc_dT = (params['a0'] + params['a1']*SOC + params['a2']*SOC**2) * 1e-3  # mV/K -> V/K
    
    # 产热
    Q_irr = I**2 * R_total  # 不可逆热 (焦耳热)
    Q_rev = -I * T * dVoc_dT  # 可逆热 (熵变热)
    Q_gen = Q_irr + Q_rev
    
    # 环境修正换热系数
    f_T = 1 + params['k_T'] * (T_amb - params['T_ref'])
    f_H = 1 - params['k_H'] * (params['humidity'] - params['H_ref'])
    f_P = (params['pressure'] / params['P_ref']) ** params['gamma']
    h_eff = params['h'] * f_T * f_H * f_P

    # 散热
    Q_loss = h_eff * params['A'] * (T - T_amb)
    
    # 温度变化率
    dT_dt = (Q_gen - Q_loss) / (params['m'] * params['Cp'])
    
    return dT_dt

def temperature_dependent_resistance(T, params):
    """计算温度依赖内阻"""
    return params['R_ref'] * np.exp(
        -params['Ea_R'] / R_gas * (1/T - 1/params['T_ref'])
    )

def temperature_dependent_capacity(T, params):
    """计算温度依赖容量"""
    return params['Q_nom'] * params['SOH'] * np.exp(
        -params['Ea_Q'] / R_gas * (1/T - 1/params['T_ref'])
    )

# 默认参数
THERMAL_PARAMS = {
    'm': 0.050,          # kg
    'Cp': 1000,          # J/(kg·K)
    'h': 10,             # W/(m²·K)
    'A': 0.006,          # m²
    'R_ref': 0.080,      # Ω
    'Ea_R': 25000,       # J/mol
    'Ea_Q': 15000,       # J/mol
    'T_ref': 298.15,     # K
    'Q_nom': 3.0,        # Ah
    'SOH': 1.0,          # -
    'a0': 0.8,           # mV/K
    'a1': -1.5,          # mV/K
    'a2': 0.4,           # mV/K
    'k_T': 0.01,          # K^-1
    'k_H': 0.002,         # %^-1
    'gamma': 0.3,         # -
    'humidity': 50,       # %
    'pressure': 101325,   # Pa
    'H_ref': 50,          # %
    'P_ref': 101325,      # Pa
}
```

### 9.2 耦合求解框架

```python
from scipy.integrate import solve_ivp

def coupled_battery_thermal_model(t, y, scenario, params):
    """
    电池-热耦合模型
    
    状态向量: y = [SOC, V_RC1, V_RC2, T]
    """
    SOC, V_RC1, V_RC2, T = y
    
    # 获取温度依赖参数
    R0 = temperature_dependent_resistance(T, params)
    Q_eff = temperature_dependent_capacity(T, params)
    
    # 计算功耗和电流
    P_total = power_model(t, scenario, params)
    
    # 迭代计算电压和电流
    V_OC = ocv_model(SOC, T, params)
    V = V_OC - V_RC1 - V_RC2  # 初始估计
    for _ in range(3):  # 迭代收敛
        I = P_total / V / 1000  # mW -> W, V -> A
        V = V_OC - I * R0 - V_RC1 - V_RC2
    
    # 电池模型微分方程
    dSOC = -I / (Q_eff * 3600)
    dV_RC1 = -V_RC1 / (params['R1'] * params['C1']) + I / params['C1']
    dV_RC2 = -V_RC2 / (params['R2'] * params['C2']) + I / params['C2']
    
    # 热模型微分方程
    dT = thermal_model(t, T, I, V, SOC, params['T_amb'], params)
    
    return [dSOC, dV_RC1, dV_RC2, dT]
```

---

## 10. 模型验证

### 10.1 验证场景

1. **恒流放电温升**：验证稳态温升与 $I^2R/(hA)$ 一致
2. **温度阶跃响应**：验证热时间常数 $\tau_{th}$
3. **内阻温度特性**：验证Arrhenius关系

### 10.2 典型验证数据

| 测试条件 | 预期结果 | 误差范围 |
|----------|----------|----------|
| 1A恒流，25°C环境 | 稳态温升 ~1.3K | ±0.5K |
| 2A恒流，25°C环境 | 稳态温升 ~5K | ±1K |
| 温度从40°C降到25°C | τ ≈ 14min | ±3min |
| 0°C时内阻 | R ≈ 2.2×R(25°C) | ±20% |

---

## 参考文献

1. **论文141**: 电化学-热耦合模型综述(JEST)
2. **论文279**: JPS温度依赖参数
3. **论文122**: Peukert温度依赖性(JPS)
4. **论文145**: 实用电化学-热模型(Energy)
5. **论文148**: 热动力学(Nature SR)
6. **论文134**: 湿度阈值与材料退化（JES）

---

*文档版本: v1.0*
*创建时间: 2026年1月31日*
*上一步: 02_power_model.md*
*下一步: 04_aging_model.md - 老化模型*
