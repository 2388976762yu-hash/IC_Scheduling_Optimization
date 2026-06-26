# -*- coding: utf-8 -*-
"""仅重写 R11 参考文献块：中文条目去掉多余空格，外文保留英文词间空格。

用法：
  python ensure_doc_closed.py --close
  python strip_reference_spaces_local.py
"""
from __future__ import annotations

import sys

from doc_paths import KAITI_DOC
from ensure_doc_closed import ensure_documents_closed
from fill_template import build_reference_block
from fix_references_local import replace_reference_block

import win32com.client


def strip_reference_spaces(*, dry_run: bool = False) -> None:
    new_refs = build_reference_block()
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    saved = False
    try:
        doc = word.Documents.Open(str(KAITI_DOC.resolve()), ReadOnly=dry_run)
        r11 = doc.Tables(2).Cell(11, 1)
        replace_reference_block(r11, new_refs, dry_run=dry_run)
        if dry_run:
            print("Preview first Chinese line:")
            for line in new_refs.splitlines():
                if line.startswith("[1]"):
                    print(line)
                    break
            return
        doc.Save()
        saved = True
        print(f"Stripped extra spaces in reference block: {KAITI_DOC.name}")
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
    try:
        ensure_documents_closed(auto_close=True)
        strip_reference_spaces()
    except Exception as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
