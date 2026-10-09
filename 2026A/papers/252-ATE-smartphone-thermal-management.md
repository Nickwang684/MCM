# 252. Applied Thermal Engineering - Smartphone Thermal Management

## 基本信息
- **标题**: Thermal Management Challenges and Solutions for Smartphones
- **期刊**: Applied Thermal Engineering
- **年份**: 2023
- **类型**: 综述论文

## 主要内容

### 智能手机热源

```
┌─────────────────────────────────┐
│      屏幕 (5-8W peak)          │
├─────────────────────────────────┤
│    SoC (5-10W peak)            │
│    ┌───┐ ┌───┐ ┌───┐          │
│    │CPU│ │GPU│ │NPU│          │
│    └───┘ └───┘ └───┘          │
├─────────────────────────────────┤
│    电池 (充电时2-5W)           │
├─────────────────────────────────┤
│    5G Modem (2-4W)             │
└─────────────────────────────────┘
```

### 热管理技术

| 技术 | 原理 | 效果 |
|------|------|------|
| 石墨片 | 面内高导热 | 均温 |
| 热管/VC | 相变传热 | 快速导热 |
| 铜箔 | 金属导热 | 热扩散 |
| 相变材料 | 吸热储热 | 削峰 |

### 热限制 (Thermal Throttling)

```
温度 < 40°C: 全速运行
温度 40-45°C: 轻度降频
温度 45-50°C: 中度降频
温度 > 50°C: 重度降频/关机
```

降频对功耗影响：
$$P_{throttled} = P_{max} \cdot \left(\frac{f_{throttled}}{f_{max}}\right)^3$$

### 手机热仿真模型
$$\frac{dT_{skin}}{dt} = \frac{P_{total} - h A (T_{skin} - T_{amb})}{C_{thermal}}$$

### 对智能手机建模的意义
- 手机热管理的系统分析
- 热限制对性能/功耗的影响
- 环境温度的作用

## 关键词
- Smartphone thermal, heat pipe, thermal throttling, cooling, SoC
