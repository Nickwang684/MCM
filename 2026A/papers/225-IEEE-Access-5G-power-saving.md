# 225. Power Saving Techniques for 5G and Beyond

## 基本信息
- **标题**: Power Saving Techniques for 5G and Beyond
- **作者**: Yu-Ngok Ruyue Li, Mengzhu Chen, Jun Xu, Li Tian, Kaibin Huang
- **期刊**: IEEE Access
- **年份**: 2020
- **DOI**: 10.1109/ACCESS.2020.3001180
- **链接**: https://ieeexplore.ieee.org/document/9112193

## 主要内容

### 研究背景
- 5G NR支持eMBB、mMTC、URLLC多场景
- 终端设备功耗成为关键挑战
- 标准化的节能技术不断演进

### 5G节能技术分类

#### 1. DRX (非连续接收)
```
On-duration: 终端监听PDCCH
Sleep period: 终端休眠节能
```
$$E_{DRX} = P_{on} \cdot T_{on} + P_{sleep} \cdot T_{sleep}$$

#### 2. BWP (带宽部分适配)
| BWP宽度 | 功耗 | 适用场景 |
|---------|------|----------|
| 20 MHz | 低 | 低速率 |
| 100 MHz | 高 | 高速率 |

#### 3. MIMO层数降低
- 4x4 MIMO → 2x2 MIMO
- 节省约15-20%功耗

#### 4. 跨时隙调度
- 减少盲检次数
- 节省PDCCH监控功耗

### 节能效果汇总
| 技术 | 节能比例 |
|------|----------|
| DRX | 30-50% |
| BWP适配 | 10-20% |
| MIMO层数降低 | 15-20% |
| 跨时隙调度 | 5-10% |

### 对智能手机建模的意义
- 5G协议层节能机制
- DRX周期对功耗的影响
- 网络配置参数与功耗的关系

## 关键词
- 5G NR, power saving, DRX, BWP, MIMO, cross-slot scheduling
