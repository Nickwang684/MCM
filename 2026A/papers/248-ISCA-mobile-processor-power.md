# 248. IEEE/ACM ISCA - Mobile Processor Power Modeling

## 基本信息
- **标题**: Accurate Power Modeling for Mobile Processors: From Microarchitecture to System Level
- **会议**: IEEE/ACM ISCA
- **年份**: 2022
- **类型**: 体系结构论文

## 主要内容

### 处理器功耗组成

$$P_{total} = P_{dynamic} + P_{static} + P_{short-circuit}$$

$$P_{dynamic} = \alpha \cdot C \cdot V_{dd}^2 \cdot f$$

$$P_{static} = I_{leak} \cdot V_{dd}$$

### 移动SoC功耗分解

| 组件 | 占比 | 可控性 |
|------|------|--------|
| CPU | 30-40% | 高(DVFS) |
| GPU | 20-30% | 高(DVFS) |
| Memory | 10-15% | 中 |
| Modem | 10-20% | 低 |
| Display | 15-25% | 中 |
| Others | 5-10% | 低 |

### 微架构功耗模型
$$P_{core} = \sum_i \alpha_i \cdot P_{component,i}$$

组件列表：
- 取指单元、解码器
- 发射队列、ROB
- ALU、FPU
- L1/L2 Cache
- TLB

### 功耗-性能Pareto分析
$$\text{Energy Efficiency} = \frac{\text{IPC}}{P_{core}}$$

最优工作点：
$$f_{opt} = \arg\max_f \frac{\text{Perf}(f)}{P(f)}$$

### 对智能手机建模的意义
- SoC功耗分解模型
- CPU/GPU功耗的精确建模
- DVFS对功耗的定量影响

## 关键词
- Mobile processor, power modeling, DVFS, SoC, microarchitecture
