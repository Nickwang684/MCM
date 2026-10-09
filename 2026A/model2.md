# 2026 MCM Problem A 文献重要性排序

> 智能手机电池续航的连续时间建模 - **340篇文献**按重要性分级（292个.md + 48个.pdf）

---

## 一、题目核心需求回顾

根据原始题目PDF的分析，2026 MCM Problem A的核心要求：

| 需求 | 描述 | 关键词 |
|------|------|--------|
| **连续时间模型** | SOC作为时间的连续函数，非离散/黑箱方法 | 微分方程、积分 |
| **耗尽时间预测** | 预测电池完全放电的剩余时间 | 续航预测 |
| **功耗因素整合** | 屏幕、CPU、网络、GPS、传感器等 | 组件功耗模型 |
| **环境因素** | 温度、湿度、气压的影响 | 热模型、环境依赖 |
| **电池老化** | 容量衰减、循环寿命 | SOH、老化机制 |
| **敏感性分析** | 参数变化对预测的影响 | 不确定性量化 |
| **实用建议** | 用户行为优化、OS节能策略 | 应用指导 |

**重要约束**：必须是显式连续时间模型，禁止纯离散曲线拟合、时间步长回归或黑箱机器学习。

---

## 二、重要性评分标准

### S级（10分）- 核心必读
- 直接解决题目核心问题
- 提供可直接使用的连续时间模型框架
- 必须引用的经典文献

### A级（8-9分）- 关键参考
- 提供核心方法或关键数据
- 解决某个重要子问题
- 高质量的综述或基准

### B级（6-7分）- 重要补充
- 提供有用的方法参考
- 补充特定领域知识
- 有价值的实验数据

### C级（4-5分）- 背景参考
- 提供背景知识
- 特定场景下有用
- 可选择性阅读

### D级（1-3分）- 专业背景
- 相关性较低
- 过于专业或边缘
- 仅作知识储备

---

## 三、第一梯队：核心必读（S级，19篇）

这些论文直接解决题目核心问题，是建模的基础和必引文献。

### 3.1 S级论文列表

| 优先级 | 编号/文件名 | 类型 | 标题/描述 | 核心价值 | 分数 |
|--------|-------------|------|-----------|----------|------|
| 1 | **Evaluation_of_Li-Based_Battery...Mobile_Phones.pdf** | PDF | IEEE Access 2020 手机电池测量 | **最直接匹配**：Vivo/Motorola手机6款App放电电流/电压/温度实测，提供PDF/NDF统计分布 | 10 |
| 2 | **Evaluation of in-service smartphone battery drainage...video calling.pdf** | PDF | Scientific Reports 2023 视频通话功耗 | **视频通话**：8款App（Zoom/WhatsApp等）完整放电profile | 10 |
| 3 | **Carroll.pdf** | PDF | USENIX 手机功耗分析 | **经典功耗分解**：CPU/RAM/GPS/WiFi/屏幕/音频逐组件功耗测量与模型 | 10 |
| 4 | **277** | MD | Applied Energy连续时间建模 | **直接匹配**：连续时间ECM模型，SOC动态方程 | 10 |
| 5 | **278** | MD | IEEE Access完整手机功耗模型 | **核心框架**：智能手机全组件功耗模型 | 10 |
| 6 | **280** | MD | Energy耗尽时间预测 | **直接匹配**：续航预测数学模型 | 10 |
| 7 | **178** | MD | UCSD 3W's功耗分析 | **精确数据**：最新智能手机功耗测量 | 10 |
| 8 | **199** | MD | Georgia Tech综合电池模型 | **经典模型**：电池动态特性综合建模 | 10 |
| 9 | **35** | MD | 连续时间ECM辨识 | **核心方法**：ECM参数连续时间辨识 | 10 |
| 10 | **Power Review** | MD | 智能手机功耗综述 | **最新综述**：2024年功耗分析综述 | 10 |
| 11 | **A Study of Model Based Protective Fast Charging...Smartphone Cells.pdf** | PDF | Adv. Energy Mater. 2021 | **智能手机快充**：LG-G5物理模型充电，锂沉积老化机制 | 10 |
| 12 | **01** | MD | EKF SOC估计 | **基础方法**：扩展卡尔曼滤波SOC估计 | 9 |
| 13 | **191** | MD | OCV模型综述 | **关键关系**：OCV-SOC曲线建模方法 | 9 |
| 14 | **106** | MD | 功耗建模综述 | **方法论**：移动设备功耗建模综述 | 9 |
| 15 | **67** | MD | 准确续航预测 | **预测方法**：电池续航精确预测 | 9 |
| 16 | **73** | MD | Sandra移动感知功耗 | **实用模型**：移动设备感知功耗预测 | 9 |
| 17 | **231** | MD | 联合SOC-SOH估计 | **综合方法**：状态联合估计框架 | 9 |
| 18 | **207** | MD | BMS状态估计综述 | **系统综述**：电池管理系统状态估计 | 9 |
| 19 | **86** | MD | PyBaMM DFN模型 | **计算工具**：开源电化学模型实现 | 9 |

