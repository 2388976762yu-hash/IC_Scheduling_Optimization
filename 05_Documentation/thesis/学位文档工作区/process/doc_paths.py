# -*- coding: utf-8 -*-
"""Shared paths for thesis Word docs (robust after workspace moves)."""
from __future__ import annotations

from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    start = start or Path(__file__).resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "开题报告").is_dir() and (candidate / "05_Documentation").is_dir():
            return candidate
    raise RuntimeError("Cannot locate repo root (开题报告 + 05_Documentation).")


REPO_ROOT = find_repo_root()
WORKSPACE = Path(__file__).resolve().parent.parent
PROCESS = Path(__file__).resolve().parent
KAITI_DIR = REPO_ROOT / "开题报告"
REFERENCE_DIR = KAITI_DIR / "参考资料"
BLANK_TEMPLATE_DIR = REFERENCE_DIR / "学院原版空白模板"

KAITI_DOC = KAITI_DIR / "2120253828-喻炫琪-研究生开题报告.doc"
MIDTERM_REPORT_DOC = KAITI_DIR / "2120253828-喻炫琪-研究生中期报告.doc"
MIDTERM_FORM_DOC = KAITI_DIR / "2120253828-喻炫琪-研究生中期考核表.doc"
KAITI_BLANK_TEMPLATE = BLANK_TEMPLATE_DIR / "2120253828-喻炫琪-研究生开题报告_学院空白模板.doc"
MIDTERM_FORM_BLANK = BLANK_TEMPLATE_DIR / "2120253828-喻炫琪-研究生中期考核表_学院空白模板.doc"
MIDTERM_REPORT_BLANK = BLANK_TEMPLATE_DIR / "2120253828-喻炫琪-研究生中期报告_学院空白模板.doc"
KAITI_BACKUP_DOC = WORKSPACE / "02_开题报告_提交版.doc"

MANAGED_DOCS = (
    KAITI_DOC,
    KAITI_BACKUP_DOC,
    MIDTERM_REPORT_DOC,
    MIDTERM_FORM_DOC,
)

DOC_TITLE_KEYWORDS = (
    "开题报告",
    "中期报告",
    "中期考核",
    "02_开题报告_提交版",
)
