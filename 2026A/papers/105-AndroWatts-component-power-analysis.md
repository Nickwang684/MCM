# AndroWatts: Unpacking the Power Consumption of Mobile Device's Components

## 基本信息
- **标题**: AndroWatts: Unpacking the Power Consumption of Mobile Device's Components
- **作者**: Édouard Guégain, Rémy Raes, Noé Chachignot, Clément Quinton, Romain Rouvoy
- **年份**: 2025
- **链接**: https://hal.science/hal-04928609v1/document

## 研究内容
提出AndroWatts工具，解析移动设备各组件的功耗贡献，提供细粒度的功耗分析能力。

## 工具特点
- **组件级分解**: 分离各硬件组件功耗
- **软件级归因**: 将功耗归因到应用和进程
- **实时监测**: 动态功耗追踪
- **开源可用**: 研究和开发可用

## 组件功耗分解

### 主要组件
1. **显示屏**: 最大功耗来源
2. **蜂窝网络**: 高功耗且波动大
3. **Wi-Fi**: 相对较低但活跃
4. **CPU**: 负载依赖
5. **GPU**: 图形任务时显著
6. **存储**: 读写操作

### 次要组件
- 传感器（加速度计、陀螺仪等）
- 音频输出
- 振动马达
- GPS

## 与考虑因素的相关性

### 功耗因素
- **所有硬件组件**: 全面的组件功耗分解
- **软件层面**: 应用对功耗的影响

### 连续时间建模
- 实时功耗追踪支持动态建模
- 时序功耗数据采集

## 与论文研究方向的关联
AndroWatts类工具可用于获取智能手机功耗的实测数据，验证和校准功耗模型。