### 3.2 S级论文阅读顺序建议

```
Week 1: 框架建立
Day 1-2: Evaluation_Mobile_Phones.pdf → Carroll.pdf → 178 (功耗测量)
Day 3-4: 277 (连续时间ECM) → 35 (ECM辨识) → 199 (综合电池模型)
Day 5-7: 278 (手机功耗模型) → 280 (耗尽预测) → 01 (EKF SOC)

Week 2: 深化理解
Day 1-2: A Study of Model Based...Smartphone.pdf (快充老化)
Day 3-4: 191 (OCV模型) → 231 (SOC-SOH联合) → 207 (BMS综述)
Day 5-7: Power Review → 106 (功耗综述) → 86 (PyBaMM)
```

---

## 四、第二梯队：关键参考（A级，59篇）

### 4.1 A级PDF论文（10篇）

| 文件名 | 标题/描述 | 核心价值 | 分数 |
|--------|-----------|----------|------|
| **Physics-based prognostics of implantable-grade lithium-ion battery.pdf** | JPS 2021 RUL预测 | 半电池模型，LAMPE/LAMNE/LLI退化参数追踪 | 9 |
| **Probabilistic machine learning for battery health diagnostics.pdf** | npj Materials 2024 | 概率ML综述：GPR/RVM/BNN在SOH/RUL预测 | 9 |
| **Deep neural network battery charging curve prediction.pdf** | Joule 2021 | DNN预测完整充电曲线，迁移学习 | 9 |
| **Bernardi_1985_J._Electrochem._Soc._132_5.pdf** | JES 1985 经典热方程 | $\dot{q}=I(U_{OCV}-V)-IT\frac{\partial U_{OCV}}{\partial T}$ | 9 |
| **What is keeping my phone awake...no-sleep energy bugs.pdf** | MobiSys | Android能耗Bug分类与检测工具 | 8 |
| **Extending battery life A low-cost practical diagnostic.pdf** | JPS 2016 | DTV微分热电压法诊断SOH | 8 |
| **Smart batteries for powering the future.pdf** | Joule 2024 综述 | 智能电池：传感器、自修复、AI决策 | 8 |
| **Thermal Runaway of Lithium-Ion Batteries.pdf** | Joule 2018 | 热失控机制：阴极释氧化学串扰 | 8 |
| **Code smells analysis for android applications.pdf** | Sci. Rep. 2024 | Android代码异味与电池消耗回归模型 | 8 |
| **Automatic battery charging system on android.pdf** | IOP 2020 | Android充电控制系统设计 | 8 |

### 4.2 A级MD论文 - 电池模型核心（12篇）

| 编号 | 标题/描述 | 核心价值 | 分数 |
|------|-----------|----------|------|
| 02 | 物理基础电化学SOC | 电化学SOC方法 | 8 |
| 03 | 在线SOC-SOH估计 | 实时估计算法 | 8 |
| 05 | 实用SOC框架JPS | 工程可用SOC框架 | 8 |
| 36 | ECM参数优化 | ECM参数估计方法 | 8 |
| 37 | JPS ECM比较研究 | ECM模型对比 | 8 |
| 81 | SPM单粒子模型 | 简化电化学模型 | 8 |
| 82 | P2D伪二维模型 | 详细电化学模型 | 8 |
| 192 | JES参数化OCV | OCV曲线参数化 | 8 |
| 193 | 温度依赖OCV | 温度对OCV影响 | 8 |
| 232 | Energy SOC综述 | SOC方法综合比较 | 8 |
| 233 | 自适应SOC估计 | 自适应滤波方法 | 8 |
| 279 | JPS温度依赖参数 | 温度参数建模 | 9 |

