# 数据检索与覆盖记录

[数据集目录](../datasets.md) · [总表 CSV](inventory.csv) · [收录与贡献](../../CONTRIBUTING.md)

首轮检索记录于 2026-11-09。以半导体制造设备为范围，沿工艺设定、运行过程、量测、故障事件和仿真输出查找。优先核对发布方记录、数据字典、文件清单和条款。对可抽查的资料进一步核对文件，例如匿名前道传感器 CSV 的连接列、BOSCH 的 NetCDF 编码与采样说明、ST-AWFD 的标签单位和许可证、CMP 公告的时序与目标字段。这里的覆盖以已追到发布入口的记录为准。

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

## 第二轮设备专题

| 专题 | 搜索词与追溯路径 | 核对重点 |
| --- | --- | --- |
| [清洗](cleaning.md) | `wafer cleaning`、`megasonic cavitation`、`post-CMP PVA brush`、`photoresist removal APPJ`，沿 DataCite、Zenodo、高校仓库和出版社附件 | 浴液设定、颗粒与损伤目标、PL 数值列、空化视频是否与同片共采 |
| [涂胶与显影](coat-develop.md) | `spin coating millisecond XRR`、`photoresist development`、`track Lithius ProZ`、`prebake PEB linewidth`，沿期刊 Source Data、Dataverse、CRAN 和作者仓库 | 区分实机设定、材料曲线、转速或流量日志、XRR／RGA 时间及拟合数组，抽查工作表能否连接 |
| [离子注入](implantation.md) | `ion implantation SIMS`、`ion beam tuning`、`ion channeling`、`implantation depth profiles`，沿 RepOD、RODARE、Zenodo、Figshare 和期刊 DOI | 记录能量、剂量、深度及单位，区分控制器、探测器和试验后的量测；分别验证 X/Y 及输入输出的关联 |
| [封装](packaging.md) | `die-to-wafer hybrid bonding`、`Cu-Cu thermocompression`、`flip-chip SAM`、`package substrate AOI`、`XCT IC package`、`wafer dicing`，沿 NIST、出版商、作者仓库和公开子集 | 按封装件、试样、图像或工况识别关联键；区分封装机和检测机；记录部分下载、签协议、图示或模型生成 |

对可访问的表格和脚本进行文件名、列名、单位与关联样本抽查。大文件用目录、说明、压缩包目录或子样本核对，页面记录不足或附件端点不可用的情况留在专题。 [覆盖矩阵和计数口径](matrix.md)

## CSV 字段

