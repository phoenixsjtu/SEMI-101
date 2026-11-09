# 代码索引

按工程任务查上游实现。这里的链接指向各项目自己的代码和说明。使用前核对上游版本、环境与数据条款，研究实现的运行结果以实际复现为准。

## 仿真与虚拟设备

| 想做什么 | 上游实现 | 使用前看什么 | 代码许可 |
| --- | --- | --- | --- |
| 计算 ALD／ALE 反应器内的传质与自限反应 | [aldFoam](https://github.com/aldsim/aldFoam) | 主分支面向 OpenFOAM 10，先看设备几何和边界条件 | GPL-3.0 |
| 计算刻蚀或沉积后的表面形貌 | [ViennaPS](https://github.com/ViennaTools/ViennaPS) | 根据任务选择 C++ 或 Python 接口，核对粒子通量和表面反应输入 | GPL-3.0 |
| 把反应机理整理成模拟器能读的模型 | [ViennaChem](https://github.com/ViennaTools/ViennaChem) | 与 ViennaPS 配合时核对反应式和速率参数 | GPL-3.0 或更新版本，详见上游许可 |
| 在虚拟沉积环境试验优化策略 | [aldenv](https://github.com/aldsim/aldenv) | 从仿真设备接口入手，核对环境状态、动作和观测 | BSD-3-Clause |
| 用仿真膜厚剖面研究 PEALD 饱和剂量 | [Plasma ALD Dataset 与脚本](https://github.com/aldsim/plasmaml) | 先看数据定义与已有切分 | 开放许可未确认 |
| 从模拟剖面与剂量预测 ALD 饱和时间 | [ALD Saturation](https://github.com/aldsim/saturationdataset) | 读取发布的 NumPy 文件，比较不同网络深度的作者训练脚本 | MIT |
| 用掩模预测光刻成像，或从目标图案反推掩模 | [LithoBench](https://github.com/shelljane/lithobench) · [LithoSim](https://dw-hongquan.github.io/LithoSim/) | 分别核对版图子集、参考求解器和评估指标。两套数据的许可各自核对 | LithoBench MIT，LithoSim Apache-2.0 |

[对应学习专题](../learn/design.md) · [设备设计完整资源](design.md)

## 工艺预测与诊断

| 想做什么 | 上游实现 | 使用前看什么 | 代码许可 |
| --- | --- | --- | --- |
| 从完整刻蚀轨迹预测刻蚀深度 | [BOSCH Etch Virtual Metrology](https://github.com/cpngfan-ui/bosch-etch-virtual-metrology) | 另取 BOSCH 数据，核对周期特征和按批次留出的验证 | MIT |
| 预测片内台阶高度并筛选需要量测的晶圆 | [ETCH-GATE](https://github.com/JUYONG-1010/ETCH-GATE) | 另取 BOSCH 数据，核对空间量测定义与筛选预算 | MIT |
| 预测 ICP 刻蚀设备的等离子体光学响应 | [Generative Modelling for Optical Plasma Diagnostics](https://github.com/gregdaly/generative_modelling_for_optical_plasma_diagnostics) | 对照 PP100 配套数据和作者的光谱、图像模型 | MIT |
| 用归一化工艺参数预测光电晶体管增益 | [FBK Phototransistor Virtual Metrology](https://github.com/mahshid-amirabgir/phototransistor-virtual-metrology) | 按工艺运行切分，区分正向增益估计和反向配方搜索 | MIT |

[对应学习专题](../learn/process.md) · [工艺智能完整资源](process.md) · [配套数据入口](datasets.md#工艺轨迹光谱和量测)

## 设备接入与故障分析

| 想做什么 | 上游实现 | 使用前看什么 | 代码许可 |
| --- | --- | --- | --- |
| 在开发环境模拟设备与主机通信 | [secsgem](https://github.com/bparzella/secsgem) | Python 的设备、主机示例与事件回调 | LGPL-2.1 |
| 在 .NET 中处理 SECS-II／HSMS-SS／GEM 消息 | [Secs4Net](https://github.com/mkjeff/secs4net) | 从上游示例确认消息格式和连接配置 | MIT |
| 整理 LAM 9600 刻蚀设备数据 | [Eigenvector Metal Etch Data Parser](https://github.com/jaganadhg/egvsemicon) | 另取 MATLAB 数据，核对转换后的晶圆标识和故障标签 | Apache-2.0 |
| 分析离子束刻蚀设备故障与剩余寿命 | [Ion Mill Etch 3-Stage PdM](https://github.com/ki-seoultech/PHM2018-Ion-Mill-Etch-3Stage-Predictive-Maintenance) | 从 PHM 2018 官方入口另取原始数据，核对脚本所需的派生输入 | MIT |

[对应学习专题](../learn/operations.md) · [设备运维完整资源](operations.md) · [配套数据入口](datasets.md#故障与健康管理)

## 清洗、涂显、注入与封装案例

| 任务 | 实现与对应数据 | 代码许可 |
| --- | --- | --- |
| 读取清洗后 XPS 的 VAMAS 原始文件 | [vamas 读取器](https://github.com/matkrin/vamas) · [清洗专题和已读样本](datasets/cleaning.md) | BSD-3-Clause |
| 机器人显影与膜厚分析 | [Stanford ROS 2／MoveIt 与分析脚本](https://github.com/alps-ml/paper.robotic-resist-development) · [C01 芯片数据](datasets/coat-develop.md#c01-stanford-机器人显影) | MIT |
| 从曝光场计算胶层与显影 | [TorchResist](https://github.com/ShiningSord/TorchResist) · [涂显仿真入口](datasets/coat-develop.md#显影建模与量测参照) | Apache-2.0 |
| 建模离子输运与深度剖面 | [Crystal-TRIM 源码与案例](https://doi.org/10.14278/rodare.5102) · [RustBCA](https://github.com/lcpp-org/RustBCA) · [注入专题](datasets/implantation.md) | Crystal-TRIM EUPL-1.2；RustBCA GPL-3.0 |
| 模拟封装 X 射线投影与重建 | [NIST xsim-chip](https://github.com/usnistgov/xsim-chip) · [K01 实测与仿真](datasets/packaging.md#k01-nist-先进封装-xct) | [NIST 软件许可](https://github.com/usnistgov/xsim-chip/blob/main/LICENSE.md) |

[学习导航](../README.md)
