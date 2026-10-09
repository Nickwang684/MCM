# A Hybrid Statistical Data-Driven Method for On-line Joint State Estimation

## 基本信息
- **标题**: A hybrid statistical data-driven method for on-line joint state estimation of lithium-ion batteries
- **作者**: Yuchen Song, Datong Liu, Haitao Liao, Yu Peng
- **期刊**: Applied Energy
- **年份**: 2020
- **卷号**: Volume 261, 114408
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S0306261919320951

## 研究内容
开发混合统计数据驱动方法，实现锂离子电池多状态（SOC、SOH、功率）的在线联合估计。

## 核心方法
- **联合状态估计**: 同时估计SOC、SOH和可用功率
- **混合方法**: 结合统计模型和数据驱动
- **在线自适应**: 适应电池老化和环境变化
- **不确定性量化**: 提供估计的置信区间

## 方法架构

### 状态估计模块
1. SOC估计: 基于ECM的滤波
2. SOH估计: 数据驱动的容量估计
3. 功率估计: 阻抗相关的功率预测

### 在线更新
- 参数自适应更新
- 模型校准
- 异常检测

## 与考虑因素的相关性

### 电池特性
- **SOC估计**: 实时荷电状态
- **SOH估计**: 健康状态评估
- **功率能力**: 瞬时功率预测

### 使用历史
- **在线学习**: 从使用数据持续学习
- **自适应**: 适应个体差异和老化

## 与论文研究方向的关联
联合状态估计对智能手机电池管理有重要价值，可同时预测续航和健康状态。
