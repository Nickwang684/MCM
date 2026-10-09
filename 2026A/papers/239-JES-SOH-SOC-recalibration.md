# 239. SOH Estimation and SOC Recalibration of Lithium-Ion Battery

## 基本信息
- **标题**: SOH Estimation and SOC Recalibration of Lithium-Ion Battery with Incremental Capacity Analysis & OCV-SOC Curve
- **期刊**: Journal of The Electrochemical Society
- **年份**: 2020
- **DOI**: 10.1149/1945-7111/ab8f56
- **链接**: https://iopscience.iop.org/article/10.1149/1945-7111/ab8f56

## 主要内容

### 研究背景
- SOH衰减导致SOC估计误差累积
- 需要基于SOH更新OCV-SOC曲线
- ICA可同时用于SOH估计和SOC校准

### OCV-SOC曲线随老化变化

#### 新电池OCV-SOC
$$OCV_{new}(SOC) = f_{new}(SOC)$$

#### 老化电池OCV-SOC
$$OCV_{aged}(SOC) = f_{aged}(SOC) \neq f_{new}(SOC)$$

主要变化：
- 低SOC区域OCV下降更快
- 高SOC区域OCV略有降低
- 平台区域缩短

### ICA峰值追踪
$$SOH = \alpha \cdot \frac{A_{peak,aged}}{A_{peak,new}} + \beta$$

峰值面积与容量线性相关

### SOC校准方法

#### 基于OCV校准
$$SOC_{corrected} = g^{-1}_{aged}(OCV_{measured})$$

#### 基于容量校准
$$SOC = \frac{Q_{accumulated}}{C_{current}} = \frac{Q_{accumulated}}{C_{nominal} \cdot SOH}$$

### 自适应OCV曲线更新
$$OCV_{updated}(SOC) = OCV_{new}(SOC) \cdot (1 + \delta \cdot (1-SOH))$$

### 对智能手机建模的意义
- OCV-SOC曲线随老化的变化模型
- SOC估计误差的校准方法
- 手机"电量突降"现象的解释

## 关键词
- SOH, SOC recalibration, ICA, OCV-SOC curve, aging
