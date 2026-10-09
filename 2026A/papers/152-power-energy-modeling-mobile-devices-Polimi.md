# 152. On Power and Energy Consumption Modeling for Smart Mobile Devices

## 基本信息
- **标题**: On Power and Energy Consumption Modeling for Smart Mobile Devices
- **作者**: M. Ferroni, A. Cazzola, F. Trovò, D. Sciuto, M.D. Santambrogio
- **机构**: Politecnico di Milano (米兰理工大学)
- **年份**: 2014
- **链接**: https://trovo.faculty.polimi.it/01papers/ferroni2014power.pdf
- **类型**: 研究论文

## 研究内容摘要
本文提出了智能移动设备功耗和能耗建模的通用方法论。研究识别了主要功耗组件，并建立了组件级和系统级的功耗模型。

## 关键发现
1. **功耗组件分解**：
   - CPU: 20-40%
   - 屏幕: 30-50%
   - 无线通信: 10-30%
   - 其他: 10-20%
2. **动态功耗**：与工作负载密切相关
3. **静态功耗**：即使空闲也有基础功耗
4. **模型通用性**：适用于多种Android设备

## 功耗模型框架
**系统总功耗**：
$$P_{total} = P_{CPU} + P_{screen} + P_{wireless} + P_{GPU} + P_{memory} + P_{base}$$

**CPU功耗**：
$$P_{CPU} = P_{idle} + \sum_{i} (P_{core,i} \cdot U_i \cdot f_i^{\alpha})$$

其中 $U_i$ 为核心利用率，$f_i$ 为频率，$\alpha \approx 2$

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 功耗 | ★★★★★ | 核心研究主题 |
| 处理器负载 | ★★★★★ | CPU功耗建模 |
| 屏幕 | ★★★★★ | 屏幕功耗建模 |
| 网络活动 | ★★★★☆ | 无线功耗建模 |

## 与论文研究方向的关联
- **组件级建模**：与idea.md中的功耗因素分类对应
- **方法论完整**：从建模到验证的完整流程
- **通用框架**：可适应不同设备
- **学术权威性**：米兰理工大学研究成果
