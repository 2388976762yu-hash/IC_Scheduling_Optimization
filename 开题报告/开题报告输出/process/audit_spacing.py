# -*- coding: utf-8 -*-
"""Audit blank lines in proposal text sources and optional Word R11/R13/R15."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
ROOT = PROCESS.parent
OUTPUT = ROOT / "02_开题报告_提交版.doc"

sys.path.insert(0, str(PROCESS))

from fill_template import build_section1, build_reference_block  # noqa: E402
from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402


def blank_line_report(name: str, text: str) -> list[int]:
    lines = text.splitlines()
    blanks = [i + 1 for i, line in enumerate(lines) if not line.strip()]
    print(f"{name}: lines={len(lines)} blank_lines={len(blanks)}")
    for b in blanks[:20]:
        prev = lines[b - 2][:50] if b > 1 else ""
        nxt = lines[b][:50] if b <= len(lines) else ""
        print(f"  L{b}: ...{prev!r} | EMPTY | {nxt!r}...")
    if len(blanks) > 20:
        print(f"  ... and {len(blanks) - 20} more")
    return blanks


def audit_word_cells() -> None:
    import win32com.client

    if not OUTPUT.exists():
        print(f"Word file missing: {OUTPUT}")
        return

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = word.Documents.Open(str(OUTPUT.resolve()), ReadOnly=True)
    try:
        t2 = doc.Tables(2)
        for row, label in ((11, "R11"), (13, "R13"), (15, "R15")):
            text = t2.Cell(row, 1).Range.Text.replace("\r\x07", "\n").replace("\x07", "")
            paras = [p for p in text.split("\r") if p is not None]
            empty = sum(1 for p in paras if not p.strip())
            print(f"Word {label}: paragraphs={len(paras)} empty_paragraphs={empty}")
    finally:
        doc.Close(False)
        word.Quit()


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit proposal blank lines.")
    parser.add_argument("--word", action="store_true", help="Also scan 02_开题报告_提交版.doc")
    args = parser.parse_args()

    total_blanks = 0
    for name, text in (
        ("SECTION1_BODY", SECTION1_BODY),
        ("SECTION2", SECTION2),
        ("SECTION3", SECTION3),
        ("reference_block", build_reference_block()),
        ("section1_full", build_section1()),
    ):
        total_blanks += len(blank_line_report(name, text))
        print()

    if args.word:
        audit_word_cells()

    if total_blanks:
        print(f"FAIL: {total_blanks} blank line(s) in text sources.")
        return 1
    print("OK: text sources have zero blank lines.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
