# RAPS: Energy-Efficient Rate-Adaptive GPS Positioning

## 基本信息
- **标题**: Energy-efficient rate-adaptive GPS-based positioning for smartphones
- **发表日期**: 2010-06-15
- **会议**: **ACM MobiSys '10**
- **链接**: https://dl.acm.org/doi/10.1145/1814433.1814463

## 研究内容
提出**RAPS(速率自适应定位系统)**，用于智能手机的节能GPS定位。

## 与考虑因素的相关性

### GPS高功耗问题
- **极其耗电**: GPS被描述为"extremely power hungry"
- **占空比权衡**: 降低采样率节省能量但降低精度
- **需要智能调度**: 自适应采样策略

### 速率自适应
- 根据移动状态调整采样率
- 静止时减少采样
- 移动时增加采样

### 精度-能耗权衡
- 平衡定位精度和能耗
- 满足应用需求的最低采样
- 智能策略节省能量

## 核心方法
1. 检测用户移动状态
2. 自适应调整GPS采样率
3. 最小化能耗同时保证精度

## 与论文研究方向的关联
- **GPS功耗**: 位置服务能耗
- **MobiSys顶会**: 移动系统权威
- **智能策略**: 节能方法参考
