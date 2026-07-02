# AI 项目过程文档（内部上下文）

> **用途**：供 Cursor / AI 助手跨会话读取，避免 token 截断后丢失项目记忆。  
> **维护**：每次有模型改动、会议结论、实验结果、关键决策时更新「变更日志」和对应章节。  
> **Git 文档（人类 + 论文）**：见 [`05_Documentation/`](../05_Documentation/README.md)  
> **最后更新**：2026-05-30

---

## 0. 30 秒速览

| 项 | 内容 |
|----|------|
| 项目 | SanDisk IC 后端制造 Simio 离散事件仿真 + 排程优化 |
| **当前主模型** | `02_Simulation_Model/AUTO_Model2.0.spfx` |
| 主数据 | **`01_Data/Simio_Import_Data-SPAN.xlsx`** |
| 最新会议 | **第七次 2026/5/23**（执行依据） |
| 当前阶段 | EXP-002 完成（26 场景）→ **待 Source 按 DueTime EDD 释放** |
| GitHub | `2388976762yu-hash/IC_Scheduling_Optimization` |
| 用户 | 喻炫琪（独自推进 Simio；导师王谦） |

---

## 1. 模型架构（Model 2.0）

### 1.1 主流程

> ⚠️ **STALE**：本节 ASCII 图与 Excel / Simio 真源不符。工序顺序见 [`MODEL_TRUTH.md`](../05_Documentation/thesis/学位文档工作区/process/MODEL_TRUTH.md)：**Taping → BG → DS → DA → WB → MOLD**。

```
Source_Orders
  → Separator_MLot
  → Server_DS → Server_DA → Server_WB
  → Separator_Mag
  → Server_MOLD → Server_BG
  → Separator_SubLot
  → Server_Taping
  → Combiner_Sub
  → Sink_Finished
```

### 1.2 与 Model 1.0 差异

- 流程顺序不同（先 DS/DA/WB，再 Mag/SubLot，后 Mold/BG/Taping）
- 有 Worker 搬运（Transfer In/Out）
- DA/WB 有换型（3min Transfer + 10min Setup）
- Source 放单问题已解决：41 单全部完成（1.0 时仅 13 单入流）

### 1.3 设备规模

DS 31 | DA 112 | WB 284 | Mold 7 | BG 17 | Taping 8（共 459 台）

### 1.4 加工时间

```simio
ProcessingTime = OrderEntity.CurrentQty / Materials.UPH[工序]
```

### 1.5 `.spfx` 解析限制

- `.spfx` = ZIP（354 文件），内部 XML 为 Simio 专有编码，**不可当明文 XML 手改**
- 解析脚本：`03_Algorithm/parse_simio_spfx.py`
- 输出：`02_Simulation_Model/modeldetail/AUTO_Model2.0_parsed.json` + `_parsed_summary.md`
- 结构理解靠：Architecture 文档 + modeldetail 截图 + 运行报告

---

## 2. 第七次会议决议（2026/5/23）— 当前执行清单

### 2.1 必做（P0）

- [x] **记录 Make Span / 工序起止时间**（用户 2026-05-24 确认已成功实现）
  - 用 Model 级 **Real** 状态变量 + `Model.TimeNow`
  - 每工序：第一个进入 → `T_Start`；每次离开更新 → `T_End`
  - Sink：`LastDepartureTime` = 全局 Make Span
- [ ] **ReleaseDate 统一为基准日**（如 1/9），41 单 = 一周工作量
- [ ] **DueDate − ReleaseDate 保留** → 交期长度（0 = 当天交）
- [ ] 语义：手里已有全部订单，尽快排完；**不是**每日新订单到达

### 2.2 排程与目标（P1）

- [ ] 首队列不用 FIFO → 按 **(DueDate − ReleaseDate) 升序**（交期最紧优先）
- [x] **Experiment1 首次跑通**（2026-05-24）：MakeSpan=78.40、Penalty=0、Objective=54.88（Ending 80h，Primary=Objective）
- [ ] 目标函数（Experiment 公式）：`0.7 × MakeSpan + 0.3 × Penalty`
  - Penalty：任一订单延期 → 大罚值（如 1e7）；全部准时 → 0
  - 会议早段曾反过来说法，**以 Experiment 演示为准**
- [ ] 仿真时长：144h 起，按实际 Make Span 调整；不够再 360/480h

### 2.3 暂缓 / 等确认

- [ ] M Lot / Sub Lot 批次大小作决策变量（数据有小数 843.75，待中芯国际同学校口径）
- [ ] `Quantity per magazine = 480` vs 960 含义
- [ ] 每台 entity 预分配机台号（导师查技术方案；当前 Cycling 不行）
- [ ] 利用率按 90% 对标（Simio 报告含空等，**先以 Make Span + 准交为主**）
- [ ] 模型结构大改 — 导师说「先别动」，等数据确认

### 2.4 沟通

- 每周至少一次，暂定 **周六晚 8 点**

---

## 3. 仿真实验与结果摘要

### 3.1 V1 原始（1×）利用率 — 负荷过低

