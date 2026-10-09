# 186. Analyzing and Classifying Energy Consumption in Android Applications

## 基本信息
- **标题**: Analyzing and Classifying Energy Consumption in Android Applications
- **机构**: Universidade do Minho / HASLab / INESC TEC
- **年份**: 2016
- **作者**: Marco Couto, Jácome Cunha, João Paulo Fernandes, Rui Pereira, João Saraiva
- **链接**: https://greenlab.di.uminho.pt/wp-content/uploads/2016/06/paper.pdf

## 核心内容

### 研究背景
- 从运行时间优化转向能耗优化
- 需要检测异常能耗的技术和工具
- 程序员缺乏能耗优化意识

### 分析方法
1. **能耗分类**: 按应用类型分类能耗模式
2. **异常检测**: 识别异常能耗行为
3. **代码分析**: 关联代码模式与能耗

### 应用类型能耗分析
| 类型 | 平均功耗 | 特点 |
|------|----------|------|
| 游戏 | 高 | GPU密集 |
| 社交 | 中高 | 网络密集 |
| 工具 | 低 | 间歇使用 |
| 媒体 | 高 | 屏幕+解码 |

### 主要发现
- 异常能耗通常与代码缺陷相关
- 后台活动是隐藏能耗源
- 广告SDK能耗可观

## 与本研究的关联
- 应用能耗分类方法
- 异常检测技术
- 支持idea.md中"应用"因素

## 标签
`能耗分类` `Android` `异常检测` `绿色计算` `代码分析`
