# D10 封装与互连

[数据覆盖矩阵](matrix.md) · [离子注入与退火](implantation.md) · [量测与缺陷](metrology.md)

封装数据可来自贴装或键合设备、后续无损检测、可靠性试验，或热仿真。先确认文件记录的是哪台设备，再区分实物、模拟与公开的统计结果。按封装件或试样关联的数据在本章写明实际单位。

| 编号 | 工序 | 可下载证据 | 关联粒度 |
| --- | --- | --- | --- |
| K01 | 先进封装 XCT | 检测设定、实验投影、重建和模拟输出 | 视场＋扫描名，模拟另按模型 |
| K02 | 芯片到晶圆混合键合 | 键合能和表面接触角的数字化数据、良率模型 | 各自的试验条件，两个试验分开 |
| K03 | 功率模块封装热分析 | HDF5 温度场、热源、掩膜与清单 | 拓扑＋样本路径 |
| K04 | 工业封装 X 光缺陷检测 | 公开子集及标签 | 图像名 |
| K05 | 倒装芯片超声显微检测 | 一份原始 C-scan 及焊点特征 | 封装样品 |
| K06 | 陶瓷封装基板光学检测 | 制造工序图像和缺陷标注子集 | 基板类别＋图像名 |
| K07 | 铜铜热压键合 | 键合条件、应力应变与微结构源数据 | 工况组与试样编号 |

## K01 NIST 先进封装 XCT

