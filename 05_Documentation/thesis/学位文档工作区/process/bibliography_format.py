# -*- coding: utf-8 -*-
"""GB/T 7714 reference list formatting from BIBLIOGRAPHY.yaml (read-only, no Word I/O)."""
from __future__ import annotations

import re
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

from section_content import SECTION1_BODY, _compact_spacing

PROCESS = Path(__file__).resolve().parent
BIBLIOGRAPHY = PROCESS / "BIBLIOGRAPHY.yaml"


def _author_string(authors):
    """GB/T 7714 list authors: ≤3 list all; >3 list first three + 等 / et al."""
    if not authors:
        return ""
    chinese = any("\u4e00" <= c <= "\u9fff" for c in authors[0])
    if len(authors) == 1:
        a = authors[0]
        if chinese:
            return a
        if ", " in a:
            return a
        return a.split(",")[0].strip()
    if len(authors) <= 3:
        if chinese:
            return ",".join(authors)
        return ", ".join(authors)
    a, b, c = authors[0], authors[1], authors[2]
    if chinese:
        return f"{a},{b},{c},等"
    return f"{a}, {b}, {c}, et al"


def _compact_western_periods(text: str) -> str:
    return re.sub(r"\.\s+", ".", text)


def _compact_western_author(author_str: str) -> str:
    return author_str.replace(", ", ",")


def _author_title_join(author_str: str, title: str) -> str:
    if author_str.endswith("."):
        return f"{author_str}{title}"
    return f"{author_str}.{title}"


def format_gbt7714(ref):
    """Format one reference entry (GB/T 7714-2015 compact style)."""
    authors = ref.get("authors", [])
    author_str = _author_string(authors)
    year = ref.get("year", "")
    title = ref.get("title", "")
    ref_type = ref.get("type", "J")
    chinese = _is_chinese_ref(ref)

    if chinese and ref_type == "J":
        venue = ref.get("venue", "")
        volume = ref.get("volume", "")
        issue = ref.get("issue", "")
        pages = ref.get("pages", "")
        vol_issue = volume
        if issue:
            vol_issue = f"{volume}({issue})"
        return f"{_author_title_join(author_str, title)}[J].{venue},{year},{vol_issue}:{pages}."

    author_str = _compact_western_author(author_str)

    if ref_type == "M":
        edition = ref.get("edition", "")
        ed_part = f"{edition} ed." if edition else ""
        place = ref.get("place", "")
        publisher = ref.get("publisher", "")
        mid = f"{ed_part} " if ed_part else ""
        return _compact_western_periods(
            f"{_author_title_join(author_str, title)}[M].{mid}{place}:{publisher},{year}."
        )

    if ref_type == "C":
        venue = ref.get("venue", "")
        pages = ref.get("pages", "")
        page_part = f":{pages}" if pages else ""
        return _compact_western_periods(
            f"{_author_title_join(author_str, title)}[C]//{venue}.{year}{page_part}."
        )

    venue = ref.get("venue", "")
    volume = ref.get("volume", "")
    issue = ref.get("issue", "")
    pages = ref.get("pages", "")
    vol_issue = volume
    if issue:
        vol_issue = f"{volume}({issue})"
    return _compact_western_periods(
        f"{_author_title_join(author_str, title)}[J].{venue},{year},{vol_issue}:{pages}."
    )


def _first_author(ref):
    authors = ref.get("authors", [])
    return authors[0] if authors else ""


def _is_chinese_ref(ref):
    return any("\u4e00" <= c <= "\u9fff" for c in _first_author(ref))


def _repair_western_authors(authors: list[str]) -> list[str]:
    if not authors or any("\u4e00" <= c <= "\u9fff" for c in authors[0]):
        return authors

    def initials_only(s: str) -> bool:
        return bool(re.match(r"^([A-Z](-[A-Z])?\.\s*)+$", s.strip()))

    merged: list[str] = []
    buf = authors[0]
    for part in authors[1:]:
        if initials_only(part):
            buf = f"{buf}, {part}"
        else:
            merged.append(buf)
            buf = part
    merged.append(buf)
    return merged


def load_references():
    if yaml is None:
        raise RuntimeError("PyYAML required: pip install pyyaml")
    data = yaml.safe_load(BIBLIOGRAPHY.read_text(encoding="utf-8"))
    refs = data.get("references", [])
    for ref in refs:
        ref["authors"] = _repair_western_authors(ref.get("authors", []))
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
    """Continuous [1]… list under section 4; no 中文文献/外文文献 sub-headings."""
    chinese, foreign = load_references()
    lines = []
    idx = 1
    for ref in chinese:
        lines.append(f"[{idx}]{format_gbt7714(ref)}")
        idx += 1
    for ref in foreign:
        lines.append(f"[{idx}]{format_gbt7714(ref)}")
        idx += 1
    return "\n".join(lines)


def build_section1():
    return _compact_spacing(SECTION1_BODY + "\n" + build_reference_block())
