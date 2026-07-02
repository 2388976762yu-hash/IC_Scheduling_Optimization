# PPT / Word 手动同步 — 全文复制版

> 工序唯一顺序：**Taping → BG → DS → DA → WB → MOLD**  
> 设备台数：**Taping 8、BG 17、DS 31、DA 112、WB 284、MOLD 7，合计 459**  
> 下面每段 **改后** 可直接全选复制进 PPT/Word，覆盖原段落。

---

# 一、PPT 全文替换

## 第 2 页｜选题背景 — 改后全文

半导体制造可划分为前道晶圆制造与后道封装测试两大环节。后道封装测试承担贴带包装、键合研磨、晶圆切割、粘片、焊线及塑封等工序，是连接芯片设计与终端应用的关键环节。在全球分工深化背景下，外包封测企业普遍采用按单生产模式，同时处理多品种、小批量、短交期 Order，排程决策直接影响 MakeSpan、Order 准交率、在制品水平及设备利用率。

存储类半导体封装后端具有多品种混线、并行 Server 规模大、Setup 频繁、Order 至 SubLot 批次结构复杂等特征。典型产线可抽象为六工序串联流程，即 Taping、BG、DS、DA、WB、MOLD。企业与 Simio 数据按此 Station 顺序统一编号。该结构属于混合流水车间调度问题，各阶段按固定 Station 顺序流转，阶段内部配置多台并行异构 Server。DA 与 WB 工序 Server 数量多，MLot 与 SubLot 批次搬运及 Setup 时间开销显著，常构成产能约束与调度热点。

本研究数据来源于典型存储类半导体封装企业提供的已脱敏 Simio 导入数据，对应实际一周排产样本的原生字段。计划人员在排程实践中需同时权衡系统层面 MakeSpan 最小化与 Order 层面准交绩效最大化，两类目标存在结构性张力，难以通过单一解析模型完整刻画系统动态。

---

## 第 8 页｜Simio 模型与数据 — 改后全文

企业脱敏 Simio 导入数据包含 Orders 表 41 个 Order、Materials 表 16 种 Material。六类 Station 按企业与模型统一顺序为 Taping 八台、BG 十七台、DS 三十一台、DA 一百一十二台、WB 二百八十四台、MOLD 七台，合计 459 台 Server。Orders 字段涵盖 OrderNumber、MaterialFK、OrderQty、ReleaseDate、DueDate 等。Materials 字段涵盖 DiesPerUnit、StripsPerMag、QtyPerMag、QtyPerSubLot 等批次拆分参数及各工序 UPH。UPH 列顺序为 UPH_Taping、UPH_BG、UPH_DS、UPH_DA、UPH_WB、UPH_Mold，与 MachineConfig 行序一致。

Simio 模型中，Order 为计划释放单元，自 Source_Orders 释放后，经 Separator 链依次形成 MLot、Magazine 与 SubLot，实体沿 Taping、BG、DS、DA、WB、MOLD 六类 Server 顺序流转后进入 Sink。DA 与 WB 每批 Transfer In 与 Transfer Out 各三分钟，Assigned_DA_Group 变化时触发十分钟 Setup。Experiment 已定义 MakeSpan、Penalty 与 Objective 三个 Response，当前 MakeSpan 暂以 MOLD 工序截面 Mold_T_End 记录。MLotFactor 与 SubLotFactor 作为 Model Properties 接入 Scenario Generator。

---

## 第 10 页｜Baseline 结果 — 改后全文

Baseline Scenario 下，MLotFactor 与 SubLotFactor 均为 1.0，Ending Time 为一百小时，41 个 Order 均可依次经 Taping、BG、DS、DA、WB、MOLD 六类 Server 完整流转，表明 Simio 主流程与 Experiment 状态变量读取链路验证通过。

Baseline 结果为 MakeSpan 七十八点四零，Penalty 零，Objective 五十四点八八。Objective 等于零点七乘以 MakeSpan，与手动验算一致。Baseline 下 Penalty 为零，可能与 DueDate 约束尚较宽松或 ReleaseDate 尚未完全基准化有关，该问题已纳入后续工作计划，不影响 Baseline 作为后续 Scenario 对比参照的功能。

---

## PPT 全文 Ctrl+H 批量替换

| 查找内容 | 替换为 |
|----------|--------|
| D/S、DA、WB、Mold、B/G、Taping | Taping、BG、DS、DA、WB、MOLD |
| D/S→DA→WB→Mold→B/G→Taping | Taping→BG→DS→DA→WB→MOLD |
| 晶圆切割、粘片、焊线、塑封、键合研磨及贴带包装 | 贴带包装、键合研磨、晶圆切割、粘片、焊线及塑封 |
| D/S 31 台、DA 112 台、WB 284 台、Mold 7 台、B/G 17 台、Taping 8 台 | Taping 8 台、BG 17 台、DS 31 台、DA 112 台、WB 284 台、MOLD 7 台 |
| 编带、分拣、装片、键合、塑封、烘烤及切筋 | Taping、BG、DS、DA、WB、MOLD |

---

