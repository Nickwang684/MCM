# 244. IEEE Trans. Industrial Electronics - SOC Estimation Review

## 基本信息
- **标题**: State of Charge Estimation for Lithium-Ion Batteries: A Review of Existing Approaches and Future Developments
- **期刊**: IEEE Transactions on Industrial Electronics
- **年份**: 2022
- **DOI**: 10.1109/TIE.2022.xxxxxx

## 主要内容

### SOC定义
$$SOC = \frac{Q_{remaining}}{Q_{nominal}} \times 100\%$$

### 估计方法分类

#### 1. 直接测量法
| 方法 | 精度 | 复杂度 | 实时性 |
|------|------|--------|--------|
| OCV法 | 高 | 低 | 差 |
| 库仑计数 | 中 | 低 | 好 |
| 阻抗法 | 中 | 高 | 中 |

#### 2. 模型驱动法
$$\hat{SOC}_{k+1} = f(\hat{SOC}_k, I_k) + K(V_k - \hat{V}_k)$$

代表算法：EKF, UKF, PF

#### 3. 数据驱动法
$$SOC = g(V, I, T, dV/dt, ...)$$

代表算法：NN, SVM, LSTM

### EKF算法流程
```
初始化: x̂₀, P₀
预测:   x̂ₖ₋ = f(x̂ₖ₋₁, uₖ₋₁)
        Pₖ₋ = AₖPₖ₋₁Aₖᵀ + Q
更新:   Kₖ = Pₖ₋Hₖᵀ(HₖPₖ₋Hₖᵀ + R)⁻¹
        x̂ₖ = x̂ₖ₋ + Kₖ(zₖ - h(x̂ₖ₋))
        Pₖ = (I - KₖHₖ)Pₖ₋
```

### 精度对比

| 方法 | MAE | RMSE | 计算量 |
|------|-----|------|--------|
| 库仑计数 | 3-5% | 4-6% | 低 |
| EKF | 1-2% | 1.5-2.5% | 中 |
| LSTM | 0.5-1% | 0.8-1.5% | 高 |

### 对智能手机建模的意义
- SOC估计方法的全面对比
- 手机BMS常用方法分析
- 精度与计算量的权衡

## 关键词
- SOC estimation, EKF, UKF, neural network, lithium-ion battery
