# EXP-001：Experiment1 基准验证

| 项 | 值 |
|----|-----|
| **实验 ID** | EXP-001 |
| **日期** | 2026-05-24 |
| **模型** | AUTO_Model2.0.spfx |
| **Experiment** | Experiment1 |
| **目的** | 验证 MakeSpan / Penalty / Objective 链路 |

---

## 设置

| 参数 | 值 |
|------|-----|
| Ending | 80 Hours（后改为 100h 测试） |
| Replications | 10 |
| Warm-up | 0 |
| Primary Response | Objective |
| MLotFactor | 1.0 |
| SubLotFactor | 1.0 |
| 订单 | 41（Table Bindings: 41 Orders） |

---

## Response 定义

| Response | 表达式 |
|----------|--------|
| MakeSpan | `Mold_T_End` |
| Penalty | `Penalty` |
| Objective | `0.7 * MakeSpan + 0.3 * Penalty` |

---

## 结果

| 指标 | Scenario1 | 备注 |
|------|-----------|------|
| MakeSpan | **78.4002** | 最后一单离开 Mold 时刻 |
| Penalty | **0** | 无延期罚记录 |
| Objective | **54.8802** | = 0.7 × 78.4 |
| 运行时间 | ~164 s | 10 replications |

---

## 结论

1. Experiment 能正确读取 Model 状态变量
2. Objective 公式与手动计算一致
3. Penalty=0 可能因交期仍松或未基准化 ReleaseDate
4. MakeSpan 接近 Ending 上限时需关注是否截断

---

## 原始文件

- `04_Output/V2-ResultsViewSampleReport.csv`（若同次运行）
- Simio Experiment 结果表（本地）

---

## 下一步

- 接入 Properties Controls 后做 EXP-002 MLot 扫描
- 考虑增加 Sink `LastDepartureTime` 对比整线 Make Span
