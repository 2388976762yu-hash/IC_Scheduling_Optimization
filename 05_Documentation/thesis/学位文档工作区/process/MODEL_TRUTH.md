# 模型与数据真源（Simio · Excel · Experiment）

> **最后更新**：2026-07-02  
> **地位**：工序顺序、设备规模、UPH 字段、Simio 流转口径的**唯一事实真源**。  
> 学位正文、PPT、Experiment 记录、Agent 协作者**必须先读本文件**，再写 `section_content.py` / `midterm_section_content.py` / PPT 文案。  
> 写作策略见 [`WRITING_RULES.md`](WRITING_RULES.md)；可写入正文的脱敏表述见 [`CLAIMS.md`](CLAIMS.md)。

---

## 0. Agent / 协作者强制工作流

动笔前按序执行，**不得跳步**：

1. **读本文件** §1–§4，确认工序顺序、设备台数、MakeSpan 口径。  
2. **读 [`CLAIMS.md`](CLAIMS.md)**，正文数字与实验名称只许用表中「脱敏表述」列。  
3. **需核对字段或 UPH 顺序** → 只读打开 `01_Data/Simio_Import_Data-SPAN.xlsx`（MachineConfig、Materials、FailureConfig、StationTuning）。  
4. **需核对 Simio 流转** → 当前主模型 `02_Simulation_Model/AUTO_Model3.0-batchfactorsspfx.spfx`；Process 名 `Input_*_Entered` / 运行 trace；**禁止**仅凭 Architecture 文档推断路径。  
5. **需核对实验数值** → `05_Documentation/experiments/records/EXP-*.md`，内部编号不得写入正文。  
6. **发现与本文件冲突** → 以本文件 + Excel + 当前 `.spfx` 为准；在 §6 冲突登记表追加一行，**不得**自行改数字或工序顺序「凑整齐」。  
7. **用户 Word 已手改** → 先 `read_submission_docs.py`，再以 doc 为准回写 py（见 WRITING_RULES §0.1）。

**禁止作为事实依据的来源（易过期或已证实错误）：**

| 文件 | 原因 |
|------|------|
| `Architecture_Document.md` §1.2、§5 流程图 | 工序顺序错误，已 STALE |
| `AI_项目过程文档.md` §1.1、`00_项目接手总说明.md` §3.2 ASCII 图 | 已 STALE 横幅 |
| 未在 CLAIMS 登记的实验数字 | 视为未核实 |

---

## 1. 六工序顺序（唯一口径）

**数据顺序 = Simio 实体流转顺序 = MachineConfig 行序 = UPH 列序：**

| 序号 | Station | Simio Server | 台数 | Materials UPH 列 |
|------|---------|--------------|------|------------------|
| 1 | Taping | Server_Taping | 8 | UPH_Taping |
| 2 | B/G | Server_BG | 17 | UPH_BG |
| 3 | D/S | Server_DS | 31 | UPH_DS |
| 4 | DA | Server_DA | 112 | UPH_DA |
| 5 | WB | Server_WB | 284 | UPH_WB |
| 6 | MOLD | Server_MOLD | 7 | UPH_Mold |

**合计 Server：459 台。**

**Excel 真源路径：** `01_Data/Simio_Import_Data-SPAN.xlsx`  
- 表 `MachineConfig`：Station 列自上而下即上表顺序。  
- 表 `Materials`：UPH_Taping … UPH_Mold 列顺序同上。  
- 表 `FailureConfig`、`StationTuning`：Station / SimioServerName 顺序同上。

**Simio 佐证（非第二套顺序，仅验证）：**

- Model 3.0 Process：`Input_Taping_Entered` → `Input_BG_Entered` → `Input_DS_Entered` → `Input_DA_Entered` → `Input_WB1_Entered` → `Input_MOLD1_Entered`。  
- Model 2.0 trace：`M_LOT` 首事件为 `Input_Taping_Entered`（见 `02_Simulation_Model/AUTO_Model2.0_Model_trace.csv`）。

**正文/PPT 写法：** 统一写 **Taping → BG → DS → DA → WB → MOLD**；不要写 D/S→DA→WB→Mold→B/G→Taping。

