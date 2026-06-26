# -*- coding: utf-8 -*-
"""开题报告技术路线图 v3 — 图2式，黑白，无多余虚线，路线不写实验数值。"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

OUT = Path(__file__).with_name("开题报告_技术路线图.png")

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "SimSun", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(10.5, 12.5), dpi=220)
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 12.5)
ax.axis("off")

BLACK = "#000000"
GRAY = "#888888"

FX, FW = 2.0, 8.2
BW, BGAP = 2.45, 0.2
MX, MW = 0.35, 1.5


def sbox(x, y, w, h, text, *, fs=8.2, bold=False):
    ax.add_patch(Rectangle((x, y), w, h, lw=0.9, ec=BLACK, fc="white", zorder=3))
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        fontweight="bold" if bold else "normal",
        color=BLACK,
        zorder=4,
        linespacing=1.28,
    )


def dbox(x, y, w, h):
    ax.add_patch(
        Rectangle((x, y), w, h, lw=0.85, ec=GRAY, fc="none", linestyle="--", zorder=1)
    )


def arr_d(x, y1, y2):
    ax.add_patch(
        FancyArrowPatch(
            (x, y1),
            (x, y2),
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=0.85,
            color=BLACK,
            shrinkA=2,
            shrinkB=2,
            zorder=2,
        )
    )


def arr_r(x1, y, x2, *, pad=0.05):
    ax.add_patch(
        FancyArrowPatch(
            (x1 + pad, y),
            (x2 - pad, y),
            arrowstyle="-|>",
            mutation_scale=11,
            linewidth=0.85,
            color=BLACK,
            shrinkA=0,
            shrinkB=0,
            zorder=2,
        )
    )


# ── 左侧方法（仅横线连到阶段框，无竖虚线）──
methods = [
    (9.25, "文献\n研究法"),
    (7.05, "离散事件\n仿真法"),
    (4.55, "仿真优化\n实验设计法"),
    (2.05, "对比实验\n与敏感性\n分析法"),
]
for cy, label in methods:
    sbox(MX, cy - 0.52, MW, 1.05, label, fs=7.5, bold=True)
    arr_r(MX + MW, cy, FX, pad=0.02)

# ═══ 阶段一 ═══
P1Y, P1H = 8.5, 1.5
dbox(FX, P1Y, FW, P1H)
sbox(FX + 2.75, P1Y + 0.88, 2.7, 0.45, "问题界定与文献综述", fs=8.3, bold=True)
arr_d(FX + 4.1, P1Y + 0.88, P1Y + 0.58)
for i, t in enumerate(["研究背景\n与意义", "国内外\n文献综述", "研究内容\n与目标"]):
    sbox(FX + 0.3 + i * (BW + BGAP), P1Y + 0.08, BW, 0.46, t, fs=7.3)
arr_d(FX + FW / 2, P1Y, 8.2)

# ═══ 阶段二 ═══
P2Y, P2H = 5.95, 2.25
dbox(FX, P2Y, FW, P2H)
b2a_x, b2a_w = FX + 0.35, 2.35
b2b_x, b2b_w = FX + 3.35, 2.55
cy2 = P2Y + 1.58
sbox(b2a_x, cy2 - 0.24, b2a_w, 0.48, "脱敏数据", fs=8)
sbox(b2b_x, cy2 - 0.24, b2b_w, 0.48, "Simio 六工序\nDES 建模", fs=7.8, bold=True)
arr_r(b2a_x + b2a_w, cy2, b2b_x, pad=0.12)
arr_d(b2b_x + b2b_w / 2, cy2 - 0.24, P2Y + 1.02)
for i, t in enumerate(["多级批次链\n结构", "搬运、转入转出\n与换型约束"]):
    x = FX + 1.35 + i * (3.35 + BGAP)
    sbox(x, P2Y + 0.12, 3.35, 0.76, t, fs=7.4)
arr_d(FX + FW / 2, P2Y, 5.75)

# ═══ 阶段三：只写路线（纵向四步）═══
P3Y, P3H = 3.45, 2.3
dbox(FX, P3Y, FW, P3H)
steps3 = [
    (P3Y + 1.68, "仿真绩效指标体系构建"),
    (P3Y + 1.12, "Scenario Generator\n批次因子网格扫描"),
    (P3Y + 0.56, "基准情景验证"),
    (P3Y + 0.06, "较优因子识别"),
]
for y, text in steps3:
    sbox(FX + 2.05, y, 4.1, 0.4, text, fs=7.4)
for i in range(len(steps3) - 1):
    y_top = steps3[i][0]
    y_bot = steps3[i + 1][0] + 0.4
    arr_d(FX + 4.1, y_top, y_bot)
arr_d(FX + FW / 2, P3Y, 3.05)

# ═══ 阶段四 ═══
P4Y, P4H = 1.05, 1.55
dbox(FX, P4Y, FW, P4H)
steps4 = [
    (P4Y + 0.98, "订单释放与\n派工规则对比"),
    (P4Y + 0.52, "释放策略对照实验"),
    (P4Y + 0.06, "负荷敏感性分析 · 瓶颈标定"),
]
for y, text in steps4:
    sbox(FX + 2.05, y, 4.1, 0.4, text, fs=7.5)
for i in range(len(steps4) - 1):
    y_top = steps4[i][0]
    y_bot = steps4[i + 1][0] + 0.4
    arr_d(FX + 4.1, y_top, y_bot)
arr_d(FX + FW / 2, P4Y, 0.85)

# ═══ 结论 ═══
sbox(FX + 2.1, 0.35, FW - 4.2, 0.5, "结论与展望", fs=9.5, bold=True)

fig.savefig(OUT, bbox_inches="tight", facecolor="white", pad_inches=0.06)
print(f"Saved: {OUT}")
