# 242. Electrochimica Acta - EIS for Battery State Estimation

## 基本信息
- **标题**: Electrochemical Impedance Spectroscopy for Battery State Estimation: A Comprehensive Review
- **期刊**: Electrochimica Acta
- **年份**: 2023
- **类型**: 综述论文

## 主要内容

### EIS基本原理
施加小幅交流扰动，测量阻抗响应：
$$Z(\omega) = \frac{V(\omega)}{I(\omega)} = Z'(\omega) + jZ''(\omega)$$

### 等效电路模型

#### Randles电路
```
    Rs      Rct
○──/\/\/──┬──/\/\/──○
          │
         ═╪═ Cdl
          │
         ─┴─ Warburg
```

$$Z = R_s + \frac{R_{ct}}{1 + j\omega R_{ct}C_{dl}} + \frac{A_W}{\sqrt{\omega}}(1-j)$$

### EIS与电池状态关系

| 频率范围 | 物理过程 | 状态关联 |
|----------|----------|----------|
| >10 kHz | 电感效应 | 连接/焊点 |
| 1-10 kHz | 欧姆电阻Rs | SOH, 温度 |
| 10-1000 Hz | SEI阻抗 | SOH, 老化 |
| 0.1-10 Hz | 电荷转移Rct | SOC, 温度 |
| <0.1 Hz | 扩散Warburg | SOC, 浓度 |

### SOC-EIS关系
$$R_{ct} = R_{ct,0} \cdot f(SOC) \cdot g(T)$$

### SOH-EIS关系
$$SOH \propto \frac{1}{R_s + R_{SEI}}$$

### 对智能手机建模的意义
- EIS可用于在线SOC/SOH估计
- 不同频率对应不同物理过程
- 阻抗变化反映电池老化

## 关键词
- EIS, impedance spectroscopy, equivalent circuit, SOC, SOH, Randles
