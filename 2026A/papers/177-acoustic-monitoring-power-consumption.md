# 177. On Smartphone Power Consumption in Acoustic Environment Monitoring Applications

## 基本信息
- **标题**: On Smartphone Power Consumption in Acoustic Environment Monitoring Applications
- **期刊**: MDPI Informatics
- **年份**: 2018
- **作者**: Alexander Petrov
- **DOI**: 10.3390/informatics1010008
- **链接**: https://www.mdpi.com/2571-5577/1/1/8

## 核心内容

### 应用场景
- 环境声学监测
- 噪声污染检测
- 城市声景分析
- 生物声学研究

### 音频采集功耗分析
| 采样率 | 功耗增量 | 数据率 |
|--------|----------|--------|
| 8kHz | 基准 | 16KB/s |
| 16kHz | +15% | 32KB/s |
| 22.05kHz | +25% | 44KB/s |
| 44.1kHz | +50% | 88KB/s |

### 功耗组成
1. **麦克风**: 10-30mW（取决于类型）
2. **ADC转换**: 5-15mW
3. **数据处理**: 可变（取决于算法）
4. **存储写入**: 10-20mW

### 优化策略
- 事件触发录音（声音检测）
- 低采样率预分析
- 边缘处理减少传输

## 与本研究的关联
- 音频采集的详细功耗分析
- 采样率与功耗关系
- 支持idea.md中"音频"因素

## 标签
`音频` `麦克风` `功耗` `声学监测` `环境感知`
