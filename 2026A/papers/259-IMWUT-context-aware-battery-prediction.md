# 259. ACM UbiComp/IMWUT - Context-Aware Battery Prediction

## 基本信息
- **标题**: Context-Aware Battery Lifetime Prediction for Mobile Devices
- **期刊**: Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT)
- **年份**: 2023
- **DOI**: 10.1145/xxxxxx

## 主要内容

### 上下文因素

| 上下文类别 | 具体因素 | 对功耗影响 |
|------------|----------|------------|
| 位置 | 室内/室外/地下 | 网络信号差异 |
| 活动 | 静止/移动/运动 | 传感器使用 |
| 时间 | 工作/休息/睡眠 | 使用强度 |
| 环境 | 温度/湿度 | 电池效率 |

### 预测模型架构

```
上下文特征         时序模型         预测结果
┌─────────┐      ┌─────────┐      ┌─────────┐
│ Location│      │         │      │剩余时间 │
│ Activity│─────>│  LSTM   │─────>│ ±5min   │
│ Time    │      │  +      │      │精度<10% │
│ History │      │Attention│      └─────────┘
└─────────┘      └─────────┘
```

### 功耗-上下文关系
$$P(t) = P_{base} + \sum_i \alpha_i \cdot C_i(t) + \epsilon(t)$$

其中 $C_i(t)$ 为上下文特征

### 预测精度

| 预测窗口 | MAPE | 方法 |
|----------|------|------|
| 30分钟 | 5-8% | LSTM+Context |
| 1小时 | 8-12% | LSTM+Context |
| 2小时 | 12-18% | LSTM+Context |
| 4小时 | 15-25% | LSTM+Context |

### 用户研究发现
- 用户偏好保守估计
- 准确性比精确性更重要
- 需要解释为什么

### 对智能手机建模的意义
- 上下文感知的功耗预测
- 剩余时间估计的准确性
- 用户可理解的预测模型

## 关键词
- Context-aware, battery prediction, LSTM, mobile device, remaining time
