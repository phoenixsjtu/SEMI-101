# 论文导读

从一个设备问题选论文。每组读物给出一个起点和一项对照，便于比较作者用什么设备、数据和验证方式支持结论。完整的来源与许可记录见各板块目录。

## 设备设计

- **腔室几何怎样影响片内均匀性？** 先看 GaN MOCVD 如何把腔室高度与生长速率对照，再看 ALE 研究如何比较四种进气与腔室构型。读图时记录几何变量、边界条件和校验量。[GaN MOCVD 腔室](https://doi.org/10.1016/j.jcrysgro.2015.09.003) · [ALE 多尺度腔室设计](https://doi.org/10.1016/j.compchemeng.2022.107757)
- **数字孪生用什么观测量约束模型？** 看 ALD 研究如何用吸收观测校准瞬态输运，再对照 ICP 研究中的实验比较，区分两种设备模型分别能解释的现象。[NIST ALD 数字孪生](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer) · [ICP 腔室与实验](https://doi.org/10.1063/1.362932)
- **如何降低设计搜索的求解成本？** 对照静电卡盘的多保真热仿真与设备条件驱动的刻蚀特征模型，记录各自的训练数据来源、预测对象和高精度复核方式。[静电卡盘多保真优化](https://doi.org/10.1007/s11081-025-10059-0) · [设备条件驱动的刻蚀形貌模型](https://repositum.tuwien.at/handle/20.500.12708/212138)

[设备设计完整资源](design.md) · [设备设计专题](../learn/design.md)

## 工艺智能

- **设备轨迹能预测哪些量测？** 从虚拟量测综述找方法，再对照 CMP 去除率与光刻套刻误差两项研究。留意量测粒度、抽检策略和预测时点。[虚拟量测综述](https://doi.org/10.1016/j.eswa.2024.123559) · [CMP 虚拟量测与动态采样](https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic) · [光刻套刻虚拟量测](https://doi.org/10.1016/j.eswa.2010.08.040)
- **怎样把模型输出用于批间控制？** 对照 CMP 研究中的设备状态与虚拟量测研究中的可信度门槛。记录模型被采纳的条件、调整对象与验证场景。[结合设备状态的 CMP 批间控制](https://doi.org/10.1109/ASMC.2018.8373161) · [基于预测可信度的批间控制](https://doi.org/10.1109/TSM.2012.2228243)
- **怎样应对设备维护或工况变化？** 比较 CVD 模型怎样选择维护前后的训练记录，以及统计模式分析怎样概括一个批次的设备轨迹。[CVD 虚拟量测与维护记录](https://doi.org/10.1109/TASE.2025.3570863) · [半导体批次的统计模式分析](https://doi.org/10.1002/aic.12247)

[工艺智能完整资源](process.md) · [工艺智能专题](../learn/process.md)

## 设备运维

- **怎样区分工艺变化与设备故障？** 对照 PECVD 内置传感器与刻蚀 OES 研究，记录故障证据来自何处，尤其是故障注入、工况差异和维护记录。[PECVD 状态特征与故障模型](https://doi.org/10.1016/j.compind.2012.10.002) · [刻蚀设备的气体流量故障检测](https://doi.org/10.3390/s23041889)
- **提前多久报警才有用？** 对照离子束刻蚀的在线寿命估计与低温泵维护实践。比较预测目标、误报成本和工程师有多长时间能安排维护。[离子束刻蚀在线 RUL](https://doi.org/10.36001/phmconf.2018.v10i1.589) · [晶圆厂低温泵预测维护](https://doi.org/10.1109/ASMC54647.2022.9792482)

[设备运维完整资源](operations.md) · [设备运维专题](../learn/operations.md)

[学习导航](../README.md) · [数据集总览](datasets.md) · [代码索引](code.md)
