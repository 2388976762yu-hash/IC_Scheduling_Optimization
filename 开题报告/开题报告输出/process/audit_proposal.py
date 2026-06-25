# -*- coding: utf-8 -*-
"""Run all proposal audits: spacing, framing, terminology."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
SCRIPTS = ("audit_spacing.py", "audit_proposal_framing.py", "audit_terminology.py")


def main() -> int:
    failed = 0
    for script in SCRIPTS:
        print(f"=== {script} ===")
        rc = subprocess.call([sys.executable, str(PROCESS / script)])
        print()
        if rc:
            failed += 1
    if failed:
        print(f"FAIL: {failed}/{len(SCRIPTS)} audit(s) failed.")
        return 1
    print("OK: all proposal audits passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
