# 电池老化模型：SOH动力学与容量衰减

> 智能手机电池连续时间建模 - 第4部分
>
> **核心目标**：建立SOH(t)的微分方程，描述日历老化和循环老化

---

## 目录

- [1. 模型概述](#1-模型概述)
- [2. SOH动力学方程](#2-soh动力学方程)
- [3. 日历老化模型](#3-日历老化模型)
- [4. 循环老化模型](#4-循环老化模型)
- [5. 内阻增长模型](#5-内阻增长模型)
- [6. 完整老化模型](#6-完整老化模型)
- [7. 智能手机典型老化场景](#7-智能手机典型老化场景)
- [8. 与其他子模型的接口](#8-与其他子模型的接口)
- [9. 数值实现](#9-数值实现)
- [10. 模型验证](#10-模型验证)
- [参考文献](#参考文献)

## 1. 模型概述

### 1.1 建模目标

将电池健康状态(SOH)建模为时间的连续函数：

$$SOH(t): [0, \infty) \rightarrow [0, 1]$$

**定义**：
$$SOH = \frac{Q_{actual}}{Q_{nom}} \times 100\%$$

**输入**：
- 时间 $t$ [s]
- 温度历史 $T(t)$ [K]
- SOC历史 $SOC(t)$ [-]
- 电流历史 $I(t)$ [A]

**输出**：
- 健康状态 $SOH(t)$ [-]
- 有效容量 $Q_{eff}(t) = Q_{nom} \cdot SOH(t)$ [Ah]
- 内阻增长 $R(t) / R_0$ [-]

### 1.2 老化机制分类

| 老化类型 | 机制 | 主要因素 | 时间尺度 |
|----------|------|----------|----------|
| **日历老化** | SEI层生长、锂损失 | 时间、温度、SOC | 月-年 |
| **循环老化** | 活性材料损失、锂镀覆 | 循环次数、DOD、C-rate | 周-月 |

**文献依据**：论文238（通用老化模型）、论文110（老化机制综述）

---

## 2. SOH动力学方程

### 2.1 总老化速率

$$\boxed{\frac{dSOH(t)}{dt} = -\left(\frac{dSOH}{dt}\right)_{cal} - \left(\frac{dSOH}{dt}\right)_{cyc}}$$

**容量损失等效**：
$$\frac{dQ_{loss}(t)}{dt} = \left(\frac{dQ}{dt}\right)_{cal} + \left(\frac{dQ}{dt}\right)_{cyc}$$

### 2.2 基本形式

通用老化速率方程：

$$\boxed{\frac{dSOH}{dt} = -k_0 \cdot \exp\left(-\frac{E_a}{RT}\right) \cdot g(SOC) \cdot h(SOH)}$$

其中：
- $k_0$：预指因子
- $E_a$：活化能
- $g(SOC)$：SOC依赖函数
- $h(SOH)$：老化状态依赖函数

---

## 3. 日历老化模型

### 3.1 SEI层生长机制

日历老化主要由SEI（固体电解质界面）层生长驱动：

$$\boxed{\frac{dSOH_{cal}}{dt} = -k_{cal} \cdot \exp\left(-\frac{E_{a,cal}}{RT}\right) \cdot f_{SOC}(SOC)}$$

**SEI动力学补充（机理型）**：

SEI厚度增长遵循扩散控制：

$$\frac{d\delta_{SEI}}{dt} = \frac{k_{SEI}}{\delta_{SEI}}\exp\left(-\frac{E_{a,SEI}}{RT}\right) f_{SOC}(SOC)$$
\tag{3.1-1}

与容量损失关系：

$$Q_{loss,cal} = \kappa \cdot \delta_{SEI}$$
\tag{3.1-2}

由此得到$Q_{loss,cal}\propto \sqrt{t}$，与3.3节一致。[文献88, 139]

### 3.2 SOC依赖性

高SOC加速老化：

$$f_{SOC}(SOC) = \exp(\beta \cdot SOC)$$

或分段线性：

$$f_{SOC}(SOC) = \begin{cases}
1 & SOC < 0.5 \\
1 + k_{high} \cdot (SOC - 0.5) & SOC \geq 0.5
\end{cases}$$

### 3.3 平方根时间规律

SEI生长遵循扩散控制的平方根时间规律：

$$Q_{loss,cal}(t) = k_{cal}(T, SOC) \cdot \sqrt{t}$$

微分形式：
$$\frac{dQ_{loss,cal}}{dt} = \frac{k_{cal}(T, SOC)}{2\sqrt{t}}$$

**注意**：$t=0$时奇异，实际从$t_{init} > 0$开始。

### 3.4 日历老化参数

**典型NMC/LCO电池参数**：

| 参数 | 符号 | 典型值 | 单位 |
|------|------|--------|------|
| 预指因子 | $k_{cal,0}$ | $5 \times 10^{8}$ | day⁻⁰·⁵ |
| 活化能 | $E_{a,cal}$ | 50-70 | kJ/mol |
| SOC系数 | $\beta$ | 1.0-2.0 | - |
| 参考温度 | $T_{ref}$ | 298.15 | K |

### 3.5 日历老化预测

**25°C、50% SOC条件下**：

| 时间 | 容量损失 | 剩余SOH |
|------|----------|---------|
| 1个月 | 0.2% | 99.8% |
| 6个月 | 0.5% | 99.5% |
| 1年 | 0.8% | 99.2% |
| 2年 | 1.2% | 98.8% |
| 3年 | 1.5% | 98.5% |

**高温(45°C)加速**：老化速率约为25°C的3-5倍

---

## 4. 循环老化模型

### 4.1 基本循环老化方程

$$\boxed{\frac{dSOH_{cyc}}{dN} = -k_{cyc} \cdot \exp\left(-\frac{E_{a,cyc}}{RT}\right) \cdot f_{DOD}(DOD) \cdot f_{rate}(C)}$$

### 4.1.1 充电窗口与SOC摆动影响

> **为什么考虑SOC窗口？**
>
> 仅DOD不足以描述老化。高SOC区停留会显著加速副反应；同样DOD下，
> 若循环窗口更靠近高SOC，老化更严重。[文献127]

引入SOC窗口修正：

$$f_{window}(SOC_{min}, SOC_{max}) = 1 + k_{win}(SOC_{avg}-SOC_{ref})$$
\tag{4.1-1}

其中$SOC_{avg}=(SOC_{min}+SOC_{max})/2$。

综合循环老化：

$$\frac{dSOH_{cyc}}{dN} = -k_{cyc} \cdot e^{-E_{a,cyc}/RT}\cdot f_{DOD}\cdot f_{rate}\cdot f_{window}$$
\tag{4.1-2}

其中 $N$ 为等效完整循环数。

### 4.2 转换为时间域

$$\frac{dSOH_{cyc}}{dt} = \frac{dSOH_{cyc}}{dN} \cdot \frac{dN}{dt}$$

等效循环速率：
$$\frac{dN}{dt} = \frac{|I(t)|}{2 \cdot Q_{nom} \cdot SOH \cdot 3600}$$

因此：
$$\boxed{\frac{dSOH_{cyc}}{dt} = -k_{cyc}(T) \cdot f_{DOD} \cdot f_{rate} \cdot \frac{|I(t)|}{2 \cdot Q_{nom} \cdot SOH \cdot 3600}}$$

### 4.3 DOD依赖性

放电深度影响（非线性）：

$$f_{DOD}(DOD) = (DOD)^{\gamma}$$

其中 $\gamma \approx 1.5-2.5$

| DOD | $f_{DOD}$ (γ=2) | 相对老化速率 |
|-----|-----------------|--------------|
| 10% | 0.01 | 1× |
| 20% | 0.04 | 4× |
| 50% | 0.25 | 25× |
| 80% | 0.64 | 64× |
| 100% | 1.00 | 100× |

**浅循环更有利于电池寿命。**

### 4.4 C-rate依赖性

放电倍率影响：

$$f_{rate}(C) = 1 + k_C \cdot (C - C_{ref})^2$$

或：
$$f_{rate}(C) = \left(\frac{C}{C_{ref}}\right)^{\alpha}$$

其中 $\alpha \approx 0.5-1.0$

**智能手机典型放电C-rate**：

| 场景 | 电流 [A] | C-rate | $f_{rate}$ |
|------|----------|--------|------------|
| 待机 | 0.05 | 0.017C | 0.13 |
| 轻度使用 | 0.3 | 0.1C | 0.32 |
| 中度使用 | 0.8 | 0.27C | 0.52 |
| 重度使用 | 1.5 | 0.5C | 0.71 |
| 游戏 | 2.5 | 0.83C | 0.91 |

### 4.5 循环老化参数

| 参数 | 符号 | 典型值 | 单位 |
|------|------|--------|------|
| 预指因子 | $k_{cyc,0}$ | $1 \times 10^{5}$ | cycle⁻¹ |
| 活化能 | $E_{a,cyc}$ | 30-50 | kJ/mol |
| DOD指数 | $\gamma$ | 2.0 | - |
| C-rate指数 | $\alpha$ | 0.7 | - |
| 参考C-rate | $C_{ref}$ | 1.0 | C |

---

## 5. 内阻增长模型

### 5.1 内阻与容量老化关系

$$\boxed{\frac{R(t)}{R_0} = 1 + k_R \cdot (1 - SOH(t))^{\delta}}$$

其中 $\delta \approx 0.5-1.0$

简化线性关系：
$$R(t) = R_0 \cdot (1 + k_R \cdot Q_{loss})$$

### 5.2 典型内阻增长

| SOH | 容量损失 | 内阻增长 ($k_R=2$) |
|-----|----------|-------------------|
| 100% | 0% | 0% |
| 95% | 5% | 10% |
| 90% | 10% | 20% |
| 85% | 15% | 30% |
| 80% | 20% | 40% |

---

## 6. 完整老化模型

### 6.1 微分方程组

$$\boxed{
\begin{aligned}
\frac{dSOH(t)}{dt} &= -\frac{dSOH_{cal}}{dt} - \frac{dSOH_{cyc}}{dt} \\[10pt]
\frac{dSOH_{cal}}{dt} &= k_{cal,0} \cdot \exp\left(-\frac{E_{a,cal}}{RT}\right) \cdot \exp(\beta \cdot SOC) \cdot \frac{1}{2\sqrt{t}} \\[10pt]
\frac{dSOH_{cyc}}{dt} &= k_{cyc,0} \cdot \exp\left(-\frac{E_{a,cyc}}{RT}\right) \cdot DOD^{\gamma} \cdot C^{\alpha} \cdot f_{window} \cdot \frac{|I|}{2Q_{nom} \cdot SOH \cdot 3600}
\end{aligned}
}$$

### 6.2 简化实用模型

对于智能手机电池建模，可采用半经验简化模型：

$$\boxed{SOH(t) = 1 - k_1 \cdot \sqrt{t_{eq}} - k_2 \cdot N_{eq}}$$

其中：
- $t_{eq}$：等效日历时间（温度加速）
- $N_{eq}$：等效循环数（DOD、C-rate加速）

**等效时间**：
$$t_{eq} = \int_0^t \exp\left[-\frac{E_a}{R}\left(\frac{1}{T(\tau)} - \frac{1}{T_{ref}}\right)\right] d\tau$$

**等效循环数**：
$$N_{eq} = \int_0^t \frac{|I(\tau)|}{2Q_{nom} \cdot 3600} \cdot f_{DOD} \cdot f_{rate} \cdot f_T \, d\tau$$

### 6.3 参数汇总

**智能手机锂电池老化参数**：

| 参数 | 符号 | 典型值 | 单位 |
|------|------|--------|------|
| 日历老化系数 | $k_1$ | 0.02 | %/√day |
| 循环老化系数 | $k_2$ | 0.02 | %/cycle |
| 日历活化能 | $E_{a,cal}$ | 60 | kJ/mol |
| 循环活化能 | $E_{a,cyc}$ | 40 | kJ/mol |
| DOD指数 | $\gamma$ | 2.0 | - |
| C-rate指数 | $\alpha$ | 0.7 | - |
| SOC系数 | $\beta$ | 1.5 | - |
| 内阻增长系数 | $k_R$ | 2.0 | - |

---

## 7. 智能手机典型老化场景

### 7.1 使用模式分析

**典型用户每日使用模式**：

| 时段 | 时长[h] | 场景 | 平均电流[A] | DOD |
|------|---------|------|-------------|-----|
| 0-7 | 7 | 充电+待机 | -1.0 → 0.02 | - |
| 7-9 | 2 | 通勤浏览 | 0.4 | 7% |
| 9-12 | 3 | 办公(轻度) | 0.2 | 5% |
| 12-13 | 1 | 午餐视频 | 0.5 | 4% |
| 13-18 | 5 | 办公(轻度) | 0.2 | 8% |
| 18-20 | 2 | 通勤+社交 | 0.5 | 8% |
| 20-24 | 4 | 娱乐+视频 | 0.6 | 20% |

**每日统计**：
- 总放电深度：~52%
- 等效完整循环：~0.52
- 平均温度：28°C
- 平均SOC：65%

### 7.2 年度老化预测

**基于典型使用模式的老化预测**：

| 时间 | 日历老化 | 循环老化 | 总SOH | 内阻增长 |
|------|----------|----------|-------|----------|
| 新机 | 0% | 0% | 100% | 0% |
| 6个月 | 0.5% | 4.7% | 94.8% | 10% |
| 1年 | 0.7% | 9.5% | 89.8% | 20% |
| 18个月 | 0.9% | 14.2% | 84.9% | 30% |
| 2年 | 1.0% | 19.0% | 80.0% | 40% |
| 3年 | 1.2% | 28.5% | 70.3% | 59% |

**注**：假设每日0.52等效循环，每年190次完整循环。

### 7.3 老化敏感性分析

| 因素 | 变化 | 2年SOH影响 |
|------|------|------------|
| 温度 +10°C | 28→38°C | -5% (75% SOH) |
| 温度 -10°C | 28→18°C | +3% (83% SOH) |
| 高SOC存储 | 50%→90% | -3% (77% SOH) |
| 深循环 | 50%→80% DOD | -8% (72% SOH) |
| 快充 | 1C→2C | -4% (76% SOH) |

---

## 8. 与其他子模型的接口

| 接口 | 方向 | 变量 | 来源/去向 |
|------|------|------|-----------|
| 输入 | ← | $T(t)$ | 热模型(03) |
| 输入 | ← | $SOC(t)$ | 电池模型(01) |
| 输入 | ← | $I(t)$ | 功耗模型(02) |
| 输出 | → | $SOH(t)$ | 电池模型(01) |
| 输出 | → | $R(t)/R_0$ | 电池模型(01) |
| 输出 | → | $Q_{eff}(t)$ | 电池模型(01) |

---

## 9. 数值实现

### 9.1 Python实现

```python
import numpy as np

R_gas = 8.314  # J/(mol·K)

def aging_model(t, SOH, T, SOC, I, params):
    """
    老化模型微分方程
    
    输入:
        t: 时间 [s]
        SOH: 当前健康状态 [-]
        T: 温度 [K]
        SOC: 荷电状态 [-]
        I: 电流 [A] (放电为正)
        params: 老化参数字典
    
    输出:
        dSOH/dt [1/s]
    """
    # 日历老化
    k_cal = params['k_cal_0'] * np.exp(-params['Ea_cal'] / (R_gas * T))
    f_SOC = np.exp(params['beta'] * SOC)
    
    # 避免t=0奇异
    t_eff = max(t, params['t_init'])
    dSOH_cal = -k_cal * f_SOC / (2 * np.sqrt(t_eff / 86400))  # 转换为天
    
    # 循环老化
    if abs(I) > 0.01:  # 有电流流动
        k_cyc = params['k_cyc_0'] * np.exp(-params['Ea_cyc'] / (R_gas * T))
        C_rate = abs(I) / params['Q_nom']
        f_rate = (C_rate / params['C_ref']) ** params['alpha']
        f_DOD = params['DOD_avg'] ** params['gamma']  # 使用平均DOD
        f_window = 1 + params['k_win'] * (params['SOC_avg'] - params['SOC_ref'])

        dSOH_cyc = -k_cyc * f_DOD * f_rate * f_window * abs(I) / (2 * params['Q_nom'] * SOH * 3600)
    else:
        dSOH_cyc = 0
    
    return dSOH_cal + dSOH_cyc

def resistance_growth(SOH, params):
    """计算内阻增长因子"""
    Q_loss = 1 - SOH
    return 1 + params['k_R'] * Q_loss ** params['delta']

# 默认老化参数
AGING_PARAMS = {
    'k_cal_0': 5e-6,      # 日历老化预指因子 [1/√s]
    'Ea_cal': 60000,      # 日历老化活化能 [J/mol]
    'beta': 1.5,          # SOC系数
    't_init': 3600,       # 初始时间(避免奇异) [s]
    
    'k_cyc_0': 2e-5,      # 循环老化预指因子 [1/Ah]
    'Ea_cyc': 40000,      # 循环老化活化能 [J/mol]
    'gamma': 2.0,         # DOD指数
    'alpha': 0.7,         # C-rate指数
    'C_ref': 1.0,         # 参考C-rate
    'DOD_avg': 0.5,       # 平均放电深度
    'SOC_avg': 0.65,       # 平均SOC
    'k_win': 2.0,          # SOC窗口系数
    'SOC_ref': 0.5,        # 参考SOC
    
    'Q_nom': 3.0,         # 标称容量 [Ah]
    'k_R': 2.0,           # 内阻增长系数
    'delta': 0.7,         # 内阻增长指数
}
```

### 9.2 长期老化模拟

```python
def simulate_aging(usage_profile, duration_days, params):
    """
    长期老化模拟
    
    usage_profile: dict with daily usage pattern
        - 'avg_current': 平均放电电流 [A]
        - 'avg_temp': 平均温度 [K]
        - 'avg_SOC': 平均SOC
        - 'daily_DOD': 每日放电深度
        - 'cycles_per_day': 每日等效循环数
    """
    t_days = np.linspace(0, duration_days, duration_days + 1)
    SOH = np.ones_like(t_days)
    R_ratio = np.ones_like(t_days)
    
    dt = 1  # 1天步长
    
    for i in range(1, len(t_days)):
        # 日历老化 (平方根时间)
        k_cal = params['k_cal_0'] * np.exp(-params['Ea_cal'] / (R_gas * usage_profile['avg_temp']))
        f_SOC = np.exp(params['beta'] * usage_profile['avg_SOC'])
        dSOH_cal = k_cal * f_SOC * (np.sqrt(t_days[i]) - np.sqrt(t_days[i-1]))
        
        # 循环老化
        N_daily = usage_profile['cycles_per_day']
        k_cyc = params['k_cyc_0'] * np.exp(-params['Ea_cyc'] / (R_gas * usage_profile['avg_temp']))
        C_rate = usage_profile['avg_current'] / params['Q_nom']
        f_rate = (C_rate / params['C_ref']) ** params['alpha']
        f_DOD = usage_profile['daily_DOD'] ** params['gamma']
        dSOH_cyc = k_cyc * f_DOD * f_rate * N_daily
        
        # 更新SOH
        SOH[i] = SOH[i-1] - dSOH_cal - dSOH_cyc
        R_ratio[i] = resistance_growth(SOH[i], params)
    
    return t_days, SOH, R_ratio

# 典型使用模式
TYPICAL_USAGE = {
    'avg_current': 0.4,       # A
    'avg_temp': 301,          # K (28°C)
    'avg_SOC': 0.65,          # -
    'daily_DOD': 0.52,        # -
    'cycles_per_day': 0.52,   # 等效完整循环/天
}
```

---

## 10. 模型验证

### 10.1 验证数据源

| 数据集 | 电池类型 | 测试条件 | 来源 |
|--------|----------|----------|------|
| NASA PCoE | 18650 Li-ion | 多温度循环 | 公开 |
| CALCE | 18650 | 动态工况 | 公开 |
| MIT-Stanford | 商用电芯 | 快充循环 | 公开 |

### 10.2 验证指标

$$RMSE_{SOH} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(SOH_{pred,i} - SOH_{meas,i})^2}$$

**精度目标**：$RMSE_{SOH} < 3\%$

---

## 参考文献

1. **论文238**: PHM通用老化模型（化学体系无关）
2. **论文110**: 电池老化机制综述
3. **论文119**: 半经验日历老化模型
4. **论文118**: 循环老化矩阵测试
5. **论文88**: Nature Energy老化研究
6. **论文139**: SEI生长时空模型（Nature Comm）
7. **论文127**: 快充循环窗口老化（JES）

---

*文档版本: v1.0*
*创建时间: 2026年1月31日*
*上一步: 03_thermal_model.md*
*下一步: 05_prediction_model.md - 耗尽时间预测*
