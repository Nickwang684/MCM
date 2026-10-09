# 智能手机功耗分解模型

> 智能手机电池连续时间建模 - 第2部分
>
> **核心目标**：建立组件级功耗模型，计算总功耗P(t)和放电电流I(t)

---

## 目录

- [1. 模型概述](#1-模型概述)
- [2. 总功耗方程](#2-总功耗方程)
- [3. 显示屏功耗模型](#3-显示屏功耗模型)
- [4. CPU功耗模型](#4-cpu功耗模型)
- [5. GPU功耗模型](#5-gpu功耗模型)
- [6. 网络功耗模型](#6-网络功耗模型)
  - [6.1 WiFi功耗](#61-wifi功耗)
  - [6.2 蜂窝网络功耗(4G/5G)](#62-蜂窝网络功耗4g5g)
  - [6.3 蓝牙功耗](#63-蓝牙功耗)
  - [6.4 蜂窝RRC状态机与“尾耗”](#64-蜂窝rrc状态机与尾耗)
- [7. 传感器功耗模型](#7-传感器功耗模型)
- [8. 其他组件功耗](#8-其他组件功耗)
- [9. 使用场景功耗汇总](#9-使用场景功耗汇总)
- [10. 完整功耗模型](#10-完整功耗模型)
- [11. 与其他子模型的接口](#11-与其他子模型的接口)
- [12. 数值实现](#12-数值实现)
- [13. 模型验证](#13-模型验证)
- [参考文献](#参考文献)

## 1. 模型概述

### 1.1 建模目标

将智能手机总功耗建模为各组件功耗之和：

$$P_{total}(t) = \sum_{i} P_i(t)$$

**输入**：
- 各组件状态参数（使用率、亮度、信号强度等）
- 用户使用场景

**输出**：
- 总功耗 $P_{total}(t)$ [W]
- 放电电流 $I(t) = P_{total}(t) / V(t)$ [A]

### 1.2 功耗组件分类

| 类别 | 组件 | 典型功耗占比 |
|------|------|--------------|
| 显示 | 屏幕（LCD/OLED） | 30-50% |
| 计算 | CPU、GPU | 20-40% |
| 通信 | WiFi、蜂窝网络、蓝牙 | 10-25% |
| 传感器 | GPS、加速度计、陀螺仪 | 5-15% |
| 其他 | 音频、相机、存储 | 5-10% |
| 基础 | 基带、待机功耗 | 5-10% |

**文献依据**：论文278（IEEE Access完整手机功耗模型）、论文178（UCSD 3W's）

---

## 2. 总功耗方程

### 2.1 基本分解模型

$$\boxed{P_{total}(t) = P_{base} + P_{display}(t) + P_{CPU}(t) + P_{GPU}(t) + P_{network}(t) + P_{sensors}(t) + P_{audio}(t) + P_{camera}(t)}$$

### 2.2 简化三状态模型

对于基本建模，可采用三状态简化：

$$P_{total}(t) = \begin{cases}
P_{idle} & \text{待机状态} \\
P_{active,low} & \text{轻度使用} \\
P_{active,high} & \text{重度使用}
\end{cases}$$

**典型功耗值**：

| 状态 | 功耗 [mW] | 电流@3.8V [mA] | 续航时间(3000mAh) |
|------|-----------|----------------|-------------------|
| 深度睡眠 | 5-15 | 1-4 | 750-3000 h |
| 待机(屏幕关) | 50-150 | 13-40 | 75-230 h |
| 轻度使用 | 500-1500 | 130-400 | 7.5-23 h |
| 重度使用 | 2000-5000 | 530-1300 | 2.3-5.7 h |
| 峰值负载 | 6000-10000 | 1600-2600 | 1.1-1.9 h |

---

## 3. 显示屏功耗模型

### 3.1 LCD屏幕

LCD功耗主要来自背光，与显示内容关系较小：

$$\boxed{P_{LCD}(t) = P_{backlight,max} \cdot B(t) + P_{driver}}$$

其中：
- $B(t) \in [0, 1]$：亮度等级（0=最暗，1=最亮）
- $P_{backlight,max}$：最大背光功耗
- $P_{driver}$：驱动电路固定功耗

**参数**：

| 参数 | 典型值 | 范围 | 单位 |
|------|--------|------|------|
| $P_{backlight,max}$ | 800 | 500-1500 | mW |
| $P_{driver}$ | 50 | 30-100 | mW |

**亮度-功耗关系**：

| 亮度 | LCD功耗 [mW] |
|------|--------------|
| 0% (最暗) | 80 |
| 25% | 250 |
| 50% | 450 |
| 75% | 650 |
| 100% (最亮) | 850 |

### 3.2 OLED屏幕

OLED功耗与显示内容强相关（黑色像素不耗电）：

$$\boxed{P_{OLED}(t) = P_{base,OLED} + \sum_{pixels} P_{pixel}(R, G, B, B_{brightness})}$$

简化为平均像素亮度模型：

$$P_{OLED}(t) = P_{base,OLED} + k_{OLED} \cdot B(t) \cdot APL(t)$$

其中：
- $APL(t)$：平均像素亮度 (Average Picture Level), $\in [0, 1]$
- $k_{OLED}$：功耗系数

**RGB颜色功耗差异**：

| 颜色  | 相对功耗 | 说明       |
| --- | ---- | -------- |
| 黑色  | 0%   | OLED像素关闭 |
| 蓝色  | 100% | 最耗电      |
| 红色  | 65%  | 中等       |
| 绿色  | 70%  | 中等       |
| 白色  | 235% | RGB全开    |

**OLED功耗方程（颜色敏感）**：

$$P_{OLED} = P_{base} + N_{pixels} \cdot B(t) \cdot [k_R \cdot \bar{R} + k_G \cdot \bar{G} + k_B \cdot \bar{B}]$$

**参数**（6.5英寸FHD+ OLED）：

| 参数 | 值 | 单位 |
|------|------|------|
| $P_{base,OLED}$ | 30 | mW |
| $k_{OLED}$ | 1200 | mW |
| $k_R$ | 0.65 | - |
| $k_G$ | 0.70 | - |
| $k_B$ | 1.00 | - |

### 3.3 刷新率影响

高刷新率屏幕额外功耗：

$$P_{display}(f_{refresh}) = P_{display,60Hz} \cdot \left(\frac{f_{refresh}}{60}\right)^{0.3}$$

| 刷新率 | 相对功耗 | 典型功耗增加 |
|--------|----------|--------------|
| 60 Hz | 1.00× | 基准 |
| 90 Hz | 1.14× | +14% |
| 120 Hz | 1.23× | +23% |
| 144 Hz | 1.29× | +29% |

**文献依据**：论文178（3W's UCSD功耗测量）

---

## 4. CPU功耗模型

### 4.1 DVFS功耗模型

CPU功耗遵循动态电压频率调节(DVFS)关系：

$$\boxed{P_{CPU}(t) = P_{static} + P_{dynamic}(t)}$$

**静态功耗**（漏电流）：
$$P_{static} = N_{cores} \cdot V^2 \cdot I_{leak}(T)$$

**动态功耗**：
$$P_{dynamic} = \alpha \cdot C_{eff} \cdot V^2 \cdot f \cdot u(t)$$

其中：
- $\alpha$：活动因子
- $C_{eff}$：有效电容
- $V$：工作电压
- $f$：时钟频率
- $u(t) \in [0, 1]$：CPU利用率

### 4.2 简化多核模型

$$\boxed{P_{CPU}(t) = P_{idle,CPU} + \sum_{i=1}^{N_{cores}} u_i(t) \cdot P_{core,max} \cdot \left(\frac{f_i}{f_{max}}\right)^3}$$

注：功耗与频率近似呈立方关系（$P \propto V^2 f$，而 $V \propto f$）

**智能手机SoC典型参数**：

| 核心类型 | 数量 | 最大频率 | 单核最大功耗 |
|----------|------|----------|--------------|
| 大核(Cortex-A7x) | 1-2 | 2.8-3.2 GHz | 2000-3000 mW |
| 中核(Cortex-A7x) | 2-3 | 2.0-2.4 GHz | 800-1200 mW |
| 小核(Cortex-A5x) | 4 | 1.8-2.0 GHz | 200-400 mW |
| **总峰值** | - | - | **8000-12000 mW** |

### 4.3 利用率-功耗查找表

实测数据拟合（骁龙8系列参考）：

| CPU利用率 | 功耗 [mW] | 说明 |
|-----------|-----------|------|
| 0% (idle) | 50-100 | 仅小核待机 |
| 10% | 150-250 | 轻度后台 |
| 25% | 300-500 | 普通应用 |
| 50% | 600-1000 | 中等负载 |
| 75% | 1200-2000 | 重度应用 |
| 100% | 2500-4000 | 游戏/渲染 |

**文献依据**：论文09（多核CPU功耗模型）、论文174（AndroWatts）

---

## 5. GPU功耗模型

### 5.1 基本模型

$$\boxed{P_{GPU}(t) = P_{idle,GPU} + u_{GPU}(t) \cdot P_{GPU,max} \cdot \left(\frac{f_{GPU}}{f_{GPU,max}}\right)^2}$$

### 5.2 典型参数

| 状态 | 功耗 [mW] | 典型场景 |
|------|-----------|----------|
| 空闲 | 0-20 | 后台/2D界面 |
| 轻度 | 100-300 | 滚动/动画 |
| 中度 | 500-1000 | 视频播放 |
| 重度 | 1500-2500 | 3D游戏 |
| 峰值 | 3000-5000 | 极限测试 |

**文献依据**：论文13（GPU功耗建模）

---

## 6. 网络功耗模型

### 6.1 WiFi功耗

$$\boxed{P_{WiFi}(t) = \begin{cases}
P_{WiFi,idle} & \text{连接但空闲} \\
P_{WiFi,base} + k_{WiFi} \cdot R_{data}(t) & \text{传输中}
\end{cases}}$$

**参数**：

| 状态 | 功耗 [mW] | 说明 |
|------|-----------|------|
| 关闭 | 0 | - |
| 空闲(连接) | 5-20 | PSM模式 |
| 扫描 | 200-400 | 查找网络 |
| 接收(Rx) | 100-200 | 下载 |
| 发送(Tx) | 200-400 | 上传 |
| 高吞吐 | 300-600 | 视频流 |

**吞吐量功耗关系**：
$$P_{WiFi} = 100 + 0.005 \cdot R_{Mbps}$$ [mW]

### 6.2 蜂窝网络功耗(4G/5G)

$$\boxed{P_{cellular}(t) = P_{cell,base}(RSRP) + k_{cell} \cdot R_{data}(t)}$$

**信号强度影响**（RSRP）：

| 信号质量 | RSRP [dBm] | 基础功耗 [mW] | 说明 |
|----------|------------|---------------|------|
| 优秀 | > -80 | 100-200 | 满格 |
| 良好 | -80 ~ -100 | 200-400 | 3-4格 |
| 一般 | -100 ~ -110 | 400-600 | 2格 |
| 差 | -110 ~ -120 | 600-1000 | 1格 |
| 极差 | < -120 | 1000-1500 | 边缘 |

**4G vs 5G对比**：

| 网络 | 空闲 [mW] | 典型 [mW] | 峰值 [mW] |
|------|-----------|-----------|-----------|
| 4G LTE | 50-100 | 200-500 | 800-1200 |
| 5G Sub-6 | 100-200 | 400-800 | 1500-2500 |
| 5G mmWave | 200-400 | 800-1500 | 2500-4000 |

**文献依据**：论文149（WiFi功耗ICDCS）、论文221（5G功耗SIGCOMM）

### 6.3 蓝牙功耗

| 状态 | 功耗 [mW] |
|------|-----------|
| 关闭 | 0 |
| 待机 | 1-3 |
| 连接(空闲) | 3-10 |
| 传输(BLE) | 10-30 |
| 传输(Classic) | 30-100 |
| 音频流(A2DP) | 50-150 |

### 6.4 蜂窝RRC状态机与“尾耗”

> **为什么要建模RRC状态机？**
> 
> 蜂窝网络功耗不仅取决于数据速率，还取决于RRC状态（Idle / Connected / DCH）。
> 即使传输结束，手机仍会停留在高功耗状态一段“尾时间”（tail time），造成额外耗电。
> 这是移动网络功耗的关键特征。[文献178, 150]

**状态集合**：

$$\mathcal{S}_{RRC}=\{\text{IDLE},\text{CONN},\text{DCH}\}$$

**状态功耗**：

$$P_{cell}(t) = P_{\text{IDLE}}\mathbb{I}[s(t)=\text{IDLE}] + P_{\text{CONN}}\mathbb{I}[s(t)=\text{CONN}] + P_{\text{DCH}}\mathbb{I}[s(t)=\text{DCH}]$$
\tag{6.4-1}

**状态转移**（简化）：

$$
\begin{aligned}
\text{IDLE} &\xrightarrow{R_{data}>0} \text{DCH} \\
\text{DCH} &\xrightarrow{t>\tau_{tail}} \text{CONN} \\
\text{CONN} &\xrightarrow{t>\tau_{idle}} \text{IDLE}
\end{aligned}
\tag{6.4-2}
$$

其中$\tau_{tail}$为尾耗时间（4G典型5-12s，5G典型2-5s），$\tau_{idle}$为空闲回退时间。[文献150]

**吞吐量修正**：

$$P_{cell}(t)=P_{state}(s(t)) + k_{cell}R_{data}(t)$$
\tag{6.4-3}

> **解释**：
> - 低数据率时功耗主要由状态决定
> - 大数据率时线性项主导

**建议实现**：

- 用简单状态机记录最近一次蜂窝传输时刻
- 传输结束后进入尾耗计时
- 尾耗结束再回到低功耗状态

---

## 7. 传感器功耗模型

### 7.1 GPS功耗

$$\boxed{P_{GPS}(t) = \begin{cases}
0 & \text{关闭} \\
P_{GPS,cold} & \text{冷启动搜星} \\
P_{GPS,track} & \text{持续跟踪}
\end{cases}}$$

**参数**：

| 状态 | 功耗 [mW] | 持续时间 |
|------|-----------|----------|
| 关闭 | 0 | - |
| 冷启动 | 150-300 | 30-60s |
| 热启动 | 100-200 | 5-10s |
| 跟踪 | 50-150 | 持续 |
| 高精度 | 150-250 | 持续 |

### 7.2 IMU传感器（加速度计/陀螺仪）

$$P_{IMU} = P_{accel} + P_{gyro} + P_{mag}$$

| 传感器 | 功耗 [mW] | 采样率影响 |
|--------|-----------|------------|
| 加速度计 | 0.5-2 | 低 |
| 陀螺仪 | 3-10 | 中 |
| 磁力计 | 1-5 | 低 |
| 气压计 | 0.1-0.5 | 极低 |
| 接近传感器 | 1-5 | 低 |
| 环境光 | 0.1-0.5 | 极低 |

**采样率功耗关系**：
$$P_{sensor}(f_s) = P_{base} + k_s \cdot f_s$$

**文献依据**：论文165（SensingKit传感器功耗）、论文161（GPS功耗TMC）

---

## 8. 其他组件功耗

### 8.1 相机

| 模式 | 功耗 [mW] |
|------|-----------|
| 关闭 | 0 |
| 预览 | 300-500 |
| 拍照 | 500-800 |
| 录像(1080p) | 600-1000 |
| 录像(4K) | 1000-1500 |
| 闪光灯 | 1000-3000 (瞬时) |

### 8.2 音频

| 模式 | 功耗 [mW] |
|------|-----------|
| 静音 | 0 |
| 扬声器(低音量) | 50-100 |
| 扬声器(高音量) | 200-500 |
| 耳机 | 10-30 |
| 蓝牙音频 | 50-150 |
| 麦克风录音 | 20-50 |

### 8.3 振动马达

| 模式 | 功耗 [mW] | 持续时间 |
|------|-----------|----------|
| 短振 | 100-300 | 50-100ms |
| 长振 | 100-300 | 持续 |
| 触觉反馈 | 50-100 | 10-20ms |

---

## 9. 使用场景功耗汇总

### 9.1 典型场景功耗表

| 场景 | 总功耗 [mW] | 主要贡献 | 续航(3000mAh) |
|------|-------------|----------|---------------|
| **待机(屏幕关)** | 50-100 | 基带、后台 | 100+ h |
| **待机(屏幕亮)** | 400-600 | 屏幕 | 19-28 h |
| **阅读/浏览** | 800-1200 | 屏幕、CPU | 9.5-14 h |
| **社交媒体** | 1200-1800 | 屏幕、网络、CPU | 6.3-9.5 h |
| **视频播放(本地)** | 1000-1500 | 屏幕、解码 | 7.6-11 h |
| **视频流(WiFi)** | 1500-2200 | 屏幕、网络、解码 | 5.2-7.6 h |
| **视频通话** | 2000-3000 | 屏幕、网络、相机、CPU | 3.8-5.7 h |
| **导航(GPS)** | 2000-2500 | 屏幕、GPS、网络 | 4.6-5.7 h |
| **游戏(轻度)** | 2500-3500 | 屏幕、CPU、GPU | 3.3-4.6 h |
| **游戏(重度)** | 4000-6000 | 全组件 | 1.9-2.9 h |
| **拍照/录像** | 2000-3500 | 相机、屏幕、存储 | 3.3-5.7 h |

### 9.2 功耗分解示例

**场景：社交媒体浏览（1500mW总功耗）**

| 组件 | 功耗 [mW] | 占比 |
|------|-----------|------|
| 屏幕(50%亮度) | 600 | 40% |
| CPU(20%利用率) | 300 | 20% |
| WiFi(接收) | 200 | 13% |
| GPU(轻度) | 150 | 10% |
| 基础功耗 | 150 | 10% |
| 其他(传感器等) | 100 | 7% |
| **总计** | **1500** | **100%** |

**文献依据**：论文178（3W's）、论文278（完整手机功耗模型）

---

## 10. 完整功耗模型

### 10.1 连续时间功耗方程

$$\boxed{
\begin{aligned}
P_{total}(t) = & P_{base} \\
& + P_{display}(B(t), APL(t), f_{refresh}) \\
& + P_{CPU}(\mathbf{u}_{CPU}(t), \mathbf{f}_{CPU}(t)) \\
& + P_{GPU}(u_{GPU}(t), f_{GPU}(t)) \\
& + P_{network}(mode(t), RSRP(t), R_{data}(t), s_{RRC}(t)) \\
& + P_{GPS}(state_{GPS}(t)) \\
& + P_{sensors}(\mathbf{s}(t)) \\
& + P_{audio}(mode_{audio}(t)) \\
& + P_{camera}(mode_{camera}(t))
\end{aligned}
}$$

### 10.2 电流计算

从功耗计算放电电流（输入到电池模型）：

$$\boxed{I(t) = \frac{P_{total}(t)}{V(t)}}$$

其中 $V(t)$ 来自电池模型(01)的输出。

### 10.3 功耗-电流迭代

由于 $V(t)$ 依赖于 $I(t)$，需要迭代求解：

```
初始化: V = V_nominal
迭代:
    I = P_total / V
    V_new = V_OC(SOC) - I*R_0 - V_RC1 - V_RC2
    如果 |V_new - V| < ε: 收敛
    V = V_new
```

通常2-3次迭代即可收敛。

---

## 11. 与其他子模型的接口

| 接口 | 方向 | 变量 | 来源/去向 |
|------|------|------|-----------|
| 输入 | ← | $V(t)$ | 电池模型(01) |
| 输入 | ← | 使用场景参数 | 用户输入/假设 |
| 输出 | → | $I(t)$ | 电池模型(01) |
| 输出 | → | $P_{total}(t)$ | 热模型(03) |

---

## 12. 数值实现

### 12.1 Python实现

```python
def power_model(t, scenario, params):
    """
    计算总功耗
    
    scenario: dict containing component states
        - brightness: 0-1
        - cpu_util: 0-1
        - gpu_util: 0-1
        - network_mode: 'off'/'wifi'/'4g'/'5g'
        - gps_state: 'off'/'tracking'
        - ...
    """
    P = params['P_base']
    
    # 显示屏
    if scenario['screen_on']:
        if params['display_type'] == 'OLED':
            P += params['P_display_base'] + params['k_display'] * scenario['brightness'] * scenario['apl']
        else:  # LCD
            P += params['P_backlight_max'] * scenario['brightness'] + params['P_driver']
    
    # CPU
    P += params['P_cpu_idle'] + scenario['cpu_util'] * params['P_cpu_max'] * (scenario['cpu_freq']/params['cpu_freq_max'])**3
    
    # GPU
    P += scenario['gpu_util'] * params['P_gpu_max'] * (scenario['gpu_freq']/params['gpu_freq_max'])**2
    
    # 网络
    if scenario['network_mode'] == 'wifi':
        P += params['P_wifi_idle'] + params['k_wifi'] * scenario['data_rate']
    elif scenario['network_mode'] in ['4g', '5g']:
        # 简化RRC状态机
        state = scenario['rrc_state']  # 'IDLE'/'CONN'/'DCH'
        P_state = params['P_rrc'][state]
        P += P_state + params['k_cell'] * scenario['data_rate']
    
    # GPS
    if scenario['gps_state'] == 'tracking':
        P += params['P_gps_track']
    
    # 传感器
    P += sum(params['P_sensor'][s] for s in scenario['active_sensors'])
    
    return P  # mW

def compute_current(P_total, V):
    """计算放电电流"""
    return P_total / V / 1000  # mW/V -> A
```

### 12.2 场景定义

```python
# 预定义使用场景
SCENARIOS = {
    'idle_screen_off': {
        'screen_on': False,
        'cpu_util': 0.02,
        'gpu_util': 0,
        'network_mode': 'off',
        'gps_state': 'off',
        'active_sensors': []
    },
    'social_media': {
        'screen_on': True,
        'brightness': 0.5,
        'apl': 0.4,
        'cpu_util': 0.20,
        'cpu_freq': 1.5e9,
        'gpu_util': 0.10,
        'gpu_freq': 0.5e9,
        'network_mode': 'wifi',
        'data_rate': 5,  # Mbps
        'gps_state': 'off',
        'active_sensors': ['accelerometer']
    },
    'gaming_heavy': {
        'screen_on': True,
        'brightness': 0.8,
        'apl': 0.6,
        'cpu_util': 0.85,
        'cpu_freq': 2.8e9,
        'gpu_util': 0.90,
        'gpu_freq': 0.9e9,
        'network_mode': 'wifi',
        'data_rate': 10,
        'gps_state': 'off',
        'active_sensors': ['accelerometer', 'gyroscope']
    }
}
```

---

## 13. 模型验证

### 13.1 验证方法

1. **组件级验证**：使用功率监测工具(PowerTutor, Battery Historian)
2. **场景级验证**：对比文献测量数据
3. **端到端验证**：对比实际续航时间

### 13.2 预期精度

| 级别 | 误差范围 |
|------|----------|
| 组件级 | ±20% |
| 场景级 | ±15% |
| 平均功耗 | ±10% |

---

## 参考文献

1. **论文278**: IEEE Access完整智能手机功耗模型
2. **论文178**: UCSD 3W's功耗测量
3. **论文174**: AndroWatts组件功耗分解
4. **论文181**: 功耗建模方法综述(Wiley)
5. **论文09**: 多核CPU功耗模型
6. **论文13**: GPU功耗建模
7. **论文149**: WiFi功耗模型(ICDCS)
8. **论文161**: GPS功耗建模(TMC)
9. **论文221**: 5G功耗测量(SIGCOMM)
10. **论文150**: WiFi/蜂窝功耗与尾耗分析(WoWMoM)

---

*文档版本: v1.0*
*创建时间: 2026年1月31日*
*上一步: 01_battery_model.md*
*下一步: 03_thermal_model.md - 温度耦合模型*
