# D5 工艺物理仿真

[数据集目录](../datasets.md) · [多物理场仿真](../../learn/methods.md#t1-多物理场仿真) · [仿真加速](../../learn/applications.md#a1-仿真加速)

这里收录能找到生成样本、基准或复现材料的工艺仿真。比较代理模型时，要同时记录求解器和模型假设、输入扫参范围、输出类型及分辨率。一个轮廓序列、一张光刻图和一个气相浓度场需要不同的验证方式。

## ALD 与刻蚀

| 编号 | 数据 | 仿真输入与输出 | 访问与许可 |
| --- | --- | --- | --- |
| S01 | [TU Wien Surface Chemistry as Data](https://researchdata.tuwien.ac.at/records/azegw-xq879) | 刻蚀、ALD、MOCVD 等表面反应模型、配置和形貌仿真输出。用工艺配置及案例文件关联 | 数据 CC BY 4.0，脚本依发布记录 |
| S02 | [Argonne PEALD](https://github.com/aldsim/plasmaml) | 高深宽比特征内的两条模拟膜厚剖面、反应与复合概率，对应达到饱和所需的剂量倍数 | 数据文件可见，许可未确认 |
| S03 | [Argonne ALD Saturation](https://github.com/aldsim/saturationdataset) | 模拟膜厚剖面、已用剂量时间及目标饱和时间，分训练与测试 NumPy 文件。与 S02 的输入、目标及发布文件不同 | 仓库根许可为 MIT。[论文](https://arxiv.org/abs/2205.08378) |
| S04 | [多工步等离子体刻蚀轮廓](https://github.com/JimmyxGuo/Predictive-Modeling-of-Plasma-Etching) | 两种截面的轮廓 PNG 序列，和按样本对应的条件向量 XLSX。适合验证跨工况的轮廓预测。轮廓生成方法待从原论文确认 | 仓库根许可为 MIT，数据条款以发布方说明为准 |

## 光刻成像与掩模

| 编号 | 数据 | 仿真输入与输出 | 访问与许可 |
| --- | --- | --- | --- |
| S05 | [LithoBench](https://github.com/shelljane/lithobench) | 电路版图切片、优化掩模、空间像和光刻胶图，任务为正向光刻建模与逆向掩模优化 | 作者仓库给出独立下载入口。使用数据时查数据包与仓库条款。[论文](https://papers.neurips.cc/paper_files/paper/2023/hash/604b9fa9e1c16284e6517d923cf9ff20-Abstract-Datasets_and_Benchmarks.html) |
| S06 | [LithoSim](https://dw-hongquan.github.io/LithoSim/) | 作者发布的大规模光刻仿真基准，按版图与工况对照仿真结果，任务涵盖正向建模与逆向优化 | 数据 CC BY-NC 4.0，代码 Apache-2.0 |
| S07 | [LithoBench-PDE](https://huggingface.co/datasets/AISDL-SNU/LithoBench-PDE) | 复用部分 LithoBench 版图重新生成光刻物理场，输出新增，版图来源继承。联合比较时需防止布局重叠 | 具体场数据和软件的许可分项见数据卡 |

## 溅射粒子输运

**S08 Cu、Ti、W 在 Ar 中的 Monte Carlo 输运。** 数据含溅射原子抵达面的能量／角度样本，分不同设置、对照计算和生产计算包。可比较输运条件与沉积通量分布的关系，适用于输运模型的验证。数据 CC BY 4.0。[仿真数据与代码](https://zenodo.org/records/23839621)

## 如何对照与复现

- **按输入组合留出。** 同一几何的所有时间帧保持在同一划分；如果关注新几何，就按结构族留出。光刻基准间复用版图时以原始版图为分组。
- **拆开求解器误差与代理误差。** 先比较代理输出与同工况的数值结果，再用实测数据评估设备适用性。若只有仿真数据，报告验证止于所选求解器和输入范围。
- **分开基准与生成工具。** [PythonDryEtchModel](https://github.com/tanglab-stanford/PythonDryEtchModel)可作为特定设备轮廓建模的代码入口，[NIST MoCl₅ 输运数字孪生](https://www.nist.gov/publications/cfd-based-digital-twin-framework-transient-mocl5-transport-experimental-atomic-layer)可用于追踪 CFD 与原位实验的校准做法。

[上一节 设备状态与运维](health.md) · [下一节 晶圆厂仿真与调度](fab.md)