### 4.3 A级MD论文 - 硬件功耗模型（15篇）

| 编号 | 标题/描述 | 核心价值 | 分数 |
|------|-----------|----------|------|
| 09 | 多核CPU功耗模型 | CPU功耗建模 | 8 |
| 10 | 自适应功耗建模 | 动态功耗适应 | 8 |
| 13 | GPU功耗模型 | GPU能耗建模 | 8 |
| 21 | OLED屏幕功耗 | 屏幕功耗模型 | 8 |
| 22 | 屏幕能耗分析 | 屏幕占比38-50% | 8 |
| 38 | 5G功耗基础 | 5G网络功耗 | 8 |
| 39 | 5G能效分析 | 5G能效特性 | 8 |
| 149 | WiFi功耗ICDCS | WiFi功耗建模 | 8 |
| 150 | WiFi功耗WoWMoM | WiFi功耗优化 | 8 |
| 161 | GPS功耗TMC | GPS能耗模型 | 8 |
| 165 | SensingKit传感器 | 传感器功耗 | 8 |
| 171 | 视频通话功耗 | 相机/视频功耗 | 8 |
| 221 | SIGCOMM 5G功耗 | 5G实测数据 | 8 |
| 222 | SIGCOMM 5G能耗 | 5G能耗分析 | 8 |
| 181 | 能耗估算综述 | 应用能耗估算 | 8 |

### 4.4 A级MD论文 - 温度与热模型（10篇）

| 编号 | 标题/描述 | 核心价值 | 分数 |
|------|-----------|----------|------|
| 59 | 热管理综述 | 电池热管理 | 8 |
| 60 | 温度效应分析 | 温度影响机制 | 8 |
| 79 | 低温性能 | 低温运行特性 | 8 |
| 80 | 低温放电 | 低温放电曲线 | 8 |
| 141 | 电热耦合综述JES | 耦合模型综述 | 8 |
| 145 | 实用电热BMS | 工程热模型 | 8 |
| 146 | 电热正常到滥用 | 热安全建模 | 8 |
| 148 | 热动力学Nature | 温度动态特性 | 8 |
| 251 | 热建模IJHMT | 热传递模型 | 8 |
| **Thermal Review** | MD | 热管理综述 | 最新热管理方法 | 9 |

### 4.5 A级MD论文 - 电池老化（12篇）

| 编号 | 标题/描述 | 核心价值 | 分数 |
|------|-----------|----------|------|
| 88 | Nature Energy老化机制 | 老化机理经典 | 9 |
| 89 | Joule十年洞察 | 长期老化研究 | 8 |
| 90 | Joule老化预测 | 老化预测模型 | 8 |
| 92 | Nature Energy寿命预测 | 数据驱动寿命 | 8 |
| 110 | 降解失效综述 | 老化机制全面 | 8 |
| 113 | 日历老化内阻 | 日历老化模型 | 8 |
| 118 | 老化矩阵协议 | 老化测试方法 | 8 |
| 119 | 半经验日历模型 | 日历老化公式 | 8 |
| 235 | PCCP老化建模 | PyBaMM老化 | 8 |
| 238 | 通用老化模型 | 化学无关模型 | 8 |
| 256 | 老化数据集 | 老化数据资源 | 8 |
| 260 | Nature Comm老化异质 | 老化非均匀性 | 8 |

---

## 五、第三梯队：重要补充（B级，80篇）

### 5.1 B级PDF论文（12篇）

