# 实验总表

| ID | 日期 | 名称 | 数据 / 变更 | 场景数 | 主结论 | 详情 |
|----|------|------|-------------|--------|--------|------|
| EXP-001 | 2026-05-24 | Experiment1 基准 | 原 Tuned V1 | 1 | MakeSpan≈78.4, Penalty=0 | [EXP-001](records/EXP-001_experiment1_baseline.md) |
| EXP-002 | 2026-05-30 | SPAN 因子全网格 | SPAN，原 Orders 序 | 26 | Obj_min=**50.61** (1.0/0.75); Pen_max=760 | [EXP-002](records/EXP-002_span_factor_grid.md) |
| EXP-003 | 2026-05-30 | SPAN + DueDate降序 | SPAN，**Orders DueDate↓** | 26 | Obj_min=**52.38** (0.75/0.5); Pen_max=**700** | [EXP-003](records/EXP-003_duedate_desc_release_grid.md) |

---

## 实验设计约定

| 字段 | 说明 |
|------|------|
| **MakeSpan** | `Mold_T_End`（仿真小时） |
| **Penalty** | Model 级累计罚函数 |
| **Objective** | `0.7 * MakeSpan + 0.3 * Penalty`，最小化 |
| **Controls** | `MLotFactor`, `SubLotFactor` |
| **主模型（最新）** | `AUTO_Model3.0-batchfactors.spfx` |

---

## 待运行队列

1. **EXP-004**：Orders 按 DueDate **升序** + Source/队列 EDD 验证
2. EXP-005：OptQuest 在较优因子区间（0.75～1.0, 0.5～0.75）寻优

---

## 待优化项

| 项 | 状态 | 说明 |
|----|------|------|
| 订单释放顺序 | EXP-003 已试降序，改善有限 | 建议改 **升序** + Source 逻辑 |
| 首队列 EDD | 待做 | Server Selection |

---

## 原始输出

- 数据：`01_Data/Simio_Import_Data-SPAN.xlsx`
- Simio Experiment1 结果表（2026-05-30 本地）
