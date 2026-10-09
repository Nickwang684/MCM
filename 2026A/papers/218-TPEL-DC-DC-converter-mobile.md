# 218. High-Efficiency DC-DC Converters for Portable Electronic Devices

## 基本信息
- **标题**: High-Efficiency DC-DC Converters for Portable Electronic Devices: A Comprehensive Review
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2019
- **卷/期**: Vol. 34, No. 8
- **类型**: 综述论文

## 主要内容

### 研究背景
- 便携设备需要高效率电源转换
- 不同组件需要不同电压轨道
- DC-DC转换器效率直接影响续航

### 主要DC-DC拓扑
1. **Buck转换器**: 降压，用于CPU核心供电
2. **Boost转换器**: 升压，用于背光和RF PA
3. **Buck-Boost**: 双向，用于电池充放电
4. **LDO**: 低噪声，用于模拟电路

### 效率模型
$$\eta_{DCDC} = \frac{P_{out}}{P_{in}} = \frac{V_{out} \cdot I_{out}}{V_{in} \cdot I_{in}}$$

损耗分解：
$$P_{loss} = P_{sw} + P_{cond} + P_{gate} + P_{core}$$

其中：
- $P_{sw} = \frac{1}{2}V_{in}I_{out}(t_r + t_f)f_{sw}$
- $P_{cond} = I_{out}^2 \cdot R_{DS(on)}$

### 轻载效率优化
- 脉冲跳跃模式 (PSM)
- 动态电压/频率调节 (DVFS)
- 多相位切换

### 对智能手机建模的意义
- 电源管理效率对续航的影响
- 不同负载下的效率变化模型
- 电压轨道功耗分配

## 关键词
- DC-DC converter, buck, boost, efficiency, portable devices, PMIC
