# 📊 MCM 2026 Problem A - 图表文档说明

## Figures Documentation for Battery SOC Modeling Paper

**文件位置:** `D:\jingsai\shumo\MCM\2026A\PAPER\figures\`

**创建日期:** 2025年1月

**项目:** MCM 2026 Problem A - 智能手机电池SOC建模与预测

---

## 📁 文件概览

| 图片文件                           | 生成脚本                             | 描述                    |
| ------------------------------ | -------------------------------- | --------------------- |
| `ecm_concentric.png/pdf`       | `create_ecm_diagram.py`          | 等效电路模型同心圆可视化          |
| `ocv_model_comparison.png/pdf` | `create_ocv_model.py`            | OCV模型对比分析（4子图）        |
| `ocv_temperature.png/pdf`      | `create_ocv_model.py`            | OCV温度依赖性分析            |
| `ocv_nernst_shepherd.png/pdf`  | `create_ocv_model.py`            | Nernst与Shepherd边界行为对比 |
| `power_soc_simulation.png/pdf` | `create_power_soc_simulation.py` | 功率驱动SOC仿真（6子图）        |
| `rc_dynamics.png/pdf`          | `create_power_soc_simulation.py` | RC电路动态响应              |
| `model_validation.png/pdf`     | `create_power_soc_simulation.py` | 模型验证分析                |

---

## 🔋 图1: 等效电路模型 (ECM Concentric Diagram)

### 文件信息
- **文件名:** `ecm_concentric.png`, `ecm_concentric.pdf`
- **生成脚本:** `create_ecm_diagram.py`
- **函数:** `create_concentric_ecm()`

### 图表描述
采用同心圆层次化设计展示二阶RC等效电路模型(2-RC ECM)的结构：

```
┌─────────────────────────────────────────┐
│           V(t) 端电压 (最外层)            │
│  ┌─────────────────────────────────┐    │
│  │         R₀ 欧姆内阻              │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │    R₁||C₁ (τ₁≈40s)      │    │    │
│  │  │  ┌─────────────────┐    │    │    │
│  │  │  │  R₂||C₂ (τ₂≈500s)│    │    │    │
│  │  │  │  ┌───────────┐  │    │    │    │
│  │  │  │  │   OCV     │  │    │    │    │
│  │  │  │  │  ┌─────┐  │  │    │    │    │
│  │  │  │  │  │ SOC │  │  │    │    │    │
│  │  │  │  │  └─────┘  │  │    │    │    │
│  │  │  │  └───────────┘  │    │    │    │
│  │  │  └─────────────────┘    │    │    │
│  │  └─────────────────────────┘    │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### 数学模型
**端电压方程:**
$$V(t) = V_{OC}(SOC) - I(t) \cdot R_0 - V_{RC1}(t) - V_{RC2}(t)$$

**RC动态方程:**
$$\frac{dV_{RC,i}}{dt} = -\frac{V_{RC,i}}{\tau_i} + \frac{I(t)}{C_i}, \quad \tau_i = R_i \cdot C_i$$

**SOC积分方程:**
$$SOC(t) = SOC_0 - \frac{1}{Q_{nom}} \int_0^t I(\tau) d\tau$$

### 模型参数 (基于LG 18650HG2)
| 参数 | 值 | 说明 |
|-----|-----|------|
| $Q_{nom}$ | 3.0 Ah | 标称容量 |
| $R_0$ | 50 mΩ | 欧姆内阻 |
| $R_1$ | 30 mΩ | 快时间常数电阻 |
| $C_1$ | 1000 F | 快时间常数电容 |
| $\tau_1$ | ~30 s | 电化学极化时间常数 |
| $R_2$ | 20 mΩ | 慢时间常数电阻 |
| $C_2$ | 25000 F | 慢时间常数电容 |
| $\tau_2$ | ~500 s | 浓差极化时间常数 |

