# -*- coding: utf-8 -*-
"""Read-only extract of学院提交 .doc body text (never writes Word).

Usage:
  python read_submission_docs.py --kaiti
  python read_submission_docs.py --midterm
  python read_submission_docs.py --kaiti --midterm
"""
from __future__ import annotations

import argparse
import re
import sys

import win32com.client

from doc_paths import KAITI_DOC, MIDTERM_REPORT_DOC

_CLEAN = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x07]")


def _clean(text: str) -> str:
    return _clean.sub("", text.replace("\r", "\n")).strip()


def read_kaiti() -> dict[str, str]:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = word.Documents.Open(str(KAITI_DOC.resolve()), ReadOnly=True)
    try:
        t2 = doc.Tables(2)
        return {
            "R11": _clean(t2.Cell(11, 1).Range.Text),
            "R13": _clean(t2.Cell(13, 1).Range.Text),
            "R15": _clean(t2.Cell(15, 1).Range.Text),
        }
    finally:
        doc.Close(False)
        word.Quit()


def read_midterm(start: int = 48, end: int = 80) -> list[tuple[int, str]]:
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = word.Documents.Open(str(MIDTERM_REPORT_DOC.resolve()), ReadOnly=True)
    try:
        out: list[tuple[int, str]] = []
        for i in range(start, min(end, doc.Paragraphs.Count) + 1):
            t = doc.Paragraphs(i).Range.Text.replace("\r", "").strip()
            if t:
                out.append((i, t))
        return out
    finally:
        doc.Close(False)
        word.Quit()


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only dump of submission Word bodies.")
    parser.add_argument("--kaiti", action="store_true")
    parser.add_argument("--midterm", action="store_true")
    args = parser.parse_args()
    if not args.kaiti and not args.midterm:
        args.kaiti = True

    if args.kaiti:
        print(f"=== {KAITI_DOC.name} ===")
        for key, text in read_kaiti().items():
            print(f"\n--- {key} ({len(text)} chars) ---\n{text}")

    if args.midterm:
        print(f"\n=== {MIDTERM_REPORT_DOC.name} ===")
        for idx, text in read_midterm():
            print(f"\nP{idx}: {text}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
