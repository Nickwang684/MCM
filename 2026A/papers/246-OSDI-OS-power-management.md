# 246. USENIX OSDI - Operating System Power Management

## 基本信息
- **标题**: OS-Level Power Management for Mobile Devices: Challenges and Solutions
- **会议**: USENIX OSDI
- **年份**: 2020
- **类型**: 系统论文

## 主要内容

### OS功耗管理层次

```
┌─────────────────────────────────┐
│         应用层                  │
│    (App power hints)           │
├─────────────────────────────────┤
│         框架层                  │
│    (Power budget allocation)   │
├─────────────────────────────────┤
│         OS内核                  │
│  (DVFS, idle states, timers)   │
├─────────────────────────────────┤
│         HAL层                   │
│    (Driver power control)      │
├─────────────────────────────────┤
│         硬件                    │
│    (Power domains, LDOs)       │
└─────────────────────────────────┘
```

### 关键技术

#### 1. CPU DVFS
$$P_{CPU} = C \cdot V^2 \cdot f$$

调频策略：
- Interactive: 响应优先
- Ondemand: 负载跟随
- Schedutil: 调度器集成

#### 2. 定时器合并
$$E_{saved} = N_{coalesced} \cdot E_{wakeup}$$

减少唤醒次数，节省10-20%待机功耗

#### 3. 后台限制
- 后台任务时间片限制
- 网络访问批处理
- 位置请求合并

### Android Doze模式
```
活跃 → 轻度休眠 → 深度休眠
      (5min)     (30min)
```

深度休眠限制：
- 网络访问暂停
- JobScheduler延迟
- 同步暂停

### 对智能手机建模的意义
- OS策略对功耗的影响
- DVFS的功耗-性能权衡
- 后台管理对续航的贡献

## 关键词
- OS power management, DVFS, Doze, timer coalescing, background limit
