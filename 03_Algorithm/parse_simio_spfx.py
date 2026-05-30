"""Parse Simio .spfx archive inventory and companion simulation artifacts."""
from __future__ import annotations

import csv
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPFX = ROOT / "02_Simulation_Model" / "AUTO_Model2.0.spfx"
OUT_JSON = ROOT / "02_Simulation_Model" / "modeldetail" / "AUTO_Model2.0_parsed.json"
OUT_MD = ROOT / "02_Simulation_Model" / "modeldetail" / "AUTO_Model2.0_parsed_summary.md"

# Known top-level model object types from archive layout
MODEL_TYPES = [
    "Source",
    "Separator",
    "Server",
    "DS_Server",
    "DA_Server",
    "WB_Server",
    "Mold_Server",
    "BG_Server",
    "Taping_Server",
    "Combiner",
    "Sink",
    "Worker",
    "MyWorker",
    "Path",
    "MovePath",
    "AllocatePath",
    "BasicNode",
    "TransferNode",
    "OrderEntity",
    "Model",
]


def classify_xml_payload(data: bytes) -> str:
    head = data[:120]
    if head.startswith(b"<?xml") or head.startswith(b"<"):
        return "plaintext_xml"
    if head.startswith(b"\xb2o_/prF"):
        return "simio_encoded"
    return "binary_or_unknown"


def inventory_spfx(path: Path) -> dict:
    inv: dict = {
        "file": str(path.name),
        "size_bytes": path.stat().st_size,
        "parsed_at": datetime.now().isoformat(timespec="seconds"),
        "entry_count": 0,
        "by_extension": Counter(),
        "by_top_folder": Counter(),
        "model_definitions": defaultdict(list),
        "process_logic_files": [],
        "encoded_xml_count": 0,
        "plaintext_xml_count": 0,
        "geometry_files": [],
        "experiments": [],
        "notes": [],
    }

    with zipfile.ZipFile(path) as z:
        inv["entry_count"] = len(z.namelist())
        for name in z.namelist():
            ext = Path(name).suffix.lower() or "(no ext)"
            inv["by_extension"][ext] += 1
            top = name.split("/")[0] if "/" in name else name
            inv["by_top_folder"][top] += 1

            if name.endswith(".xml"):
                kind = classify_xml_payload(z.read(name))
                if kind == "simio_encoded":
                    inv["encoded_xml_count"] += 1
                elif kind == "plaintext_xml":
                    inv["plaintext_xml_count"] += 1

            parts = name.split("/")
            if len(parts) >= 2 and parts[0] == "Models":
                mtype = parts[1]
                if mtype in MODEL_TYPES and len(parts) == 3 and parts[2].endswith(".xml"):
                    inv["model_definitions"][mtype].append(parts[2])
                if len(parts) >= 4 and parts[2] == "Processes":
                    inv["process_logic_files"].append(name)

            if ext in {".s3d", ".png"}:
                inv["geometry_files"].append(name)
            if "Experiment" in name:
                inv["experiments"].append(name)

    inv["by_extension"] = dict(inv["by_extension"])
    inv["by_top_folder"] = dict(inv["by_top_folder"])
    inv["model_definitions"] = {
        k: sorted(v) for k, sorted_keys in sorted(inv["model_definitions"].items())
        for v in [sorted_keys]
    }
    inv["process_logic_count"] = len(inv["process_logic_files"])
    inv["notes"].append(
        "Simio .spfx 内部 Models/*.xml 与 Project.xml 为 Simio 专有编码，"
        "不能当作普通 XML 直接解析；结构理解需结合 Architecture 文档、截图与运行报告。"
    )
    return inv


