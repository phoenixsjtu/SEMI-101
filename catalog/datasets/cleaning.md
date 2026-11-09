# D7 清洗与湿法前处理

[数据覆盖矩阵](matrix.md) · [涂胶与显影](coat-develop.md) · [沉积与 CMP](deposition-cmp.md)

清洗研究常用颗粒去除率、图形损伤、残留和表面终止状态作目标。先确认目标是清洗效果，还是清洗对后续量测信号的影响。实验室常发布浓度、时间和图像，只有机台数据才会留下逐片流量、温度、功率和执行事件。

| 编号 | 工序与设备 | 可下载证据 | 关联粒度 |
| --- | --- | --- | --- |
| M04 | 硅片 HF 湿法前处理 | 处理条件、PL 原图及数值线扫 | 图号、样品条件与采集时间 |
| W01 | 大气压等离子体射流（APPJ）去胶 | 功率／流量、去除速率、FTIR、TALIF | 试验条件及图号 |
| W02 | 槽式兆声清洗 | 空化高速摄影、论文中的去除率和损伤 | 浴液配方条件 |
| W03 | InSb 表面 HCl 清洗与退火 | XPS、器件原始电测和良率表 | 处理组；电测内部可到器件 |
| W04 | p-GaN 湿洗、真空热处理与 Ar⁺ 表面清理 | VAMAS 光谱、EDX 表和 SEM | 处理阶段与测点 |

## M04 HF 前处理与硅片光致发光

