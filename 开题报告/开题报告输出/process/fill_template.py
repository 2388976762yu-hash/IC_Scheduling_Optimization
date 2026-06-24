# -*- coding: utf-8 -*-
"""Fill official Nankai 开题报告 template tables."""
import shutil
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
OUTPUT_DOCX = ROOT / "02_开题报告_提交版.docx"
OUTPUT_TMP = ROOT / "_tmp_开题报告_提交版.doc"
BIBLIOGRAPHY = PROCESS / "BIBLIOGRAPHY.yaml"

TITLE_CN = "多目标优化的半导体后端制造生产排程研究"
TITLE_EN = (
    "Multi-Objective Optimization of Production Scheduling in "
    "Semiconductor Backend Manufacturing"
)

WD_FORMAT_XML_DOCUMENT = 16


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


def set_cell(table, row, col, text, font_name="宋体", font_size=12):
    cell = table.Cell(row, col)
    cell.Range.Text = text
    cell.Range.Font.Name = font_name
    cell.Range.Font.NameFarEast = font_name
    cell.Range.Font.Size = font_size
    pf = cell.Range.ParagraphFormat
    pf.LineSpacingRule = 1
    pf.LineSpacing = 24


def apply_content_cell(cell, content):
    cell.Range.Text = content
    cell.Range.Font.Name = "Times New Roman"
    cell.Range.Font.NameFarEast = "宋体"
    cell.Range.Font.Size = 12
    cell.Range.ParagraphFormat.LineSpacingRule = 1
    cell.Range.ParagraphFormat.LineSpacing = 24


def main():
    section1 = build_section1()
    for stale in (OUTPUT, OUTPUT_DOCX, OUTPUT_TMP):
        if stale.exists():
            try:
                stale.unlink()
            except OSError:
                pass
    shutil.copy2(TEMPLATE, OUTPUT_TMP)
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(str(OUTPUT_TMP.resolve()))

    t1 = doc.Tables(1)
    t1.Cell(1, 2).Range.Text = TITLE_CN

    t2 = doc.Tables(2)
    t2.Cell(3, 2).Range.Text = f"{TITLE_CN}\n{TITLE_EN}"
    t2.Cell(4, 2).Range.Text = "导师科研项目"
    t2.Cell(5, 2).Range.Text = "预计开始时间：2026年6月      预计结束时间：2027年5月"
    t2.Cell(7, 2).Range.Text = "王谦"
    t2.Cell(7, 3).Range.Text = "副教授"
    t2.Cell(7, 4).Range.Text = "系统建模与仿真"

    for row, content in [(11, section1), (13, SECTION2), (15, SECTION3)]:
        apply_content_cell(t2.Cell(row, 1), content)

    doc.Save()
    try:
        doc.SaveAs2(str(OUTPUT_DOCX.resolve()), FileFormat=WD_FORMAT_XML_DOCUMENT)
    except Exception:
        pass
    doc.Close(SaveChanges=True)
    word.Quit()
    shutil.copy2(OUTPUT_TMP, OUTPUT)
    if OUTPUT_TMP.exists():
        OUTPUT_TMP.unlink()

    char_count = len(section1) + len(SECTION2) + len(SECTION3)
    ref_count = len(load_references())
    print(f"Filled: {OUTPUT}")
    print(f"Exported: {OUTPUT_DOCX}")
    print(f"References: {ref_count}")
    print(f"Approx chars (sections): {char_count}")


if __name__ == "__main__":
    main()