| 文件名 | 描述 | 分数 |
|--------|------|------|
| 储能锂离子电池容量衰减机制和寿命预测综述_马悦.pdf | 中文综述 | 7 |
| 基于FFRLS-AIEKF的锂离子电池SOC估计_阮爱国.pdf | 自适应EKF | 7 |
| 基于改进无迹卡尔曼滤波的锂电池SOC估计方法_程竹明.pdf | 改进UKF | 7 |
| 基于SUKF-EKF融合的锂电池状态估计方法_王期文.pdf | 融合滤波 | 7 |
| 基于AFFRLS-MIASRCKF算法的锂电池SOC估计_王保德.pdf | SRCKF算法 | 7 |
| 基于FFRLS-AUKF算法的锂离子电池SOC估计_卓世龙.pdf | AUKF算法 | 7 |
| 考虑多时间尺度特性的锂离子电池建模与参数辨识_夏永凯.pdf | 多尺度ECM | 7 |
| Advanced Energy Materials - 2025 - Li - Mechanistic Considerations for Battery Charging Protocol Design.pdf | 充电协议 | 7 |
| Formation Challenges of Lithium-Ion Battery Manufacturing.pdf | 制造工艺 | 6 |
| Liquid electrolyte The nexus of practical lithium metal batteries.pdf | 电解质综述 | 6 |
| Modeling and simulation of dual-battery FANET system using MADRL.pdf | 多智能体优化 | 6 |
| 3132062.3132066.pdf / 3173162.3173188.pdf / 3636534.3695905.pdf | ACM论文 | 6 |

### 5.2 B级MD论文 - Peukert效应与放电倍率（8篇）

| 编号 | 标题/描述 | 分数 |
|------|-----------|------|
| 61 | Peukert方程基础 | 7 |
| 62 | Peukert应用 | 7 |
| 121 | Peukert批判JES | 7 |
| 122 | Peukert温度JPS | 7 |
| 123 | Peukert综述JPS 2006 | 6 |
| 124 | 锂离子Peukert扩展 | 7 |
| 125 | Peukert容量评估 | 6 |
| 196 | OCV放电率依赖 | 7 |

### 5.3 B级MD论文 - 用户行为与应用（12篇）

| 编号 | 标题/描述 | 分数 |
|------|-----------|------|
| 15 | 后台能耗MobiCom | 7 |
| 49 | Carat用户行为 | 7 |
| 50 | 用户使用模式 | 7 |
| 51 | 使用习惯分析 | 6 |
| 201 | CHI电池货币价值 | 7 |
| 202 | CHI Carat研究 | 7 |
| 203 | HBI人机交互 | 7 |
| 204 | IMC使用模式 | 7 |
| 253 | CSCW协作感知 | 6 |
| 274 | MobiCom后台应用 | 7 |
| 276 | UbiComp电池感知 | 7 |
| 259 | UbiComp应用分析 | 6 |

### 5.4 B级MD论文 - 其他（48篇）
- 应用层功耗：16-20, 63-65, 182, 189
- 网络功耗详细：11-12, 40, 52, 151, 156-157, 223-225
- 传感器与GPS：45-48, 162-164, 166-167, 258
- 充电与快充：126-130, 158-160, 211-212
- SOC/SOH进阶：04, 06-08, 116-117, 236-237

---

## 六、第四梯队：背景参考（C级，107篇）

### 6.1 C级PDF论文（12篇）

| 文件名 | 描述 | 分数 |
|--------|------|------|
| 基于灰狼优化算法和组合核函数GPR模型的锂电池剩余使用寿命预测_胡林静.pdf | 机器学习RUL | 5 |
| 基于遗传算法优化BP神经网络的锂电池容量预测研究_何法.pdf | GA-BP预测 | 5 |
| 基于阻抗与扩展卡尔曼滤波的锂离子电池荷电状态估计方法研究_徐浩楠.pdf | EIS+EKF | 5 |
| 基于应变和温度的锂离子电池荷电状态_穆玉航.pdf | 应变传感 | 5 |
| Advanced Energy Materials - 2025 - Liu - Designing Advanced Separators.pdf | 隔膜设计 | 4 |
| The advanced copper oxide coating separator.pdf | 隔膜涂层 | 4 |
| Influence of electrolyte conductivity on the performance.pdf | 电解质电导率 | 4 |
| Lithium-rich borate coated LiMn0.6Fe0.4PO4 cathodes.pdf | 正极材料 | 4 |
| Electrocapillary boosting electrode wetting.pdf | 电极润湿 | 4 |
| 1-s2.0-S0013468624003888-main.pdf | Electrochimica Acta | 4 |
| 1-s2.0-S0013468623005406-main.pdf | Electrochimica Acta | 4 |
| 1-s2.0-S0013468624014749-main.pdf | Electrochimica Acta | 4 |

