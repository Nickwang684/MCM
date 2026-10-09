# 258. ACM SenSys - Mobile Sensing Power Optimization

## 基本信息
- **标题**: Adaptive Mobile Sensing with Power-Aware Optimization
- **会议**: ACM SenSys
- **年份**: 2022
- **类型**: 系统论文

## 主要内容

### 移动感知功耗分析

| 传感器 | 典型功耗 | 采样率 | 能耗/样本 |
|--------|----------|--------|-----------|
| 加速度计 | 0.5-2 mW | 50 Hz | 10-40 μJ |
| 陀螺仪 | 3-6 mW | 50 Hz | 60-120 μJ |
| 磁力计 | 1-3 mW | 10 Hz | 100-300 μJ |
| 气压计 | 0.1-0.5 mW | 1 Hz | 100-500 μJ |
| GPS | 50-150 mW | 1 Hz | 50-150 mJ |
| 相机 | 200-500 mW | 30 fps | 7-17 mJ |

### 自适应采样策略

#### 1. 活动感知采样
$$f_{sample} = f(Activity\_Level)$$

```
静止: 1 Hz
步行: 10 Hz
跑步: 50 Hz
```

#### 2. 传感器融合节能
用低功耗传感器触发高功耗传感器

$$E_{fused} = E_{trigger} + P_{trigger} \cdot E_{primary}$$

#### 3. 批处理
$$E_{batch} = E_{wakeup} + n \cdot E_{sample}$$

批量唤醒比单次唤醒更节能

### 节能效果
- 自适应采样：节省40-60%
- 传感器融合：节省30-50%
- 批处理：节省20-30%

### 对智能手机建模的意义
- 传感器功耗的精确数据
- 采样策略对功耗的影响
- 感知应用的能耗建模

## 关键词
- Mobile sensing, power optimization, adaptive sampling, sensor fusion
