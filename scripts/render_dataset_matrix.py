"""Render the dataset coverage chart and its accessible Markdown equivalent."""

import argparse
import csv
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog/datasets"
ASSETS = ROOT / "assets/datasets"
CHAPTERS = (
    ("cleaning", "清洗与湿法前处理"),
    ("coat-develop", "涂胶、烘烤与显影"),
    ("implantation", "离子注入与退火"),
    ("packaging", "封装与互连"),
    ("etch", "刻蚀与等离子体"),
    ("deposition-cmp", "沉积、外延与 CMP"),
    ("metrology", "量测与缺陷检测"),
    ("health", "设备状态与运维"),
    ("simulation", "工艺物理仿真"),
    ("fab", "晶圆厂仿真与调度"),
)
MEASURES = ("配方数值", "原始时序", "实测结果", "仿真结果", "同片关联")
FILE_ACCESS = {"public-files", "upstream-linked", "mirror", "supplement-data"}
MEASURED_ORIGINS = {"industrial-measured", "lab-measured", "fault-injected", "industrial-context"}
PALETTES = {
    "light": {
        "canvas": "#FFFFFF", "text": "#152B3C", "muted": "#4B6477",
        "line": "#DDE7EE", "focus": "#F4F8FB", "accent": "#326686",
        "cells": ("#F2F6F8", "#DCEBF2", "#B5D1E1", "#295773"),
        "numbers": ("#4B6477", "#214661", "#173E58", "#FFFFFF"),
    },
    "dark": {
        "canvas": "#101820", "text": "#E3EDF4", "muted": "#A5BAC9",
        "line": "#30424F", "focus": "#17242F", "accent": "#8BB6CE",
        "cells": ("#202D38", "#2D4A5E", "#426981", "#96BED4"),
        "numbers": ("#A5BAC9", "#ECF6FB", "#FFFFFF", "#102A3B"),
    },
}


def summarize(records):
    known_chapters = {slug for slug, _ in CHAPTERS}
    unknown = {record["chapter"] for record in records} - known_chapters
    if unknown:
        raise ValueError(f"Unknown coverage chapters: {', '.join(sorted(unknown))}")
    summary = []
    for slug, title in CHAPTERS:
        all_rows = [record for record in records if record["chapter"] == slug]
        files = [record for record in all_rows if record["access"] in FILE_ACCESS]
        measured = [record for record in files if record["origin"] in MEASURED_ORIGINS]
        counts = (
            sum(row["recipe"] in {"settings", "partial", "normalized"} for row in measured),
            sum(row["trace"] == "timeseries" for row in measured),
            sum(row["metrology"] != "none" for row in measured),
            sum(row["simulation"] not in {"none", "summary", "fab-model"} for row in files),
            sum(row["join_level"] == "wafer" for row in measured),
        )
        summary.append((slug, title, len(all_rows), counts))
    return summary


def render_markdown(summary):
    output = [
        "# 数据覆盖矩阵",
        "",
        "[数据集首页](../datasets.md) · [下载总表 CSV](inventory.csv) · [检索记录](coverage.md)",
        "",
        "选择一行进入设备专题。数字表示本仓库已登记、符合该列口径的资源数。同一资源可以出现在多列。"
        "「已收录」还包括图表附件、配方参考和模型生成工具。",
        "",
        "| 工序或专题 | 已收录 | " + " | ".join(MEASURES) + " |",
        "| --- | ---: | " + " | ".join("---:" for _ in MEASURES) + " |",
    ]
    for slug, title, total, counts in summary:
        values = " | ".join(str(count) if count else "—" for count in counts)
        output.append(f"| [{title}]({slug}.md) | {total} | {values} |")
    output += [
        "",
        "覆盖列只计发布方提供文件、上游说明链接独立文件或已有镜像的记录。仅有图示的附件、参考配方、竞赛介绍与"
        "仅有生成器的条目在章节中另行注明。获取方式与许可证分别见总表。",
        "",
        "| 列 | 计数口径 |",
        "| --- | --- |",
        "| 配方数值 | 实测实验有可对应工况的数值设定，包括部分参数和归一化设定。配方编号、工步名称和仿真输入另列。 |",
        "| 原始时序 | 设备执行或运行时留下的采样序列。分阶段照片、标准化序列、摘要统计和量测仪器扫频另列。 |",
        "| 实测结果 | 样片、晶圆、芯片或封装件的物理量、电测、图像或测试结果。标签型设备状态另列。 |",
        "| 仿真结果 | 可获取的数值剖面、图像、场或粒子分布。论文图表汇总、厂级配置和仅有求解器的条目另列。 |",
        "| 同片关联 | 可用公开字段把实测机台输入或工艺条件接到同一片晶圆的物理量测或电测。按工况、试样或图号对齐时，在专题内说明其粒度。 |",
        "",
        "「—」表示目前目录没有符合该口径的文件。其余关联层级见[字段说明](coverage.md#csv-字段)。",
        "",
    ]
    return "\n".join(output)


