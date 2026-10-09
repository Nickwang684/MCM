# 230. WiFi Energy Consumption Modeling and Optimization

## 基本信息
- **标题**: WiFi Energy Consumption: Measurement, Modeling and Optimization (综合)
- **来源**: Multiple ACM/IEEE papers
- **年份**: 2015-2024

## 主要内容

### WiFi功耗模型综述

#### 基本功耗模型
$$P_{WiFi} = P_{idle} + P_{tx} \cdot D_{tx} + P_{rx} \cdot D_{rx}$$

其中：
- $P_{idle}$ ≈ 50-100mW
- $P_{tx}$ ≈ 800-1200mW
- $P_{rx}$ ≈ 400-600mW
- $D_{tx/rx}$ = 占空比

#### 状态机模型
```
┌────────┐      ┌────────┐      ┌────────┐
│  IDLE  │ ←──→ │  SCAN  │ ←──→ │ ACTIVE │
│ 50mW   │      │ 500mW  │      │ 800mW  │
└────────┘      └────────┘      └────────┘
```

### 信号强度影响
| RSSI (dBm) | 发射功率 | 相对能耗 |
|------------|----------|----------|
| -50 | 低 | 1.0x |
| -70 | 中 | 1.3x |
| -85 | 高 | 1.8x |
| -90 | 最高 | 2.5x |

### PSM (省电模式)
$$E_{PSM} = E_{beacon} \cdot N_{beacon} + E_{active} \cdot T_{active}$$

- Beacon间隔：100ms (典型)
- 节能效果：30-50%

### WiFi 6 (802.11ax) 能效改进
- TWT (目标唤醒时间): 节省40%
- OFDMA: 提高频谱效率
- BSS Coloring: 减少干扰

### 对智能手机建模的意义
- WiFi各状态的功耗数值
- 信号强度对功耗的影响
- PSM和TWT的节能效果模型

## 关键词
- WiFi, power consumption, PSM, TWT, 802.11ax, RSSI
