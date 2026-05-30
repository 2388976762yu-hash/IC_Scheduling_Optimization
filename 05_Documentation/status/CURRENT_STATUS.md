# 当前项目状态

> **最后更新**：2026-05-24  
> **维护**：有重大进展、会议、实验完成后更新本节与待办清单。

---

## 阶段概览

| 项 | 状态 |
|----|------|
| 项目阶段 | Model 2.0 已跑通 → Experiment 已接入 → 批次因子实验进行中 |
| 主模型 | `AUTO_Model2.0.spfx` |
| 最新会议 | 第七次（2026/5/23） |
| 下一里程碑 | MLotFactor 敏感性实验 + ReleaseDate 基准化 |

---

## 已完成

- [x] Model 2.0 六工序 + Worker + 批次拆分/合并
- [x] 各工序 `T_Start` / `T_End` 记录（Real 状态变量）
- [x] `Penalty` 及对应逻辑
- [x] Experiment1：MakeSpan / Penalty / Objective 三个 Response
- [x] Properties：`MLotFactor`、`SubLotFactor` + Experiment Controls
- [x] Scenario Generator 可用
- [x] Experiment 首次跑通（基准 Scenario1）

---

## 进行中

- [ ] Scenario Generator：MLot 0.8 / 1.0 / 1.2 三档对比（SubLot 固定 1.0）
- [ ] Separator 确认已使用 `× MLotFactor` / `× SubLotFactor`
- [ ] ReleaseDate 统一基准日 + 保留 DueDate 交期差
- [ ] 派工：按 (DueDate − ReleaseDate) 升序，替代 FIFO

---

## 待办（按优先级）

| P | 任务 | 负责层 |
|---|------|--------|
| P0 | ReleaseDate / DueDate 基准化脚本或 Excel | 数据 |
| P0 | 确认 MakeSpan 用 Mold_T_End 还是 Sink 整线时间 | 模型 + 论文口径 |
| P1 | MLot / SubLot 敏感性实验（3～9 Scenario） | Experiment |
| P1 | Penalty 在基准化日期后是否仍全 0 | 验证 |
| P2 | OptQuest 在较优 Factor 区间内寻优 | Experiment |
| P2 | 中芯国际同学校 batch / magazine 数据口径 | 外部 |
| P3 | 开题报告 20 页 | 文档 |

---

## 阻塞 / 风险

| 项 | 说明 |
|----|------|
| 数据口径 | QtyPerMLot 小数、Quantity per magazine 480 vs 960 待确认 |
| 机器预分配 | 拆分后 entity 指定机台 — 导师查技术方案 |
| 利用率 | Simio 报告含空等；论文主指标暂以 MakeSpan + Penalty 为主 |
| Scenario Generator Min=0 | 会导致批次为 0，应用 0.8～1.2 |

---

## 关键数值（最新基准）

| 指标 | 值 | 条件 |
|------|-----|------|
| MakeSpan | 78.40 → 81.10（略有波动） | Mold_T_End，Ending 80～100h |
| Penalty | 0 | 41 单 |
| Objective | ≈ 0.7×MakeSpan | Penalty=0 时 |
| 订单完成 | 41/41 | V1 基准 |

---

## 沟通节奏

- 与导师：**周六晚 8 点**（暂定）

---

## 相关链接

- [实验总表](../experiments/EXPERIMENT_LOG.md)
- [变更日志](../process/CHANGELOG.md)
- [决策记录](../process/DECISIONS.md)
- [接手总说明](../../项目辅助材料/00_项目接手总说明.md)
