# 168. Sensors are Power Hungry: An Investigation of Smartphone Sensors Impact on Battery Power from Lifelogging Perspective

## 基本信息
- **标题**: Sensors are Power Hungry: An Investigation of Smartphone Sensors Impact on Battery Power from Lifelogging Perspective
- **期刊/会议**: ResearchGate / Conference
- **年份**: 2016
- **链接**: https://www.researchgate.net/publication/317494054

## 核心内容

### 研究动机
- 生活日志(Lifelogging)应用需要持续传感器采集
- 电池续航成为主要瓶颈
- 需要量化各传感器对电池的影响

### 实验设计
1. **测试传感器**: 加速度计、陀螺仪、磁力计、GPS、相机、麦克风
2. **测试场景**: 持续采集、间歇采集、组合采集
3. **测量指标**: 电池消耗率、温度变化、续航时间

### 关键结果
| 传感器组合 | 电池消耗率 | 估计续航 |
|------------|------------|----------|
| 仅加速度计 | 1.5%/h | 67h |
| 加速度计+陀螺仪 | 3.2%/h | 31h |
| 全传感器 | 8.5%/h | 12h |
| +GPS | 15%/h | 7h |
| +相机 | 25%/h | 4h |

### 发现
- **GPS最耗电**: 是加速度计的10倍以上
- **相机次之**: 视频录制极度耗电
- **惯性传感器相对节能**: 适合always-on应用

### 建议
- 分层传感器策略
- 低功耗传感器触发高功耗传感器
- 云端offloading处理任务

## 与本研究的关联
- 提供传感器功耗的综合对比数据
- 生活日志场景接近持续使用模式
- 直接支持idea.md中传感器功耗建模

## 标签
`传感器` `功耗对比` `生活日志` `电池续航` `多传感器`
