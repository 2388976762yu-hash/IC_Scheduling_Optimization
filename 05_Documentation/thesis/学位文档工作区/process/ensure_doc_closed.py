# -*- coding: utf-8 -*-
"""开题报告 doc 工作前检查：确保 Word/WPS 未占用模板与提交版。

用法：
  python ensure_doc_closed.py           # 仅检查，占用则退出码 1
  python ensure_doc_closed.py --close   # 尝试结束占用进程后再检查
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

from doc_paths import (
    KAITI_BACKUP_DOC,
    KAITI_DOC,
    MIDTERM_FORM_DOC,
    MIDTERM_REPORT_DOC,
    MANAGED_DOCS,
    DOC_TITLE_KEYWORDS,
    WORKSPACE,
)


def probe_file_locked(path: Path) -> bool:
    """Return True when another process prevents exclusive open."""
    if not path.exists():
        return False
    try:
        fd = os.open(str(path), os.O_RDWR | os.O_APPEND)
        os.close(fd)
        return False
    except OSError:
        return True


def _run_tasklist(image: str) -> str:
    result = subprocess.run(
        ["tasklist", "/FI", f"IMAGENAME eq {image}", "/NH"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout or ""


def office_processes_running() -> dict[str, bool]:
    return {
        "WINWORD.EXE": "WINWORD.EXE" in _run_tasklist("WINWORD.EXE"),
        "wps.exe": "wps.exe" in _run_tasklist("wps.exe"),
    }


def wps_thesis_window_pids() -> list[int]:
    """Return PIDs of WPS instances whose main window title mentions 开题报告."""
    ps = (
        "Get-Process wps -ErrorAction SilentlyContinue | "
        "Where-Object { $_.MainWindowTitle -match '开题报告|中期报告|中期考核' } | "
        "ForEach-Object { $_.Id }"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps],
        capture_output=True,
        text=True,
        check=False,
    )
    return [int(x.strip()) for x in result.stdout.split() if x.strip().isdigit()]


def close_wps_for_thesis_docs() -> list[int]:
    """Stop WPS processes whose main window title mentions 开题报告."""
    pids = wps_thesis_window_pids()
    for pid in pids:
        subprocess.run(
            ["taskkill", "/F", "/PID", str(pid)],
            capture_output=True,
            check=False,
        )
    return pids


def close_winword() -> bool:
    listed = _run_tasklist("WINWORD.EXE")
    if "WINWORD.EXE" not in listed:
        return False
    subprocess.run(
        ["taskkill", "/F", "/IM", "WINWORD.EXE"],
        capture_output=True,
        check=False,
    )
    return True


def clear_readonly_flags() -> None:
    for path in MANAGED_DOCS:
        if not path.exists():
            continue
        try:
            os.chmod(path, os.stat(path).st_mode | os.W_OK)
        except OSError:
            pass
        subprocess.run(["attrib", "-R", str(path)], capture_output=True, check=False)


def collect_issues() -> list[str]:
    issues: list[str] = []
    if office_processes_running()["WINWORD.EXE"]:
        issues.append("Microsoft Word (WINWORD.EXE) 仍在运行")

    locked = [p for p in MANAGED_DOCS if probe_file_locked(p)]
    for path in locked:
        issues.append(f"文件被占用: {path.name}")

    wps_pids = wps_thesis_window_pids()
    if wps_pids:
        issues.append(
            f"WPS 仍打开开题报告窗口 (PID: {', '.join(map(str, wps_pids))})"
        )

    return issues


def ensure_documents_closed(*, auto_close: bool = False) -> None:
    """Raise RuntimeError if thesis docs are not free for automation."""
    if auto_close:
        closed_word = close_winword()
        closed_wps = close_wps_for_thesis_docs()
        if closed_word or closed_wps:
            time.sleep(1.5)
        clear_readonly_flags()

    issues = collect_issues()
    if issues:
        hint = (
            "请先保存并关闭 WPS/Word 中的开题报告文档，再运行脚本。\n"
            "或执行: python ensure_doc_closed.py --close\n"
            "或 PowerShell: .\\release_word_lock.ps1 -CloseWps"
        )
        raise RuntimeError("文档未处于可写入状态:\n  - " + "\n  - ".join(issues) + f"\n\n{hint}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Ensure thesis doc files are closed.")
    parser.add_argument(
        "--close",
        action="store_true",
        help="End WINWORD and WPS windows titled 开题报告, then re-check.",
    )
    args = parser.parse_args()
    try:
        ensure_documents_closed(auto_close=args.close)
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        return 1
    print("OK: 学位文档均未占用，可安全运行 fill_template.py / fill_midterm.py。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
