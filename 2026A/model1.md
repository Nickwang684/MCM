# 智能手机电池耗电建模 - 文献重要性排序

> 依据2026年MCM问题A：智能手机电池耗电建模
> 
> **核心任务**：建立连续时间数学模型，将SOC作为时间函数，预测剩余电量耗尽时间

---

## 排序原则

根据题目要求，文献重要性按以下维度评估：

| 维度         | 权重    | 说明                 |
| ---------- | ----- | ------------------ |
| **连续时间模型** | ★★★★★ | 核心要求：必须是连续时间方程/方程组 |
| **SOC动力学** | ★★★★★ | 建模SOC(t)是核心输出      |
| **功耗分解模型** | ★★★★☆ | 屏幕、CPU、网络、GPS等组件功耗 |
| **温度影响**   | ★★★★☆ | 题目明确提及温度变化影响       |
| **电池老化**   | ★★★☆☆ | 题目提及使用历史影响性能       |
| **参数可获取性** | ★★★☆☆ | 需要公开数据集或技术规范       |
| **物理机制清晰** | ★★★☆☆ | 非黑箱ML，需明确连续时间模型    |

---

## 第一梯队：核心必读文献（15篇）

> 这些文献直接支撑模型构建的核心框架，必须精读

### 1.1 连续时间电池模型（5篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| **1** | **277** | Applied Energy: Continuous-Time Battery Modeling | **最核心**：直接提供连续时间建模方法论，包含SOC动力学方程 $\frac{dSOC}{dt}=-\frac{I(t)}{Q_{nom}}$，ECM电压方程，热动力学方程 |
| **2** | **35** | Continuous-Time ECM Battery Model | 连续时间系统辨识方法，二阶ECM模型，直接从采样数据建立连续时间模型 |
| **3** | **280** | Energy: Empty Time Prediction | **预测目标**：电池耗尽时间预测算法，直接对应题目"预测剩余电量耗尽时间"要求 |
| **4** | **145** | Practical ECM-Thermal Model (Energy) | 实用电化学-热耦合模型，SPM简化为可嵌入式运行，精度与效率平衡 |
| **5** | **191** | OCV-SOC Models Review (Energies) | OCV模型综述，提供 $V_{OC}(SOC)$ 关系式，SOC估计核心组件 |

### 1.2 智能手机功耗模型（5篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| **6** | **278** | IEEE Access: Complete Smartphone Power Model | **最全面**：完整手机功耗分解模型 $P_{total}=\sum P_i$，各场景功耗数据，直接可用 |
| **7** | **178** | 3 W's of Smartphone Power (UCSD) | 最新精确测量数据，ODPM硬件级功耗隔离，显示屏30-50%功耗占比 |
| **8** | **174** | AndroWatts Component Power | 组件级功耗分解工具，覆盖CPU/GPU/相机/音频/网络/传感器 |
| **9** | **181** | Survey on Energy Estimation (Wiley) | 功耗建模方法综述，分类体系完整，方法论参考 |
| **10** | **11** | Mobile Energy Modeling Survey (ACM) | 移动设备能耗建模综述，方法分类与比较 |

### 1.3 温度与老化模型（5篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| **11** | **279** | JPS: Temperature Dependent Parameters | **温度核心**：电池参数温度依赖性，Arrhenius关系，内阻/容量随温度变化数据 |
| **12** | **122** | Peukert Temperature Dependency (JPS) | 温度扩展Peukert方程，温度-倍率耦合模型 |
| **13** | **141** | Electrochemical-Thermal Coupled Review | 热模型综述，Bernardi产热方程，热-电化学耦合方法 |
| **14** | **238** | PHM Chemistry-Agnostic Degradation | 通用老化模型，SOC和温度联合影响，日历/循环老化分离 |
| **15** | **110** | Battery Degradation Mechanisms Review | 老化机制综述，SEI生长、锂镀覆、结构相变等机理 |

---

## 第二梯队：重要参考文献（25篇）

> 这些文献提供具体组件模型、参数数据或方法细节

