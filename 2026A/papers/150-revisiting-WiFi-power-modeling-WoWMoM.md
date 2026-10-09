# 150. Revisiting 802.11 Power Consumption Modeling in Smartphones

## 基本信息
- **标题**: Revisiting 802.11 Power Consumption Modeling in Smartphones
- **作者**: Swetank Kumar Saha, Pratham Malik, Selvaganesh Dharmeswaran, Dimitrios Koutsonikolas
- **机构**: University at Buffalo, SUNY
- **会议**: IEEE WoWMoM
- **年份**: 2016
- **链接**: https://cse.buffalo.edu/faculty/dimitrio/publications/wowmom16.pdf

## 研究内容摘要
本文重新审视了智能手机802.11 WiFi功耗建模方法。作者评估并改进了Serrano等人提出的"跨因素"(cross-factor)模型，该模型考虑了帧在协议栈中传输的能量消耗。

## 关键发现
1. **跨因素(cross-factor)概念**：帧穿越协议栈需要额外能量
2. **模型组成**：
   - NIC功耗（传统WiFi功耗）
   - 跨因素功耗（协议栈处理）
3. **多设备验证**：在多种Android设备上验证模型
4. **精度提升**：考虑跨因素后预测误差减少40%

## WiFi功耗分解
$$P_{total} = P_{NIC} + P_{cross}$$

$$P_{NIC} = P_{tx} \cdot T_{tx} + P_{rx} \cdot T_{rx} + P_{idle} \cdot T_{idle}$$

$$P_{cross} = k_{cross} \cdot N_{frames}$$

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 网络活动 | ★★★★★ | WiFi功耗详细分解 |
| 功耗 | ★★★★★ | 精确功耗模型 |
| 处理器负载 | ★★★★☆ | 协议栈处理负载 |

## 与论文研究方向的关联
- **模型改进**：跨因素概念提高了WiFi功耗预测精度
- **系统级视角**：考虑NIC和CPU的协同功耗
- **多设备验证**：增强模型的普适性
- **方法论参考**：功耗分解的思路可推广
