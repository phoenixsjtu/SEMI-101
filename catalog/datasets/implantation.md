# D9 离子注入与退火

[数据覆盖矩阵](matrix.md) · [清洗与前处理](cleaning.md) · [封装与互连](packaging.md)

离子注入的数据有三种时间轴：机台调束或执行配方的时间、探测器记录单粒子的时间、注入后退火的工艺时间。深度剖面的横轴通常是距离。建模前先认清样本单位，再判断是否有同片量测。

| 编号 | 可下载内容 | 可关联到什么 |
| --- | --- | --- |
| E04 | 量产机调束特征与成败、耗时 | 按发布拆分与样本索引配对 |
| I01 | Ge 注入 GaN 的多段配方、SIMS 和 DFT 数据 | 配方到样片及退火状态；DFT 另按计算条件组织 |
| I02 | 单离子注入探测的计数、脉冲参数及氧化层厚度 | 按样片和测量页对照 |
| I03 | 晶态／非晶硅膜的离子通道化实验及仿真 | 按离子、能量和薄膜结构对照 |
| I04 | Crystal-TRIM 输入、输出及源代码 | 按模拟案例配对 |
| I05 | Se 注入 Ge 后的退火、RBS 与形貌 | 图号及处理条件 |
| I06 | 同位素硅注入，SIMS 与 TRIDYN | 图号、能量、注量及材料条件 |
| I07 | 宽禁带材料 DP-MD 势函数及掺杂深度输出 | 材料、模拟案例及重复序号 |

## E04 Infineon 离子束调束

