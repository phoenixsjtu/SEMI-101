<p align="right"><a href="README_EN.md">English</a></p>

# SEMI 101

**半导体设备手册。** 从薄膜沉积和刻蚀入门，学会用配方、机台记录和晶圆量测读懂一次加工。

**[从晶圆与设备工艺开始](learn/foundations.md#f1-晶圆与设备工艺)** · [查数据集](catalog/datasets.md) · [找论文与代码](#research-resources)

<div><a name="learning-map"></a><a name="学习地图"></a></div>

## 手册目录

- <a name="01-半导体知识导读"></a>**[工艺原理](learn/foundations.md)**　薄膜怎样长起来，等离子体怎样刻蚀材料。
- <a name="02-技术方法"></a>**[仿真、数据与控制](learn/methods.md)**　给腔室建模，按工步读传感器记录，再用量测检验预测。
- <a name="03-工程应用"></a>**[工艺开发与量产](learn/applications.md)**　优化配方、做虚拟量测，或排查生产中的异常。

## 一片晶圆的 89 个量测点

这片晶圆的最高台阶高度出现在边缘附近。用实验日期和晶圆号，可以把这张出片量测图接到 BOSCH 刻蚀时记录的压力、功率和光谱。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/home/bosch-wafer-dark.svg">
  <img src="assets/home/bosch-wafer-light.svg" width="460" alt="晶圆 2024-07-02_01 的 89 个台阶高度量测点，约 41 至 53 微米。">
</picture>

<sub>晶圆 2024-07-02_01，按原始点位绘制。数据来自 Sayyed 等人，<a href="https://zenodo.org/records/17122442">BOSCH 数据集</a>（CC BY 4.0）。</sub>

[做第一个数据练习](learn/README.md#第一个读数据练习) · [看字段和关联方法](catalog/datasets/etch.md#e01-bosch-深硅刻蚀)

<div><a name="research-resources"></a><a name="研究资料"></a><a name="04-半导体设备数据集"></a></div>

## 资料索引

[数据覆盖矩阵](catalog/datasets/matrix.md) · [论文导读](catalog/papers.md) · [代码索引](catalog/code.md)

按设备环节浏览 [设备设计](catalog/design.md) · [工艺智能](catalog/process.md) · [设备运维](catalog/operations.md)

<div><a name="offline"></a></div>

[阅读指南](learn/README.md) · [术语速查](catalog/glossary.md) · [收录与贡献](CONTRIBUTING.md) · [下载 ZIP](https://github.com/phoenixsjtu/SEMI-101/archive/refs/heads/main.zip)