### 6.2 C级MD论文（95篇）
- 电化学详细：82-87, 97-99, 242-243, 255, 266, 270
- SEI与库仑效率：135-140, 243, 264
- 湿度与环境：26, 131-134, 273
- 热模型详细：142-144, 147, 240, 252, 267, 279
- 音频/震动/相机：96, 102-104, 172-180
- OS与架构：205-206, 209-210, 245-248, 257, 271-272
- 充电器电路：213-220, 275
- 数据集资源：30, 91, 93, 108, 114, 256
- ML/数据驱动：14, 111, 117, 120, 234, 236, 244, 265
- 其他应用相关：66-72, 74-76, 152-155, 183-188

---

## 七、第五梯队：专业背景（D级，75篇）

### 7.1 D级PDF论文（10篇）

| 文件名 | 描述 | 分数 |
|--------|------|------|
| A Compact Nanoconfined Sulfur Cathode for High-Performance Lithium-Sulfur Batteries.pdf | 锂硫电池 | 2 |
| Acetylene black interlayer regulated sulfur deposition for lithium-sulfur batteries.pdf | 锂硫电池 | 2 |
| Silicon Nanowires and Lithium Cobalt Oxide Nanowires in Graphene.pdf | 纳米材料 | 2 |
| High Areal Energy Density 3D Lithium-Ion Microbatteries.pdf | 微电池 | 2 |
| 1-s2.0-S0378775304003593-main.pdf | JPS材料 | 2 |
| 1-s2.0-S0378775305000832-main.pdf | JPS材料 | 2 |
| 基于FFRLS-AIEKF的锂离子电池SOC估计_阮爱国 (1).pdf | 重复文件 | 1 |

### 7.2 D级MD论文（65篇）
- 材料科学：241, 254, 261-262, 267-268, 269
- 先进电池技术（非手机）
- 安全与诊断专用
- 基础测量
- EV/Pack级别等非手机场景
- 历史/早期文献（2010年前）

---

## 八、统计摘要

| 等级 | MD论文 | PDF论文 | 合计 | 占比 | 阅读优先级 |
|------|--------|---------|------|------|------------|
| S级 | 15 | 4 | **19** | 5.6% | 必读 |
| A级 | 49 | 10 | **59** | 17.4% | 重点读 |
| B级 | 68 | 12 | **80** | 23.5% | 选择读 |
| C级 | 95 | 12 | **107** | 31.5% | 参考 |
| D级 | 65 | 10 | **75** | 22.1% | 备用 |
| **总计** | **292** | **48** | **340** | 100% | - |

---

## 九、Top 25必读清单

按阅读顺序排列：

### 智能手机专用论文（最高优先）
1. **Evaluation_of_Li-Based_Battery...Mobile_Phones.pdf** - 手机App放电实测（IEEE Access 2020）
2. **Evaluation of in-service smartphone...video calling.pdf** - 视频通话功耗（Sci. Rep. 2023）
3. **Carroll.pdf** - 手机硬件功耗分解经典
4. **A Study of Model Based...Smartphone Cells.pdf** - 智能手机快充老化（Adv. Energy Mater. 2021）

### 电池模型核心
5. **277** - Applied Energy连续时间ECM（框架基础）
6. **35** - ECM参数辨识（建模方法）
7. **199** - Georgia Tech综合电池模型（经典参考）
8. **01** - EKF SOC估计（核心算法）

### 功耗建模
9. **278** - IEEE Access手机功耗模型（功耗框架）
10. **178** - UCSD 3W's功耗测量（精确数据）
11. **106** - 功耗建模综述（方法论）

### 续航预测
12. **280** - Energy耗尽预测（预测模型）
13. **67** - 准确续航预测（预测方法）
14. **73** - Sandra移动感知（实用预测）

### 电池科学
15. **Bernardi_1985.pdf** - 经典热生成方程
16. **Physics-based prognostics.pdf** - RUL预测物理模型
17. **191** - OCV模型综述（电压模型）
18. **231** - SOC-SOH联合估计（综合方法）

### 老化与温度
19. **88** - Nature Energy老化机制（老化核心）
20. **59** - 热管理综述（温度建模）
21. **Thermal Review** - 热管理最新综述

