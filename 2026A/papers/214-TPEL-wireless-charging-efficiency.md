# 214. A Constant-Power and Optimal-Transfer-Efficiency Wireless Inductive Power Transfer Converter for Battery Charger

## 基本信息
- **标题**: A Constant-Power and Optimal-Transfer-Efficiency Wireless Inductive Power Transfer Converter for Battery Charger
- **作者**: Liu et al.
- **期刊**: IEEE Transactions on Power Electronics
- **年份**: 2023
- **卷/期**: Vol. 38, No. 5
- **DOI**: 10.1109/TPEL.2023.3241568
- **链接**: https://ieeexplore.ieee.org/document/10038747/

## 主要内容

### 研究背景
- 无线充电在智能手机中日益普及
- 传统WPT系统效率随负载变化波动大
- 需要恒功率输出和高效率的平衡

### 关键贡献
1. **恒功率控制**: 实现宽负载范围内恒功率输出
2. **效率优化**: 最大效率可达92%
3. **自适应调节**: 根据电池SOC自动调整功率

### 无线充电效率模型
$$\eta_{WPT} = \eta_{TX} \cdot \eta_{coupling} \cdot \eta_{RX}$$

其中：
$$\eta_{coupling} = \frac{k^2 Q_1 Q_2}{1 + k^2 Q_1 Q_2}$$

- $k$ = 耦合系数
- $Q_1, Q_2$ = 发射/接收线圈品质因数

### 对智能手机建模的意义
- 无线充电过程的能量损耗建模
- 充电方式（有线vs无线）对效率的影响
- 可用于对比不同充电方式的能耗

## 关键词
- Wireless charging, WPT, efficiency optimization, constant power, Qi
