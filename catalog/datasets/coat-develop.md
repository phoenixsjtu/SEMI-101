# D8 涂胶、烘烤与显影

[数据覆盖矩阵](matrix.md) · [量测与缺陷](metrology.md) · [光刻仿真](simulation.md#光刻成像与掩模)

这组数据覆盖旋涂、软烘烤、曝光后烘烤（PEB）与显影。先确定需要的是配方设定值、胶膜或线宽量测，还是液膜随时间变化的机理证据。曝光剂量、显影时间和电测结果的粒度各不相同。

| 编号 | 数据 | 关联粒度 |
| --- | --- | --- |
| C01 | Stanford 机器人显影，膜厚表、器件电阻表、视频和代码 | 芯片与片内测点 |
| C02 | Lithius ProZ 量产型涂显设备实验，液膜快照、CD、缺陷与分子模拟 | 图号、工况、时间及半径 |
| C03 | 工业光刻 DOE，编码工艺因子与晶圆线宽 | 晶圆、行记录 |
| C04 | NANYTE 光刻胶配方与旋涂曲线 | 胶型、来源、旋涂转速 |
| C05 | Bath 双重 Talbot 光刻，光强仿真和显影后 SEM | 掩模、曝光图案及位移工况 |
| C06 | PMMA 旋涂的毫秒 XRR 反射率和拟合 | 试验内文件顺序与量测时间 |
| C08 | LithoDreamer 公开的版图、掩模与显影图子集 | 样本 ID 和元数据路径 |
| M02 | KU Leuven EUV 光刻胶、残余厚度和粗糙度 | 胶型、剂量、测量条件 |

## C01 Stanford 机器人显影

Stanford 在 MECA500 实验平台上测得芯片的胶膜厚度与器件电阻。数据 CC BY 4.0，机器人控制与分析代码 MIT。[数据、视频与压缩包](https://zenodo.org/records/17636138) · [论文](https://doi.org/10.1063/5.0313577) · [作者代码](https://github.com/alps-ml/paper.robotic-resist-development)

| 文件 | 已核对字段或内容 |
| --- | --- |
| `chip_thickness_summary.xlsx` | `Chip Name`、`X Position (mm)`、`Y Position (mm)`、`MMA Thickness (nm)`、`PMMA Thickness (nm)` |
| `resistance_raw.xlsx` | 每张表对应一块芯片及器件布局，行和列标识片内电阻测点 |
| `Develop_video.mp4` | 显影过程视频。ROS 2／MoveIt 配置与分析脚本另附 |

抽取电阻工作表名称中下划线前的芯片名，18 张表都能接到厚度表的 `Chip Name`。比较芯片之间的厚度或电测时，验证集整片留出。视频和机器人配置可以帮助理解流程，控制器的逐样片日志需要另找。

## C02 Lithius ProZ 液膜与缺陷

论文在 12 英寸晶圆上描述胶型、旋涂转速与时间、软烘烤、PEB 和显影步骤。公开工作簿有 17 张表。图 17b 提供 `Radius (mm)` 和 0.5、2.5、4.0 s 的液膜厚度快照。其他工作表含 SEM／AFM 关键尺寸（nm）、`Defect Number (N)`、分子动力学的高度坐标（Å）、分布函数和平均力势（kcal/mol）。[论文及数据声明](https://doi.org/10.1038/s41467-025-63689-4) · [直接下载 XLSX](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-025-63689-4/MediaObjects/41467_2025_63689_MOESM3_ESM.xlsx)

按图号、条件、时间和半径复核曲线。不同图的 CD、缺陷与模拟结果没有共享晶圆或运行键。论文采用 CC BY-NC-ND 4.0，工作簿单独再分发条款未确认。

## C03 工业光刻 DOE

R 包 `mdhglm` 附公开的 `circuit.rda`。字段为 `Width`、`A`–`I`、`Wafer`、`waf`、`exp`。A–H 对应掩模尺寸、黏度、旋涂转速、烘烤温度与时间、光阑、曝光和显影时间等因素。I 是刻蚀时间，研究刻蚀前的线宽时排除。许多设定在 R 对象里是编码水平。包许可标为 Unlimited，原工业数据单独的再分发条款未确认。[字段定义](https://github.com/cran/mdhglm/blob/master/man/circuit.Rd) · [下载 RDA](https://raw.githubusercontent.com/cran/mdhglm/master/data/circuit.rda) · [原论文](https://doi.org/10.1002/j.1538-7305.1983.tb02298.x)

每行可以把配方因子与线宽对应，用 `Wafer` 或 `exp + waf` 将同一片晶圆的五个观测放入同一划分。发布表没有逐点坐标和设备执行时序。

## C04 光刻胶配方与旋涂曲线

NANYTE 将公开数据手册整理为 JSON。用 `slug` 定位材料，再查看 `spinCurves[].points[].rpm/um`、`softbake`、`peb`、`develop` 与 `provenance`。`humanVerified` 表示编者人工核对状态。这个入口适合比较数据手册建议与旋涂曲线，具体试验应回查胶型、溶剂、机台和原始文档。发布页声明 CC BY 4.0。[配方说明及许可](https://nanyte.com/photoresists) · [下载 JSON](https://nanyte.com/photoresists/recipes.json)

设备级参考可看 [Utah Nanofab 的 Shipley 1813](https://www.nanofab.utah.edu/wp-content/uploads/2022/12/Shipley-1813-Positive-Photoresist.htm)、[Caltech KNI 配方库](https://lab.kni.caltech.edu/Optical_Lithography_Resources)和 [DTU NanoLab 的 CSAR](https://labadviser.nanolab.dtu.dk/index.php?title=Specific_Process_Knowledge%2FLithography%2FCSAR)。其中的试验条件和图表可作为工艺起点。

## C05 Bath 双重 Talbot 光刻

Bath 分图发布仿真 CSV、MATLAB 图文件和显影后 SEM，也有经沉积和剥离的图像。仿真目录用 `x.csv`、`y.csv` 给坐标（µm），`Data.csv` 给归一化光强矩阵，列对应 X、行对应 Y。按图号、掩模周期与曝光位移条件对照。仿真光强与 SEM 属于不同物理量，工况一致时可比较几何趋势，文件没有图像间的逐像素配准。数据 CC BY 4.0。[数据记录与分卷](https://doi.org/10.15125/BATH-00709) · [CSV 说明](https://researchdata.bath.ac.uk/709/6/readme.docx) · [论文](https://doi.org/10.1364/OE.27.032037)

## C06 PMMA 旋涂毫秒反射率

`Spincoating/data.zip` 含 730 份 `dataNNNN.txt`。配套 Notebook 使用前两列作为散射矢量与反射率。`result_spin.npy` 存膜厚、粗糙度和散射长度密度的拟合结果，Notebook 按数组顺序用 `t_spin.npy` 对齐毫秒时间块。数据可研究成膜动力学，时间来自 XRR 量测，未发现配套电机转速和阀门日志。仓库的 Gold 子目录是另一试验。代码和数据再分发许可未确认。[原始数据 ZIP](https://raw.githubusercontent.com/DavidMarecek2/Millisecond-XRR/main/Spincoating/data.zip) · [作者 Notebook](https://github.com/DavidMarecek2/Millisecond-XRR/tree/main/Spincoating) · [论文](https://doi.org/10.1107/S1600576724001171)

## M02 KU Leuven EUV 光刻胶

公开包含原始和归一化的椭偏厚度 CSV、FTIR CSV、RGA ASC、GPC CSV，以及 CD-SEM 图像、条件文本和线宽粗糙度数据。椭偏表以剂量和残余胶厚为主，RGA 文件的 `Cycle`、`Date`、`Time`、`RelTime[s]` 和质量通道计数是分析仪导出的时间轴。以胶型、剂量和各测量的条件文件核对对应关系。FTIR、GPC、RGA 有作者提供的 Python 分析脚本。数据 CC BY 4.0，脚本独立许可未确认。[数据记录](https://doi.org/10.48804/3OFFSV) · [README](https://rdr.kuleuven.be/api/access/datafile/396372) · [脚本 ZIP](https://rdr.kuleuven.be/api/access/datafile/396328)

## C08 LithoDreamer 仿真子集

公开 `train/index.csv` 可定位 100 个样本及两组工艺配置。以保留前导零的 `sample_id` 和样本 JSON 的 `files.*` 关联版图、掩模、胶层与显影后图像；后者包含 JPG 和 PNG。配置有 `source_type`、`resist_threshold`、`focus_nm`、相对曝光倍数 `exposure_dose`。该子集为仿真，条款限非商业研究及学术用途。[数据、样本字段与许可](https://github.com/7jiangyq/lithodreamer)

## 显影建模与量测参照

- [S07 LithoBench-PDE](simulation.md#光刻成像与掩模) 提供烘烤和显影阶段的数值场。可按版图样本对照光酸浓度、去保护率与显影到达时间。
- [TorchResist](https://github.com/ShiningSord/TorchResist) 提供可微光刻胶工艺模型与演示样本，代码 Apache-2.0。适合复算模型输出和做梯度实验。[论文](https://arxiv.org/abs/2502.06838)
- **C07** [NIST／SEMATECH 光刻 CD 示例](https://itl.nist.gov/div898/handbook/pmc/section6/pmc611.htm) 用 `Cassette + Wafer + Site` 表达 30 盒、每盒三片、每片五点的层次结构。字段包括线宽和测量顺序，配套有 [DAT 文件](https://itl.nist.gov/div898/handbook/datasets/LITHOGRA.DAT)及 [R 示例](https://itl.nist.gov/div898/handbook/pmc/section6/pmc611.r)。原始数据许可未确认。

另有一套 [Dryad 光刻胶剂量与膜厚数据](https://doi.org/10.5061/dryad.7d7wm3877)，可查到 CC0 元数据与字段说明，本轮文件下载返回 403。

量产轨迹的主要缺口仍是可逐片对齐的旋涂电机转速、喷液流量、热板温度及显影运行记录。公开工作簿里的半径剖面和测量时间切片可以校验液膜变化，读时应保留它们原有的采样口径。

[回到数据集目录](../datasets.md)
