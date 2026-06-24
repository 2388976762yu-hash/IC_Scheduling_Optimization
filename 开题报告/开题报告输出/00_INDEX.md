# 开题报告输出 — 总索引

> **最后更新**：2026-06-24  
> **论文题目（锁定）**：多目标优化的半导体后端制造生产排程研究

---

## 文档地图

| 文件 | 用途 | 真源角色 |
|------|------|----------|
| **`02_开题报告_提交版.doc`** | **学院模板填表版（主提交）** | 自原版 template 复制填表 |
| `02_开题报告_提交版.docx` | Word 2007+ 格式副本 | 由脚本导出 |
| [01_开题报告正文.md](01_开题报告正文.md) | 结构说明与版本对照 | 指向表格内容 |
| [process/FORMAT_SPEC.md](process/FORMAT_SPEC.md) | 标点、引用、GB/T 7714 规范 | 格式真源 |
| [process/section_content.py](process/section_content.py) | SECTION1/2/3 正文 prose | **内容真源** |
| [process/fill_template.py](process/fill_template.py) | 填表脚本 + 参考文献生成 | 生成 .doc/.docx |
| [process/OUTLINE.md](process/OUTLINE.md) | 章节大纲与页数预算 | 结构真源 |
| [process/BIBLIOGRAPHY.yaml](process/BIBLIOGRAPHY.yaml) | 文献元数据 | **参考文献唯一真源**（32 篇） |
| [process/REFERENCE_VERIFICATION.md](process/REFERENCE_VERIFICATION.md) | 逐条 Scholar/DOI 核实 | 核实记录 |
| [process/CLAIMS.md](process/CLAIMS.md) | 事实断言 ↔ 内部真源 ↔ 脱敏表述 | 校验真源 |
| [process/ANONYMIZATION.md](process/ANONYMIZATION.md) | 脱敏规则与扫描记录 | 合规真源 |
| [process/WRITING_LOG.md](process/WRITING_LOG.md) | 撰写/修改日志 | 过程记录 |
| [process/LITERATURE_REVIEW_NOTES.md](process/LITERATURE_REVIEW_NOTES.md) | 综述分条笔记 | 写作素材 |
| [process/TITLE_LOCK.md](process/TITLE_LOCK.md) | 题目锁定记录 | 决策记录 |

---

## 规模估计（2026-06-24 修订版）

| 项 | 数值 |
|----|------|
| 参考文献 | **32 篇**（含文件夹 3 篇唯一 PDF） |
| 第一节正文中文字 | **~5 160**（不含文献列表） |
| 三节正文汉字合计 | **~7 310**（不含文献列表） |
| 含 GB/T 7714 列表总字符 | **~19 000**（约 15—18 页打印量） |

---

## 只读参考（不修改）

| 路径 | 说明 |
|------|------|
| [../2120253828-喻炫琪-研究生开题报告.doc](../2120253828-喻炫琪-研究生开题报告.doc) | 学院 Word 模板 |
| [../商学院学术学位硕士研究生开题报告及中期考核实施细则（2025-10-22）.pdf](../商学院学术学位硕士研究生开题报告及中期考核实施细则（2025-10-22）.pdf) | 实施细则 |

---

## 项目真源（数字与决策，正文经 CLAIMS 脱敏后引用）

| 路径 | 说明 |
|------|------|
| [../../05_Documentation/process/DECISIONS.md](../../05_Documentation/process/DECISIONS.md) | 目标函数、因子定义等 ADR |
| [../../05_Documentation/experiments/records/](../../05_Documentation/experiments/records/) | EXP-001～003 实验数字 |
| [../../05_Documentation/thesis/THESIS_NOTES.md](../../05_Documentation/thesis/THESIS_NOTES.md) | 论文素材索引 |
| [../../02_Simulation_Model/modeldetail/AUTO_Model2.0_Architecture_Document.md](../../02_Simulation_Model/modeldetail/AUTO_Model2.0_Architecture_Document.md) | 模型架构 |
| [../../项目辅助材料/参考文献/](../../项目辅助材料/参考文献/) | 5 PDF（3 篇唯一文献） |

---

## 双向索引

- 本目录 ← [`05_Documentation/thesis/THESIS_NOTES.md`](../../05_Documentation/thesis/THESIS_NOTES.md) §开题报告
- 实验数字 ← [`05_Documentation/experiments/EXPERIMENT_LOG.md`](../../05_Documentation/experiments/EXPERIMENT_LOG.md)

---

## 脱敏原则（摘要）

开题报告正文及 Word **不得出现**企业名、品牌名、可识别合作方信息。详见 [process/ANONYMIZATION.md](process/ANONYMIZATION.md)。

---

## 重新生成提交版

```bash
cd 开题报告/开题报告输出/process
python fill_template.py
```
