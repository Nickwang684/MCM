# 125. Analysis of Peukert and Liebenow Equations Use for Evaluation of Capacity Released by Lithium-Ion Batteries

## 基本信息
- **标题**: Analysis of Peukert and Liebenow Equations Use for Evaluation of Capacity Released by Lithium-Ion Batteries
- **作者**: Galushkin et al.
- **期刊**: Processes (MDPI)
- **年份**: 2021
- **卷/期**: Volume 9, Issue 10, 1753
- **DOI**: 10.3390/pr9101753
- **链接**: https://www.mdpi.com/2227-9717/9/10/1753
- **开放获取**: 是

## 研究内容摘要
本文比较分析了Peukert方程和Liebenow方程在评估锂离子电池释放容量中的应用。Liebenow方程是Peukert方程的替代形式，两者在不同条件下各有优势。

## 关键发现
1. **两种方程对比**：
   - Peukert方程：$C = I^n \cdot t$
   - Liebenow方程：$C = C_0 - k \cdot I \cdot t$
2. **适用范围**：Liebenow方程在低放电倍率下更准确
3. **组合应用**：提出组合两种方程的混合方法
4. **锂离子特性**：锂离子电池更适合Liebenow方程描述

## 方程对比
| 方程 | 形式 | 适用范围 | 锂电池适用性 |
|-----|------|---------|-------------|
| Peukert | 幂律 | 高放电倍率 | 中等 |
| Liebenow | 线性 | 低放电倍率 | 较好 |
| 混合 | 分段 | 全范围 | 最佳 |

## 与考虑因素的相关性
| 考虑因素 | 相关性 | 说明 |
|---------|--------|------|
| 放电倍率效应 | ★★★★★ | 两种方程的核心应用 |
| SOC估计 | ★★★★☆ | 容量释放评估 |
| 使用历史 | ★★★☆☆ | 不同使用强度下的容量变化 |

## 与论文研究方向的关联
- **方法选择指导**：智能手机正常使用时放电倍率较低（0.2C-1C），Liebenow方程可能更适用
- **模型简化**：对于锂离子电池，线性模型可能足够准确
- **建模权衡**：在模型复杂度和准确性之间提供选择依据
- **开放获取**：方便获取完整方法论和数据
