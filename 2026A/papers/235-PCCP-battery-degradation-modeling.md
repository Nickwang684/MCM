# 235. Lithium-Ion Battery Degradation: How to Model It

## 基本信息
- **标题**: Lithium-Ion Battery Degradation: How to Model It
- **作者**: Simon E. J. O'Kane, Weilong Ai, et al.
- **期刊**: Physical Chemistry Chemical Physics (PCCP)
- **年份**: 2022
- **卷**: Volume 24
- **页码**: 7909-7922
- **DOI**: 10.1039/D2CP00417H
- **链接**: https://pubs.rsc.org/en/content/articlehtml/2022/cp/d2cp00417h

## 主要内容

### 老化机制分类

#### SEI生长
$$\frac{d\delta_{SEI}}{dt} = -k_{SEI} \cdot \exp\left(-\frac{E_a}{RT}\right) \cdot c_{Li}$$

#### 锂析出
当 $\phi_s - \phi_e < 0$（相对Li/Li+）时发生

#### 活性材料损失
$$\frac{d\epsilon_{AM}}{dt} = -k_{LAM} \cdot f(SOC, T, \sigma)$$

### 老化模型层次

| 层次 | 模型类型 | 计算成本 | 精度 |
|------|----------|----------|------|
| 0 | 经验模型 | 低 | 中 |
| 1 | 等效电路+老化 | 低-中 | 中 |
| 2 | SPM+老化 | 中 | 中-高 |
| 3 | P2D+老化 | 高 | 高 |
| 4 | 3D多物理场 | 很高 | 很高 |

### 容量衰减半经验模型
$$Q_{loss} = A \cdot \exp\left(-\frac{E_a}{RT}\right) \cdot t^{0.5} + B \cdot N^z$$

其中：
- 第一项：日历老化 ($\sqrt{t}$依赖)
- 第二项：循环老化 (N为循环次数)

### PyBaMM实现
- 开源Python电池建模包
- 支持多种老化模型
- 可与实验数据拟合

### 对智能手机建模的意义
- 电池老化机理的物理理解
- 不同复杂度模型的选择
- 容量衰减预测的数学框架

## 关键词
- Battery degradation, SEI, lithium plating, aging model, PyBaMM
