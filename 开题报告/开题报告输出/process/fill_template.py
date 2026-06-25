# -*- coding: utf-8 -*-
"""Fill official Nankai 开题报告 template tables.

封面与 Table 1 / Table 2 基础信息（姓名、题目、课题来源、导师等）
以 TEMPLATE 中已填写内容为准，本脚本**只**写入正文单元格 R11/R13/R15。
修改基础信息请直接编辑模板 doc，勿在本脚本中硬编码覆盖。

**注意**：`02_开题报告_提交版.doc` 手调版式后以 02 为提交真源；bulk 改字见 WRITING_RULES.md / METADATA_POLICY.md。
"""
import os
import shutil
import stat
import subprocess
import time
import win32com.client
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

from section_content import SECTION1_BODY, SECTION2, SECTION3
from ensure_doc_closed import ensure_documents_closed

ROOT = Path(__file__).resolve().parents[1]
PROCESS = Path(__file__).resolve().parent
TEMPLATE = ROOT.parent / "2120253828-喻炫琪-研究生开题报告.doc"
OUTPUT = ROOT / "02_开题报告_提交版.doc"
BIBLIOGRAPHY = PROCESS / "BIBLIOGRAPHY.yaml"

# Table 2 正文内容行（其余行由模板保留，见 METADATA_POLICY.md）
CONTENT_ROWS = (11, 13, 15)

# 生成后抽样核对：这些键必须与模板一致
METADATA_CHECK_KEYS = (
    (1, 2, 2),   # Table1 姓名
    (1, 3, 2),   # Table1 学号
    (2, 4, 2),   # Table2 课题来源
    (2, 7, 2),   # Table2 导师姓名
)


def _author_string(authors):
    if len(authors) == 1:
        return authors[0].split(",")[0].strip()
    if len(authors) == 2:
        a, b = authors
        if any("\u4e00" <= c <= "\u9fff" for c in a):
            return f"{a}，{b}"
        return f"{a}, {b}"
    first = authors[0].split(",")[0].strip()
    if any("\u4e00" <= c <= "\u9fff" for c in first):
        return f"{first}，等"
    return f"{first}, et al."


def format_gbt7714(ref):
    """Format one reference entry (GB/T 7714-2015 style)."""
    authors = ref.get("authors", [])
    author_str = _author_string(authors)
    year = ref.get("year", "")
    title = ref.get("title", "")
    ref_type = ref.get("type", "J")

    if ref_type == "M":
        edition = ref.get("edition", "")
        ed_part = f"{edition} ed. " if edition else ""
        place = ref.get("place", "")
        publisher = ref.get("publisher", "")
        return (
            f"{author_str}. {title}[M]. {ed_part}{place}: {publisher}, {year}."
        )

    if ref_type == "C":
        venue = ref.get("venue", "")
        pages = ref.get("pages", "")
        page_part = f": {pages}" if pages else ""
        return f"{author_str}. {title}[C]//{venue}. {year}{page_part}."

    # Journal [J]
    venue = ref.get("venue", "")
    volume = ref.get("volume", "")
    issue = ref.get("issue", "")
    pages = ref.get("pages", "")
    vol_issue = volume
    if issue:
        vol_issue = f"{volume}({issue})"
    return f"{author_str}. {title}[J]. {venue}, {year}, {vol_issue}: {pages}."


def _first_author(ref):
    authors = ref.get("authors", [])
    return authors[0] if authors else ""


def _is_chinese_ref(ref):
    return any("\u4e00" <= c <= "\u9fff" for c in _first_author(ref))


