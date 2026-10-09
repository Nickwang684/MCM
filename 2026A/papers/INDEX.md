# 智能手机电池续航建模文献索引

> 2026年MCM数学建模竞赛 - 智能手机电池续航的连续时间建模

## 文献总览

| 类别 | 编号范围 | 数量 | 状态 |
|------|----------|------|------|
| SOC/SOH估计 | 01-10, 78, 81-90, 116-120, 207-208, 231-239, 244, 265 | ~42篇 | ✅ |
| 屏幕功耗 | 21-24 | ~4篇 | ✅ |
| CPU/GPU功耗 | 09-10, 13-14, 41-44, 101, 205-206, 209-210, 247-248 | ~16篇 | ✅ |
| 内存/存储功耗 | 271-272 | ~2篇 | ✅ |
| 网络功耗 (WiFi/LTE/5G) | 11-12, 38-40, 52, 149-157, 221-230, 249-250 | ~27篇 | ✅ |
| GPS/传感器功耗 | 45-48, 161-170, 258 | ~16篇 | ✅ |
| 相机/音频/震动 | 102-104, 171-180 | ~15篇 | ✅ |
| 应用层功耗 | 15-20, 63-70, 181-190, 259, 274 | ~22篇 | ✅ |
| 温度影响/热模型 | 59-60, 79-80, 141-148, 240, 251-252, 267, 279 | ~20篇 | ✅ |
| 电池老化 | 25-34, 88-100, 110-115, 118-119, 235, 238, 256, 260, 264, 270 | ~32篇 | ✅ |
| Peukert/放电倍率 | 61-62, 121-125 | ~8篇 | ✅ |
| 湿度/气压影响 | 26, 131-134, 273 | ~6篇 | ✅ |
| 库仑效率/SEI | 135-140, 243, 264 | ~8篇 | ✅ |
| 快充影响 | 126-130, 158-160, 211-216, 263, 269 | ~16篇 | ✅ |
| 电化学模型 (SPM/P2D/DFN) | 81-87, 242, 255, 266 | ~10篇 | ✅ |
| ECM模型 | 35-37, 97-99, 277 | ~7篇 | ✅ |
| OCV-SOC关系 | 191-200, 239 | ~11篇 | ✅ |
| 人机交互/用户行为 | 49-51, 201-204, 253, 276 | ~10篇 | ✅ |
| 体系结构/OS功耗管理 | 205-206, 209-210, 245-246, 257 | ~7篇 | ✅ |
| 电力电子/充电器 | 211-220, 275 | ~11篇 | ✅ |
| 材料科学/先进电池 | 241, 254, 261-262, 267-268 | ~6篇 | ✅ |
| 续航预测/完整模型 | 278, 280 | ~2篇 | ✅ |
| 公开数据集 | 30, 91-93, 108, 114 | ~6篇 | ✅ |

---

## 按研究因素分类 (对应idea.md)

### 1. 功耗因素

#### 1.1 屏幕功耗
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 21 | OLED Power Modeling and Optimization | OLED屏幕功耗模型 |
| 22 | Smartphone Display Energy Consumption | 屏幕能耗分析 |
| 23 | Automated OLED Power Modeling | 自动化建模方法 |
| 24 | Display Energy 38-50 Percent | 屏幕占总功耗38-50% |

#### 1.2 处理器负载
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 09 | CPU Power Model Multicore Smartphone | 多核CPU功耗模型 |
| 10 | Adaptive Smartphone Power Modeling | 自适应功耗建模 |
| 13 | GPU Power Model Smartphone | GPU功耗模型 |
| 14 | Neural Network Smartphone Power | 神经网络功耗预测 |
| 41-44 | ARM big.LITTLE, DVFS, EAS | 处理器能效策略 |
| 101 | Mobile AP Power Modeling | 应用处理器功耗 |

#### 1.3 网络活动
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 11-12 | Mobile Energy Modeling Survey, Total Energy | 网络能耗综述 |
| 38-40 | 5G Power Modeling | 5G网络功耗 |
| 52 | Wireless Signal Strength Battery Drain | 信号强度影响 |
| 149-157 | WiFi Power Modeling系列 | WiFi详细功耗模型 |
| 221-222 | SIGCOMM 5G Measurement | 5G实测功耗数据 |
| 223-226 | 5G Energy Efficiency系列 | 5G能效优化 |
| 227-230 | 4G/5G/WiFi能耗建模 | 综合网络功耗 |

