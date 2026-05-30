# 决策记录（ADR 简版）

记录「选了什么、为什么、替代方案是什么」，便于论文方法章与答辩引用。

---

## D-001：主模型版本

| 项 | 内容 |
|----|------|
| **日期** | 2026-05 |
| **决策** | 以 **AUTO_Model2.0** 为唯一主模型，Model 1.0 归档 |
| **原因** | 2.0 解决 Source 放单、含 Worker/换型、流程与会议讨论一致 |
| **放弃** | 继续在 1.0 上 patch |

---

## D-002：Experiment 主响应 MakeSpan 口径

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-24 |
| **决策** | 暂用 **`Mold_T_End`** 作为 Experiment 的 MakeSpan |
| **原因** | 用户已实现且首次跑通 |
| **待决** | 是否与导师统一为 Sink 整线 Make Span（`LastDepartureTime`） |
| **影响** | 论文中需明确「制程截面」vs「整线完成时间」 |

---

## D-003：Factor 用 Properties 而非 States

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-24 |
| **决策** | `MLotFactor` / `SubLotFactor` 定义为 **Model Properties** |
| **原因** | Simio Experiment Control 只认 Properties；States 无法 Add Control |
| **实现** | Separator 表达式 `× MLotFactor`；Scenario Generator 扫参 |

---

## D-004：目标函数权重

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-23 会议 |
| **决策** | **Objective = 0.7×MakeSpan + 0.3×Penalty**（Experiment 公式以此为准） |
| **备注** | 会议口述曾出现 70% 罚函数说法，与 Experiment 演示不一致，以公式为准 |
| **Penalty** | 延期则大罚值（如 1e7）；全准时为 0 |

---

## D-005：Scenario Generator 参数范围

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-24 |
| **决策** | 首扫 **MLot 0.8～1.2，3 水平**；SubLot 固定 1.0 |
| **原因** | 避免 Min=0；先单因子敏感性再二维 9 场景 |
| **放弃** | 首次即 0～1、5 水平（含 0 无意义） |

---

## D-006：Git 忽略项

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-24 |
| **决策** | 忽略 `*.backup`、`02_Simulation_Model/old/` |
| **原因** | 减小仓库体积；主模型与文档保留 |
| **保留** | `.spfx`、xlsx、`04_Output` 摘要与 JSON |

---

## D-007：SPAN 为主实验数据

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-30 |
| **决策** | 后续 Experiment 默认使用 **`Simio_Import_Data-SPAN.xlsx`** |
| **原因** | 含 Make Span / 交期相关字段；EXP-002 已跑通 26 场景 |

---

## D-008：下一优化 — Source 按交期释放（待实现）

| 项 | 内容 |
|----|------|
| **日期** | 2026-05-30 |
| **问题** | 订单释放顺序未按 DueTime 紧急度 |
| **决策** | Source + 首队列改为 **EDD**（交期差或 DueDate 升序） |
| **验证** | EXP-003 复跑最优因子 (1.0, 0.75)，对比 Penalty |

---

## 待决策

| ID | 问题 | 选项 |
|----|------|------|
| T-001 | 全局 Make Span 定义 | Mold_T_End vs Sink LastDepartureTime |
| T-002 | 负荷校准方式 | 复制订单+改 ReleaseDate vs quantity×N |
| T-003 | 论文主决策变量 | 仅批次因子 vs 含派工规则 |
