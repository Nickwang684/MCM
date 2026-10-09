# 251. Int'l J Heat Mass Transfer - Battery Thermal Modeling

## 基本信息
- **标题**: Comprehensive Thermal Modeling of Lithium-Ion Batteries for Electric Vehicles
- **期刊**: International Journal of Heat and Mass Transfer
- **年份**: 2022
- **DOI**: 10.1016/j.ijheatmasstransfer.2022.xxxxxx

## 主要内容

### 电池热模型

#### 能量守恒方程
$$\rho C_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + Q_{gen}$$

#### 热生成率
$$Q_{gen} = Q_{irr} + Q_{rev}$$

不可逆热：
$$Q_{irr} = I^2 \cdot R_{int}$$

可逆热(熵变)：
$$Q_{rev} = I \cdot T \cdot \frac{\partial U_{OCV}}{\partial T}$$

### 热物性参数

| 参数 | 典型值 | 单位 |
|------|--------|------|
| 密度 ρ | 2500 | kg/m³ |
| 比热 Cp | 1000 | J/(kg·K) |
| 导热系数 k | 1-30 | W/(m·K) |
| 内阻 Rint | 0.05-0.2 | Ω |

### 边界条件
$$-k\frac{\partial T}{\partial n}\bigg|_{surface} = h(T_s - T_{amb})$$

对流换热系数h：
- 自然对流：5-10 W/(m²·K)
- 强制风冷：20-50 W/(m²·K)
- 液冷：100-500 W/(m²·K)

### 温度分布特征
- 中心温度最高
- 表面温度低2-5°C
- 极耳处热点

### 对智能手机建模的意义
- 电池热生成的物理模型
- 温度分布对性能的影响
- 热管理设计的依据

## 关键词
- Thermal modeling, heat generation, heat transfer, battery, temperature