#### 1.4 传感器
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 45-48 | GPS Energy, SensingKit, Jigsaw, RAPS | GPS和传感器功耗 |
| 165-170 | 传感器功耗系列 | 加速度计/陀螺仪/IMU |

#### 1.5 音频、震动
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 96 | TI Haptic Energy Consumption | 触觉反馈能耗 |
| 103 | Vibration Feedback Power Perception | 振动功耗与感知 |
| 175-177 | 触觉/音频功耗系列 | ERM/LRA/麦克风 |

#### 1.6 相机
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 102 | Camera Energy Saving Activity Sensing | 相机节能策略 |
| 104 | Video Playback Power Modeling | 视频播放功耗 |
| 171-174 | 视频通话/录像/相机功耗 | 综合相机功耗分析 |

#### 1.7 应用
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 15-20 | Background Energy, WattsOn等 | 后台能耗/应用估算 |
| 63-70 | App Energy Profiling系列 | 应用能耗分析 |
| 181-190 | 应用层功耗分析 | 综合应用功耗建模 |

---

### 2. 环境因素

#### 2.1 温度变化
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 59-60 | Thermal Management LIB, Temperature Effect | 热管理综述 |
| 79-80 | Low Temperature Performance | 低温性能 |
| 141-148 | 电化学-热耦合模型系列 | 热模型详解 |
| 193, 196 | OCV-SOC温度关系 | 温度对电压影响 |

#### 2.2 湿度与气压
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 26 | Humidity Battery Degradation JPS | 湿度对老化影响 |
| 131-134 | 湿度影响系列 | 详细湿度效应 |
| 273 | Atmospheric Pressure Battery | 气压对电池影响 |

---

### 3. 使用历史和充电方式

#### 3.1 使用习惯
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 49-51 | Carat, User Usage Patterns | 用户行为分析 |
| 73-76 | Sandra, Powerlet, SmartDC | 移动感知/预测 |
| 201 | CHI Monetary Battery Life | 电池寿命货币价值评估 |
| 202 | CHI Carat User Behavior | Carat大规模用户研究 |
| 203 | HBI Human-Battery Interaction | 人-电池交互模型 |
| 204 | IMC Smartphone Usage Patterns | 大规模用户使用模式 |

#### 3.2 充电方式
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 126-130 | Fast Charging系列 | 快充对寿命影响 |
| 158-160 | 充电策略/老化 | 充电优化 |
| 211-216 | IEEE TPEL快充/充电器 | 充电器电路与控制 |
| 217-220 | TPEL BMS/电力电子 | 电池管理系统电力电子 |

---

### 4. 电池特性

#### 4.1 SOC估计
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 01-08 | SOC Estimation系列 | EKF/物理/在线方法 |
| 53-54 | Coulomb Counting | 库仑计数法 |
| 78 | SOC Estimation without Current | 无电流传感器SOC |
| 81-87 | SPM/P2D/DFN模型 | 电化学SOC估计 |
| 116-120 | 混合/ML SOC方法 | 机器学习SOC估计 |
| 231-233 | 联合SOC-SOH估计 | 自适应估计框架 |
| 236-237 | 数据驱动SOH/ICA方法 | 增量容量分析 |

#### 4.2 放电倍率效应 (Peukert)
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 61-62 | Peukert Equation系列 | Peukert方程基础 |
| 121-125 | Peukert深入分析 | 温度扩展/对比研究 |

#### 4.3 电池老化
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 25-34 | Capacity Fade/Aging系列 | 容量衰减机理 |
| 88-100 | 老化机制/数据集 | 详细老化分析 |
| 110-115 | 降解/老化建模 | 老化预测模型 |
| 118-119 | Calendar/Cycling Aging | 日历/循环老化 |
| 235 | PCCP Battery Degradation Modeling | 老化机理与PyBaMM |
| 238 | PHM Chemistry-Agnostic Model | 通用老化模型 |
| 240 | Thermal Runaway Safety | 热失控与安全 |

