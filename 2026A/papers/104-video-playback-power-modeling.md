# Modeling Video Playback Power Consumption on Mobile Devices

## 基本信息
- **标题**: Modeling Video Playback Power Consumption on Mobile Devices
- **作者**: Bekir Turkkan, Adithya Raman, Tevfik Kosar
- **机构**: IBM Research, University at Buffalo
- **年份**: 2025
- **链接**: https://par.nsf.gov/servlets/purl/10563541

## 研究内容
提出移动设备视频播放功耗的新型建模方法，考虑最新视频技术和硬件特性。

## 核心发现
移动硬件和流媒体技术的进步使高质量视频流成为可能，但代价是功耗增加。

## 功耗影响因素

### 视频参数
- **分辨率**: 720p vs 1080p vs 4K
- **帧率**: 30fps vs 60fps
- **编解码器**: H.264 vs H.265 vs VP9 vs AV1
- **比特率**: 影响解码复杂度

### 硬件组件
- **显示屏**: 渲染功耗
- **解码器**: 硬解码 vs 软解码
- **网络**: 流媒体带宽需求

## 功耗模型
P_video = P_display + P_decode + P_network + P_audio

## 与考虑因素的相关性

### 功耗因素
- **屏幕功耗**: 视频播放时的显示能耗
- **处理器负载**: 视频解码的计算需求
- **网络活动**: 流媒体的网络功耗

### 使用习惯
- **视频观看时间**: 典型使用场景的主要活动
- **内容质量选择**: 用户偏好对功耗的影响

## 与论文研究方向的关联
视频播放是智能手机的主要使用场景之一，理解其功耗特性对续航建模至关重要。
