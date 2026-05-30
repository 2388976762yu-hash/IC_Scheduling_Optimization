#!/usr/bin/env python3
"""Build human-readable inventory from AUTO_Model2.0.spfx without Simio IDE."""
from __future__ import annotations

import json
import sqlite3
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path


def main() -> None:
    spfx = Path("02_Simulation_Model/AUTO_Model2.0.spfx")
    out_md = Path("02_Simulation_Model/modeldetail/AUTO_Model2.0_spfx_inventory.md")
    out_json = Path("02_Simulation_Model/modeldetail/AUTO_Model2.0_spfx_inventory.json")

    with zipfile.ZipFile(spfx) as zf:
        names = zf.namelist()

        # Group by top-level category
        by_cat: dict[str, list[str]] = defaultdict(list)
        for n in names:
            cat = n.split("/")[0] if "/" in n else n
            by_cat[cat].append(n)

        # Model definition folders (one folder per Simio object type/instance)
        model_folders = sorted(
            {
                parts[1]
                for n in names
                if n.startswith("Models/") and len(parts := n.split("/")) >= 2
            }
        )

        # Process logic files per server/object
        processes: dict[str, list[str]] = defaultdict(list)
        for n in names:
            if "/Processes/" in n and n.endswith(".xml"):
                owner = n.split("/")[1]
                proc_name = Path(n).stem
                processes[owner].append(proc_name)

        # ViewInfos -> instantiated objects in main model
        view_infos = [n for n in names if n.startswith("ViewInfos/") and n.endswith(".xml")]

        # Embedded results
        results_files = [n for n in names if n.startswith("Results/")]

        # SQLite table snapshot
        sqlite_summary: dict = {}
        sqlite_path = "Results/Model/TableStates.sqlite"
        if sqlite_path in names:
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".sqlite")
            tmp.write(zf.read(sqlite_path))
            tmp.close()
            conn = sqlite3.connect(tmp.name)
            cur = conn.cursor()
            tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'")]
            sqlite_summary["tables"] = tables
            for t in tables:
                try:
                    count = cur.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
                    cols = [c[1] for c in cur.execute(f"PRAGMA table_info([{t}])")]
                    sample = cur.execute(f"SELECT * FROM [{t}] LIMIT 3").fetchall()
                    sqlite_summary[t] = {"row_count": count, "columns": cols, "sample": sample}
                except sqlite3.Error as e:
                    sqlite_summary[t] = {"error": str(e)}
            conn.close()
            Path(tmp.name).unlink(missing_ok=True)

        inventory = {
            "source": str(spfx),
            "size_bytes": spfx.stat().st_size,
            "total_entries": len(names),
            "categories": {k: len(v) for k, v in sorted(by_cat.items())},
            "model_folders": model_folders,
            "process_logic_by_object": dict(sorted(processes.items())),
            "view_info_files": [Path(v).name for v in view_infos],
            "embedded_results": results_files,
            "sqlite_summary": sqlite_summary,
            "compression_note": (
                "All Models/*.xml and Project.xml use Simio proprietary compression "
                "(magic bytes b2o_/prF). Plain XML parsing requires Simio export or IDE."
            ),
        }

        out_json.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")

        lines = [
            "# AUTO_Model2.0.spfx 解压清单",
            "",
            f"- 源文件: `{spfx}`",
            f"- 大小: {inventory['size_bytes']:,} bytes",
            f"- ZIP 内条目: {inventory['total_entries']}",
            "",
            "## 压缩说明",
            "",
            inventory["compression_note"],
            "",
            "仍可稳定读取的内容:",
            "- ZIP 目录结构（对象类型、Process 逻辑文件名）",
            "- `Results/Model/TableStates.sqlite`（上次运行残留的状态表）",
            "- `04_Output/*.csv` 导出的 Results 报告",
            "- `modeldetail/` 截图与架构文档",
            "",
            "## ZIP 顶层分类",
            "",
            "| 分类 | 文件数 |",
            "|------|--------|",
        ]
        for k, v in sorted(inventory["categories"].items()):
            lines.append(f"| {k} | {v} |")

        lines += [
            "",
            "## 模型对象类型（Models/ 下文件夹）",
            "",
        ]
        for f in model_folders:
            procs = processes.get(f, [])
            proc_str = f" — Processes: {', '.join(sorted(procs))}" if procs else ""
            lines.append(f"- **{f}**{proc_str}")

        lines += ["", "## ViewInfos（主模型实例视图）", ""]
        for v in sorted(inventory["view_info_files"]):
            lines.append(f"- `{v}`")

        if sqlite_summary.get("tables"):
            lines += ["", "## 内嵌 SQLite（TableStates）", ""]
            for t in sqlite_summary["tables"]:
                info = sqlite_summary.get(t, {})
                if isinstance(info, dict) and "row_count" in info:
                    lines.append(f"- **{t}**: {info['row_count']} rows, columns: `{', '.join(info['columns'])}`")

        lines += ["", "## 内嵌 Results 文件", ""]
        for r in results_files:
            lines.append(f"- `{r}`")

        out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote {out_json}")
        print(f"Wrote {out_md}")


if __name__ == "__main__":
    main()
