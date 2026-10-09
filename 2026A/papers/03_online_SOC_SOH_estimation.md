# An Online SOC and SOH Estimation Model for Lithium-Ion Batteries

## 基本信息
- **标题**: An Online SOC and SOH Estimation Model for Lithium-Ion Batteries
- **发表日期**: 2017-04-10
- **期刊**: MDPI Energies
- **链接**: https://www.mdpi.com/1996-1073/10/4/512

## 研究内容
开发了一种可靠、准确的锂离子电池SOC和SOH在线同时估计模型。

## 与考虑因素的相关性

### SOC与SOH联合估计
- **瞬时放电电压V**: 作为关键输入
- **单位时间电压降V'**: 新参数，反映电池状态
- **线性关系假设**: SOC方程假设为线性关系

### 电池老化(SOH)
- 同时考虑电池健康状态
- 追踪电池容量衰减
- 考虑使用历史对电池的影响

### 实时估计
- 在线算法，适合移动设备
- 低计算复杂度
- 可部署于智能手机BMS

## 核心方法
1. 建立V和V'与SOC/SOH的关系
2. 开发在线参数识别算法
3. 验证模型准确性

## 与论文研究方向的关联
- **双重估计**: 同时考虑SOC（剩余电量）和SOH（电池老化）
- **使用历史**: 与题目中"使用历史"因素直接相关
- **实时预测**: 满足智能手机实时显示需求