### 2.1 SOC估计方法（8篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| 16 | **01** | EKF SOC Estimation (MDPI) | 扩展卡尔曼滤波SOC估计，连续时间状态估计方法 |
| 17 | **02** | Physics-Based Electrochemical SOC | 基于物理的电化学模型，偏微分方程描述 |
| 18 | **05** | Practical SOC Framework (JPS) | 实用SOC估计框架，JPS顶刊方法 |
| 19 | **03** | Online SOC-SOH Estimation | 在线联合估计，实时应用 |
| 20 | **06** | SOC with Aging and Temperature | 考虑老化和温度的SOC估计 |
| 21 | **81** | SPM Stress Observer SOC | 单颗粒模型SOC估计，连续时间框架 |
| 22 | **82** | Particle Filter P2D SOC | 粒子滤波+P2D模型，高精度参考 |
| 23 | **231** | Joint SOC-SOH Estimation | 联合估计框架，状态空间方法 |

### 2.2 组件功耗模型（10篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| 24 | **09** | CPU Power Model Multicore | 多核CPU功耗模型，DVFS影响 |
| 25 | **13** | GPU Power Model Smartphone | GPU功耗建模 |
| 26 | **149** | WiFi Power Modeling (ICDCS) | WiFi功耗模型，$P=P_{base}+k\cdot Throughput$ |
| 27 | **161** | GPS Power Modeling (TMC) | GPS功耗模型，IEEE TMC |
| 28 | **165** | SensingKit Sensor Power (iOS) | 传感器功耗数据，加速度计/陀螺仪/GPS |
| 29 | **15** | Background Energy (MobiCom) | 后台活动功耗，MobiCom顶会 |
| 30 | **221** | SIGCOMM 5G Power | 5G网络功耗测量 |
| 31 | **171** | Video Calling Battery (Nature SR) | 视频通话功耗分析 |
| 32 | **101** | Mobile AP Power Modeling | 应用处理器功耗 |
| 33 | **104** | Video Playback Power | 视频播放功耗模型 |

### 2.3 Peukert效应与放电倍率（4篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| 34 | **121** | Peukert Critical Review (JES) | Peukert方程批判性评估，锂电池指数接近1 |
| 35 | **123** | Peukert Critical Review (JPS 2006) | Peukert方程经典综述 |
| 36 | **124** | Generalized Peukert Li-ion | 广义Peukert方程，多种锂电池格式 |
| 37 | **125** | Peukert-Liebenow Capacity | Peukert容量评估方法 |

### 2.4 公开数据集（3篇）

| 排名 | 编号 | 标题 | 重要性理由 |
|------|------|------|------------|
| 38 | **108** | Open Battery Datasets Comparison | **数据资源**：14个公开数据集对比，NASA/MIT/Oxford等 |
| 39 | **91** | NASA Battery Aging Datasets | NASA PCoE经典数据集 |
| 40 | **114** | 21700 Cycle Aging Data | 21700电池完整循环数据 |

---

## 第三梯队：补充参考文献（40篇）

> 这些文献提供特定领域深入内容或边缘案例

### 3.1 电化学模型深入（10篇）

| 排名 | 编号 | 标题 | 简述 |
|------|------|------|------|
| 41 | 85 | P2D Fast Solver | P2D模型快速求解 |
| 42 | 86 | PyBaMM DFN Model | PyBaMM开源实现 |
| 43 | 87 | DFN Parameter Identification | DFN模型参数辨识 |
| 44 | 192 | JES Parameterized OCV | 参数化OCV模型 |
| 45 | 194 | Real-time SOC OCV Curve | 实时SOC估计 |
| 46 | 195 | OCV Relaxation SOC-SOH | OCV弛豫方法 |
| 47 | 196 | OCV Temperature Relation | OCV温度关系 |
| 48 | 197 | Hysteresis OCV Model | OCV迟滞模型 |
| 49 | 242 | Electrochimica Acta EIS | EIS状态估计 |
| 50 | 255 | Energy Battery Modeling Review | 电池建模综述 |

