# 247. ACM EuroSys - Energy-Aware Scheduling

## 基本信息
- **标题**: Energy-Aware Scheduling for Mobile and Embedded Systems
- **会议**: ACM EuroSys
- **年份**: 2021
- **类型**: 系统论文

## 主要内容

### 能效调度目标
$$\min E_{total} = \int_0^T P(t) \, dt$$
$$\text{s.t. } \text{Deadline constraints met}$$

### 调度策略分类

#### 1. EAS (Energy Aware Scheduling)
ARM big.LITTLE调度：
$$\text{Task} \rightarrow \begin{cases} \text{Big core} & \text{if } \text{load} > \text{threshold} \\ \text{Little core} & \text{otherwise} \end{cases}$$

#### 2. WALT (Window Assisted Load Tracking)
$$\text{Load}_{avg} = \alpha \cdot \text{Load}_{current} + (1-\alpha) \cdot \text{Load}_{prev}$$

#### 3. SchedTune
能效提示：
```c
struct sched_attr {
    util_min,  // 最小利用率
    util_max,  // 最大利用率
    latency_nice  // 延迟敏感度
};
```

### 能效对比

| 策略 | 能耗 | 性能 | 适用场景 |
|------|------|------|----------|
| 性能优先 | 高 | 最佳 | 游戏 |
| 平衡 | 中 | 良好 | 日常 |
| 节能 | 低 | 可接受 | 低电量 |

### 实测数据
- Big.LITTLE节能：20-40%
- EAS vs CFS：15-25%节能
- SchedTune微调：5-10%额外节能

### 对智能手机建模的意义
- CPU调度对功耗的影响
- 多核处理器能效建模
- 负载-功耗关系

## 关键词
- Energy-aware scheduling, EAS, big.LITTLE, WALT, SchedTune
