# Magnetic field sensing of inhomogeneous degradation in Lithium-ion batteries with spatio-temporal evolution  
利用磁场传感技术检测锂离子电池时空演化过程中不均匀的退化现象

Author links open overlay panelQirui Wang 1  
王其锐 1​, Jie Gao 2  
捷高 2 号, Lei Mao 3  
雷猫 3 号, Yan Lyu 2  
严吕 2

Show more  显示更多

Add to Mendeley  添加到 Mendeley

Share  分享

Cite  引

[https://doi.org/10.1016/j.ensm.2026.104933](https://doi.org/10.1016/j.ensm.2026.104933 "Persistent link using digital object identifier")[Get rights and content  获取版权和内容](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S2405829726000668&orderBeanReset=true)

## Abstract  抽象的

Inhomogeneous degradation is a critical factor leading to performance decay and safety risks in lithium-ion batteries. Multi-regional physical information of Lithium-ion batteries facilitates the analysis of inhomogeneous degradation processes, yet its spatio-temporal evolution remains challenging to probe non-invasively. In this study, a magnetic field sensing methodology is proposed to map and analyze regional degradation with spatio-temporal evolution. A Regional Magnetic Feature Selection and Integration (RMFSI) strategy was developed to construct an optimized magnetic feature matrix that shows strong correlation with the state of health (SOH). Then, a quantitative link between macroscopic magnetic response and electrochemical degradation was established through differential magnetic capacity (dB/dV) analysis. Moreover, spatio-temporal evolution mapping of regional magnetic fields revealed a progressive behavior from localized failure to widespread, inhomogeneous degradation throughout the cell. The heightened sensitive response for regions identified by this approach was finally validated by post-mortem scanning electron microscopy (SEM) analysis. It provides a non-invasive methodology for elucidating dynamic degradation, which is promising for early safety warnings and spatial management strategies in future battery systems.  
锂离子电池中非均匀退化是导致性能衰减和安全风险的关键因素。锂离子电池的多区域物理信息有助于分析非均匀退化过程，但其时空演化过程的非侵入式探测仍然具有挑战性。本研究提出了一种磁场传感方法，用于绘制和分析具有时空演化的区域退化图。我们开发了一种区域磁特征选择与集成（RMFSI）策略，构建了一个与电池健康状态（SOH）高度相关的优化磁特征矩阵。然后，通过微分磁容量（dB/dV）分析，建立了宏观磁响应与电化学退化之间的定量联系。此外，区域磁场的时空演化映射揭示了从局部失效到整个电池范围内广泛非均匀退化的渐进行为。最后，通过电池失效后的扫描电子显微镜（SEM）分析验证了该方法识别出的区域具有更高的灵敏度。它提供了一种非侵入式方法来阐明动态退化，这有望用于未来电池系统的早期安全预警和空间管理策略。

## Introduction  介绍

Lithium-ion batteries currently dominate the electrochemical energy storage landscape due to their high energy density, extended cycle life, and superior storage capabilities [1]. Inhomogeneous degradation is a critical factor leading to performance decay and safety hazards in lithium-ion batteries, which is predominantly attributed to uneven electrochemical reactions. It may originate from multiple sources, such as electrode material defects, non-uniform formation of the solid electrolyte interphase (SEI), spatially inhomogeneous current distribution, and mechanically induced stresses during cycling [2,3]. These inhomogeneities can cause localized overcharging or over-discharging of local regions, leading to lithium plating and even local material failure. Consequently, rapid performance degrades in local regions and poses significant safety hazards [4]. Monitoring and analyzing spatio-temporal inhomogeneous degradation in batteries is critical to enable early safety warnings at localized weak points and provide foundational insights to optimize battery design and management.  
锂离子电池凭借其高能量密度、长循环寿命和优异的存储性能，目前在电化学储能领域占据主导地位[1]。锂离子电池性能衰减和安全隐患的关键因素是非均匀衰减，这主要归因于电化学反应的不均匀性。非均匀衰减可能源于多种因素，例如电极材料缺陷、固体电解质界面（SEI）形成不均匀、空间电流分布不均匀以及循环过程中机械应力[2,3]。这些不均匀性会导致局部区域过充或过放，进而导致锂沉积甚至局部材料失效。因此，局部区域的性能会迅速下降，并构成严重的安全隐患[4]。监测和分析电池时空非均匀衰减对于在局部薄弱环节发出早期安全预警以及为优化电池设计和管理提供基础性见解至关重要。

The State of Health (SOH) was used to track the cell-wide degradation progress and provide a timeline for analyzing the regional inhomogeneity. The characterization of degradation by electricity is dominant in both research and industrial practice. Zhang et al. developed a hybrid model integrating fractional-order derivative theory with machine learning algorithms, achieving high-precision SOH evaluation [5]. Wan et al. introduced a novel co-prediction method for SOH and remaining useful life based on short-term relaxation voltage, attaining SOH estimation errors below 1.6%. This approach was further adapted to diverse batteries through a transfer learning framework [6]. Gong et al. incorporated battery swelling stress as supplementary to voltage, utilizing Long Short-Term Memory (LSTM) networks to capture the relationship between mechanical deformation and aging [7]. Liu et al. proposed a multi-time-resolution feature extraction method with interactive learning, thereby improving SOH estimation precision [8]. While highly adaptive data-driven approaches represent vital options for battery degradation prediction, reliance solely on electrical parameters (e.g., current, voltage, internal resistance) generally is unable to provide spatially resolved insight into the battery condition and detect subtle local electrochemical variations. Consequently, the application is limited in early warning of localized failure.  
电池健康状态 (SOH) 用于追踪电池整体的退化进程，并为分析区域不均匀性提供时间线。在研究和工业实践中，利用电能表征退化是主流方法。Zhang 等人开发了一种混合模型，将分数阶导数理论与机器学习算法相结合，实现了高精度的 SOH 评估 [5]。Wan 等人提出了一种基于短期弛豫电压的 SOH 和剩余使用寿命联合预测新方法，SOH 估计误差低于 1.6%。该方法通过迁移学习框架进一步应用于多种电池 [6]。Gong 等人将电池膨胀应力作为电压的补充，利用长短期记忆 (LSTM) 网络捕捉机械变形与老化之间的关系 [7]。Liu 等人提出了一种具有交互式学习的多时间分辨率特征提取方法，从而提高了 SOH 估计精度 [8]。虽然高度自适应的数据驱动方法是电池衰减预测的重要选择，但仅仅依赖电参数（例如电流、电压、内阻）通常无法提供电池状态的空间分辨信息，也无法检测到细微的局部电化学变化。因此，这种方法在局部故障的早期预警方面应用有限。

Despite the inhomogeneous distribution of lithium-ion investigated via neutron diffraction [9], scanning transmission electron microscopy [10], and Raman mapping [11], these techniques face limitations in cost and technical feasibility, resulting in unsuitable online detection. Recent research focuses on exploiting battery swelling characteristics to study inhomogeneous aging behavior. However, it suffers from spatial resolution constraints and multiple-factor interference, restricting practical implementation in quantifying the degradation degree assessment [12,13]. Ultrasonic detection techniques offer promising alternatives by capturing dynamic evolution in electrode mechanical properties (e.g., elastic modulus, density) during lithium intercalation. Davies et al. achieved precise degradation prediction related to cycling by integrating machine learning with ultrasonic signals [14]. Williams et al. [15] revealed a strong nonlinear correlation between SOH decline, primarily caused by lithium inventory loss, and reduced ultrasonic time-of-flight. Ultrasonic guided wave technology further demonstrates potential for spatially resolved battery status detection. Robinson et al. [16] identified electrode attenuation during charging via regional acoustic variations, confirming spatially inhomogeneous degradation. Huang et al. [17] implemented multi-region inhomogeneous state of charge (SOC) visualization using global-focused scanning of ultrasonic signals. Our prior numerical studies established strong correlations between SOC and multi-mode dispersion curves, and subsequent multi-region experiments revealed significant ultrasonic response variations across regions and operational stages [18,19]. Ultrasonic technology has been reported for detecting SOC, SOH, and defects including gas evolution [20], electrolyte wetting state [21], and lithium deposition [22,23]. Although it provides distinct advantages in space for inhomogeneous degradation analysis, he accuracy and reliability of measurement are affected by the sensitivity to sensor installation and environmental noise [24].

Magnetic characterization technology is an ideal candidate because of its high sensitivity to current distribution and non-contact characteristics. Current density distribution is utilized as a medium to establish a spatial mapping relationship between the magnetic field and battery degradation [25]. Further, the local current distribution resulting from inhomogeneous degradation can be captured by a magnetic field sensor. Zhao et al. simulated magnetic field distributions under diverse localized anomalies, validating the feasibility of early-stage micro-short circuit detection [26]. Bason et al. drew cell magnetic fields and reconstructed current density images through inverse analysis [27]. Matsuda et al. visualized and monitored short-circuit regions by correlating magnetic field variations with conductivity distribution changes [28]. Chen et al. generated multi-region magnetic field images during battery operation, enabling fault localization and classification via anomalous field [29]. Lee et al. achieved real-time current distribution imaging through magnetic field analysis for spatially resolved failure detection [30]. Wang et al. tracked and visualized magnetic field variations from unbalanced cell currents to characterize capacity inconsistency [31]. These studies demonstrate the spatial diagnostic capability of magnetic characterization, but the focus remains predominantly on fault diagnosis and localization. Although Javadipour et al. correlated degradation-induced current density distributions with magnetic fields for SOH evaluation, there was no systematic exploration for resolving the dynamic evolution of degradation inhomogeneities throughout the entire battery lifecycle [32,33].

In summary, a critical gap remains in exploring the dynamic evolution of inhomogeneous degradation by magnetic characterization. Different from existing magnetic characterization studies that primarily focus on the localization and diagnosis of pre-defined localized faults, this work introduces a magnetic field methodological framework developed to achieve spatio-temporal monitoring of inhomogeneous degradation shown in Fig.1, which is also a vital supplementary dimension to traditional electrical detection technologies. First, a multi-sensor fluxgate array is employed to construct a magnetic field imaging system, capturing spatial magnetic information reflecting local current density distributions and establishing a foundational dataset for spatial analysis. Subsequently, because multi-component magnetic data exhibit varying sensitivities to degradation across regions, multiple magnetic field information is integrated by RMFSI to capture regional degeneration signals robustly. What’s more, the core RMFSI strategy can be adaptively replaced with more advanced method tailored to different battery chemistries and magnetic datasets. Further, for bridging macroscopic magnetic information with underlying electrochemical mechanisms, a quantitative correlation is established between magnetic field response (dB/dV) and electrochemical degradation modes (dQ/dV). Finally, the proposed methodology is applied to analyze spatio-temporal evolution of degeneration inhomogeneity, achieving spatio-temporal dynamic tracking and discussing the dominant degradation mechanisms. Besides, the severe localized degradation in near-tab areas as inferred from the magnetic data, is validated through post-mortem scanning electron microscopy (SEM) analysis.

## Section snippets

## Magnetic field information in different regions

Customized LiCoO₂/graphite (LCO) pouch lithium-ion batteries served as experimental samples, with approximately 5700 mAh capacity and 125 mm × 78 mm dimensions. The cathode consists of LiCoO2 with a volume fraction of 97.2% and a single-layer thickness of 46.5 μm, while the anode comprises graphite with a volume fraction of 95.7% and a single-layer thickness of 65.5 μm. The current collector thicknesses of Al and Cu are 12 μm and 6 μm, respectively. A conventional polyethylene separator with a

## Conclusion

This research presents a magnetic field sensing methodology for non-destructive, spatio-temporal monitoring of inhomogeneous degradation in pouch lithium-ion batteries. Magnetic field information was captured using a multi-sensor fluxgate array throughout the degradation process. The RMFSI strategy was employed to integrate multi-dimensional magnetic information into a robust feature matrix that exhibits a strong correlation with the SOH of the battery. The correlation between the magnetic

## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work the authors used Gemini/deepseek in order to improve the language and readability of the manuscript. After using this tool/service, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

## Uncited References

[49]

## CRediT authorship contribution statement

**Qirui Wang:** Writing – original draft, Methodology, Investigation, Conceptualization. **Jie Gao:** Validation, Software, Investigation, Funding acquisition, Data curation. **Lei Mao:** Supervision, Resources. **Yan Lyu:** Writing – review & editing, Visualization, Supervision, Project administration, Methodology.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work is supported by National natural Science Foundation of China (No.12402216).

We would like to express our gratitude to the Measurement, Control and Information Processing Group, University of Science and Technology of China, for their invaluable assistance in this research.

## Reference (49)

- S. Fang _et al._
    
    ### [Cell design and image analysis for in situ Raman mapping of inhomogeneous state-of-charge profiles in lithium-ion batteries[J]](https://www.sciencedirect.com/science/article/pii/S0378775317303531)
    
    ### Journal of Power Sources
    
    (2017)
    
- X. Zhang _et al._
    
    ### [A novel method for state of health estimation of lithium-ion batteries based on fractional-order differential voltage-capacity curve[J]](https://www.sciencedirect.com/science/article/pii/S0306261924017872)
    
    ### Applied Energy
    
    (2025)
    
- F. Wan _et al._
    
    ### [Prediction of state-of-health and remaining useful life for lithium-ion batteries using short-term relaxation voltage[J]](https://www.sciencedirect.com/science/article/pii/S2352152X25021103)
    
    ### Journal of Energy Storage
    
    (2025)
    
- R. Liu _et al._
    
    ### [A multi-time-resolution attention-based interaction network for co-estimation of multiple battery states[J]](https://www.sciencedirect.com/science/article/pii/S0306261924024814)
    
    ### Applied Energy
    
    (2025)
    
- M J Mühlbauer _et al._
    
    ### [Effect of fatigue/ageing on the lithium distribution in cylinder-type Li-ion batteries[J]](https://www.sciencedirect.com/science/article/pii/S0378775317302616)
    
    ### Journal of power sources
    
    (2017)
    
- S. Fang _et al._
    
    ### [Cell design and image analysis for in situ Raman mapping of inhomogeneous state-of-charge profiles in lithium-ion batteries[J]](https://www.sciencedirect.com/science/article/pii/S0378775317303531)
    
    ### Journal of Power Sources
    
    (2017)
    
- F. Brauchle _et al._
    
    ### [Spatially resolved degradation and inhomogeneity analysis of lithium-ion pouch cells using an array of eddy-current sensors[J]](https://www.sciencedirect.com/science/article/pii/S2352152X24003244)
    
    ### Journal of Energy Storage
    
    (2024)
    
- D. Williams _et al._
    
    ### [Battery age monitoring: Ultrasonic monitoring of ageing and degradation in lithium-ion batteries[J]](https://www.sciencedirect.com/science/article/pii/S0378775325000102)
    
    ### Journal of Power Sources
    
    (2025)
    
- J. Gao _et al._
    
    ### [Guided waves propagation in lithium-ion batteries: Theoretical modeling and experimental analysis[J]](https://www.sciencedirect.com/science/article/pii/S0963869524000677)
    
    ### NDT & E International
    
    (2024)
    
- X. Lin _et al._
    
    ### [Thermoelastic guided wave behavior modeling and distributed experimental analysis of the inhomogeneous state of charge for silicon carbon lithium-ion batteries[J]](https://www.sciencedirect.com/science/article/pii/S2352152X25006097)
    
    ### Journal of Energy Storage
    
    (2025)
    

View more references

## Cited by (0)

[View full text](https://www.sciencedirect.com/science/article/pii/S2405829726000668)

© 2026 Published by Elsevier B.V.

## Recommended articles

No articles found.  未找到文章。

[![Elsevier logo with wordmark](https://www.sciencedirect.com/shared-assets/47/images/elsevier-non-solus-new-with-wordmark.svg)](https://www.elsevier.com/)

- [About ScienceDirect](https://www.elsevier.com/solutions/sciencedirect)
- [Remote access](https://www.sciencedirect.com/user/institution/login?targetURL=%2Fscience%2Farticle%2Fpii%2FS2405829726000668)
- [Contact and support](https://service.elsevier.com/ci/pta/login/redirect/contact/supporthub/sciencedirect/p_li/ZGV7PPcYjEOgD54VjyfXqn1Y1O6yTWNsh2jeEHPptZfqjk9kr0oicgnjScVnsVoJ_nk9uB0bsm1ysXcCIKIR_NRhzrq6HBf2bQ7qg~HiZmn~yTzAFXTmg60wDnPoA1L5D1NXHNStam9mCEEHnVIqnucltYao7xVvDsLZqeEHdC8hm8vJuS9xjFACA1khlfJXQIuUbVAAJLJ1MK~qmtO0HWoYC9v4aV42SJlafO58LO6niOj0Ariix1yRJMy6kZ5e~uO_UPcM79egFx7zk7rgMmJ9_uI1B77uNsdSmyE6dzAYjMzzlixXOM~_k5wOJDfOBDSJh7KRDK0YvfYzm~E~DkOy4RWFsLA4KCEnXx5tVfs_TTpC2WEe2avW_izejtQGcyxnqp2hiS62q56JBgCkWIqi4fRxK6Z7vpaTn3MGsup2AbfKBsk6r0qSdzZ47WNAtYg8HeRzyBejU6QMKjL2YA**)
- [Terms and conditions](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions)
- [Privacy policy](https://www.elsevier.com/legal/privacy-policy)
- Cookie settings

All content on this site: Copyright © 2026 Elsevier B.V., its licensors, and contributors. All rights are reserved, including those for text and data mining, AI training, and similar technologies. For all open access content, the relevant licensing terms apply.

[![RELX group home page](https://www.sciencedirect.com/shared-assets/60/images/logo-relx-tm.svg)](https://www.relx.com/)