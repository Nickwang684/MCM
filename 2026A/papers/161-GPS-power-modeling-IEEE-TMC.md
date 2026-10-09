# 161. Modeling and Improving the Energy Performance of GPS Receivers for Location Services

## 基本信息
- **标题**: Modeling and Improving the Energy Performance of GPS Receivers for Location Services
- **期刊/会议**: IEEE Transactions on Mobile Computing (TMC)
- **年份**: 2020
- **DOI/链接**: https://ieeexplore.ieee.org/document/8943418

## 核心内容

### 研究目标
建立GPS接收器的能耗性能模型，并提出改进策略以延长智能手机电池寿命。

### 主要发现
1. GPS定位是智能手机最耗电的功能之一
2. GPS能耗与信号获取时间（TTFF）、定位精度需求密切相关
3. 提出自适应GPS采样策略，根据移动速度和场景调整采样率
4. 冷启动vs热启动能耗差异显著

### 功耗模型要点
- **TTFF能耗**: 冷启动可达30-45秒，热启动2-5秒
- **持续跟踪功耗**: 约25-35mW
- **占空比策略**: 显著降低平均功耗

### 与本研究的关联
- 提供GPS功耗的详细量化模型
- 可用于智能手机定位相关场景的能耗估算
- 支持连续时间功耗建模中的GPS组件

## 关键引用
> "GPS receivers consume significant power during signal acquisition, with cold start consuming up to 10x more energy than hot start."

## 标签
`GPS` `功耗建模` `定位服务` `移动计算` `能耗优化`
