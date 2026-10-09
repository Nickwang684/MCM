# 212. Accurate, Compact, and Power-Efficient Li-Ion Battery Charger Circuit

## 基本信息
- **标题**: Accurate, Compact, and Power-Efficient Li-Ion Battery Charger Circuit
- **作者**: Chen et al.
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2006
- **卷/期**: Vol. 21, No. 4
- **DOI**: 10.1109/TPEL.2006.876891
- **链接**: https://ieeexplore.ieee.org/document/4012370/

## 主要内容

### 研究背景
- 便携设备对高效紧凑充电器的需求
- 传统线性充电器效率低、发热大
- 需要精确的电压/电流控制

### 关键贡献
1. **高效率设计**: 开关型充电器效率达90%以上
2. **精确控制**: 电压精度±1%，电流精度±5%
3. **紧凑集成**: 单芯片PMIC设计

### 充电效率模型
$$\eta_{charger} = \frac{P_{battery}}{P_{input}} = \frac{V_{bat} \cdot I_{charge}}{V_{in} \cdot I_{in}}$$

### CC-CV充电曲线
```
Phase 1 (CC): I = I_max, V increases until V_max
Phase 2 (CV): V = V_max, I decreases until I_cutoff
```

### 对智能手机建模的意义
- 定量分析充电器效率对能量传递的影响
- 充电过程功耗建模的基础参考
- 经典CC-CV充电模型的工程实现

## 关键词
- Li-ion charger, CC-CV, power efficiency, PMIC, portable devices
