# 文献综述分条笔记

## 综述线 1：半导体/封装后端排程与派工规则

- **Lin and Chen (2015)**：真实 OSAT 混合流水 + GA + OCBA + lot split/merge → **文件夹主文献，必引**
- **Sang-Jin Lee 与 Tae-Eog Lee（2011）**：MCP 组装线，DA/WB 重入、并行异构机台、换型显著
- **Sang-Jin Lee 与 Tae-Eog Lee（2008）**：WSC 会议版，产能分配策略降低 setup 同时维持 OTD
- **Chiu et al. (2023)**：订单分配 + 灵活拆分，进化仿真优化
- **Chiu et al. (2026)**：后端组装 + DRL + 仿真优化
- **Chen et al. (2013)**：后段组装 PSO+OCBA
- **Hoppe et al. (2025)**：Structured RL，组合动作空间 → **文件夹文献**
- **Luttmann and Xie (2026)**：MACSIM，FFSP/FJSP → **文件夹文献**

**述评要点**：后端组装文献聚焦 MCP/HFSP，但较少同时考虑 Order—MLot—Magazine—SubLot 批次链 + 交期惩罚 + 商业 DES 平台 Experiment。

---

## 综述线 2：批次/子批次拆分与批处理调度

- **Klemmt et al. (2011)**：半导体 oven 批处理，MIP + DES 混合，交期与完工时间 → 仿真与优化结合范式。
- **França et al. (2005)** / lot streaming 经典：子批次加速流动。
- **Potts and Van Wassenhove (1982)**：lot streaming 基础。
- **Akçali et al. (2003)**：仿真评估 batching 启发式，due-date 绩效。
- **王卓君等 (2023)**：晶圆批处理设备，组批+指派，CIMS。

**述评要点**：批次拆分对 WIP/流动时间影响明确，但封装后端 Order—MLot—Magazine—SubLot 批次链与 Experiment 因子扫参结合研究较少。

---

## 综述线 3：离散事件仿真与仿真优化

- **Law (2015)**：DES 方法论经典。
- **Banks et al. (2010)**：DES 教材。
- **Chen-Ritzo et al. (2011)**：半导体制造仿真支持运营决策的工业实践。
- **Chien et al. (2011)**：半导体制造建模分析挑战综述（EJIE 特刊）。
- **Stubbe and Rose (2011)**：小批量与 batch 工具替换的仿真分析。

**述评要点**：Simio 等 DES 适合复杂 Worker/换型/随机故障；仿真优化（Scenario/OptQuest）是管理科学与工程常用路径。

---

## 综述线 4：多目标/交期惩罚排程

- **Pinedo (2016)**：Scheduling Theory，tardiness/max lateness 目标。
- **赵子夜等 (2025)**：半导体封装测试 FFS，多目标含拖期惩罚，CIMS。
- **Fang et al. (2023)**：半导体制造机器调度综述， Sustainability。
- **Panwalkar et al. (1977)**：dispatching rules 综述（EDD、SPT 等）— 年份已更正

**述评要点**：MakeSpan + 延期惩罚的加权标量化适合 Experiment Response；需明确 MakeSpan 统计口径（整线 vs 工序截面）。

---

## 研究缺口（汇总）

1. 面向 **封装后端六工序** 的一体化 DES 模型（含 Worker、换型、Order—MLot—Magazine—SubLot 批次链）与 **企业脱敏 Simio 导入数据** 的结合研究不足。
2. **批次因子**（MLot/SubLot）与 **交期驱动释放/派工** 的联合优化实验较少。
3. 加权多目标（MakeSpan + Penalty）在 Simio Experiment 框架下的 **可复现实验设计** 有待系统化。
