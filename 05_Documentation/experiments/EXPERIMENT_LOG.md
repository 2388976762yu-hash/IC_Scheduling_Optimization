# 实验总表

| ID | 日期 | 名称 | 数据 | 场景数 | 主结论 | 详情 |
|----|------|------|------|--------|--------|------|
| EXP-001 | 2026-05-24 | Experiment1 基准 | 原 Tuned V1 | 1 | MakeSpan≈78.4, Penalty=0, 链路跑通 | [EXP-001](records/EXP-001_experiment1_baseline.md) |
| EXP-002 | 2026-05-30 | SPAN 因子全网格 | **Simio_Import_Data-SPAN.xlsx** | 26 | Objective_min=**50.61** (1.0/0.75); Penalty_max=760 | [EXP-002](records/EXP-002_span_factor_grid.md) |

---

## 实验设计约定

| 字段 | 说明 |
|------|------|
| **MakeSpan** | 当前 = `Mold_T_End`（仿真小时） |
| **Penalty** | Model 级累计罚函数 |
| **Objective** | `0.7 * MakeSpan + 0.3 * Penalty`，最小化 |
| **Controls** | `MLotFactor`, `SubLotFactor`（Properties） |
| **Replication** | 确定性模型建议 1；本次 SPAN 网格为 5～10 |

---

## 待运行队列

1. **EXP-003**：Source 按 DueDate/交期差 EDD 释放 → 复跑 SPAN + 最优因子 (1.0, 0.75)
2. EXP-004：ReleaseDate 基准化（若 SPAN 尚未统一）
3. EXP-005：OptQuest 在 MLot∈[0.8,1.2], SubLot∈[0.6,1.0] 寻优

---

## 待优化项（来自 EXP-002）

| 项 | 说明 | 优先级 |
|----|------|--------|
| **订单释放顺序** | 未按 DueTime 紧急度释放；应越紧急越早释放 | **P0** |
| 首队列派工 | Server Selection 改为 EDD | P1 |

---

## 原始输出位置

- CSV 报告：`04_Output/`
- 汇总 JSON：`04_Output/v1v2_analysis.json`
- SPAN 数据：`01_Data/Simio_Import_Data-SPAN.xlsx`
