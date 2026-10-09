# 124. Generalized Peukert Equations Use for Finding the Remaining Capacity of Lithium-Ion Cells of Any Format

## 基本信息
- **标题**: Generalized Peukert Equations Use for Finding the Remaining Capacity of Lithium-Ion Cells of Any Format
- **作者**: Nataliya N. Yazvinskaya, Nikolay E. Galushkin, Dmitriy N. Galushkin
- **期刊**: Energies (MDPI)
- **年份**: 2021
- **卷/期**: Volume 14, Issue 16, 5009
- **DOI**: 10.3390/en14165009
- **链接**: https://www.mdpi.com/1996-1073/14/16/5009
- **开放获取**: 是

## 研究内容摘要
本文提出了广义Peukert方程，适用于任何格式的锂离子电池单体。研究建立了统一的数学框架，可以预测不同几何形状（圆柱形、方形、软包）和化学体系的锂离子电池的剩余容量。

## 关键发现
1. **通用方程形式**：提出适用于各种电池格式的广义Peukert方程
2. **格式独立性**：验证了方程在18650、21700、软包等不同格式电池上的适用性
3. **化学体系兼容**：LFP、NMC、LCO等不同正极材料电池均可应用
4. **精度分析**：在宽放电倍率范围内预测误差<5%

## 核心方程
**广义Peukert方程**:
$$Q = Q_0 \cdot \left(\frac{I_0}{I}\right)^{n-1} \cdot \left[1 - k \cdot \ln\left(\frac{I}{I_0}\right)\right]$$

其中：
- $Q$ = 实际可用容量
- $Q_0$ = 标称容量
- $n$ = 广义Peukert指数
- $k$ = 修正系数

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 放电倍率效应 | ★★★★★ | 核心建模对象 |
| SOC估计 | ★★★★★ | 剩余容量预测 |
| 电池特性 | ★★★★☆ | 适用于多种电池格式 |

## 与论文研究方向的关联
- **智能手机电池适用性**：智能手机使用软包锂聚合物电池，本文方程可直接应用
- **开放获取**：MDPI开放期刊，数据和方法可公开获取
- **连续时间模型**：广义Peukert方程可嵌入到智能手机电池续航的连续时间模型中
- **验证参考**：提供了不同格式电池的实验数据用于模型验证
