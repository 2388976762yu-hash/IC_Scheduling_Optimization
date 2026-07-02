# 学位文档工作区 — 总索引

> **最后更新**：2026-06-25  
> **论文题目（锁定）**：多目标优化的半导体后端制造生产排程研究

---

## 学院提交文件（`开题报告/` 根目录，仅 3 个 .doc）

| 文件 | 用途 |
|------|------|
| [`../../开题报告/2120253828-喻炫琪-研究生开题报告.doc`](../../开题报告/2120253828-喻炫琪-研究生开题报告.doc) | **开题报告**（脚本就地更新 R11/R13/R15） |
| [`../../开题报告/2120253828-喻炫琪-研究生中期报告.doc`](../../开题报告/2120253828-喻炫琪-研究生中期报告.doc) | **中期报告** |
| [`../../开题报告/2120253828-喻炫琪-研究生中期考核表.doc`](../../开题报告/2120253828-喻炫琪-研究生中期考核表.doc) | **中期考核表**（学生填摘要/题目/关键词；思想品德与课程学习由学院填） |

本目录存放 Markdown 真源、脚本与备份；**不要在 `开题报告/` 根目录放 MD**。

---

## 真源层级

| 领域 | 唯一真源 | 说明 |
|------|----------|------|
| **模型与数据** | [`process/MODEL_TRUTH.md`](process/MODEL_TRUTH.md) | 工序 Taping→BG→DS→DA→WB→MOLD |
| **PPT/Word 手改** | [`process/MANUAL_SYNC_PPT_WORD.md`](process/MANUAL_SYNC_PPT_WORD.md) | 改前/改后对照，不跑 fill 脚本 |
| **开题写作策略** | [`process/WRITING_RULES.md`](process/WRITING_RULES.md) | §1/§2 拟开展；§3 可写标定数值 |
| **开题正文** | [`process/section_content.py`](process/section_content.py) | R11/R13/R15 |
| **中期正文** | [`process/midterm_section_content.py`](process/midterm_section_content.py) | 中期报告 P58 + 考核表摘要 |
| **表头** | 各 `.doc` 封面表格 | 见 [`process/METADATA_POLICY.md`](process/METADATA_POLICY.md) |
| **参考文献** | [`process/BIBLIOGRAPHY.yaml`](process/BIBLIOGRAPHY.yaml) | 32 篇 |
| **审计** | [`process/audit_proposal.py`](process/audit_proposal.py) | 开题 D1–D8 |
| **开题备份** | [`02_开题报告_提交版.doc`](02_开题报告_提交版.doc) | 手调版式备份；`--from-template` 恢复用 |

**学院参考材料（空白模板、填写说明、细则 PDF）** → [`../../开题报告/参考资料/00_README.md`](../../开题报告/参考资料/00_README.md)（**勿移走**；脚本不写入该目录）

---

## 脚本命令

```powershell
cd 05_Documentation\thesis\学位文档工作区\process
python read_submission_docs.py --kaiti    # 只读提取开题 R11/R13/R15（同步后端前必跑）
python ensure_doc_closed.py

# 开题（只写文字，会同步备份 02）
python fill_template.py
python audit_proposal.py --word

# 中期（只写文字，不改格式）
python fill_midterm.py
```

---

## 文档地图

| 路径 | 用途 |
|------|------|
| [01_开题报告正文.md](01_开题报告正文.md) | 开题结构索引 |
| [process/](process/) | 全部脚本与规则 |
| [参考资料/](参考资料/) | 学院填写注意事项 PDF/docx |

项目交叉索引 → [THESIS_NOTES.md](../THESIS_NOTES.md)、[experiments/](../../experiments/)
