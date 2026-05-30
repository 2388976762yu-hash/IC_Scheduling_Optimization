# EXP-002：SPAN 数据批次因子全网格 Experiment

| 项 | 值 |
|----|-----|
| **实验 ID** | EXP-002 |
| **日期** | 2026-05-30 |
| **模型** | AUTO_Model2.0.spfx |
| **Experiment** | Experiment1 |
| **数据** | `01_Data/Simio_Import_Data-SPAN.xlsx` |
| **目的** | MLotFactor × SubLotFactor 网格扫描；Penalty 在 SPAN 交期下是否触发 |

---

## 设置

| 参数 | 值 |
|------|-----|
| Ending | 100 Hours |
| Warm-up | 0 |
| Replications | Scenario1: 10；其余 Scenario: 5 |
| Primary Response | Objective |
| Controls | `MLotFactor`, `SubLotFactor`（Properties） |
| Scenario 数 | **26**（Scenario Generator 全组合） |
| 订单 | 41（Table Bindings: Materials / Orders / MachineConfig / SetupConfig） |
| 总运行时间 | ~2493 s（约 41 min） |

### 因子水平（约）

MLotFactor / SubLotFactor 组合涵盖 **0.5、0.8、1.0、1.25、1.3、1.5** 等（Scenario 命名如 `0.5_0.5`、`1.0_0.75`、`1.25_1.25`）。

---

## Response 定义

| Response | 表达式 |
|----------|--------|
| MakeSpan | `Mold_T_End` |
| Penalty | `Penalty` |
| Objective | `0.7 * MakeSpan + 0.3 * Penalty` |

---

## 主要结果（摘要）

| 指标 | 最优 Scenario | 数值 | 最差 Scenario | 数值 |
|------|---------------|------|---------------|------|
| **Objective** | **1.0_0.75** | **50.6132** | 1.25_1.25 | 291.181 |
| MakeSpan | 1.0_0.75 | **72.3045** | 1.0_1.5 | 97.3895 |
| Penalty | 多个 | 0 | 1.25_1.25 / 1.25_1.5 | **760** |

### 观察

1. **Penalty 不再全 0**：SPAN 数据下部分因子组合出现高 Penalty（最高 760），Objective 受罚函数显著拉动。
2. **MakeSpan 与 Penalty 存在权衡**：低 MakeSpan 场景（如 1.0_0.75）Objective 最优；高因子组合（1.25×1.25）MakeSpan 与 Penalty 双高。
3. **当前较优因子区间（初判）**：MLot≈1.0，SubLot≈0.75～1.0。

---

## 待优化项（P0）

### 订单释放未按交期紧急程度排序

**现象**：`Source_Orders` 释放顺序未按 DueDate / 交期紧迫度排列，导致本可避免的延期（Penalty）。

**期望**（第七次会议一致）：

- 41 单作为「已有订单池」，应**越紧急越早释放 / 越早进入系统**
- 排序依据：`DueDate - ReleaseDate` 升序，或 DueDate 升序（EDD）
- **不是** Priority 字段的泛泛优先级，而是**交期约束**

**建议改动**：

1. **Source_Orders**：到达/释放顺序改为按交期差或 DueDate 排序
2. 首队列 Server：**Selection Rule** 改为 EDD（与 Source 一致）
3. 改完后复跑 EXP-002 最优因子附近 Scenario，对比 Penalty 是否下降

---

## 结论

1. SPAN 数据集 + 批次因子网格实验已完成，Experiment 链路可用于论文对比表。
2. 最优 Objective ≈ **50.61**（MLot=1.0, SubLot=0.75），优于 EXP-001 基准（~54.88）。
3. **下一优化重点**：Source 按 DueTime 紧急度释放订单，而非当前 FIFO/无序释放。

---

## 原始文件

- 数据：`01_Data/Simio_Import_Data-SPAN.xlsx`
- Simio Experiment1 结果表（本地，2026/5/30 导出）

---

## 论文可用表述（草稿）

> 在 SPAN 基准数据下，对 MLotFactor 与 SubLotFactor 进行 26 组全因子实验。当 SubLotFactor=0.75、MLotFactor=1.0 时，综合目标函数最小（50.61）。部分因子组合出现最高 760 的延期惩罚，表明在当前 Source 释放逻辑下交期约束未被充分满足。后续将通过 EDD 释放规则优化订单入流顺序。
