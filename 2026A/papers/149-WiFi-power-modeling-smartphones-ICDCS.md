# 149. Modeling WiFi Active Power/Energy Consumption in Smartphones (ICDCS 2014)

## 基本信息
- **标题**: Modeling WiFi Active Power/Energy Consumption in Smartphones
- **作者**: Li Sun, Ramanujan K. Sheshadri, Wei Zheng, Dimitrios Koutsonikolas
- **会议**: IEEE International Conference on Distributed Computing Systems (ICDCS)
- **年份**: 2014
- **链接**: https://ece.northeastern.edu/fac-ece/dkoutsonikolas/publications/icdcs14.pdf
- **类型**: 会议论文

## 研究内容摘要
本文对智能手机WiFi活动功耗模型进行了首次详细的测量研究。研究分析了应用层吞吐量与WiFi功耗之间的关系，建立了实用的功耗预测模型。

## 关键发现
1. **线性功率-吞吐量模型**：
$$P_{WiFi} = P_{base} + k \cdot Throughput$$

2. **802.11n特性**：
   - 空闲功率：~100mW
   - 最大活动功率：~800mW
3. **模型局限**：现有模型在高吞吐量时欠预测
4. **改进建议**：提出分段线性模型

## WiFi功耗模型
| 状态 | 功率范围 | 主要影响因素 |
|-----|---------|-------------|
| 空闲(idle) | 50-100mW | 扫描周期 |
| 低吞吐量 | 200-400mW | 发包数 |
| 中吞吐量 | 400-600mW | 吞吐量 |
| 高吞吐量 | 600-800mW | 吞吐量+协议栈 |

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 网络活动 | ★★★★★ | 核心研究主题 |
| 功耗 | ★★★★★ | WiFi功耗建模 |
| 应用 | ★★★★☆ | 应用层吞吐量 |

## 与论文研究方向的关联
- **idea.md关联**：直接对应"网络活动"功耗因素
- **实用模型**：可直接应用于智能手机电池续航预测
- **ICDCS会议**：分布式计算领域顶级会议
- **开发者友好**：模型参数对应用开发者可获取
