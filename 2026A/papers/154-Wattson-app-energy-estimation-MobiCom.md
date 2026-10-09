# 154. Empowering Developers to Estimate App Energy Consumption (Wattson)

## 基本信息
- **标题**: Empowering Developers to Estimate App Energy Consumption
- **作者**: Radhika Mittal, Aman Kansal, Ranveer Chandra
- **机构**: IIT Kharagpur, Microsoft Research
- **会议**: ACM MobiCom
- **年份**: 2012
- **链接**: https://radhikam.web.illinois.edu/WattsonMobicom12.pdf
- **会议级别**: 移动计算领域顶级会议

## 研究内容摘要
本文提出Wattson，一个能量仿真工具，允许开发者在开发工作站上估算移动应用的能耗。该工具可以模拟不同网络条件、运营商和用户设置下的能耗变化。

## 关键发现
1. **能量仿真**：在开发机上模拟手机能耗
2. **场景探索**：支持多种使用场景的能耗预测
3. **开发者友好**：无需实际手机即可优化能耗
4. **变量控制**：可控制网络拥塞、屏幕亮度等变量

## Wattson功能
| 功能 | 描述 |
|-----|------|
| 资源缩放 | 模拟手机CPU/GPU性能 |
| 网络仿真 | 模拟不同网络条件 |
| 能耗预测 | 预测应用能耗 |
| 热点识别 | 识别高能耗代码段 |

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 应用 | ★★★★★ | 应用能耗估算 |
| 功耗 | ★★★★★ | 能耗建模工具 |
| 网络活动 | ★★★★☆ | 网络场景仿真 |
| 屏幕 | ★★★★☆ | 屏幕亮度影响 |

## 与论文研究方向的关联
- **ACM MobiCom顶会**：移动计算最高级别会议
- **开发者工具**：为应用能耗优化提供工具
- **Microsoft Research**：工业界研究权威
- **场景分析**：支持不同使用场景的比较