**文件与字段。** `x_train.csv`、`y_train.csv`、`x_valid.csv`、`y_valid.csv`，另有发布者 Notebook。输入含 `equipment`、`current_recipe_1..5`、`upcoming_recipe_1..5`、`offset_recipe_1..5`、工程特征和设备信号汇总。输出为 `setup_result`、秒级 `duration` 和 `duration_interval`。数据 CC BY 4.0。[文件与字典](https://zenodo.org/records/11084332) · [作者 Notebook](https://zenodo.org/records/11084332/files/ionbeamtuning.ipynb) · [配套论文](https://doi.org/10.3233/FAIA241042)

**关联。** 训练 38,848 条、验证 9,713 条，两对 X/Y 在各自拆分内的首列索引逐行吻合，跨拆分会重号。合表用 `(split, index)`。这些样本对应配方切换的首次调束，发布字段中没有晶圆 ID、批次 ID 或原始传感器时序。部分配方字段匿名，数值的物理含义和单位应以设备记录为准。

## I01 Ge 注入 GaN

**文件与字段。** `Ion Implantation Parameters.txt` 给出样片 A1–A4、目标浓度和 60／120／230 keV 三段能量与面剂量。SIMS 表的成对列以样片和退火状态标注，物理量是深度（nm）与 Ge 浓度（cm⁻³）。还有 Hall、PL、XRD 和 DFT 数据。DFT 结果含迁移能垒与理论扩散系数。数据 CC BY 4.0。[RepOD 原始记录](https://doi.org/10.18150/SI2JQO) · [配方表](https://repod.icm.edu.pl/api/access/datafile/97537) · [SIMS](https://repod.icm.edu.pl/api/access/datafile/96485) · [DFT](https://repod.icm.edu.pl/api/access/datafile/96486) · [论文](https://doi.org/10.1016/j.mssp.2026.110540)

**关联。** 从 SIMS 列名提取样片号和退火状态，将样片号接到配方表。深度坐标是样片内量测轴。DFT 文件按迁移机制、电荷态或温度组织，可与实验现象做物理对照。发布说明列出 SIESTA、ASE 与 CI-NEB，发布包没有逐样片的计算输入或配套源代码。

## I02 锑单离子探测

**文件与字段。** 工作簿发布 25 keV Sb⁺、50 keV Sb²⁺ 的计数实验，含 `Sample`、`pulse width [ns]`、`Average I [fA]`、`total hits`、`total pulses`、`Corrected lambda`。厚度表有 `Sample number`、累计 SiO₂ 厚度与标准差。数据 CC BY 4.0。[发布记录与工作簿](https://zenodo.org/records/17804196) · [论文](https://doi.org/10.1021/acs.nanolett.5c05280)

**关联。** 按工作表内填充完整的 `Sample` 对照厚度表，分析时保留能量与测量页。计数在脉冲条件上汇总，适合研究氧化层厚度与探测效率。逐脉冲波形和逐晶圆剂量图需要另找来源。

## I03 硅膜离子通道化

**文件与字段。** 实验 TXT 的列包括 `Event #`、`Total Time (s)`、`# of Counts` 和最多四组位置／飞行时间（X、Y、ToF）。模拟 `.tra` 发布位置、方向、能量与轨迹状态；各模拟压缩包约 2–2.7 GB。数据 CC BY 4.0。[数据包](https://zenodo.org/records/15658828) · [论文](https://doi.org/10.1016/j.apsusc.2025.163734) · [IMSIL 仿真器说明](https://www.tuwien.at/en/etit/fke/research/process-simulation)

**关联。** 四组实测和四组仿真按入射离子、能量和 200 nm 硅膜的层序对照。实验与模拟各自生成粒子事件，比较时按工况和分布做验证。事件时间来自探测器。

## I04 Crystal-TRIM 注入模拟

**文件与字段。** RODARE ZIP 有 Fortran 源码和八组案例。案例用四字符名称把 `.IN`／`.DAT` 与 `.OUT`／`.1D1`／`*range.dat` 关联，输出包括深度、掺杂浓度或损伤。软件包 EUPL-1.2。[源代码与八组案例](https://doi.org/10.14278/rodare.5102) · [模型论文](https://doi.org/10.1149/1.1837618)

若需跨材料复算输运，可以对照 [RustBCA](https://github.com/lcpp-org/RustBCA) 的 BCA 算法和输入格式，代码 GPL-3.0。拿实验 SIMS 对照预测时，应先统一剂量归一化、深度标定与退火状态。[RustBCA 论文](https://doi.org/10.21105/joss.03298)

## I05 Se 注入 Ge 与退火

论文给出 150 keV、面剂量 6 × 10¹⁵ cm⁻²、倾角 7° 的固定注入条件，并比较不同退火方式。拉曼 CSV 记录 `Wavenumber (cm-1)` 与退火分组，RBS CSV 记录 `Energy (MeV)` 与处理前后计数。发布另有白光干涉形貌 `.fibps` 和 SEM `.tif`。按图号和处理条件复核，无统一逐片键。数据 CC BY 4.0。[数据](https://zenodo.org/records/12567660) · [论文](https://doi.org/10.1063/5.0213637)

## I06 同位素硅注入与自溅射

实验 `Fig2a_experimental_data.dat` 含温度、通量档、能量（keV）、注量和膨胀／收缩（nm）。`Fig3a.dat` 是 SIMS 深度（nm）与硅同位素浓度（ppm）。TRIDYN 结果另有注量与膨胀、同位素浓度。通过图号和工况比对，先换算 Å、nm 及面注量单位。包内有绘图脚本 `FigS0.py`，求解器许可另查。数据 CC BY-NC-ND 4.0。[数据与脚本](https://doi.org/10.26188/29275775.v2) · [论文](https://doi.org/10.1103/787r-9jps)

## I07 宽禁带材料 DP-MD 注入深度

Figshare 发布势函数表、`Dopant-profile.xlsx`、50 次模拟的深度／计数文件 `range_md-*`，并提供 `batch.sh` 和汇总到 `depth.txt` 的脚本。作者说明计算使用 LAMMPS。按材料、模拟设置和重复编号选择输出，适合比较不同建模假设下的深度分布。数据 CC BY 4.0。[输入、脚本与仿真输出](https://doi.org/10.6084/m9.figshare.27747795.v2) · [论文](https://doi.org/10.1016/j.surfin.2025.106140)

## 量产数据缺口

目前可分别研究调束、受控注入实验和模拟输出。按同一晶圆关联的束流、扫描位置、剂量积分与片内剂量或片阻图仍缺少公开例子。用深度剖面校准注入物理时，先比较相同离子、靶材、能量、面剂量、倾角和退火条件。

[回到数据集目录](../datasets.md)
