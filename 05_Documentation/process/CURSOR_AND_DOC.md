# Cursor 工具与 Word 文档（.doc）

> **最后更新**：2026-06-25  
> 说明：Cursor Marketplace / MCP 里有什么「文档类」能力，以及**本开题项目该用哪套**。

---

## 1. Cursor Marketplace 有 doc 相关的吗？

**几乎没有适合本项目的。**

官方 [Cursor Marketplace](https://cursor.com/marketplace) 里与「文档」沾边的多是：

| 类型 | 例子 | 是否适合开题 `.doc` |
|------|------|---------------------|
| 协作文档 | Linear、monday 文档 | 否，不是 Word |
| 代码文档 | 自动生成 API/架构说明、Canvas 渲染 | 否，不是学院填表 |
| 数据/运维 | Datadog、Railway 等 | 否 |

**没有**「南开开题报告 / Simio / `.doc` 填表」一类官方插件。

---

## 2. MCP：Word 类服务器（多为 `.docx`）

可在 **Customize → MCP** 或 `.cursor/mcp.json` 里自行添加，常见有：

| 名称 | 格式 | 说明 |
|------|------|------|
| [docx-mcp-server](https://pypi.org/project/docx-mcp-server/) | **.docx** | 创建/编辑 docx、markdown 转 docx |
| [office-word-mcp-server](https://cursormcp.dev/mcp-servers/776-office-word-mcp-server) | **.docx** | 读写 Word，偏 docx |
| [MCP-Doc](https://github.com/MeterLong/MCP-Doc) | **.docx** | FastMCP + python-docx |

### 为什么不推荐替换本项目的 `fill_template.py`

| 本项目现实 | MCP docx 的局限 |
|------------|-----------------|
| 学院模板是 **`.doc`**（Table 填表） | MCP 普遍只稳支持 **`.docx`** |
| 需写 Table2 **R11/R13/R15** 单元格 | MCP 不懂你校模板行号 |
| 需保留表头、手调版式 | bulk 改 docx 仍易冲格式 |
| 已有 `win32com` + 真源链 | 与 `WRITING_RULES` / `METADATA_POLICY` 已对齐 |

**结论**：开题 **继续用** `section_content.py` →（必要时）`fill_template.py` → WPS 手调 **`02_开题报告_提交版.doc`**。MCP 可作为将来「纯 docx 草稿」实验，**不替代**提交版 `.doc` 流程。

---

## 3. 本项目已具备的「doc 工作流」（优于 Marketplace）

| 工具 | 作用 |
|------|------|
| `开题报告/开题报告输出/process/section_content.py` | 正文真源（无空行） |
| `fill_template.py` | 只写 R11/R13/R15；默认**就地更新** 02 |
| `ensure_doc_closed.py` | 写 doc 前检查 WPS/Word 是否占用 |
| `audit_spacing.py --word` | 审计空段是否为 0 |
| `audit_proposal.py --word` | 一键审计 D1–D8（含 Word 空行） |
| `scripts/push-via-clash.ps1` | push 走 Clash（见 `GIT_AND_NETWORK.md`） |

规则与 Skill（本仓库，非 Marketplace）：

| 路径 | 作用 |
|------|------|
| `.cursor/rules/kaiti-proposal.mdc` | 打开 `开题报告/**` 时约束真源、禁空行、慎跑 fill |
| `.cursor/skills/kaiti-proposal/SKILL.md` | 聊天 `/kaiti-proposal` 走开题流程 |

写作真源：`开题报告/开题报告输出/process/WRITING_RULES.md`

---

## 4. 若仍想试 MCP docx（可选）

仅用于**新建 docx 草稿**，不要直接改 `02_…提交版.doc`：

```json
{
  "mcpServers": {
    "docx-mcp": {
      "command": "uvx",
      "args": ["docx-mcp-server"]
    }
  }
}
```

需本机已装 Python/`uvx`。配置路径：**Cursor → Settings → Features → MCP**。

---

## 5. 相关索引

- 开题总索引：`开题报告/开题报告输出/00_INDEX.md`
- Git / Clash：`05_Documentation/process/GIT_AND_NETWORK.md`
- 表头与脚本：`开题报告/开题报告输出/process/METADATA_POLICY.md`
