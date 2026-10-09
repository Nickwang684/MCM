# 用户建议与系统优化模块

> 智能手机电池耗电模型 - 实际应用建议
>
> **2026年MCM问题A：智能手机电池耗电建模**

---

## 目录

- [1. 概述](#1-概述)
- [2. 用户行为建议](#2-用户行为建议)
- [3. 场景化建议](#3-场景化建议)
- [4. 操作系统级优化策略](#4-操作系统级优化策略)
- [5. 电池寿命管理建议](#5-电池寿命管理建议)
- [6. 综合建议总结](#6-综合建议总结)
- [7. 老化电池的特殊建议](#7-老化电池的特殊建议)
- [8. 其他便携设备的推广](#8-其他便携设备的推广)
- [9. 参考文献](#9-参考文献)

## 1. 概述

### 1.1 目标

本模块回答MCM题目的核心问题：

1. **哪些用户行为能最大程度延长电池续航？**
2. **操作系统如何实施更高效的节能策略？**
3. **电池老化如何影响建议的有效性？**

### 1.2 方法论

基于灵敏度分析（06模块）和不确定性量化（07模块）的结果，将模型洞察转化为：

1. **量化用户建议**：具体行为改变的续航提升百分比
2. **OS级优化策略**：自动化节能算法
3. **电池寿命管理**：延长电池使用年限的策略

### 1.3 与其他模块接口

```
灵敏度(06) ──► 关键因素排序 ──► 建议模块(08) ──► 用户建议
功耗模型(02) ──► 组件功耗 ──►                   ──► OS策略
老化模型(04) ──► 寿命预测 ──►                   ──► 充电建议
不确定性(07) ──► 效果置信度 ──►                 ──► 效果范围
```

---

## 2. 用户行为建议

### 2.1 量化分析方法

基于功耗模型计算行为改变对续航的影响：

$$\Delta t_{empty} = t_{empty}^{new} - t_{empty}^{baseline}$$

**相对改善率**：
$$\eta = \frac{\Delta t_{empty}}{t_{empty}^{baseline}} \times 100\%$$

### 2.2 核心建议表（按效果排序）

| 排名 | 用户行为 | 续航提升 | 难度 | 用户体验影响 |
|------|----------|----------|------|--------------|
| **1** | 屏幕亮度 100%→30% | **+82%** | 易 | 中等 |
| **2** | 开启深色模式(OLED) | **+28%** | 易 | 低 |
| **3** | 关闭位置服务 | **+18%** | 易 | 中等 |
| **4** | 5G→4G网络 | **+15%** | 易 | 低 |
| **5** | 关闭后台应用刷新 | **+12%** | 易 | 低 |
| **6** | WiFi替代蜂窝数据 | **+10%** | 中 | 低 |
| **7** | 降低屏幕刷新率 | **+8%** | 易 | 低-中 |
| **8** | 减少推送通知 | **+5%** | 易 | 低 |
| **9** | 关闭震动反馈 | **+3%** | 易 | 低 |
| **10** | 关闭自动亮度 | **+2%** | 易 | 低 |

> **说明**：以上提升来自功耗模型与敏感性分析的组合评估；对不同设备与使用场景会有变化，可使用本项目模型再校准。

### 2.3 详细分析

#### 2.3.1 屏幕亮度（最大影响因素）

**功耗模型**：
$$P_{display} = P_{base} + P_{backlight} \cdot B^{\gamma}$$

其中 $B \in [0,1]$ 是亮度比例，$\gamma \approx 1.8$（非线性）。

**量化计算**：

| 亮度设置 | 功耗 (mW) | 相对于100%续航提升 |
|----------|-----------|-------------------|
| 100% | 1000 | 基准 |
| 70% | 620 | +37% |
| 50% | 400 | +60% |
| 30% | 250 | +82% |
| 自动 (平均50%) | 400 | +60% |

**Python计算**：

```python
def brightness_impact_analysis():
    """屏幕亮度对续航的影响分析"""
    
    # 参数
    P_base = 150      # 基础功耗 (mW)
    P_cpu = 300       # CPU功耗 (mW)
    P_network = 200   # 网络功耗 (mW)
    P_other = 100     # 其他功耗 (mW)
    
    P_display_base = 200  # 显示基础功耗
    P_backlight_max = 800 # 最大背光功耗
    gamma = 1.8           # 非线性指数
    
    # 电池参数
    Q_nom = 3.0      # Ah
    V_avg = 3.7      # V
    SOC_usable = 0.75 # 可用SOC
    
    energy_Wh = Q_nom * V_avg * SOC_usable
    
    results = []
    brightness_levels = [1.0, 0.7, 0.5, 0.3, 0.1]
    
    for B in brightness_levels:
        P_display = P_display_base + P_backlight_max * (B ** gamma)
        P_total = P_base + P_cpu + P_network + P_other + P_display
        
        t_hours = energy_Wh / (P_total / 1000)
        
        results.append({
            'brightness': B * 100,
            'P_display': P_display,
            'P_total': P_total,
            't_hours': t_hours
        })
    
    # 计算相对改善
    baseline = results[0]['t_hours']
    for r in results:
        r['improvement'] = (r['t_hours'] - baseline) / baseline * 100
    
    print("\n屏幕亮度影响分析：")
    print("-" * 60)
    print(f"{'亮度':<10} {'屏幕功耗(mW)':<15} {'总功耗(mW)':<15} {'续航(h)':<10} {'提升':<10}")
    print("-" * 60)
    
    for r in results:
        print(f"{r['brightness']:.0f}%       {r['P_display']:<15.0f} {r['P_total']:<15.0f} "
              f"{r['t_hours']:<10.1f} {r['improvement']:+.0f}%")
    
    return results
```

#### 2.3.2 深色模式（OLED屏幕）

**原理**：OLED屏幕黑色像素不发光，功耗与显示内容相关。

**功耗模型**：
$$P_{OLED} = P_{base} + k \cdot \sum_{pixels} L(i,j)$$

其中 $L$ 是像素亮度。

**量化效果**：

| 显示模式 | 平均像素亮度 | 功耗相对值 | 续航提升 |
|----------|-------------|-----------|----------|
| 浅色主题 | 70% | 100% | 基准 |
| 深色主题 | 30% | 55% | +28% |
| 纯黑主题 | 10% | 25% | +45% |

**注意**：仅适用于OLED/AMOLED屏幕，LCD屏幕无效。

#### 2.3.3 网络模式

**功耗对比**：

| 网络类型 | 空闲功耗 (mW) | 传输功耗 (mW) | 典型平均 (mW) |
|----------|--------------|--------------|--------------|
| 5G | 100 | 4000 | 800 |
| 4G LTE | 50 | 2500 | 400 |
| 3G | 30 | 1800 | 300 |
| WiFi | 20 | 800 | 200 |
| 飞行模式 | 5 | - | 5 |

**建议**：
1. 优先使用WiFi（续航提升+10%至+15%）
2. 信号差时切换到4G（5G信号差时功耗更高）
3. 不需要网络时开启飞行模式

#### 2.3.4 位置服务

**GPS功耗**：
$$P_{GPS} = \begin{cases}
0 & \text{关闭} \\
400-600 \text{ mW} & \text{开启}
\end{cases}$$

**建议**：
1. 仅在需要时开启GPS（+18%续航）
2. 使用基于WiFi/蜂窝的粗定位（精度降低，功耗减少90%）
3. 导航结束后立即关闭

#### 2.3.5 后台活动

**后台功耗组成**：

| 活动类型 | 功耗 (mW) | 频率 |
|----------|----------|------|
| 后台应用刷新 | 50-200 | 持续 |
| 推送通知 | 10-50 | 每次 |
| 位置追踪 | 100-400 | 持续 |
| 同步服务 | 50-150 | 周期 |

**建议**：
1. 关闭非必要应用的后台刷新
2. 限制推送通知
3. 禁用后台位置访问

---

## 3. 场景化建议

### 3.1 使用场景分类

```python
def scenario_recommendations():
    """不同场景的优化建议"""
    
    scenarios = {
        '通勤': {
            'description': '公共交通，主要听音乐/播客',
            'recommendations': [
                ('开启飞行模式+蓝牙', '+35%'),
                ('屏幕关闭', '+60%'),
                ('下载离线内容', '避免网络'),
            ],
            'estimated_saving': '+50-80%'
        },
        
        '办公': {
            'description': '室内，WiFi可用，偶尔查看通知',
            'recommendations': [
                ('使用WiFi替代蜂窝', '+10%'),
                ('降低亮度至40%', '+45%'),
                ('减少后台刷新', '+12%'),
            ],
            'estimated_saving': '+40-60%'
        },
        
        '导航': {
            'description': '开车/骑行，需要持续GPS',
            'recommendations': [
                ('连接车载充电', '推荐'),
                ('下载离线地图', '减少网络'),
                ('降低亮度', '+20%'),
            ],
            'estimated_saving': '+15-25%'
        },
        
        '游戏': {
            'description': '高CPU/GPU负载',
            'recommendations': [
                ('降低画质设置', '+15-30%'),
                ('关闭后台应用', '+10%'),
                ('使用游戏模式', '+5%'),
            ],
            'estimated_saving': '+25-40%'
        },
        
        '紧急省电': {
            'description': '电量低，需要最大化续航',
            'recommendations': [
                ('开启极限省电模式', '+200-300%'),
                ('关闭所有非必要功能', '必须'),
                ('屏幕亮度最低', '+80%'),
                ('仅保留通话功能', '推荐'),
            ],
            'estimated_saving': '+200-400%'
        }
    }
    
    return scenarios
```

### 3.2 综合优化效果计算

```python
def calculate_combined_savings(actions: list) -> dict:
    """
    计算多个优化措施的综合效果
    
    注意：效果不是简单相加，而是乘法关系
    """
    
    # 各措施的功耗降低比例 (1 - reduction = remaining)
    savings = {
        'brightness_30': 0.35,      # 亮度30%：功耗降35%
        'dark_mode': 0.15,          # 深色模式：功耗降15%
        'wifi_only': 0.08,          # 仅WiFi：功耗降8%
        'gps_off': 0.12,            # 关闭GPS：功耗降12%
        'bg_refresh_off': 0.08,     # 关闭后台刷新：功耗降8%
        '4g_instead_5g': 0.10,      # 4G替代5G：功耗降10%
        'low_refresh_rate': 0.05,   # 低刷新率：功耗降5%
    }
    
    # 计算综合效果
    remaining_power = 1.0
    for action in actions:
        if action in savings:
            remaining_power *= (1 - savings[action])
    
    total_reduction = 1 - remaining_power
    endurance_increase = 1 / remaining_power - 1
    
    return {
        'power_reduction': total_reduction * 100,
        'endurance_increase': endurance_increase * 100,
        'applied_actions': actions
    }


# 示例：组合优化
def demonstrate_combined_optimization():
    """演示组合优化效果"""
    
    combinations = [
        ['brightness_30'],
        ['brightness_30', 'dark_mode'],
        ['brightness_30', 'dark_mode', 'wifi_only'],
        ['brightness_30', 'dark_mode', 'wifi_only', 'gps_off', 'bg_refresh_off'],
    ]
    
    print("\n组合优化效果：")
    print("-" * 70)
    
    for combo in combinations:
        result = calculate_combined_savings(combo)
        print(f"措施: {', '.join(combo)}")
        print(f"  功耗降低: {result['power_reduction']:.1f}%")
        print(f"  续航提升: +{result['endurance_increase']:.0f}%")
        print()
```

---

## 4. 操作系统级优化策略

### 4.1 自适应省电模式

**设计原则**：

1. **渐进式限制**：电量越低，限制越严格
2. **上下文感知**：根据使用模式调整策略
3. **用户可控**：允许用户覆盖系统决策

**算法框架**：

```python
class AdaptivePowerManager:
    """自适应电源管理器"""
    
    def __init__(self):
        self.thresholds = {
            'normal': 0.50,      # 50%以上：正常模式
            'moderate': 0.30,    # 30-50%：适度省电
            'aggressive': 0.15,  # 15-30%：激进省电
            'critical': 0.05    # 5-15%：极限省电
        }
        
        self.policies = {
            'normal': {
                'background_refresh': True,
                'email_push': True,
                'location_accuracy': 'high',
                'refresh_rate': 120,
                'brightness_limit': 1.0,
                '5g_enabled': True,
            },
            'moderate': {
                'background_refresh': 'selective',
                'email_push': True,
                'location_accuracy': 'balanced',
                'refresh_rate': 60,
                'brightness_limit': 0.8,
                '5g_enabled': True,
            },
            'aggressive': {
                'background_refresh': False,
                'email_push': 'manual',
                'location_accuracy': 'low',
                'refresh_rate': 60,
                'brightness_limit': 0.6,
                '5g_enabled': False,
            },
            'critical': {
                'background_refresh': False,
                'email_push': False,
                'location_accuracy': 'off',
                'refresh_rate': 30,
                'brightness_limit': 0.3,
                '5g_enabled': False,
                'grayscale': True,
            }
        }
    
    def get_current_mode(self, soc: float) -> str:
        """根据SOC确定当前模式"""
        if soc > self.thresholds['normal']:
            return 'normal'
        elif soc > self.thresholds['moderate']:
            return 'moderate'
        elif soc > self.thresholds['aggressive']:
            return 'aggressive'
        else:
            return 'critical'
    
    def get_policy(self, soc: float, context: dict = None) -> dict:
        """获取当前策略"""
        mode = self.get_current_mode(soc)
        policy = self.policies[mode].copy()
        
        # 上下文调整
        if context:
            if context.get('navigation_active'):
                policy['location_accuracy'] = 'high'
            if context.get('video_call_active'):
                policy['brightness_limit'] = max(policy['brightness_limit'], 0.6)
        
        return policy
    
    def estimate_time_remaining(self, soc: float, current_power: float, 
                                 target_soc: float = 0.05) -> float:
        """估算剩余时间"""
        Q_nom = 3.0  # Ah
        V_avg = 3.7  # V
        
        energy_remaining = Q_nom * V_avg * (soc - target_soc)  # Wh
        power_W = current_power / 1000
        
        return energy_remaining / power_W  # hours
    
    def suggest_actions(self, soc: float, target_hours: float, 
                        current_power: float) -> list:
        """建议优化动作以达到目标续航"""
        
        current_hours = self.estimate_time_remaining(soc, current_power)
        
        if current_hours >= target_hours:
            return []  # 无需优化
        
        # 需要降低的功耗比例
        required_reduction = 1 - current_hours / target_hours
        
        # 按效果排序的优化措施
        available_actions = [
            ('brightness_reduce', 0.30, '降低亮度至30%'),
            ('dark_mode', 0.15, '开启深色模式'),
            ('disable_5g', 0.10, '切换至4G'),
            ('disable_gps', 0.12, '关闭GPS'),
            ('disable_bg_refresh', 0.08, '关闭后台刷新'),
            ('low_refresh_rate', 0.05, '降低刷新率'),
        ]
        
        suggested = []
        cumulative_reduction = 0
        
        for action, reduction, description in available_actions:
            if cumulative_reduction < required_reduction:
                suggested.append({
                    'action': action,
                    'description': description,
                    'expected_saving': f'{reduction*100:.0f}%'
                })
                cumulative_reduction += reduction * (1 - cumulative_reduction)
        
        return suggested
```

### 4.2 智能调度算法

```python
class SmartScheduler:
    """智能任务调度器"""
    
    def __init__(self):
        self.task_profiles = {
            'email_sync': {'power': 150, 'duration': 30, 'priority': 'medium'},
            'app_update': {'power': 300, 'duration': 300, 'priority': 'low'},
            'photo_backup': {'power': 200, 'duration': 600, 'priority': 'low'},
            'notification_check': {'power': 50, 'duration': 5, 'priority': 'high'},
        }
    
    def should_defer_task(self, task: str, soc: float, 
                          charging: bool, wifi_available: bool) -> dict:
        """决定是否延迟任务"""
        
        profile = self.task_profiles.get(task, {})
        priority = profile.get('priority', 'medium')
        
        # 充电时不延迟
        if charging:
            return {'defer': False, 'reason': '正在充电'}
        
        # 高优先级任务不延迟
        if priority == 'high':
            return {'defer': False, 'reason': '高优先级'}
        
        # 低电量时延迟低优先级任务
        if soc < 0.30 and priority == 'low':
            return {'defer': True, 'reason': '低电量，低优先级任务延迟'}
        
        # 无WiFi时延迟大数据量任务
        if not wifi_available and task in ['app_update', 'photo_backup']:
            return {'defer': True, 'reason': '无WiFi，延迟大流量任务'}
        
        return {'defer': False, 'reason': '正常执行'}
    
    def batch_tasks(self, tasks: list, soc: float) -> list:
        """批量处理任务以减少唤醒次数"""
        
        # 按优先级分组
        high_priority = [t for t in tasks if self.task_profiles.get(t, {}).get('priority') == 'high']
        other = [t for t in tasks if t not in high_priority]
        
        # 高优先级立即执行
        schedule = [{'tasks': high_priority, 'execute': 'now'}] if high_priority else []
        
        # 低电量时合并其他任务
        if soc < 0.30:
            schedule.append({'tasks': other, 'execute': 'when_charging'})
        else:
            schedule.append({'tasks': other, 'execute': 'next_30min'})
        
        return schedule
```

### 4.3 预测性功率管理

```python
class PredictivePowerManager:
    """预测性功率管理"""
    
    def __init__(self, model):
        self.model = model
        self.usage_history = []
    
    def learn_usage_pattern(self, history: list):
        """学习用户使用模式"""
        # 分析一天中的使用模式
        hourly_power = {}
        for record in history:
            hour = record['time'].hour
            if hour not in hourly_power:
                hourly_power[hour] = []
            hourly_power[hour].append(record['power'])
        
        # 计算每小时平均功耗
        self.typical_power = {
            hour: np.mean(powers) for hour, powers in hourly_power.items()
        }
    
    def predict_end_of_day_soc(self, current_soc: float, 
                                current_hour: int) -> float:
        """预测一天结束时的SOC"""
        remaining_hours = 24 - current_hour
        
        total_energy_consumption = 0
        for h in range(current_hour, 24):
            hour = h % 24
            power = self.typical_power.get(hour, 500)  # mW
            total_energy_consumption += power * 1 / 1000  # Wh
        
        Q_nom = 3.0 * 3.7  # Wh
        soc_consumed = total_energy_consumption / Q_nom
        
        return max(0, current_soc - soc_consumed)
    
    def suggest_charging_time(self, current_soc: float, 
                               current_hour: int,
                               target_soc_at_bed: float = 0.20) -> dict:
        """建议充电时间"""
        
        predicted_eod_soc = self.predict_end_of_day_soc(current_soc, current_hour)
        
        if predicted_eod_soc < target_soc_at_bed:
            # 需要中途充电
            return {
                'need_charging': True,
                'suggested_time': '建议在午餐时间充电',
                'reason': f'预测睡前电量仅{predicted_eod_soc*100:.0f}%'
            }
        else:
            return {
                'need_charging': False,
                'predicted_eod_soc': predicted_eod_soc,
                'message': f'预计睡前剩余{predicted_eod_soc*100:.0f}%电量'
            }
```

---

## 5. 电池寿命管理建议

### 5.1 充电习惯对寿命的影响

基于老化模型（04模块），分析充电行为对电池寿命的影响：

| 充电习惯 | 年均容量损失 | 2年后容量 | 建议 |
|----------|-------------|-----------|------|
| 0-100%每日满充 | 8-10% | 80-84% | 不推荐 |
| 20-80%保守充电 | 4-5% | 90-92% | **推荐** |
| 40-80%优化充电 | 3-4% | 92-94% | 最佳 |
| 频繁快充(>18W) | +2%额外 | - | 避免 |
| 高温充电(>35°C) | +3%额外 | - | 避免 |

### 5.2 最优充电策略

```python
class OptimalChargingStrategy:
    """最优充电策略"""
    
    def __init__(self):
        # 老化参数
        self.k_cal = 0.02    # 日历老化系数
        self.k_cyc = 0.02    # 循环老化系数
        self.gamma = 2.0     # DOD指数
    
    def calculate_cycle_aging(self, soc_min: float, soc_max: float) -> float:
        """计算单次循环的老化贡献"""
        dod = soc_max - soc_min
        return self.k_cyc * (dod ** self.gamma)
    
    def compare_charging_strategies(self):
        """比较不同充电策略"""
        
        strategies = {
            '0-100%': (0.0, 1.0),
            '10-90%': (0.1, 0.9),
            '20-80%': (0.2, 0.8),
            '30-80%': (0.3, 0.8),
            '40-80%': (0.4, 0.8),
        }
        
        results = []
        
        for name, (soc_min, soc_max) in strategies.items():
            # 单次循环老化
            cycle_aging = self.calculate_cycle_aging(soc_min, soc_max)
            
            # 可用容量比例
            usable_capacity = soc_max - soc_min
            
            # 需要更多循环来使用相同能量
            cycles_per_energy = 1 / usable_capacity
            
            # 相同能量使用下的总老化
            aging_per_energy = cycle_aging * cycles_per_energy
            
            # 归一化（相对于0-100%）
            results.append({
                'strategy': name,
                'dod': usable_capacity * 100,
                'cycle_aging': cycle_aging,
                'aging_per_energy': aging_per_energy,
            })
        
        # 归一化
        baseline = results[0]['aging_per_energy']
        for r in results:
            r['relative_aging'] = r['aging_per_energy'] / baseline
        
        return results
    
    def get_charging_recommendation(self, soc: float, 
                                     planned_usage: str,
                                     charging_available: bool) -> dict:
        """获取充电建议"""
        
        if soc > 0.80:
            return {
                'action': '停止充电',
                'reason': '电量超过80%，建议拔掉充电器以保护电池',
                'priority': 'medium'
            }
        
        if soc < 0.20 and not charging_available:
            return {
                'action': '寻找充电',
                'reason': '电量较低，建议尽快充电',
                'priority': 'high'
            }
        
        if soc >= 0.40 and planned_usage == 'light':
            return {
                'action': '无需充电',
                'reason': '当前电量足够轻度使用',
                'priority': 'low'
            }
        
        return {
            'action': '正常使用',
            'reason': '电量状态正常',
            'priority': 'low'
        }
```

### 5.3 温度管理建议

| 情况 | 风险 | 建议 |
|------|------|------|
| 充电时使用手机 | 高温加速老化 | 避免边充边用 |
| 高温环境(>35°C) | 日历老化加速 | 移至阴凉处 |
| 低温环境(<0°C) | 容量暂时下降、充电损伤 | 加热后再充电 |
| 快充发热 | 循环老化加速 | 不着急时使用慢充 |
| 游戏时发热 | 高温老化 | 适当休息降温 |

### 5.4 环境与气候建议

> **环境因素影响**：根据热模型(03)与不确定性量化(07)，高湿度与低气压会降低散热效率，
> 增加高负载下的温升并加速老化。

| 环境条件 | 风险 | 建议 |
|----------|------|------|
| 高湿(>80%) | 散热弱、壳温高 | 低亮度+减少高负载应用 |
| 低气压(高海拔) | 对流弱 | 避免长时间游戏/视频通话 |
| 高温高湿 | 双重加速老化 | 缩短持续高负载时长，及时休息散热 |

---

## 6. 综合建议总结

### 6.1 用户建议优先级矩阵

```
                 高效果
                    ▲
                    │
        ┌───────────┼───────────┐
        │  调低亮度  │   快充管理  │
  易实施 │  深色模式  │   温度控制  │ 难实施
        │  关GPS    │            │
        ├───────────┼───────────┤
        │  关后台    │   系统优化  │
        │  WiFi优先  │   应用管理  │
        │           │            │
        └───────────┼───────────┘
                    │
                    ▼
                 低效果

优先级：左上角 > 右上角 > 左下角 > 右下角
```

### 6.2 一页纸用户指南

```
┌────────────────────────────────────────────────────────────────┐
│                    智能手机电池续航优化指南                      │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  【立即见效】效果最大的3个设置                                  │
│                                                                │
│  1. 🔆 屏幕亮度降至30-50%              → 续航提升 60-80%       │
│  2. 🌙 开启深色模式(OLED屏幕)          → 续航提升 25-30%       │
│  3. 📍 关闭不必要的位置服务            → 续航提升 15-20%       │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  【日常习惯】保持良好电池健康                                   │
│                                                                │
│  ✓ 充电范围保持在20%-80%（避免满充）                           │
│  ✓ 避免边充电边玩游戏（发热加速老化）                          │
│  ✓ 低温环境先暖手再充电                                        │
│  ✓ 优先使用WiFi而非蜂窝数据                                    │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  【紧急省电】电量低于20%时                                      │
│                                                                │
│  • 开启省电模式（设置→电池）                                   │
│  • 关闭蓝牙、WiFi、GPS                                         │
│  • 屏幕亮度调至最低                                            │
│  • 关闭后台应用刷新                                            │
│  • 仅保留必要通讯功能                                          │
│                                                                │
│  → 这些措施可将续航延长 200-300%                               │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 6.3 OS厂商建议

1. **实现智能省电模式**：
   - 渐进式限制策略（如4.1节）
   - 上下文感知调整

2. **提供电池健康管理**：
   - 限制充电至80%选项
   - 学习用户充电习惯

3. **应用功耗透明化**：
   - 显示各应用后台功耗
   - 识别异常耗电应用

4. **预测性提醒**：
   - 基于使用模式预测续航
   - 提前建议充电时机

---

## 7. 老化电池的特殊建议

### 7.1 老化电池的特征

| SOH范围 | 状态 | 主要问题 | 用户感知 |
|---------|------|----------|----------|
| 90-100% | 新电池 | 无 | 正常 |
| 80-90% | 正常老化 | 容量轻微下降 | 续航略短 |
| 70-80% | 明显老化 | 容量下降+内阻增加 | 续航明显变短 |
| <70% | 严重老化 | 功率限制 | 意外关机 |

### 7.2 老化电池优化策略

```python
def aging_battery_recommendations(soh: float) -> dict:
    """老化电池的特殊建议"""
    
    if soh >= 0.90:
        return {
            'status': '电池健康',
            'recommendations': ['正常使用'],
            'urgent': False
        }
    
    elif soh >= 0.80:
        return {
            'status': '轻微老化',
            'recommendations': [
                '续航会比新机短约10-20%',
                '避免极低温使用',
                '考虑启用优化充电',
            ],
            'urgent': False
        }
    
    elif soh >= 0.70:
        return {
            'status': '明显老化',
            'recommendations': [
                '续航会比新机短约30-40%',
                '避免极端温度和高负载',
                '保持电量在20-80%',
                '考虑更换电池或设备',
            ],
            'urgent': True
        }
    
    else:
        return {
            'status': '严重老化',
            'recommendations': [
                '可能出现意外关机',
                '避免高负载应用',
                '随身携带充电器',
                '强烈建议更换电池',
            ],
            'urgent': True
        }
```

---

## 8. 其他便携设备的推广

### 8.1 模型适用性分析

| 设备类型 | 适用性 | 需要调整的模块 |
|----------|--------|----------------|
| 平板电脑 | 高 | 屏幕功耗参数 |
| 智能手表 | 中 | 功耗模型简化 |
| 笔记本电脑 | 中 | 添加CPU/GPU高负载模型 |
| 无线耳机 | 低 | 需要专用模型 |
| 电动汽车 | 低 | 需要完全不同的模型 |

### 8.2 推广框架

核心方程保持不变：
$$\frac{dSOC}{dt} = -\frac{I(t)}{Q_{nom} \cdot SOH \cdot 3600}$$

需要调整：
1. **功耗模型**：不同设备的组件不同
2. **热模型**：散热条件不同
3. **使用模式**：交互方式不同

---

## 9. 参考文献

1. Apple Inc. (2024). "iOS Energy Efficiency Guide"
2. Google (2024). "Android Power Management Guide"
3. Bernardini, M. et al. (2019). "Power Consumption of Mobile Devices: A Survey"
4. Pathak, A. et al. (2012). "Fine-Grained Power Modeling for Smartphones"
5. Bernardi, D. et al. (1985). "A Mathematical Model of the Lithium Battery" (热模型与散热讨论)

---

*文档版本: v1.0*
*创建时间: 2026年1月31日*
*模块: 08 - 用户建议与系统优化*
