# 194. Real-Time State of Charge-Open Circuit Voltage Curve Construction for Battery State of Charge Estimation

## 基本信息
- **标题**: Real-Time State of Charge-Open Circuit Voltage Curve Construction for Battery State of Charge Estimation
- **期刊**: IEEE Transactions on Vehicular Technology
- **年份**: 2023
- **作者**: Onur Kadem, Jongrae Kim
- **机构**: University of Leeds
- **链接**: https://eprints.whiterose.ac.uk/id/eprint/196412/

## 核心内容

### 研究动机
- 传统SOC估计依赖离线测量的OCV-SOC曲线
- 电池老化导致曲线变化
- 需要实时更新能力

### 方法创新
1. **在线OCV识别**: 运行时识别OCV
2. **自适应曲线更新**: 实时调整OCV-SOC关系
3. **老化补偿**: 适应电池老化变化

### 技术实现
- 等效电路模型参数识别
- 递归估计算法
- 实时计算效率优化

### 验证结果
- SOC估计误差<2%
- 适应不同老化程度
- 实时运行可行

## 与本研究的关联
- 实时OCV-SOC更新方法
- 考虑老化影响
- 支持连续时间SOC估计

## 标签
`实时SOC` `OCV曲线` `在线估计` `老化补偿` `IEEE TVT`
