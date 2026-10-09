# 165. SensingKit: Evaluating the Sensor Power Consumption in iOS Devices

## 基本信息
- **标题**: SensingKit: Evaluating the Sensor Power Consumption in iOS devices
- **期刊/会议**: arXiv / ACM Workshop
- **年份**: 2016
- **作者**: Kleomenis Katevas, Hamed Haddadi, Laurissa Tokarchuk
- **机构**: Queen Mary University of London
- **链接**: https://arxiv.org/abs/1606.05576

## 核心内容

### 研究目标
- 开发跨平台传感器采集库
- 系统评估iOS设备上各传感器的功耗

### 测量的传感器
1. **加速度计** (Accelerometer)
2. **陀螺仪** (Gyroscope)
3. **磁力计** (Magnetometer)
4. **气压计** (Barometer)
5. **GPS/Location**
6. **麦克风** (Audio)
7. **Motion处理器**

### 关键功耗数据
| 传感器 | 采样率 | 功耗增量 |
|--------|--------|----------|
| 加速度计 | 100Hz | ~2-5mW |
| 陀螺仪 | 100Hz | ~6-12mW |
| 磁力计 | 100Hz | ~3-6mW |
| GPS | 持续 | ~25-40mW |
| 气压计 | 1Hz | <1mW |

### 方法论
- 精确功耗测量设备
- 控制变量实验设计
- 多设备验证（iPhone 5s, 6, 6s）

## 与本研究的关联
- 提供iOS传感器功耗的权威数据
- 直接支持智能手机传感器功耗建模
- 与idea.md中"传感器"因素对应

## 标签
`传感器` `iOS` `功耗测量` `加速度计` `陀螺仪`
