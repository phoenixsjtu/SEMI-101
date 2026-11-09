# 工艺智能

工艺智能关心设备如何把配方变成合格的晶圆。设备按配方设定功率、流量、压力或时间，传感器记录实际运行过程，量测设备随后给出膜厚、刻蚀深度或套刻误差等结果。把这些信息按晶圆、批次、腔室和配方版本关联起来，才能追查哪些变量与工艺结果有关，以及什么时候需要重新量测或修正配方。

- 初次接触工艺数据，可以从 CMP 挑战赛的设备图和字段表读起，理解同一片晶圆的轨迹如何关联到材料去除率。[PHM Society CMP 任务说明](https://phmsociety.org/wp-content/uploads/2016/05/PHM16DataChallengeCFP.pdf)
- 想找能同时看到设备轨迹、光谱和晶圆量测的数据，可以看 BOSCH 等离子刻蚀的发布页和数据字典。[BOSCH 刻蚀数据](https://zenodo.org/records/17122442)
- 想了解虚拟量测如何参与生产决策，可以从半导体 VM 综述进入，再按设备类型查阅下面的案例。[半导体虚拟量测综述](https://doi.org/10.1016/j.eswa.2024.123559)

## 配方开发与闭环控制

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| 等离子刻蚀腔室 | 在虚拟工艺中比较专家与贝叶斯优化的配方搜索策略，并衡量达到工艺规格所需的试验成本 | 论文 | [Kanarik 等 · 人机协作开发刻蚀工艺](https://www.nature.com/articles/s41586-023-05773-7) | 论文 CC BY 4.0，部分图表源数据可下载，模拟器演示需联系作者 |
| 工业等离子刻蚀腔室 | 用等离子阻抗估计电子密度，并用模型预测控制应对腔室扰动 | 论文 | [Lynn 等 · 实时虚拟量测与电子密度控制](https://doi.org/10.3182/20110828-6-IT-1002.03199) | 出版方页面，按 IFAC 条款 |
| CMP 抛光设备 | 将设备状态加入逐次控制（R2R），分析工况变化对材料去除率控制的影响 | 论文 | [Advanced run-to-run controller with real-time equipment condition](https://doi.org/10.1109/ASMC.2018.8373161) | 出版方页面，按 IEEE 条款 |
| 工艺控制系统与设备接口 | 查阅自动工艺控制系统（APC）接口的定义 | 标准 | [SEMI E133 · Automated Process Control Systems Interface](https://store-us.semi.org/products/e13300-semi-e133-specification-for-automated-process-control-systems-interface) | 摘要公开，正文按 SEMI 授权获取 |
| 工艺模块与基片跟踪 | 了解设备怎样向工厂系统报告配方步骤和基片加工事件 | 标准 | [SEMI E157 · Module and Substrate Process Tracking](https://store-us.semi.org/products/e15700-semi-e157-specification-for-module-process-tracking) | 摘要公开，正文按 SEMI 授权获取 |

## 虚拟量测与统计过程监控

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| CMP、刻蚀、沉积等工艺设备 | 按工艺和模型梳理虚拟量测（VM），理解采样、模型更新和设备差异带来的部署问题 | 综述 | [Maitra 等 · Virtual metrology in semiconductor manufacturing](https://doi.org/10.1016/j.eswa.2024.123559) | 出版方页面，全文按 Elsevier 条款获取 |
| CMP 抛光设备 | 用在线高斯过程跟踪去除率预测中的漂移，并依据不确定度安排量测 | 论文 | [Han 等 · 半导体虚拟量测与动态采样](https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic) | NIST 提供论文下载入口，复用按文中权利说明 |
| 光刻设备 | 用设备数据预测晶圆套刻误差，为逐次反馈控制补充量测信息 | 论文 | [Kang 等 · Virtual metrology for run-to-run control](https://doi.org/10.1016/j.eswa.2010.08.040) | 出版方页面，全文按 Elsevier 条款获取 |
| CVD 沉积设备 | 比较多种配方下的虚拟量测表现，用滚动窗口与维护记录组织模型更新 | 论文 | [Rolling-window and production-maintenance-based virtual metrology](https://doi.org/10.1109/TASE.2025.3570863) | 出版方页面，按 IEEE 条款 |
| 批次式半导体加工设备 | 将轨迹转成批次统计量，用于统计过程监控与异常检测 | 论文 | [He 与 Wang · Statistics Pattern Analysis](https://doi.org/10.1002/aic.12247) | 出版方页面，按 AIChE 和 Wiley 条款 |
| 半导体设备逐次控制环 | 用预测可信度与相似性判断是否把虚拟量测纳入反馈，并在仿真中检验设备变化后的控制效果 | 论文 | [Run-to-Run Control Utilizing Virtual Metrology With Reliance Index](https://doi.org/10.1109/TSM.2012.2228243) | 出版方页面，按 IEEE 条款 |
| 封装超声键合机 | 从已有设备信号、工艺参数和时序特征预测键合剪切力 | 论文 | [Buchner 等 · Shear force quality prediction of ultrasonic wire bonds](https://doi.org/10.1007/s00170-024-14055-z) | 论文 CC BY 4.0，研究数据未随文提供 |

## 工艺轨迹与量测数据

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| BOSCH 深硅等离子刻蚀设备 | 结合设备轨迹、原位光发射光谱（OES）和空间量测，研究刻蚀深度、选择比与片内均匀性 | 实验数据集 | [TU Chemnitz 与 Fraunhofer · BOSCH Plasma Etching](https://zenodo.org/records/17122442) | 可下载 NetCDF、CSV 和文档，CC BY 4.0 |
| CMP 抛光设备 | 以晶圆和加工阶段关联设备轨迹与平均材料去除率，建立虚拟量测基准 | 挑战赛数据集 | [PHM 2016 CMP · 官方任务与下载入口](https://phmsociety.org/wp-content/uploads/2016/05/PHM16DataChallengeCFP.pdf) | 公告指向第三方下载页，未标注再分发许可 |
| PVD 溅射设备 | 用配方与设备信号统计量预测 AlCu、WTi 膜层量测。更新版 AlCu 另有晶圆、批次与设备字段 | 设备测试数据集 | [PVD APC/SPC v1 · AlCu 与 WTi](https://zenodo.org/records/16881338) · [v2 · 更新的 AlCu 文件](https://zenodo.org/records/23442538) | 两版均可下载 CSV，CC BY 4.0 |
| Gemstar XT ALD 与薄膜量测 | 用 HfO₂ 薄膜的椭偏和 X 射线反射数据比较片内与跨批量测，理解量测点位和不确定度 | 实验数据集 | [NIST · ALD Hafnia on Silicon, Set 00](https://catalog.data.gov/dataset/nanometer-scale-planar-reference-materials-project-data-year-2025-set-00-10nm-hafnia-on-si) | 数据公开下载，按 [NIST 开放条款](https://www.nist.gov/open/license) |
| 两台匿名半导体前道设备 | 将多变量轨迹与晶圆测试结果按批次和晶圆标识关联，练习质量预测与跨工序排查 | 设备轨迹数据集 | [Equipment Sensor Data from Semiconductor Frontend Production](https://zenodo.org/records/4322353) | 可下载 ZIP，CC BY 4.0 |
| 匿名半导体制造工序 | 用工艺测量特征预测通过或失败，比较缺失值处理与不平衡分类方法 | 表格数据集 | [UCI SECOM](https://archive.ics.uci.edu/dataset/179/secom) | 可下载，CC BY 4.0 |
| Oxford Instruments PP100 ICP 刻蚀设备 | 用工艺设定、光发射光谱和图像建立配方到等离子状态的代理模型 | 实验数据集 | [Daly 等 · ICP 光学诊断数据](https://zenodo.org/records/7704879) | 可下载，CC BY 4.0 |

## 上游代码

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| BOSCH 等离子刻蚀设备 | 从完整刻蚀轨迹提取周期特征，比较硅刻蚀深度预测模型并按批次留出验证 | 开源代码 | [BOSCH Etch Virtual Metrology](https://github.com/cpngfan-ui/bosch-etch-virtual-metrology) | 代码 MIT，数据需从 Zenodo 获取 |
| BOSCH 等离子刻蚀设备 | 预测片内台阶高度分布，并比较有限量测预算下的晶圆筛选策略 | 开源代码 | [ETCH-GATE](https://github.com/JUYONG-1010/ETCH-GATE) | 代码 MIT，数据许可独立 |
| Oxford Instruments PP100 ICP 刻蚀设备 | 通过自编码器学习工艺设定与等离子光谱、图像之间的关系，探索在线诊断所需的代理模型 | 作者开源代码 | [Generative Modelling for Optical Plasma Diagnostics](https://github.com/gregdaly/generative_modelling_for_optical_plasma_diagnostics) · [配套 ICP 数据](https://zenodo.org/records/7704879) | 代码 MIT，配套数据 CC BY 4.0 |

## 用这些资源做验证

- **先确定预测时点。** 整段运行结束后才能得到的特征适合做工后虚拟量测。若要做运行中预警或终点检测，特征应在该决策时点之前已经可用。
- **按工艺结构留出数据。** 同一片晶圆的多个量测点、同一批次的晶圆和同一腔室的相邻批次可能高度相关。做片内预测时至少按晶圆分组，验证跨批、跨腔室或长期使用时应再按相应的批次、腔室或时间段留出。
- **核对量测定义。** 刻蚀深度、台阶高度、CMP 材料去除率和膜厚属于不同的物理量。对照单位、点位、基准面和量测方式，再比较模型误差。ALD 的公开条目侧重薄膜量测，光刻条目侧重套刻控制方法。
- **核对可追溯性。** SECOM 的匿名特征可以用来比较算法。要做设备根因分析，还需要可追溯的传感器、配方步骤和维修或试验记录。
