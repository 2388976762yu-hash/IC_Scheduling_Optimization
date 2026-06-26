# 仓库根目录归档规则（REPO_FILING）

> **最后更新**：2026-06-25  
> **用途**：用户常把新文件放在项目根目录；AI 协作者应在会话中**主动阅读并归档**，保持根目录整洁。

---

## 根目录应保留什么

| 允许常驻 | 说明 |
|----------|------|
| `README.md` | 项目入口 |
| `.gitignore` | Git 配置 |
| `01_Data/` … `05_Documentation/` | 编号主目录 |
| `开题报告/` | **根目录仅 3 个待提交 `.doc`**；学院参考材料在 [`开题报告/参考资料/`](../开题报告/参考资料/00_README.md)（**禁止移走或覆盖**） |
| `项目辅助材料/` | 会议纪要、参考文献 PDF 等 |
| `scripts/` | 工具脚本 |

**不应**在根目录长期堆放：分析报告、实验 Word、临时导出、学位文档 MD/脚本、学院注意事项 docx/pdf。

---

## 归档决策表（读文件名 + 抽样内容后执行）

| 文件特征 | 目标位置 | 归档后动作 |
|----------|----------|------------|
| 仿真 / Experiment **结果分析**（含 MakeSpan、场景、因子、V* 版本号） | `05_Documentation/experiments/analysis/`（现行）或 `…/analysis/legacy/`（旧版 V1/V8） | 更新该目录 `00_INDEX.md` 一行 |
| 单次实验记录、可复现实验参数 | `05_Documentation/experiments/records/EXP-xxx_*.md` | 更新 `EXPERIMENT_LOG.md` |
| **项目状态** / 阶段总结 / 待办 | `05_Documentation/status/CURRENT_STATUS.md`（摘要）+ 原 Word → `status/archives/` | CHANGELOG 留痕 |
| 论文 / 开题 / 中期正文、脚本、GB/T 文献 | `05_Documentation/thesis/学位文档工作区/` | 见该目录 `00_INDEX.md` |
| 学院填写注意事项 docx、实施细则 pdf、**空白 Word 模板** | **`开题报告/参考资料/`**（用户对照用；与 3 份提交件分开） | 可 **复制** 到工作区备份，**不得从开题报告删除** |
| Simio 报告 CSV / 导出 JSON | `04_Output/` | 结论写入 `experiments/records/` |
| 模型架构、spfx 说明 | `02_Simulation_Model/modeldetail/` | — |
| 会议原始记录 | `项目辅助材料/会议纪要/` | 决议摘录 → `process/DECISIONS.md` |
| 参考文献 PDF | `项目辅助材料/参考文献/` | 开题引用 → `BIBLIOGRAPHY.yaml` |
| 书写规范 / 学院细则 PDF | `开题报告/参考资料/` 或 `项目辅助材料/书写规范/` | 开题中期细则优先放 `开题报告/参考资料/` |
| 无法判断 | **先读内容**，在 `process/CHANGELOG.md` 说明暂存理由；可建 `05_Documentation/inbox/` 短期存放 | 下次会话再分类 |

---

## AI 协作者工作流（用户把文件丢进根目录时）

1. **列出** 根目录新增/非常驻文件（对比 git status 或 `ls`）。
2. **阅读** 文件名 + 前几段正文（Word/PDF 用 `python-docx` / 已有脚本），判断上表类别。
3. **移动** 到目标目录（`git mv` 或 `shutil.move`），**不要**在根目录留副本。
4. **更新索引**：对应目录 `00_INDEX.md` 或 `EXPERIMENT_LOG.md` / `CURRENT_STATUS.md` / `CHANGELOG.md`。
5. **勿提交** 含 PII 的 dump；学位 `.doc` 表头个人信息不写入 markdown 真源。
6. **输出 ≠ 参考**：脚本只更新 `开题报告/` 根目录 3 份提交 `.doc` 的**空位**；** never ** 用空白模板 `copy` 覆盖；** never ** 覆盖 `开题报告/参考资料/`。
7. **本地优先**：用户在 WPS 已编辑的内容视为真源；AI 未经明确要求不得运行 `fill_midterm.py` / `fill_template.py`。

---

## 已归档示例（2026-06-25）

| 原路径（根目录） | 现路径 |
|------------------|--------|
| `V1仿真结果详细分析报告.docx` 等 4 份 | [`experiments/analysis/legacy/`](../experiments/analysis/legacy/00_INDEX.md) |
| `项目状态总结与论文方向报告.docx` | [`status/archives/`](../status/archives/00_INDEX.md) |

---

## 相关文档

- 文档中心地图：[`../README.md`](../README.md)
- Cursor 规则：`.cursor/rules/repo-root-filing.mdc`（与本文同步）