---

## 2. 批次链与 Separator（与工序顺序配合）

| 层级 | 英文 | 说明 |
|------|------|------|
| 订单 | Order | Source_Orders 释放；Orders 表一行 |
| 制造批次 | MLot | Separator_MLot |
| 弹夹批次 | Magazine | Separator_Mag |
| 子批次 | SubLot | Separator_SubLot |

批次链：**Order → MLot → Magazine → SubLot**（详见 [`TERMINOLOGY.md`](TERMINOLOGY.md)）。

StationTuning 备注（Excel，建模分段参考，**不改变 §1 工序顺序**）：

- Server_Taping、Server_BG：与 MLot 建模相关  
- Server_DS：Magazine 前段建模相关  
- Server_MOLD：可按批次聚合  

---

## 3. 加工时间与 Setup

| 项 | 口径 | 真源 |
|----|------|------|
| 加工时间 | `CurrentQty / Materials.UPH_<Station>` | Materials 表 + 上表 UPH 列 |
| DA/WB Transfer | 每批转入、转出各 3 分钟 | SetupConfig / 模型说明 |
| DA/WB Setup | Assigned_DA_Group 或 Material Group 变化时 10 分钟 | SetupConfig |
| Objective | `0.7 × MakeSpan + 0.3 × Penalty` | DECISIONS / Experiment |
| MakeSpan（当前 Experiment） | Mold 工序截面 `Mold_T_End` | EXP-001；与 MOLD 为末道加工站一致 |
| MakeSpan（计划主口径） | Sink 整线 `LastDepartureTime` | 待统一，见 CLAIMS C-012 |

---

## 4. 当前主模型与 Experiment

| 项 | 值 |
|----|-----|
| 当前主模型文件 | `02_Simulation_Model/AUTO_Model3.0-batchfactorsspfx.spfx` |
| 主数据 | `01_Data/Simio_Import_Data-SPAN.xlsx` |
| 订单数 | 41 |
| 物料数 | 16 |
| Baseline | MLotFactor=1.0, SubLotFactor=1.0 → 见 EXP-001 / CLAIMS C-006 |
| 因子网格 | 26 Scenario → EXP-002 / CLAIMS C-007、C-008 |
| 释放顺序对照 | Orders DueDate 降序 → EXP-003 / CLAIMS C-009 |

Experiment 数值**只**从 EXP 记录或 CLAIMS 引用，禁止心算或沿用旧 Architecture 文档中的示例数。

---

## 5. 下游同步清单（改本文件后必查）

| 下游 | 动作 |
|------|------|
| [`CLAIMS.md`](CLAIMS.md) | C-001 等与工序/设备相关行与 §1 一致 |
| [`TERMINOLOGY.md`](TERMINOLOGY.md) | 工序表顺序与 §1 一致 |
| `section_content.py` / `midterm_section_content.py` | 正文工序表述与 §1 一致 |
| PPT / 答辩稿 | 用户手改；Agent 供稿时只引用 §1 |
| `audit_consistency.py` / `audit_terminology.py` | 提交前跑审计 |
| [`WRITING_LOG.md`](WRITING_LOG.md) | 追加变更一行 |
| 用户 PPT / Word | 见 [`MANUAL_SYNC_PPT_WORD.md`](MANUAL_SYNC_PPT_WORD.md)，用户手改 |

---

## 6. 冲突登记（已消项 2026-07-02）

| 文件 | 处理 |
|------|------|
| `section_content.py` | 已改为 Taping→…→MOLD |
| `midterm_section_content.py` | 已改摘要与 §1.2 |
| `THESIS_NOTES.md` | 已改 |
| `Architecture_Document.md` | STALE 横幅；正文待论文阶段重写 |
| 用户 PPT / Word | 见 MANUAL_SYNC_PPT_WORD.md |

---

## 7. 历史冲突登记（归档）

| 日期 | 文件 | 冲突 | 处理 |
|------|------|------|------|
| 2026-07-02 | section_content.py | D/S→Taping 旧顺序 | 已修正 |
| 2026-07-02 | midterm 摘要 | 编带、分拣… | 已修正 |
