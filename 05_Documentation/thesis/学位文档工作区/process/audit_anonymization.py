# -*- coding: utf-8 -*-
"""D5: De-identification scan for proposal body."""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

ALL_TEXT = "\n".join((SECTION1_BODY, SECTION2, SECTION3))

FORBIDDEN = [
    (re.compile(r"SanDisk|Sandisk", re.I), "品牌名 SanDisk"),
    (re.compile(r"Simio_Import_Data|SPAN\.xlsx"), "内部数据文件名"),
    (re.compile(r"U盘|USB闪存|存储卡"), "可识别终端产品场景"),
    (re.compile(r"导师"), "人事安排句式「导师…」"),
    (re.compile(r"fill_template|section_content\.py|BIBLIOGRAPHY\.yaml"), "内部脚本/文件名"),
]


def main() -> int:
    issues: list[str] = []
    for pattern, msg in FORBIDDEN:
        for m in pattern.finditer(ALL_TEXT):
            line = ALL_TEXT[: m.start()].count("\n") + 1
            snippet = ALL_TEXT[max(0, m.start() - 10) : m.end() + 10].replace("\n", " ")
            issues.append(f"L{line}: {msg} → …{snippet}…")

    if issues:
        print("FAIL: anonymization audit")
        for item in issues:
            print(f"  - {item}")
        return 1

    print("OK: anonymization audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
