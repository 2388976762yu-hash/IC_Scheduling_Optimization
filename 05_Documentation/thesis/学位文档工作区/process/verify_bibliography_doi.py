# -*- coding: utf-8 -*-
"""Cross-check BIBLIOGRAPHY.yaml entries against Crossref (DOI) or note gaps."""
from __future__ import annotations

import json
import urllib.request
from pathlib import Path

import yaml

BIB = Path(__file__).resolve().parent / "BIBLIOGRAPHY.yaml"


def fetch_crossref(doi: str) -> dict | None:
    url = f"https://api.crossref.org/works/{doi}"
    req = urllib.request.Request(url, headers={"User-Agent": "thesis-bib-verify/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode())["message"]
    except Exception as exc:
        return {"error": str(exc)}


def main() -> None:
    data = yaml.safe_load(BIB.read_text(encoding="utf-8"))
    lines = []
    for ref in data["references"]:
        rid = ref["id"]
        doi = ref.get("doi")
        if not doi:
            lines.append(f"{rid}: NO DOI (manual verify required)")
            continue
        msg = fetch_crossref(doi)
        if "error" in msg:
            lines.append(f"{rid}: FAIL {doi} -> {msg['error']}")
            continue
        title = (msg.get("title") or [""])[0][:60]
        year = None
        for key in ("published-print", "published-online", "issued"):
            parts = (msg.get(key) or {}).get("date-parts") or []
            if parts and parts[0]:
                year = parts[0][0]
                break
        pages = msg.get("page") or ""
        container = (msg.get("container-title") or [""])[0][:40]
        lines.append(
            f"{rid}: OK doi={doi} crossref_year={year} pages={pages} venue={container} title={title}..."
        )
    out = Path(__file__).resolve().parent / "verify_bibliography_report.txt"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
