# 243. Electrochimica Acta - Lithium Plating Detection and Prevention

## 基本信息
- **标题**: Lithium Plating in Lithium-Ion Batteries: Detection, Prevention and Modeling
- **期刊**: Electrochimica Acta
- **年份**: 2021
- **DOI**: 10.1016/j.electacta.2021.xxxxx

## 主要内容

### 锂析出机理
当负极电位低于Li/Li+参考电位时发生：
$$\phi_{anode} - \phi_{electrolyte} < 0 \text{ V vs Li/Li}^+$$

### 析出条件

| 因素 | 促进析出 | 抑制析出 |
|------|----------|----------|
| 温度 | <10°C | >25°C |
| 充电倍率 | >1C | <0.5C |
| SOC | >80% | <70% |
| 老化程度 | 老化电池 | 新电池 |

### 析出动力学模型
$$i_{Li} = i_0 \cdot \left[\exp\left(\frac{\alpha_a F \eta}{RT}\right) - \exp\left(-\frac{\alpha_c F \eta}{RT}\right)\right]$$

其中过电位：
$$\eta = \phi_s - \phi_e - U_{eq,Li} < 0 \text{ (析出条件)}$$

### 检测方法
1. **电压曲线分析**: 充电后静置电压回升
2. **dQ/dV分析**: 析出峰识别
3. **EIS**: 高频阻抗异常
4. **厚度测量**: 电极膨胀

### 预防策略
- 低温充电限流
- 阶梯式充电协议
- 实时电位监控

### 对智能手机建模的意义
- 快充边界条件的确定
- 低温使用的安全限制
- 充电策略对寿命的影响

## 关键词
- Lithium plating, low temperature, fast charging, anode potential, safety
