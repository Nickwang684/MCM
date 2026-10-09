# 153. V-edge: Fast Self-constructive Power Modeling of Smartphones Based on Battery Voltage Dynamics

## 基本信息
- **标题**: V-edge: Fast Self-constructive Power Modeling of Smartphones Based on Battery Voltage Dynamics
- **作者**: Fengyuan Xu, Yunxin Liu, Qun Li, Yongguang Zhang
- **机构**: College of William and Mary, Microsoft Research Asia
- **会议**: USENIX NSDI
- **年份**: 2013
- **链接**: https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final135.pdf
- **会议级别**: 系统领域顶级会议

## 研究内容摘要
本文提出V-edge，一种基于电池电压动态特性的快速自建构功耗模型。该方法无需外部功率计，无需电流传感器，可在普通智能手机上自动建立功耗模型。

## 关键发现
1. **创新方法**：利用电池电压边缘(voltage edge)推断功耗
2. **无需外部设备**：仅使用手机内置传感器
3. **快速建模**：模型建立时间<1分钟
4. **精度验证**：与地面真值相比误差<10%

## V-edge方法原理
**电压-功率关系**：
$$\Delta V = f(P, SOC, T)$$

**功率推断**：
$$P = g(\frac{dV}{dt}, V, T)$$

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 功耗 | ★★★★★ | 功耗建模核心方法 |
| SOC估计 | ★★★★☆ | 电压-SOC关系 |
| 电池特性 | ★★★★☆ | 电池电压动态 |

## 与论文研究方向的关联
- **USENIX NSDI顶会**：系统领域最高级别会议
- **实用性强**：无需额外硬件即可应用
- **自适应建模**：可针对特定设备自动调整
- **Microsoft Research**：工业界顶尖研究机构
