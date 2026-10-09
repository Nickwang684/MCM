# 198. Sudden Drop in the Battery Level? Understanding Smartphone State of Charge Anomaly

## 基本信息
- **标题**: Sudden Drop in the Battery Level? Understanding Smartphone State of Charge Anomaly
- **期刊/会议**: HotPower 2015 (ACM Workshop)
- **年份**: 2015
- **作者**: Mohammad A. Hoque, Sasu Tarkoma
- **机构**: University of Helsinki
- **链接**: https://engineering.purdue.edu/~hotpower/HotPower_2015_paper_1.pdf

## 核心内容

### 研究问题
- 智能手机电量突然大幅下降现象
- SOC估计不准确的原因
- 电池老化对SOC估计的影响

### 主要发现
1. **电压曲线与容量**: 电压曲线隐含电池可用容量信息
2. **SOC估计缺陷**: 当前技术未充分考虑容量损失
3. **老化影响**: 老化电池更容易出现异常

### SOC异常原因
- 电池老化导致容量衰减
- SOC算法基于初始容量
- 实际可用容量低于预期

### 改进建议
- 动态更新容量估计
- 考虑老化因素
- 校准电压-SOC映射

## 与本研究的关联
- 智能手机SOC估计的实际问题
- 电池老化对SOC的影响
- 符合idea.md中"使用历史"和"电池老化"考虑

## 标签
`SOC异常` `智能手机` `电池老化` `电量突降` `HotPower`
