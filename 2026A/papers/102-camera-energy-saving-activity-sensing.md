# A Context Aware Energy-Saving Scheme for Smart Camera Phones

## 基本信息
- **标题**: A Context Aware Energy-Saving Scheme for Smart Camera Phones based on Activity Sensing
- **作者**: Yuanyuan Fan, Lei Xie, Yafeng Yin, Sanglu Lu
- **机构**: Nanjing University
- **会议**: IEEE MASS 2015
- **链接**: https://cs.nju.edu.cn/yafeng/YinPaper/MASS2015Fan.pdf

## 研究内容
针对智能手机拍照功能的高功耗问题，提出基于活动感知的上下文感知节能方案。

## 核心问题
- 智能手机拍照是高功耗功能
- 相机模块功耗: 300-500mW
- 图像处理增加CPU负载
- 预览模式持续消耗电量

## 节能方法
- **活动感知**: 检测用户拍照意图
- **预测性管理**: 提前预测拍照行为
- **自适应控制**: 根据情境调整相机功耗状态
- **传感器融合**: 利用加速度计等低功耗传感器

## 相机功耗分解
| 状态 | 功耗 |
|------|------|
| 相机关闭 | 0mW |
| 预览模式 | 300-400mW |
| 拍照/录像 | 400-600mW |
| 图像处理 | 额外100-200mW |

## 与考虑因素的相关性

### 功耗因素
- **相机功耗**: 移动摄影的能耗特性
- **CPU负载**: 图像处理的计算需求

### 使用习惯
- **拍照行为**: 用户拍照模式的建模
- **情境感知**: 环境和活动的影响

## 与论文研究方向的关联
相机使用是智能手机电池消耗的重要场景，理解其功耗特性对续航预测有帮助。
