# -*- coding: utf-8 -*-
"""D4: Academic norms for master's thesis proposal body text."""
from __future__ import annotations

import re
import sys
from pathlib import Path

PROCESS = Path(__file__).resolve().parent
sys.path.insert(0, str(PROCESS))

from section_content import SECTION1_BODY, SECTION2, SECTION3  # noqa: E402

ALL_TEXT = "\n".join((SECTION1_BODY, SECTION2, SECTION3))

SECTION_REQUIRED = {
    "SECTION1_BODY": [
        "1.1 产业环境与问题提出",
        "1.2 业务特征与调度难点",
        "1.3 本研究数据来源与研究场景",
        "2. 研究意义",
        "3.1 半导体封装后端排程与派工规则",
        "3.6 本研究与现有研究的定位",
        "4. 主要参考文献",
    ],
    "SECTION2": [
        "1.1 研究目标",
        "1.2 研究内容",
        "1.3 拟解决的关键问题",
        "2.1 研究思路与技术路线",
        "2.4 可行性分析",
        "3. 研究的特色与创新点",
        "4. 研究工作计划",
        "5. 预期研究成果",
    ],
    "SECTION3": [
        "1. 与本项目有关的研究工作积累和已取得的研究工作成绩",
        "2.1 已具备条件",
        "2.2 尚缺条件与解决途径",
    ],
}


def main() -> int:
    issues: list[str] = []

    if "本课题" in ALL_TEXT:
        issues.append("全文禁止「本课题」，应统一为「本研究」")

    if re.search(r"\*\*.+\*\*", ALL_TEXT):
        issues.append("正文禁止 Markdown 加粗 **")

    if re.search(r"^#+\s", ALL_TEXT, re.M):
        issues.append("正文禁止 Markdown 标题 #")

    # Half-width parens immediately after author-year pattern
    for m in re.finditer(r"[\u4e00-\u9fffA-Za-z\-]+(?:等)?\([0-9]{4}", ALL_TEXT):
        line = ALL_TEXT[: m.start()].count("\n") + 1
        issues.append(f"L{line}: 引用括号应为全角（），非半角 ()")

    if "本研究" not in ALL_TEXT:
        issues.append("正文应使用「本研究」表述")

    for name, text in (
        ("SECTION1_BODY", SECTION1_BODY),
        ("SECTION2", SECTION2),
        ("SECTION3", SECTION3),
    ):
        for heading in SECTION_REQUIRED[name]:
            if heading not in text:
                issues.append(f"{name}: 缺少必要小节标题「{heading}」")

    if SECTION3 and "学位论文" not in SECTION3 and "正式结论" not in SECTION3:
        issues.append("SECTION3: 标定实验段应限定正式结论以学位论文为准")

    if issues:
        print("FAIL: academic audit")
        for item in issues:
            print(f"  - {item}")
        return 1

    print("OK: academic audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