### 数据集来源
- **类型:** 概念图/合成数据
- **参数来源:** LG 18650HG2 Li-ion Battery Data (McMaster University)
- **原始数据集路径:** `D:\jingsai\shumo\MCM\2026A\dataset\LG 18650HG2 Li-ion Battery Data\`

### 论文引用位置
- **LaTeX文件:** `sections/model1_soc.tex`
- **章节:** 2.1 等效电路模型结构

---

## 📈 图2: OCV模型对比分析 (OCV Model Comparison)

### 文件信息
- **文件名:** `ocv_model_comparison.png`, `ocv_model_comparison.pdf`
- **生成脚本:** `create_ocv_model.py`
- **函数:** `create_ocv_comparison_figure()`

### 子图描述

#### (a) OCV-SOC模型对比曲线
展示三种OCV模型在全SOC范围(0-100%)的拟合效果：
- **Nernst方程** (蓝色虚线)
- **多项式模型** (绿色点线)  
- **Shepherd模型** (红色实线) ✓ 最优

#### (b) 低SOC边界行为放大
放大显示SOC < 10%区域的模型行为：
- Nernst方程在SOC→0时发散至-∞
- Shepherd模型通过双对数项保持有界

#### (c) 残差分析柱状图
各模型的均方根误差(RMSE)对比：
| 模型 | RMSE |
|-----|------|
| Nernst | ~15.7 mV |
| Polynomial | ~8.3 mV |
| Shepherd | ~4.2 mV |

#### (d) 模型演化示意图
展示从基础Nernst方程到改进Shepherd模型的演化路径：
```
Nernst基础 → 添加线性项 → 双对数边界修正 → Shepherd模型
```

### 数学模型

**Nernst方程:**
$$V_{OC} = E_0 + \frac{RT}{nF} \ln\left(\frac{SOC}{1-SOC}\right)$$

**多项式模型 (6阶):**
$$V_{OC} = \sum_{i=0}^{6} a_i \cdot SOC^i$$

**Shepherd模型 (本文采用):**
$$V_{OC} = E_0 + K_1 \cdot SOC + K_2 \cdot \ln(SOC) + K_3 \cdot \ln(1-SOC)$$

### Shepherd模型参数
| 参数 | 值 | 物理意义 |
|-----|-----|---------|
| $E_0$ | 3.685 V | 参考电势 |
| $K_1$ | 0.2156 | 线性SOC系数 |
| $K_2$ | 0.0351 | 低SOC对数系数 |
| $K_3$ | -0.0175 | 高SOC对数系数 |

### 数据集来源
- **类型:** 合成数据
- **基准:** LG 18650HG2电池OCV特性曲线
- **参考数据集:** 
  - `D:\jingsai\shumo\MCM\2026A\dataset\LG 18650HG2 Li-ion Battery Data\`
  - `D:\jingsai\shumo\MCM\2026A\dataset\battery data\低电流开路电压\` (中文OCV数据)

### 论文引用位置
- **LaTeX文件:** `sections/model1_soc.tex`
- **章节:** 2.2 开路电压模型

---

## 🌡️ 图3: OCV温度依赖性 (OCV Temperature Dependence)

### 文件信息
- **文件名:** `ocv_temperature.png`, `ocv_temperature.pdf`
- **生成脚本:** `create_ocv_model.py`
- **函数:** `create_ocv_temperature_figure()`

### 子图描述

#### (a) 不同温度下的OCV曲线
展示5个温度点的OCV-SOC关系：
- 0°C (蓝色)
- 10°C (青色)
- 25°C (绿色) - 参考温度
- 40°C (橙色)
- 50°C (红色)

**观察结果:** 低温时OCV整体下移，高温时上移

#### (b) OCV温度偏移量
不同SOC水平下OCV随温度的变化：
- SOC = 20%, 50%, 80%三条曲线
- 温度系数: $\frac{dE}{dT} \approx -0.3$ mV/K

### 数学模型
**温度修正的Shepherd模型:**
$$V_{OC}(SOC, T) = V_{OC,ref}(SOC) + \alpha_T (T - T_{ref})$$

其中:
- $T_{ref} = 25°C$ (参考温度)
- $\alpha_T = -0.3$ mV/K (温度系数)

**Arrhenius温度补偿:**
$$R(T) = R_{ref} \exp\left[\frac{E_a}{R_{gas}}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]$$

### 数据集来源
- **类型:** 合成数据 + Arrhenius温度模型
- **温度范围参考:** LG 18650HG2数据集 (-20°C ~ 40°C)
- **原始数据集路径:** `D:\jingsai\shumo\MCM\2026A\dataset\LG 18650HG2 Li-ion Battery Data\`

### 论文引用位置
- **LaTeX文件:** `sections/model1_soc.tex`
- **章节:** 2.2.3 温度影响分析

---

## 📊 图4: Nernst与Shepherd边界行为 (Nernst vs Shepherd Boundary)

### 文件信息
- **文件名:** `ocv_nernst_shepherd.png`, `ocv_nernst_shepherd.pdf`
- **生成脚本:** `create_ocv_model.py`
- **函数:** `create_nernst_shepherd_comparison()`

### 子图描述

#### (a) 纯Nernst方程发散问题
展示Nernst方程在边界的数学奇点：
- SOC → 0: $V_{OC} \rightarrow -\infty$
- SOC → 1: $V_{OC} \rightarrow +\infty$
- **问题:** 实际电池不会出现无穷大电压

#### (b) Shepherd模型有界行为
展示改进后的Shepherd模型边界特性：
- 双对数项相互抵消边界奇点
- 全SOC范围内保持物理合理的电压值
- 边界值: $V_{min} \approx 2.5V$, $V_{max} \approx 4.2V$

#### (c) dOCV/dSOC导数对比
比较两种模型的SOC敏感度（卡尔曼滤波H矩阵）：
$$H = \frac{\partial V_{OC}}{\partial SOC}$$

| 区域 | Nernst | Shepherd |
|-----|--------|----------|
| SOC→0 | →∞ | 有界大值 |
| SOC=50% | ~0.1 V | ~0.15 V |
| SOC→1 | →∞ | 有界大值 |

### 理论意义
**为什么选择Shepherd模型:**
1. **数值稳定性:** 避免卡尔曼滤波器在边界发散
2. **物理合理性:** 电压保持在实际电池范围内
3. **SOC全域适用:** 无需分段处理

### 数据集来源
- **类型:** 纯解析对比（无实验数据）
- **目的:** 理论模型行为分析

### 论文引用位置
- **LaTeX文件:** `sections/model1_soc.tex`
- **章节:** 2.2.2 模型选择理由

---

## 📱 图5: 功率驱动SOC仿真 (Power-Driven SOC Simulation)

### 文件信息
- **文件名:** `power_soc_simulation.png`, `power_soc_simulation.pdf`
- **生成脚本:** `create_power_soc_simulation.py`
- **函数:** `create_power_soc_simulation()`

### 子图描述 (6-Panel Layout)

#### (a) SOC放电曲线
6种使用场景的SOC随时间变化：

| 场景 | 描述 | 电池寿命 |
|-----|------|---------|
| Light Use | 轻度使用(阅读、待机) | ~20.2 h |
| Moderate | 中度使用(社交媒体) | ~9.8 h |
| Video Streaming | 视频播放 | ~5.2 h |
| Gaming | 高性能游戏 | ~3.1 h |
| Navigation | GPS导航 | ~4.5 h |
| Mixed | 混合使用模式 | ~7.3 h |

#### (b) 模型vs"实验"对比
仿真结果与添加噪声的"实验"数据对比，验证模型准确性

#### (c) 端电压演化
不同场景下端电压V(t)随时间变化：
- 高功率场景电压降落更快
- 截止电压: $V_{cutoff} = 2.5V$

#### (d) 功率分解
展示总功率的组成成分：
$$P_{total} = P_{base} + P_{display} + P_{CPU} + P_{network} + P_{GPS}$$

#### (e) 放电电流
由功率和电压计算的电流：
$$I(t) = \frac{P(t)}{V(t)}$$

#### (f) 电池寿命对比柱状图
6种场景的续航时间横向对比

### 功率模型 (基于AndroWatts)

```python
# 基础功率
P_base = 100 mW  # 系统基础消耗

