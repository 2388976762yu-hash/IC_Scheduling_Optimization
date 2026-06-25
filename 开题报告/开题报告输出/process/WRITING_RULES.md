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
| **术语** | `TERMINOLOGY.md` | 正文专名 | 换型Setup/弹夹批次Magazine 等 |
| **审计** | `audit_proposal.py` | 提交前检查 | spacing + framing + terminology |
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

## 4. 实验时态与术语（开题正文）

### 4.1 时态：计划 vs 结论

| 章节 | 写什么 | **禁止** |
|------|--------|----------|
| §1.3 研究场景 | 数据、场景参数、**拟**构建模型、**拟**开展实验步骤 | 「前期已完成」「初步结果表明」+ Objective/MakeSpan/Penalty **数值** |
| §1 意义/综述 | 文献缺口、**拟检验**的机制 | 把网格扫描最优值当作已得出结论 |
| §2 实验方案 | 「第一步…」「拟开展…」 | — |
| §2.4 可行性 | 数据、平台、方法**条件具备** | 用实验最优值证明可行 |
| §3 研究基础 | 模型框架、工具链、文献**已搭建/已研读** | 「初步实验结果」段落及 Penalty 峰值等数字 |

**原则**：开题正文中的实验是**将要去做**的研究内容；提前试跑的结果**不得**写入第一节，第二节可行性亦不得引用具体最优 Objective。数值结论留待中期/论文，内部真源见 [`CLAIMS.md`](CLAIMS.md)。

### 4.2 实验中文名称（与 CLAIMS 脱敏表述一致）

| 内部真源 | 正文用语 |
|----------|----------|
| EXP-001 | 因子均为 1.0 的**基准情景** |
| EXP-002 | **26 情景批次因子全因子网格扫描** |
| EXP-003 | **仅调整订单表释放顺序的对照** |
| 拟开展 | **交期升序释放与 FIFO 的对照实验** |

内部编号只保留在 `05_Documentation/experiments/` 及 CLAIMS「内部真源」列。

### 4.3 术语

专业名词对照见 [`TERMINOLOGY.md`](TERMINOLOGY.md)。提交前运行 `python audit_proposal.py`（含 spacing / framing / terminology 三项审计）。

**换型Setup ≠ 设置 ≠ 换型总称**；Magazine = **弹夹批次**（非「杂志」）；DA/WB 推荐句见 TERMINOLOGY。

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
