# 数据集总览

按数据怎么来的、包含什么信号以及能回答什么问题来选。对同一任务，单传感器基准可以快速检验算法，带配方、腔室和量测的实测数据更适合检验工艺解释。数据按发布方版本和条款获取。

## 仿真与设计

| 数据 | 设备与数据形态 | 可验证的任务 | 获取与许可 |
| --- | --- | --- | --- |
| [Surface Chemistry as Data](https://researchdata.tuwien.ac.at/records/azegw-xq879) | 刻蚀、ALD、MOCVD 等场景的化学模型、形貌仿真输出和脚本 | 特征尺度表面反应与形貌预测 | 数据 CC BY 4.0，脚本许可见发布记录 |
| [Argonne Plasma ALD Dataset](https://github.com/aldsim/plasmaml) | PEALD 高深宽比结构的仿真膜厚剖面 | 估计达到饱和所需的相对剂量时间 | 仓库提供数据和脚本，开放许可未确认 |

## 工艺轨迹、光谱和量测

| 数据 | 设备与数据形态 | 可验证的任务 | 获取与许可 |
| --- | --- | --- | --- |
| [BOSCH Plasma Etching](https://zenodo.org/records/17122442) | 深硅刻蚀设备实测 OES、工艺轨迹和晶圆空间量测 | 刻蚀深度预测、片内均匀性、过程阶段分析 | 可下载，CC BY 4.0 |
| [PP100 ICP 光学诊断数据](https://zenodo.org/records/7704879) | ICP 刻蚀设备实测工艺设定、光谱和图像 | 估计不同配方下的等离子体光学响应 | 可下载，CC BY 4.0 |
| [PHM 2016 CMP](https://phmsociety.org/wp-content/uploads/2016/05/PHM16DataChallengeCFP.pdf) | CMP 挑战赛，按晶圆和加工阶段关联设备轨迹与平均材料去除率 | 材料去除率预测、按晶圆验证 | 公告指向外部下载页，数据再分发许可未确认 |
| [PVD AlCu / WTi](https://zenodo.org/records/16881338) | PVD 设备测试的工艺信号汇总与薄膜量测 | 膜厚预测，评估设备与批次差异 | v1 覆盖 AlCu 和 WTi，[v2](https://zenodo.org/records/23442538)更新 AlCu 并提供更多标识，两版均为 CC BY 4.0 |
| [NIST ALD Hafnia on Silicon](https://catalog.data.gov/dataset/nanometer-scale-planar-reference-materials-project-data-year-2025-set-00-10nm-hafnia-on-si) | ALD HfO₂ 参考样品的椭偏与 X 射线反射量测 | 比较薄膜量测方法、点位和不确定度 | 可下载，依 [NIST 开放条款](https://www.nist.gov/open/license) |
| [Semiconductor Frontend Equipment Sensor Data](https://zenodo.org/records/4322353) | 两台匿名前道设备的多变量轨迹与晶圆测试结果 | 按晶圆及批次关联设备记录，探索质量预测和跨工序异常 | 可下载，CC BY 4.0 |
| [UCI SECOM](https://archive.ics.uci.edu/dataset/179/secom) | 1,567 条匿名生产实体记录、591 个工艺测量特征和通过／失败标签 | 缺失值处理、特征选择、类不平衡分类 | 可下载，CC BY 4.0 |

## 故障与健康管理

| 数据 | 设备与数据形态 | 可验证的任务 | 获取与许可 |
| --- | --- | --- | --- |
| [Eigenvector Metal Etch](https://eigenvector.com/resources/data-sets/) | LAM 9600 金属刻蚀机的实测工程变量，含故障注入 | 多变量异常检测、跨实验批次验证 | 发布方提供 MATLAB 文件，许可未确认 |
| [UCR Wafer](https://zenodo.org/records/11198387) | 每条序列对应一片晶圆的一路设备传感信号，带正常／异常标签 | 单变量时序分类、类不平衡基线 | UCR 归档版本可下载，CC BY 4.0 |
| [PHM 2018 Ion Mill](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2018-b/phm-data-challenge-6/) | 离子束刻蚀设备冷却子系统的运行信号、配方与故障时间 | 三类故障的失效时间或 RUL 估计 | 官方页提供外部下载入口，数据许可未确认 |

选定数据后，可以回到[设备设计](design.md)、[工艺智能](process.md)或[设备运维](operations.md)找对应论文和代码。
