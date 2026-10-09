# An Analysis of Power Consumption in a Smartphone

## 基本信息
- **标题**: An Analysis of Power Consumption in a Smartphone
- **作者**: Aaron Carroll, Gernot Heiser
- **机构**: NICTA, University of New South Wales
- **会议**: USENIX Annual Technical Conference
- **年份**: 2010
- **链接**: https://www.usenix.org/legacy/event/atc10/tech/full_papers/Carroll.pdf

## 研究内容
对智能手机（Openmoko Neo Freerunner）进行详细的功耗分析，测量整体系统功率和主要硬件组件的功耗分解。

## 核心方法
- **直接功率测量**: 各硬件组件的独立功率测量
- **微基准测试**: SPEC CPU2000和定制微基准
- **宏基准测试**: 典型使用场景的功耗
- **功率模型**: 基于测量构建功率模型

## 组件功耗分析
| 组件 | 功耗占比 |
|------|----------|
| 显示屏 | 38-50% |
| 蜂窝网络 | 20-35% |
| CPU | 10-20% |
| 内存/存储 | 5-10% |
| 音频 | 2-5% |
| 其他 | <5% |

## 与考虑因素的相关性

### 功耗因素
- **屏幕功耗**: 最大的功耗来源
- **网络活动**: 蜂窝网络是第二大功耗
- **CPU负载**: DVFS对CPU功耗的影响
- **音频/震动**: 相对较小但不可忽视

## 关键发现
1. 显示屏是最大的功耗来源
2. 蜂窝网络即使空闲也消耗显著功率
3. DVFS可有效降低CPU功耗但有限

## 与论文研究方向的关联
这是智能手机功耗分析的经典论文，提供了组件级功耗分解的基准数据和方法论。
