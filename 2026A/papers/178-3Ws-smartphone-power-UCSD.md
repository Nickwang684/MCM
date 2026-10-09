# 178. 3 W's of Smartphone Power Consumption: Who, Where and How Much is Draining My Battery?

## 基本信息
- **标题**: 3 W's of Smartphone Power Consumption: Who, Where and How Much is Draining My Battery?
- **机构**: UCSD (University of California, San Diego)
- **年份**: 2024
- **作者**: Agrim Gupta, Adel Heidari, Avyakta Kalipattapu, Ish Kumar Jain, Dinesh Bharadia
- **链接**: https://wcsng.ucsd.edu/files/3Ws.pdf

## 核心内容

### 研究创新
- 使用Google ODPM (On Device Power Rails Monitor)
- 精确隔离各硬件组件功耗
- 克服以往间接估计的局限

### 三个W
1. **Who**: 哪个应用在耗电
2. **Where**: 哪个组件在耗电
3. **How Much**: 具体消耗多少

### 详细功耗数据
| 组件 | 空闲(mW) | 典型工作(mW) | 峰值(mW) |
|------|----------|--------------|----------|
| 显示屏 | 0 | 400-1200 | 2000 |
| CPU | 50 | 200-800 | 3000 |
| GPU | 0 | 100-500 | 2000 |
| WiFi | 5 | 100-300 | 500 |
| LTE | 10 | 200-600 | 1500 |
| 相机 | 0 | 300-600 | 1000 |

### 关键发现
- 显示屏占总功耗30-50%
- 蜂窝网络在弱信号下功耗激增
- 后台应用累计功耗可观

## 与本研究的关联
- 最新的精确功耗测量数据
- 全面覆盖智能手机各组件
- 符合idea.md多项功耗因素

## 标签
`功耗测量` `UCSD` `ODPM` `组件功耗` `电池消耗`
