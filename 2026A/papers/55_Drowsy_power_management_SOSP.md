# Drowsy: Power Management for Mobile OS

## 基本信息
- **标题**: Drowsy: A New Power Management State for Mobile Devices
- **会议**: **USENIX SOSP 2015**
- **链接**: https://users.cs.duke.edu/~mlentz/papers/drowsy_sosp2015.pdf

## 研究内容
提出**Drowsy**，一种Android操作系统内核中的新电源管理状态，提高短任务的能效。

## 与考虑因素的相关性

### 操作系统电源管理
- **新电源状态**: 替代传统"唤醒"状态
- **短任务优化**: 针对移动设备常见的短任务
- **内核级实现**: Android内核实现

### 传统方法问题
- 传统Linux/Android唤醒所有组件
- 短任务效率低下
- 能量浪费

### 效率提升
- 仅唤醒必要组件
- 减少不必要能耗
- 适应移动使用模式

## 核心贡献
1. Drowsy电源状态设计
2. Android内核实现
3. 显著能效提升

## 与论文研究方向的关联
- **操作系统策略**: 系统级节能
- **SOSP顶会**: 操作系统顶级会议
- **用户建议**: 理解系统行为
