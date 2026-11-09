# 半导体知识导读

从一片晶圆开始。跟踪它经过的设备、表面发生的变化，以及工程师用来判断加工结果的量测。

## F1 晶圆与设备工艺

晶圆是承载器件结构的薄片，常见基材是硅。芯片制造在晶圆上反复增加材料、定义图形、去除材料。以在一层二氧化硅上开窗口为例，沉积设备先形成薄膜，光刻在光刻胶上定义开口，刻蚀再去除开口处暴露的薄膜，把图形转移到材料里。工艺完成后，可以用膜厚和窗口尺寸检查结果。[ASML 芯片制造导读](https://www.asml.com/en/technology/all-about-microchips/how-microchips-are-made)

从设备角度看，一次加工有来料、有执行过程，也有可检查的结果。来料带有既有的膜层、图形和尺寸，配方定义设备要执行的步骤与设定，传感器记录执行时的压力、功率等信号，量测提供加工后的材料或形貌指标。把这些记录按晶圆、加工批次和腔室关联起来，才能知道某条信号对应哪次加工。[SEMI 设备数据与工艺追踪标准索引](https://www.semi.org/en/products-services/standards/information_and_control)

## F2 薄膜沉积

沉积是在晶圆上形成一层材料，可以用来导电、绝缘或保护表面。区分沉积方法时，先看材料从哪里来，再看它怎样留在表面。[MIT 薄膜沉积课程](https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/resources/mit6_774f04_lec18_mp4/) · [Vanderbilt ALD 导读](https://www.vanderbilt.edu/vinse/2025/08/08/atomic-layer-deposition-for-precise-control-of-deposited-thin-films/)

| 方法 | 成膜机制 | 一个量测例子 |
| --- | --- | --- |
| 物理气相沉积（PVD） | 以溅射为例，离子撞击固体靶材，使靶材原子逸出并沉积到晶圆上 | 沉积金属后，量测晶圆不同位置的膜厚，比较片内均匀性 |
| 化学气相沉积（CVD） | 气态前驱体送到晶圆附近，通过反应在表面形成固体薄膜，副产物离开表面 | 沉积介质层后，量测膜厚与成分，评估是否符合下一道工艺要求 |
| 原子层沉积（ALD） | 交替引入反应物，每次暴露的表面反应随可反应位点逐渐耗尽而趋于饱和。气体分步送达，中间清除残余 | 用每循环的膜厚增量估算生长速率，并比较沟槽顶面、侧壁和底部的覆盖 |

局部膜厚衡量薄膜沿表面法向的尺寸。片内均匀性描述不同位置的膜厚差异，台阶覆盖描述薄膜在三维结构顶面、侧壁和底部的厚度关系。平坦晶圆的膜厚图适合评价片内均匀性，沟槽覆盖则需要能区分不同表面位置的量测。[WashU 薄膜制备与量测](https://imse.washu.edu/facilities/fabrication-techniques.html)

## F3 刻蚀

刻蚀从晶圆上去除指定材料。图形化刻蚀常用光刻胶或硬掩膜保护要保留的区域。湿法刻蚀依靠液相反应，材料去除的方向性取决于反应体系和材料。某些湿法会同时向下、向侧面侵蚀，单晶硅也可沿不同晶向表现出明显不同的去除速率。[MIT 微加工刻蚀课程](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/6f533cbf3074f26dad3b2e819442dfc5_07lecture03.pdf)

反应离子刻蚀（RIE）是一种等离子体干法刻蚀。等离子体中的自由基常参与表面化学反应，正离子可在晶圆附近的电场中加速，以较强的方向性轰击表面。离子轰击可以促进反应或清除阻碍反应的表层，反应产物随后离开晶圆。把沟槽截面切开观察时，深度反映向下去除了多少材料，侧壁形貌则反映横向去除和表面保护的共同作用。[Stanford RIE 设备导读](https://snfguide.stanford.edu/guide/equipment/processing-technique/etching/dry-etching/capacitively-coupled-plasma-etching-ccp/reactive-ion-etching-rie) · [MIT 等离子体刻蚀课程](https://www.ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/83b8c6a46af5214061af4f03542cec40_lecture16.pdf)

选择比比较两种材料的去除速率，例如目标层与掩膜的刻蚀速率之比。各向异性描述同一种材料在不同方向上的去除差异，例如垂直去除比横向去除快。工程上常把刻蚀深度、侧壁角度和掩膜损耗一起检查，因为它们回答不同问题。[MIT 微加工刻蚀课程](https://ocw.mit.edu/courses/6-777j-design-and-fabrication-of-microelectromechanical-devices-spring-2007/6f533cbf3074f26dad3b2e819442dfc5_07lecture03.pdf)

**读数练习。** 两次试验都在相同时间内去除了 100 nm 的目标层。甲消耗 10 nm 掩膜，乙消耗 20 nm。按这段加工的平均速率估算，目标层对掩膜选择比分别是 10∶1 和 5∶1。要比较两者的各向异性，再看截面的横向去除量或侧壁角度。

## F4 物理化学过程

许多沉积和干法刻蚀设备在低于大气压的腔室中工作。工艺气体进入后，腔压由进气与排气共同决定。气体越稀薄，分子在两次碰撞之间平均走得越远。比较这段距离和腔室尺寸，可以判断模型里该怎样描述气体输运。[真空与半导体制造导读](https://milnepublishing.geneseo.edu/introtovacuumtech/chapter/vacuum-an-enabling-technology/)

以气相沉积为例，前驱体从入口进入腔室，随气体流动并扩散到晶圆附近。到达表面的分子可以吸附、发生反应，副产物再脱附并被带走。传热决定晶圆各处的温度，进而影响吸附、反应和脱附的速率。在某些 CVD 工况下，整体生长速率主要受表面反应限制，在另一些工况下则主要受反应物输运限制。[MIT 气相沉积与输运课程](https://ocw.mit.edu/courses/6-774-physics-of-microfabrication-front-end-processing-fall-2004/1sSADV3Iiuifbp51EEBEB0v15lnIZkjBA_transcript.pdf)

假设晶圆边缘的膜比中心薄，可以分别检查边缘的温度和反应物供给。若两处温度接近，下一步可检查进气几何、气体流动和边界处的浓度变化。若温差明显，则要评估表面反应对温度的敏感性。比较膜厚分布、温度信息和腔室模型，有助于区分这些候选机制。[MIT 传热与传质课程](https://ocw.mit.edu/courses/3-185-transport-phenomena-in-materials-engineering-fall-2003/pages/lecture-notes/)

## F5 关键术语

| 术语 | 阅读设备工艺时的含义 |
| --- | --- |
| 晶圆（wafer）、批次（lot）、加工记录（run） | 分别指加工对象、生产批次和一次设备加工。一次加工对应几片晶圆取决于设备和记录粒度 |
| 设备（tool）、工艺模块（module）、腔室（chamber） | 整台设备、执行特定功能的单元，以及进行沉积或刻蚀等过程的物理空间 |
| 配方（recipe）、步骤（step）、设定值（setpoint） | 配方组织执行顺序，步骤标记特定阶段，设定值给出设备在该阶段要达到的目标 |
| 轨迹（trace）、量测（metrology） | 轨迹按时间记录设备信号，量测给出膜厚、线宽或深度等结果 |
| 前驱体（precursor）、自由基（radical）、离子（ion） | 前驱体提供反应所需的物质，自由基带有未成对电子，离子带电并可被电场加速 |
| 关键尺寸（CD）、深宽比（aspect ratio） | 关键尺寸是指定结构的关键几何量，例如线宽。沟槽的深宽比用其深度除以指定宽度 |

[完整术语表](../catalog/glossary.md) · [技术方法](methods.md) · [学习地图](../README.md)
