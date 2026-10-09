# 227. Unlocking the Power of 4G/5G Mobile Networks: An Empirical Study on YouTube Edge Services

## 基本信息
- **标题**: Unlocking the Power of 4G/5G Mobile Networks: An Empirical Dive into Quality and Energy Efficiency in YouTube Edge Services
- **作者**: Peixuan Song, JunKyu Lee, Ahmed M. Abdelmoniem, Lev Mukhanov
- **期刊**: Computer Networks
- **年份**: 2025
- **DOI**: 10.1016/j.comnet.2025.111344
- **链接**: https://www.sciencedirect.com/science/article/pii/S1389128625003111

## 主要内容

### 研究背景
- 视频流是移动数据流量的主要组成
- 边缘服务影响视频质量和能耗
- 4G/5G网络下的YouTube能耗特性

### 关键发现

#### 视频流能耗模型
$$E_{video} = E_{network} + E_{decode} + E_{display}$$

分解：
- 网络传输：30-40%
- 视频解码：20-30%
- 屏幕显示：30-40%

#### 分辨率与能耗
| 分辨率 | 码率 | 相对能耗 |
|--------|------|----------|
| 360p | 0.5 Mbps | 1.0x |
| 720p | 2 Mbps | 1.5x |
| 1080p | 5 Mbps | 2.2x |
| 4K | 20 Mbps | 4.0x |

#### 网络类型影响
- 5G下载快但唤醒功耗高
- 4G中等速度，功耗平衡
- WiFi最节能（适合长视频）

### 边缘缓存效果
$$E_{cached} = E_{network} \times (1 - \text{Cache Hit Rate}) + E_{local}$$

### 对智能手机建模的意义
- 视频应用的详细能耗分解
- 码率-能耗关系模型
- 网络选择策略的能耗影响

## 关键词
- Video streaming, YouTube, 4G, 5G, energy efficiency, edge services
