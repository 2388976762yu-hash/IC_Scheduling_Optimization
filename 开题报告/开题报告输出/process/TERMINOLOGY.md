# 开题正文专业术语对照（精校真源）

> 与 [`AUTO_Model2.0_Architecture_Document.md`](../../../02_Simulation_Model/modeldetail/AUTO_Model2.0_Architecture_Document.md) 口径一致。  
> 正文以**中文为主、英文专名保留**，避免机翻式括号堆砌。  
> **`audit_terminology.py` 据此自动审计 `section_content.py`。**

---

## 工序与设备

| 英文/代号 | 正文用语 | 说明 |
|-----------|----------|------|
| D/S | 晶圆切割D/S | Die Saw |
| DA | 粘片DA | Die Attach |
| WB | 焊线WB | Wire Bond |
| Mold | 塑封Mold | — |
| B/G | 键合/研磨B/G | Ball attach / Grind |
| Taping | 贴带包装Taping | — |
| Server | 工序站Server | Simio 加工站，非 IT「服务器」 |
| Sink | 汇点Sink | 产线终点 |
| Worker | 搬运工Worker | 跨工序物流 |

## 生产与调度

| 英文 | 正文用语 | 说明 |
|------|----------|------|
| OSAT | 外包封装测试OSAT | Outsourced Semiconductor Assembly and Test |
| MTO | 按单生产MTO | Make-to-Order |
| HFS | 混合流水车间HFS | 产线结构（Hybrid Flow Shop） |
| HFSP | 混合流水车间调度问题HFSP | 调度问题（Hybrid Flow Shop Problem） |
| WIP | 在制品WIP | **禁止**写「WIP在制品」 |
| MakeSpan | 制造周期MakeSpan | **禁止**用「完工时间」指 MakeSpan |
| Flow Time | 流动时间Flow Time | — |
| UPH | 单位小时产能UPH | Units Per Hour |
| EDD | 最早交期先出规则EDD | Earliest Due Date |
| FIFO | 先进先出规则FIFO | — |
| OCBA | 最优计算预算分配OCBA | — |
| SO | 仿真优化SO | Simulation Optimization |
| GA / PSO | 遗传算法GA / 粒子群优化PSO | — |
| 元启发式 | 元启发式算法 | **禁止**裸写 metaheuristic |

## 换型 / 搬运 / Setup（重要）

| 英文 | 正文用语 | **不是** |
|------|----------|----------|
| Changeover | 换型 | 总称，不等于 Setup 一词 |
| Transfer In/Out | 批次**搬运**（转入/转出） | 各 **3 分钟/批**，固定发生 |
| Setup Time | **换型Setup** 10 分钟 | **不是**「设置」；物料 Group 变化时触发 |

**推荐整句（DA/WB）**：

> DA/WB每批转入与转出搬运各3分钟；当前后批次物料Group不同时，触发10分钟换型Setup。

**禁止写法**：「换型含搬运3分钟与设置10分钟」「含搬运换型」「Worker/换型约束」

## 批次结构

| 英文 | 正文用语 | 说明 |
|------|----------|------|
| Order | 订单Order | 计划释放单元，Orders 表一行 |
| MLot | 制造批次MLot | Separator 链第一级 |
| Magazine | **弹夹批次Magazine** | 载体/弹夹单元；**不是**「杂志批次」 |
| SubLot | 子批次SubLot | 最小加工单元 |
| 批次链 | Order→MLot→Magazine→SubLot | 仿真四层结构 |
| MLotFactor / SubLotFactor | 批次缩放因子MLotFactor、SubLotFactor | Model Properties |
| Separator / Combiner | Separator/Combiner拆分合并逻辑 | 正文避免 `Separator_MLot` 等内部对象名 |
| BOM | 物料清单BOM | — |
| lot streaming | 批次流lot streaming | 文献专名可保留 |

## 仿真与实验

| 英文 | 正文用语 | 说明 |
|------|----------|------|
| DES | 离散事件仿真DES | — |
| Experiment | Simio Experiment | 实验模块 |
| Scenario Generator | Scenario Generator情景生成器 | — |
| Model Properties | 模型属性Model Properties | — |
| Primary Response | 主响应变量Primary Response | — |
| Response | 响应变量Response | 复数 Responses 同义 |
| Replications | 重复运行Replications | — |
| Source | 订单源Source | 订单释放 |
| Server Selection Rule | 设备队列派工规则 | — |
| Penalty | 延期惩罚Penalty | 本研究阈值式设计 |
| Objective | 综合目标函数Objective | 0.7×MakeSpan+0.3×Penalty |
| Mold_T_End | Mold工序截面时刻Mold_T_End | 过渡口径 |
| LastDepartureTime | Sink整线LastDepartureTime | 全局制造周期主口径 |
| OptQuest | OptQuest仿真优化器 | — |
| Common Random Numbers | 公共随机数Common Random Numbers | 方差缩减 |
| 性能评估 oracle | **仿真性能评估器** | **禁止**裸写 oracle |

## 数据与脱敏

| 内部 | 正文用语 |
|------|----------|
| Simio_Import_Data-SPAN.xlsx | **企业脱敏 Simio 导入数据** |
| AUTO_Model* | **六工序Simio模型**（不写内部文件名） |
| Source_Orders | **订单源Source**释放逻辑 |

Orders/Materials/MachineConfig 字段见 Architecture 与 Excel 真源。

## 目标与绩效表述

| 概念 | 正文 | 文献引用时可写 |
|------|------|----------------|
| 准交 | 准交 | — |
| 延期 | 延期惩罚Penalty | — |
| tardiness 文献 | — | 拖期惩罚（引用他人工作时） |
| 瓶颈 | 瓶颈工序 | 「喂料不足伪瓶颈」表低负荷 |

## 开题时态

| 章节 | 写什么 | 不写什么 |
|------|--------|----------|
| §1.3 研究场景 | 企业脱敏**原数据字段**、**拟**开展实验 | 已跑 Objective/MakeSpan 最优值 |
| §1 意义/综述 | 文献缺口、**预期**贡献 | 具体实验数字 |
| §2 实验方案/可行性 | 未来步骤、条件具备 | 用实验最优值证明可行 |
| §3 研究基础 | 模型框架、**阶段性标定实验与数值**（简要） | 学位论文结论口吻 |
| 全文 | 客观表述 | **「导师……」**句式 |

## 文风禁写（机翻痕迹）

| 禁止 | 改用 |
|------|------|
| what-if | 情景假设分析 |
| metaheuristic | 元启发式算法 |
| oracle | 仿真性能评估器 |
| EXP-xxx / D-xxx | 中文实验名或删除 |
| 杂志批次 | 弹夹批次Magazine |
