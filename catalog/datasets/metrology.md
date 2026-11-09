# D3 量测、检测与晶圆图

[数据集目录](../datasets.md) · [设备数据与量测](../../learn/methods.md#t2-设备数据与量测)

本节的数据由量测、检测或电测产生。膜厚和复折射率可作为连续量测目标，SEM 与光致发光图像可用于识别和定位缺陷，晶圆图可用于判断空间模式。只有数据提供跨表标识时，才有条件把这些结果与前序机台运行记录拼起来。

## 膜厚与参考样片

**M01 NIST ALD HfO₂ 参考薄膜。** 在 200 mm Si 晶圆上沉积约 10 nm 的 HfO₂，发布椭偏与 X 射线反射量测及其说明。先按样片和点位识别测量结果，再比较厚度估计的重复性、空间变化与方法差异。适合验证测量流程与不确定度。采集于参考样片项目，许可依 NIST 数据条款。[数据记录](https://catalog.data.gov/dataset/nanometer-scale-planar-reference-materials-project-data-year-2025-set-00-10nm-hafnia-on-si) · [项目资料](https://www.nist.gov/programs-projects/nanometer-scale-planar-reference-materials) · [NIST 条款](https://www.nist.gov/open/license)

光刻胶表征和处理条件见[涂胶、烘烤与显影](coat-develop.md)，硅片光致发光与湿法前处理见[清洗专题](cleaning.md)。

## 缺陷图像与晶圆图

| 编号 | 数据 | 内容与关联粒度 | 访问与许可 |
| --- | --- | --- | --- |
| M03 | [Carinthia](https://zenodo.org/records/10715190) / [Carinthia-S](https://zenodo.org/records/16895427) | 同源的 4,591 张未图形化晶圆生产层 SEM 缺陷图，原版有六类标签，S 版加专家验证的分割掩膜。用图像配对，两个版本应共用同一数据划分 | 两版可下载，均为 CC BY 4.0 |
| M05 | [全晶圆 4H-SiC 缺陷显微分析](https://zenodo.org/records/11229837) | 公开附件为后处理结果 PDF，原始显微图需申请。适合复核论文测得的缺陷分布 | 附件 CC BY 4.0。原图按作者条件 |
| M06 | WM-811K / LSWMD | 真实制造数据的晶圆缺陷图、批次字段及部分缺陷类型标注。可做空间模式分类和按批次泛化 | 原始论文可查，常用文件为第三方镜像，原始再分发授权未确认。[作者论文](https://doi.org/10.1109/TSM.2014.2364237) · [Hugging Face 镜像](https://huggingface.co/datasets/lslattery/wafer-defect-detection/blob/main/LSWMD.pkl) |

### 选题与验证

- 研究图像识别时，优先按原始晶圆或批次划分。公开包只有图像编号时，记录这一限制，至少保证同一图像的所有裁剪、增强和掩膜落在同一划分。
- 晶圆图上的空间模式可用来筛选排查方向。要验证异常来自哪台设备，还需要路由、设备历史或可核对的工艺事件。
- 同一晶圆先后量到的信号可能来自不同处理阶段。训练前确认坐标系、单位、标注时间和量测方法。

[上一节 沉积、外延与 CMP](deposition-cmp.md) · [下一节 设备状态与运维](health.md)
