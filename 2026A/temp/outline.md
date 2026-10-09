# 2026 MCM Problem A 论文大纲（强化版：每一模块“写什么 + 顺序”）

> 题目：智能手机电池耗电建模（连续时间模型）
>
> 目标：满足题目九项要求，并对齐 COMAP Summary Sheet 与 O 奖论文常见结构。

---

## 目录（控制 8 点以内，便于 1 页目录）
1. Introduction（含问题重述、假设、流程图、符号表、数据处理）
2. Model Preparation & Task-Based Modeling
3. Parameter Settings & Solution Method
4. Results, Validation & Evaluation
5. Sensitivity & Uncertainty Analysis
6. Recommendations & Extension
7. Strengths, Weaknesses & Conclusion
8. References & Appendices

---

## Summary Sheet（第 1 页，独立模板）
> **写作顺序**：最后写，但放在首页。
**摘要 6 句模板（80–550 词）**
1. 背景与挑战（续航预测的现实意义）
2. 任务目标（SOC 连续时间建模 + 续航预测 + 影响因素识别 + 不确定性）
3. 模型框架（Model I–V：电池/功耗/热/老化/预测）
4. 关键方法或创新（ECM+EKF、热-老化耦合、Sobol+MC）
5. 1–2 个核心结果（主要耗电因素与置信区间）
6. 验证/意义（模型验证 + 建议价值）
**关键词**：5–8 个

---

## 1. Introduction（必须包含：问题重述 + 假设 + 流程图 + 符号表 + 数据处理）
> **写作顺序**：
1) 背景与价值 → 2) 问题重述/任务拆解 → 3) 假设及依据 → 4) 总体流程图 → 5) 符号表 → 6) 数据处理说明

### 1.1 Background & Motivation
- 现实背景、应用价值、研究意义（可配图）

### 1.2 Problem Restatement (Task 1–9)
- 将题目要求逐条列为任务，确保对齐题意

### 1.3 Key Assumptions (with Justifications)
- 三段式：假设 → 现实依据 → 建模简化

### 1.4 Research Workflow (Flowchart)
- “功耗 → 电池 → 热 → 老化 → 预测 → 评估/建议”流程图

### 1.5 Notation and Symbols
- 统一符号表（SOC, SOH, P_total, I, T, R 等）

### 1.6 Data Acquisition & Processing
- 数据来源、清洗、归一化与提取方法

---

## 2. Model Preparation & Task-Based Modeling
> **写作顺序**：数据来源 → 处理流程 → 得到可用于建模的变量/参数。
- 功耗分解数据来源与处理
- 电池参数来源（规格书/文献/实验）
- 热模型与老化模型的标定参数

---

### Task 1: 建立连续时间 SOC 与电池状态模型
**写什么 + 顺序**：
1) SOC 连续时间方程
2) 二阶 ECM 电压方程
3) OCV-SOC 关系
4) EKF 状态估计框架

### Task 2: 建立功耗分解与电流输入模型
**写什么 + 顺序**：
1) 总功耗分解公式
2) 各组件功耗子模型
3) 功率 → 电流转换

### Task 3: 建立热耦合模型
**写什么 + 顺序**：
1) 集总参数热平衡
2) 产热项与散热项
3) Arrhenius 温度依赖

### Task 4: 建立老化模型并量化 SOH 影响
**写什么 + 顺序**：
1) SOH 定义
2) 日历老化
3) 循环老化
4) SOH 影响容量/内阻

### Task 5: 预测耗尽时间并给出置信区间
**写什么 + 顺序**：
1) 续航时间积分式
2) 数值求解流程
3) 输出 t_empty 与置信区间

---

## 3. Parameter Settings & Solution Method
> **写作顺序**：模型参数表 → 求解器选择 → 多时间尺度处理。
- 参数表格（电池/热/老化/功耗）
- 数值积分方法（solve_ivp/ode45）
- 多时间尺度求解策略

---

## 4. Results, Validation & Evaluation
> **写作顺序**：基准场景 → 情景对比 → 可视化总结。
- 基准场景续航预测结果（轻度/中度/重度）
- 情景对比（低温、低 SOC、老化）
- 图表展示：SOC 曲线、温度曲线、耗尽时间柱状图

### Validation（并入本节）
> **写作顺序**：验证方法 → 误差指标 → 鲁棒性测试。
- 文献/实验对比
- 误差指标（RMSE/MAE/MAPE）
- 极端情景稳定性检验

---

## 5. Sensitivity & Uncertainty Analysis
> **写作顺序**：选参数 → Sobol/Morris → 结论（大/小影响因素）。
- Sobol 全局灵敏度指数
- Morris 筛选（可选）
- **重点回答**：快速耗电因素 & 影响小因素

### Uncertainty Quantification
> **写作顺序**：不确定性来源 → Monte Carlo → 置信区间。
- Monte Carlo 传播
- 95% 置信区间
- 不确定性来源分解

---

## 6. Recommendations & Extension
> **写作顺序**：基于敏感性结果 → 给出用户建议 → 给出 OS 建议。
### 6.1 User Behavior Recommendations
- 屏幕亮度/深色模式/关闭后台等

### 6.2 OS-Level Optimization Strategies
- DVFS 调度、网络批处理、预测性功耗管理

### Extension & Generalization
> **写作顺序**：扩展方向 → 可迁移性分析。
- 推广到平板/笔记本/电动车的可迁移性

---

## 7. Strengths, Weaknesses & Conclusion
> **写作顺序**：优势 → 局限。
### Strengths
- 结构合理、数据支撑、可解释性强

### Weaknesses
- 数据依赖、假设限制、极端场景偏差

### Conclusion
> **写作顺序**：核心发现 → 对应题目要求 → 未来改进。
- 核心发现总结
- 对题目九项要求的对应结论

---

## 8. References & Appendices
- 文献与数据来源（统一英文格式）
- Appendices（可选）：公式推导 / 完整参数表 / 伪代码

---

## AI Use Report（单独附在最后，不计入 25 页）
- 工具、用途、交互方式说明
