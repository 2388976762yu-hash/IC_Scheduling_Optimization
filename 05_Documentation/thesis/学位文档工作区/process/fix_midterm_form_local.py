# -*- coding: utf-8 -*-
"""Minimal in-place fixes on local 中期考核表 — no template restore, no overwrite of filled fields.

Usage (WPS/Word must be closed):
  python fix_midterm_form_local.py
"""
from __future__ import annotations

import re
import subprocess
import sys
import time
import win32com.client

from doc_paths import MIDTERM_FORM_DOC
from ensure_doc_closed import ensure_documents_closed

GUIDANCE_PATTERNS = (
    re.compile(r"（300\s*字左右）"),
    re.compile(r"\(300\s*字左右\)"),
    re.compile(r"（300字左右）"),
)


def close_word(word):
    try:
        while word.Documents.Count > 0:
            word.Documents(1).Close(SaveChanges=0)
    except Exception:
        pass
    try:
        word.Quit(SaveChanges=0)
    except Exception:
        pass
    time.sleep(0.5)
    subprocess.run(
        ["taskkill", "/F", "/IM", "WINWORD.EXE"],
        capture_output=True,
        check=False,
    )


def cell_plain(cell) -> str:
    return cell.Range.Text.replace("\r\x07", "").replace("\x07", "").replace("\r", "")


def strip_guidance_from_header(cell) -> bool:
    raw = cell.Range.Text
    new_raw = raw
    for pat in GUIDANCE_PATTERNS:
        new_raw = pat.sub("", new_raw, count=1)
    if new_raw == raw:
        return False
    cell.Range.Text = new_raw
    return True


def normalize_checkbox_cell(cell, option: str) -> bool:
    plain = cell_plain(cell)
    if f"( √ {option}" in plain or f"(√{option}" in plain:
        return False
    needle = f"( {option}"
    if needle not in plain:
        return False
    new_plain = plain.replace(needle, f"( √ {option}", 1)
    raw = cell.Range.Text
    if raw.endswith("\r\x07"):
        cell.Range.Text = new_plain + "\r\x07"
    elif raw.endswith("\x07"):
        cell.Range.Text = new_plain + "\x07"
    else:
        cell.Range.Text = new_plain
    return True


def main() -> int:
    try:
        ensure_documents_closed(auto_close=True)
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = word.Documents.Open(str(MIDTERM_FORM_DOC.resolve()), ReadOnly=False)
    try:
        t2 = doc.Tables(2)
        changes = []

        if strip_guidance_from_header(t2.Cell(5, 1)):
            changes.append("摘要标题：已去掉「（300字左右）」")
        if normalize_checkbox_cell(t2.Cell(3, 2), "应用研究"):
            changes.append("课题性质：已确认勾选「应用研究」")
        if normalize_checkbox_cell(t2.Cell(4, 2), "与导师研究课题无关"):
            changes.append("导师关系：已确认勾选「与导师研究课题无关」")

        if not changes:
            print("无需修改。")
        else:
            for line in changes:
                print(line)
            doc.Save()
            print(f"已保存: {MIDTERM_FORM_DOC.name}")
    finally:
        doc.Close(SaveChanges=True)
        close_word(word)

    return 0


if __name__ == "__main__":
    sys.exit(main())