| 工序 | 平均利用率 |
|------|-----------|
| DS | 13.7% |
| DA | 13.5% |
| WB | 13.4% |

- 41 单 Order 完成率 100%
- 拆分后：MLot 283 / SubLot 652 / Mag 1255
- 汇总：`04_Output/v1v2_analysis.json`

### 3.2 已知 Trace 问题

`AUTO_Model2.0_Model_trace.csv`：`WB_Failed_1` Seize 节点类型不匹配（OrderEntity vs WB_Server）

### 3.3 数据扩容注意

- 导师认为 **单订单 quantity ×6 不合理**；更合理是 **复制订单 + 改 ReleaseDate**
- Warm-up：长跑丢弃前几小时，避免冷启动利用率失真

---

## 4. Simio 技术备忘（易忘）

### 4.1 状态变量类型

| 类型 | 何时用 |
|------|--------|
| **Real** | `Model.TimeNow`、Make Span、工序 T_Start/T_End、时长差 |
| **Integer** | 进入计数 EnterCount |
| **DateTime** | Excel 的 ReleaseDate/DueDate（entity 属性）；**不用于**记录仿真时刻 |
| **Boolean** | 可选，是否已开始记录 |

### 4.2 工序时间记录模式（用户已实现）

```simio
// 第一个进入（On Entered Input Buffer / In 节点）
If DS_EnterCount == 0 Then DS_T_Start = Model.TimeNow
DS_EnterCount = DS_EnterCount + 1

// 每次离开（On Exited / Out 节点）
DS_T_End = Model.TimeNow

// 工序跨度
DS_StationSpan = DS_T_End - DS_T_Start
```

- 最后一单无法预知 → **每次离开都更新 T_End**，仿真结束时的值即所求
- 触发点选型：要含排队用 Input Buffer；只要加工用 Processing

### 4.3 实现方式选项

- **方案 A**（推荐省事）：直接在 Server State Assignment
- **方案 B**（用户倾向）：工序前后各一个 BasicNode（Transfer=0）+ State Assignment

---

## 5. 关键文件索引

| 路径 | 说明 |
|------|------|
| `项目辅助材料/00_项目接手总说明.md` | 人类接手文档（2026-05-24 已更新至 Model 2.0） |
| `项目辅助材料/AI_项目过程文档.md` | **本文件** |
| `项目辅助材料/会议纪要/` | 第七次 2026/5/23 为最新 |
| `02_Simulation_Model/AUTO_Model2.0.spfx` | 主模型 |
| `02_Simulation_Model/modeldetail/AUTO_Model2.0_Architecture_Document.md` | 架构详解 |
| `03_Algorithm/parse_simio_spfx.py` | spfx 解压清单 |
| `04_Output/v1v2_analysis.json` | V1/V2 利用率汇总 |
| `01_Data/Simio_Import_Data_Tuned_V*.xlsx` | 各版实验数据 |

---

## 6. 开题与论文方向

- 题目方向：**多目标优化的 IC 制造企业生产排程**
- 开题报告约 20 页（课程要求；导师认为不必过度投入）
- 核心指标：**Make Span + 准交率（罚函数）**；利用率辅且计算方式待讨论
- 决策变量候选：M Lot / Sub Lot 批次大小、派工规则、换型策略

---

## 7. 待用户 / 导师下一步

1. Excel：ReleaseDate 基准化 + 保留交期差
2. Simio：首队列改为 EDD（DueDate−ReleaseDate 升序）
3. Simio：Experiment 框架 + 罚函数 Response
4. 负荷校准（复制订单 / warm-up，非简单 ×quantity）
5. 等导师/中芯国际确认 magazine、batch size 数据口径

---

## 8. 变更日志

| 日期 | 变更 |
|------|------|
| 2026-05-24 | 开题报告初稿：`开题报告/开题报告输出/`，28 篇文献，脱敏正文 |
| 2026-05-30 | EXP-003 DueDate降序复跑；Obj_min=52.38, Pen_max=700；模型 Model3.0-batchfactors |
| 2026-05-30 | EXP-002 SPAN 26 场景；Objective_min=50.61；GitHub push |
| 2026-05-24 | 创建本 AI 过程文档 |
| 2026-05-24 | 解压解析 AUTO_Model2.0.spfx；更新 `00_项目接手总说明.md` 至 Model 2.0 |
| 2026-05-24 | 梳理第七次会议纪要；明确 Real vs DateTime、工序时间记录方案 |
| 2026-05-24 | 初始化 Git；新建 `05_Documentation/`（状态/过程/实验/论文文档） |
| 2026-05-24 | Properties 接入 MLotFactor/SubLotFactor；Scenario Generator 可用 |

---

## 9. AI 助手读取说明

新会话开始时建议优先读：

1. 本文件 §0 速览 + §2 会议清单 + §8 变更日志
2. `00_项目接手总说明.md`（细节）
3. 若涉及模型逻辑 → Architecture 文档
4. 若涉及实验数字 → `v1v2_analysis.json` 或最新 `04_Output/*Results*.csv`

更新本文件时：**只追加变更日志 + 修改对应章节**，不要重复粘贴整份接手文档。
