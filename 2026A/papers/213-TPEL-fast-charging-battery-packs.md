# 213. Fast Charging Control for Battery Packs With Combined Optimization of Charger and Equalizers

## 基本信息
- **标题**: Fast Charging Control for Battery Packs With Combined Optimization of Charger and Equalizers
- **作者**: Cao et al.
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2020
- **卷/期**: Vol. 36, No. 4
- **DOI**: 10.1109/TPEL.2020.3028997
- **链接**: https://ieeexplore.ieee.org/document/9222542

## 主要内容

### 研究背景
- 电池组快充面临单体不一致性问题
- 传统充电策略无法同时优化速度和均衡
- 需要充电器和均衡器的协同控制

### 关键贡献
1. **联合优化框架**: 同时优化充电速度和SOC均衡
2. **模型预测控制**: 基于MPC的实时充电策略
3. **均衡效率**: 提高均衡速度40%以上

### 优化目标函数
$$\min J = \sum_{k=0}^{N} \left[ \alpha \cdot t_{charge} + \beta \cdot \sum_{i} (SOC_i - \overline{SOC})^2 \right]$$

约束条件：
- $I_{max}$ 限制
- $V_{max}$ 限制
- 温度限制

### 对智能手机建模的意义
- 虽然手机多为单电芯，但优化思路可借鉴
- 提供了充电过程优化的数学框架
- 多约束条件下的充电控制策略

## 关键词
- Battery pack, fast charging, SOC balancing, MPC, equalizer
