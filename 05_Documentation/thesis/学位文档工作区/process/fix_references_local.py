# -*- coding: utf-8 -*-
"""仅修正开题报告 Word 中的参考文献列表与正文著者-出版年引用（Find 替换，不改其它段落）。

规则（用户指定）：
- 文献列表：作者 ≤2 人写全；≥3 人写前 2 人 + 等 / et al
- 正文引用：仅 1 人写姓名；≥2 人写第一著者 + 等

用法：
  python ensure_doc_closed.py --close
  python fix_references_local.py
  python fix_references_local.py --dry-run
"""
from __future__ import annotations

import argparse
import sys

import win32com.client

from doc_paths import KAITI_DOC
from ensure_doc_closed import ensure_documents_closed
from fill_template import build_reference_block

CONTENT_ROWS = (11, 13, 15)

# 长串优先；只替换正文中的双作者旧写法 → 第一著者等
INTEXT_REPLACEMENTS = (
    ("Sang-Jin Lee 与 Tae-Eog Lee（", "Lee等（"),
    ("Potts和Van Wassenhove（", "Potts等（"),
    ("Panwalkar和Iskander（", "Panwalkar等（"),
    ("Habenicht和Mönch（", "Habenicht等（"),
    ("Stubbe和Rose（", "Stubbe等（"),
    ("Luttmann和Xie（", "Luttmann等（"),
    ("Jain和Meeran（", "Jain等（"),
    ("Lin 和 Chen（", "Lin等（"),
    ("Lin和Chen（", "Lin等（"),
    ("Banks 等（", "Banks等（"),
    ("Chen-Ritzo 等（", "Chen-Ritzo等（"),
)

WD_REPLACE_ALL = 2


INTEXT_REPLACEMENTS = (
    if old == new or old not in cell.Range.Text:
        return 0
    if dry_run:
        return cell.Range.Text.count(old)
    finder = cell.Range.Find
    finder.ClearFormatting()
    finder.Replacement.ClearFormatting()
    finder.Text = old
    finder.Replacement.Text = new
    finder.Forward = True
    finder.Wrap = 0
    finder.Format = False
    finder.MatchCase = True
    finder.MatchWholeWord = False
    if not finder.Execute(Replace=WD_REPLACE_ALL):
        return 0
    return 1


def replace_reference_block(cell, new_block: str, *, dry_run: bool) -> bool:
    dup = cell.Range.Duplicate
    find = dup.Find
    find.ClearFormatting()
    find.Text = "中文文献"
    find.Forward = True
    find.Wrap = 0
    if not find.Execute():
        raise RuntimeError("R11 中未找到「中文文献」起始标记")

    start = dup.Start
    end = cell.Range.End - 1
    if dry_run:
        old_len = end - start
        print(f"Would replace reference block from 中文文献 ({old_len} chars) → {len(new_block)} chars")
        return True

    replace_rng = cell.Range
    replace_rng.SetRange(start, end)
    replace_rng.Text = new_block + "\r"
    return True


def normalize_intext_spacing_in_cell(cell, *, dry_run: bool) -> None:
    """「著者 等（」→「著者等（」，Find 替换保留版式。"""
    if " 等（" not in cell.Range.Text:
        return
    if dry_run:
        return
    finder = cell.Range.Find
    finder.ClearFormatting()
    finder.Replacement.ClearFormatting()
    finder.Text = " 等（"
    finder.Replacement.Text = "等（"
    finder.Forward = True
    finder.Wrap = 0
    finder.Execute(Replace=WD_REPLACE_ALL)


def fix_document(*, dry_run: bool = False) -> None:
    new_refs = build_reference_block()
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    saved = False
    try:
        doc = word.Documents.Open(str(KAITI_DOC.resolve()), ReadOnly=dry_run)
        t2 = doc.Tables(2)

        r11 = t2.Cell(11, 1)
        replace_reference_block(r11, new_refs, dry_run=dry_run)

        total = 0
        for row in CONTENT_ROWS:
            cell = t2.Cell(row, 1)
            for old, new in INTEXT_REPLACEMENTS:
                total += replace_in_cell(cell, old, new, dry_run=dry_run)
            normalize_intext_spacing_in_cell(cell, dry_run=dry_run)

        if dry_run:
            print(f"In-text pattern passes (rows {CONTENT_ROWS}): {len(INTEXT_REPLACEMENTS)} rules")
            return

        doc.Save()
        saved = True
        print(f"Updated references in {KAITI_DOC.name}")
        print(f"Applied in-text citation replacements across R{CONTENT_ROWS}")
    finally:
        if doc is not None:
            try:
                doc.Close(SaveChanges=saved)
            except Exception:
                pass
        try:
            word.Quit()
        except Exception:
            pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix bibliography and in-text citations in kaiti doc only.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        if not args.dry_run:
            ensure_documents_closed(auto_close=True)
        fix_document(dry_run=args.dry_run)
    except Exception as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
