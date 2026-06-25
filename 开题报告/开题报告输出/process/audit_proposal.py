# -*- coding: utf-8 -*-
"""Run all proposal quality audits (multi-dimensional gate)."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent

SCRIPTS = (
    "audit_spacing.py",
    "audit_proposal_framing.py",
    "audit_terminology.py",
    "audit_academic.py",
    "audit_anonymization.py",
    "audit_consistency.py",
    "audit_citations.py",
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run all proposal audits. See AUDIT_DIMENSIONS.md."
    )
    parser.add_argument(
        "--word",
        action="store_true",
        help="Also run audit_spacing.py --word on 02 doc",
    )
    args = parser.parse_args()

    failed = 0
    for script in SCRIPTS:
        print(f"=== {script} ===")
        cmd = [sys.executable, str(PROCESS / script)]
        if script == "audit_spacing.py" and args.word:
            cmd.append("--word")
        rc = subprocess.call(cmd)
        print()
        if rc:
            failed += 1

    if failed:
        print(f"FAIL: {failed}/{len(SCRIPTS)} audit(s) failed.")
        print("See AUDIT_DIMENSIONS.md for dimension definitions.")
        return 1

    print("OK: all proposal audits passed (D1–D7).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
