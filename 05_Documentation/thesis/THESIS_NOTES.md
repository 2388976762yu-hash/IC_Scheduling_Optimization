# 论文撰写素材

随研究进展积累，正式写作时从这里提取。

---

## 开题报告（已撰写 — 2026-06-24 重大修订）

| 项 | 内容 |
|----|------|
| **题目（锁定）** | **多目标优化的半导体后端制造生产排程研究** |
| **Word 提交版** | [02_开题报告_提交版.doc](../../开题报告/开题报告输出/02_开题报告_提交版.doc)（**学院表格填表版**） |
| **docx 副本** | [02_开题报告_提交版.docx](../../开题报告/开题报告输出/02_开题报告_提交版.docx) |
| **格式规范** | [process/FORMAT_SPEC.md](../../开题报告/开题报告输出/process/FORMAT_SPEC.md) |
| 正文真源 | [process/section_content.py](../../开题报告/开题报告输出/process/section_content.py) |
| 结构说明 | [01_开题报告正文.md](../../开题报告/开题报告输出/01_开题报告正文.md) |
| **索引** | [开题报告/开题报告输出/00_INDEX.md](../../开题报告/开题报告输出/00_INDEX.md) |
| **文献真源** | [process/BIBLIOGRAPHY.yaml](../../开题报告/开题报告输出/process/BIBLIOGRAPHY.yaml)（**32 篇**） |
| **文献核实** | [process/REFERENCE_VERIFICATION.md](../../开题报告/开题报告输出/process/REFERENCE_VERIFICATION.md) |
| **脱敏** | 正文不含企业/品牌名；见 [ANONYMIZATION.md](../../开题报告/开题报告输出/process/ANONYMIZATION.md) |
| **重新生成** | `cd 开题报告/开题报告输出/process && python fill_template.py` |

---

## 拟定题目方向

**多目标优化的半导体后端制造生产排程研究**

（学位论文可与开题题目保持一致或微调）

---

## 摘要要点（待充实）

- **背景**：封装后端六工序、DA/WB 为关键资源、批次拆分影响 WIP 与 Make Span
- **方法**：Simio 离散事件仿真 + Experiment / 多场景对比
- **决策变量**：M Lot / Sub Lot 批次因子（Properties）；后续派工规则
- **目标**：Make Span 最小化 + 延期惩罚最小化（Objective = 0.7×MakeSpan + 0.3×Penalty）
- **数据**：行业脱敏订单 41 单基准（一周工作量）

---

## 第 1 章 绪论 — 素材

- 半导体后端流程：DS → DA → WB → Mold → BG → Taping
- 排程问题：交期、换型、批次、设备分配
- 仿真 vs 纯数学模型：考虑 Worker、换型、拆分合并
- 文献综述四线：见 [LITERATURE_REVIEW_NOTES.md](../../开题报告/开题报告输出/process/LITERATURE_REVIEW_NOTES.md)

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
| EXP-002 | 26 场景因子网格 | [EXP-002](../experiments/records/EXP-002_span_factor_grid.md) |
| EXP-003 | DueDate 降序复跑 | [EXP-003](../experiments/records/EXP-003_duedate_desc_release_grid.md) |

### 可写对比维度

1. MLotFactor / SubLotFactor 水平
2. 派工：FIFO vs EDD（DueDate−ReleaseDate）
3. 是否换型 / 故障（后续）

---

## 图表清单（计划）

- [ ] 工艺流程图（Model 2.0 主流程）
- [ ] MakeSpan vs MLotFactor 折线/柱状
- [ ] Objective vs 因子组合热力图（26 场景）
- [ ] 各工序利用率（注明 Simio 报告口径）

---

## 参考文献

- 开题报告已录入 28 篇：见 [BIBLIOGRAPHY.yaml](../../开题报告/开题报告输出/process/BIBLIOGRAPHY.yaml)
- 正文引用格式：著者-出版年（如 Klemmt et al. (2011)）

---

## 待导师/业务确认后写入论文

- Quantity per magazine = 480 含义
- M Lot / Sub Lot 与产线一致性
- 利用率计算口径
- MakeSpan 全局口径（Mold_T_End vs Sink）
