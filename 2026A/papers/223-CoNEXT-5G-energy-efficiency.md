# 223. Sustainable Connections: Exploring Energy Efficiency in 5G Networks

## 基本信息
- **标题**: Sustainable Connections: Exploring Energy Efficiency in 5G Networks
- **作者**: Yibo Ma, Tong Li, Yuwei Du, et al.
- **会议**: ACM CoNEXT 2024
- **机构**: Tsinghua University, TU Wien
- **链接**: https://conferences.sigcomm.org/co-next/2024/

## 主要内容

### 研究背景
- 5G网络能效是可持续发展的关键
- 基站和终端的能耗需要优化
- 网络侧节能与用户体验的平衡

### 能效指标
$$EE = \frac{\text{Throughput (Gbps)}}{\text{Power (W)}}$$

### 关键发现

#### 基站能耗分解
| 组件 | 占比 |
|------|------|
| 功放 (PA) | 50-60% |
| 基带处理 | 20-30% |
| 冷却系统 | 10-15% |
| 其他 | 5-10% |

#### 终端能效优化
1. **动态带宽适配**: 根据需求调整
2. **智能休眠**: 减少不必要的连接
3. **载波聚合优化**: 平衡速度和功耗

### 5G能效模型
$$P_{UE} = P_{idle} + P_{active}(\text{BW}, \text{MCS}, \text{TX power})$$

### 对智能手机建模的意义
- 5G能效的系统性分析
- 终端侧节能策略
- 网络条件对手机功耗的影响

## 关键词
- 5G, energy efficiency, sustainable, network optimization