# 显示屏功率
P_display = 50 + 800 * B^1.8  # B: 亮度 0-1

# CPU功率
P_cpu = 50 + 1950 * U^1.5  # U: 利用率 0-1

# 网络功率
P_wifi = 20 (idle) ~ 800 (active) mW
P_4g = 50 (idle) ~ 2500 (active) mW

# GPS功率
P_gps = 500 mW (when active)
```

### 场景参数配置

| 场景 | 亮度 | CPU利用率 | 网络 | GPS |
|-----|------|----------|------|-----|
| Light Use | 30% | 10% | WiFi idle | Off |
| Moderate | 50% | 30% | WiFi active | Off |
| Video | 70% | 40% | WiFi streaming | Off |
| Gaming | 80% | 90% | WiFi active | Off |
| Navigation | 70% | 50% | 4G active | On |
| Mixed | 变化 | 变化 | 变化 | 变化 |

### 数据集来源
- **电池参数:** LG 18650HG2 (合成)
- **功率模型:** AndroWatts智能手机功率模型
- **使用场景:** 典型智能手机使用模式

### 论文引用位置
- **LaTeX文件:** `sections/model2_prediction.tex`
- **章节:** 3.1 使用场景建模与仿真

---

## ⚡ 图6: RC电路动态响应 (RC Circuit Dynamics)

### 文件信息
- **文件名:** `rc_dynamics.png`, `rc_dynamics.pdf`
- **生成脚本:** `create_power_soc_simulation.py`
- **函数:** `create_rc_dynamics_figure()`

### 子图描述 (4-Panel Layout)

#### (a) RC极化电压
展示两个RC环节的动态响应：
- $V_{RC1}(t)$: 快时间常数极化 (τ₁≈30s)
- $V_{RC2}(t)$: 慢时间常数极化 (τ₂≈500s)

**特点:**
- 电流突变时$V_{RC1}$快速响应
- $V_{RC2}$变化缓慢，代表浓差极化

#### (b) 电压降分解
端电压损失的三个组成部分：
$$\Delta V = I \cdot R_0 + V_{RC1} + V_{RC2}$$

| 组成 | 特性 | 典型值(1A) |
|-----|------|-----------|
| $IR_0$ | 瞬时响应 | 50 mV |
| $V_{RC1}$ | 快极化 | 0~30 mV |
| $V_{RC2}$ | 慢极化 | 0~20 mV |

#### (c) OCV vs 端电压
比较开路电压与实际端电压的差异：
- OCV: 理想无负载电压
- V(t): 实际负载下端电压
- 差值 = 总极化损失

#### (d) 功率-电流关系
展示P(t)与I(t)的非线性关系：
$$P = V \cdot I \Rightarrow I = \frac{P}{V}$$

高功率时电压下降，导致电流非线性增加

### 仿真场景
- **选用场景:** Gaming (高动态负载)
- **仿真时长:** 3+ 小时
- **采样间隔:** 1秒

### 数据集来源
- **类型:** 仿真数据
- **电池模型:** 2-RC ECM with LG 18650HG2 parameters
- **负载模型:** Gaming场景功率曲线

### 论文引用位置
- **LaTeX文件:** `sections/model1_soc.tex`
- **章节:** 2.1.2 RC动态响应分析

---

## ✅ 图7: 模型验证分析 (Model Validation)

### 文件信息
- **文件名:** `model_validation.png`, `model_validation.pdf`
- **生成脚本:** `create_power_soc_simulation.py`
- **函数:** `create_validation_figure()`

### 子图描述 (4-Panel Layout)

#### (a) SOC模型vs实验散点图
- X轴: "实验"SOC值
- Y轴: 模型预测SOC值
- 理想线: y = x (虚线)
- **决定系数:** R² = 0.9927

#### (b) 电压模型vs实验散点图
- X轴: "实验"电压值
- Y轴: 模型预测电压值
- **决定系数:** R² > 0.99

#### (c) SOC残差时间序列
展示SOC预测误差随时间的分布：
- 残差 = SOC_model - SOC_experiment
- **RMSE ≈ 1.85%**
- 无明显系统性偏差

#### (d) 残差直方图
SOC残差的统计分布：
- 近似正态分布
- 均值 ≈ 0
- 标准差 ≈ 1.85%

### 验证方法
```
1. 运行模型仿真 → SOC_model(t), V_model(t)
2. 添加高斯噪声 → SOC_exp(t), V_exp(t)
   - SOC噪声: σ = 2%
   - 电压噪声: σ = 10 mV
