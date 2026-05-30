# 论文撰写素材

随研究进展积累，正式写作时从这里提取。

---

## 拟定题目方向

**考虑交期约束与批次拆分的 IC 后端制造生产排程仿真优化研究**

（备选：多目标优化的集成电路后端制造生产排程）

---

## 摘要要点（待充实）

- **背景**：后端六工序、DA/WB 为关键资源、批次拆分影响 WIP 与 Make Span
- **方法**：Simio 离散事件仿真 + Experiment / 多场景对比
- **决策变量**：M Lot / Sub Lot 批次因子（Properties）；后续派工规则
- **目标**：Make Span 最小化 + 延期惩罚最小化
- **数据**：SanDisk 41 单基准（一周工作量）

---

## 第 1 章 绪论 — 素材

- 半导体后端流程：DS → DA → WB → Mold → BG → Taping
- 排程问题：交期、换型、批次、设备分配
- 仿真 vs 纯数学模型：考虑 Worker、换型、拆分合并

---

## 第 3 章 模型 — 素材

- 引用：`02_Simulation_Model/modeldetail/AUTO_Model2.0_Architecture_Document.md`
- 加工时间：`CurrentQty / UPH`
- DA/WB：Transfer 3min + Setup 10min
- 批次三级：MLot → Mag → SubLot → Combiner

---

## 第 4 章 实验 — 素材

| 实验 | 内容 | 文档 |
|------|------|------|
| EXP-001 | Experiment 基准 | [EXP-001](../experiments/records/EXP-001_experiment1_baseline.md) |
| EXP-002 | MLot 敏感性 | 待跑 |

### 可写对比维度

1. MLotFactor / SubLotFactor 水平
2. 派工：FIFO vs EDD（DueDate−ReleaseDate）
3. 是否换型 / 故障（后续）

---

## 图表清单（计划）

- [ ] 工艺流程图（Model 2.0 主流程）
- [ ] MakeSpan vs MLotFactor 折线/柱状
- [ ] Objective vs 因子组合热力图（9 场景）
- [ ] 各工序利用率（注明 Simio 报告口径）

---

## 参考文献线索

- `项目辅助材料/参考资料/` 内 PDF
- 导师提供 FlexSim 论文（方法对照）

---

## 待导师/业务确认后写入论文

- Quantity per magazine = 480 含义
- M Lot / Sub Lot 与产线一致性
- 利用率计算口径
