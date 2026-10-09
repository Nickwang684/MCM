# 221. A Variegated Look at 5G in the Wild: Performance, Power, and QoE Implications

## 基本信息
- **标题**: A Variegated Look at 5G in the Wild: Performance, Power, and QoE Implications
- **作者**: Arvind Narayanan, Xumiao Zhang, Ruiyang Zhu, Ahmad Hassan, et al.
- **会议**: ACM SIGCOMM 2021
- **机构**: University of Minnesota, University of Michigan
- **链接**: https://dl.acm.org/doi/10.1145/3452296.3472923

## 主要内容

### 研究背景
- 5G网络快速部署，但实际性能如何？
- 5G对手机功耗的影响未被充分研究
- 需要全面评估5G的性能-功耗-QoE权衡

### 关键发现

#### 5G功耗特性
| 网络类型 | 平均功耗 | 峰值功耗 |
|----------|----------|----------|
| LTE | ~1.5W | ~2.5W |
| 5G SA | ~2.5W | ~4.0W |
| 5G mmWave | ~3.5W | ~5.5W |

#### RRC状态功耗
```
RRC Connected: 2.5-4W (5G)
RRC Inactive:  0.5-1W
RRC Idle:      <0.1W
```

### 核心观察
1. **5G mmWave功耗高**: 比LTE高2-3倍
2. **RRC状态转换延迟**: 5G的RRC状态转换更耗能
3. **下行大于上行**: 下载场景功耗更可控
4. **信号强度敏感**: 弱信号时功耗显著增加

### 功耗模型
$$P_{5G}(t) = P_{base} + P_{TX}(SNR, MCS) + P_{RX}(throughput)$$

### 对智能手机建模的意义
- 5G网络功耗的实测数据
- 不同5G部署方式的功耗对比
- RRC状态转换对功耗的影响模型

## 关键词
- 5G, power consumption, mmWave, NSA, SA, RRC state, QoE
