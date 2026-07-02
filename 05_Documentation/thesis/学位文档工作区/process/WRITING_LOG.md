# 撰写日志

| 日期 | 动作 | 文件 |
|------|------|------|
| 2026-05-24 | 锁定题目 | process/TITLE_LOCK.md |
| 2026-05-24 | 创建索引与 process 骨架 | 00_INDEX.md, OUTLINE, CLAIMS, ANONYMIZATION |
| 2026-05-24 | 录入 BIBLIOGRAPHY.yaml（28 篇） | process/BIBLIOGRAPHY.yaml |
| 2026-05-24 | 按学院表格模板重写：GB/T7714 文献、[序号]+字母序、全角标点、著者（年份）引用 |
| 2026-05-24 | 生成 `02_开题报告_提交版.doc`（fill_template.py 填表） |
| 2026-05-24 | 脱敏扫描 | process/ANONYMIZATION.md |
| 2026-05-24 | 更新 THESIS_NOTES 双向索引 | 05_Documentation/thesis/THESIS_NOTES.md |
| **2026-06-24** | **重大修订**：扩展 SECTION1/2/3 至 ~7300 汉字（正文）+ 32 篇文献 | process/section_content.py |
| **2026-06-24** | 纳入文件夹 3 篇唯一 PDF：Lin2015、Hoppe2025、Luttmann2026 | BIBLIOGRAPHY.yaml |
| **2026-06-24** | 更正 Panwalkar 年份 1993→1977 | BIBLIOGRAPHY.yaml, REFERENCE_VERIFICATION.md |
| **2026-06-24** | fill_template 从 YAML 自动生成 GB/T7714 列表；导出 docx | fill_template.py |
| **2026-06-24** | 新建 REFERENCE_VERIFICATION.md | process/REFERENCE_VERIFICATION.md |
| **2026-06-24** | 重新生成提交版 doc/docx | 02_开题报告_提交版.doc/.docx |
| **2026-06-24** | fill_template 改为仅写 R11/R13/R15；基础信息以模板 doc 为准 | fill_template.py, FORMAT_SPEC.md |
| **2026-06-24** | 新增 METADATA_POLICY；辅助 md 不再复制个人信息 | METADATA_POLICY.md, 01_, OUTLINE, TITLE_LOCK |
| **2026-06-24** | 正文减括号堆砌；参考文献改中文/外文分列排序 | section_content.py, fill_template.py, FORMAT_SPEC.md |
| **2026-06-24** | 工作前 doc 关闭检查 ensure_doc_closed.py；fill 自动预检 | ensure_doc_closed.py, METADATA_POLICY.md |
| **2026-06-24** | 正文去除 EXP 内部编号；改中文实验名称表述 | section_content.py, FORMAT_SPEC.md |
| **2026-06-24** | 新增 WRITING_RULES.md 活文档（规则可随时修改） | WRITING_RULES.md, 00_INDEX, FORMAT_SPEC |
| **2026-06-24** | 整合写作规则真源：WRITING_RULES 策略 / FORMAT 排版 / METADATA 表头；CLAIMS 对齐中文实验名 | WRITING_RULES, FORMAT_SPEC, METADATA, CLAIMS, 00_INDEX |
| **2026-06-24** | 锁定段落排版：无标题间空行；fill 默认就地更新；禁止 --from-template 覆盖手调 02 | section_content, fill_template, FORMAT_SPEC, WRITING_RULES |
| **2026-06-24** | 空行审计 audit_spacing.py；fix 参考文献拼接空行；Word R11/R13/R15 重填 | audit_spacing.py, fill_template.py, 02 doc |
| **2026-06-24** | 建立 D1–D7 多维度审计（AUDIT_DIMENSIONS + audit_*.py）；批次链与数据用语统一 | AUDIT_DIMENSIONS, audit_*.py, section_content, WRITING_RULES |
| **2026-06-26** | **中期考核表**：英文题目 Back-End；关键词去 Simio、增仿真优化 | midterm_section_content.py, TITLE_LOCK.md |
| **2026-06-26** | **强制先读 doc 再同步**：新增 `read_submission_docs.py`；禁止猜测多删句 | WRITING_RULES §0.1, read_submission_docs.py |
| **2026-07-02** | **删除全部写 Word 脚本**（fill_template / fill_midterm / insert_tech_route 等）；Word 仅用户 WPS 手改 | 删 py，WRITING_RULES §0.1 |
| **2026-07-02** | **工序真源统一**：section_content、midterm 改 Taping→MOLD；MANUAL_SYNC_PPT_WORD 供用户手改 PPT/Word | section_content, midterm, MODEL_TRUTH, MANUAL_SYNC |
| **2026-07-02** | **MODEL_TRUTH.md**：工序唯一顺序；Agent 强制工作流 | MODEL_TRUTH, CLAIMS, TERMINOLOGY, WRITING_RULES |

## 2026-06-24 修订说明

- 第一节新增 1.1—1.3 产业/业务/数据分节，扩展四线文献综述与 3.6 课题定位
- 第二节补充研究方法（DES、Scenario Generator、EDD、敏感性）、实验方案与可行性
- 第三节写模型框架与工具链积累（不写实验数值结论）
- 参考文献 28→32；文件夹 5 PDF 映射为 3 篇唯一文献
