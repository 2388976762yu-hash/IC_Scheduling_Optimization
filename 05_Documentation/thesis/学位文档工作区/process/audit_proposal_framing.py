# -*- coding: utf-8 -*-
"""Audit 开题正文：禁止错误时态、导师句式、术语误用。"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

FORBIDDEN_NUMBERS = re.compile(r"\b(?:50\.61|54\.88|52\.38|78\.40|291\.18|760|700)\b")

FORBIDDEN_PAST_FRAMING = re.compile(
    r"前期已完成|初步批次因子网格扫描表明|与前期已完成|"
    r"关键数值已与内部记录核对"
)

FORBIDDEN_TERMS = re.compile(
    r"设置10分钟|换型含搬运3分钟与设置|杂志批次|WIP在制品|"
    r"含搬运换型|Worker/换型|(?<![\u4e00-\u9fff])what-if|(?<!\w)oracle(?!\w)|metaheuristic"
)

FORBIDDEN_ADVISOR = re.compile(r"导师")


def scan(name: str, text: str, *, check_numbers: bool) -> list[str]:
    issues: list[str] = []
    if check_numbers:
        for m in FORBIDDEN_NUMBERS.finditer(text):
            line = text[: m.start()].count("\n") + 1
            issues.append(f"{name} L{line}: 不得出现已跑实验数值")
        for m in FORBIDDEN_PAST_FRAMING.finditer(text):
            line = text[: m.start()].count("\n") + 1
            issues.append(f"{name} L{line}: 不得写已完成实验结论式表述")
    for pattern, msg in (
        (FORBIDDEN_TERMS, "术语/机翻用语"),
        (FORBIDDEN_ADVISOR, "正文不写导师人事安排句式"),
    ):
        for m in pattern.finditer(text):
            line = text[: m.start()].count("\n") + 1
            issues.append(f"{name} L{line}: {msg}")
    return issues


def main() -> int:
    issues: list[str] = []
    issues.extend(scan("SECTION1_BODY", SECTION1_BODY, check_numbers=True))
    issues.extend(scan("SECTION2", SECTION2, check_numbers=True))
    issues.extend(scan("SECTION3", SECTION3, check_numbers=False))

    if issues:
        print("FAIL: proposal framing audit")
        for item in issues:
            print(f"  - {item}")
        return 1

    print("OK: proposal framing audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
