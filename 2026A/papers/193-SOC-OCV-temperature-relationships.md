# 193. A Novel Method for Constructing the Relationships between State of Charge and Open-Circuit Voltage under Different Temperatures

## 基本信息
- **标题**: A Novel Method for Constructing the Relationships between State of Charge and Open-Circuit Voltage of Lithium-Ion Battery under Different Temperatures with Reduced Test Time
- **期刊**: Journal of Cleaner Production (Elsevier)
- **年份**: 2023
- **作者**: C. Chen et al.
- **DOI**: 10.1016/j.jclepro.2023.139554
- **链接**: https://www.sciencedirect.com/science/article/abs/pii/S0959652623037125

## 核心内容

### 研究创新
- 快速构建温度相关的SOC-OCV关系
- 显著减少测试时间
- 保持高精度

### 传统方法问题
- 需要长时间静置测量OCV
- 每个温度点需要完整测试
- 测试成本高昂

### 新方法
1. **参考温度测试**: 完整测试一个温度点
2. **温度系数提取**: 快速测量温度依赖性
3. **模型推导**: 构建任意温度的OCV-SOC曲线

### 温度依赖性
```
V_OCV(SOC, T) = V_OCV(SOC, T_ref) + α(SOC)·(T - T_ref)
```
其中α(SOC)是温度系数

### 精度验证
- 误差<10mV（-20°C到45°C）
- 测试时间减少70%

## 与本研究的关联
- 温度对OCV-SOC关系的影响
- 支持idea.md中"温度变化"因素
- 实用的快速测试方法

## 标签
`OCV-SOC` `温度依赖` `快速测试` `锂离子电池` `建模`
