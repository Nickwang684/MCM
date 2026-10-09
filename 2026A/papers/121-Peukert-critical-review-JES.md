# 121. A Critical Review of Using the Peukert Equation and its Generalizations for Lithium-Ion Cells

## 基本信息
- **标题**: A Critical Review of Using the Peukert Equation and its Generalizations for Lithium-Ion Cells
- **作者**: N. E. Galushkin, N. N. Yazvinskaya, D. N. Galushkin
- **期刊**: Journal of The Electrochemical Society (JES)
- **年份**: 2020
- **DOI**: 10.1149/1945-7111/abad69
- **链接**: https://iopscience.iop.org/article/10.1149/1945-7111/abad69
- **开放获取**: 是

## 研究内容摘要
本文对Peukert方程及其广义形式在锂离子电池中的应用进行了批判性评估。Peukert方程最初为铅酸电池设计，描述了放电电流与可用容量之间的关系。作者系统分析了该方程在不同类型锂离子电池中的适用性和局限性。

## 关键发现
1. **Peukert指数差异**：锂离子电池的Peukert指数（通常1.00-1.10）远小于铅酸电池（1.1-1.4），表明锂电池受放电倍率影响较小
2. **方程适用性**：经典Peukert方程在锂离子电池中的适用范围有限，需要修正
3. **广义形式**：提出了考虑温度和SOC依赖性的广义Peukert方程
4. **实验验证**：在多种商用锂离子电池上验证了改进模型的准确性

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 放电倍率效应 | ★★★★★ | 核心研究主题，直接建模倍率对容量的影响 |
| SOC估计 | ★★★★☆ | Peukert方程可用于剩余容量预测 |
| 使用历史 | ★★★☆☆ | 放电模式影响有效容量 |
| 温度变化 | ★★★☆☆ | 广义方程考虑温度依赖性 |

## 核心方程
**经典Peukert方程**:
$$C_p = I^n \cdot t$$

其中：
- $C_p$ = Peukert容量常数
- $I$ = 放电电流
- $n$ = Peukert指数
- $t$ = 放电时间

**广义形式**（考虑温度）:
$$C(I,T) = C_0 \cdot f(I) \cdot g(T)$$

## 与论文研究方向的关联
本文对于建立智能手机电池续航的连续时间模型具有直接价值：
- 提供了放电倍率对有效容量影响的数学框架
- 可用于解释高负载（处理器、屏幕）下电池续航的非线性下降
- 广义Peukert方程可整合到环境温度敏感的电池模型中
- JES作为电化学顶刊，文献权威性高
