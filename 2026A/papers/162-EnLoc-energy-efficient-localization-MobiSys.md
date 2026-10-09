# 162. EnLoc: Energy-Efficient Localization for Mobile Phones

## 基本信息
- **标题**: EnLoc: Energy-Efficient Localization for Mobile Phones
- **期刊/会议**: IEEE/ACM International Conference on Mobile Systems (MobiSys)
- **年份**: 2010
- **作者**: Ionut Constandache, Shravan Gaonkar, Matt Sayler, Romit Roy Choudhury, Landon Cox
- **链接**: https://synrg.csl.illinois.edu/papers/enloc5.pdf

## 核心内容

### 研究背景
- GPS提供高精度定位但能耗极高（电池寿命<9小时）
- WiFi/GSM定位节能但精度较低
- 需要在能耗和精度之间找到平衡

### 主要贡献
1. **能耗-精度权衡量化**: 首次系统量化不同定位技术的能耗-精度权衡
2. **EnLoc系统**: 智能切换定位技术的自适应框架
3. **替代方案评估**: GSM、WiFi、GPS混合定位策略

### 关键数据
- GPS平均功耗: ~150mW（持续运行）
- WiFi定位功耗: ~30-50mW
- GSM定位功耗: ~10-20mW
- 精度vs能耗非线性关系

### 技术方法
- 基于移动模式预测选择定位方式
- 上下文感知的自适应切换
- 能耗预算约束下的定位策略

## 与本研究的关联
- 提供多种定位技术的功耗对比数据
- 支持location-based应用的能耗建模
- 可用于优化策略的参考

## 标签
`定位` `能效` `GPS` `WiFi定位` `MobiSys`
