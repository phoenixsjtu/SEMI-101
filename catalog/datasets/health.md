# D4 设备状态与运维

[数据集目录](../datasets.md) · [设备运维资源](../operations.md) · [FDC 与 RCA](../../learn/applications.md#a5-故障检测与分类)

设备状态数据要从标签的生成过程读起。人为注入故障、晶圆出片后判异常、因失效维护停机，三个事件在时间和证据强度上各不相同。

| 编号 | 数据 | 信号与关联 | 标签、访问与许可 |
| --- | --- | --- | --- |
| H01 | [Eigenvector LAM 9600 Metal Etch](https://eigenvector.com/resources/data-sets/) | 实测金属刻蚀机工程变量，按运行组织；含受控故障注入 | 故障实验类型；发布方提供 MATLAB 文件，许可未确认 |
| H02 | [PHM 2018 Ion Mill](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2018-b/phm-data-challenge-6/) | 离子束刻蚀设备冷却系统，按机台和时间记录传感器、类别型 `recipe` 和 `recipe_step` | 三类故障以操作员维护停机时刻标记，许可未确认。[官方字段说明](https://phmsociety.org/wp-content/uploads/2018/05/PHM-Data-Challenge-2018-vFinal-v2_0.pdf)。[NASA 镜像](https://c3.ndc.nasa.gov/dashlink/resources/1009/)属于同一套数据 |
| H03 | [STMicroelectronics ST-AWFD](https://github.com/STMicroelectronics/ST-AWFD) | 真实制造的 D1 / D2 分组时序，`MaterialID` 对应生产批次，`StepID` 区分工步，时间和特征经过归一化 | `target` 标记异常批次，`is_test` 记录作者划分。CC BY-NC-SA 4.0。[论文](https://doi.org/10.3390/s21165465) |
| H04 | [Semiconductor Frontend Equipment Sensor Data](https://zenodo.org/records/4322353) | 两份匿名前道设备传感器 CSV 和一份对应的晶圆测试结果表。用 `lot + wafer` 拼接，`timestamp` 是各设备的采样索引 | 数值响应和阈值生成的良／不良类别。CC BY 4.0。发布说明未交代机型和完整生产背景 |
| H05 | [UCI SECOM](https://archive.ics.uci.edu/dataset/179/secom) | 1,567 条匿名生产实体记录和 591 个工艺测量特征，带时间与缺失值 | 通过／失败，CC BY 4.0。适合表格基线和时间切分 |
| H06 | [UCR Wafer](https://zenodo.org/records/11198387) | 单路晶圆传感器时序，提供固定训练／测试文件 | 正常／异常，归档版本 CC BY 4.0。适合单变量分类入门。[数据原始说明](https://www.cs.cmu.edu/~bobski/data/data.html) |

## 三种复现方式

1. **工步感知 FDC。** 用 H03 的发布划分做基线，按 `MaterialID` 统计指标。比较工步特征、全段特征与早期截断。特征已经归一化，若要验证现场设阈值，还要重新评估量纲与部署时的缩放方式。
2. **跨设备异常排查。** H04 发布包中，设备 1、设备 2、响应表分别有 971、1,319、1,319 个唯一 `lot + wafer` 组合，三表交集为 971。先报告联结覆盖率，再按批次留出。对比单设备和双设备的解释变量。设备字段相关性可以形成排查假设，确认根因需要工艺或故障证据。
3. **RUL 事件回放。** 用 H02 的设备标识、事件时间和公开规则建立标签，对比按设备留出与按时间回放的表现。预测目标应写清是距哪类停机／维护事件的时间，评估要区分采样时刻与可见告警时刻。

[上一节 量测、检测与晶圆图](metrology.md) · [下一节 工艺物理仿真](simulation.md)
