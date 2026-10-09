# Comprehensive review of thermal management strategies for lithium-ion batteries: from heat generation mechanism to advanced cooling solutions  
锂离子电池热管理策略综述：从热生成机制到先进冷却解决方案

Author links open overlay panelKai Du a  杜凯 a, Guopeng Chen a  陈国鹏 a, Yuheng Zhang a, Shuo Li a  李硕 a, Benqi Shi a  , Tianze Zhang a  , Junhao Liu a  , [Fengxiang Chen b](https://www.sciencedirect.com/author/57207568162/fengxiang-chen), Shangzhen Xie a, [Zhiguang Guo a c](https://www.sciencedirect.com/author/8671116800/zhiguang-guo)

Show more  显示更多

Add to Mendeley  添加到 Mendeley

Share  分享

Cite  引用

[https://doi.org/10.1016/j.ensm.2025.104597](https://doi.org/10.1016/j.ensm.2025.104597 "Persistent link using digital object identifier")[Get rights and content  获取权限和内容](https://s100.copyright.com/AppDispatchServlet?publisherName=ELS&contentID=S2405829725005951&orderBeanReset=true)

## Abstract  摘要

Lithium-ion batteries (LIBs) are pivotal in decarbonizing transportation due to their high energy density and efficiency. However, their long-term performance and safety critically depend on effective thermal management, as excessive heat accumulation can precipitate catastrophic failures like thermal runaway. This review systematically analyzes LIB thermal dynamics, beginning with the fundamental operational principles and heat generation mechanisms, followed by an in-depth examination of thermal runaway triggers. We then present a dual-pathway approach to thermal management: Internal strategies focus on material-level modifications to reduce heat generation and enhance thermal conduction, while external strategies evaluate four advanced cooling techniques, including liquid cooling, phase change materials, thermoelectric coolers, and heat pipes, with detailed discusSiOns on their heat transfer physics, efficiency, and implementation challenges. Furthermore, concerning the issue of thermal runaway propagation, the article presents reasonable countermeasures. To enable the prediction of battery behavior, the article introduces the Battery Management System (BMS) and two prediction methods (model-based and AI-based methods) in its final part, and also provides thermal management solutions for battery systems other than lithium-ion batteries, with sodium-ion batteries as an example. By integrating theoretical insights with practical applications, this review not only synthesizes the state-of-the-art in LIB thermal management but also provides actionable guidelines for researchers and engineers to optimize battery safety and durability in next-generation energy storage systems.  

## Graphical abstract  图形摘要

This review describes the working principle and heat generation mechanism of lithium-ion batteries, as well as the triggering and hazards of thermal runaway, and presents relevant thermal management methods: internal material thermal management and four external thermal management strategies. The article outlines the research progress in battery thermal management and provides guiding principles for future studies.  

![Image, graphical abstract](https://ars.els-cdn.com/content/image/1-s2.0-S2405829725005951-ga1.jpg)

1. [Download: Download high-res image (156KB)](https://ars.els-cdn.com/content/image/1-s2.0-S2405829725005951-ga1_lrg.jpg "Download high-res image (156KB)")
2. [Download: Download full-size image](https://ars.els-cdn.com/content/image/1-s2.0-S2405829725005951-ga1.jpg "Download full-size image")

## Introduction

Due to environmental degradation, fossil fuel shortages, and a series of related issues, traditional internal combustion engine vehicles, known for their high pollution and excessive fossil fuel consumption, are being phased out, with many countries announcing plans to ban the sale of gasoline-powered cars. Cleaner and more environmentally friendly new energy vehicles have emerged as alternatives, providing consumers with sustainable options. Electric vehicles (EVs), representing clean and eco-friendly transportation, have developed rapidly due to their reduced environmental impact. Most EVs rely on lithium-ion batteries as their power source. As a key component of energy storage systems, lithium-ion batteries offer advantages such as high energy density, high power density, long lifespan, and environmental friendliness [1]. However, certain challenges still hinder their widespread adoption, including spontaneous combustion and exploSiOns caused by thermal runaway [[2], [3], [4], [5], [6]].

To ensure battery safety, researchers continue to investigate the heat generation mechanisms of batteries [[7], [8], [9]] and the triggering conditions of thermal runaway [10]. Various technologies have been employed to control battery temperature, such as improving battery materials to reduce heat generation and prevent thermal propagation, as well as developing battery thermal management systems (BTMS) to maintain uniform temperature distribution across individual cells and battery packs. Based on cooling methods, widely used battery thermal management technologies can be categorized into liquid cooling (LC), PCM cooling (PCMS), thermoelectric cooling (TEC), and heat pipe cooling (HP). Numerous review papers on lithium-ion batteries for EVs have been published. For instance, Jaguemont et al. [11]. summarized the current state of BTMS and systematically introduced traditional cooling systems. Choudhari et al [12]. reviewed temperature control systems using different cooling techniques, including air convection, liquid convection, phase-change materials, and their combinations. However, most reviews focus only on external battery thermal management, with limited discusSiOn on internal heat generation principles and material-based thermal management, lacking a comprehensive overview of thermal management for lithium-ion batteries.

Therefore, the purpose of this review is to first provide a brief overview of the working principles of lithium-ion batteries, heat generation mechanisms, and the triggers and hazards of thermal runaway, offering readers fundamental knowledge of battery functionality. Additionally, thermal management approach is divided into internal material-based thermal management and external system-based thermal management. Meanwhile, the article also introduces the prediction methods for batteries behaviors. Finally, the prospects for battery thermal management in future lithium-ion EV applications are discussed.

## Section snippets

## Mechanism of LIB heat generation

As illustrated in Fig. 1, lithium-ion battery (LIB) packs consist of interconnected cells arranged in series or parallel to deliver electrical energy at specified current rates. Each cell contains four key components: current collectors, cathode, anode, and separator. The electrodes host lithium ions and facilitate intercalation/deintercalation reactions, while the electrolyte-typically a lithium salt dissolved in organic carbonates (e.g., ethylene carbonate)-enables ionic conduction. The

## Internal thermal management of the batteries

Since improving the internal materials of the battery itself or optimizing the battery interior can fundamentally manage and control battery heat generation, this section introduces the internal thermal management of lithium-ion batteries from these two aspects. The material optimization of lithium-ion batteries includes improvements to the cathode, anode, electrolyte, and separator. For cathode material improvement, three effective approaches are adopting safer materials, conducting elemental

## External thermal management of batteries

To ensure safe operation and prevent thermal risks, various hazards, such as physical, chemical, and environmental dangers, lithium-ion batteries require precise thermal regulation with optimal operating temperatures maintained at 25–35°C and inter-cell temperature differences constrained within 2–3°C [85]. This strict thermal requirement necessitates the implementation of battery external thermal management systems. As illustrated in Fig. 4, existing thermal management strategies primarily

## The introduction of BMS

To ensure the normal operation and expected service life of batteries, the implementation of an effective Battery Management Strategy (BMS) is crucial [344,345]. The BMS serves as a key system connecting batteries and vehicles, encompassing a series of functions such as battery state monitoring, thermal management, battery balancing, state estimation, and fault diagnosis [346,347]. It is mainly composed of modules including battery pack, central controller, data acquisition, charge-discharge

## Outlook

Recent advances in thermal management for lithium-ion batteries have demonstrated unparalleled heat dissipation capabilities and potential, establishing this technology as an indispensable component in contemporary energy applications. This review systematically consolidates thermal management strategies, encompassing the operational principles and heat generation mechanisms of lithium-ion batteries, while detailing the triggering factors and hazards of thermal runaway. It provides a

## CRediT authorship contribution statement

**Kai Du:** Writing – original draft, Visualization, Validation, Methodology, Investigation, Conceptualization. **Guopeng Chen:** Writing – original draft, Visualization, Validation. **Yuheng Zhang:** Visualization, Validation, Methodology. **Shuo Li:** Visualization, Validation. **Benqi Shi:** Visualization, Validation. **Tianze Zhang:** Visualization, Validation. **Junhao Liu:** Visualization, Validation. **Fengxiang Chen:** Writing – review & editing, Visualization, Validation, Funding acquisition. **Shangzhen Xie:** Writing – 

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

Funding: We acknowledge the support from the National Natural Science Foundation of ChiNa (NSFC) (No.12205226). National Natural Science Foundation of China (52373058, 52373090 and U21A2095), Department of Science and Technology of Hubei Province (No. 2025CSA001 and 2024CSA076), Outstanding Young and Middle-aged Scientific and Technology Innovation Team of Higher Education Institutions of Hubei Province (No. T2024010).

## References (378)

- L. Lu _et al._
    
    ### [A review on the key issues for lithium-ion battery management in electric vehicles](https://www.sciencedirect.com/science/article/pii/S0378775312016163)
    
    ### J. Power Sources
    
    (2013)
    
- X. Feng
    
    ### [Thermal runaway mechanism of lithium ion battery for electric vehicles: a review](https://www.sciencedirect.com/science/article/pii/S2405829716303464)
    
    ### Energy Storage Mater.
    
    (2018)
    
- R.R. Kohlmeyer
    
    ### [Pushing the thermal limits of Li-ion batteries](https://www.sciencedirect.com/science/article/pii/S2211285519306342)
    
    ### Nano Energy
    
    (2019)
    
- W. Li _et al._
    
    ### [A surrogate thermal modeling and parametric optimization of battery pack with air cooling for EVs](https://www.sciencedirect.com/science/article/pii/S1359431118352074)
    
    ### Appl. Therm. Eng.
    
    (2019)
    
- D. Ren _et al._
    
    ### [Overcharge behaviors and failure mechanism of lithium-ion batteries under different test conditions](https://www.sciencedirect.com/science/article/pii/S0306261919308566)
    
    ### Appl. Energy
    
    (2019)
    
- T. Wu _et al._
    
    ### [Comparison analysis on the thermal runaway of lithium-ion battery under two heating modes](https://www.sciencedirect.com/science/article/pii/S0304389417308440)
    
    ### J. Hazard. Mater.
    
    (2018)
    
- L. Raijmakers _et al._
    
    ### [A review on various temperature-indication methods for Li-ion batteries](https://www.sciencedirect.com/science/article/pii/S0306261919303757)
    
    ### Appl. Energy
    
    (2019)
    
- X. Feng _et al._
    
    ### [Mitigating thermal runaway of lithium-ion batteries](https://www.sciencedirect.com/science/article/pii/S254243512030088X)
    
    ### Joule
    
    (2020)
    
- J. Jaguemont _et al._
    
    ### [A comprehensive review of future thermal management systems for battery-electrified vehicles](https://www.sciencedirect.com/science/article/pii/S2352152X20301754)
    
    ### J. Energy Storage
    
    (2020)
    
- V. Choudhari _et al._
    
    ### [A review on effect of heat generation and various thermal management systems for lithium ion battery used for electric vehicle](https://www.sciencedirect.com/science/article/pii/S2352152X20315668)
    
    ### J. Energy Storage
    
    (2020)
    

View more references  查看更多参考文献

## Cited by (1)

- ### [Optimizing the thermal and energy efficiency of a thermoelectric-based battery thermal management system via adaptive control strategies and phase change materials  
    通过自适应控制策略和相变材料优化热电基电池热管理系统中的热能效率](https://www.sciencedirect.com/science/article/pii/S036054422505488X)
    
    2026, Energy
    
    Show abstract  显示摘要
    

[View full text  全文](https://www.sciencedirect.com/science/article/pii/S2405829725005951)

© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.  
© 2025 Elsevier B.V. 保留所有权利，包括文本和数据挖掘、AI 训练等类似技术的权利。

## Recommended articles

- ### [Insights into the coupled thermal behavior of silicon/graphite composite anodes in high energy density lithium-ion battery](https://www.sciencedirect.com/science/article/pii/S2405829725008384 "Insights into the coupled thermal behavior of silicon/graphite composite anodes in high energy density lithium-ion battery")  
    
    Energy Storage Materials, Volume 84, 2026, Article 104841  
    
    Wei Zeng, …, Qingsong Wang
    
- ### [Unveiling thermal risks of presumed safe lithium iron phosphate batteries](https://www.sciencedirect.com/science/article/pii/S2590116825001389 "Unveiling thermal risks of presumed safe lithium iron phosphate batteries")  
    
    eTransportation, Volume 27, 2026, Article 100531  
    
    Dian Zhang, …, Xin-Bing Cheng
    
- ### [Numerical exploration for bioconvective nanofluid flow towards a rotating surface with chemical reaction and radiative effects](https://www.sciencedirect.com/science/article/pii/S2666818125002360 "Numerical exploration for bioconvective nanofluid flow towards a rotating surface with chemical reaction and radiative effects")  
    
    Partial Differential Equations in Applied Mathematics, Volume 16, 2025, Article 101310  
    
    Tooba Sadaf, …, Nidhal Ben Khedher  
    托巴·萨达夫，……，尼达尔·本·赫德赫
    

Show 3 more articles  显示更多文章

## Article Metrics

### Citations  引用

- Citation Indexes  引文索引1

### Captures  捕捉

- Mendeley Readers  Mendeley 阅读24

### Mentions  提及

- News Mentions  新闻提及1

![PlumX Metrics Logo](https://cdn.plu.mx/3ba727faf225e19d2c759f6ebffc511d/plumx-logo.png)[View details  查看详细信息](https://plu.mx/plum/a/?doi=10.1016%2Fj.ensm.2025.104597&theme=plum-sciencedirect-theme&hideUsage=true)

[![Elsevier logo with wordmark](https://www.sciencedirect.com/shared-assets/47/images/elsevier-non-solus-new-with-wordmark.svg)](https://www.elsevier.com/)

- [About ScienceDirect](https://www.elsevier.com/solutions/sciencedirect)
- [Remote access](https://www.sciencedirect.com/user/institution/login?targetURL=%2Fscience%2Farticle%2Fpii%2FS2405829725005951)
- [Contact and support](https://service.elsevier.com/ci/pta/login/redirect/contact/supporthub/sciencedirect/p_li/ZGV7PPcYjEOgD54VjyfXqn1Y1O6yTWNsh2jeEHPptZfqjk9kr0oicgnjScVnsVoJ_nk9uB0bsm1ysXcCIKIR_NRhzrq6HBf2bQ7qg~HiZmn~yTzAFXTmg60wDnPoA1L5D1NXHNStam9mCEEHnVIqnucltYao7xVvDsLZqeEHdC8hm8vJuS9xjFACA1khlfJXQIuUbVAAJLJ1MK~qmtO0HWoYC9v4aV42SJlafO58LO6niOj0Ariix1yRJMy6kZ5e~uO_UPcM79egFx7zk7rgMmJ9_uI1B77uNsdSmyE6dzAYjMzzlixXOM~_k5wOJDfOBDSJh7KRDK0YvfYzm~E~DkOy4RWFsLA4KCEnXx5tVfs_TTpC2WEe2avW_izejtQGcyxnqp2hiS62q56JBgCkWIqi4fRxK6Z7vpaTn3MGsur2lH7p9qvZkEQjoIMFusnlnQQ1JayJqnOp92Pl50aPvQ**)
- [Terms and conditions](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions)
- [Privacy policy](https://www.elsevier.com/legal/privacy-policy)
- Cookie settings

All content on this site: Copyright © 2026 Elsevier B.V., its licensors, and contributors. All rights are reserved, including those for text and data mining, AI training, and similar technologies. For all open access content, the relevant licensing terms apply.

[![RELX group home page](https://www.sciencedirect.com/shared-assets/60/images/logo-relx-tm.svg)](https://www.relx.com/)