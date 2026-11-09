# D6 晶圆厂仿真与调度

[数据集目录](../datasets.md) · [设备运维资源](../operations.md)

厂级离散事件模型用产品路由、设备组、派工规则和停机分布产生运行事件。适合研究批次流转、重入、搬运和瓶颈。模型中的流程名与加工时间要按工厂仿真口径解释，工步内的压力、功率等物理量见工艺数据章节。

| 编号 | 数据 | 可观察的结构 | 访问与许可 |
| --- | --- | --- | --- |
| F01 | SMT2020 | 公开的半导体前道厂模型，高产低混与低产高混等场景。用产品路由、步骤、设备组等标识组织排程输入 | [作者站点](https://p2schedgen.fernuni-hagen.de/index.php/downloads/simulation) · [SMT2020 ZIP](https://p2schedgen.fernuni-hagen.de/fileadmin/ess/uploads_p2schedgen/SMT2020/SMT2020.zip)。数据许可未确认 |
| F02 | [SMAT2022](https://github.com/kwoo-lee/SMAT2022) | 在 SMT2020 基础上增加自动物料搬运系统（AMHS），包括轨道、区域、地址、设备和端口等模型表 | 作者仓库说明描述四个模型，当前目录可定位到 LVHM_E XLSX。数据许可未确认，沿用 F01 的基础流程 |
| F03 | [MIMAC-2026](https://semiconfab.org/benchmark) | 发布方构建的 300 mm 晶圆厂调度基准，按场景组织模型与性能基线 | 提供 JSON 配置和模拟器，当前版本以批次派工为主，搬运拥塞与交互式维护范围见包内说明。数据许可未确认。[模拟器包](https://semiconfab.org/downloads/mimac2026-simulator.zip) |
| F04 | 历史 MIMAC | SEMATECH/JESSI 半导体厂容量与调度测试集，按厂型、产品路由和设备组组织 | [高校存档 ZIP](https://p2schedgen.fernuni-hagen.de/fileadmin/ess/uploads_p2schedgen/Simulation/MIMAC_datasets.zip) · [背景论文](https://repository.lib.ncsu.edu/bitstreams/b8e70671-d1c0-4742-a09f-5a48441168ea/download)。数据许可未确认 |

## 建议实验

在同一厂型、需求负载和故障配置上比较派工策略。保持仿真预热长度、随机种子集合和评估区间一致。分别报告产出、在制品、周期时间分布和交期表现。SMAT2022 的搬运扩展适合验证拥塞是否改变瓶颈。

[上一节 工艺物理仿真](simulation.md) · [回到目录](../datasets.md)