NIST 在 Zeiss Xradia Versa XRM 500 上扫描 Tesla P100 封装。发布覆盖 BGA、RDL、TSV、C4 和微凸点等结构。文件按视场、像素尺寸与扫描名称组织。以 `FOV2_PixSz_7p00um` 为例，配方截图 `recipe_Test1_160kv_pixsz7p0.PNG` 与同名 `.txrm` 投影、`*_shifts.csv` 位移表和 `recon_*.txm` 重建文件对应。部分扫描另有 `temperature_history_*.bmp`。README 和配方截图可读，参数 ODS 和位移 CSV 的端点抽查返回错误。[数据 DOI](https://doi.org/10.18434/mds2-4172) · [文件目录](https://data.nist.gov/od/id/mds2-4172) · [实验文件说明](https://data.nist.gov/cch/fst3/mds2-4172/Experiments_XCT_P100_GPU/ReadMe_XCT_Experiments.txt) · [已核对的配方截图](https://data.nist.gov/cch/fst2/mds2-4172/Experiments_XCT_P100_GPU/FOV2_PixSz_7p00um/recipe_Test1_160kv_pixsz7p0.PNG) · [NIST 数据条款](https://www.nist.gov/open/license)

模拟以简化的封装结构生成数值投影与重建，适合对照伪影和可检出的结构尺度。实测与模拟可按结构类型、尺寸和扫描设置比较，文件没有逐体素的实验／仿真配准。作者发布了 [xsim-chip](https://github.com/usnistgov/xsim-chip) 代码。检测机的投影序列记录的是成像过程，键合或贴装机执行时序需要另找。

## K02 芯片到晶圆混合键合

复现 ZIP 中的 `fq_tcpmt2025_digitized.csv` 记录文献图中储存时间与键合能。另一份 `s6c_guo2024_digitized.csv` 含 `substrate`、`native_deg`、`ashed_deg`、`aged_3h_deg`、`aged_24h_deg`。两个表来自不同实验，分别按储存时间或基材、表面处理条件解读。包内有 Python 包装脚本、模型输出和日志，以固定版本 YAP+ 复算。数据页 CC BY 4.0，代码条款以各上游为准。[复现包](https://zenodo.org/records/22686628) · [模型基准论文](https://doi.org/10.1109/TCPMT.2025.3636933) · [YAP+](https://github.com/nanocad-lab/YAP)

这里可比较储存或排队条件的模型影响，晶圆对晶圆的逐片键合强度、对准偏差、缺陷图与良率需要独立数据。另有 CERN 超薄混合组件报告可用于查试验设计，公开包是报告 Word 文件。[CERN 技术报告](https://zenodo.org/records/17698520)

## K03 功率模块封装热仿真

作者仓库的 `metadata/manifest.csv` 含 `split`、`topology`、`mask_id`、`Pigbt`、`Pfwd`、`h_value` 和 `path`。按 `path` 打开单样本 HDF5，可取温度场、热源、区域掩膜与芯片最高温。适合做温度场代理模型，并按拓扑留出评估。发布包包含读取示例，作者说明用 CADQuery 和 COMSOL／MATLAB 有限元生成，未给出同封装件的实测温度。数据 CC BY 4.0，配套稿件信息见仓库 `CITATION.cff`。[数据、样本与脚本](https://github.com/henkuailederen/Multi-topology-Dataset)

## K04 工业封装 X 光气泡缺陷

CXray 来自封装缺陷检测研究。公开 Google Drive 目录可见 `JPEGImages.zip` 与 `labels.zip`，按图像名连接 PNG 与对应缺陷标注，核对到 1,960 对。标签 ZIP 的 YOLO TXT 字段为归一化的类别和边界框（类别、中心 X、中心 Y、宽、高）。配方、键合参数与封装批次的关联字段在公开说明中没有确认。作者声明 CC BY，未标版本。[作者发布与获取说明](https://github.com/EudicL/CXray) · [论文](https://doi.org/10.3390/electronics12143060)

## K05 倒装芯片超声显微检测

FA10 样品的 `Figure 1.bmp` 是 403 × 403 的 C-scan，`Table 1.docx` 有 317 行焊点特征，列名为 `X`、`N`、`M`、`P`、`S²`、`K`，物理含义见论文。两份文件可以按同一封装样品归组。特征表没有凸点坐标或 ID，若做像素级分割，需要另标图像。数据 CC BY 4.0。[数据与原始图](https://data.mendeley.com/datasets/9n5z75smz3/1) · [论文](https://www.sciencedirect.com/science/article/pii/S0026271416303183)

## K06 陶瓷封装基板 AOI

CPS2D-AD 的场景包含陶瓷基板冲孔、填孔和印刷。作者公开的 `CPS-AD2D.zip` 有 3,735 对 JPG 和 PNG，按 `cps_1…cps_6 + basename` 关联图像和掩膜。部分样本的图像和掩膜放在不同拆分目录，连接键无需目录中的 split。论文描述的框标签未在该公开 ZIP 中确认。未确认能按图像拼接上游设备配方或基板批次。发布方声明 CC BY 4.0。[公开子集入口](https://github.com/Bingyang0410/CPS2D-AD) · [ICCV 论文](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Anomaly_Detection_of_Integrated_Circuits_Package_Substrates_Using_the_Large_ICCV_2025_paper.pdf)

## K07 铜铜热压键合

作者源工作簿的 `Figure 4o` 按工况给 `Strain (%)`／`Stress (MPa)` 曲线，例如 `DL-100 °C/30 min` 与 `DL-100 °C/60 min`。 `Figure 4p` 按相同工况给 `Sample 1…3` 的键合应力，可据工况组对照。 `Figure 3c` 另有 `Depth (nm)` 及元素信号。 `Figure 2b` 的 `Time (min)` 是独立材料试验的归一化电阻量测。工况组可比较温度和保温时间，跨图没有共享 wafer ID。论文 CC BY-NC-ND 4.0，工作簿独立许可未确认。[论文](https://doi.org/10.1038/s41467-024-51510-7) · [已核对的源 XLSX](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-024-51510-7/MediaObjects/41467_2024_51510_MOESM5_ESM.xlsx)

## 仍待补充的工序

- **晶圆减薄、切割。** 研究中有划片电流与崩边结果的配对线索，暂未核对到公开的原始机台文件。[划片信号研究](https://www.mdpi.com/2227-7390/10/24/4631) · [CHDL 切割图像申请线索](https://arxiv.org/abs/2507.06738)
- **引线键合、贴片、混合键合。** 优先找带设备设置、力／超声功率／位移波形和拉力、剪切或空洞标签的数据。已有 OSAT 引线键合 FDC 研究描述不同配方的数据采集，文件按作者说明申请。开源引线键合 AOI 实现提供替代演示数据，实拍数据为私有。 [引线键合 FDC](https://www.techscience.com/cmc/v88n1/67302/html) · [AOI 代码与数据声明](https://github.com/jacomof/aoi-ssl)
- **超声显微检测。** UltraChip 提供封装 C-scan 研究数据的申请入口，作者要求签署协议。[访问条件](https://iiplab.net/ultrachip/)

[回到数据集目录](../datasets.md)
