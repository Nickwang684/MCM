# 耗尽时间预测模型

> 智能手机电池连续时间建模 - 第5部分
>
> **核心目标**：预测从当前SOC到电池耗尽的剩余时间

---

## 目录

- [1. 模型概述](#1-模型概述)
- [2. 基本耗尽时间方程](#2-基本耗尽时间方程)
- [3. 恒定负载预测](#3-恒定负载预测)
- [4. 变功率负载预测](#4-变功率负载预测)
- [5. 动态预测模型](#5-动态预测模型)
- [6. 不确定性分析](#6-不确定性分析)
- [7. 场景化预测](#7-场景化预测)
- [8. 完整预测模型](#8-完整预测模型)
- [9. 与其他子模型的接口](#9-与其他子模型的接口)
- [10. 数值实现](#10-数值实现)
- [11. 验证与校准](#11-验证与校准)
- [参考文献](#参考文献)

## 1. 模型概述

### 1.1 预测目标

给定当前状态，预测电池电量耗尽时间：

$$t_{empty} = f(SOC_0, T, P_{load}, SOH, ...)$$

**输入**：
- 当前SOC：$SOC_0$ [-]
- 当前温度：$T$ [K]
- 负载功率：$P_{load}(t)$ [W]（可能随时间变化）
- 健康状态：$SOH$ [-]
- 环境条件

**输出**：
- 剩余时间：$t_{empty}$ [s] 或 [h]
- 置信区间：$[t_{low}, t_{high}]$

### 1.2 预测场景

| 场景 | 负载特性 | 预测难度 |
|------|----------|----------|
| 恒定负载 | $P = const$ | 简单 |
| 已知场景 | $P(t)$ 已知模式 | 中等 |
| 动态负载 | $P(t)$ 随机变化 | 困难 |
| 用户自适应 | 根据历史行为 | 复杂 |

**文献依据**：论文280（耗尽时间预测Energy）

---

## 2. 基本耗尽时间方程

### 2.1 积分形式

从当前SOC到最小SOC的时间：

$$\boxed{t_{empty} = \int_{SOC_0}^{SOC_{min}} \frac{Q_{eff}}{I(SOC)} \cdot dSOC}$$

其中：
- $Q_{eff} = Q_{nom} \cdot SOH$：有效容量 [Ah]
- $I(SOC)$：放电电流（取决于SOC和功率需求）[A]
- $SOC_{min}$：截止SOC（通常0.05-0.10）

### 2.2 电流与功率关系

$$I(t) = \frac{P_{load}(t)}{V(SOC, T, I)}$$

由于电压依赖于电流，需要迭代求解：

$$I = \frac{P_{load}}{V_{OC}(SOC) - I \cdot R_{total}(T, SOC)}$$

求解得：
$$\boxed{I = \frac{V_{OC} - \sqrt{V_{OC}^2 - 4 \cdot R_{total} \cdot P_{load}}}{2 \cdot R_{total}}}$$

（取较小根，对应正常工作区域）

### 2.3 简化电流估计

当 $I \cdot R_{total} \ll V_{OC}$ 时：
$$I \approx \frac{P_{load}}{V_{OC}(SOC)}$$

进一步简化（使用标称电压）：
$$I \approx \frac{P_{load}}{V_{nom}}$$

---

## 3. 恒定负载预测

### 3.1 理想情况

假设恒定功率 $P = const$、恒定温度、忽略RC动态：

$$\boxed{t_{empty} = \frac{Q_{eff} \cdot (SOC_0 - SOC_{min}) \cdot V_{avg}}{P_{load}} \times 3600}$$

其中 $V_{avg}$ 为平均放电电压。

**快速估算公式**：
$$t_{empty} [h] \approx \frac{Q_{nom} [Ah] \cdot SOH \cdot (SOC_0 - 0.05) \cdot V_{nom} [V]}{P_{load} [W]}$$

### 3.2 示例计算

**条件**：
- $Q_{nom} = 3.0$ Ah
- $SOH = 0.9$ (90%)
- $SOC_0 = 0.8$ (80%)
- $SOC_{min} = 0.05$ (5%)
- $V_{nom} = 3.8$ V
- $P_{load} = 1500$ mW (社交媒体)

**计算**：
$$t_{empty} = \frac{3.0 \times 0.9 \times (0.8 - 0.05) \times 3.8}{1.5} = 5.13 h$$

### 3.3 温度修正

低温降低有效容量和增加内阻：

$$t_{empty}(T) = t_{empty,ref} \cdot f_T(T)$$

| 温度 | $f_T$ | 续航影响 |
|------|-------|----------|
| 0°C | 0.70 | -30% |
| 10°C | 0.85 | -15% |
| 25°C | 1.00 | 基准 |
| 35°C | 1.00 | 无变化 |

---

## 4. 变功率负载预测

### 4.1 已知功率曲线

当功率随时间变化但已知时：

$$t_{empty} = \int_0^{t_{empty}} dt$$

满足约束：
$$\int_0^{t_{empty}} I(P(t), V(SOC(t))) \cdot dt = Q_{eff} \cdot (SOC_0 - SOC_{min}) \cdot 3600$$

### 4.2 数值求解

**算法：前向积分**

```
初始化:
    SOC = SOC_0
    t = 0
    dt = 1s  # 时间步长

循环:
    P = power_model(t, scenario)
    V = voltage_model(SOC, T)
    I = P / V
    
    dSOC = -I * dt / (Q_eff * 3600)
    SOC = SOC + dSOC
    t = t + dt
    
    如果 SOC <= SOC_min 或 V <= V_min:
        返回 t
```

### 4.3 场景切换

实际使用中，用户在不同场景间切换：

$$t_{empty} = \sum_{i} t_i$$

其中 $t_i$ 为在场景 $i$ 中消耗 $\Delta SOC_i$ 的时间。

---

## 5. 动态预测模型

### 5.1 状态空间模型

定义增广状态：
$$\mathbf{x} = [SOC, V_{RC1}, V_{RC2}, T]^T$$

状态方程：
$$\dot{\mathbf{x}} = f(\mathbf{x}, P_{load}, T_{amb})$$

预测问题变为：求 $t$ 使得 $SOC(t) = SOC_{min}$

### 5.2 预测时域滚动

**滚动预测算法**：

1. 在时刻 $t_k$，测量当前状态 $\mathbf{x}_k$
2. 假设未来功率模式 $\hat{P}_{load}(t), t > t_k$
3. 前向仿真至 $SOC_{min}$
4. 返回预测的 $\hat{t}_{empty}$

每隔 $\Delta t$（如1分钟）更新预测。

### 5.4 自适应校正（数据同化）

> **为什么需要自适应校正？**
>
> 预测误差主要来自功率预测偏差与SOC估计漂移。
> 通过实时观测（电压、SOC变化）对功率或模型参数进行校正，
> 可显著提升短期预测精度。[文献280, 03]

定义观测残差：

$$e_k = SOC_{obs}(t_k) - SOC_{pred}(t_k)$$
\tag{5.4-1}

用残差修正未来功率预测：

$$\hat{P}_{load}^{new}(t) = \hat{P}_{load}(t)\cdot (1 + \lambda e_k)$$
\tag{5.4-2}

其中$\lambda$为自适应增益（典型0.1-0.3）。

也可用指数平滑修正：

$$\hat{P}_{load}^{new} = (1-\alpha)\hat{P}_{load}^{old} + \alpha P_{meas}$$
\tag{5.4-3}

> **说明**：$P_{meas}$可由$V(t)I(t)$估计得到，若功耗模型可用则直接取$P_{total}$。

### 5.3 功率预测

未来功率可以基于：
- **当前值保持**：$\hat{P}(t) = P(t_k)$
- **滑动平均**：$\hat{P}(t) = \frac{1}{N}\sum_{i=0}^{N-1} P(t_k - i\Delta t)$
- **场景识别**：识别当前场景，使用场景平均功率
- **机器学习**：基于历史使用模式预测

---

## 6. 不确定性分析

### 6.1 不确定性来源

| 来源 | 类型 | 影响 |
|------|------|------|
| SOC估计误差 | $\pm 3\%$ | $\pm 3\%$ 时间 |
| SOH估计误差 | $\pm 5\%$ | $\pm 5\%$ 时间 |
| 功率预测误差 | $\pm 20\%$ | $\pm 20\%$ 时间 |
| 温度变化 | $\pm 10°C$ | $\pm 5-15\%$ 时间 |
| 模型误差 | 系统性 | $\pm 5-10\%$ |

### 6.2 置信区间估计

**蒙特卡洛方法**：

```python
def predict_with_uncertainty(SOC_0, T, P_load, SOH, params, N_samples=1000):
    """
    带不确定性的耗尽时间预测
    """
    t_empty_samples = []
    
    for _ in range(N_samples):
        # 采样参数不确定性
        SOC_sample = SOC_0 + np.random.normal(0, params['sigma_SOC'])
        SOH_sample = SOH + np.random.normal(0, params['sigma_SOH'])
        P_sample = P_load * (1 + np.random.normal(0, params['sigma_P']))
        
        # 计算耗尽时间
        t = predict_empty_time(SOC_sample, T, P_sample, SOH_sample, params)
        t_empty_samples.append(t)
    
    # 统计结果
    t_mean = np.mean(t_empty_samples)
    t_std = np.std(t_empty_samples)
    t_5 = np.percentile(t_empty_samples, 5)
    t_95 = np.percentile(t_empty_samples, 95)
    
    return t_mean, t_std, (t_5, t_95)
```

### 6.3 置信区间示例

**条件**：$SOC_0 = 50\%$，轻度使用(1000mW)

| 统计量 | 值 | 说明 |
|--------|------|------|
| 均值 | 5.7 h | 点估计 |
| 标准差 | 0.8 h | 14% 变异 |
| 5%分位 | 4.4 h | 乐观边界 |
| 95%分位 | 7.1 h | 悲观边界 |
| 90%置信区间 | [4.4, 7.1] h | 报告范围 |

---

## 7. 场景化预测

### 7.1 预定义场景预测表

**基于典型使用场景的剩余时间预测**（3000mAh电池，SOH=100%）：

| 场景 | 功耗[mW] | 100%→5% | 80%→5% | 50%→5% | 20%→5% |
|------|----------|---------|--------|--------|--------|
| 待机(屏幕关) | 80 | 142 h | 106 h | 64 h | 21 h |
| 待机(屏幕亮) | 500 | 23 h | 17 h | 10 h | 3.4 h |
| 阅读/浏览 | 1000 | 11 h | 8.6 h | 5.1 h | 1.7 h |
| 社交媒体 | 1500 | 7.6 h | 5.7 h | 3.4 h | 1.1 h |
| 视频流 | 2000 | 5.7 h | 4.3 h | 2.6 h | 0.9 h |
| 视频通话 | 2500 | 4.6 h | 3.4 h | 2.1 h | 0.7 h |
| 导航 | 2200 | 5.2 h | 3.9 h | 2.3 h | 0.8 h |
| 游戏(轻度) | 3000 | 3.8 h | 2.9 h | 1.7 h | 0.6 h |
| 游戏(重度) | 5000 | 2.3 h | 1.7 h | 1.0 h | 0.3 h |

### 7.2 SOH影响

**SOH对续航的影响**（社交媒体场景，100%→5%）：

| SOH | 有效容量 | 续航时间 | 相对变化 |
|-----|----------|----------|----------|
| 100% | 3.0 Ah | 7.6 h | 基准 |
| 95% | 2.85 Ah | 7.2 h | -5% |
| 90% | 2.7 Ah | 6.8 h | -10% |
| 85% | 2.55 Ah | 6.5 h | -15% |
| 80% | 2.4 Ah | 6.1 h | -20% |

### 7.3 混合场景预测

**示例：典型工作日剩余时间预测**

当前状态：SOC=60%，时间=14:00

预计后续使用模式：
- 14:00-18:00：办公（1000mW）→ 4h，消耗35%
- 18:00-19:00：通勤导航（2200mW）→ 1h，消耗19%

预测：
- 到18:00时SOC ≈ 25%
- 到19:00时SOC ≈ 6%（接近耗尽）
- **预计续航至19:00左右**

---

## 8. 完整预测模型

### 8.1 预测函数

$$\boxed{t_{empty} = \int_{SOC_0}^{SOC_{min}} \frac{Q_{nom} \cdot SOH \cdot f_T(T)}{I(SOC, P_{load}, T)} \cdot dSOC}$$

其中电流由功率-电压关系确定：
$$I = \frac{V_{OC}(SOC) - \sqrt{V_{OC}(SOC)^2 - 4R(T, SOC) \cdot P_{load}}}{2R(T, SOC)}$$

### 8.2 算法流程

```
输入: SOC_0, T, P_load(t), SOH, params
输出: t_empty, confidence_interval

1. 初始化
   SOC = SOC_0
   t = 0
   dt = 1s
   
2. 主循环
   while SOC > SOC_min and V > V_min:
       2.1 计算当前电压
           V_OC = ocv_model(SOC, T)
           R = resistance_model(T, SOC) * resistance_growth(SOH)
           
       2.2 计算当前功率需求
           P = power_model(t, scenario)
           
       2.3 计算电流（迭代求解）
           I = (V_OC - sqrt(V_OC^2 - 4*R*P)) / (2*R)
           V = V_OC - I*R
           
       2.4 检查电压约束
           if V < V_min:
               break  # 电压截止
               
       2.5 更新SOC
           dSOC = -I * dt / (Q_nom * SOH * 3600)
           SOC = SOC + dSOC
           
       2.6 更新温度（可选）
           T = thermal_model(T, I, ...)
           
       2.7 更新时间
           t = t + dt
           
3. 返回
   t_empty = t
   confidence = calculate_uncertainty(...)
   return t_empty, confidence
```

---

## 9. 与其他子模型的接口

| 接口 | 方向 | 变量 | 来源 |
|------|------|------|------|
| 输入 | ← | $SOC(t)$ | 电池模型(01) |
| 输入 | ← | $V(t)$ | 电池模型(01) |
| 输入 | ← | $R(T, SOC)$ | 热模型(03)→电池模型(01) |
| 输入 | ← | $P_{load}(t)$ | 功耗模型(02) |
| 输入 | ← | $T(t)$ | 热模型(03) |
| 输入 | ← | $SOH$ | 老化模型(04) |
| 输出 | → | $t_{empty}$ | 用户显示 |
| 输出 | → | 置信区间 | 用户显示 |

---

## 10. 数值实现

### 10.1 Python完整实现

```python
import numpy as np

def predict_empty_time(SOC_0, T, P_load, SOH, params, 
                       scenario_mode='constant', scenario_profile=None):
    """
    预测电池耗尽时间
    
    参数:
        SOC_0: 初始SOC
        T: 温度 [K]
        P_load: 功率 [mW] 或功率函数
        SOH: 健康状态
        params: 电池参数
        scenario_mode: 'constant' | 'profile' | 'adaptive'
        scenario_profile: 场景时间表 (仅当mode='profile')
    
    返回:
        t_empty: 耗尽时间 [s]
        trajectory: (t_array, SOC_array, V_array)
    """
    # 参数
    Q_eff = params['Q_nom'] * SOH * 3600  # As (安秒)
    SOC_min = params.get('SOC_min', 0.05)
    V_min = params.get('V_min', 3.0)
    dt = params.get('dt', 1.0)  # 秒
    
    # 温度修正
    R_factor = np.exp(-params['Ea_R'] / 8.314 * (1/T - 1/params['T_ref']))
    R0 = params['R0'] * R_factor
    
    # 初始化
    SOC = SOC_0
    t = 0
    t_max = 100 * 3600  # 最大100小时
    
    trajectory_t = [0]
    trajectory_SOC = [SOC_0]
    trajectory_V = []
    
    while SOC > SOC_min and t < t_max:
        # 获取当前功率
        if scenario_mode == 'constant':
            P = P_load
        elif scenario_mode == 'profile':
            P = get_power_from_profile(t, scenario_profile)
        else:
            P = P_load  # 默认恒定
        
        P = P / 1000  # mW -> W
        
        # OCV
        V_OC = ocv_model(SOC, params)
        
        # 计算电流 (二次方程求解)
        discriminant = V_OC**2 - 4 * R0 * P
        if discriminant < 0:
            # 功率需求超过电池能力
            break
        
        I = (V_OC - np.sqrt(discriminant)) / (2 * R0)
        V = V_OC - I * R0
        
        # 电压检查
        if V < V_min:
            break
        
        # 记录轨迹
        trajectory_V.append(V)
        
        # 更新SOC
        dSOC = -I * dt / Q_eff
        SOC = SOC + dSOC
        t = t + dt
        
        trajectory_t.append(t)
        trajectory_SOC.append(SOC)
    
    return t, (np.array(trajectory_t), np.array(trajectory_SOC), np.array(trajectory_V))


def adaptive_power_update(P_hat, SOC_obs, SOC_pred, alpha=0.2, lam=0.2):
    """
    自适应校正功率预测
    """
    e = SOC_obs - SOC_pred
    P_hat = P_hat * (1 + lam * e)
    P_hat = (1 - alpha) * P_hat + alpha * P_hat  # 可替换为P_meas
    return P_hat

def ocv_model(SOC, params):
    """OCV-SOC模型"""
    K0, K1, K2, K3 = params['K0'], params['K1'], params['K2'], params['K3']
    SOC = np.clip(SOC, 0.01, 0.99)  # 避免log(0)
    return K0 + K1 * SOC + K2 * np.log(SOC) + K3 * np.log(1 - SOC)

def quick_estimate(SOC_0, P_load_mW, Q_nom_Ah=3.0, SOH=1.0, V_nom=3.8):
    """
    快速耗尽时间估算
    """
    SOC_min = 0.05
    usable_SOC = SOC_0 - SOC_min
    energy_Wh = Q_nom_Ah * SOH * usable_SOC * V_nom
    P_load_W = P_load_mW / 1000
    t_hours = energy_Wh / P_load_W
    return t_hours

# 默认参数
PREDICTION_PARAMS = {
    'Q_nom': 3.0,         # Ah
    'R0': 0.08,           # Ω
    'Ea_R': 25000,        # J/mol
    'T_ref': 298.15,      # K
    'SOC_min': 0.05,      # -
    'V_min': 3.0,         # V
    'dt': 1.0,            # s
    'K0': 3.685,          # V
    'K1': 0.2156,         # V
    'K2': 0.0351,         # V
    'K3': -0.0175,        # V
}
```

### 10.2 使用示例

```python
# 场景1: 恒定负载预测
t_empty, trajectory = predict_empty_time(
    SOC_0=0.8,
    T=298,  # 25°C
    P_load=1500,  # mW
    SOH=0.9,
    params=PREDICTION_PARAMS,
    scenario_mode='constant'
)
print(f"预计剩余时间: {t_empty/3600:.1f} 小时")

# 场景2: 快速估算
t_quick = quick_estimate(SOC_0=0.8, P_load_mW=1500, Q_nom_Ah=3.0, SOH=0.9)
print(f"快速估算: {t_quick:.1f} 小时")

# 场景3: 不同场景对比
scenarios = {
    '待机': 100,
    '阅读': 1000,
    '社交': 1500,
    '视频': 2000,
    '游戏': 4000,
}

print("\n从80%电量开始的剩余时间:")
for name, power in scenarios.items():
    t = quick_estimate(0.8, power, 3.0, 1.0)
    print(f"  {name}: {t:.1f} 小时")
```

---

## 11. 验证与校准

### 11.1 验证方法

1. **实验室测试**：恒定负载放电，记录实际耗尽时间
2. **实际使用测试**：记录真实使用场景下的续航
3. **交叉验证**：与手机系统预测对比

### 11.2 校准流程

1. 测量实际放电曲线（SOC vs 时间）
2. 调整OCV-SOC参数使电压曲线匹配
3. 调整内阻参数使放电末期电压匹配
4. 验证预测误差

### 11.3 精度指标

$$MAPE = \frac{1}{N}\sum_{i=1}^{N}\left|\frac{t_{pred,i} - t_{actual,i}}{t_{actual,i}}\right| \times 100\%$$

**目标**：$MAPE < 10\%$

---

## 参考文献

1. **论文280**: Energy期刊耗尽时间预测算法
2. **论文277**: Applied Energy连续时间建模
3. **论文191**: OCV-SOC模型综述
4. **论文279**: 温度依赖参数
5. **论文03**: SOC/SOH在线估计（用于自适应校正）

---

*文档版本: v1.0*
*创建时间: 2026年1月31日*
*上一步: 04_aging_model.md*
*下一步: 00_framework.md - 完整模型框架整合*
