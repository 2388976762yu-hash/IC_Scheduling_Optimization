# -*- coding: utf-8 -*-
"""Cross-check doc truth sources for internal consistency (D8)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT.parent
DOCS = OUTPUT / "00_INDEX.md"
RULES = ROOT / "WRITING_RULES.md"
THESIS = ROOT.parents[2] / "05_Documentation" / "thesis" / "THESIS_NOTES.md"
BODY = ROOT / "section_content.py"
ANON = ROOT / "ANONYMIZATION.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    issues: list[str] = []
    index = read(DOCS)
    rules = read(RULES)
    body = read(BODY)

    required_truth_keys = (
        "WRITING_RULES.md",
        "section_content.py",
        "BIBLIOGRAPHY.yaml",
        "TERMINOLOGY.md",
        "AUDIT_DIMENSIONS.md",
        "audit_proposal.py",
    )
    for key in required_truth_keys:
        if key not in index:
            issues.append(f"00_INDEX 真源表缺少 {key}")
        if key not in rules and key not in ("audit_proposal.py",):
            if key == "AUDIT_DIMENSIONS.md" and "AUDIT_DIMENSIONS" not in rules:
                issues.append(f"WRITING_RULES 真源表缺少 {key}")

    if "32 篇" not in index or "32 篇" not in rules:
        issues.append("文献数量应统一为 32 篇（00_INDEX / WRITING_RULES）")

    if THESIS.exists():
        thesis = read(THESIS)
        if "28 篇" in thesis:
            issues.append("THESIS_NOTES 仍写 28 篇，应为 32 篇")
        if "行业脱敏订单" in thesis and "企业脱敏 Simio" not in thesis:
            issues.append("THESIS_NOTES 数据来源用语与正文不一致")

    if "行业脱敏订单" in body or re.search(r"行业脱敏(?!\s*Simio)", body):
        issues.append("section_content 应使用「企业脱敏 Simio 导入数据」")

    anon = read(ANON)
    if "导师科研项目" in anon and "正文禁用" not in anon:
        issues.append("ANONYMIZATION 须标明「导师…」仅内部可用、正文禁用")

    if issues:
        print("FAIL: doc truth audit (D8)")
        for item in issues:
            print(f"  - {item}")
        return 1

    print("OK: doc truth audit passed (D8).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
