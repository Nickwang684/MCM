# Modeling the Total Energy Consumption of Mobile Network Services and Applications

## 基本信息
- **标题**: Modeling the Total Energy Consumption of Mobile Network Services and Applications
- **发表日期**: 2019-01-07
- **期刊**: MDPI Energies
- **链接**: https://www.mdpi.com/1996-1073/12/1/184

## 研究内容
提出端到端移动服务的能耗模型，从终端设备到数据中心的全链路考虑。

## 与考虑因素的相关性

### 智能手机能耗模型
- **E_smartphone模型**: 包含CPU和4G连接功耗积分
- **多组件**: 综合多个能耗源
- **服务相关**: 考虑具体服务的能耗特性

### 网络活动功耗
- **4G连接功耗**: 移动网络能耗建模
- **CPU功耗**: 处理器能耗组件
- **积分方法**: 使用功耗积分计算总能耗

### 应用层能耗
- 特定服务的能耗特性
- 应用程序能耗差异
- 用户使用模式影响

## 核心方法
$$E_{smartphone} = \int P_{CPU} dt + \int P_{4G} dt$$

## 与论文研究方向的关联
- **网络活动**: 直接对应考虑因素
- **功耗积分**: 连续时间建模方法
- **多因素**: 综合CPU和网络影响