论文用 HF 浸泡、去离子水冲洗与干燥作为光致发光（PL）成像前处理。发布 CC BY 4.0。[数据记录](https://zenodo.org/records/19603335) · [论文](https://doi.org/10.1088/1361-6641/aea702)

| 文件 | 已核对字段或内容 |
| --- | --- |
| `Figure_3a_data.csv` | `Concentration, immersion time`、`Lower modal quartile`、`Mode`、`Upper modal quartile` 及归一化列 |
| `Figure_4b_data.csv` | 处理前后的正反面 PL 线扫及归一化数据。空行或空值须按图注识别扫描段 |
| `Figure_6a_0min_raw_image.raw` 等 | 1,024 × 1,024、32 位 PL 原图，按图号及暴露时间定位 |
| `Figure_6a_data.csv`、`Figure_6b_data.csv` | 不同空气暴露时长的 PL 线扫 |

从图号和文件说明建立条件表，再按正反面、样品处理和成像时间对照。浓度与时间可以预测 PL 对比变化；若要评价颗粒去除或金属污染，需要另有量测标签。[原始浓度／浸泡表](https://zenodo.org/records/19603335/files/Figure_3a_data.csv) · [前后处理线扫](https://zenodo.org/records/19603335/files/Figure_4b_data.csv)

## W01 York APPJ 干式去胶

University of York 发布 `EtchingData.zip)，五组 DAT 与对应字段说明。CC BY 4.0。[数据 DOI](https://doi.org/10.15124/051062ea-0b26-4b1c-a6e0-6ef300e4d590) · [下载 ZIP](https://pure.york.ac.uk/ws/portalfiles/portal/69710173/EtchingData.zip) · [论文](https://doi.org/10.1088/0963-0252/25/2/02LT01)

| 文件 | 已核对字段 |
| --- | --- |
| `Figure2_FreqComparison.dat` | `slm`、`13.56MHz`、`40.68MHz` |
| `Figure3_PowerVariation.dat` | `Power`、`EtchRate`、`RateError` |
| `Figure4_FlowRate.dat` | `FlowRate`、`EtchRate`、`RateError` |
| `Figure5_FTIRSpectra.dat` | `Wavenumber`、`BlankSiWafer`、`PR`、`ICPEtched`、`APPJEtched` |
| `Figure6_TALIF.dat` | `FlowRate`、`Lifetime`、`Signal` |

图 4 与图 6 可在核对工况后按 `FlowRate` 对照去除率和氧诊断信号。不同实验的频率或试样条件要先拆开。文件没有跨表晶圆 ID 或射流执行波形。

## W02 兆声清洗的高速影像

研究拍摄了不同 SDS 浓度与水中含氢状态下的空化。11 个公开 MP4 中，S1–S10 是工况视频，S11 是机理说明。论文图 11 另有颗粒去除率及图形损伤，部分条件可对照。录制空化时未放入待清洗样片，因此关联单位是浴液配方条件，无法按晶圆或采样时刻拼接。论文 CC BY-NC-ND 4.0，视频随论文发布。[论文与完整附件目录](https://pmc.ncbi.nlm.nih.gov/articles/PMC8799594/) · [视频 S1](https://ars.els-cdn.com/content/image/1-s2.0-S1350417721004016-mmc1.mp4) · [视频 S11](https://ars.els-cdn.com/content/image/1-s2.0-S1350417721004016-mmc11.mp4)

## W03 Warwick InSb 湿法清洗与电测

实验比较 HCl 水溶液和异丙醇体系，并研究清洗后退火对 InSb／Al₂O₃ MOS 电容的影响。ZIP 可下载，数据 CC BY 4.0。[数据 DOI](https://doi.org/10.82444/warw.33777148) · [直接下载 ZIP](https://ndownloader.figshare.com/files/68613265) · [说明](https://ndownloader.figshare.com/files/68613262) · [论文](https://doi.org/10.1088/1361-6641/ab0331)

- `Analysed CV Data.xlsx` 含 `Sample`、`Field`、`Radius (um)`、`Index`、`Anneal Gas`、`Time (mins)`、`Temp. (°C)`，以及平带电压、迟滞和界面陷阱相关量。
- `Yield Spreadsheet.xlsx` 含 `Treatment`、`Die`、`Structure (L/O)`、`Size (L/M/S)`、`ID Number`、泄漏及阶段通过标志。原始器件 TXT 文件名编码处理组、die、结构、尺寸与索引。
- 两份 VAMAS 文件的 XPS 可按 HCl 溶剂及退火阶段分组。XPS 与器件电测只有处理条件对应，缺少共享的试样编号。

## W04 p-GaN 表面清理与活化

HZDR 的两项发布覆盖湿法处理、真空热处理与 Ar⁺ 溅射清理。用 `.vms` 文件名与论文图号恢复温度、时长和处理步骤；例如 `5_650C_40min.vms` 与 `6_after 1.5kV sputtering.vms`。 `EDX_comparison_evaluation.xlsx` 给 `energy/ eV` 和 `CPS`，区分 `Pos. 1`、`Pos. 2`、`hole` 等测点。另有 SEM TIFF，以及按样片 A–D 和处理阶段组织的 XPS 文本。可在样片或条件内比较谱线，未发现覆盖整片的污染分布或设备原始时序。两个归档的部分 VAMAS 文件相同，本目录合并登记。数据 CC BY 4.0。[清理数据](https://doi.org/10.14278/rodare.2168) · [关联 XPS 发布](https://doi.org/10.14278/rodare.1891) · [清理研究](https://doi.org/10.1002/sia.7207) · [活化研究](https://doi.org/10.1038/s41598-023-30329-0)

用第三方 `vamas` 成功读取 W03 的两份 VAMAS 文件，各 30 个谱块，以及 W04 的两份湿法谱，各 17 和 3 个谱块。谱线与处理工况仍需按原始说明关联。读取器为 BSD-3-Clause。[vamas 源码](https://github.com/matkrin/vamas)

## 设备与实验线索

- **RCA 湿法台。** 工艺手册可查设备兼容材料、浴槽步骤、清洗与漂洗设定。分析生产波动需要逐片执行记录和清洗前后量测。[NIST 湿法台](https://www.nist.gov/laboratories/tools-instruments/nanofab-tool-rca-wet-bench-b102) · [单片清洗机](https://www.nist.gov/laboratories/tools-instruments/nanofab-tool-ssec-single-wafer-cleaning-system-3) · [工艺手册 PDF](https://www.nist.gov/system/files/documents/2017/05/09/ReynioldsTech_CMOS_RCA_Clean_USERSMANUAL_v1-2.pdf)
- **CMP 后 PVA 刷洗。** 已追到刷洗氧化铜的实验曲线和颗粒去除研究，仍需独立的刷压、转速或摩擦时序文件，以及可连接的残留数据。[刷洗电化学实验](https://doi.org/10.3390/lubricants13070301) · [PVA 刷形变与颗粒去除](https://doi.org/10.1088/1361-6641/ad78fa) · [EPFL 刷洗机配方界面](https://www.epfl.ch/research/facilities/cmi/equipment/etching/post-cmp-cleaning-system-gnp-cleaner-428/) · [OpenFOAM 刷洗研究](https://doi.org/10.20965/ijat.2025.p0890)
- **冲洗与干燥。** 激光扫描辅助干燥研究有可下载的图示附录，涵盖液滴、时序示意、XPS 和轮廓量测。附录里的图片可以读实验趋势，数值列和逐帧文件待补。[论文](https://doi.org/10.1016/j.apsusc.2023.158844) · [图示附件](https://ars.els-cdn.com/content/image/1-s2.0-S0169433223025242-mmc1.docx)

[回到数据集目录](../datasets.md)
