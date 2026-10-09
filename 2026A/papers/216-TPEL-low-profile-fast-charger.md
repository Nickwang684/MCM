# 216. A Low-Profile High-Efficiency Fast Battery Charger With Unifiable Constant-Current and Constant-Voltage Regulation

## 基本信息
- **标题**: A Low-Profile High-Efficiency Fast Battery Charger With Unifiable Constant-Current and Constant-Voltage Regulation
- **作者**: Zhang et al.
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2020
- **卷/期**: Vol. 35, No. 12
- **DOI**: 10.1109/TPEL.2020.3010756
- **链接**: https://ieeexplore.ieee.org/document/9149792

## 主要内容

### 研究背景
- 快充需要高功率密度的充电器
- CC和CV模式切换通常需要复杂控制
- 统一控制架构可简化设计

### 关键贡献
1. **统一控制**: CC/CV模式使用同一控制器
2. **低剖面设计**: 适合超薄设备
3. **高效率**: 全负载范围效率>92%

### CC-CV统一控制方程
控制变量：
$$u = K_p \cdot e + K_i \int e \, dt$$

其中误差定义：
$$e = \min(I_{ref} - I, V_{ref} - V)$$

### 充电功率曲线
```
时间 t    | 功率 P(t)
---------|----------
0-30min  | P_max (CC阶段)
30-60min | P下降 (CV阶段)
60min+   | P_min (涓流)
```

### 对智能手机建模的意义
- CC-CV充电过程的功率变化模型
- 充电时间与功率的关系
- 可用于建模充电过程中的能量输入

## 关键词
- Fast charger, CC-CV, unified control, low profile, high efficiency