### 3.2 热模型详细（8篇）

| 排名 | 编号 | 标题 | 简述 |
|------|------|------|------|
| 51 | 142 | Pseudo-3D Thermal EV | 伪3D热模型 |
| 52 | 143 | Coupled Electro-Thermal EV | 电-热耦合 |
| 53 | 144 | Thermal-Electrochemical Penn State | 完整微分方程组 |
| 54 | 146 | Electro-Thermal Abuse (Applied Energy) | 热滥用模型 |
| 55 | 147 | Nonisothermal Modeling | 非等温建模 |
| 56 | 148 | Thermal Dynamics (Nature SR) | 热动力学 |
| 57 | 251 | IJHMT Battery Thermal | 热传递模型 |
| 58 | 252 | Applied Thermal Engineering | 热管理工程 |

### 3.3 老化机制详细（10篇）

| 排名 | 编号 | 标题 | 简述 |
|------|------|------|------|
| 59 | 88 | Nature Energy Aging | Nature Energy老化机制 |
| 60 | 89 | Joule Decade Insights | Joule十年洞察 |
| 61 | 92 | Nature Energy Cycle Life | 循环寿命预测 |
| 62 | 118 | Aging Matrix Cycling | 循环老化矩阵 |
| 63 | 119 | Calendar Aging Model | 日历老化模型 |
| 64 | 235 | PCCP Degradation Modeling | 老化建模指南 |
| 65 | 264 | Nano Letters SEI | SEI层演化 |
| 66 | 270 | ACS Nano Aging Nanoscale | 纳米尺度老化 |
| 67 | 139 | SEI Growth Nature Comm | SEI时空生长 |
| 68 | 135 | Coulombic Efficiency 99.9% | 库仑效率研究 |

### 3.4 网络功耗详细（7篇）

| 排名 | 编号 | 标题 | 简述 |
|------|------|------|------|
| 69 | 150 | WiFi Power Revisited | WiFi功耗重审 |
| 70 | 151 | WiFi Transmission TMC | WiFi传输功耗 |
| 71 | 152 | Power Modeling Polimi | Polimi功耗模型 |
| 72 | 222 | SIGCOMM 5G Energy | 5G能耗测量 |
| 73 | 223 | CoNEXT 5G | 5G网络能效 |
| 74 | 38 | 5G Power Modeling | 5G功耗建模 |
| 75 | 52 | Signal Strength Battery | 信号强度影响 |

### 3.5 传感器与相机（5篇）

| 排名 | 编号 | 标题 | 简述 |
|------|------|------|------|
| 76 | 45 | GPS Energy SenSys | GPS能耗 |
| 77 | 102 | Camera Energy Saving | 相机节能 |
| 78 | 169 | IMU Power Gait | IMU功耗 |
| 79 | 173 | Video Streaming Energy | 视频流能耗 |
| 80 | 177 | Acoustic Monitoring Power | 音频监控功耗 |

---

## 第四梯队：一般参考文献（60篇）

> 这些文献提供背景知识或特定细节，按需查阅

### 4.1 用户行为与应用（15篇）

| 编号 | 标题 | 简述 |
|------|------|------|
| 49 | Carat User Study | 用户行为研究 |
| 50 | Usage Patterns | 使用模式 |
| 51 | User Battery Perception | 用户感知 |
| 63-70 | App Energy Profiling系列 | 应用能耗分析 |
| 201 | CHI Battery Monetary | 电池货币价值 |
| 202 | CHI Carat Behavior | Carat用户行为 |
| 203 | HBI Interaction | 人-电池交互 |
| 204 | IMC Usage Patterns | 使用模式分析 |
| 253 | CSCW Collaborative | 协作电池感知 |
| 276 | UbiComp Perception | 用户感知研究 |

### 4.2 系统架构与OS（10篇）

