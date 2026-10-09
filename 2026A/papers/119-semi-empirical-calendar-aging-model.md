# Semi-Empirical Model of Calendar Ageing for Automotive and Deep-Space Applications

## 基本信息
- **标题**: A semi-empirical model of the calendar ageing of lithium-ion batteries aimed at automotive and deep-space applications
- **期刊**: Journal of Energy Storage
- **年份**: 2024
- **卷号**: Volume 85
- **链接**: https://www.sciencedirect.com/science/article/pii/S2352152X23037878

## 研究内容
开发半经验模型预测锂离子电池在汽车和深空应用中的日历老化。

## 模型结构

### 容量衰减模型
ΔQ = A·exp(-Ea/RT)·t^n·f(SOC)

其中:
- A: 前因子
- Ea: 活化能
- T: 绝对温度
- t: 存储时间
- n: 时间指数(通常0.5-1)
- f(SOC): SOC依赖函数

### 内阻增加模型
ΔR = B·exp(-Eb/RT)·t^m·g(SOC)

## 模型参数

### 典型活化能
- 容量衰减: 30-60 kJ/mol
- 内阻增加: 25-50 kJ/mol

### SOC依赖性
- 高SOC加速老化
- 低SOC相对稳定
- 存在最优存储SOC(~50%)

## 与考虑因素的相关性

### 环境因素
- **温度**: Arrhenius温度依赖
- **存储条件**: SOC对日历老化的影响

### 电池特性
- **日历老化**: 非使用期间的退化
- **寿命预测**: 长期存储的影响

## 与论文研究方向的关联
日历老化模型可用于预测智能手机电池在非使用期间的退化。