| 字段 | 如何读 |
| --- | --- |
| `id` / `chapter` | 稳定编号和章节文件名。章节用编号连接到总表，多个版本说明保留在章节中。 |
| `origin` | `industrial-measured` 为工业实测，`lab-measured` 为实验室实测，`industrial-context` 为半导体场景发布、采集来源交代有限，`fault-injected` 为含受控故障的设备实测，`literature` 为文献汇编，`physical-simulation` 和 `fab-simulation` 为两种尺度的仿真，`profile-source-unconfirmed` 表示能查到条件和轮廓文件，生成方法待确认。 |
| `recipe` | `settings` 为公开数值工况，`partial` 为部分数值条件或论文参数，`normalized` 为归一化的配方值，`identifier` 为配方编号或类别，`context` 为工步、试验设计或工况上下文，`coded` 为编码或匿名变量，`instrument-settings` 为量测设备设定，`sim-input` 为仿真输入。 |
| `trace` | `timeseries` 为采样序列，`normalized-series` 为归一化序列，`aggregates` 为轨迹汇总，`feature-table` 为时序来源或汇总方式未明的特征表，`spectra-images` 为工况下的光谱和图像，`snapshots` 为分阶段采集，`video` 为诊断视频，`measurement-series` 为量测仪器序列，`detector-events` 为探测器事件，`benchmark-series` 为基准归档序列。 |
| `metrology` | `physical` 为膜厚、速率、折射率等物理量，`spatial` 为多点量测，`inspection` 为缺陷图像或晶圆图，`downstream-test` 为下游测试结果。 |
| `simulation` | 输出的形态，如 `profiles` 剖面、`fields` 场量、`images` 仿真图、`volumes` 三维体数据、`particle-distribution` 粒子分布、`summary` 结果汇总或 `fab-model` 厂级模型。 |
| `task` | 主要可验证任务，用斜杠分隔多个用途。 |
| `join_level` | 可把输入、结果或不同观测接到的最可靠层级。 `wafer` 为同片且有对应工艺输入与结果；`lot` 为批次；`run` 为设备或量测运行；`specimen` 为试样、芯片或封装件；`sample` 为发布样本；`condition` 为实验条件；`figure` 为论文图表；`case` 为模拟案例；`none` 或 `unknown` 表示无可用关联或未确认。 |
| `join_keys` | 发布包可以关联的字段或层级。跨表前检查唯一性、单位、空值和基数。 |
| `access` | `public-files` 为发布页提供文件，`upstream-linked` 为上游说明指向独立存档，`official-challenge` 为竞赛入口，`supplement` 为图示、影像等论文附件，`supplement-data` 为含可读取数值数据的论文附件，`mirror` 为第三方镜像，`generator` 为模型与生成工具。 |
| `data_files` / `paper` / `code` | 已核对的代表文件名、配套论文与实现入口。代码项也可指向论文附件脚本或可见源码，能否再分发以独立许可为准；空白表示未记录。 |
| `license` / `source` | 发布入口与单独核对的条款。未明示的条款按未确认处理，需申请的文件另记。 |

`none` 表示本轮在可获取的版本中没有确认该类字段或产物。访问状态基于发布页和文件清单，部分文件做过抽查。已登记的代码指向上游实现，复现状态依各项目的说明。

## 待补证据

| 目前的覆盖缺口 | 已找到的线索与下一步核对项 |
| --- | --- |
| 同一批量产晶圆关联完整配方版本、工步时序、片内量测与下游电测 | BOSCH 有相连的轨迹和空间量测，Infineon PVD 有轨迹摘要和量测，FBK 有归一化配方和电学目标。分别查看各发布的关联层级，再追带物理单位的逐工步设定和变更记录。[BOSCH](https://zenodo.org/records/17122442) · [Infineon PVD](https://zenodo.org/records/23442538) · [FBK](https://zenodo.org/records/21379926) |
| 原始 OES 与跨腔室终点标签，及 PECVD 配方与沉积率 | 已追到论文入口，本轮未确认独立可下载的完整文件或对应许可。[跨腔室终点检测](https://doi.org/10.1007/s10845-025-02715-0) · [PECVD 沉积率研究](https://doi.org/10.1002/aidi.202500074) |
| CFD 输入、网格、全场输出与同工况实测 | 已追到 ALD 原位校准研究，继续查网格、求解器边界条件及成对实验文件。[NIST MoCl₅ 数字孪生](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer) |
| 优先四类的设备原始时序 | 已定位实验设定、时间快照、探测事件、扫描序列与部分工况配对，仍需要带机台时戳与晶圆／芯片键的清洗、涂显、注入及键合设备日志。各专题末尾列出具体缺口。 |
| 实际厂级事件日志 | 历史 SEMATECH/JESSI MIMAC 已定位到高校存档，许可未确认。真实厂日志和厂级仿真模型分开登记。[历史数据集说明](https://repository.lib.ncsu.edu/bitstreams/b8e70671-d1c0-4742-a09f-5a48441168ea/download) |

原理模板、通用机械故障、PCB 组装数据和纯器件电路仿真适合作为检索线索或其他主题资料。此目录登记直接与半导体制造设备、工艺或量测相关的样本、模型和附录。[ALD/ALE 字段模板示例](https://zenodo.org/records/16413857)

[回到数据集目录](../datasets.md)
