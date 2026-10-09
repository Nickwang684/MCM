# 179. Android Power Profile: Measure Power Values

## 基本信息
- **标题**: Measure Power Values (Android Power Profile)
- **来源**: Android Open Source Project (AOSP)
- **类型**: 官方技术文档
- **链接**: https://source.android.com/docs/core/power/values

## 核心内容

### 文档目的
- 指导设备制造商测量各组件功耗
- 定义power_profile.xml格式
- 标准化Android功耗估算

### 需测量的组件
1. **CPU**: 各频率点功耗
2. **屏幕**: 亮度级别功耗
3. **WiFi**: 扫描、传输、接收功耗
4. **蓝牙**: 扫描、传输功耗
5. **GPS**: 持续定位功耗
6. **相机**: 闪光灯功耗
7. **音频**: 扬声器功耗
8. **无线电**: 各状态功耗

### 测量方法
- 精确电流表（μA精度）
- 控制变量测试
- 多次测量取平均

### 典型数值范例
```xml
<item name="screen.on">200</item>  <!-- mA -->
<item name="screen.full">400</item>
<item name="wifi.on">2</item>
<item name="wifi.active">200</item>
<item name="gps.on">50</item>
<item name="camera.avg">500</item>
<item name="audio">15</item>
```

## 与本研究的关联
- Android官方功耗参考标准
- 覆盖所有主要硬件组件
- 直接支持功耗建模

## 标签
`Android` `功耗配置` `官方文档` `AOSP` `power_profile`