# 二、Word：中期考核表摘要 — 改后全文

本研究面向典型存储类半导体封装后端产线调度优化问题，以企业脱敏 Simio 导入数据为基准，建立涵盖 Taping、BG、D/S、DA、WB、MOLD 六工序的离散事件仿真模型，完整纳入订单释放、Order—MLot—Magazine—SubLot 多级批次链、Worker 搬运输送及 DA/WB 工序换型 Setup 等关键约束。研究采用 MakeSpan 与准交惩罚 Penalty 双指标，构建加权 Objective=0.7×MakeSpan+0.3×Penalty 评价函数，并通过 Experiment 接入 MLotFactor、SubLotFactor 情景生成器开展系统参数扫描。已完成基准情景验证与 26 组批次因子全因子网格实验，基准 MakeSpan 为 78.40，网格扫描 Objective 最优 50.61；另有释放顺序对照实验表明，释放逻辑须与 Source 层交期驱动释放机制协同设计。当前正推进负荷校准、MakeSpan 统计口径统一、Source 层 EDD 释放与队列派工规则对比及与 FIFO 基线对照，为后续学位论文系统实验与正式论文撰写奠定基础。

---

# 三、Word：中期报告 §1.2 — 改后全文

已建立涵盖 Taping→BG→D/S→DA→WB→MOLD 六工序的 Simio 模型，并与企业脱敏 Simio 导入数据绑定：Orders 表 41 条订单、Materials 表 16 种物料、MachineConfig 合计 459 台 Server，按 Station 顺序为 Taping 8 台、B/G 17 台、D/S 31 台、DA 112 台、WB 284 台、MOLD 7 台。加工时间按 CurrentQty/UPH 计算；DA/WB 每批转入与转出搬运各 3 分钟，Assigned_DA_Group 变化时触发 10 分钟换型 Setup。订单 Order 经 Separator 链依次形成制造批次 MLot、弹夹批次 Magazine 与子批次 SubLot，并纳入 Worker 搬运逻辑。Experiment 已定义 MakeSpan、Penalty 与 Objective=0.7×MakeSpan+0.3×Penalty 三个 Response；MLotFactor、SubLotFactor 作为 Model Properties 接入 Scenario Generator。

---

# 四、Word：开题报告 — 改后全文片段

## 4.1 §1.1 产业背景 — 改后一句

后道封装测试OSAT承担贴带包装、键合研磨、晶圆切割、粘片、焊线及塑封等工序，是连接芯片设计与终端应用的关键枢纽。

## 4.2 §1.1 六工序定义 — 改后整段

存储类半导体封装后端具有多品种混线、并行设备规模大、换型频繁、批次结构复杂等特点。典型产线可抽象为六工序串联流程：Taping→BG→D/S→DA→WB→MOLD。该结构在运筹学上属于混合流水车间HFS：各阶段按企业与Simio数据统一的Station顺序流转，阶段内部配置多台并行异构Server。DA与WB工序Server数量多、批次搬运与换型Setup开销显著，常成为产能约束与调度热点；MOLD等工序在特定负荷条件下亦可能形成瓶颈。与理想化流水车间不同，封装后端同时存在订单到达随机性、批次拆分与合并、跨工序Worker搬运、序列相关换型Setup时间以及多级WIP等离散事件特征，使得纯解析优化模型难以完整刻画系统动态。Jain和Meeran（1999）对作业车间调度的长期回顾表明，真实生产环境中的资源异构、工序顺序与动态到达使NP-hard问题更加复杂；Stubbe和Rose（2011）的仿真研究亦说明，小批量与批处理设备替换会显著改变系统绩效。

## 4.3 §1.3 MachineConfig 台数 — 改后整句

MachineConfig 工作表给出六工序工序站 Server 台数，合计 459 台，即 Taping 8 台、B/G 17 台、D/S 31 台、DA 112 台、WB 284 台、MOLD 7 台。

## 4.4 §2 文献综述 MakeSpan 口径 — 改后整句

两种口径在末道MOLD工序截面与Sink整线完工程度之间可能产生差异。

## 4.5 §3 仿真模型建设 — 改后整段

第一，仿真模型建设。已搭建六工序 Simio 模型框架，涵盖 Taping→BG→D/S→DA→WB→MOLD 主流程、订单 Order 经 Separator 链形成 MLot→Magazine→SubLot 批次结构、Worker 搬运及 DA/WB 换型 Setup。设备规模与 MachineConfig 一致：Taping 8 台、B/G 17 台、D/S 31 台、DA 112 台、WB 284 台、MOLD 7 台，合计 459 台。各工序站 Server 加工时间按 CurrentQty 与 Materials 表 UPH 计算，DA/WB 每批转入与转出搬运各 3 分钟，Assigned_DA_Group 变化时触发 10 分钟换型 Setup。

---

# 五、改完自检

- Ctrl+F 搜 `D/S→`、`编带、分拣`、`Mold、B/G、Taping`，应为 0 处
- 工序顺序全文仅 **Taping → BG → DS → DA → WB → MOLD** 一套
- 勿运行 fill_template.py / fill_midterm.py
