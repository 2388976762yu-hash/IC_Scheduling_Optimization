# -*- coding: utf-8 -*-
"""Audit proposal terminology against TERMINOLOGY.md."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

# (pattern, message, sections) — sections: "all" | "1" | "2" | "3"
RULES: list[tuple[re.Pattern[str], str, str]] = [
    (re.compile(r"杂志批次"), "Magazine 应为「弹夹批次Magazine」", "all"),
    (re.compile(r"WIP在制品"), "应为「在制品WIP」", "all"),
    (re.compile(r"设置10分钟|换型含搬运|与设置10"), "换型Setup 表述，见 TERMINOLOGY §换型", "all"),
    (re.compile(r"含搬运换型"), "应为「Worker搬运、换型Setup」", "all"),
    (re.compile(r"Worker/换型"), "应为「Worker搬运与换型Setup」", "all"),
    (re.compile(r"完工时间"), "MakeSpan 统一为「制造周期MakeSpan」", "all"),
    (re.compile(r"\bwhat-if\b", re.I), "改用「情景假设分析」", "all"),
    (re.compile(r"\boracle\b", re.I), "改用「仿真性能评估器」", "all"),
    (re.compile(r"\bmetaheuristic\b", re.I), "改用「元启发式算法」", "all"),
    (re.compile(r"AUTO_Model"), "不写内部模型文件名", "all"),
    (re.compile(r"Separator_MLot|Separator_Mag|Separator_SubLot|Combiner_Sub|Source_Orders"), "不写 Simio 内部对象名", "all"),
    (re.compile(r"EXP-\d+|D-\d{3}"), "正文禁止内部实验/决策编号", "all"),
    (re.compile(r"(?<![脱敏])SPAN(?![\s]*基准数据集)"), "SPAN 须写「行业脱敏SPAN基准数据集」", "all"),
    (re.compile(r"前期已完成|初步实验结果|初步批次因子网格扫描表明"), "开题勿写已完成实验结论", "1"),
    (
        re.compile(r"\b(?:50\.61|54\.88|52\.38|78\.40|291\.18|760|700)\b"),
        "开题正文禁止已跑实验数值",
        "all",
    ),
]

# SPAN rule is tricky - let me refine: forbid bare "SPAN数据" "SPAN数据集" without 行业脱敏 prefix
SPAN_BARE = re.compile(r"(?<![\u4e00-\u9fff])SPAN(?:基准)?(?:数据|数据集|基准集)(?!集)")
# Actually current text uses "行业脱敏SPAN基准数据集" - good
# Also "在SPAN基准数据上" - need fix in content

SECTIONS = {
    "SECTION1_BODY": SECTION1_BODY,
    "SECTION2": SECTION2,
    "SECTION3": SECTION3,
}


def scan(name: str, text: str, section_num: str) -> list[str]:
    issues: list[str] = []
    for pattern, msg, scope in RULES:
        if scope not in ("all", section_num):
            continue
        for m in pattern.finditer(text):
            line = text[: m.start()].count("\n") + 1
            snippet = text[max(0, m.start() - 15) : m.end() + 15].replace("\n", " ")
            issues.append(f"{name} L{line}: {msg} → …{snippet}…")
    # Additional: bare SPAN without 行业脱敏 within 20 chars before
    for m in re.finditer(r"SPAN", text):
        before = text[max(0, m.start() - 12) : m.start()]
        if "行业脱敏" not in before and "脱敏" not in before:
            line = text[: m.start()].count("\n") + 1
            snippet = text[max(0, m.start() - 20) : m.end() + 20].replace("\n", " ")
            issues.append(f"{name} L{line}: SPAN 须带「行业脱敏」前缀 → …{snippet}…")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit proposal terminology.")
    args = parser.parse_args()
    _ = args

    all_issues: list[str] = []
    for name, text in SECTIONS.items():
        num = "1" if name == "SECTION1_BODY" else name.replace("SECTION", "")[0]
        all_issues.extend(scan(name, text, num))

    if all_issues:
        print("FAIL: terminology audit")
        for item in all_issues:
            print(f"  - {item}")
        return 1

    print("OK: terminology audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
