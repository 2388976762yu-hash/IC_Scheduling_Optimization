# -*- coding: utf-8 -*-
"""Fill official Nankai 开题报告 template tables.

封面与 Table 1 / Table 2 基础信息（姓名、题目、课题来源、导师等）
以 TEMPLATE 中已填写内容为准，本脚本**只**写入正文单元格 R11/R13/R15。
修改基础信息请直接编辑模板 doc，勿在本脚本中硬编码覆盖。

**注意**：`02_开题报告_提交版.doc` 可在你手调版式后作为提交真源；
重复运行本脚本会覆盖三节正文并可能破坏已调格式，仅在 bulk 更新文字时使用。
"""
import os
import shutil
import stat
import win32com.client
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

from section_content import SECTION1_BODY, SECTION2, SECTION3

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


def load_references():
    if yaml is None:
        raise RuntimeError("PyYAML required: pip install pyyaml")
    data = yaml.safe_load(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    refs = data.get("references", [])
    return sorted(refs, key=lambda r: r["sort_key"].upper())


def build_reference_block():
    refs = load_references()
    lines = []
    for i, ref in enumerate(refs, start=1):
        lines.append(f"[{i}] {format_gbt7714(ref)}")
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
    tpl_t1 = tpl_doc.Tables(1)
    tpl_t2 = tpl_doc.Tables(2)
    tpl_tables = {1: tpl_t1, 2: tpl_t2}
    mismatches = []
    for table_idx, row, col in METADATA_CHECK_KEYS:
        tpl_val = _cell_text(tpl_tables[table_idx], row, col)
        out_val = _cell_text(tables[table_idx], row, col)
        if tpl_val != out_val:
            mismatches.append((table_idx, row, col, tpl_val, out_val))
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


def main():
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

    word = win32com.client.Dispatch("Word.Application")
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
            doc.Close(SaveChanges=saved)
        word.Quit()

    ensure_writable(OUTPUT)

    char_count = len(section1) + len(SECTION2) + len(SECTION3)
    ref_count = len(load_references())
    print(f"Filled: {OUTPUT}")
    print(f"References: {ref_count}")
    print(f"Approx chars (sections): {char_count}")
    print(
        "Note: re-run overwrites R11/R13/R15 text; manual formatting in 02 is lost. "
        "Edit 02 directly for final submission polish."
    )


if __name__ == "__main__":
    main()
