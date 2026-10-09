# 237. SOH Estimation Based on Incremental Capacity Analysis Considering C-rate

## 基本信息
- **标题**: A State-of-Health Estimation Method Based on Incremental Capacity Analysis for Li-ion Battery Considering Charging/Discharging Rate
- **作者**: Wang Chunyu et al.
- **期刊**: Journal of Energy Storage
- **年份**: 2023
- **DOI**: 10.1016/j.est.2023.109858
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S2352152X23024088

## 主要内容

### 研究背景
- ICA是SOH估计的有效方法
- 充放电倍率影响IC曲线形态
- 需要考虑C-rate的补偿方法

### 增量容量分析 (ICA)

#### IC曲线定义
$$IC = \frac{dQ}{dV}$$

数值计算：
$$IC_i = \frac{Q_{i+1} - Q_i}{V_{i+1} - V_i}$$

#### 典型IC曲线特征
```
IC
│
│     ╭─╮     ╭─╮
│    /   \   /   \    <- 峰值对应相变
│___/     \_/     \___
│
└───────────────────────> V
    3.2V   3.6V   4.0V
```

### C-rate影响

| C-rate | 峰值位置 | 峰值高度 | 峰值宽度 |
|--------|----------|----------|----------|
| C/10 | 标准 | 高 | 窄 |
| C/5 | 右移 | 中 | 中 |
| C/2 | 明显右移 | 低 | 宽 |
| 1C | 大幅右移 | 很低 | 很宽 |

### C-rate补偿模型
$$IC_{corrected} = IC_{measured} \cdot f(C_{rate}, T)$$

其中补偿函数：
$$f(C, T) = 1 + a \cdot C + b \cdot C^2 + c \cdot (T - T_{ref})$$

### SOH-峰值关系
$$SOH = \alpha \cdot A_{peak} + \beta \cdot V_{peak} + \gamma$$

### 对智能手机建模的意义
- IC曲线用于在线SOH估计
- 不同放电倍率的补偿方法
- 手机充电过程可提取IC特征

## 关键词
- ICA, incremental capacity, C-rate, SOH, charging rate, peak analysis
