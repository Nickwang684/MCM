# 151. Modeling Energy Consumption of Data Transmission over Wi-Fi

## 基本信息
- **标题**: Modeling Energy Consumption of Data Transmission over Wi-Fi
- **作者**: Yu Xiao, Yong Cui, Petri Savolainen, Matti Siekkinen, An Wang, Liu Yang, Antti Ylä-Jääski, Sasu Tarkoma
- **期刊**: IEEE Transactions on Mobile Computing (TMC)
- **年份**: 2013
- **链接**: https://users.aalto.fi/~siekkine/pub/xiao13tmc.pdf
- **期刊级别**: CCF-A类期刊

## 研究内容摘要
本文研究了WiFi数据传输的能耗特性，特别关注互联网流特性和网络环境的影响。提出了确定性模型，描述了WiFi数据传输能耗与流量突发性、吞吐量、重传率和省电机制参数的关系。

## 关键发现
1. **能耗影响因素**：
   - 流量突发性
   - 网络吞吐量
   - 重传率
   - 省电机制(PSM)参数
2. **突发性影响**：突发性传输比连续传输更节能
3. **PSM优化**：合理配置PSM可节能30-50%
4. **实用性**：模型输入在移动平台易获取

## 能耗模型
$$E = E_{active} + E_{idle} + E_{tail}$$

$$E_{active} = \frac{Data}{Throughput} \cdot P_{active}$$

$$E_{tail} = T_{tail} \cdot P_{tail}$$

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 网络活动 | ★★★★★ | 核心研究主题 |
| 功耗 | ★★★★★ | 详细能耗建模 |
| 应用 | ★★★★☆ | 流量模式影响 |

## 与论文研究方向的关联
- **IEEE TMC顶刊**：移动计算领域最高级别期刊
- **实用模型**：参数在手机上可直接获取
- **省电策略**：为电池续航优化提供理论依据
- **多因素考虑**：综合考虑网络和设备因素
