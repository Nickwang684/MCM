# 167. Understanding Energy Consumption of Sensor Enabled Applications on Mobile Phones

## 基本信息
- **标题**: Understanding Energy Consumption of Sensor Enabled Applications on Mobile Phones
- **期刊/会议**: IEEE EMBC (Engineering in Medicine and Biology Conference)
- **年份**: 2009
- **作者**: Igor Crk, Fahd Albinali, Chris Gniady, John Hartman
- **机构**: MIT / University of Arizona
- **链接**: https://dspace.mit.edu/handle/1721.1/53727

## 核心内容

### 研究背景
- 智能手机传感器应用快速增长（健康监测、运动追踪）
- 传感器能耗对电池寿命影响缺乏系统研究

### 研究方法
1. **硬件级测量**: 精确电流/电压采集
2. **软件级分析**: 应用层能耗分解
3. **综合评估**: 传感器+处理+传输能耗

### 主要发现
- **传感器采集能耗**: 占总能耗10-30%
- **数据处理能耗**: 占总能耗40-60%
- **无线传输能耗**: 占总能耗20-40%

### 各传感器能耗特征
| 传感器类型 | 典型功耗 | 特点 |
|------------|----------|------|
| 加速度计 | 低 | 始终在线可行 |
| 陀螺仪 | 中高 | 需要间歇采样 |
| GPS | 高 | 仅按需使用 |
| 音频 | 中 | 取决于采样率 |

### 优化建议
- 自适应采样率
- 本地预处理减少传输
- 传感器协同调度

## 与本研究的关联
- 传感器应用的能耗分解分析
- 支持功耗建模中的传感器组件
- 医疗/健康应用场景参考

## 标签
`传感器` `能耗分析` `移动健康` `EMBC` `医疗应用`
