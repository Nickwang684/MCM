# 169. Reducing the Power Consumption of an IMU-Based Gait Measurement System

## 基本信息
- **标题**: Reducing the Power Consumption of an IMU-Based Gait Measurement System
- **期刊/会议**: PCM (Pacific-Rim Conference on Multimedia) - LNCS 7674
- **年份**: 2012
- **作者**: Shenggao Zhu, Hugh Anderson, Ye Wang
- **机构**: National University of Singapore
- **链接**: https://smcnus.comp.nus.edu.sg/archive/pdf/2012-2013/2012_Power_PCM2012.pdf

## 核心内容

### 系统描述
- 足部安装的步态测量系统(GMS)
- 基于惯性测量单元(IMU): 加速度计+陀螺仪
- 用于步态分析和辅助系统

### 功耗优化策略
1. **自适应采样率**: 根据活动状态调整
2. **零速度检测(ZUPT)**: 静止时降低采样
3. **数据压缩**: 减少存储和传输能耗
4. **处理器休眠**: 优化MCU占空比

### 功耗数据
| 组件 | 功耗 |
|------|------|
| 加速度计 (ADXL345) | 23-140µA |
| 陀螺仪 (ITG-3200) | 6.5mA |
| MCU (MSP430) | 0.1-330µA |
| 总系统 | ~10-20mW |

### 优化效果
- 功耗降低40-60%
- 电池寿命从8小时延长到20小时
- 精度损失<5%

## 与本研究的关联
- IMU功耗的详细分解
- 可穿戴设备功耗优化策略
- 加速度计/陀螺仪功耗参考数据

## 标签
`IMU` `惯性传感器` `功耗优化` `步态分析` `可穿戴`