#### 4.4 库仑效率
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 135-140 | Coulombic Efficiency/SEI系列 | CE与SEI形成 |

#### 4.5 OCV-SOC关系
| 编号 | 标题 | 关键点 |
|------|------|--------|
| 191-200 | OCV模型系列 | OCV-SOC曲线建模 |

---

### 5. 体系结构与OS功耗管理

| 编号 | 标题 | 关键点 |
|------|------|--------|
| 205 | ASPLOS OS-Level Power Management | 操作系统级功耗管理 |
| 206 | HPCA Connected Standby Energy | 待机功耗优化策略 |
| 207 | BMS State Estimation Review | BMS状态估计综述 |
| 208 | Battery Pack SOC Balancing | 电池包SOC均衡综述 |
| 209 | UX-Driven CPU Frequency Scaling | 用户体验驱动的CPU调频 |
| 210 | Smartphone Processor Energy Tradeoff | 处理器能效权衡综述 |

---

## 按来源分类

### 顶级期刊
- **Nature Energy**: 88, 92, 135-138
- **Nature Communications**: 260
- **Nature Materials**: 261, 266
- **Joule**: 57, 89-90
- **Nature Scientific Reports**: 133, 148, 171, 231
- **Advanced Energy Materials**: 241, 254
- **ACS Nano**: 262, 267, 270
- **ACS Energy Letters**: 263, 265, 268
- **Nano Letters**: 264, 269
- **Journal of Power Sources (JPS)**: 05, 26-27, 34, 37, 80, 122-123, 131, 256, 279
- **Journal of The Electrochemical Society (JES)**: 25, 28, 121, 127, 134, 192, 239
- **Electrochimica Acta**: 242, 243
- **Applied Energy**: 53, 126, 145-146, 234, 277
- **Energy**: 232, 255, 280
- **IEEE Trans. Power Electronics (TPEL)**: 211-220, 275
- **IEEE Trans. Industrial Electronics (TIE)**: 244, 245
- **IEEE JSAC**: 249
- **IEEE TWC**: 250
- **IEEE TMC**: 70, 151, 161, 273
- **IEEE Access**: 225, 257, 278
- **Physical Chemistry Chemical Physics**: 235
- **Int'l J Heat and Mass Transfer**: 251
- **Applied Thermal Engineering**: 252

### 顶级会议
- **ACM MobiCom**: 15, 69, 154, 182, 274
- **ACM MobiSys**: 48, 66, 68, 164
- **ACM UbiComp/IMWUT**: 73-74, 259, 276
- **ACM SenSys**: 45, 47, 258
- **ACM CHI**: 201, 202
- **ACM CSCW**: 253
- **ACM IMC**: 204
- **ACM SIGCOMM**: 221, 222
- **ACM CoNEXT**: 223, 224
- **ACM EuroSys**: 247
- **ACM ASPLOS**: 205, 271
- **IEEE/ACM ISCA**: 248
- **USENIX OSDI**: 246
- **USENIX FAST**: 272
- **IEEE HPCA**: 206

### 官方文档
- **Apple Developer**: 77, 190
- **Android AOSP**: 179
- **NIST**: 155, 184
- **Texas Instruments**: 96, 175, 180

---

## 关键参考文献（建议优先阅读）

### 电池建模基础
1. **199** - Georgia Tech综合电池模型 (IEEE TEC, 经典)
2. **192** - JES参数化OCV模型
3. **86** - PyBaMM DFN模型实现

### 智能手机功耗
1. **178** - UCSD 3W's功耗分析 (最新精确测量)
2. **174** - AndroWatts组件功耗分解
3. **181** - 能耗估算综述

### SOC估计
1. **01-03** - EKF/物理/在线SOC估计
2. **191** - OCV模型综述

### 电池老化
1. **88** - Nature Energy老化机制
2. **89** - Joule十年老化洞察
3. **92** - Nature Energy数据驱动寿命预测

### 传感器/组件功耗
1. **165** - SensingKit传感器功耗
2. **171** - 视频通话电池消耗

### 用户行为
1. **202** - CHI Carat用户行为研究
2. **203** - 人-电池交互HBI
3. **204** - IMC大规模使用模式分析

### 体系结构
1. **205** - ASPLOS OS级功耗管理
2. **206** - HPCA待机功耗优化
3. **209** - UX驱动CPU调频