def parse_results_report(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = list(csv.reader(text.splitlines()))

    out: dict = {
        "file": path.name,
        "project": None,
        "run_date": None,
        "created": {},
        "destroyed": {},
        "source_throughput": None,
        "sink_throughput": None,
    }

    for row in lines[:5]:
        joined = ",".join(row)
        if "Project:" in joined:
            out["project"] = joined.split("Project:")[-1].split(",")[0].strip()
        if "Run Date:" in joined:
            out["run_date"] = joined.split("Run Date:")[-1].strip(" ,")

    section = None
    for row in lines:
        if not row:
            continue
        label = row[0].strip() if row[0] else ""
        if label == "NumberCreated - Total":
            section = "created"
            continue
        if label == "NumberDestroyed - Total":
            section = "destroyed"
            continue
        if section and len(row) >= 5 and row[0] and row[4]:
            key = row[0].strip()
            val = row[4].strip()
            if key in {"Order", "M_LOT", "SUB_LOT", "MAG"}:
                out[section][key] = val
        if label.startswith("Source_Orders") and len(row) >= 5 and row[2] == "Throughput":
            out["source_throughput"] = row[4]
        if label.startswith("Sink_Finished") and len(row) >= 5 and row[2] == "Throughput":
            out["sink_throughput"] = row[4]

    return out


def load_v1v2_analysis(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def render_markdown(inv: dict, reports: dict, analysis: dict) -> str:
    lines = [
        "# AUTO_Model2.0 解压解析摘要",
        "",
        f"- 源文件: `{inv['file']}`",
        f"- 文件大小: {inv['size_bytes']:,} bytes",
        f"- 压缩包条目: {inv['entry_count']}",
        f"- 解析时间: {inv['parsed_at']}",
        "",
        "## 1. 压缩包结构",
        "",
        "| 顶层目录 | 文件数 |",
        "|---------|--------|",
    ]
    for folder, count in sorted(inv["by_top_folder"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| `{folder}` | {count} |")

    lines.extend(
        [
            "",
            "## 2. XML 可读性说明",
            "",
            f"- Simio 编码 XML: **{inv['encoded_xml_count']}** 个",
            f"- 明文 XML: **{inv['plaintext_xml_count']}** 个",
            f"- Process 逻辑文件: **{inv['process_logic_count']}** 个",
            "",
            "> " + inv["notes"][0],
            "",
            "## 3. 模型定义类型（来自压缩包目录结构）",
            "",
            "| 类型 | 定义文件数 | 说明 |",
            "|------|-----------|------|",
        ]
    )

    type_desc = {
        "Source": "订单释放",
        "Separator": "批次拆分（通用模板）",
        "DS_Server": "D/S 切割工序",
        "DA_Server": "DA 粘片工序",
        "WB_Server": "WB 焊线工序",
        "Mold_Server": "Mold 塑封工序",
        "BG_Server": "B/G 键合研磨工序",
        "Taping_Server": "Taping 贴带工序",
        "Combiner": "SubLot 合并",
        "Sink": "完成汇点",
        "Worker": "搬运 Worker 模板",
        "MyWorker": "自定义 Worker",
        "OrderEntity": "订单实体定义",
        "Model": "顶层 Model 容器",
        "Path": "路径",
        "MovePath": "搬运路径",
        "AllocatePath": "分配路径",
        "BasicNode": "节点",
        "TransferNode": "转移节点",
    }
    for t in MODEL_TYPES:
        files = inv["model_definitions"].get(t, [])
        if files:
            lines.append(f"| `{t}` | {len(files)} | {type_desc.get(t, '')} |")

    lines.extend(["", "## 4. 关键 Process 逻辑文件（部分）", ""])
    interesting = [
        p
        for p in inv["process_logic_files"]
        if any(
            k in p
            for k in [
                "changover",
                "Processing",
                "OnEntered",
                "OnExited",
                "Arrival",
                "Setup",
                "Transfer",
                "Failed",
            ]
        )
    ]
    for p in sorted(interesting)[:40]:
        lines.append(f"- `{p}`")
    if len(interesting) > 40:
        lines.append(f"- ... 另有 {len(interesting) - 40} 个")

    if inv["experiments"]:
        lines.extend(["", "## 5. Experiment 相关文件", ""])
        for e in inv["experiments"]:
            lines.append(f"- `{e}`")

    if reports:
        lines.extend(["", "## 6. 最新运行报告摘要", ""])
        for name, rep in reports.items():
            lines.append(f"### `{name}`")
            lines.append(f"- Project: {rep.get('project')}")
            lines.append(f"- Run Date: {rep.get('run_date')}")
            if rep.get("created"):
                lines.append(f"- Created: {rep['created']}")
            if rep.get("destroyed"):
                lines.append(f"- Destroyed: {rep['destroyed']}")
            lines.append(
                f"- Source throughput: {rep.get('source_throughput')} | "
                f"Sink throughput: {rep.get('sink_throughput')}"
            )
            lines.append("")

    if analysis:
        lines.extend(["", "## 7. V1/V2 利用率摘要（来自 v1v2_analysis.json）", ""])
        for scenario, data in analysis.items():
            util = data.get("utilization", {})
            if not util:
                continue
            lines.append(f"### {scenario}")
            for station in ["DS", "DA", "WB", "MOLD", "BG", "Taping"]:
                if station in util:
                    u = util[station]
                    lines.append(
                        f"- {station}: avg {u['avg']:.2f}%, max {u['max']:.2f}%, count {u['count']}"
                    )
            comp = data.get("completion", {}).get("Order", {})
            if comp:
                lines.append(
                    f"- Order completion: {comp.get('destroyed')}/{comp.get('created')} "
                    f"({comp.get('rate')}%)"
                )
            lines.append("")

    return "\n".join(lines)


def main() -> int:
    if not SPFX.exists():
        print(f"Missing: {SPFX}", file=sys.stderr)
        return 1

    inv = inventory_spfx(SPFX)
    reports = {
        "V2-ResultsViewSampleReport.csv": parse_results_report(
            ROOT / "04_Output" / "V2-ResultsViewSampleReport.csv"
        ),
        "V1_ResultsViewSampleReport.csv": parse_results_report(
            ROOT / "04_Output" / "V1_ResultsViewSampleReport.csv"
        ),
    }
    analysis = load_v1v2_analysis(ROOT / "04_Output" / "v1v2_analysis.json")

    payload = {"inventory": inv, "reports": reports, "v1v2_analysis_keys": list(analysis.keys())}
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(inv, reports, analysis), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
