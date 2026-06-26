# -*- coding: utf-8 -*-
"""D6: Cross-section wording consistency."""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

ALL = SECTION1_BODY + SECTION2 + SECTION3

OBJECTIVE = "0.7×MakeSpan + 0.3×Penalty"
DATA_PHRASE = "企业脱敏 Simio 导入数据"


def main() -> int:
    issues: list[str] = []

    if "行业脱敏订单" in ALL or "行业脱敏 SPAN" in ALL:
        issues.append("数据来源应统一为「企业脱敏 Simio 导入数据」")

    if re.search(r"(?<![\u4e00-\u9fff])SPAN(?![\s]*基准)", ALL):
        if "SPAN" in ALL.replace("企业脱敏 Simio 导入数据", ""):
            issues.append("避免单独使用 SPAN 代号")

    if "杂志批次" in ALL:
        issues.append("Magazine 应为「弹夹批次Magazine」")

    if ALL.count(OBJECTIVE.replace(" ", "")) < 2 and "0.7×MakeSpan+0.3×Penalty" not in ALL:
        issues.append("Objective 公式表述应前后一致")

    if "459 台" not in ALL and "459台" not in ALL:
        issues.append("设备规模 459 台应在正文中出现")

    if "41 条订单" not in ALL and "41条订单" not in ALL and "41 张订单" not in ALL:
        issues.append("订单规模 41 条应在正文中出现")

    # §3 must mention staged experiment disclaimer
    if "标定" not in SECTION3 and "阶段性" not in SECTION3:
        issues.append("SECTION3 应标明阶段性/标定实验")

    if issues:
        print("FAIL: consistency audit")
        for item in issues:
            print(f"  - {item}")
        return 1

    print("OK: consistency audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
