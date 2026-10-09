# 164. Energy-Efficient Rate-Adaptive GPS-based Positioning for Smartphones

## 基本信息
- **标题**: Energy-Efficient Rate-Adaptive GPS-based Positioning for Smartphones
- **期刊/会议**: ACM MobiSys 2010
- **年份**: 2010
- **作者**: Jeongyeup Paek, Joongheon Kim, Ramesh Govindan
- **DOI**: 10.1145/1814433.1814463

## 核心内容

### 问题陈述
- GPS是首选定位技术（精度高）
- GPS极度耗电，常见做法是周期性duty-cycling
- Duty-cycling牺牲定位精度换取低能耗

### 创新方法
1. **速率自适应采样**: 根据用户移动速度动态调整GPS采样率
2. **预测辅助**: 利用加速度计预测位置，减少GPS唤醒
3. **能耗模型**: 建立采样率与能耗的定量关系

### 技术细节
- 高速移动: 增加采样率保证精度
- 静止或低速: 降低采样率节能
- 加速度计辅助推算: 低功耗填补GPS采样间隙

### 性能结果
- 能耗降低50-70%
- 精度损失<5米
- 适用于导航和位置跟踪应用

## 与本研究的关联
- 提供GPS占空比策略的能耗模型
- 移动模式与功耗关系（idea.md中的使用习惯）
- 多传感器融合策略参考

## 标签
`GPS` `自适应采样` `MobiSys` `能效` `定位`