### 综述与工具
22. **Power Review** - 智能手机功耗综述
23. **Probabilistic ML.pdf** - 概率机器学习综述
24. **Smart batteries.pdf** - 智能电池综述
25. **86** - PyBaMM DFN（计算工具）

---

## 十、按题目需求的文献映射

### 10.1 连续时间SOC模型
**核心PDF**：Physics-based prognostics.pdf, Bernardi_1985.pdf
**核心MD**：277, 35, 199, 01, 191
**补充**：02, 03, 05, 36, 81-86

### 10.2 功耗因素整合
**核心PDF**：Carroll.pdf, Evaluation_Mobile_Phones.pdf, Code smells.pdf
**屏幕**：21, 22, 23, 24
**CPU/GPU**：09, 10, 13, 14, 101
**网络**：38-40, 149-157, 221-230
**GPS/传感器**：45-48, 161-170
**应用**：15-20, 63-70, 181-190

### 10.3 耗尽时间预测
**核心**：280, 67, 73, 278
**PDF补充**：Deep neural network.pdf, Extending battery life.pdf
**补充**：17, 74-76

### 10.4 环境因素
**温度PDF**：Thermal Runaway.pdf
**温度MD**：59-60, 79-80, 141-148, Thermal Review
**湿度**：26, 131-134
**气压**：273

### 10.5 电池老化
**核心PDF**：A Study of Model Based...Smartphone.pdf, Probabilistic ML.pdf
**核心MD**：88, 89, 90, 92, 110
**补充**：113, 118-119, 235, 238, 260

### 10.6 敏感性分析
**方法**：参考106综述中的敏感性方法
**PDF**：Probabilistic ML.pdf (贝叶斯不确定性)
**数据**：30, 91, 92, 108, 114

### 10.7 用户行为与建议
**PDF**：What is keeping my phone awake.pdf, Code smells.pdf
**行为分析**：49-51, 201-204
**节能策略**：205-206, 209-210

---

## 附录A：关键公式来源

| 公式类型 | 主要来源论文 |
|----------|--------------|
| SOC微分方程 | 277, 01, 199, Physics-based.pdf |
| OCV-SOC关系 | 191, 192, 193, Bernardi_1985.pdf |
| 功耗加和模型 | 278, 178, 106, Carroll.pdf |
| 温度修正系数 | 59, 79, 141, 279, Thermal Runaway.pdf |
| 老化容量衰减 | 88, 110, 119, Smartphone Cells.pdf |
| Peukert修正 | 121, 122, 124 |
| 耗尽时间积分 | 280, 67 |
| 热生成方程 | Bernardi_1985.pdf |

---

## 附录B：48个PDF论文完整索引

### S级（4篇）
1. Evaluation_of_Li-Based_Battery_Current_Voltage_and_Temperature_Profiles_for_In-Service_Mobile_Phones.pdf
2. Evaluation of in-service smartphone battery drainage profile for video calling feature in major apps.pdf
3. A Study of Model Based Protective Fast Charging and Associated Degradation in Commercial Smartphone Cells...pdf
4. Carroll.pdf

### A级（10篇）
5. Physics-based prognostics of implantable-grade lithium-ion battery for remaining useful life prediction.pdf
6. Probabilistic machine learning for battery health diagnostics and prognostics.pdf
7. Deep neural network battery charging curve prediction using 30 points collected in 10 min.pdf
8. Bernardi_1985_J._Electrochem._Soc._132_5.pdf
9. What is keeping my phone awake...no-sleep energy bugs in smartphone apps.pdf
10. Extending battery life A low-cost practical diagnostic technique for lithium-ion batteries.pdf
11. Smart batteries for powering the future.pdf
12. Thermal Runaway of Lithium-Ion Batteries without Internal Short Circuit.pdf
13. Code smells analysis for android applications and a solution for less battery consumption.pdf
14. Automatic battery charging system on android smartphones.pdf

### B级（12篇）
15-26. 中文论文 + 制造/充电协议论文

### C级（12篇）
27-38. 材料/电解质/隔膜相关

### D级（10篇）
39-48. 锂硫电池/微电池/重复文件

---

*文献重要性排序更新于 2025年*
*基于2026 MCM Problem A题目需求分析*
*包含全部340篇论文（292个.md + 48个.pdf）*
