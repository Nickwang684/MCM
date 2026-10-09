# Embedded sensing: The neural frontier and early-warning revolution in battery safety monitoring  
嵌入式传感：电池安全监测的神经前沿与早期预警革命

Author links open overlay panelSheng Guo a  盛国 a, [Hao Luo a](https://www.sciencedirect.com/author/57213205900/hao-luo)  , 洛浩 a , Zhe Gao a  哲高 a, Yizheng Ding a, Shiwen Wang b  石 wen 王 b, Pengcheng Wang b, Feihong Wang c  王飞鸿 c, Jizhong Cao c  曹吉中 c, Yajie Song d  宋亚杰 d, Ning Ren e  任宁 e, [Mi Lu a](https://www.sciencedirect.com/author/22985771700/mi-lu)  , 吕密 a 

Show more  显示更多

Add to Mendeley  添加到 Mendeley

Share  分享

Cite  引用

[https://doi.org/10.1016/j.ensm.2025.104582](https://doi.org/10.1016/j.ensm.2025.104582 "Persistent link using digital object identifier")[Get rights and content  获取权限和内容](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S240582972500580X&orderBeanReset=true)

## Highlights  亮点

- •
    
    The review identifies critical challenges of embedded sensors in batteries: material compatibility, miniaturization, and multidimensional sensing.  
    综述指出了电池中嵌入式传感器的关键挑战：材料兼容性、微型化和多维传感。
    
- •
    
    Highlights recent advances in thermocouple, fiber-optic, and thin-film sensors for in-situ battery safety monitoring.  
    概述了热电偶、光纤和薄膜传感器在原位电池安全监测方面的最新进展。
    
- •
    
    System-level integration of intelligent, multifunctional sensors for safety monitoring and early warning is proposed.  
    提出了用于安全监测和早期预警的智能、多功能传感器的系统级集成方案。
    

## Abstract  摘要

The rapid proliferation of battery systems has positioned thermal runaway prevention as a crucial technological imperative. In-situ sensor-based monitoring frameworks enable real-time tracking of internal parameters, thereby providing early warnings and interventions for thermal management. However, conventional sensors, limited by their unidimensional architectures, struggle to accurately capture the intricate interplay among thermal, mechanical, and chemical fields. This limitation results in significant blind spots when predicting battery degradation under multiphysics conditions over the entire lifecycle. Consequently, advancing multi-parameter sensing technologies and developing multidimensional sensing architectures become essential for achieving comprehensive battery safety monitoring. From an embedded sensing perspective, this review systematically examines critical challenges related to chemical compatibility, measurement accuracy, and multi-parameter monitoring encountered during sensor integration. It provides a detailed elaboration on the operating principles and practical applications of thermocouples, optical fiber sensors, and thin-film sensors in batteries. To address technological bottlenecks, such as risks to structural integrity, electrolyte-induced performance degradation, and limitations in single-parameter monitoring, we propose strategies that include sensor miniaturization, the selection of chemically robust materials, integrated multidimensional in-situ platforms, and the incorporation of artificial intelligence (AI) technologies. This review advances comprehensive understanding of battery multidimensional sensing systems, significantly enhancing active safety engineering and multiphysics diagnostic frameworks.  
电池系统的迅速普及将热失控预防定位为关键技术需求。原位传感器基监测框架能够实时跟踪内部参数，从而提供热管理的早期预警和干预。然而，传统传感器受限于其一维架构，难以准确捕捉热、机械和化学场之间的复杂交互作用。这种限制在多物理场条件下整个生命周期内预测电池退化时产生了显著的盲区。因此，推进多参数传感技术和开发多维传感架构对于实现全面的电池安全监测变得至关重要。从嵌入式传感的角度来看，本文系统地探讨了传感器集成过程中遇到的化学兼容性、测量准确性和多参数监测的关键挑战。详细阐述了热电偶、光纤传感器和薄膜传感器在电池中的工作原理及其实际应用。 为解决技术瓶颈，如结构完整性风险、电解液引起的性能退化以及单一参数监测的局限性，我们提出了包括传感器微型化、选择化学稳定材料、集成多维原位平台以及引入人工智能（AI）技术在内的策略。本综述推进了对电池多维传感系统的全面理解，显著增强了主动安全工程和多物理场诊断框架。

## Graphical abstract  图形摘要

This review presents a comprehensive summary of the research advancements in embedded sensor technologies, including thermocouples, light sensors, and thin-film sensors. It further elaborates on the key challenges currently facing the development of embedded sensing systems, as well as their interdisciplinary nature and diverse applications in battery safety technology.  
本综述全面总结了嵌入式传感器技术的研究进展，包括热电偶、光传感器和薄膜传感器。此外，还详细阐述了嵌入式传感系统当前面临的诸多挑战，以及它们的跨学科性质和在电池安全技术中的多样应用。

![Image, graphical abstract](https://ars.els-cdn.com/content/image/1-s2.0-S240582972500580X-ga1.jpg)

1. [Download: Download high-res image (394KB)](https://ars.els-cdn.com/content/image/1-s2.0-S240582972500580X-ga1_lrg.jpg "Download high-res image (394KB)")
2. [Download: Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S240582972500580X-ga1.jpg "Download full-size image")

## Introduction

Lithium-ion batteries (LIBs), widely recognized for their high energy density, excellent efficiency, and extended cycle life, have emerged as the predominant energy sources for electric transportation and large-scale energy storage systems [[1], [2], [3], [4], [5], [6], [7]]. However, persistent safety issues such as thermal runaway, [[8], [9], [10], [11]] reduced performance at low temperatures, [[12], [13], [14]] and structural degradation induced by temperature fluctuations [[15], [16], [17], [18]] continue to present significant challenges to their reliable and widespread deployment. These challenges originate from the complex physicochemical processes that occur during charging and discharging; even minor deviations from the intended electrochemical pathways may initiate a cascade of failures, including internal short circuits, [[19], [20], [21]] gas generation, [[22], [23], [24], [25]] and the formation of lithium dendrites [26,27]. Among the numerous factors influencing battery performance, temperature plays a pivotal role, directly affecting safety, durability, and operational efficiency. Consequently, high-precision real-time temperature monitoring, coupled with timely assessment of interrelated parameters such as mechanical stress, is essential for accurate fault diagnosis and proactive safety management.

Embedded sensing technology has emerged as a promising approach for in-situ, high-resolution monitoring of internal temperature variations, stress development, and gas emission. In contrast to conventional external diagnostic methods, embedded sensors provide direct contact with electrodes and electrolytes, allowing for the detection of subtle transient events with minimal spatial and temporal dela [28,29]. By integrating high-precision sensing components, these systems are capable of detecting subtle temperature changes, minor pressure fluctuations, and rapid gas release events with remarkable sensitivity [30,31]. This functionality enables the conversion of otherwise undetectable internal processes into continuous and quantifiable data streams, thereby supporting advanced data analysis, real-time diagnostics, and the development of customized health profiles that provide comprehensive insights into the dynamic internal states under varying operational and environmental conditions. The resulting data not only serves as a foundation for optimizing material and structural design but also allows for the early detection of emerging failure mechanisms, facilitating prompt countermeasures such as thermal regulation, circuit disconnection, or other protective strategies to prevent severe incidents [32,33]. When integrated with edge-computing diagnostic modules, system response latency can be reduced to the millisecond level, representing a significant advancement in real-time risk mitigation [34,35]. Collectively, these advancements highlight the inherently interdisciplinary character of embedded battery sensing, which integrates concepts from materials science, microelectronics, data analytics, and intelligent systems engineering (Fig. 1). Nonetheless, the large-scale implementation of embedded sensing technology remains hindered by interconnected challenges, such as the demand for miniaturized and mechanically durable architectures, sustained stability in harsh chemical and thermal environments, the difficulty of decoupling signals from coupled thermal–mechanical–electrochemical interactions, and the necessity to reduce processing latency to enable prompt protective responses. Addressing these obstacles is critical for advancing embedded sensing from laboratory-scale prototypes to commercially viable and field-deployable safety solutions [36].

Most existing reviews have focused on individual sensing modalities or isolated performance metrics, lacking a systematic comparison of the capabilities of different embedded sensing technologies under coupled multi-physical-field operating conditions. In contrast, this review provides a comparative evaluation of three representative embedded sensing methodologies—thermocouples, optical fiber sensors, and thin-film sensors—within the context of battery safety. It presents an in-depth analysis of their fundamental sensing principles and practical implementations, along with a comprehensive overview of recent advancements in utilizing these technologies to improve battery safety performance. Furthermore, this paper investigates the application of artificial intelligence technology in the field of battery safety and presents a comprehensive comparative analysis with embedded sensing technology. Beyond summarizing recent progress, this review critically examines the primary technical challenges that limit the effectiveness of embedded sensing in battery systems and investigates novel strategies with the potential to advance the field. Furthermore, it outlines emerging trends and key research priorities. This comprehensive perspective aims to guide the development of next-generation battery safety architectures that are inherently safer, more intelligent, and more resilient.

## Section snippets

## The evolution of sensor technology

Battery monitoring technologies have experienced continuous evolution and refinement, shifting from external measurement to increasingly sophisticated internal monitoring. To more clearly illustrate this progression, Fig. 2 provides a chronological summary of the key milestones.

Initially, battery monitoring primarily depended on fundamental instruments such as hydrometers [37] and optical hydrometers, [38] which were only capable of providing rough estimates of battery parameters. These

## The utilization of thermocouple-based sensing technology for battery temperature monitoring

Thermocouple operates based on the thermoelectric effect, wherein two dissimilar homogeneous conductors form a closed circuit. When a temperature gradient is established between their junctions, a current is induced, resulting in the generation of a Seebeck voltage, or thermoelectric potential, across the loop. As a temperature-sensing device, thermocouples convert thermal gradients into measurable electrical signals. When integrated with a signal acquisition and demodulation system, the

## The implementation of optical fiber sensing technology for monitoring battery parameters

Optical fiber sensing serves as a highly effective diagnostic technique, utilizing the light propagation characteristics within optical fibers to detect subtle changes in physical parameters with high sensitivity and precision. By analyzing optical phenomena such as reflection, interference, diffraction, and scattering, optical fiber sensors enable high-resolution measurements of temperature, pressure, strain, and other critical parameters. As highlighted by Li et al. [29], next-generation

## Investigation into the application of thin-film sensors for battery safety monitoring

Contemporary methods for monitoring the internal conditions of LIBs primarily depend on optical fiber and conventional rigid sensors, both of which may substantially interfere with the internal electrochemical processes. In contrast, thin-film sensors have gained attention as a viable alternative for integration into battery systems. This is attributed to their minimal influence on stress-induced lithium plating, relatively low fabrication costs, and significant flexibility in material design.

## Machine learning technology predicts battery safety status

In recent years, ML has become a key enabler in the fields of battery health management and performance prognostics. Accurate estimation of the SOH and remaining useful life (RUL) plays a crucial role in ensuring battery safety, reliability, and efficient utilization. Through the analysis of historical datasets, ML algorithms are capable of identifying complex performance degradation patterns under various operational conditions, thereby facilitating high-precision state monitoring and

## Future perspective

The Battery 2030+ Roadmap, launched by the European Union, outlines a vision for next-generation batteries equipped with an advanced network of embedded sensors to enable accurate and real-time signal acquisition. The realization of this vision necessitates the seamless integration of intelligent functionalities—such as high-precision sensing and diagnostic capabilities—directly within battery architectures. These embedded technologies are expected to enable batteries to autonomously monitor

## CRediT authorship contribution statement

**Sheng Guo:** Writing – review & editing, Writing – original draft, Software, Investigation, Formal analysis, Data curation. **Hao Luo:** Writing – review & editing, Supervision, Methodology, Investigation, Funding acquisition. **Zhe Gao:** Writing – review & editing, Software, Investigation, Data curation. **Yizheng Ding:** Software, Investigation, Data curation. **Shiwen Wang:** Software, Investigation, Data curation. **Pengcheng Wang:** Software, Formal analysis, Data curation. **Feihong Wang:** Methodology,

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was supported by the Significant Science and Technology Project in Xiamen (Future Industry field) (No. 3502Z20231057, 3502Z20241032, 3502Z20254009), the Natural Science Foundation of Fujian Province (No. 2024J011210)

## References (272)

- B. Nykvist _et al._
    
    ### [The feasibility of heavy battery electric trucks](https://www.sciencedirect.com/science/article/pii/S2542435121001306)
    
    ### Joule
    
    (2021)
    
- X. Feng _et al._
    
    ### [Thermal runaway mechanism of lithium ion battery for electric vehicles: a review](https://www.sciencedirect.com/science/article/pii/S2405829716303464)
    
    ### Energy Storage Mater.
    
    (2018)
    
- X. Feng _et al._
    
    ### [Mitigating thermal runaway of lithium-ion batteries](https://www.sciencedirect.com/science/article/pii/S254243512030088X)
    
    ### Joule
    
    (2020)
    
- Y. Zheng _et al._
    
    ### [Thermal state monitoring of lithium-ion batteries: progress, challenges, and opportunities](https://www.sciencedirect.com/science/article/pii/S0360128523000503)
    
    ### Prog. Energy Combust. Sci.
    
    (2024)
    
- J. Bang _et al._  J. Bang 等人
    
    ### [Rapid thermal runaway detection of lithium-ion battery via swelling-based state-of-charge monitoring using piezoresistive sponge sensor  
    基于膨胀状态估计的锂离子电池快速热失控检测方法：压阻海绵传感器](https://www.sciencedirect.com/science/article/pii/S2590116825000116)
    
    ### Etransportation  E 运输
    
    (2025)
    
- X. Hu _et al._  胡翔等
    
    ### [Battery warm-up methodologies at subzero temperatures for automotive applications: recent advances and perspectives  
    汽车应用中零下温度下的电池预热方法：近期进展与展望](https://www.sciencedirect.com/science/article/pii/S0360128519301169)
    
    ### Prog. Energy Combust. Sci.  
    Prog. 能源与燃烧学
    
    (2020)
    
- J. Zhu _et al._  J. 朱等
    
    ### [An improved electro-thermal battery model complemented by current dependent parameters for vehicular low temperature application  
    适用于车辆低温应用的改进电热电池模型，包含电流依赖参数](https://www.sciencedirect.com/science/article/pii/S0306261919307093)
    
    ### Appl. Energy  应用能源
    
    (2019)
    
- G. Zhu _et al._  朱光等.
    
    ### [Materials insights into low-temperature performances of lithium-ion batteries  
    锂离子电池低温性能的材料见解](https://www.sciencedirect.com/science/article/pii/S0378775315303153)
    
    ### J. Power. Sources.  电化学学报.
    
    (2015)
    
- X. Lin _et al._  林欣等.
    
    ### [Lithium plating mechanism, detection, and mitigation in lithium-ion batteries  
    锂离子电池的锂枝晶成因、检测与抑制](https://www.sciencedirect.com/science/article/pii/S0360128521000514)
    
    ### Prog. Energy Combust. Sci.
    
    (2021)
    
- H. Luo _et al._   Luo et al.
    
    ### [Diversified battery recycling: advances in recovery techniques and value-added functional applications  
    多元化电池回收：回收技术与增值功能应用进展](https://www.sciencedirect.com/science/article/pii/S2211285525003325)
    
    ### Nano Energy  纳米能源
    
    (2025)
    

View more references  查看更多参考文献

## Cited by (0)

[View full text  全文](https://www.sciencedirect.com/science/article/pii/S240582972500580X)

© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.  
© 2025 Elsevier B.V. 保留所有权利，包括文本和数据挖掘、AI 训练等类似技术的权利。

## Recommended articles

No articles found.  未找到相关文章。

## Article Metrics

### Captures  捕捉

- Mendeley Readers  Mendeley 阅读19

### Mentions  提及

- News Mentions  新闻提及1

![PlumX Metrics Logo](https://cdn.plu.mx/3ba727faf225e19d2c759f6ebffc511d/plumx-logo.png)[View details  查看详细信息](https://plu.mx/plum/a/?doi=10.1016%2Fj.ensm.2025.104582&theme=plum-sciencedirect-theme&hideUsage=true)

[![Elsevier logo with wordmark](https://www.sciencedirect.com/shared-assets/47/images/elsevier-non-solus-new-with-wordmark.svg)](https://www.elsevier.com/)

- [About ScienceDirect](https://www.elsevier.com/solutions/sciencedirect)
- [Remote access](https://www.sciencedirect.com/user/institution/login?targetURL=%2Fscience%2Farticle%2Fpii%2FS240582972500580X)
- [Contact and support](https://service.elsevier.com/app/contact/supporthub/sciencedirect/)
- [Terms and conditions](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions)
- [Privacy policy](https://www.elsevier.com/legal/privacy-policy)
- Cookie settings

All content on this site: Copyright © 2026 Elsevier B.V., its licensors, and contributors. All rights are reserved, including those for text and data mining, AI training, and similar technologies. For all open access content, the relevant licensing terms apply.

[![RELX group home page](https://www.sciencedirect.com/shared-assets/60/images/logo-relx-tm.svg)](https://www.relx.com/)