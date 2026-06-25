# 开题报告多维度审计说明

> **用途**：提交前质量门禁；脚本真源见 `audit_proposal.py`。  
> **正文真源**：`section_content.py`；**规则真源**：`WRITING_RULES.md`。

---

## 运行方式

```powershell
cd 开题报告\开题报告输出\process
python ensure_doc_closed.py
python audit_proposal.py              # 全部维度
python audit_proposal.py --word     # 含 Word R11/R13/R15 空行
```

退出码 `0` = 通过；非零 = 须修正后再提交。

---

## 维度一览

| ID | 脚本 | 维度 | 检查内容 |
|----|------|------|----------|
| D1 | `audit_spacing.py` | **排版** | 源文本与 Word 无空段落；标题间无 `\n\n` |
| D2 | `audit_proposal_framing.py` | **时态与禁写** | §1/§2 无实验数值；无「导师…」；无 EXP/D 编号 |
| D3 | `audit_terminology.py` | **术语** | 弹夹批次、换型Setup、禁机翻词、§1/§2 无数值 |
| D4 | `audit_academic.py` | **学术规范** | 人称、著者-出版年括号、章节结构、禁 Markdown |
| D5 | `audit_anonymization.py` | **脱敏** | 企业名/品牌/内部文件名零命中 |
| D6 | `audit_consistency.py` | **表述一致** | 数据来源用语、批次链、Objective 公式一致 |
| D7 | `audit_citations.py` | **引用可核** | 正文引用年份 ⊆ BIBLIOGRAPHY；无 `[1]` 式正文引用 |

---

## 各维度细则

### D4 学术规范（`audit_academic.py`）

| 项 | 要求 |
|----|------|
| 人称 | 全文「**本研究**」，禁止「本课题」 |
| 引用括号 | 著者-出版年用**全角**（），如 `Law（2015）` |
| 两作者西文 | 特殊：`Sang-Jin Lee 与 Tae-Eog Lee（2008，2011）` |
| 章节 | §1 含 1.1–1.3、2.、3.1–3.6、4. 主要参考文献；§2 含目标/内容/方法/可行性/创新/计划/成果；§3 含积累与尚缺条件 |
| 禁 Markdown | 正文无 `#`、`**` |
| 开题语气 | §3 标定实验须含「学位论文」或「正式结论」限定语 |

### D5 脱敏（`audit_anonymization.py`）

见 [`ANONYMIZATION.md`](ANONYMIZATION.md)。正文禁用企业/品牌/可识别产品场景词。

### D6 一致性（`audit_consistency.py`）

| 项 | 统一表述 |
|----|----------|
| 数据来源 | **企业脱敏 Simio 导入数据**（禁 bare SPAN 文件名） |
| 批次 | **Order—MLot—Magazine—SubLot**（禁「杂志批次」；慎用孤立的「三级批次」） |
| 目标函数 | `Objective = 0.7×MakeSpan + 0.3×Penalty` |
| 设备规模 | 459 台；41 条订单；16 种物料 |

### D7 引用（`audit_citations.py`）

- 正文只用著者-出版年，不用 `[1]`。
- 抽样校验：正文出现的 `(20xx)` 年份在 `BIBLIOGRAPHY.yaml` 中有对应条目。

---

## 人工复核清单（脚本不覆盖）

- [ ] 表头个人信息与学院模板一致（`METADATA_POLICY.md`）
- [ ] 文献列表 32 篇、GB/T 7714 格式
- [ ] 逻辑：研究缺口 ↔ 研究内容 ↔ 实验方案 三者对应
- [ ] 进度计划 2026.6—2027.5 与学院学制匹配
- [ ] 导师组签字页未误填

---

## 维护

新增禁写项或维度 → 更新对应 `audit_*.py` + 本文件 + `WRITING_RULES.md` §4 + `WRITING_LOG.md` 一行。