| 编号 | 标题 | 简述 |
|------|------|------|
| 205 | ASPLOS OS Power | OS级功耗管理 |
| 206 | HPCA Standby | 待机功耗优化 |
| 209 | UX-Driven CPU | UX驱动调频 |
| 210 | Processor Tradeoff | 处理器能效权衡 |
| 245 | TIE Energy | 工业电子能效 |
| 246 | OSDI OS | OS功耗管理 |
| 247 | EuroSys EAS | 能效调度 |
| 248 | ISCA Mobile | 移动处理器功耗 |
| 271 | ASPLOS Memory | 内存功耗 |
| 272 | FAST Storage | 存储功耗 |

### 4.3 充电与BMS（12篇）

| 编号 | 标题 | 简述 |
|------|------|------|
| 126-130 | Fast Charging系列 | 快充影响 |
| 158-160 | Charging Strategy | 充电策略 |
| 207 | BMS State Estimation | BMS状态估计 |
| 208 | SOC Balancing | SOC均衡 |
| 211-216 | TPEL Charging | 充电器电路 |

### 4.4 材料科学（10篇）

| 编号 | 标题 | 简述 |
|------|------|------|
| 241 | Adv Energy Mat | 高能量密度 |
| 254 | Adv Energy Mat | 先进电池 |
| 261 | Nature Mat Li-ion | 材料综述 |
| 262 | ACS Nano Si Anode | 硅负极 |
| 263 | ACS Energy Fast Charge | 快充机制 |
| 265 | ACS Energy Health | 健康诊断 |
| 266 | Nature Mat Kinetics | 动力学 |
| 267 | ACS Nano Thermal | 热特性 |
| 268 | ACS Energy Electrolyte | 电解质 |
| 269 | Nano Lett Dendrite | 锂枝晶 |

### 4.5 环境因素（8篇）

| 编号 | 标题 | 简述 |
|------|------|------|
| 26 | Humidity Degradation JPS | 湿度老化 |
| 79-80 | Low Temperature | 低温性能 |
| 131-134 | Humidity系列 | 湿度影响 |
| 273 | Atmospheric Pressure | 气压影响 |

### 4.6 其他（5篇）

| 编号 | 标题 | 简述 |
|------|------|------|
| 07 | Sudden Drop Battery | 电池突降 |
| 274 | MobiCom Background | 后台应用 |
| 275 | TPEL Pack Design | 电池包设计 |
| 93 | BatteryML Platform | ML平台 |
| 155 | NIST Power Measurements | NIST测量 |

---

## 第五梯队：低优先级文献（140篇）

> 其余文献与核心建模任务关联较弱，仅在需要特定细节时查阅

包括：
- 纯ML/黑箱方法（与题目"非黑箱"要求冲突）
- 纯硬件/电路设计（非建模层面）
- 高度特化的材料研究
- 与智能手机关联弱的EV/大型储能研究

**第五梯队文献编号列表**：
04, 07, 08, 10, 12, 14, 16-20, 21-24, 25, 27-34, 36-37, 39-44, 46-48, 53-58, 59-62, 64-68, 70-78, 83-84, 90, 93-100, 103, 105-107, 109, 111-113, 115-117, 120, 126-134, 136-138, 140, 153-160, 162-164, 166-168, 170, 172, 175-176, 179-180, 182-190, 193, 198-200, 207-210, 211-220, 224-230, 232-234, 236-237, 239-241, 243-250, 253-254, 256-263, 267-269, 274-276

---

## 建模路线图建议

根据文献排序，建议按以下顺序构建模型：

### 阶段1：基础电池模型
**必读文献**：277, 35, 191, 279

$$\frac{dSOC}{dt} = -\frac{I(t)}{Q_{nom} \cdot SOH}$$
$$V(t) = U_{oc}(SOC, T) - I(t) \cdot R(SOC, T) - V_{RC}(t)$$

### 阶段2：功耗分解模型
**必读文献**：278, 178, 174, 181

$$P_{total}(t) = P_{display} + P_{CPU} + P_{network} + P_{GPS} + P_{sensors} + P_{background}$$
$$I(t) = \frac{P_{total}(t)}{V(t)}$$

### 阶段3：温度耦合模型
**必读文献**：141, 122, 279

