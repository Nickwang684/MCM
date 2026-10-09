# 205. Automated OS-level Device Runtime Power Management (ACM ASPLOS)

## 基本信息
- **标题**: Automated OS-level Device Runtime Power Management
- **期刊/会议**: ACM ASPLOS 2015 (体系结构顶会)
- **年份**: 2015
- **作者**: Chao Xu (Rice), Felix Xiaozhu Lin (Purdue), Yuyang Wang (Tsinghua), Lin Zhong (Rice)
- **链接**: https://www.yecl.org/publications/xu2015asplos.pdf

## 核心内容

### 问题陈述
- SoC上的非CPU设备占据显著芯片面积
- 空闲设备需要进入低功耗状态
- 当前依赖驱动程序进行功耗管理是有害的

### 核心贡献
1. **三个关键信息**: 识别设备运行时功耗管理的必要信息
2. **自动化方法**: 无需驱动程序参与的功耗管理
3. **操作系统级实现**: OS层面的统一管理

### 技术方法
- 自动检测设备空闲状态
- 统一的低功耗状态进入机制
- 保持性能预期的同时最小化能耗

## 与本研究的关联
- ASPLOS体系结构顶会
- 操作系统级功耗管理
- 支持idea.md中"处理器负载"因素

## 标签
`ASPLOS` `功耗管理` `操作系统` `设备驱动` `体系结构`
