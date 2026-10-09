# 229. Flexible Energy Modeling for Sustainable 5G Networks

## 基本信息
- **标题**: Charting 5G Energy Efficiency: Flexible Energy Modeling for Sustainable Networks
- **作者**: Anderson L de Araujo, Luc Deneire, Guillaume Urvoy-Keller, André L F de Almeida
- **来源**: HAL / IEEE Conference
- **年份**: 2025
- **链接**: https://hal.science/hal-04955001v1

## 主要内容

### 研究背景
- 5G网络能耗建模缺乏灵活性
- 需要适应不同部署场景的模型
- 可持续发展要求精确能耗预测

### 灵活能耗模型框架

#### 基站能耗模型
$$P_{BS} = P_0 + \Delta_p \cdot P_{out}$$

其中：
- $P_0$ = 空载功耗
- $\Delta_p$ = 负载斜率
- $P_{out}$ = 输出功率

#### 负载相关模型
$$P(L) = P_{idle} + (P_{max} - P_{idle}) \cdot L^\alpha$$

- $L$ = 负载率 (0-1)
- $\alpha$ = 非线性因子

### 场景化参数
| 部署 | $P_0$ | $P_{max}$ | $\alpha$ |
|------|-------|-----------|----------|
| 宏站 | 500W | 1500W | 0.8 |
| 微站 | 50W | 150W | 0.9 |
| 小站 | 10W | 30W | 1.0 |

### 对智能手机建模的意义
- 网络基础设施能耗影响服务质量
- 网络负载与终端体验的关系
- 可持续网络设计考量

## 关键词
- 5G, energy modeling, sustainable networks, base station, load model
