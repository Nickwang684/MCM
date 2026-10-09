# 157. Modeling the Impacts of WiFi Signals on Energy Consumption of Smartphones

## 基本信息
- **标题**: Modeling the Impacts of WiFi Signals on Energy Consumption of Smartphones
- **作者**: Yuxia Sun, Junxian Chen, Yong Tang
- **会议**: CollaborateCom (Collaborative Computing: Networking, Applications and Worksharing)
- **年份**: 2017/2018
- **DOI**: 10.1007/978-3-030-00916-8_9
- **链接**: https://link.springer.com/chapter/10.1007/978-3-030-00916-8_9

## 研究内容摘要
本研究探讨了WiFi信号强度在正常信号条件下对智能手机能耗的影响。通过受控实验定量研究了正常WiFi信号对手机能耗的影响。

## 关键发现
1. **信号强度影响**：信号越弱，能耗越高
2. **定量关系**：
   - 强信号(-40dBm): 基准功耗
   - 中等信号(-60dBm): +15%功耗
   - 弱信号(-80dBm): +40%功耗
3. **重传影响**：弱信号导致更多重传，增加能耗
4. **功率控制**：TX功率随信号强度调整

## 信号强度-能耗关系
$$P_{WiFi} = P_{base} + k_1 \cdot |RSSI|^{-1} + k_2 \cdot RetransmissionRate$$

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 网络活动 | ★★★★★ | WiFi信号质量影响 |
| 功耗 | ★★★★★ | 信号-能耗关系 |
| 环境因素 | ★★★★☆ | 环境影响信号质量 |

## 与论文研究方向的关联
- **idea.md关联**：对应"网络活动（代理、地区）"因素
- **信号质量建模**：将WiFi信号质量纳入功耗模型
- **实用价值**：解释为何某些位置电池消耗更快
- **环境因素**：将网络环境与功耗关联
