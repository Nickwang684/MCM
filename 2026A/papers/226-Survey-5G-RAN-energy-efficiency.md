# 226. A Survey on 5G Radio Access Network Energy Efficiency

## 基本信息
- **标题**: A Survey on 5G Radio Access Network Energy Efficiency: Massive MIMO, Lean Carrier Design, Sleep Modes, and Machine Learning
- **作者**: Multiple authors
- **来源**: arXiv / IEEE Communications Surveys & Tutorials
- **年份**: 2021
- **链接**: https://arxiv.org/abs/2101.11246

## 主要内容

### 研究背景
- 5G RAN能耗是4G的2-3倍
- 需要系统性的能效提升方案
- 机器学习为能效优化提供新途径

### 能效优化技术分类

#### 1. Massive MIMO能效
$$EE_{MIMO} = \frac{R_{sum}}{P_{total}} = \frac{\sum_{k=1}^{K} R_k}{P_{PA} + P_{circuit} + P_{backhaul}}$$

#### 2. Lean Carrier设计
- 减少始终开启的信号
- 按需发送参考信号
- 节省20-30%基站能耗

#### 3. 休眠模式
| 模式 | 唤醒时间 | 节能效果 |
|------|----------|----------|
| 微休眠 | μs级 | 10-20% |
| 轻休眠 | ms级 | 30-50% |
| 深休眠 | s级 | 60-80% |

#### 4. 机器学习方法
- 流量预测驱动的休眠
- 强化学习优化参数
- 联邦学习保护隐私

### 对智能手机建模的意义
- 理解网络侧能效对终端体验的影响
- 网络优化策略的终端侧响应
- 机器学习在功耗预测中的应用

## 关键词
- 5G RAN, energy efficiency, massive MIMO, sleep mode, machine learning
