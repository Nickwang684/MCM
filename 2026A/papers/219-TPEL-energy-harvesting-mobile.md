# 219. Energy Harvesting for Mobile and Wearable Devices

## 基本信息
- **标题**: Energy Harvesting for Mobile and Wearable Devices: Recent Advances and Future Directions
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2021
- **类型**: 综述论文

## 主要内容

### 研究背景
- 移动设备续航受限于电池容量
- 能量收集可作为辅助电源
- 多种能量来源可供利用

### 能量收集来源

| 来源 | 功率密度 | 适用场景 |
|------|----------|----------|
| 太阳能 | 10-100 mW/cm² | 户外使用 |
| 射频能量 | 1-100 μW/cm² | 无线环境 |
| 振动能量 | 10-1000 μW/cm³ | 运动中 |
| 热能 | 10-100 μW/cm² | 体温差 |

### 太阳能收集模型
$$P_{solar} = A \cdot G \cdot \eta_{cell} \cdot FF$$

其中：
- $A$ = 电池面积
- $G$ = 光照强度 (W/m²)
- $\eta_{cell}$ = 电池效率
- $FF$ = 填充因子

### 最大功率点跟踪 (MPPT)
$$P_{max} = V_{MPP} \cdot I_{MPP}$$

### 对智能手机建模的意义
- 辅助能量输入的建模
- 环境条件对可用能量的影响
- 可延伸到可穿戴设备续航分析

## 关键词
- Energy harvesting, solar, RF, thermoelectric, MPPT, wearable
