# 189. Predicting Power Usage of Android Applications

## 基本信息
- **标题**: Predicting Power Usage of Android Applications
- **机构**: University of Wisconsin-Madison
- **年份**: 2014
- **作者**: Benjamin Bramble, Michael Swift
- **文档**: Technical Report TR1808
- **链接**: https://pages.cs.wisc.edu/~swift/papers/TR1808.pdf

## 核心内容

### 系统名称: SApp

### 目标
- 教育用户了解应用对电池的影响
- 通过智能决策减少电池消耗
- 预测未来应用对电池的影响

### 三步流程
1. **组件影响测试**: 测量各设备组件的功耗
2. **应用性能测量**: 测量应用的资源消耗
3. **启发式预测**: 结合测量和启发式预测未来影响

### 技术方法
| 步骤 | 方法 | 输出 |
|------|------|------|
| 组件建模 | 微基准测试 | 功耗曲线 |
| 应用分析 | 运行时监控 | 资源使用 |
| 预测 | 机器学习+启发式 | 电池影响 |

### 应用场景
- 帮助用户识别耗电应用
- 指导应用优先级设置
- 电池寿命延长建议

## 与本研究的关联
- 用户视角的功耗预测
- 组件+应用的综合方法
- 预测模型设计参考

## 标签
`Android` `功耗预测` `用户教育` `应用分析` `Wisconsin`
