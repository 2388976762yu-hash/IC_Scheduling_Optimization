# 开题报告基础信息维护规则（表头与脚本真源）

> 写作策略 → [`WRITING_RULES.md`](WRITING_RULES.md)。格式排版 → [`FORMAT_SPEC.md`](FORMAT_SPEC.md)。**本文件只管表头、脚本写入范围与 doc 工作流。**

## 工作前检查（必做）

凡 **AI 改正文并写回 Word**、**运行 `fill_template.py`** 或 **批量更新参考文献** 之前：

1. 在 WPS/Word 中 **保存并关闭** `02_开题报告_提交版.doc` 与模板 doc 的标签页（WPS 关标签后进程可能仍在，需确认无占用）。
2. 在项目目录执行检查：
   ```powershell
   cd 开题报告\开题报告输出\process
   python ensure_doc_closed.py
   ```
3. 若提示占用，先手动关文档；或执行：
   ```powershell
   python ensure_doc_closed.py --close
   # 或
   .\release_word_lock.ps1 -CloseWps
   ```
4. 看到 `OK: 模板与提交版均未占用` 后再跑 `fill_template.py`。

`fill_template.py` 启动时会 **自动调用** `ensure_documents_closed(auto_close=True)`：尝试结束 WINWORD 及标题含「开题报告」的 WPS 窗口；仍失败则中止并提示，避免 silently 写旧版或 PermissionError。

## 唯一真源

**[`2120253828-喻炫琪-研究生开题报告.doc`](../../2120253828-喻炫琪-研究生开题报告.doc)**

姓名、学号、培养单位、题目、课题来源、导师、工作周期、报告日期、评审组等**表格基础信息只在此文件维护**。

## 生成输出时不得覆盖的单元格

| 区域 | 说明 |
|------|------|
| Table 1 全部 | 封面 |
| Table 2 R1—R9 | 表头与培养指导小组 |
| Table 2 R16—R18 | 承诺与导师意见（手写） |
| Table 3 全部 | 评审组（已在模板中填写则保留） |

## 允许写入的单元格

| 单元格 | 内容来源 |
|--------|----------|
| Table 2 R11 | `section_content.py` SECTION1 + `BIBLIOGRAPHY.yaml` |
| Table 2 R13 | `section_content.py` SECTION2 |
| Table 2 R15 | `section_content.py` SECTION3 |

## 各文件职责

| 文件 | 职责 | 不得包含 |
|------|------|----------|
| `2120253828-…开题报告.doc` | 基础信息 + 作为填表模板 | — |
| `fill_template.py` | 复制模板 → 只写 R11/R13/R15 | 硬编码姓名、导师、课题来源等 |
| `section_content.py` | 三节正文 | 封面字段 |
| `BIBLIOGRAPHY.yaml` | 参考文献 | 个人信息 |
| `TITLE_LOCK.md` | 锁定**题目**与脱敏规则 | 不再维护个人信息副本 |
| `01_开题报告正文.md` | 结构索引 | 封面字段副本 |
| `02_开题报告_提交版.doc` | **提交真源**（可手调版式）；脚本仅批量写入 R11/R13/R15 文字 | 脚本不得改基础信息；手改后慎重复跑脚本 |

## 协作约定

0. **写作策略**以 [`WRITING_RULES.md`](WRITING_RULES.md) 为唯一真源；格式以 [`FORMAT_SPEC.md`](FORMAT_SPEC.md)；表头以本文件。**规则可随时修改**，改后 [`WRITING_LOG.md`](WRITING_LOG.md) 留痕。

1. 你改**基础信息** → 只改 `2120253828-…开题报告.doc`。
2. 改正文 bulk / 文献 → 改 `section_content.py` / `BIBLIOGRAPHY.yaml`；需要时再运行 `fill_template.py`（**会覆盖** R11/R13/R15 文字，可能打乱你已调的版式）。
3. 你改**提交版版式与细节** → 直接在 `02_开题报告_提交版.doc` 里改（WPS/Word 手调）；**以你手改后的 02 为提交真源**。脚本生成的格式常需人工修正，属正常流程。
4. AI 或脚本**不要**把 markdown 里的旧个人信息写回 Word，也**不要**在生成时“同步更新”模板里已有的表格字段。
5. 运行 `fill_template.py` 前请**关闭** WPS/Word 中已打开的 `02_开题报告_提交版.doc`（见上文「工作前检查」）；脚本会自动预检，仍占用则中止。
6. 脚本生成后会清除文件只读属性，并取消 Word「建议只读」标记；若仍无法保存，请关闭文档后重新打开。

## 为什么有时要强制结束 Word（WINWORD.EXE）

`fill_template.py` 通过 **Microsoft Word 的 COM 接口**在后台自动填表（不是 WPS）。正常结束时会 `Quit` 并关文档；但在以下情况 **Word 可能留在后台**，导致文件被锁、WPS 显示只读：

| 情况 | 说明 |
|------|------|
| 脚本中途报错 | 旧版未用 `try/finally` 关干净时，Word 进程可能残留 |
| 你正用 WPS 开着 02 | 与 Word 争用同一文件，脚本失败或 Word 挂起 |
| Word 弹窗被挡住 | 后台 `Visible=False`，对话框阻塞 `Quit` |
| 手动中断 Python | Ctrl+C 时 COM 来不及释放 |

**处理**：任务管理器结束 **Microsoft Word**（`WINWORD.EXE`），不是 WPS；然后重新打开 02。  
**预防**：跑脚本前关闭 WPS/Word 里的 02；脚本跑完看任务栏有没有隐藏的 Word 窗口。

日常手改提交版用 **WPS 即可**，不必开 Word；只有运行 `fill_template.py` 时才会短暂启动 Word。
