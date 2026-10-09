# Energy Aware Scheduling (EAS) in Linux Kernel

## 基本信息
- **标题**: Energy Aware Scheduling
- **来源**: Linux Kernel Documentation
- **链接**: https://www.kernel.org/doc/html/v5.15/scheduler/sched-energy.html

## 研究内容
描述Linux内核中的**能量感知调度(EAS)**机制。

## 与考虑因素的相关性

### 操作系统能耗管理
- **调度器优化**: 在任务调度时考虑能耗
- **能量模型(EM)**: 使用CPU能量模型指导调度
- **性能/功耗比**: 最大化能效比

### 异构CPU支持
- ARM big.LITTLE支持
- 任务到合适CPU的分配
- 负载与能力匹配

### 内核级优化
- Linux内核实现
- CFS调度器扩展
- 无需应用修改

## 核心机制
1. CPU能量模型定义
2. 能量感知任务放置
3. 频率选择优化

## 与论文研究方向的关联
- **处理器负载**: CPU能耗管理
- **操作系统**: 系统级节能策略
- **用户建议**: 理解系统行为
