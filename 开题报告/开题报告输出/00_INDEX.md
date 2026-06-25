# 开题报告输出 — 总索引

> **最后更新**：2026-06-24  
> **论文题目（锁定）**：多目标优化的半导体后端制造生产排程研究

---

## 真源层级（唯一、不冲突）

| 领域 | 唯一真源 | 说明 |
|------|----------|------|
| **写作策略** | [`process/WRITING_RULES.md`](process/WRITING_RULES.md) | 人称、括号、实验表述、禁写项；**可随时修改** |
| **正文内容** | [`process/section_content.py`](process/section_content.py) | R11/R13/R15 prose |
| **格式排版** | [`process/FORMAT_SPEC.md`](process/FORMAT_SPEC.md) | 表格行、GB/T 7714、字体 |
| **表头信息** | [`2120253828-…开题报告.doc`](../2120253828-喻炫琪-研究生开题报告.doc) | [`METADATA_POLICY.md`](process/METADATA_POLICY.md) |
| **参考文献** | [`process/BIBLIOGRAPHY.yaml`](process/BIBLIOGRAPHY.yaml) | 32 篇 |
| **题目** | [`process/TITLE_LOCK.md`](process/TITLE_LOCK.md) | — |
| **脱敏** | [`process/ANONYMIZATION.md`](process/ANONYMIZATION.md) | — |
| **事实数字** | [`process/CLAIMS.md`](process/CLAIMS.md) | 内部 EXP 仅作内部真源列 |
| **术语** | [`process/TERMINOLOGY.md`](process/TERMINOLOGY.md) | — |
| **学院提交** | [`02_开题报告_提交版.doc`](02_开题报告_提交版.doc) | 手调版式后以 02 为准 |

规则变更 → [`process/WRITING_LOG.md`](process/WRITING_LOG.md)。

---

## 文档地图

| 文件 | 用途 |
|------|------|
| **`02_开题报告_提交版.doc`** | 学院提交 Word（脚本只 bulk 写 R11/R13/R15 文字） |
| [01_开题报告正文.md](01_开题报告正文.md) | 结构索引 |
| [process/WRITING_RULES.md](process/WRITING_RULES.md) | **写作策略真源** |
| [process/FORMAT_SPEC.md](process/FORMAT_SPEC.md) | 格式与著录真源 |
| [process/METADATA_POLICY.md](process/METADATA_POLICY.md) | 表头与 doc 工作流 |
| [process/section_content.py](process/section_content.py) | 正文内容真源 |
| [process/fill_template.py](process/fill_template.py) | 填表脚本 |
| [process/ensure_doc_closed.py](process/ensure_doc_closed.py) | 写 doc 前检查 |
| [process/audit_spacing.py](process/audit_spacing.py) | **空行审计**（`--word` 检查 02） |
| [process/audit_proposal.py](process/audit_proposal.py) | **综合审计**（空行+时态+术语） |
| [process/TERMINOLOGY.md](process/TERMINOLOGY.md) | **术语精校真源** |
| [process/OUTLINE.md](process/OUTLINE.md) | 章节大纲 |
| [process/BIBLIOGRAPHY.yaml](process/BIBLIOGRAPHY.yaml) | 文献元数据 |
| [process/CLAIMS.md](process/CLAIMS.md) | 事实断言登记 |
| [process/ANONYMIZATION.md](process/ANONYMIZATION.md) | 脱敏规范 |
| [`process/WRITING_LOG.md`](process/WRITING_LOG.md) | 修改日志 |
| [process/TITLE_LOCK.md](process/TITLE_LOCK.md) | 题目锁定 |

---

## 规模估计（2026-06-24）

| 项 | 数值 |
|----|------|
| 参考文献 | **32 篇** |
| 三节正文汉字合计 | **~7 310**（不含文献列表） |

---

## 项目交叉索引（内部，正文不引 EXP 编号）

| 路径 | 说明 |
|------|------|
| [../../05_Documentation/experiments/](../../05_Documentation/experiments/) | EXP 工作日志（内部） |
| [../../05_Documentation/process/DECISIONS.md](../../05_Documentation/process/DECISIONS.md) | 技术决策 ADR |
| [../../05_Documentation/thesis/THESIS_NOTES.md](../../05_Documentation/thesis/THESIS_NOTES.md) | 论文素材 |

---

## 重新生成提交版

```powershell
cd 开题报告\开题报告输出\process
python ensure_doc_closed.py
python fill_template.py
```

表头请在模板 doc 维护。详见 [`METADATA_POLICY.md`](process/METADATA_POLICY.md) 与 [`WRITING_RULES.md`](process/WRITING_RULES.md)。
