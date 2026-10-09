# A Survey on Energy Estimation and Power Modeling Schemes for Smartphone Applications

## 基本信息
- **标题**: A survey on energy estimation and power modeling schemes for smartphone applications
- **作者**: Raja Wasim Ahmad, Abdullah Gani, Siti Hafizah Ab Hamid, Mohammad Shojafar 等
- **期刊**: International Journal of Communication Systems
- **年份**: 2017
- **链接**: https://onlinelibrary.wiley.com/doi/10.1002/dac.3234

## 研究内容
全面综述智能手机应用的能量估计和功率建模方案。

## 功率建模方法分类

### 基于测量的方法
- **外部功率计**: 使用Monsoon等设备直接测量
- **电池API**: 读取电池电流/电压信息
- **优点**: 准确
- **缺点**: 需要特殊硬件或root权限

### 基于模型的方法
- **组件模型**: 各硬件组件的功耗模型
- **使用模式模型**: 基于使用行为的估计
- **机器学习**: 数据驱动的功耗预测
- **优点**: 无需特殊硬件
- **缺点**: 需要校准，准确性依赖模型质量

## 典型功率模型结构
P_total = P_display + P_cpu + P_gpu + P_wifi + P_cellular + P_sensors + P_audio + P_misc

## 与考虑因素的相关性

### 功耗因素
- **综合功耗模型**: 涵盖所有主要组件
- **应用级归因**: 将功耗归因到具体应用

### 方法论
- **建模方法综述**: 不同方法的优缺点
- **验证策略**: 模型准确性评估

## 与论文研究方向的关联
该综述为智能手机功耗建模提供了方法论指导和现有工作的全面回顾。
