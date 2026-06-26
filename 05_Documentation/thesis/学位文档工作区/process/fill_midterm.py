# -*- coding: utf-8 -*-
"""Fill midterm report / assessment form **in place** on the local submission .doc.

Default: never copy from blank template; never overwrite non-empty cells the user edited.
Use --restore-from-blank only when you explicitly want to reset table layout from 参考资料.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import time
import win32com.client

from doc_paths import (
    KAITI_DOC,
    MIDTERM_FORM_BLANK,
    MIDTERM_FORM_DOC,
    MIDTERM_REPORT_DOC,
)
from ensure_doc_closed import ensure_documents_closed
from midterm_section_content import (
    FORM_ABSTRACT_HEADER,
    FORM_ADVISOR_RELATION,
    FORM_TOPIC_NATURE,
    KEYWORDS_CN,
    KEYWORDS_EN,
    MIDTERM_ABSTRACT,
    THESIS_TITLE_CN,
    THESIS_TITLE_EN,
    midterm_report_paragraphs,
)

REPORT_DOC = MIDTERM_REPORT_DOC
FORM_DOC = MIDTERM_FORM_DOC
REPORT_TITLE_CELL = (1, 2)
BODY_TITLE_PARAGRAPH = 50
BODY_DELETE_FROM = 51

# Table2 rows the script must never touch (学院填写 / 考核组)
FORM_PROTECTED_T2_ROWS = (6, 7)

FORM_COVER = {
    (1, 2): "title",
    (2, 2): "喻炫琪",
    (3, 2): "2120253828",
    (4, 2): "南开大学商学院",
    (5, 2): "管理科学与工程",
    (6, 2): "管理学硕士",
    (7, 2): "王谦",
    (9, 2): "系统建模与仿真",
    (10, 2): "2026.07.03",
}


def close_word_app(word):
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
    listed = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq WINWORD.EXE", "/NH"],
        capture_output=True,
        text=True,
        check=False,
    )
    if listed.stdout and "WINWORD.EXE" in listed.stdout:
        subprocess.run(
            ["taskkill", "/F", "/IM", "WINWORD.EXE"],
            capture_output=True,
            check=False,
        )


def cell_plain(cell) -> str:
    return cell.Range.Text.replace("\r\x07", "").replace("\x07", "").replace("\r", "")


def cell_is_empty(cell) -> bool:
    return not cell_plain(cell).strip()


def set_if_empty(cell, text: str, label: str) -> bool:
    if not cell_is_empty(cell):
        print(f"  skip (已有内容): {label}")
        return False
    cell.Range.Text = text
    print(f"  filled: {label}")
    return True


def checkbox_cell_is_set(cell) -> bool:
    plain = cell_plain(cell)
    return "√" in plain or "☑" in plain or "✓" in plain


def mark_checkbox_option(cell, option_label: str) -> bool:
    if checkbox_cell_is_set(cell):
        print(f"  skip checkbox (本地已有勾选，不改动): {option_label}")
        return False
    plain = cell_plain(cell)
    raw = cell.Range.Text
    for needle, repl in (
        (f"( {option_label}", f"( √ {option_label}"),
        (f"({option_label}", f"( √ {option_label}"),
    ):
        if needle in plain:
            new_plain = plain.replace(needle, repl, 1)
            if raw.endswith("\r\x07"):
                cell.Range.Text = new_plain + "\r\x07"
            elif raw.endswith("\x07"):
                cell.Range.Text = new_plain + "\x07"
            else:
                cell.Range.Text = new_plain
            print(f"  checked: {option_label}")
            return True
    print(f"  warn: checkbox not found: {option_label}")
    return False


def abstract_body_after_header(cell, header: str) -> str:
    plain = cell_plain(cell)
    if header not in plain:
        return plain.strip()
    return plain.split(header, 1)[1].strip()


def fill_abstract_if_empty(cell, header: str, body: str, *, force: bool = False) -> bool:
    rest = abstract_body_after_header(cell, header)
    if not rest:
        for legacy in ("一、中期报告摘要（300字左右）", "一、中期报告摘要"):
            if legacy != header:
                rest = abstract_body_after_header(cell, legacy)
                if rest:
                    break
    if rest and not force:
        if rest == body.strip() or len(rest) > 30:
            print("  skip abstract (保留本地已写摘要)")
            return False
        print("  skip abstract (单元格已有文字，未使用 --force)")
        return False
    raw = cell.Range.Text
    suffix = ""
    if raw.endswith("\x07"):
        core = raw[:-1]
        trailing = core[len(core.rstrip("\r")) :]
        suffix = trailing + "\x07" if trailing else "\r\r\r\r\r\x07"
    else:
        suffix = "\r\r\r\r\r"
    cell.Range.Text = header + "\r" + body + suffix
    print("  filled: abstract")
    return True


def read_kaiti_title_cn() -> str:
    if not KAITI_DOC.exists():
        return THESIS_TITLE_CN
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(str(KAITI_DOC.resolve()), ReadOnly=True)
        try:
            val = cell_plain(doc.Tables(1).Cell(1, 2)).strip().splitlines()[0].strip()
            return val or THESIS_TITLE_CN
        finally:
            doc.Close(SaveChanges=False)
    finally:
        word.Quit(SaveChanges=0)


def _para_text(doc, index: int) -> str:
    return (
        doc.Paragraphs(index)
        .Range.Text.replace("\r", "")
        .replace("\x07", "")
        .strip()
    )


def _report_body_has_user_content(doc) -> bool:
    t = _para_text(doc, BODY_TITLE_PARAGRAPH)
    if not t:
        return False
    if "重点论述部分" in t or "中期报告提纲" in t:
        return False
    if t.startswith("一、") and len(t) > 40:
        return True
    if "1.1" in t or "研究进展" in t:
        return True
    return len(t) > 200


def fill_report(word, title_cn: str, *, rewrite_body: bool = False) -> None:
    doc = word.Documents.Open(str(REPORT_DOC.resolve()), ReadOnly=False)
    try:
        t1 = doc.Tables(1)
        set_if_empty(t1.Cell(*REPORT_TITLE_CELL), title_cn, "cover title")

        if rewrite_body:
            for i in range(1, doc.Paragraphs.Count + 1):
                if "中期报告提纲" in _para_text(doc, i):
                    doc.Paragraphs(i).Range.Text = "\r"
                    break
            body_end = BODY_DELETE_FROM
            for i in range(doc.Paragraphs.Count, BODY_DELETE_FROM - 1, -1):
                t = _para_text(doc, i)
                if i == BODY_TITLE_PARAGRAPH:
                    break
                if i >= BODY_DELETE_FROM and t and not t.startswith("说"):
                    doc.Paragraphs(i).Range.Delete()
            lines = midterm_report_paragraphs()
            doc.Paragraphs(BODY_TITLE_PARAGRAPH).Range.Text = "\r".join(lines) + "\r"
            print("  rewrote report body (--rewrite-body)")
        elif _report_body_has_user_content(doc):
            print("  skip report body (保留本地正文)")
        else:
            lines = midterm_report_paragraphs()
            doc.Paragraphs(BODY_TITLE_PARAGRAPH).Range.Text = "\r".join(lines) + "\r"
            print("  filled empty report body")

        doc.Save()
        print(f"Saved in place: {REPORT_DOC.name}")
    finally:
        doc.Close(SaveChanges=True)


def fill_form(
    word,
    title_cn: str,
    *,
    force: bool = False,
    restore_from_blank: bool = False,
    abstract_only: bool = False,
    fill_checkboxes: bool = False,
) -> None:
    if restore_from_blank:
        if not MIDTERM_FORM_BLANK.exists():
            raise FileNotFoundError(f"Missing: {MIDTERM_FORM_BLANK}")
        shutil.copy2(MIDTERM_FORM_BLANK, FORM_DOC)
        print("  WARNING: restored from blank template (本地修改已丢失，除非你有备份)")

    doc = word.Documents.Open(str(FORM_DOC.resolve()), ReadOnly=False)
    try:
        t2 = doc.Tables(2)
        if abstract_only:
            print("  abstract-only (不碰勾选项与其它单元格):")
            fill_abstract_if_empty(
                t2.Cell(5, 1),
                FORM_ABSTRACT_HEADER,
                MIDTERM_ABSTRACT,
                force=force,
            )
        else:
            print("  in-place edit (不覆盖已有单元格):")
            t1 = doc.Tables(1)
            for (row, col), value in FORM_COVER.items():
                text = title_cn if value == "title" else value
                set_if_empty(t1.Cell(row, col), text, f"T1 R{row}C{col}")

            set_if_empty(
                t2.Cell(1, 2),
                f"{title_cn}\r{THESIS_TITLE_EN}",
                "thesis title",
            )
            set_if_empty(
                t2.Cell(2, 2),
                f"{KEYWORDS_CN}\r{KEYWORDS_EN}",
                "keywords",
            )
            if fill_checkboxes:
                mark_checkbox_option(t2.Cell(3, 2), FORM_TOPIC_NATURE)
                mark_checkbox_option(t2.Cell(4, 2), FORM_ADVISOR_RELATION)
            else:
                print("  skip checkboxes (默认不改动本地勾选项)")
            fill_abstract_if_empty(
                t2.Cell(5, 1),
                FORM_ABSTRACT_HEADER,
                MIDTERM_ABSTRACT,
                force=force,
            )

        doc.Save()
        print(f"Saved in place: {FORM_DOC.name}")
    finally:
        doc.Close(SaveChanges=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fill midterm docs in place on local submission files.",
    )
    parser.add_argument("--report-only", action="store_true")
    parser.add_argument("--form-only", action="store_true")
    parser.add_argument(
        "--restore-from-blank",
        action="store_true",
        help="DANGER: copy blank 考核表 template over submission file first",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite abstract even if non-empty (use with --abstract-only)",
    )
    parser.add_argument(
        "--abstract-only",
        action="store_true",
        help="Only update Table2 R5 abstract; never touch checkbox rows",
    )
    parser.add_argument(
        "--fill-checkboxes",
        action="store_true",
        help="Explicitly write checkbox marks into empty/unmarked rows only",
    )
    parser.add_argument(
        "--rewrite-body",
        action="store_true",
        help="DANGER: rewrite midterm report body paragraphs",
    )
    args = parser.parse_args()

    ensure_documents_closed(auto_close=True)

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        title_cn = read_kaiti_title_cn()
        if not args.form_only:
            fill_report(word, title_cn, rewrite_body=args.rewrite_body)
        if not args.report_only:
            fill_form(
                word,
                title_cn,
                force=args.force,
                restore_from_blank=args.restore_from_blank,
                abstract_only=args.abstract_only,
                fill_checkboxes=args.fill_checkboxes,
            )
    finally:
        close_word_app(word)

    print("Done (local file updated in place).")


if __name__ == "__main__":
    main()
