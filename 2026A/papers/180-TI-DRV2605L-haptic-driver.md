# 180. DRV2605L Haptic Driver for LRA and ERM - Texas Instruments Datasheet

## 基本信息
- **标题**: DRV2605L 2- to 5.2-V Haptic Driver for LRA and ERM with Effect Library and Smart-Loop Architecture
- **发布机构**: Texas Instruments
- **文档编号**: SLOS854D
- **年份**: 2018 (Rev. D)
- **类型**: 数据手册
- **链接**: https://www.ti.com/lit/ds/symlink/drv2605l.pdf

## 核心内容

### 器件特性
- 支持LRA和ERM两种振动马达
- I2C控制的数字播放引擎
- 内置效果库（123种波形）
- 智能循环架构

### 功耗规格
| 状态 | 电流 |
|------|------|
| 关断模式 | <1μA |
| 待机模式 | 15μA |
| 空闲（就绪） | 0.5mA |
| 驱动LRA | 10-50mA |
| 驱动ERM | 20-100mA |

### 关键特性
1. **自动共振跟踪**: 保持LRA最佳效率
2. **过驱动和制动**: 缩短响应时间
3. **电池电压补偿**: 保持振动一致性
4. **智能循环**: 降低功耗

### 典型应用
- 智能手机触觉反馈
- 可穿戴设备通知
- 游戏控制器振动

## 与本研究的关联
- 触觉/振动驱动器的详细功耗数据
- 工业标准参考
- 支持idea.md中"震动"功耗建模

## 标签
`触觉驱动器` `LRA` `ERM` `功耗规格` `TI` `数据手册`
