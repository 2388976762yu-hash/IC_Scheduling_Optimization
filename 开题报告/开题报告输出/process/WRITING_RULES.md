# 开题报告写作规则（活文档 · 策略真源）

> **最后更新**：2026-06-24  
> **地位**：开题正文「怎么写」的**唯一策略真源**。格式细则、表头维护、脱敏、题目等见下文索引，**不得与本文件冲突**；若冲突，以本文件 + 用户最新指示为准，并回写专项文件。

---

## 0. 规则维护（可随时修改）

- 本文件及 [`FORMAT_SPEC.md`](FORMAT_SPEC.md)、[`METADATA_POLICY.md`](METADATA_POLICY.md)、[`ANONYMIZATION.md`](ANONYMIZATION.md) 均为**活规则**，**可随时修改**，不必等 Word 定稿。
- **以仓库最新 markdown 为准**；[`02_开题报告_提交版.doc`](../02_开题报告_提交版.doc) 是输出物/提交物，不是规则真源。
- 每次改规则或正文策略 → [`WRITING_LOG.md`](WRITING_LOG.md) **追加一行**（日期、摘要、文件）。
- AI/协作者动笔前：读本文件 §1 真源表 + 下文；与用户口头要求冲突时，**以用户为准**并回写本文件。

---

## 1. 真源层级（唯一、不冲突）

| 领域 | 唯一真源 | 产出 / 下游 | 专项说明 |
|------|----------|-------------|----------|
| **写作策略** | **本文件** | `section_content.py` | — |
| **正文内容** | `section_content.py` | R11/R13/R15 | 不写表头字段 |
| **格式与排版** | `FORMAT_SPEC.md` | `fill_template.py` 字体行距 | 不重复策略条文 |
| **表头 / 封面** | `2120253828-…开题报告.doc` | 复制为 02 的表头 | [`METADATA_POLICY.md`](METADATA_POLICY.md) |
| **参考文献** | `BIBLIOGRAPHY.yaml` | R11 末尾列表 | GB/T 7714，见 FORMAT_SPEC |
| **题目** | `TITLE_LOCK.md` | 模板 R3 | 个人信息不在此维护 |
| **脱敏** | `ANONYMIZATION.md` | 正文用语 | 配合 CLAIMS 映射 |
| **事实数字** | `CLAIMS.md` | 写入正文的表述 | 内部 EXP/DECISIONS 仅作内部真源列 |
| **章节结构** | `OUTLINE.md` | 大纲与篇幅 | 非逐字正文 |
| **提交文件** | `02_开题报告_提交版.doc` | 学院提交 | 手调版式后以 02 为准；bulk 改字走脚本 |

**禁止**：在多个 md 中重复维护同一规则的不同版本；禁止脚本硬编码表头个人信息。

**工作流真源**：写回 Word 的步骤以 [`METADATA_POLICY.md`](METADATA_POLICY.md) §工作前检查 为准（`ensure_doc_closed.py` → `fill_template.py`）。

---

## 2. 人称、术语与禁写项

- 全文 **「本研究」**，不用「本课题」。
- 正文**不得出现**：`EXP-xxx`、`D-xxx`、脚本/内部文件名（`CLAIMS.md`、`fill_template.py` 等）、未在当节定义的实验代号。
- 英文缩写：首次可直写缩写或简短中文释义，**避免反复括号注释**；后文直接用 DES、EDD、UPH、MakeSpan 等。
- 学院模板表格内：不用 Markdown 符号（`#`、`**`）。

---

## 3. 标点与括号

- 中文叙述用**全角标点**：，。；：（）“”。
- **少用括号堆砌**；补充说明并入句子。
- **可保留括号**：著者-出版年 `Law（2015）`；参考文献类型 [J]/[M]（仅文献列表）。
- **避免**：句内 `（A，2008；B，2015）` 连写 → 改为分句；`（1）（2）（3）` 列举 → **「第一，……；第二，……」** 或分号并列；`（如……）` 旁注 → 写入正文。
- 设备台数、实验数值用顿号/逗号嵌入句中，不用括号包裹。

引用格式示例见 [`FORMAT_SPEC.md`](FORMAT_SPEC.md) §正文引用。

---

## 4. 实验与初步工作（开题正文）

| 场景 | 写法 |
|------|------|
| 已完成 | 可读中文名称 + **首次出现**说明内容 |
| 计划中 | 第二节「实验方案」：「第一步…」「拟开展…对照实验」 |
| 研究意义/综述 | 不得突然抛出未定义代号 + 数值；举例须承接前文已命名实验 |

**标准中文名称**（与 [`CLAIMS.md`](CLAIMS.md) 脱敏表述列一致）：

| 内部真源 | 正文用语 |
|----------|----------|
| EXP-001 | 因子均为 1.0 的**基准情景** |
| EXP-002 | **26 情景批次因子全因子网格扫描** |
| EXP-003 | **仅调整订单表释放顺序的对照** |
| 拟开展 | **交期升序释放与 FIFO 的对照实验** |

内部编号只保留在 `05_Documentation/experiments/` 及 CLAIMS「内部真源」列。

---

## 5. 参考文献（正文侧规则）

- 列表真源：`BIBLIOGRAPHY.yaml`（32 篇）。
- 结构：**中文文献** + **外文文献** 分列；各自按第一作者字母序；编号全文连续 `[1]` 起。
- 著录格式：GB/T 7714—2015。生成：`fill_template.py`。**手改 02 文献后慎重跑脚本**。

细则见 [`FORMAT_SPEC.md`](FORMAT_SPEC.md) §参考文献列表。

---

## 6. 脱敏（摘要）

正文与 02 **不得出现**企业名、品牌名、可识别合作方、含内部代号的数据文件名。替代表述见 [`ANONYMIZATION.md`](ANONYMIZATION.md)；数字与事实经 [`CLAIMS.md`](CLAIMS.md) 登记后再写入 `section_content.py`。

---

## 7. 段落排版（与 1.1 手调版一致）

- 见 [`FORMAT_SPEC.md`](FORMAT_SPEC.md) §Word 单元格排版。
- **`section_content.py` 禁止在标题之间、标题与正文之间插入空行**（无 `\n\n`）；由 `_compact_spacing()` 保证。
- **手调后的 `02_开题报告_提交版.doc` 为提交真源**；AI **不得**擅自运行 `fill_template.py --from-template`。
- 仅在你明确要求 bulk 改字时，才运行 `fill_template.py`（默认就地更新）；跑脚本前须 `ensure_doc_closed.py`。

---

## 8. 专项文件索引（只延伸，不另立策略）

| 文件 | 职责 |
|------|------|
| [`FORMAT_SPEC.md`](FORMAT_SPEC.md) | 表格行映射、GB/T 7714、引用示例、Word 字体 |
| [`METADATA_POLICY.md`](METADATA_POLICY.md) | 表头真源、R11/R13/R15 写入范围、doc 关闭检查 |
| [`TITLE_LOCK.md`](TITLE_LOCK.md) | 中英文题目锁定 |
| [`OUTLINE.md`](OUTLINE.md) | 章节大纲 |
| [`WRITING_LOG.md`](WRITING_LOG.md) | 修改历史 |
| [`CLAIMS.md`](CLAIMS.md) | 事实断言 ↔ 内部真源 ↔ 正文脱敏表述 |
| [`00_INDEX.md`](../00_INDEX.md) | 目录与项目交叉索引 |
