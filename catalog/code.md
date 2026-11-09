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

[对应学习专题](../learn/design.md) · [设备设计完整资源](design.md)

## 工艺预测与诊断

| 想做什么 | 上游实现 | 使用前看什么 | 代码许可 |
| --- | --- | --- | --- |
| 从完整刻蚀轨迹预测刻蚀深度 | [BOSCH Etch Virtual Metrology](https://github.com/cpngfan-ui/bosch-etch-virtual-metrology) | 另取 BOSCH 数据，核对周期特征和按批次留出的验证 | MIT |
| 预测片内台阶高度并筛选需要量测的晶圆 | [ETCH-GATE](https://github.com/JUYONG-1010/ETCH-GATE) | 另取 BOSCH 数据，核对空间量测定义与筛选预算 | MIT |
| 预测 ICP 刻蚀设备的等离子体光学响应 | [Generative Modelling for Optical Plasma Diagnostics](https://github.com/gregdaly/generative_modelling_for_optical_plasma_diagnostics) | 对照 PP100 配套数据和作者的光谱、图像模型 | MIT |

[对应学习专题](../learn/process.md) · [工艺智能完整资源](process.md) · [配套数据入口](datasets.md#工艺轨迹光谱和量测)

## 设备接入与故障分析

| 想做什么 | 上游实现 | 使用前看什么 | 代码许可 |
| --- | --- | --- | --- |
| 在开发环境模拟设备与主机通信 | [secsgem](https://github.com/bparzella/secsgem) | Python 的设备、主机示例与事件回调 | LGPL-2.1 |
| 在 .NET 中处理 SECS-II／HSMS-SS／GEM 消息 | [Secs4Net](https://github.com/mkjeff/secs4net) | 从上游示例确认消息格式和连接配置 | MIT |
| 整理 LAM 9600 刻蚀设备数据 | [Eigenvector Metal Etch Data Parser](https://github.com/jaganadhg/egvsemicon) | 另取 MATLAB 数据，核对转换后的晶圆标识和故障标签 | Apache-2.0 |
| 分析离子束刻蚀设备故障与剩余寿命 | [Ion Mill Etch 3-Stage PdM](https://github.com/ki-seoultech/PHM2018-Ion-Mill-Etch-3Stage-Predictive-Maintenance) | 从 PHM 2018 官方入口另取原始数据，核对脚本所需的派生输入 | MIT |

[对应学习专题](../learn/operations.md) · [设备运维完整资源](operations.md) · [配套数据入口](datasets.md#故障与健康管理)

[学习导航](../README.md)
