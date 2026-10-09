# 175. Haptic Energy Consumption - Texas Instruments Application Note

## 基本信息
- **标题**: Haptic Energy Consumption
- **发布机构**: Texas Instruments
- **文档编号**: SLOA194A (Rev. A)
- **年份**: 2022
- **类型**: 应用笔记
- **链接**: https://www.ti.com/lit/an/sloa194a/sloa194a.pdf

## 核心内容

### 文档目的
- 量化触觉反馈的能耗特性
- 比较不同类型振动马达的功耗
- 为电池敏感应用提供设计指导

### 振动马达类型
1. **ERM (Eccentric Rotating Mass)**: 偏心转子马达
2. **LRA (Linear Resonant Actuator)**: 线性共振驱动器

### 能耗对比
| 驱动器类型 | 典型功耗 | 能效 |
|------------|----------|------|
| ERM | 60-150mW | 较低 |
| LRA | 30-80mW | 较高 |

### 关键参数
- **启动能耗**: ERM较高（需要克服惯性）
- **持续振动**: LRA更节能
- **脉冲反馈**: LRA响应更快，能耗更低

### 优化策略
- 使用闭环驱动器
- 自动共振跟踪
- 过驱动和制动优化

## 与本研究的关联
- 提供触觉/振动功耗的权威数据
- 符合idea.md中"音频、震动"因素
- TI作为行业领导者的数据可信度高

## 标签
`触觉反馈` `振动马达` `ERM` `LRA` `功耗` `TI`