3. 计算统计指标 → R², RMSE, MAE
```

### 验证结果汇总

| 指标 | SOC | 电压 |
|-----|-----|------|
| R² | 0.9927 | 0.9951 |
| RMSE | 1.85% | 8.3 mV |
| MAE | 1.42% | 6.7 mV |
| Max Error | 5.2% | 28 mV |

### 数据集来源
- **仿真数据:** Moderate Use场景
- **"实验"数据:** 仿真数据 + 高斯噪声
- **目的:** 展示模型验证方法论

### 论文引用位置
- **LaTeX文件:** `sections/model2_prediction.tex`
- **章节:** 3.3 模型验证与误差分析

---

## 📚 数据集汇总

### 实际使用的数据集

| 数据集 | 路径 | 用途 |
|-------|------|------|
| LG 18650HG2 | `dataset\LG 18650HG2 Li-ion Battery Data\` | ECM参数提取 |
| 低电流OCV | `dataset\battery data\低电流开路电压\` | OCV模型参考 |

### 参数提取说明

**注意:** 本文所有图表使用的是**合成数据**，基于以下原始数据集提取的参数：

1. **电池容量与内阻:** 从LG 18650HG2数据集的放电曲线提取
2. **OCV特性:** 参考低电流OCV测试数据拟合Shepherd模型
3. **温度系数:** 基于多温度测试数据(-20°C~40°C)

### 为什么使用合成数据

1. **可控性:** 精确控制仿真条件
2. **可重复性:** 结果100%可复现
3. **场景覆盖:** 可模拟任意使用场景
4. **噪声控制:** 验证时添加已知噪声

---

## 🔗 图表与数据集关系映射

| 图表 | 主要数据集 | 数据类型 | 参数来源 |
|-----|-----------|---------|---------|
| ecm_concentric | LG 18650HG2 | 合成/概念 | ECM参数 |
| ocv_model_comparison | LG 18650HG2 + 低电流OCV | 合成 | OCV特性曲线 |
| ocv_temperature | LG 18650HG2 | 合成 | 多温度测试数据 |
| ocv_nernst_shepherd | 无 | 解析 | 数学模型 |
| power_soc_simulation | LG 18650HG2 + AndroWatts | 合成 | 电池+功率模型 |
| rc_dynamics | LG 18650HG2 | 仿真 | ECM参数 |
| model_validation | LG 18650HG2 | 仿真+噪声 | 验证方法论 |

---

## 🛠️ 图表生成脚本

### 环境要求
```python
# requirements.txt
numpy>=1.20.0
matplotlib>=3.4.0
scipy>=1.7.0
```

### 运行方法
```bash
cd D:\jingsai\shumo\MCM\2026A\PAPER\figures

# 生成ECM图
python create_ecm_diagram.py

# 生成OCV模型图
python create_ocv_model.py

# 生成功率仿真图
python create_power_soc_simulation.py
```

### 输出格式
- **PNG:** 用于文档预览，300 DPI
- **PDF:** 用于LaTeX论文，矢量图

---

## 📝 LaTeX引用示例

```latex
% 在model1_soc.tex中
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/ecm_concentric.pdf}
    \caption{Two-RC equivalent circuit model structure}
    \label{fig:ecm}
\end{figure}

% 在model2_prediction.tex中
\begin{figure}[htbp]
    \centering
    \includegraphics[width=\textwidth]{figures/power_soc_simulation.pdf}
    \caption{Power-driven SOC simulation results}
    \label{fig:power-sim}
\end{figure}
```

---

## 📋 更新日志

| 日期 | 更新内容 |
|-----|---------|
| 2025-01 | 创建初始文档，包含7个图表说明 |
| 2025-01 | 添加数据集来源说明 |
| 2025-01 | 完善数学公式与参数表格 |
| 2025-01 | 添加图表与数据集关系映射表 |

---

**文档作者:** MCM 2026 Team  
**最后更新:** 2025年1月
