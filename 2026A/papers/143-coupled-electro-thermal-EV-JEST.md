# 143. Coupled Electro-Thermal Modeling of Lithium-Ion Batteries for Electric Vehicle Application

## 基本信息
- **标题**: Coupled electro-thermal modeling of lithium-ion batteries for electric vehicle application
- **作者**: Tedjani Mesbahi, Rocío Bendala Sugrañes, Reda Bakri, Patrick Bartholomeüs
- **期刊**: Journal of Energy Storage
- **年份**: 2021
- **卷/页**: Volume 35, 102260
- **DOI**: 10.1016/j.est.2021.102260
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S2352152X21000281
- **被引次数**: 28+

## 研究内容摘要
本研究建立了用于电动汽车应用的锂离子电池电-热耦合模型。模型考虑了电池的电化学特性、热特性及其相互作用。

## 关键发现
1. **耦合策略**：双向耦合比单向耦合更准确
2. **参数温度依赖**：
   - 电导率：随温度增加
   - 扩散系数：随温度增加
   - 内阻：随温度降低
3. **动态响应**：模型可捕捉快速充放电时的热瞬态
4. **验证结果**：与实验数据吻合良好

## 温度依赖参数模型
**Arrhenius型温度依赖**：
$$\sigma(T) = \sigma_{ref} \cdot \exp\left[\frac{E_a}{R} \cdot \left(\frac{1}{T_{ref}} - \frac{1}{T}\right)\right]$$

**内阻温度依赖**：
$$R(T) = R_{25} \cdot \exp\left[k_R \cdot \left(\frac{1}{T} - \frac{1}{298}\right)\right]$$

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 温度变化 | ★★★★★ | 核心研究主题 |
| 电池特性 | ★★★★★ | 参数温度依赖 |
| 处理器负载 | ★★★★☆ | 负载影响产热 |

## 与论文研究方向的关联
- **参数建模**：温度依赖参数的数学表达式
- **连续时间模型**：电-热耦合的微分方程组
- **实用验证**：模型经过实验验证
- **方法论参考**：耦合建模的系统方法
