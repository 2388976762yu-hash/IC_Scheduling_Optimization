# -*- coding: utf-8 -*-
"""D7: In-text citations vs BIBLIOGRAPHY.yaml."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

ALL_TEXT = SECTION1_BODY + SECTION2 + SECTION3
BIB = PROCESS / "BIBLIOGRAPHY.yaml"


def load_years() -> set[int]:
    data = yaml.safe_load(BIB.read_text(encoding="utf-8"))
    return {int(r["year"]) for r in data["references"]}


def main() -> int:
    issues: list[str] = []
    bib_years = load_years()

    if re.search(r"\[\d+\]", ALL_TEXT):
        issues.append("正文禁止 [1] 式引用，应使用著者-出版年")

    cited_years: set[int] = set()
    for m in re.finditer(r"（(\d{4}(?:，\d{4})*)）", ALL_TEXT):
        for y in re.findall(r"\d{4}", m.group(1)):
            cited_years.add(int(y))

    orphan = sorted(y for y in cited_years if y not in bib_years)
    if orphan:
        issues.append(f"正文引用年份不在 BIBLIOGRAPHY: {orphan}")

    if issues:
        print("FAIL: citations audit")
        for item in issues:
            print(f"  - {item}")
        return 1

    print(f"OK: citations audit passed ({len(cited_years)} distinct years cited).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