### 电力电子与充电
1. **211** - TPEL快速充电移动设备
2. **212** - TPEL高效Li-ion充电器电路
3. **214** - TPEL无线充电效率优化
4. **220** - TPEL BMS电力电子综述

### 5G网络能耗
1. **221** - SIGCOMM 5G功耗/QoE研究
2. **222** - SIGCOMM 5G能耗测量
3. **225** - IEEE Access 5G节能技术

### SOH估计进阶
1. **231** - 联合SOC-SOH估计框架
2. **235** - PCCP电池老化建模指南
3. **236** - 数据驱动SOH预测
4. **237** - ICA方法考虑C-rate

### 补充领域 (Round 5 新增)
1. **241** - Advanced Energy Materials高能量密度电池
2. **242** - Electrochimica Acta EIS电池状态估计
3. **246** - USENIX OSDI OS功耗管理
4. **247** - ACM EuroSys能效调度(EAS)
5. **248** - ISCA移动处理器功耗建模
6. **251** - Int'l J Heat Mass Transfer电池热建模
7. **253** - ACM CSCW协作电池感知
8. **255** - Energy电池建模综述
9. **260** - Nature Communications电池老化异质性

### 材料科学与先进电池 (Round 6 新增)
1. **261** - Nature Materials锂离子电池材料综述
2. **262** - ACS Nano硅负极材料
3. **263** - ACS Energy Letters快充机制
4. **264** - Nano Letters SEI层演化
5. **265** - ACS Energy Letters电池健康诊断
6. **266** - Nature Materials电极动力学
7. **267** - ACS Nano电池热特性
8. **268** - ACS Energy Letters电解质稳定性
9. **269** - Nano Letters锂析出与枝晶
10. **270** - ACS Nano纳米尺度老化机制

### 补充覆盖 (Round 6 新增)
1. **271** - ASPLOS内存系统功耗
2. **272** - USENIX FAST闪存存储功耗
3. **273** - IEEE TMC气压对电池影响
4. **274** - MobiCom后台应用能耗
5. **275** - TPEL消费电子电池包设计
6. **276** - UbiComp用户电池感知
7. **277** - Applied Energy连续时间建模
8. **278** - IEEE Access完整手机功耗模型
9. **279** - JPS温度依赖参数
10. **280** - Energy耗尽时间预测

---

## 数据集资源

| 编号 | 名称 | 类型 | 链接/说明 |
|------|------|------|----------|
| 30 | Nature Comprehensive Aging Dataset | 老化数据 | 公开数据集 |
| 91 | NASA Battery Aging Datasets | 老化数据 | PCoE数据库 |
| 92 | Nature Energy Cycle Life Prediction | 循环寿命 | 早期寿命预测数据 |
| 93 | BatteryML Open Source Platform | ML平台 | 开源工具 |
| 108 | Open Battery Datasets Comparison | 数据集对比 | 多数据集比较 |
| 114 | 21700 Cycle Aging Comprehensive Data | 循环数据 | 21700电池详细数据 |

---

## 文献统计

- **总计**: 280篇编号文献 + 若干PDF文件
- **覆盖年份**: 2005-2025
- **主要语言**: 英文
- **文件格式**: Markdown摘要 + 部分原始PDF
- **覆盖期刊/会议**: 45+
- **Round 5新增 (211-260)**: 
  - IEEE TPEL电力电子/充电器(211-220)
  - ACM SIGCOMM/5G网络能耗(221-230)
  - Energy Storage Materials/SOH估计(231-240)
  - 补充缺口领域(241-260)
- **Round 6新增 (261-280)**:
  - 材料科学: Nature Materials, ACS Nano, ACS Energy Letters, Nano Letters (261-270)
  - 内存/存储功耗: ASPLOS, USENIX FAST (271-272)
  - 气压影响: IEEE TMC (273)
  - 后台应用能耗: MobiCom (274)
  - 电池包设计: TPEL (275)
  - 用户感知: UbiComp (276)
  - 连续时间建模: Applied Energy (277)
  - 完整功耗模型: IEEE Access (278)
  - 温度参数: JPS (279)
  - 耗尽预测: Energy (280)

---

*最后更新: 2026年1月30日*
