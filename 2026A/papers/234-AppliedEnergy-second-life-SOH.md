# 234. State of Health Estimation Methods for Second Life Lithium-Ion Battery

## 基本信息
- **标题**: State of Health (SoH) Estimation Methods for Second Life Lithium-Ion Battery—Review and Challenges
- **作者**: Vignesh S et al.
- **期刊**: Applied Energy
- **年份**: 2024
- **卷**: Volume 369
- **DOI**: 10.1016/j.apenergy.2024.123542
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S0306261924009255

## 主要内容

### 研究背景
- 电池退役后可用于储能等二次应用
- 二次利用需要准确的SOH评估
- 老化历史未知带来额外挑战

### 二次利用SOH标准

| 应用场景 | SOH要求 | 功率要求 |
|----------|---------|----------|
| 电动汽车 | >80% | 高 |
| 储能系统 | 60-80% | 中 |
| 备用电源 | 50-60% | 低 |

### 快速SOH评估方法

#### 1. 脉冲测试法
$$R_{DC} = \frac{\Delta V}{\Delta I}$$

测试时间：秒级

#### 2. EIS法
$$Z(\omega) = R_s + \frac{R_{ct}}{1 + j\omega R_{ct}C_{dl}} + Z_W$$

测试时间：分钟级

#### 3. 容量测试法
$$C = \int_0^{t_{end}} I(t) \, dt$$

测试时间：小时级

### 挑战与解决方案
1. **历史未知**: 基于当前状态的评估
2. **一致性差**: 分选分级技术
3. **安全风险**: 严格的测试协议

### 对智能手机建模的意义
- 老化电池的特性评估
- 旧手机电池性能预测
- 电池回收与再利用考量

## 关键词
- Second life battery, SOH, rapid assessment, retired battery, reuse
