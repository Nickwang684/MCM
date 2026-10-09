# Accurate Power Modeling of Modern Mobile Application Processors

## 基本信息
- **标题**: Accurate power modeling of modern mobile application processors
- **作者**: Chanmin Yoon, Seokjun Lee, Yonghun Choi, Rhan Ha, Hojung Cha
- **期刊**: Journal of Systems Architecture
- **年份**: 2017
- **卷号**: Volume 81, Pages 17-31
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S1383762117301947

## 研究内容
针对现代移动应用处理器(AP)的功率建模挑战，提出准确的功率模型构建方法。

## 核心方法
- **组件级建模**: 分离CPU、GPU、内存等组件功耗
- **DVFS考虑**: 不同频率电压下的功耗特性
- **负载特征**: 根据工作负载类型建模
- **验证方法**: 与实测功率对比

## 移动AP功率模型

### CPU功耗模型
P_cpu = f(频率, 电压, 利用率, 温度)
- 动态功耗: P_dyn ∝ C·V²·f
- 静态功耗: P_static ∝ V·T·exp(-Ea/kT)

### GPU功耗模型
- 图形负载依赖
- 渲染复杂度影响
- DVFS效应

## 与考虑因素的相关性

### 功耗因素
- **处理器负载**: CPU/GPU利用率对功耗的影响
- **DVFS**: 频率电压调节的节能效果

### 连续时间建模
- 功率随时间变化的动态特性
- 瞬态功耗与平均功耗

## 关键发现
1. 现代AP功耗建模需考虑多核异构架构
2. GPU功耗可能超过CPU
3. 温度对静态功耗影响显著

## 与论文研究方向的关联
处理器功耗模型是智能手机电池续航建模的关键组成部分。
