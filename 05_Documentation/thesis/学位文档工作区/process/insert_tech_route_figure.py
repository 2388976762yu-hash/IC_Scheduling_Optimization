# -*- coding: utf-8 -*-
"""在开题报告 R13「2.1 研究思路与技术路线」段落后插入技术路线图（仅增图，不改正文）。

用法：
  python ensure_doc_closed.py --close
  python insert_tech_route_figure.py
  python insert_tech_route_figure.py --dry-run
"""
from __future__ import annotations

import argparse
import sys

import win32com.client

from doc_paths import KAITI_DOC, WORKSPACE

FIGURE_PATH = WORKSPACE / "figures" / "开题报告_技术路线图_提交.png"
CONTENT_ROW = 13
MARKER = "技术路线如下"
CAPTION = "图1 技术路线图"
WIDTH_CM = 13.0

WD_ALIGN_PARAGRAPH_CENTER = 1
WD_COLLAPSE_END = 0


def _para_text(para) -> str:
    return para.Range.Text.replace("\r\x07", "").replace("\x07", "").strip()


def find_marker_paragraph(cell):
    for i in range(1, cell.Range.Paragraphs.Count + 1):
        para = cell.Range.Paragraphs(i)
        if MARKER in _para_text(para):
            return i, para
    return None, None


def figure_already_present(cell) -> bool:
    if cell.Range.InlineShapes.Count > 0:
        return True
    for i in range(1, cell.Range.Paragraphs.Count + 1):
        if CAPTION in _para_text(cell.Range.Paragraphs(i)):
            return True
    return False


def insert_figure(*, dry_run: bool = False) -> None:
    if not FIGURE_PATH.is_file():
        raise FileNotFoundError(f"Missing figure: {FIGURE_PATH}")
    if not KAITI_DOC.is_file():
        raise FileNotFoundError(f"Missing doc: {KAITI_DOC}")

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    saved = False
    try:
        doc = word.Documents.Open(str(KAITI_DOC.resolve()), ReadOnly=dry_run)
        cell = doc.Tables(2).Cell(CONTENT_ROW, 1)

        if figure_already_present(cell):
            print("Skip: figure or caption already present in R13.")
            return

        idx, marker_para = find_marker_paragraph(cell)
        if marker_para is None:
            raise RuntimeError(f'Cannot find paragraph containing "{MARKER}" in R13.')

        print(f"Target: R13 paragraph {idx}: {_para_text(marker_para)[:60]}...")
        if dry_run:
            print(f"Would insert: {FIGURE_PATH.name} ({WIDTH_CM} cm wide), caption: {CAPTION}")
            return

        anchor = marker_para.Range
        anchor.Collapse(WD_COLLAPSE_END)
        anchor.InsertParagraphAfter()

        fig_para = cell.Range.Paragraphs(idx + 1)
        fig_rng = fig_para.Range
        fig_rng.ParagraphFormat.Alignment = WD_ALIGN_PARAGRAPH_CENTER
        fig_rng.ParagraphFormat.FirstLineIndent = 0
        fig_rng.ParagraphFormat.CharacterUnitFirstLineIndent = 0

        inline = fig_rng.InlineShapes.AddPicture(
            FileName=str(FIGURE_PATH.resolve()),
            LinkToFile=False,
            SaveWithDocument=True,
        )
        inline.LockAspectRatio = True
        inline.Width = WIDTH_CM / 2.54 * 72

        fig_rng.InsertParagraphAfter()
        cap_para = cell.Range.Paragraphs(idx + 2)
        cap_rng = cap_para.Range
        cap_rng.Text = CAPTION + "\r"
        cap_rng.ParagraphFormat.Alignment = WD_ALIGN_PARAGRAPH_CENTER
        cap_rng.ParagraphFormat.FirstLineIndent = 0
        cap_rng.ParagraphFormat.CharacterUnitFirstLineIndent = 0
        cap_rng.Font.NameFarEast = "宋体"
        cap_rng.Font.Name = "Times New Roman"
        cap_rng.Font.Size = 12

        doc.Save()
        saved = True
        print(f"Inserted figure into {KAITI_DOC.name}")
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
    parser = argparse.ArgumentParser(description="Insert tech-route figure into kaiti doc R13 only.")
    parser.add_argument("--dry-run", action="store_true", help="Locate anchor only; do not write.")
    args = parser.parse_args()
    try:
        from ensure_doc_closed import ensure_documents_closed

        if not args.dry_run:
            ensure_documents_closed(auto_close=True)
        insert_figure(dry_run=args.dry_run)
    except Exception as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