def render_svg(summary, palette):
    chart = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="920" height="599" viewBox="0 0 920 599" role="img" aria-labelledby="title description">',
        '<title id="title">SEMI 101 半导体设备数据覆盖</title>',
        '<desc id="description">按工序显示配方数值、原始时序、实测结果、仿真结果和同片关联的资源数量。前四行是本轮重点。</desc>',
    ]

    def rect(x, y, width, height, fill, radius=0):
        chart.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}"/>')

    def label(x, y, value, size, color, weight=400, anchor="start", tracking=0):
        chart.append(
            f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" letter-spacing="{tracking}">{escape(str(value))}</text>'
        )

    rect(0, 0, 920, 599, palette["canvas"])
    chart.append('<g font-family="Inter, -apple-system, BlinkMacSystemFont, PingFang SC, Noto Sans CJK SC, Microsoft YaHei, sans-serif">')
    label(32, 37, "SEMI 101   /   DATA ATLAS", 13, palette["accent"], 700, tracking=2)
    label(32, 80, "半导体设备数据覆盖", 31, palette["text"], 700)
    label(33, 107, "按工序统计可定位到文件的证据", 14, palette["muted"])
    label(886, 77, f'{sum(row[2] for row in summary):02}', 41, palette["text"], 650, "end")
    label(886, 105, "已收录资源", 14, palette["muted"], 450, "end")
    rect(32, 128, 856, 1, palette["line"])
    label(48, 155, "工序 / 专题", 14, palette["muted"], 550)
    for i, name in enumerate(MEASURES):
        label(305 + i * 126, 155, name, 15, palette["text"], 600, "middle")

    rect(32, 165, 856, 144, palette["focus"], 8)
    rect(32, 174, 3, 126, palette["accent"], 1.5)
    for index, (_, title, _, counts) in enumerate(summary):
        y = 170 + 36 * index + (8 if index >= 4 else 0)
        label(49, y + 18, f"{index + 1:02}", 12, palette["accent"] if index < 4 else palette["muted"], 600)
        label(80, y + 19, title, 15, palette["text"], 650 if index < 4 else 500)
        for i, count in enumerate(counts):
            center = 305 + i * 126
            level = min(count, 3)
            rect(center - 52, y, 104, 27, palette["cells"][level], 5)
            label(center, y + 19, count if count else "—", 16, palette["numbers"][level], 650, "middle")

    rect(32, 545, 856, 1, palette["line"])
    rect(32, 565, 3, 15, palette["accent"], 1.5)
    label(43, 577, "本轮重点", 13, palette["muted"], 550)
    label(166, 577, "—  暂无符合口径的文件", 13, palette["muted"])
    for i, value in enumerate(("0", "1", "2", "3+")):
        x = 729 + i * 40
        rect(x, 561, 35, 23, palette["cells"][i], 4)
        label(x + 17.5, 577, value, 12, palette["numbers"][i], 650, "middle")
    chart += ["</g>", "</svg>", ""]
    return "\n".join(chart)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify that generated files are current.")
    args = parser.parse_args()
    with (CATALOG / "inventory.csv").open(encoding="utf-8", newline="") as file:
        summary = summarize(list(csv.DictReader(file)))
    outputs = {CATALOG / "matrix.md": render_markdown(summary)}
    outputs.update({
        ASSETS / f"coverage-{theme}.svg": render_svg(summary, palette)
        for theme, palette in PALETTES.items()
    })
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                parser.exit(1, f"Dataset coverage is stale: {path.relative_to(ROOT)}\n")
        else:
            path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
