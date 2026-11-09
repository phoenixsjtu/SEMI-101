# 数据检索与覆盖记录

[数据集目录](../datasets.md) · [总表 CSV](inventory.csv) · [收录与贡献](../../CONTRIBUTING.md)

本轮检索记录于 2026-11-09。以半导体制造设备为范围，沿工艺设定、运行过程、量测、故障事件和仿真输出查找。优先核对发布方记录、数据字典、文件清单和条款。对可抽查的资料进一步核对文件，例如匿名前道传感器 CSV 的连接列、BOSCH 的 NetCDF 编码与采样说明、ST-AWFD 的标签单位和许可证、CMP 公告的时序与目标字段。这里的覆盖以已追到发布入口的记录为准。

## 检索路径

| 入口 | 查询示例 | 核对内容 |
| --- | --- | --- |
| [DataCite](https://commons.datacite.org/) | `types.resourceTypeGeneral:Dataset AND (wafer AND (etch OR etching))`，以及薄膜/溅射、CMP/离子注入、量测/光刻、配方/虚拟量测五组词 | 每组抽查首批 25 条，沿 DOI 查发布文件、版本和同源记录 |
| [Zenodo](https://zenodo.org/) · [Mendeley Data](https://data.mendeley.com/) · [高校数据仓储](https://www.repository.cam.ac.uk/) | `plasma etch OES wafer measurements`、`ion beam tuning`、`PVD APC SPC thickness`、`ALD PECVD MOVPE sputtering wafer` | 配方参数与实测信号的区别、字段关联、点位坐标、附件类型、开放许可 |
| [PHM Society](https://phmsociety.org/) · [NASA DASHlink](https://c3.ndc.nasa.gov/dashlink/) · [UCI](https://archive.ics.uci.edu/) | `chemical mechanical planarization challenge`、`ion mill faults`、`semiconductor FDC wafer fault` | 赛题标签、训练测试边界、机台或批次标识、原始发布与镜像 |
| [NIST 数据目录](https://data.nist.gov/) · [Data.gov](https://catalog.data.gov/) · [期刊数据声明](https://doi.org/10.1038/s41586-023-05773-7) | `wafer thickness XRR ellipsometry`、`wafer SEM inspection`、`EUV resist exposure`、`semiconductor etch data availability` | 区分原始图像、图表源数据、后处理附件、按申请提供 |
| [国家基础学科公共科学数据中心](https://www.nbsdc.cn/) · [国家计量科学数据中心](https://www.nmdc.ac.cn/) | 半导体机台、晶圆量测、碳化硅晶片检测 | 核对项目页是否提供独立数据文件及使用条款 |
| [GitHub](https://github.com/) · [Hugging Face](https://huggingface.co/datasets) · [NeurIPS](https://proceedings.neurips.cc/) | `etch profile condition vector`、`ALD saturation simulated dataset`、`lithography simulation aerial image`、`wafer fab SMT2020 AMHS` | 区分数据包、派生标签、生成器和仅有代码的仓库 |
| [刻蚀虚拟量测文献结构化索引](https://doi.org/10.48366/R1907748) · [HCAI 项目索引](https://hcai.etf.unsa.ba/datasets.html) | 从同一团队、引用和作者代码追溯关联资源 | 确定旧版、新版、复现仓与独立数据来源 |

同一批图像的勘误、镜像或标注扩展沿用同一编号。例如 Carinthia-S 与 Carinthia 归在 M03。以旧基准输入重新求解或新增模型表的资源单列，并注明复用了哪些输入。例如 LithoBench-PDE 继承部分版图，SMAT2022 继承 SMT2020 的基础流程。

## CSV 字段

| 字段 | 如何读 |
| --- | --- |
| `id` / `chapter` | 稳定编号和章节文件名。章节用编号连接到总表，多个版本说明保留在章节中。 |
| `origin` | `industrial-measured` 为工业实测，`lab-measured` 为实验室实测，`industrial-context` 为半导体场景发布、采集来源交代有限，`fault-injected` 为含受控故障的设备实测，`literature` 为文献汇编，`physical-simulation` 和 `fab-simulation` 为两种尺度的仿真，`profile-source-unconfirmed` 表示能查到条件和轮廓文件，生成方法待确认。 |
| `recipe` | `settings` 为公开实验工况，`partial` 为部分条件或论文参数，`normalized` 为归一化的配方值，`identifier` 为配方编号或类别，`context` 为工步、试验设计或工况上下文，`sim-input` 为仿真输入。 |
| `trace` | `timeseries` 为采样序列，`normalized-series` 为归一化序列，`aggregates` 为轨迹汇总，`feature-table` 为时序来源或汇总方式未明的特征表，`spectra-images` 为工况下的光谱和图像，`snapshots` 为分阶段采集的观测。 |
| `metrology` | `physical` 为膜厚、速率、折射率等物理量，`spatial` 为多点量测，`inspection` 为缺陷图像或晶圆图，`downstream-test` 为下游测试结果。 |
| `simulation` | 输出的形态，如 `profiles` 剖面、`fields` 场量、`images` 仿真图、`particle-distribution` 粒子分布、`summary` 结果汇总或 `fab-model` 厂级模型。 |
| `task` | 主要可验证任务，用斜杠分隔多个用途。 |
| `join_keys` | 发布包可以关联的字段或层级。跨表前检查唯一性、单位、空值和基数。 |
| `access` | `public-files` 为发布页提供文件，`upstream-linked` 为上游说明指向独立存档，`official-challenge` 为竞赛入口，`supplement` 为论文附件，`mirror` 为第三方镜像，`generator` 为模型与生成工具。 |
| `license` / `source` | 发布入口与单独核对的条款。未明示的条款按未确认处理，需申请的文件另记。 |

`none` 表示本轮在可获取的版本中没有确认该类字段或产物。访问状态基于发布页和文件清单，部分文件做过抽查。已登记的代码指向上游实现，复现状态依各项目的说明。

## 待补证据

| 目前的覆盖缺口 | 已找到的线索与下一步核对项 |
| --- | --- |
| 同一批量产晶圆关联完整配方版本、工步时序、片内量测与下游电测 | BOSCH 有相连的轨迹和空间量测，Infineon PVD 有轨迹摘要和量测，FBK 有归一化配方和电学目标。分别查看各发布的关联层级，再追带物理单位的逐工步设定和变更记录。[BOSCH](https://zenodo.org/records/17122442) · [Infineon PVD](https://zenodo.org/records/23442538) · [FBK](https://zenodo.org/records/21379926) |
| 原始 OES 与跨腔室终点标签，及 PECVD 配方与沉积率 | 已追到论文入口，本轮未确认独立可下载的完整文件或对应许可。[跨腔室终点检测](https://doi.org/10.1007/s10845-025-02715-0) · [PECVD 沉积率研究](https://doi.org/10.1002/aidi.202500074) |
| CFD 输入、网格、全场输出与同工况实测 | 已追到 ALD 原位校准研究，继续查网格、求解器边界条件及成对实验文件。[NIST MoCl₅ 数字孪生](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer) |
| 清洗、涂胶显影、离子注入后剂量图、晶圆键合、减薄切割与封装设备 | 目前有光刻胶、湿法前处理与注入机调束样本。对其他工序优先追具体设备、工艺输入和逐片或逐工步数据；制造生命周期清单单独看待。[EUV 光刻胶数据](https://doi.org/10.48804/3OFFSV) · [PL 与湿法前处理](https://zenodo.org/records/19603335) · [离子注入调束](https://zenodo.org/records/11084332) |
| 实际厂级事件日志 | 历史 SEMATECH/JESSI MIMAC 已定位到高校存档，许可未确认。真实厂日志和厂级仿真模型分开登记。[历史数据集说明](https://repository.lib.ncsu.edu/bitstreams/b8e70671-d1c0-4742-a09f-5a48441168ea/download) |

原理模板、通用机械故障、PCB 组装数据和纯器件电路仿真适合作为检索线索或其他主题资料。此目录登记直接与半导体制造设备、工艺或量测相关的样本、模型和附录。[ALD/ALE 字段模板示例](https://zenodo.org/records/16413857)

[回到数据集目录](../datasets.md)
