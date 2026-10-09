# 238. Lithium-Ion Battery Degradation Model Agnostic to Cell Chemistry

## 基本信息
- **标题**: A Lithium-Ion Battery Degradation Model Agnostic to Cell Chemistry with Integrated State-of-Charge and Temperature Dependence
- **作者**: Bruno Masserano, Jorge E. Garcia Bustos, Camilo Ramirez, et al.
- **会议**: Annual Conference of the PHM Society
- **年份**: 2025
- **链接**: https://papers.phmsociety.org/index.php/phmconf/article/view/4373

## 主要内容

### 研究背景
- 不同电池化学体系老化特性不同
- 需要通用的老化模型框架
- 考虑SOC和温度的联合影响

### 化学体系无关模型

#### 统一容量衰减方程
$$\frac{dC}{dt} = -k_0 \cdot \exp\left(-\frac{E_a}{RT}\right) \cdot g(SOC) \cdot h(C)$$

其中：
- $k_0$ = 老化速率常数
- $E_a$ = 活化能
- $g(SOC)$ = SOC影响函数
- $h(C)$ = 当前容量影响函数

### SOC影响函数
$$g(SOC) = 1 + \alpha \cdot (SOC - 0.5)^2$$

高SOC和低SOC加速老化

### 温度影响
$$k(T) = k_{ref} \cdot \exp\left[-\frac{E_a}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right]$$

| 温度 | 相对老化速率 |
|------|--------------|
| 25°C | 1.0x |
| 35°C | 2.0x |
| 45°C | 4.0x |
| 55°C | 8.0x |

### 循环与日历老化分离
$$C_{loss} = C_{loss,cal} + C_{loss,cyc}$$

$$C_{loss,cal} = A \cdot t^{0.5}$$
$$C_{loss,cyc} = B \cdot N \cdot DOD^n$$

### 对智能手机建模的意义
- 通用老化模型可适配不同手机电池
- SOC和温度联合影响的建模
- 日历老化和循环老化的分离

## 关键词
- Battery degradation, chemistry agnostic, SOC dependence, temperature, universal model
