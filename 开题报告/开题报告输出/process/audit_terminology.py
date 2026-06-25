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

RULES_ALL: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"杂志批次"), "Magazine 应为「弹夹批次Magazine」"),
    (re.compile(r"WIP在制品"), "应为「在制品WIP」"),
    (re.compile(r"设置10分钟|换型含搬运|与设置10"), "换型Setup 表述，见 TERMINOLOGY §换型"),
    (re.compile(r"含搬运换型"), "应为「Worker搬运、换型Setup」"),
    (re.compile(r"Worker/换型"), "应为「Worker搬运与换型Setup」"),
    (re.compile(r"完工时间"), "MakeSpan 统一为「制造周期MakeSpan」"),
    (re.compile(r"\bwhat-if\b", re.I), "改用「情景假设分析」"),
    (re.compile(r"\boracle\b", re.I), "改用「仿真性能评估器」"),
    (re.compile(r"\bmetaheuristic\b", re.I), "改用「元启发式算法」"),
    (re.compile(r"AUTO_Model"), "不写内部模型文件名"),
    (re.compile(r"Separator_MLot|Separator_Mag|Separator_SubLot|Combiner_Sub|Source_Orders"), "不写 Simio 内部对象名"),
    (re.compile(r"EXP-\d+|D-\d{3}"), "正文禁止内部实验/决策编号"),
    (re.compile(r"导师"), "正文不写导师人事安排句式"),
]

FORBIDDEN_NUMBERS = re.compile(r"\b(?:50\.61|54\.88|52\.38|78\.40|291\.18|760|700)\b")

SECTIONS = {
    "SECTION1_BODY": ("1", SECTION1_BODY),
    "SECTION2": ("2", SECTION2),
    "SECTION3": ("3", SECTION3),
}


def scan(name: str, text: str, section_num: str) -> list[str]:
    issues: list[str] = []
    for pattern, msg in RULES_ALL:
        for m in pattern.finditer(text):
            line = text[: m.start()].count("\n") + 1
            snippet = text[max(0, m.start() - 15) : m.end() + 15].replace("\n", " ")
            issues.append(f"{name} L{line}: {msg} → …{snippet}…")
    if section_num in ("1", "2"):
        for m in FORBIDDEN_NUMBERS.finditer(text):
            line = text[: m.start()].count("\n") + 1
            snippet = text[max(0, m.start() - 15) : m.end() + 15].replace("\n", " ")
            issues.append(f"{name} L{line}: §{section_num} 不得出现已跑实验数值 → …{snippet}…")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit proposal terminology.")
    _ = parser.parse_args()

    all_issues: list[str] = []
    for name, (num, text) in SECTIONS.items():
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
