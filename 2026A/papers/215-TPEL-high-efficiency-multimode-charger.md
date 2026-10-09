# 215. A High-Efficiency Integrated Multimode Battery Charger With an Adaptive Supply Voltage Control Scheme

## 基本信息
- **标题**: A High-Efficiency Integrated Multimode Battery Charger With an Adaptive Supply Voltage Control Scheme
- **作者**: Kim et al.
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2018
- **卷/期**: Vol. 33, No. 9
- **DOI**: 10.1109/TPEL.2017.2771779
- **链接**: https://ieeexplore.ieee.org/document/8063975

## 主要内容

### 研究背景
- 移动设备需要高效率的集成充电器
- 不同充电阶段需要不同的工作模式
- 自适应电压控制可提高整体效率

### 关键贡献
1. **多模式切换**: 涓流-CC-CV三阶段自动切换
2. **自适应供电**: 根据电池电压调整输入电压
3. **峰值效率**: 达到93.5%

### 效率优化策略
```
Low SOC (涓流):   I = 0.1C, 低功率模式
Medium SOC (CC):  I = 1C~2C, 最大效率模式
High SOC (CV):    V = V_max, 电流逐渐减小
```

### 功率损耗分解
$$P_{loss} = P_{conduction} + P_{switching} + P_{gate} + P_{quiescent}$$

### 对智能手机建模的意义
- 充电过程中的效率变化建模
- 不同SOC阶段的充电功耗特性
- 充电器效率对整体能量传递的影响

## 关键词
- Multimode charger, adaptive voltage, high efficiency, CC-CV, PMIC
