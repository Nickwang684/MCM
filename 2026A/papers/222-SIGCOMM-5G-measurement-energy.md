# 222. Understanding Operational 5G: A First Measurement Study on Its Coverage, Performance and Energy Consumption

## 基本信息
- **标题**: Understanding Operational 5G: A First Measurement Study on Its Coverage, Performance and Energy Consumption
- **作者**: Dongzhu Xu, Anfu Zhou, Xinyu Zhang, et al.
- **会议**: ACM SIGCOMM 2020
- **机构**: Beijing University of Posts and Telecommunications, UC San Diego
- **链接**: https://dl.acm.org/doi/10.1145/3387514.3405882

## 主要内容

### 研究背景
- 5G商用网络开始运营
- 实际部署与理论性能存在差距
- 能耗是用户关心的关键问题

### 测量方法
- 中国主要城市5G网络测试
- 多种场景：室内、室外、移动中
- 专用功耗测量设备

### 关键发现

#### 能耗对比 (每GB数据)
| 网络 | 能耗 (Wh/GB) | 相对LTE |
|------|--------------|---------|
| LTE | 0.8-1.2 | 1.0x |
| 5G (sub-6) | 0.6-0.9 | 0.75x |
| 5G (mmWave) | 1.2-2.0 | 1.5x |

#### 功耗-吞吐量关系
$$P = P_0 + \alpha \cdot \text{Throughput} + \beta$$

其中：
- $P_0$ = 基础功耗 (~1W)
- $\alpha$ = 功耗-吞吐量系数
- $\beta$ = 信号条件相关项

### 5G vs LTE效率
- **高吞吐量场景**: 5G更节能 (每比特能耗低)
- **低吞吐量场景**: 5G反而更耗能 (高基础功耗)

### 对智能手机建模的意义
- 5G网络能耗的真实测量数据
- 吞吐量与功耗的关系模型
- 网络选择策略对续航的影响

## 关键词
- 5G, measurement, energy consumption, coverage, performance
