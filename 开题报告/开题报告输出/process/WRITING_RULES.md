# 开题报告写作规则（活文档）

> **最后更新**：2026-06-24  
> **适用范围**：`section_content.py` → `02_开题报告_提交版.doc` 的全部正文写作与修订

---

## 0. 规则本身的维护（随时修改）

- 本文件及 [`FORMAT_SPEC.md`](FORMAT_SPEC.md)、[`METADATA_POLICY.md`](METADATA_POLICY.md) 均为**活规则**，**可随时修改**，无需等某一版 Word 定稿后再改。
- **以仓库中最新 markdown 为准**；Word 提交版是输出物，规则变更后应同步改 `section_content.py` 并重跑 `fill_template.py`（或手改 02）。
- 每次调整规则或正文策略，在 [`WRITING_LOG.md`](WRITING_LOG.md) **追加一行**，注明日期、改了什么、涉及文件。
- AI 或协作者动笔前应先读本节 + 下文；若与用户口头要求冲突，**以用户最新指示优先**，并回写本文件避免再次偏离。

---

## 1. 真源与产出链

| 层级 | 文件 | 说明 |
|------|------|------|
| 规则 | 本文件、`FORMAT_SPEC.md` | 怎么写 |
| 内容 | `section_content.py` | 写什么 |
| 文献 | `BIBLIOGRAPHY.yaml` | 参考文献元数据 |
| 表头 | `2120253828-…开题报告.doc` | 姓名、学科等（脚本不覆盖） |
| 提交 | `02_开题报告_提交版.doc` | 学院表格填表版 |

详见 [`METADATA_POLICY.md`](METADATA_POLICY.md)、[`00_INDEX.md`](../00_INDEX.md)。

---

## 2. 用语与格式

### 2.1 人称与术语

- 全文使用 **「本研究」**，不用「本课题」。
- 正文中**不写**内部决策编号（如 D-004）、内部文件名（如 `CLAIMS.md`）、脚本名，除非学院模板明确要求。

### 2.2 括号

- **少用括号堆砌**；英译、补充说明优先并入句子。
- 可保留：术语**首次**英译、参考文献类型 [J]/[M]（仅文献列表）、著者-出版年 `Law（2015）`。
- 综述与研究意义段落：不用 `（1）（2）（3）` 列举，改用 **「第一，……；第二，……」** 或分号并列。
- 设备台数、实验数值用顿号/逗号嵌入句中，不用括号包裹。

### 2.3 引用

- 正文：**著者-出版年制**（全角括号），见 `FORMAT_SPEC.md`。
- 参考文献：**中文文献 + 外文文献** 分列，各自按第一作者字母序，全文编号连续；真源 `BIBLIOGRAPHY.yaml`。

---

## 3. 实验与初步工作（开题专用）

- **禁止**在开题正文使用项目组内部编号：`EXP-001`、`EXP-002` 等。
- 内部编号仅保留在 `05_Documentation/experiments/` 等工作日志。
- 已完成工作：用可读中文名称，并在**首次出现处**说明内容，例如：
  - 因子均为 1.0 的**基准情景**
  - **26 情景批次因子全因子网格扫描**
  - **仅调整订单表释放顺序的对照**
- 计划工作：写在第二节 **「实验方案」**，用「第一步…第四步…」「拟开展…对照实验」。
- **研究意义、文献综述**等段落：不得突然抛出未定义代号 + 具体数值；若举例，须承接前文已定义的实验名称。

---

## 4. 写回 Word 的流程

1. 改 `section_content.py` / `BIBLIOGRAPHY.yaml`（及本规则若需）。
2. **保存并关闭** WPS/Word 中的开题 doc。
3. `python ensure_doc_closed.py` → 显示 OK。
4. `python fill_template.py`（自动预检 + 只写 R11/R13/R15）。
5. 在 02 中手调版式（字体、行距等）；**以手调后的 02 为提交真源**。

失败时：`python ensure_doc_closed.py --close` 或 `.\release_word_lock.ps1 -CloseWps`。

---

## 5. 脱敏

- 正文与 Word **不得出现**企业名、品牌名、可识别合作方信息。见 [`ANONYMIZATION.md`](ANONYMIZATION.md)。

---

## 6. 相关文件索引

| 文件 | 内容 |
|------|------|
| [`FORMAT_SPEC.md`](FORMAT_SPEC.md) | 表格行映射、GB/T 7714、标点细则 |
| [`METADATA_POLICY.md`](METADATA_POLICY.md) | 表头真源、脚本写入范围 |
| [`TITLE_LOCK.md`](TITLE_LOCK.md) | 题目锁定 |
| [`OUTLINE.md`](OUTLINE.md) | 章节大纲 |
| [`WRITING_LOG.md`](WRITING_LOG.md) | 修改历史 |
| [`CLAIMS.md`](CLAIMS.md) | 事实断言核查（内部用，正文不引用编号） |
