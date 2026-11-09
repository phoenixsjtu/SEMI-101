# D2 沉积、外延与 CMP

[数据集目录](../datasets.md) · [薄膜沉积原理](../../learn/foundations.md#f2-薄膜沉积) · [虚拟量测](../../learn/applications.md#a2-虚拟量测)

膜厚、空间均匀性、生长速率、材料去除率和器件电学性能属于不同目标。选择数据时先确定要预测哪个量，以及它是在机台内、出片后还是器件测试阶段得到的。

## P01 Infineon PVD

**数据与版本。** 首次发布分开提供 AlCu、WTi 的 APC 工艺特征表和 SPC 膜厚目标表。更新版针对 AlCu，提供含 `wafer_id`、`lot`、`equipment`、`machine`、`runstart` 等字段的输入输出合表。该 CSV 首行是表名，第二行是以分号分隔的表头。输入来自机台轨迹汇总，新版包括 17 点膜厚、方块电阻及由两者计算的电阻率。膜厚和方块电阻的对应点位相邻，测量坐标有差别。APC 的匿名缩放因变量而异，保留单变量相对变化，均值、极差等统计量之间的原始代数关系可能不成立。两版为 CC BY 4.0。[AlCu 与 WTi 分表版](https://zenodo.org/records/16881338) · [更新的 AlCu 合表](https://zenodo.org/records/23442538)

**建议实验。** 先拟合单目标膜厚，再比较共享特征的多输出回归。分别按机台或腔室和时间切分，检查设备域偏移。若用早版和新版一起做实验，先查 AlCu 样本重合。量测位置可以作为向量维度，复原带物理坐标的厚度场还需要点位坐标和坐标系。[发布方说明](https://zenodo.org/records/23442538)

## P02 PHM 2016 CMP

**数据与关联。** 挑战赛提供 CMP 加工过程数据与训练或验证的平均材料去除率目标。用 `WAFER_ID + STAGE` 将时序和目标相连。设备信号与去除率的样本单位有层级差异，晶圆的多个阶段可能产生多条记录。分开检查挑战赛训练、验证、测试所公开的目标文件。原公告的 Dropbox 返回错误页，社区仓库有文件副本，数据再分发许可未确认。[官方挑战入口](https://phmsociety.org/conference/annual-conference-of-the-phm-society/annual-conference-of-the-prognostics-and-health-management-society-2016/phm-data-challenge-4/) · [字段和下载公告](https://phmsociety.org/wp-content/uploads/2016/05/PHM16DataChallengeCFP.pdf) · [第三方副本](https://github.com/akangel0307/PHM-Data-Challenge)

**建议实验。** 对比工步摘要与整段轨迹，报告去除率误差并检查不同设备或工段的表现。想研究耗材老化时，先确认累计使用量字段的定义和记录边界。去除率目标代表晶圆上的平均值，片内均匀性需要多点量测。

## 实验室沉积与外延

| 编号 | 数据 | 设备条件和实际输出 | 可做的事 | 许可 |
| --- | --- | --- | --- | --- |
| P03 | [Cambridge 反应溅射 AZTO](https://doi.org/10.17863/CAM.6224) | 远程等离子体反应溅射工艺实验配套压缩包，含薄膜与 TFT 表征资料 | 按试样和图表追溯工艺变化与薄膜或器件性能 | CC BY 4.0 |
| P04 | [GaN MOVPE 原位光学量测](https://zenodo.org/records/12801851) | AIXTRON 反应器内 1045 °C 外延过程，由反射光谱拟合不同阶段的复折射率 | 比较阶段间光学响应，用于量测模型和生长机理研究 | CC BY 4.0 |

**P05 FBK 光电晶体管虚拟量测。** 工艺参数与增益在晶圆级关联，发布含两种实验纳入规则、字段字典和 Python 分析流程。配方以各实验组参考中位数归一化，支持比较相对工艺变化。按工艺运行划分数据，再检查两个实验组的重叠。公开的参数比值用于相对配方搜索，绝对机台设定和逐 die 电测需要额外数据。数据 CC BY 4.0，配套代码 MIT。[数据、字典与复现包](https://zenodo.org/records/21379926) · [作者代码](https://github.com/mahshid-amirabgir/phototransistor-virtual-metrology)

仿真生成的 ALD 剖面与饱和剂量见[工艺物理仿真](simulation.md#ald-与刻蚀)。实测参考薄膜的椭偏和 XRR 文件见[量测章节](metrology.md#膜厚与参考样片)。

[上一节 刻蚀与等离子体](etch.md) · [下一节 量测、检测与晶圆图](metrology.md)
