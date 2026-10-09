# 249. IEEE JSAC - Mobile Network Energy Efficiency

## 基本信息
- **标题**: Energy Efficiency in Mobile Networks: From Protocol Design to System Optimization
- **期刊**: IEEE Journal on Selected Areas in Communications
- **年份**: 2023
- **类型**: 综述论文

## 主要内容

### 移动网络能效定义
$$EE = \frac{\text{Throughput (bits)}}{\text{Energy (Joule)}} \quad \text{(bits/J)}$$

### 协议层能效分析

#### 物理层
$$E_{PHY} = \frac{P_{TX} + P_{circuit}}{R}$$

其中：
- $P_{TX}$ = 发射功率
- $P_{circuit}$ = 电路功耗
- $R$ = 数据速率

#### MAC层
$$E_{MAC} = \frac{E_{PHY}}{1 - P_{collision}}$$

碰撞概率增加能耗

#### 网络层
$$E_{NET} = E_{MAC} \cdot (1 + H_{overhead})$$

$H_{overhead}$ = 头部开销

### RRC状态能效

| 状态 | 功耗 | 数据能力 | 转换延迟 |
|------|------|----------|----------|
| CONNECTED | 高 | 即时 | - |
| INACTIVE | 中 | 快速恢复 | 10-50ms |
| IDLE | 低 | 需建立 | 50-200ms |

### 能效优化技术
1. **DRX**: 不连续接收，节省30-50%
2. **DTX**: 不连续发送
3. **自适应调制**: 根据信道调整
4. **功率控制**: 最小必要功率

### 对智能手机建模的意义
- 网络协议能效的量化模型
- RRC状态转换的能耗
- 网络条件对功耗的影响

## 关键词
- Mobile network, energy efficiency, RRC, DRX, protocol optimization
