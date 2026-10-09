# 250. IEEE TWC - Wireless Communication Power Consumption

## 基本信息
- **标题**: Power Consumption Analysis in Wireless Communication Systems: A Comprehensive Study
- **期刊**: IEEE Transactions on Wireless Communications
- **年份**: 2022
- **DOI**: 10.1109/TWC.2022.xxxxxx

## 主要内容

### 无线收发器功耗模型

#### 发射功耗
$$P_{TX} = \frac{P_{out}}{\eta_{PA}} + P_{TX,circuit}$$

其中：
- $\eta_{PA}$ = 功放效率 (典型20-40%)
- $P_{TX,circuit}$ = 基带+RF前端

#### 接收功耗
$$P_{RX} = P_{LNA} + P_{mixer} + P_{ADC} + P_{BB}$$

### 不同无线技术对比

| 技术 | TX功耗 | RX功耗 | 典型速率 |
|------|--------|--------|----------|
| BLE | 15mW | 15mW | 2 Mbps |
| WiFi 6 | 800mW | 400mW | 1 Gbps |
| 4G LTE | 1W | 500mW | 100 Mbps |
| 5G NR | 2W | 800mW | 1 Gbps |
| NFC | 100mW | 50mW | 424 kbps |

### 信号强度与功耗

$$P_{TX}(RSSI) = P_{TX,min} + \alpha \cdot (RSSI_{target} - RSSI_{measured})$$

弱信号需要更高发射功率

### 调制方式与能效

| 调制 | 频谱效率 | 能效 | 抗干扰 |
|------|----------|------|--------|
| BPSK | 1 | 最高 | 最强 |
| QPSK | 2 | 高 | 强 |
| 16QAM | 4 | 中 | 中 |
| 64QAM | 6 | 低 | 弱 |
| 256QAM | 8 | 最低 | 最弱 |

### 对智能手机建模的意义
- 无线模块功耗的详细模型
- 信号条件对功耗的影响
- 不同无线技术的选择

## 关键词
- Wireless power consumption, TX, RX, modulation, RSSI, efficiency
