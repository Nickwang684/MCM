# 172. Modeling Video Playback Power Consumption on Mobile Devices

## 基本信息
- **标题**: Modeling Video Playback Power Consumption on Mobile Devices
- **期刊/会议**: ACM MMSys 2024
- **年份**: 2024
- **作者**: Bekir Turkkan (IBM Research), Adithya Raman, Tevfik Kosar (University at Buffalo)
- **链接**: https://par.nsf.gov/servlets/purl/10563541

## 核心内容

### 研究动机
- 视频流媒体是主流移动应用
- 现有功耗模型未考虑新技术（HDR, HEVC, AV1）
- 需要更准确的视频播放功耗预测

### 建模方法
1. **分层功耗模型**: 解码器 + 渲染 + 显示
2. **参数化模型**: 分辨率、帧率、编解码器、HDR
3. **机器学习增强**: 非线性关系建模

### 关键影响因素
| 因素 | 功耗影响 |
|------|----------|
| 分辨率 (1080p→4K) | +40-60% |
| 帧率 (30→60fps) | +20-30% |
| HDR | +15-25% |
| 硬件解码vs软件解码 | 硬件节省50-70% |

### 模型精度
- 预测误差 <8%
- 涵盖多种设备和视频格式
- 实时功耗估计可行

## 与本研究的关联
- 视频播放的详细功耗建模
- 参数化方法可借鉴
- 支持idea.md中"应用"因素

## 标签
`视频播放` `功耗建模` `MMSys` `IBM Research` `流媒体`
