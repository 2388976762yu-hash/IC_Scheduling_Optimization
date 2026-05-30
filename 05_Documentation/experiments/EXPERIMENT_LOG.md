# 实验总表

| ID | 日期 | 名称 | 模型 | 场景数 | 主结论 | 详情 |
|----|------|------|------|--------|--------|------|
| EXP-001 | 2026-05-24 | Experiment1 基准 | AUTO_Model2.0 | 1 | MakeSpan≈78.4, Penalty=0, 链路跑通 | [records/EXP-001](records/EXP-001_experiment1_baseline.md) |
| EXP-002 | （待跑） | MLot 敏感性 0.8/1.0/1.2 | AUTO_Model2.0 | 3 | — | — |

---

## 实验设计约定

| 字段 | 说明 |
|------|------|
| **MakeSpan** | 当前 = `Mold_T_End`（仿真小时） |
| **Penalty** | Model 级累计罚函数 |
| **Objective** | `0.7 * MakeSpan + 0.3 * Penalty`，最小化 |
| **Controls** | `MLotFactor`, `SubLotFactor`（Properties） |
| **Replication** | 确定性模型建议 1；有随机再 10+ |

---

## 待运行队列

1. EXP-002：MLotFactor ∈ {0.8, 1.0, 1.2}，SubLotFactor=1.0
2. EXP-003：SubLotFactor ∈ {0.8, 1.0, 1.2}，MLotFactor=1.0
3. EXP-004：ReleaseDate 基准化后 Penalty 复测
4. EXP-005：3×3 因子全组合（可选）

---

## 原始输出位置

- CSV 报告：`04_Output/`
- 汇总 JSON：`04_Output/v1v2_analysis.json`
