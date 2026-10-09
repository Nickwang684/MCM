# 122. Expanding the Peukert Equation for Battery Capacity Modeling Through Inclusion of a Temperature Dependency

## 基本信息
- **标题**: Expanding the Peukert equation for battery capacity modeling through inclusion of a temperature dependency
- **作者**: Austin Hausmann, Christopher Depcik
- **期刊**: Journal of Power Sources
- **年份**: 2013
- **卷/页**: Volume 235, Pages 148-158
- **DOI**: 10.1016/j.jpowsour.2013.01.174
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S0378775313002322

## 研究内容摘要
本文扩展了经典Peukert方程，将温度依赖性纳入电池容量建模。研究发现，在动态负载和变化温度条件下，经典Peukert方程的准确性显著降低。作者提出了一种修正方法，将温度效应与放电倍率效应耦合。

## 关键发现
1. **温度-倍率耦合**：低温下放电倍率效应更加显著
2. **Arrhenius修正**：使用Arrhenius型温度修正因子改进模型
3. **动态工况适用性**：修正后的模型在变负载条件下准确性提升
4. **实验验证**：在-20°C至45°C范围内验证模型有效性

## 核心方程
**温度扩展Peukert方程**:
$$C(I,T) = C_{ref} \cdot \left(\frac{I_{ref}}{I}\right)^{n(T)-1} \cdot \exp\left[-E_a \cdot \left(\frac{1}{T} - \frac{1}{T_{ref}}\right) / R\right]$$

其中：
- $E_a$ = 活化能
- $R$ = 气体常数
- $n(T)$ = 温度依赖的Peukert指数

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 温度变化 | ★★★★★ | 核心创新点，建立温度-容量关系 |
| 放电倍率效应 | ★★★★★ | Peukert方程的核心应用 |
| 处理器负载 | ★★★★☆ | 高负载导致高放电倍率 |
| 环境因素 | ★★★★☆ | 环境温度直接影响模型参数 |

## 与论文研究方向的关联
- **直接应用价值**：智能手机在不同环境温度下使用，本文模型可预测温度对续航的影响
- **连续时间建模**：提供了温度-倍率耦合的连续时间数学框架
- **敏感性分析**：可用于量化温度变化对电池续航预测的不确定性
- Journal of Power Sources是电池领域顶刊
