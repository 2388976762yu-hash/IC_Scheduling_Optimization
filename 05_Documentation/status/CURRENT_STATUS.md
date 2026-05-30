# 当前项目状态

> **最后更新**：2026-05-30  
> **维护**：有重大进展、会议、实验完成后更新本节与待办清单。

---

## 阶段概览

| 项 | 状态 |
|----|------|
| 项目阶段 | SPAN 数据 26 场景因子实验完成 → **待优化 Source 按交期释放** |
| 主模型 | `AUTO_Model2.0.spfx` |
| 主数据 | **`01_Data/Simio_Import_Data-SPAN.xlsx`** |
| 远程仓库 | GitHub `2388976762yu-hash/IC_Scheduling_Optimization` |
| 下一里程碑 | Source EDD 释放 + EXP-003 复测 |

---

## 已完成

- [x] Model 2.0 + Experiment Controls（MLotFactor / SubLotFactor）
- [x] EXP-001 基准跑通
- [x] **EXP-002**：SPAN 数据 26 Scenario 全网格（2026-05-30）
- [x] Git 本地仓库 + `05_Documentation/` 文档体系
- [x] GitHub 远程连接与 push

---

## 进行中 / 待优化（P0）

- [ ] **Source_Orders：按 DueDate / 交期紧迫度释放**（越紧急越早）
  - 现状：释放未考虑 duetime，导致可避免的 Penalty（EXP-002 最高 760）
  - 期望：EDD 或 `(DueDate - ReleaseDate)` 升序
- [ ] 首队列 Server Selection：FIFO → EDD（与 Source 一致）

---

## 待办

| P | 任务 |
|---|------|
| P0 | 实现 Source 紧急度释放 + EXP-003 复跑 (1.0, 0.75) |
| P1 | 确认 MakeSpan 口径（Mold_T_End vs Sink 整线） |
| P2 | OptQuest 在较优因子区间寻优 |
| P3 | 开题报告 |

---

## EXP-002 关键数值（SPAN，2026-05-30）

| 指标 | 最优 | 最差 |
|------|------|------|
| Objective | **50.6132** (MLot=1.0, SubLot=0.75) | 291.181 (1.25/1.25) |
| MakeSpan | 72.3045 | 97.3895 |
| Penalty | 0（多场景） | **760** |

---

## 相关链接

- [EXP-002 详情](../experiments/records/EXP-002_span_factor_grid.md)
- [实验总表](../experiments/EXPERIMENT_LOG.md)
- [变更日志](../process/CHANGELOG.md)