def load_references():
    if yaml is None:
        raise RuntimeError("PyYAML required: pip install pyyaml")
    data = yaml.safe_load(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    refs = data.get("references", [])
    chinese = sorted(
        [r for r in refs if _is_chinese_ref(r)],
        key=lambda r: r["sort_key"].upper(),
    )
    foreign = sorted(
        [r for r in refs if not _is_chinese_ref(r)],
        key=lambda r: r["sort_key"].upper(),
    )
    return chinese, foreign


def build_reference_block():
    chinese, foreign = load_references()
    lines = []
    idx = 1
    if chinese:
        lines.append("中文文献")
        for ref in chinese:
            lines.append(f"[{idx}] {format_gbt7714(ref)}")
            idx += 1
    if foreign:
        if chinese:
            lines.append("")
        lines.append("外文文献")
        for ref in foreign:
            lines.append(f"[{idx}] {format_gbt7714(ref)}")
            idx += 1
    return "\n".join(lines)


def build_section1():
    return SECTION1_BODY + "\n\n" + build_reference_block()


def ensure_writable(path: Path):
    """Clear Windows read-only flag so WPS/Word can save in place."""
    if not path.exists():
        return
    os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
    if hasattr(path, "stat"):
        attrs = path.stat().st_file_attributes
        if attrs & stat.FILE_ATTRIBUTE_READONLY:
            os.chmod(path, attrs & ~stat.FILE_ATTRIBUTE_READONLY)


def prepare_doc_for_editing(doc):
    """Avoid 'read-only recommended' / protection blocking saves in WPS."""
    try:
        doc.ReadOnlyRecommended = False
    except Exception:
        pass
    try:
        if doc.ProtectionType != -1:
            doc.Unprotect(Password="")
    except Exception:
        pass


def apply_content_cell(cell, content):
    cell.Range.Text = content
    cell.Range.Font.Name = "Times New Roman"
    cell.Range.Font.NameFarEast = "宋体"
    cell.Range.Font.Size = 12
    cell.Range.ParagraphFormat.LineSpacingRule = 1
    cell.Range.ParagraphFormat.LineSpacing = 24


def _cell_text(table, row, col):
    return (
        table.Cell(row, col)
        .Range.Text.replace("\r\x07", "")
        .replace("\x07", "")
        .strip()
    )


def verify_metadata_unchanged(word, doc):
    """Ensure output still matches template for sampled metadata cells."""
    t1 = doc.Tables(1)
    t2 = doc.Tables(2)
    tables = {1: t1, 2: t2}
    tpl_doc = word.Documents.Open(str(TEMPLATE.resolve()))
    try:
        tpl_t1 = tpl_doc.Tables(1)
        tpl_t2 = tpl_doc.Tables(2)
        tpl_tables = {1: tpl_t1, 2: tpl_t2}
        mismatches = []
        for table_idx, row, col in METADATA_CHECK_KEYS:
            tpl_val = _cell_text(tpl_tables[table_idx], row, col)
            out_val = _cell_text(tables[table_idx], row, col)
            if tpl_val != out_val:
                mismatches.append((table_idx, row, col, tpl_val, out_val))
    finally:
        tpl_doc.Close(SaveChanges=False)

    if mismatches:
        details = "\n".join(
            f"  T{ti}R{r}C{c}: template={tpl!r} output={out!r}"
            for ti, r, c, tpl, out in mismatches
        )
        raise RuntimeError(
            "Metadata mismatch after fill (should not overwrite template):\n"
            + details
        )


def close_word_app(word):
    """Close all documents and quit Word COM (wdDoNotSaveChanges=0)."""
    try:
        while word.Documents.Count > 0:
            word.Documents(1).Close(SaveChanges=0)
    except Exception:
        pass
    try:
        word.Quit(SaveChanges=0)
    except Exception:
        pass
    # 脚本启动的 Word 偶发 Quit 后仍残留，会锁 doc；仅在此情况下结束 WINWORD
    time.sleep(0.8)
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


def main():
    ensure_documents_closed(auto_close=True)
    section1 = build_section1()
    if OUTPUT.exists():
        try:
            OUTPUT.unlink()
        except OSError as exc:
            raise RuntimeError(
                f"Cannot replace {OUTPUT.name}: close it in WPS/Word first."
            ) from exc

    shutil.copy2(TEMPLATE, OUTPUT)
    ensure_writable(OUTPUT)

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    doc = None
    saved = False
    try:
        doc = word.Documents.Open(str(OUTPUT.resolve()), ReadOnly=False)
        prepare_doc_for_editing(doc)

        t2 = doc.Tables(2)
        content_by_row = {
            11: section1,
            13: SECTION2,
            15: SECTION3,
        }
        for row in CONTENT_ROWS:
            apply_content_cell(t2.Cell(row, 1), content_by_row[row])

        verify_metadata_unchanged(word, doc)
        prepare_doc_for_editing(doc)
        doc.Save()
        saved = True
    finally:
        if doc is not None:
            try:
                doc.Close(SaveChanges=saved)
            except Exception:
                pass
        close_word_app(word)

    ensure_writable(OUTPUT)

    char_count = len(section1) + len(SECTION2) + len(SECTION3)
    chinese, foreign = load_references()
    ref_count = len(chinese) + len(foreign)
    print(f"Filled: {OUTPUT}")
    print(f"References: {ref_count}")
    print(f"Approx chars (sections): {char_count}")
    print(
        "Note: re-run overwrites R11/R13/R15 text; manual formatting in 02 is lost. "
        "Edit 02 directly for final submission polish."
    )


if __name__ == "__main__":
    main()