$$mC_p\frac{dT}{dt} = I^2R + h(T_{amb} - T)$$
$$R(T) = R_{ref} \cdot \exp\left[-\frac{E_a}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]$$

### 阶段4：老化模型（可选扩展）
**必读文献**：238, 110, 88

$$\frac{dSOH}{dt} = -f(I, T, SOC, t)$$

### 阶段5：耗尽时间预测
**必读文献**：280

$$t_{empty} = \int_{SOC}^{SOC_{min}} \frac{Q_{nom} \cdot SOH}{I(V, P_{load})} dSOC$$

---

## 数据资源推荐

| 优先级 | 数据集 | 用途 | 来源文献 |
|--------|--------|------|----------|
| ★★★★★ | NASA PCoE | 老化验证 | 91, 108 |
| ★★★★★ | 3W's UCSD | 功耗数据 | 178 |
| ★★★★☆ | MIT-Stanford | 快充循环 | 108 |
| ★★★★☆ | AndroWatts | 组件功耗 | 174 |
| ★★★☆☆ | Oxford | 日历老化 | 108 |

---

## 完整排序列表

### 按重要性完整排序（前100篇）

| 排名 | 编号 | 类别 | 重要性 |
|------|------|------|--------|
| 1 | 277 | 连续时间建模 | ★★★★★ |
| 2 | 35 | 连续时间ECM | ★★★★★ |
| 3 | 280 | 耗尽时间预测 | ★★★★★ |
| 4 | 145 | 电化学-热模型 | ★★★★★ |
| 5 | 191 | OCV-SOC模型 | ★★★★★ |
| 6 | 278 | 手机功耗模型 | ★★★★★ |
| 7 | 178 | UCSD功耗测量 | ★★★★★ |
| 8 | 174 | 组件功耗分解 | ★★★★★ |
| 9 | 181 | 功耗建模综述 | ★★★★★ |
| 10 | 11 | 移动能耗综述 | ★★★★★ |
| 11 | 279 | 温度参数 | ★★★★★ |
| 12 | 122 | Peukert温度 | ★★★★★ |
| 13 | 141 | 热模型综述 | ★★★★★ |
| 14 | 238 | 通用老化模型 | ★★★★★ |
| 15 | 110 | 老化机制综述 | ★★★★★ |
| 16 | 01 | EKF SOC | ★★★★☆ |
| 17 | 02 | 电化学SOC | ★★★★☆ |
| 18 | 05 | JPS SOC框架 | ★★★★☆ |
| 19 | 03 | 在线SOC-SOH | ★★★★☆ |
| 20 | 06 | SOC老化温度 | ★★★★☆ |
| 21 | 81 | SPM SOC | ★★★★☆ |
| 22 | 82 | P2D粒子滤波 | ★★★★☆ |
| 23 | 231 | 联合SOC-SOH | ★★★★☆ |
| 24 | 09 | CPU功耗 | ★★★★☆ |
| 25 | 13 | GPU功耗 | ★★★★☆ |
| 26 | 149 | WiFi功耗 | ★★★★☆ |
| 27 | 161 | GPS功耗 | ★★★★☆ |
| 28 | 165 | 传感器功耗 | ★★★★☆ |
| 29 | 15 | 后台功耗 | ★★★★☆ |
| 30 | 221 | 5G功耗 | ★★★★☆ |
| 31 | 171 | 视频通话 | ★★★★☆ |
| 32 | 101 | AP功耗 | ★★★★☆ |
| 33 | 104 | 视频播放 | ★★★★☆ |
| 34 | 121 | Peukert JES | ★★★★☆ |
| 35 | 123 | Peukert JPS | ★★★★☆ |
| 36 | 124 | 广义Peukert | ★★★★☆ |
| 37 | 125 | Peukert容量 | ★★★★☆ |
| 38 | 108 | 数据集对比 | ★★★★☆ |
| 39 | 91 | NASA数据 | ★★★★☆ |
| 40 | 114 | 21700数据 | ★★★★☆ |
| 41 | 85 | P2D快速求解 | ★★★☆☆ |
| 42 | 86 | PyBaMM | ★★★☆☆ |
| 43 | 87 | DFN参数 | ★★★☆☆ |
| 44 | 192 | JES OCV | ★★★☆☆ |
| 45 | 194 | 实时SOC | ★★★☆☆ |
| 46 | 195 | OCV弛豫 | ★★★☆☆ |
| 47 | 196 | OCV温度 | ★★★☆☆ |
| 48 | 197 | OCV迟滞 | ★★★☆☆ |
| 49 | 242 | EIS估计 | ★★★☆☆ |
| 50 | 255 | 建模综述 | ★★★☆☆ |
| 51 | 142 | 伪3D热 | ★★★☆☆ |
| 52 | 143 | 电热耦合 | ★★★☆☆ |
| 53 | 144 | Penn State | ★★★☆☆ |
| 54 | 146 | 热滥用 | ★★★☆☆ |
| 55 | 147 | 非等温 | ★★★☆☆ |
| 56 | 148 | 热动力学 | ★★★☆☆ |
| 57 | 251 | IJHMT热 | ★★★☆☆ |
| 58 | 252 | 热工程 | ★★★☆☆ |
| 59 | 88 | NE老化 | ★★★☆☆ |
| 60 | 89 | Joule洞察 | ★★★☆☆ |
| 61 | 92 | NE循环 | ★★★☆☆ |
| 62 | 118 | 老化矩阵 | ★★★☆☆ |
| 63 | 119 | 日历老化 | ★★★☆☆ |
| 64 | 235 | PCCP老化 | ★★★☆☆ |
| 65 | 264 | SEI演化 | ★★★☆☆ |
| 66 | 270 | 纳米老化 | ★★★☆☆ |
| 67 | 139 | SEI生长 | ★★★☆☆ |
| 68 | 135 | 库仑效率 | ★★★☆☆ |
| 69 | 150 | WiFi重审 | ★★★☆☆ |
| 70 | 151 | WiFi TMC | ★★★☆☆ |
| 71 | 152 | Polimi | ★★★☆☆ |
| 72 | 222 | 5G SIGCOMM | ★★★☆☆ |
| 73 | 223 | CoNEXT 5G | ★★★☆☆ |
| 74 | 38 | 5G建模 | ★★★☆☆ |
| 75 | 52 | 信号强度 | ★★★☆☆ |
| 76 | 45 | GPS SenSys | ★★★☆☆ |
| 77 | 102 | 相机节能 | ★★★☆☆ |
| 78 | 169 | IMU功耗 | ★★★☆☆ |
| 79 | 173 | 视频流 | ★★★☆☆ |
| 80 | 177 | 音频功耗 | ★★★☆☆ |
| 81-100 | 见第四梯队 | 一般参考 | ★★☆☆☆ |

---

## 总结

### 必读核心15篇（按优先级）

1. **277** - 连续时间建模方法论
2. **35** - 连续时间ECM
3. **280** - 耗尽时间预测
4. **145** - 实用电化学-热模型
5. **191** - OCV-SOC模型综述
6. **278** - 完整手机功耗模型
7. **178** - UCSD 3W's功耗测量
8. **174** - AndroWatts组件功耗
9. **181** - 功耗建模综述
10. **11** - 移动能耗建模综述
11. **279** - 温度依赖参数
12. **122** - Peukert温度扩展
13. **141** - 热模型综述
14. **238** - 通用老化模型
15. **110** - 老化机制综述

### 建模关键方程

```
核心SOC动力学:
dSOC/dt = -I(t)/(Q_nom × SOH)

电压模型:
V(t) = U_oc(SOC,T) - I(t)×R(SOC,T) - V_RC(t)

功耗分解:
P_total = Σ P_component(state, parameters)

热动力学:
dT/dt = (I²R - h×ΔT)/(m×Cp)

耗尽时间:
t_empty = ∫[SOC→0] Q/(I(P)) dSOC
```

---

*文档生成时间: 2026年1月30日*
*基于280篇文献的系统性评估*
