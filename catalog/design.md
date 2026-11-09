# 设备设计

设备设计关注结构、材料和控制接口如何影响晶圆上能测到的结果。以刻蚀为例，线圈和腔体影响等离子体分布，静电卡盘影响晶圆温度，两者都可能改变片内均匀性。阅读一个仿真案例时，先找出可以改动的设计变量、模型的输出，以及作者拿什么实测量做校验。

入门可先读 Kushner 等人的 ICP 腔室模型，理解结构与晶圆结果之间的联系。接着看 Argonne 的 aldFoam 示例，了解反应器模型如何定义流动与表面反应。最后读 Wang 等人的静电卡盘案例，学习如何用不同精度的仿真结果训练代理模型并搜索设计参数。

## 先修选读

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| ICP 刻蚀腔室 | 理解线圈馈电和腔体非对称性如何改变离子通量与片内刻蚀均匀性 | 论文 | [Kushner 等，三维 ICP 腔室模型与实验比较（1996）](https://doi.org/10.1063/1.362932) | AIP 版权，另有[作者课题组提供的全文](https://cpseg.eecs.umich.edu/pub/articles/jap_80_1337_1996.pdf) |
| 静电卡盘（ESC） | 看静电夹持、晶圆背面的氦气压力、晶圆变形和传热如何耦合 | 仿真示例 | [COMSOL Electrostatic Chuck](https://www.comsol.com/model/electrostatic-chuck-105311) | 厂商模型文件，运行需商业许可或试用 |

## 腔室流动、输运与反应

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| 垂直式 GaN MOCVD 腔室 | 用 CFD 和实验对照腔室高度、流型、外延生长速率和均匀性的关系 | 论文 | [Transport phenomena and the effects of reactor geometry for epitaxial GaN growth（2015）](https://doi.org/10.1016/j.jcrysgro.2015.09.003) | 出版商页面，按来源页条款 |
| 热原子层刻蚀（ALE）腔室 | 结合 CFD 与动力学蒙特卡洛，对比四种腔室构型的前驱体输运和刻蚀表现 | 论文 | [Yun 等，Multiscale CFD modeling of thermal atomic layer etching（2022）](https://doi.org/10.1016/j.compchemeng.2022.107757) | 出版商页面，另有[作者机构存档](https://escholarship.org/uc/item/67c3f705) |
| ALD / ALE 反应器 | 模拟圆柱和 300 mm 晶圆横流反应器中的自限性反应输运 | 开源代码 | [Argonne aldFoam](https://github.com/aldsim/aldFoam) | GPL-3.0，主分支面向 OpenFOAM 10 |
| 实验型 ALD 反应器 | 用吸收成像约束和验证 CFD 模型，分析前驱体脉冲的输运、停留与吹扫 | 论文 | [NIST，基于 CFD 的瞬态前驱体输运数字孪生（2026）](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer) | 期刊版 CC BY 4.0，另有[期刊记录](https://doi.org/10.1016/j.dche.2026.100304) |

## 从腔室条件到晶圆表面

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| 刻蚀和沉积设备 | 由粒子通量和表面反应计算晶圆微结构的形貌演化 | 开源代码 | [TU Wien ViennaPS](https://github.com/ViennaTools/ViennaPS) | GPL-3.0，C++ 与 Python 接口 |
| CVD、ALD 和等离子刻蚀 | 把表面化学反应方程转成 ViennaPS 可读的动力学模型 | 开源代码 | [TU Wien ViennaChem](https://github.com/ViennaTools/ViennaChem) | GPL-3.0 或更新版本，详见上游许可 |
| 刻蚀、MOCVD、ALD 等设备的特征尺度模型 | 用八类化学体系的反应文件、仿真结果和脚本对比形貌预测 | 仿真数据与代码 | [TU Wien，Surface chemistry as data（v1）](https://researchdata.tuwien.ac.at/records/azegw-xq879) | 数据 CC BY 4.0，代码按组件采用 GPL-3.0 或 GPL-3.0-or-later |
| 等离子刻蚀设备与晶圆微结构 | 将设备尺度的条件传给特征尺度模型，研究机器学习如何辅助形貌预测 | 论文 | [Filipovic 等，Equipment-Informed Machine Learning-Assisted Feature-Scale Plasma Etching Model（2024）](https://repositum.tuwien.at/handle/20.500.12708/212138) | TU Wien 机构记录，论文按出版方条款 |

## 代理模型、设计优化与虚拟设备

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| 刻蚀设备静电卡盘 | 融合两种精度的热仿真，搜索冷却流道和表面凸点参数以改善片内温度均匀性 | 论文 | [Wang 等，半导体设备多保真代理优化（2026 卷期）](https://doi.org/10.1007/s11081-025-10059-0) | 期刊版受出版条款约束，有[作者预印本](https://arxiv.org/abs/2411.08149) |
| 等离子刻蚀设备 | 用 ViennaPS 仿真样本训练含物理约束的神经网络，预测刻蚀形貌 | 学位论文 | [MIT，Physics-Informed Deep Learning for Plasma Etch Optimization（2024）](https://hdl.handle.net/1721.1/157256) | 学位论文 CC BY-NC-ND 4.0 |
| 等离子增强 ALD（PEALD）设备 | 用模拟膜厚剖面估计高深宽比结构达到饱和所需的剂量时间倍数 | 仿真数据与读取脚本 | [Argonne Plasma ALD Dataset](https://github.com/aldsim/plasmaml) | 上游可访问，仓库未标明开放许可 |
| 实验型 ALD 反应器 | 研究如何在设备控制软件外封装 Python 接口，供 AI 智能体调用 | 论文 | [Argonne，Design and performance of AI agents interfacing with an atomic layer deposition tool（2026）](https://doi.org/10.1063/5.0318770) | 出版商页面，按来源页条款 |
| 虚拟 ALD / 选择性沉积设备 | 在虚拟设备接口中评测智能体和工艺优化算法 | 开源代码 | [Argonne aldenv](https://github.com/aldsim/aldenv) | BSD-3-Clause |
| 半导体制造设备研发 | 了解设备厂商如何结合仿真与 AI 探索设备和工艺条件 | 产业案例 | [Tokyo Electron，Digital Twins Accelerate Innovation in Semiconductor Technology](https://www.tel.com/blog/all/20250828_001.html) | 厂商公开文章，按来源页条款 |

## 其他设备子系统

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| EUV 光刻机晶圆台 | 建模位置相关的柔性动态，并在实际晶圆台验证主动补偿设计 | 论文 | [Broens 等，Active compensation of position dependent flexible dynamics（2025）](https://research.tue.nl/p/en/research-outputs/active-compensation-of-position-dependent-flexible-dynamics-in-hi) | 期刊版 CC BY 4.0 |
| CMP 多区载具与保持环 | 用有限元模型分析保持环截面和分区压力如何改变晶圆接触压力与去除均匀性 | 论文 | [Park 等，多区载具压力与保持环截面研究（2020）](https://doi.org/10.3390/app10238362) | 期刊版 CC BY 4.0 |
| 离子注入机真空系统 | 用分子流模型分析注入机低压环境中的气体输运 | 仿真示例 | [COMSOL Molecular Flow in an Ion-Implant Vacuum System](https://www.comsol.com/model/molecular-flow-in-an-ion-implant-vacuum-system-10011) | 厂商模型文件，运行需商业许可或试用 |
| 双流体晶圆清洗设备 | 用多相流仿真和实验研究旋转晶圆上的液膜厚度与均匀性 | 论文 | [Optimization of dual-fluid wafer cleaning system](https://doi.org/10.1016/j.cep.2025.110519) | 摘要公开，全文依出版方条款 |

## 复用边界

- ViennaPS 的特征尺度计算关注晶圆表面形貌。若要比较腔室方案，仍需提供设备尺度模型或测量给出的通量和边界条件。
- 两份仿真数据分别提供特征尺度输出和模拟膜厚。用来做模型验证时，可参考[工艺目录](process.md)的设备实测数据，先核对设备、工况与预测量是否一致。
- ESC 代理优化论文提供了方法和案例描述，公开来源未提供可直接重跑的商业卡盘几何及完整高低保真数据。不同工具的模型也依赖各自的版本、材料参数与实验校准。
