# 224. Traffic-aware Techniques to Reduce 3G/LTE Wireless Energy Consumption

## 基本信息
- **标题**: Traffic-aware Techniques to Reduce 3G/LTE Wireless Energy Consumption
- **作者**: Feng Qian et al.
- **会议**: ACM CoNEXT 2012
- **机构**: AT&T Labs Research, University of Michigan
- **链接**: https://dl.acm.org/doi/10.1145/2413176.2413198

## 主要内容

### 研究背景
- 无线网络是手机主要耗电源之一
- RRC状态机导致大量尾部能耗
- 需要流量感知的节能技术

### RRC状态机模型
```
         ┌───────────────┐
         │  CONNECTED    │ (高功耗: 1.5-2W)
         │  (DCH/FACH)   │
         └───────┬───────┘
                 │ inactivity timer
                 ▼
         ┌───────────────┐
         │   PCH/IDLE    │ (低功耗: <0.1W)
         └───────────────┘
```

### 尾部能耗问题
$$E_{tail} = P_{high} \times T_{inactivity}$$

典型值：
- 3G尾部：12秒，消耗约12-18焦耳
- LTE尾部：5秒，消耗约5-8焦耳

### 节能技术
1. **快速休眠 (Fast Dormancy)**: 主动触发状态转换
2. **请求合并**: 批量处理网络请求
3. **预取**: 预测性数据加载
4. **延迟容忍**: 推迟非紧急传输

### 节能效果
- 快速休眠：节省20-30%无线能耗
- 请求合并：节省15-25%
- 组合策略：节省40-50%

### 对智能手机建模的意义
- RRC状态机的能耗模型
- 尾部能耗的量化方法
- 应用层网络行为对功耗的影响

## 关键词
- RRC state machine, tail energy, fast dormancy, LTE, 3G, traffic-aware
