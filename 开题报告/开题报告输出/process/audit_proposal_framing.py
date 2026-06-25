# -*- coding: utf-8 -*-
"""Audit 开题正文：禁止已跑实验数值、错误时态、术语误用。"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

# 开题正文不应出现的实验结论数字（内部真源见 CLAIMS.md）
FORBIDDEN_NUMBERS = re.compile(
    r"\b(?:50\.61|54\.88|52\.38|78\.40|291\.18|760|700)\b"
)

# 第一节/综述：不应写「已完成实验」式表述
FORBIDDEN_PAST_FRAMING = re.compile(
    r"前期已完成|初步实验结果|初步批次因子网格扫描表明|与前期已完成|"
    r"已表明.*不足以|关键数值已与内部记录核对"
)

# 术语：「设置10分钟」易与换型混淆；应写换型Setup
FORBIDDEN_TERMS = re.compile(
    r"设置10分钟|换型含搬运3分钟与设置|杂志批次|WIP在制品|"
    r"含搬运换型|Worker/换型|(?<![\u4e00-\u9fff])what-if|(?<!\w)oracle(?!\w)|metaheuristic"
)

SECTION1_ONLY_PATTERNS = (
    (FORBIDDEN_NUMBERS, "§1 不得出现已跑实验数值"),
    (FORBIDDEN_PAST_FRAMING, "§1 不得写已完成实验结论式表述"),
)

ALL_SECTIONS_PATTERNS = (
    (FORBIDDEN_TERMS, "应使用「换型Setup」而非「设置」"),
)


def scan(name: str, text: str, patterns: tuple) -> list[str]:
    issues: list[str] = []
    for pattern, msg in patterns:
        for m in pattern.finditer(text):
            line = text[: m.start()].count("\n") + 1
            snippet = text[max(0, m.start() - 20) : m.end() + 20].replace("\n", " ")
            issues.append(f"{name} L{line}: {msg} → …{snippet}…")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit proposal framing and terminology.")
    parser.add_argument(
        "--strict-section1",
        action="store_true",
        default=True,
        help="Apply numeric/past-framing checks to SECTION1 only (default).",
    )
    args = parser.parse_args()

    all_issues: list[str] = []
    all_issues.extend(scan("SECTION1_BODY", SECTION1_BODY, SECTION1_ONLY_PATTERNS))
    all_issues.extend(scan("SECTION1_BODY", SECTION1_BODY, ALL_SECTIONS_PATTERNS))
    all_issues.extend(scan("SECTION2", SECTION2, ALL_SECTIONS_PATTERNS))
    if args.strict_section1:
        all_issues.extend(scan("SECTION2", SECTION2, ((FORBIDDEN_NUMBERS, "§2 可行性等不应引用实验最优值"),)))
    all_issues.extend(scan("SECTION3", SECTION3, ALL_SECTIONS_PATTERNS))
    if args.strict_section1:
        all_issues.extend(
            scan(
                "SECTION3",
                SECTION3,
                (
                    (FORBIDDEN_NUMBERS, "§3 研究基础不应写实验数值"),
                    (re.compile(r"初步实验结果"), "§3 不应有「初步实验结果」段落"),
                ),
            )
        )

    if all_issues:
        print("FAIL: proposal framing audit")
        for item in all_issues:
            print(f"  - {item}")
        return 1

    print("OK: proposal framing audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
