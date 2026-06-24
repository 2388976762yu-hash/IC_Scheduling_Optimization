# 当前项目状态

> **最后更新**：2026-05-30（EXP-003 完成后）

---

## 阶段概览

| 项 | 状态 |
|----|------|
| 项目阶段 | EXP-003 完成 → 待 DueDate **升序** + Source EDD |
| 主模型 | **`AUTO_Model3.0-batchfactors.spfx`** |
| 主数据 | `01_Data/Simio_Import_Data-SPAN.xlsx` |
| GitHub | `2388976762yu-hash/IC_Scheduling_Optimization` |

---

## 最新实验 EXP-003（2026-05-30）

| 指标 | 结果 | vs EXP-002 |
|------|------|------------|
| Objective_min | **52.38** (0.75/0.5) | 50.61 → 略差 |
| Penalty_max | **700** | 760 → 略好 |
| MakeSpan 范围 | 74.82～89.97 | — |
| 变更 | Orders **DueDate 降序** | — |

---

## 已完成

- [x] EXP-001 / EXP-002 / **EXP-003**
- [x] Git + GitHub push

---

## 待办（P0）

- [ ] **EXP-004**：DueDate **升序**（交期最早在前）复跑
- [ ] Source_Orders 确认是否按表序释放；Server 队列改 EDD
- [ ] 澄清降序 vs 升序对 Penalty 的影响

---

## 相关链接

- [EXP-003](../experiments/records/EXP-003_duedate_desc_release_grid.md)
- [实验总表](../experiments/EXPERIMENT_LOG.md)
