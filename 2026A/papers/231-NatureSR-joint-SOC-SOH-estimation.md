# 231. Joint Estimation of SOC and SOH for Lithium-Ion Batteries

## 基本信息
- **标题**: Joint Estimation of SOC and SOH for Lithium-Ion Batteries Based on Adaptive Extended Kalman Filter
- **作者**: Yan et al.
- **期刊**: Nature Scientific Reports
- **年份**: 2025
- **DOI**: 10.1038/s41598-025-24571-x
- **链接**: https://www.nature.com/articles/s41598-025-24571-x

## 主要内容

### 研究背景
- SOC和SOH的联合估计对BMS至关重要
- 传统方法分别估计，忽略耦合关系
- 需要自适应算法应对老化变化

### 联合估计框架

#### 状态空间模型
$$x_k = \begin{bmatrix} SOC_k \\ SOH_k \\ R_{int,k} \end{bmatrix}$$

状态转移方程：
$$x_{k+1} = f(x_k, I_k) + w_k$$

观测方程：
$$V_k = OCV(SOC_k, SOH_k) - I_k \cdot R_{int,k} + v_k$$

### 自适应EKF算法
1. **预测步骤**:
   $$\hat{x}_{k|k-1} = f(\hat{x}_{k-1}, I_{k-1})$$
   $$P_{k|k-1} = F_k P_{k-1} F_k^T + Q_k$$

2. **更新步骤**:
   $$K_k = P_{k|k-1} H_k^T (H_k P_{k|k-1} H_k^T + R_k)^{-1}$$
   $$\hat{x}_k = \hat{x}_{k|k-1} + K_k (V_k - h(\hat{x}_{k|k-1}))$$

### 自适应机制
- 噪声协方差在线调整
- 遗忘因子适应老化
- 多时间尺度更新

### 对智能手机建模的意义
- SOC/SOH联合估计的数学框架
- 适用于实时BMS的算法
- 考虑电池老化的状态估计

## 关键词
- SOC, SOH, joint estimation, adaptive EKF, lithium-ion battery
