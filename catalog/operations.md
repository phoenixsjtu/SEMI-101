# 设备运维

运维智能化要判断设备发生了什么、工程师有多少提前量，以及应该检查哪个部件。通常要把配方步骤、腔室、设备事件、传感器和维修记录对齐，再区分工况变化、工艺异常与部件失效。

初学可以从 SEMI 的设备通信导读了解事件和数据如何产生，用 LAM 9600 数据练习按晶圆检测异常，再读 PHM 2018 的任务说明，了解异常检测与剩余寿命估计的差别。

## 设备接入与可靠性

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| 前道设备与工厂主机 | 理解 GEM 设备行为、事件和状态报告，以及 SECS-II 与 HSMS 的职责 | 技术资料 | [SEMI SECS/GEM 导读](https://www.semi.org/en/standards-watch-2022-Sept/intro-to-semi-communication-standards) | 公开导读，适用 SEMI 站点条款 |
| 前道设备的数据采集接口 | 定位 EDA 的设备元数据、自描述和数据采集计划等标准 | 技术资料 | [SEMI Information & Control 标准索引](https://www.semi.org/en/products-services/standards/information_and_control) | 索引公开，标准全文按 SEMI 条款获取 |
| 工艺设备与生产模块 | 给可靠性、可用性、可维护性和利用率定义统一统计口径 | 标准 | [SEMI E10](https://store-us.semi.org/products/e01000-semi-e10-specification-for-definition-and-measurement-of-equipment-reliability-availability-and-maintainability-ram-and-utilization) | 摘要公开，全文由 SEMI 提供 |
| 工艺设备与生产模块 | 自动跟踪设备和模块状态、阻塞原因及各状态持续时间 | 标准 | [SEMI E116](https://store-us.semi.org/products/e11600-semi-e116-specification-for-equipment-performance-tracking) | 摘要公开，全文由 SEMI 提供 |
| 工艺设备与工厂主机 | 在本地模拟 GEM 主机和设备的事件回调与通信 | 开源代码 | [secsgem](https://github.com/bparzella/secsgem) | Python 源码，LGPL-2.1 |
| 工艺设备与工厂主机 | 用 .NET 构建 SECS-II / HSMS-SS / GEM 通信原型 | 开源代码 | [Secs4Net](https://github.com/mkjeff/secs4net) | .NET 源码，MIT |

## 异常检测、故障分类与诊断

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| LAM 9600 金属刻蚀机 | 按实验批次比较 108 片正常与 21 片故障注入晶圆的工程变量时序 | 数据集 | [Eigenvector Metal Etch Data](https://eigenvector.com/resources/data-sets/) | 发布方提供 MATLAB 数据，许可未确认 |
| LAM 9600 金属刻蚀机 | 把 MATLAB 的工程变量时序整理成 Python 可分析的表 | 开源代码 | [Eigenvector Metal Etch Data Parser](https://github.com/jaganadhg/egvsemicon) | Python 源码，Apache-2.0，数据许可独立 |
| LAM 9600 等离子刻蚀机 | 通过设备传感器、光谱与射频监测估计过程状态，并做故障检测和分类 | 预印本 | [Virtual Sensor Based Fault Detection and Classification](https://arxiv.org/abs/0706.0465) | 公开预印本，许可见 arXiv |
| Lam Kiyo 45 刻蚀机与 MFC | 以刻蚀 OES 信号分析气体流量故障场景，并比较小样本类别增强 | 论文 | [Choi 等，GAN 与刻蚀设备故障检测](https://doi.org/10.3390/s23041889) | 文章 CC BY 4.0 |
| 300 mm PECVD 设备 | 从不同子系统的内置传感器提取状态特征并构建故障模型 | 论文 | [Bleakie 与 Djurdjanovic，PECVD 状态监测](https://doi.org/10.1016/j.compind.2012.10.002) | 摘要公开，全文依出版方条款 |
| 晶圆工艺设备的真空腔室传感器 | 从单个传感器的处理时序区分正常与异常晶圆 | 数据集 | [UCR Wafer](https://zenodo.org/records/11198387) · [原始数据入口](https://www.cs.cmu.edu/~bobski/data/data.html) | UCR 归档版本公开下载，CC BY 4.0 |
| 前道设备，类型匿名 | 用设备条件层次和 run 间波动把综合告警定位到传感器 | 论文 | [Blue 等，FDC R2R variation monitoring](https://doi.org/10.1109/ASMC.2014.6846984) | 摘要公开，全文依出版方条款 |

## 健康管理、寿命预测与维护决策

| 设备或子系统 | 任务 | 类型 | 上游资源 | 获取与许可 |
| --- | --- | --- | --- | --- |
| 离子束刻蚀设备的 Flowcool 子系统 | 用传感器、配方和设备使用量预测三类冷却系统故障的失效时间 | 数据集 | [PHM 2018 Ion Mill · 官方数据入口](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2018-b/phm-data-challenge-6/) | 官方页提供外部下载入口，数据许可未确认 |
| 离子束刻蚀设备的 Flowcool 子系统 | 了解三类故障、数据字段和竞赛预测任务 | 技术资料 | [PHM Society 2018 任务说明](https://phmsociety.org/wp-content/uploads/2018/05/PHM-Data-Challenge-2018-vFinal-v2_0.pdf) | 公开任务说明，许可未确认 |
| 离子束刻蚀设备 | 用递归模型估计在线 RUL，比较故障模式和信号筛选 | 论文 | [PHM 2018 在线 RUL 方法](https://doi.org/10.36001/phmconf.2018.v10i1.589) | 论文 CC BY 3.0，详见发布页 |
| 离子束刻蚀设备 | 查看告警筛选、故障分类和 RUL 回归的分级实现 | 开源代码 | [Ion Mill Etch 3-Stage PdM](https://github.com/ki-seoultech/PHM2018-Ion-Mill-Etch-3Stage-Predictive-Maintenance) | Python 源码，MIT，需另行准备挑战数据及派生输入 |
| 半导体工艺干式真空泵 | 结合泵参数和上游工艺条件估计退化程度与 RUL | 论文 | [Butler 等，Vacuum Pump Degradation](https://doi.org/10.3182/20090630-4-ES-2003.00267) | 出版页提供阅读入口，复用依出版方条款 |
| 晶圆厂低温泵 | 了解氦回路污染、再生故障的规则检测和基于机台数据的维护优先级 | 论文 | [Collart 等，Cryogenic Pump Predictive Maintenance](https://doi.org/10.1109/ASMC54647.2022.9792482) | 摘要公开，全文依出版方条款 |
| 晶圆厂低温泵 | 结合变点检测和状态诊断处理缓慢退化与运行变化 | 论文 | [Saha 等，低温泵预测维护框架](https://papers.phmsociety.org/index.php/phmconf/article/view/4180) | 论文 CC BY 3.0，详见发布页 |
| 晶圆搬运机器人 | 将图像测得的拾取位置偏移转为时序特征，在边缘设备上预测位置偏移故障 | 论文 | [Chung 与 Huang，Wafer-handling robot arm prognostics](https://doi.org/10.1007/s00170-026-18232-0) | 论文 CC BY-NC-ND 4.0 |
| 半导体成品测试设备 | 融合多台设备的多模态数据，按工序建模设备故障 | 论文 | [Process-aware equipment prognostics at semiconductor final test](https://doi.org/10.1016/j.cie.2026.111872) | 摘要公开，全文依出版方条款 |

## 验证时优先看什么

- 先定义告警、部件失效和维修动作的时点。状态检测可看每台设备每天的误报数与事件级召回。预测维护还应按故障模式报告提前量或 RUL 误差。
- 按设备、批次或时间留出测试集。同一故障前后的重叠窗口、换件后的使用量重置、按全量数据计算的特征都可能泄漏答案。
- 故障注入适合验证已知扰动的可辨识性。现场泛化需要额外的真实事件与维修记录。匿名时序适合做分类基线，难以支持指定零部件的根因判断。

更多按数据形态和任务整理的入口见[数据集总览](datasets.md)。配方与工艺结果的控制方法见[工艺智能](process.md)。
