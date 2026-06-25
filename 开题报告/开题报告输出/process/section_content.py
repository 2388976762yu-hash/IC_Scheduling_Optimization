# -*- coding: utf-8 -*-
"""开题报告 SECTION1/2/3 正文（不含参考文献列表，列表由 fill_template 从 BIBLIOGRAPHY.yaml 生成）

写作策略真源：WRITING_RULES.md。术语真源：TERMINOLOGY.md。勿写表头字段 — 见 METADATA_POLICY.md。
排版：标题与正文之间、段与段之间均**不要空行**（见 FORMAT_SPEC §段落排版）。
"""


def _compact_spacing(text: str) -> str:
    """Remove blank lines so Word does not insert empty paragraphs between headings/body."""
    return "\n".join(line for line in text.splitlines() if line.strip())


SECTION1_BODY = _compact_spacing(r"""1. 论文选题的背景

1.1 产业环境与问题提出

半导体产业是国民经济与国家安全的重要支柱，其制造链条可概括为前道晶圆制造与后道封装测试两大环节。后道封装测试OSAT承担晶圆切割、粘片、键合、塑封、研磨及贴带包装等工序，是连接芯片设计与终端应用的关键枢纽。全球半导体分工深化以来，OSAT企业普遍服务多家无晶圆设计客户，在MTO按单生产模式下同时处理多品种、小批量、短交期订单，排程决策直接影响制造周期、准交率、在制品WIP水平及设备利用率。Chien等（2011）指出，半导体制造建模需在产能约束、工艺路线柔性、随机扰动与信息不完全之间取得平衡；对于封装后端而言，上述矛盾往往体现为物流驱动型排程问题，而非单纯的前道工艺优化问题。

存储类半导体封装后端具有多品种混线、并行设备规模大、换型频繁、批次结构复杂等特点。典型产线可抽象为六工序串联流程：晶圆切割D/S→粘片DA→焊线WB→塑封Mold→键合/研磨B/G→贴带包装Taping。该结构在运筹学上属于混合流水车间HFS：各阶段按固定工艺顺序流转，阶段内部配置多台并行异构设备。DA与WB工序设备数量多、批次搬运与换型Setup开销显著，常成为产能约束与调度热点；Mold等工序在特定负荷条件下亦可能形成瓶颈。与理想化流水车间不同，封装后端同时存在订单到达随机性、批次拆分与合并、跨工序Worker搬运、序列相关换型Setup时间以及多级WIP等离散事件特征，使得纯解析优化模型难以完整刻画系统动态。Jain和Meeran（1999）对作业车间调度的长期回顾表明，真实生产环境中的资源异构、工序顺序与动态到达使NP-hard问题更加复杂；Stubbe和Rose（2011）的仿真研究亦说明，小批量与批处理设备替换会显著改变系统绩效。

1.2 业务特征与调度难点

从业务视角看，OSAT企业订单在ReleaseDate、DueDate、Material类型、OrderQty等方面高度异质。Lin和Chen（2015）在对真实封装组装设施的混合流水排程研究中指出，订单常被拆分为若干子作业并行加工后再合并，且同一订单的子作业在各阶段须使用相容的机台类型，以满足质量追溯与产品—机台资格约束。这一拆分—并行—合并行为显著增加了释放控制、批次规模与派工决策的耦合复杂度。Wu等（2023）在半导体制造机器调度综述中强调，后端组装与前道晶圆厂相比更突出物流、交期与流动时间Flow Time管理问题；短制造周期与稳健准交能力直接关联库存风险、销售损失与客户满意度。Lee和Lee（2008，2011）针对MCP多芯片封装组装线的研究亦表明，重入工序、异构并行机与换型时间对产能分配策略具有决定性影响，与本研究DA/WB结构高度相关。

在实际排程实践中，计划人员通常同时关注两类相互制约的目标：一是系统层面制造周期MakeSpan或流动时间最小化，反映产线吞吐效率；二是订单层面准交与延期惩罚最小化，反映交期承诺履行能力。Pinedo（2016）系统论述了制造周期、拖期与误期等经典目标函数；在多目标无法同时最优时，加权标量化是管理科学与工程领域常用的决策支持方式。本研究拟采用加权标量目标函数Objective = 0.7×MakeSpan + 0.3×Penalty，并在Simio Experiment中作为主响应变量Primary Response用于情景排序与比较；其中Penalty在任一订单发生延期时取大罚值、全部准时则为零，以体现准交约束的硬边界特征。

1.3 本研究数据来源与研究场景

本研究数据来自典型存储类半导体封装企业提供的已脱敏 Simio 导入数据集，对应企业实际一周排产样本的原生字段，未经虚构扩充。Orders 工作表含 41 条订单，字段包括 OrderNumber、MaterialFK、OrderQty、ReleaseDate、DueTime 及 DA/WB 工序 Assigned_DA_Group、Assigned_WB_Group；Materials 工作表含 16 种物料，给出 DiesPerUnit、StripsPerMag、QtyPerMag、QtyPerSubLot 等批次拆分参数及各工序 UPH；MachineConfig 工作表给出六工序工序站 Server 台数，合计 459 台，即 D/S 31 台、DA 112 台、WB 284 台、Mold 7 台、B/G 17 台、Taping 8 台。加工时间按 CurrentQty/UPH 计算；DA/WB 每批转入与转出搬运各 3 分钟，Assigned_DA_Group 或 Material 变化时触发 10 分钟换型 Setup。

在模型与实验层面，拟采用 Simio 离散事件仿真 DES 构建六工序一体化模型：订单 Order 为计划释放单元，经 Separator 链拆分为制造批次 MLot、弹夹批次 Magazine 与子批次 SubLot，并纳入 Worker 搬运、换型 Setup 及订单源 Source 释放逻辑。Law（2015）与 Banks 等（2010）所阐述的 DES 建模、验证与实验设计流程，为本研究提供了方法规范。研究决策变量包括批次缩放因子 MLotFactor 与 SubLotFactor，二者拟定义为 Model Properties 并接入 Scenario Generator 情景生成器；订单释放与派工拟采用最早交期先出规则 EDD。拟按以下步骤开展仿真研究：第一，在因子均为 1.0 的基准情景下验证 Experiment 对 MakeSpan、Penalty 与 Objective 的计算链路；第二，在上述基准数据上对 MLotFactor 与 SubLotFactor 开展全因子网格扫描，识别加权 Objective 较优的因子区间；第三，在仅调整 Orders 表 DueDate 行序、不改 Source 释放逻辑的对照中，检验表序调整能否替代 Source 层 EDD；第四，实现 Source 层 EDD 释放并与 FIFO 等基线对比，评估 Penalty 与 Objective 的改善幅度。上述步骤为本研究拟完成的实验方案，定量结论以学位论文阶段的系统实验为准。

2. 研究意义

2.1 理论意义

本研究将多目标排程理论、混合流水车间调度与批次拆分问题置于离散事件仿真框架下加以整合，具有以下理论价值。

第一，丰富封装后端排程建模范式。在统一Simio模型中同时刻画六工序流转、三级批次拆分与合并、Worker搬运与DA/WB换型Setup，有助于弥补简化流水模型对OSAT场景刻画不足的问题，回应Chien等（2011）与Chen-Ritzo等（2011）关于仿真需贴近工业逻辑方能支持运营决策的论断。

第二，拓展仿真优化在后端组装的应用边界。以MakeSpan与延期惩罚构建加权多目标Response，并借助Scenario Generator开展二维因子网格实验，为Fowler等（2008）与Lin和Chen（2015）所总结的仿真评估与参数搜索范式提供可复现案例；与Chen等（2013）GA/PSO+OCBA、Chiu等（2023，2026）智能优化研究形成方法对照，明确DES Experiment在工业级复杂约束下的基准作用。

第三，揭示效率—准交权衡结构。通过对比FIFO、EDD等经典派工规则及批次因子敏感性，Panwalkar和Iskander（1977）的综述为本研究提供了规则基准，有助于识别MakeSpan与Penalty的Pareto权衡区间，并补充Pinedo（2016）调度理论在含批次拆分与交期惩罚场景下的实证讨论。Framinan等（2004）与Ruiz等（2006）关于流水与混合流水制造周期启发式的研究，为本研究解析因子与规则交互效应提供了理论参照。

2.2 实践意义

在无需新增资本投入的前提下，通过仿真寻优识别批次因子与释放/派工策略的改进区间，可为封装后端产线计划人员提供可操作的排程参数建议。本研究预期通过批次因子网格扫描与EDD/FIFO对比，揭示MLotFactor、SubLotFactor与Objective、Penalty之间的可解释映射关系，识别盲目放大批次可能恶化准交绩效的风险区间，并为降低延期风险、缩短制造周期及负荷校准后改善DA/WB等关键工序利用率提供决策依据。

对于企业生产计划部门而言，本研究输出的并非一次性最优解，而是一组可解释的参数—绩效映射关系：在给定脱敏订单结构与设备规模下，何种批次缩放区间更可能同时控制MakeSpan与Penalty；在何种负荷水平下瓶颈由喂料不足转向DA/WB约束；EDD释放相对于FIFO究竟改善多少Penalty。此类情景假设分析正是Chen-Ritzo等（2011）所强调的仿真决策支持价值。对于学院管理科学与工程训练而言，本研究贯穿数据治理、随机系统建模、实验设计与多目标决策，符合系统建模与仿真研究方向的人才培养目标。

此外，所构建的脱敏Simio模型与Experiment框架可复用于后续负荷敏感性分析、EDD派工对比及潜在OptQuest与元启发式算法扩展，为产学研协同提供可迁移的实验平台。Hoppe等（2025）与Luttmann和Xie（2026）等最新组合优化/强化学习研究虽提供了方法前沿，但与工业DES平台对接仍需可复现基准模型，本研究的积累可为此类对照研究提供基础场景。项目成果亦可以实验记录、对比图表形式支撑后续期刊论文或会议投稿，提升研究的延续性与学术产出潜力。

3. 国内外研究现状分析

3.1 半导体封装后端排程与派工规则

半导体制造调度研究长期以前道晶圆厂为主，但后端组装同样面临多品种、并行机台、换型与交期约束等难题。Wu等（2023）系统梳理了半导体制造机器调度问题及精确算法、启发式与仿真优化等求解方法，指出后端场景在订单拆分、异构并行机与交期管理方面具有鲜明特征。刘琼等（2022）从中文文献角度综述了半导体制造调度问题，为国内研究提供了系统入口。Chien等（2011）从全球产业链视角总结了半导体制造建模分析的主要挑战，强调脱敏真实数据与仿真验证对管理决策支持的重要性。

在封装组装线领域，Lee和Lee（2008，2011）针对MCP组装线研究了重入工序、异构并行机与换型下的产能分配与派工策略，是后端排程的代表性工作。Lin和Chen（2015）基于真实OSAT数据提出混合流水仿真优化方法，以遗传算法结合最优计算预算分配OCBA求解产线—机台类型指派，并开展需求、产品结构与批次大小情景分析，与本研究真实数据+仿真优化路线高度契合。Chen等（2013）将粒子群优化PSO与OCBA用于后段组装动态并行机调度，验证了元启发式与仿真联动的有效性。赵子夜等（2025）针对封装测试柔性流水车间建立含拖期惩罚的多目标模型；轩华等（2020）研究考虑运输的柔性流水车间调度，为混合流水扩展提供参考。

从派工规则视角看，Panwalkar和Iskander（1977）的经典综述表明，EDD、SPT、CR等规则在不同目标下表现各异；在交期导向场景中，EDD常作为基准规则，但其效果依赖释放策略与队列形成机制。文献与行业经验均表明，Source释放顺序与设备队列派工规则若未与EDD协同，Penalty触发情景下可能出现高额延期惩罚，说明后端排程需同时优化入流顺序与队列排序。Lee和Lee（2011）的产能分配策略亦提示，仅优化局部队列不足以解决全局交期问题，需与订单释放、批次拆分协同。本研究拟通过Source层EDD实现与Orders表行序对照实验，检验上述机制在本场景下的作用边界。

近年来，智能优化方法加速向后端延伸。Chiu等（2023）研究半导体组装订单分配与灵活拆分规则的进化仿真优化；Chiu等（2026）将深度强化学习与仿真优化集成于后端组装调度。Yedidsion等（2021）与Zhou等（2020）在晶圆厂/智能制造场景下展示了深度强化学习对动态调度的潜力。Hoppe等（2025）提出结构化强化学习SRL，通过嵌入组合优化层处理大规模组合动作空间；Luttmann和Xie（2026）的多动作自改进方法MACSIM在柔性流水/作业车间调度基准上展示了神经组合优化进展。上述研究丰富了方法谱系，但面向六工序一体化、含Worker搬运、换型Setup与三级批次的Simio Experiment框架仍相对少见，且部分智能方法对数据规模与训练成本要求较高，尚难直接替代工业DES上的可解释参数扫描。

3.2 批次拆分、批处理与lot streaming

批次与子批次决策深刻影响WIP水平、流动时间与设备利用率。Potts和Van Wassenhove（1982）奠定了多阶段调度中lot streaming分解的理论基础；Uzsoy等（1992）给出同构子批的单机调度算法。Klemmt等（2011）比较混合整数规划与离散事件仿真，提出仿真与数学规划结合的时间窗分解方法，是半导体批处理调度的重要参考。Akçali等（2003）通过仿真评估批处理启发式对延期指标的影响；Mönch等（2001）研究不兼容产品族并行批处理机的启发式调度；Habenicht和Mönch（2002）将高级派工规则集成于晶圆厂批处理工具调度。Stubbe和Rose（2011）分析小批量与批处理设备替换的仿真绩效。王卓君等（2023）研究晶圆批处理设备的组批与指派。

在封装后端，计划释放单元为订单 Order，仿真批次经 Separator 链依次形成制造批次 MLot、弹夹批次 Magazine 与子批次 SubLot。Lin和Chen（2015）指出，Magazine 是跨工序搬运与追溯的关键单元，拆分粒度直接影响作业在 DA/WB 等热点工序的并行度与等待时间。本研究拟通过MLotFactor、SubLotFactor对Separator逻辑进行缩放，在不改动底层BOM的前提下模拟批次放大/缩小政策，属于参数化敏感性分析而非重新设计Lot结构。既有文献提示，SubLotFactor适度减小可能缩短流动时间，但因子过大时Penalty与MakeSpan可能同时恶化，体现批次规模与交期约束的非线性耦合；本研究将通过网格扫描定量检验上述规律在本脱敏场景下的表现。

现有文献多聚焦前道炉管批处理或一般lot streaming，对三级批次、换型Setup、搬运与多目标Penalty的组合研究相对有限。本研究将在Klemmt等（2011）与Stubbe和Rose（2011）的仿真优化思路上，结合Simio Combiner/Separator逻辑，形成可复现实验网格，填补封装后端批次参数扫描的实证空白。

3.3 离散事件仿真与仿真优化

Law（2015）、Banks等（2010）系统阐述了DES建模、验证、输出分析与实验设计方法论，是管理科学与工程领域开展仿真研究的经典教材。Chen-Ritzo等（2011）总结了半导体制造中仿真支持运营决策的工业实践经验，指出仿真模型需与MES/计划系统数据口径一致。Fowler等（2008）综述了基于仿真的调度研究进展，强调仿真优化在随机环境下的必要性。商业DES平台Simio支持Experiment模块与Scenario Generator，便于对批次因子、释放规则等离散或连续决策变量进行网格扫描，并为后续接入OptQuest等仿真优化器预留接口。本研究拟采用Scenario Generator全因子扫描MLotFactor×SubLotFactor，并开展释放顺序对照及EDD/FIFO对比，属于仿真优化中的序贯敏感性分析策略。

仿真优化一般包括三个环节：以仿真模型作为仿真性能评估器；以优化或搜索策略在决策空间上引导采样；以OCBA、Common Random Numbers等统计方法处理仿真噪声。Lin和Chen（2015）与Chen等（2013）代表了元启发式与OCBA路线；本研究开题至中期阶段以Scenario Generator穷举/网格为主，优势在于对工业参数的直接可解释性与较低实现门槛。Fowler等（2008）亦指出，在复杂系统中，先用仿真摸清参数敏感性再嵌入优化器，是常见且稳健的技术路线。

在模型验证方面，本研究拟在41单一周基准场景下检验订单能否完整流转、加工时间逻辑是否与模型说明一致，以满足Law（2015）所强调的概念模型与运行模型一致性要求。后续将在负荷校准情景下进一步检查利用率与瓶颈位置是否合理，避免在喂料不足伪瓶颈下得出错误调度结论。

3.4 多目标排程、制造周期与交期惩罚

制造周期最小化与准交/拖期最小化是生产排程的两类经典目标。Pinedo（2016）系统论述了相关目标函数及算法体系。Panwalkar和Iskander（1977）综述了包括EDD、SPT等在内的派工规则，EDD在交期约束场景下仍具基准价值。Framinan等（2004）研究流水车间制造周期与流动时间的启发式；Ruiz等（2006）给出混合流水鲁棒调度算法。赵子夜等（2025）在柔性流水车间中集成拖期惩罚，展示了多目标建模在国内封装测试研究中的应用。

在多目标处理策略上，常见方法包括Pareto前沿求解、分层优化与加权标量化。本研究拟采用Objective = 0.7×MakeSpan + 0.3×Penalty，属于加权标量化，便于在Simio Experiment中作为单一主响应变量Primary Response排序Scenario。Penalty采用延期则大罚、全准时为零的阈值式设计，强调准交硬约束，与部分文献中连续拖期积分目标不同；该设计更贴近计划部门对是否延期的离散管理口径，但需在论文中明确Penalty标度对权重解读的影响。

MakeSpan统计口径方面，Experiment拟并行采用Mold工序截面时刻Mold_T_End与Sink整线LastDepartureTime两种记录方式，并以后者作为全局制造周期主口径。两种口径在订单后段B/G、Taping占用显著时将产生差异。Chen-Ritzo等（2011）强调KPI定义与仿真事件记录点必须一致；本研究将在实验中并行记录两种MakeSpan，并在论文中报告口径敏感性，避免结论对外部读者产生歧义。

3.5 文献述评与研究缺口

综合上述研究，可以得到以下缺口。第一，面向封装后端六工序一体化、含Worker搬运、DA/WB换型Setup及三级批次结构的DES模型与脱敏真实订单数据相结合的实证研究仍不足。第二，在MakeSpan与延期惩罚双目标下，批次因子与EDD释放/派工策略的联合优化及对比验证有待系统化；文献与行业经验提示，仅调整订单表行序可能不足以实现交期驱动释放，本研究拟通过Source层EDD与表序对照实验加以检验。第三，负荷校准、ReleaseDate/DueDate基准化与Penalty触发机制尚未在统一实验协议下充分揭示。本研究将在上述缺口上开展可复现的Simio Experiment研究，并为后续OptQuest或智能优化对照预留接口。

3.6 本研究与现有研究的定位

与Lin和Chen（2015）聚焦产线—机台类型指派、GA与OCBA相比，本研究将决策重点放在批次缩放因子与释放/派工规则，以Simio Experiment Scenario Generator为平台，强调MakeSpan与Penalty加权多目标在固定工艺路线下的参数敏感性，而非重新求解指派组合爆炸。与Chiu等（2023，2026）的智能优化路线相比，本研究优先保证工业级DES模型的可解释性与可复现性，使实验结论可直接对接计划员可操作的MLotFactor、SubLotFactor与EDD规则。与Klemmt等（2011）、Stubbe和Rose（2011）的批处理仿真研究相比，本研究突出封装后端三级批次结构及Worker搬运与换型Setup约束，而非前道炉管批处理。与Hoppe等（2025）、Luttmann和Xie（2026）等组合优化/神经方法相比，本研究提供基于真实脱敏订单的基准场景，可作为未来智能调度算法对照的数字孪生底座。

从研究方法论链条看，本研究遵循数据基准化→DES建模→KPI/Experiment→因子与规则扫描→负荷校准→论文凝练的递进逻辑，与Law（2015）所强调的仿真研究规范一致；在优化搜索层面，开题至中期以全因子网格为主，后续可逐步引入OptQuest或借鉴Chen等（2013）的PSO+OCBA进行连续/离散混合寻优。在绩效测度层面，将同步推进MakeSpan口径统一与Penalty触发机制分析，避免KPI混用导致结论不可比，Chen-Ritzo等（2011）对此亦有强调。

从数据与实验条件看，41 条订单、16 种物料、459 台设备及 DA/WB 搬运与换型 Setup 参数均直接对应企业脱敏 Simio 导入数据与模型架构说明，场景设定可追溯、可复现。

综上，本研究在理论层面衔接HFSP调度、批次拆分与多目标仿真优化文献；在实践层面面向典型存储类封装后端脱敏场景；在方法层面以Simio DES+Experiment为主干，吸收派工规则与仿真优化文献成果，形成具有可验证实验计划的管理科学与工程硕士研究方案。

4. 主要参考文献""")

SECTION2 = _compact_spacing(r"""1. 研究目标、研究内容和拟解决的关键问题

1.1 研究目标

本研究旨在面向典型存储类半导体封装后端产线，构建可运行的Simio离散事件仿真模型，并在加权多目标框架下开展批次因子与释放/派工策略的仿真优化与情景对比。具体目标包括：建立涵盖六工序、三级批次、搬运与换型Setup逻辑的DES模型，实现与行业脱敏订单及设备数据的可重复绑定；以MakeSpan最小化与延期惩罚最小化为核心，构建Objective=0.7×MakeSpan+0.3×Penalty的Experiment绩效体系，通过Scenario Generator对MLotFactor、SubLotFactor及EDD等策略进行网格扫描与对比；识别效率—准交权衡下的较优参数区间及瓶颈工序，为学位论文提供可验证的实验结论与管理启示。

1.2 研究内容

第一，数据绑定与流程建模。基于企业脱敏 Simio 导入数据，将 Orders、Materials、MachineConfig 等工作表绑定至模型；41 条订单构成一周排产基准样本，ReleaseDate/DueDate 拟按基准化方案统一；在 Simio 中实现六工序主流程，订单 Order 经 Separator 链形成 MLot→Magazine→SubLot 批次结构，加工时间按 CurrentQty/UPH 计算，DA/WB 每批转入与转出搬运各 3 分钟，Assigned_DA_Group 变化时触发 10 分钟换型 Setup。

第二，绩效指标与Experiment框架。定义MakeSpan、Penalty及加权Objective三个响应变量Response；将MLotFactor、SubLotFactor设为Model Properties并接入Scenario Generator，开展二维因子网格实验；明确MakeSpan统计口径，并行采用Mold工序截面Mold_T_End与Sink整线LastDepartureTime，并在论文中报告口径敏感性。

第三，交期驱动释放与派工策略。在Source及首队列引入EDD规则，按DueDate或DueDate减ReleaseDate升序释放与派工，对比先进先出FIFO等基线；开展交期升序释放与FIFO的对比实验，评估Penalty与Objective改善幅度。

第四，负荷校准与敏感性分析。通过订单复制、压缩ReleaseDate窗口或调整有效设备规模等方式，将DA/WB利用率提升至可反映瓶颈特征的水平，目标区间约50%至90%，在此基础上重复因子网格与派工对比，分析结论稳健性。

1.3 拟解决的关键问题

本研究拟回答三类关键问题：批次因子如何影响WIP、MakeSpan与Penalty，不同MLotFactor与SubLotFactor组合是否呈现可解释的权衡规律；订单释放顺序与队列派工规则如何影响准交绩效，Source层EDD与Orders表行序调整的效果边界何在；在负荷校准条件下，如何识别DA/WB/Mold等瓶颈工序并解释Experiment较优情景的运作机制。

2. 拟采取的研究思路与方法、技术路线、实验方案及可行性分析

2.1 研究思路与技术路线

研究分四阶段推进：第一阶段完成 Orders 表 ReleaseDate/DueDate 基准化与企业脱敏数据固化；第二阶段完善 Simio 六工序模型及 Experiment 绩效体系；第三阶段开展批次因子网格、EDD 策略及负荷校准实验；第四阶段汇总结果、撰写学位论文。

技术路线如下：行业脱敏数据准备→Simio DES建模，含六工序、批次、搬运与换型Setup→定义MakeSpan/Penalty/Objective→Scenario Generator因子扫描→EDD释放/派工优化→负荷敏感性实验→结论与论文定稿。

2.2 研究方法

第一，离散事件仿真法。采用Simio构建封装后端系统模型，通过多次重复运行Replications估计响应均值，遵循Law（2015）所述建模—验证—实验设计流程。

第二，仿真优化与全因子实验设计。以MLotFactor、SubLotFactor为可控因子，利用Scenario Generator构造网格场景；主响应变量Primary Response设为Objective，对比各情景MakeSpan、Penalty及综合目标，方法上对标Lin和Chen（2015）、Chen等（2013）的仿真优化框架；后续可探索OptQuest与元启发式算法接入。

第三，派工与释放规则对比法。以Panwalkar和Iskander（1977）所述EDD为交期驱动基准，与FIFO对比，并在Source与Server Selection Rule层协同实现。

第四，情景分析与敏感性分析。参照Stubbe和Rose（2011）、Lee和Lee（2011）的做法，在不同负荷水平、因子水平下比较系统绩效，解释Penalty触发条件与瓶颈迁移现象。

2.3 实验方案

实验分四步推进：第一步，在因子均为 1.0 的基准情景下验证 Objective 计算链路；第二步，基于上述企业脱敏数据对 MLotFactor 与 SubLotFactor 开展 26 情景全因子网格扫描，识别较优因子区间；第三步，在仅调整 Orders 表释放顺序的对照中检验 Source 释放逻辑的必要性；第四步，实现 DueDate 升序的 EDD 释放，并在较优因子附近情景与 FIFO 基线对比。仿真终止时间设为 100 至 144 小时量级，以全部 41 单完成为准；预热期按基准化方案将起始日前历史到达视为预热窗口。

2.4 可行性分析

本研究在数据、平台与方法三方面具备开展条件。数据方面，已获得企业脱敏 Simio 导入数据，含 41 条订单、16 种物料及六工序 459 台设备配置，字段覆盖 OrderQty、ReleaseDate、DueTime、MaterialFK、各工序 UPH 与 DA/WB 换型 Setup 参数。平台方面，Simio DES 及 Experiment、Scenario Generator 模块可支撑六工序一体化建模与多情景批量运行；课题组已搭建六工序模型框架，含 Order—MLot—Magazine—SubLot 批次链、Worker 搬运及 DA/WB 换型 Setup 逻辑。方法方面，Law（2015）与 Banks 等（2010）的 DES 验证与实验设计规范、Lin 和 Chen（2015）等的仿真优化范式，为实验方案提供了成熟方法论支撑。各因子最优区间及 EDD 改善幅度等结论，须待后续实验按方案系统完成后凝练。

3. 研究的特色与创新点

第一，在单一Simio模型中集成六工序、Worker搬运、DA/WB换型Setup及三级批次结构，贴近OSAT后端实际逻辑，克服简化流水模型对封装场景刻画不足的问题。

第二，将批次因子与Experiment Scenario Generator联动，形成可复现的二维参数网格与加权多目标响应体系，为MakeSpan—Penalty权衡提供量化实验证据。

第三，在统一DES框架下联合考察批次缩放与EDD释放/派工策略，并通过Source层实现与Orders表行序对照，检验交期驱动释放的作用机制，为后续负荷校准与OptQuest扩展预留方法接口。

4. 研究工作计划

2026年6—8月：完成ReleaseDate/DueDate基准化，统一MakeSpan口径，开展负荷校准实验；2026年9—12月：实现Source与队列EDD，完成交期升序释放与派工对比实验；2027年1—3月：扩展因子水平与稳健性分析，整理实验图表；2027年4—5月：撰写、修改学位论文并准备答辩。

5. 预期研究成果

预期形成以下成果：完成硕士学位论文《多目标优化的半导体后端制造生产排程研究》1 篇；交付可运行的 Simio 封装后端仿真模型及与上述企业脱敏数据一致的实验数据集；通过批次因子网格扫描与 EDD/FIFO 对比实验，形成关于 MakeSpan—Penalty 权衡、瓶颈工序识别及排程参数建议的管理启示；整理可复用的 Experiment 配置与实验记录，为后续期刊论文或技术报告提供素材。具体数值结论与图表以学位论文定稿为准。""")

SECTION3 = _compact_spacing(r"""1. 与本项目有关的研究工作积累和已取得的研究工作成绩

第一，仿真模型建设。已搭建六工序 Simio 模型框架，涵盖 D/S→DA→WB→Mold→B/G→Taping 主流程、订单 Order 经 Separator 链形成 MLot→Magazine→SubLot 批次结构、Worker 搬运及 DA/WB 换型 Setup。设备规模与 MachineConfig 一致：D/S 31 台、DA 112 台、WB 284 台、Mold 7 台、B/G 17 台、Taping 8 台，合计 459 台。各工序站 Server 加工时间按 CurrentQty 与 Materials 表 UPH 计算，DA/WB 每批转入与转出搬运各 3 分钟，Assigned_DA_Group 变化时触发 10 分钟换型 Setup。

第二，Experiment 与数据体系。已定义 MakeSpan、Penalty 与 Objective=0.7×MakeSpan+0.3×Penalty 三个响应变量 Response；MLotFactor、SubLotFactor 已作为 Model Properties 接入 Scenario Generator。企业脱敏 Simio 导入数据含 41 条订单与 16 种物料，已绑定至模型并完成基准情景运行。

第三，阶段性仿真实验。已完成因子均为 1.0 的基准情景验证，MakeSpan=78.40、Penalty=0、Objective=54.88；已完成 26 情景批次因子全因子网格扫描，Objective 最优 50.61，对应 MLotFactor=1.0、SubLotFactor=0.75，部分因子组合 Penalty 高达 760；已完成仅调整 Orders 表 DueDate 行序的对照，Objective 最优 52.38，表明释放顺序须与 Source 层逻辑协同。上述结果为标定实验与后续 EDD、负荷校准研究提供基线，正式结论将在学位论文中系统报告。

第四，文献与开题准备。已系统研读半导体排程、仿真优化、多目标调度等领域文献，完成开题报告撰写，并整理参考文献元数据与事实核查记录。

2. 已具备的实验、资料等条件，尚缺少的实验、资料条件和拟解决的途径

2.1 已具备条件

Simio 软件及六工序模型源文件；企业脱敏 Simio 导入数据，含 Orders、Materials、MachineConfig 等工作表；模型架构说明文档；Experiment 与 Scenario Generator 配置及上述阶段性实验记录。

2.2 尚缺条件与解决途径

第一，设备利用率偏低。原始场景各工序平均利用率约 13%，距反映瓶颈的负荷水平差距较大。拟通过复制订单并压缩 ReleaseDate 窗口、或调整有效 DA/WB 台数等方式开展负荷敏感性实验，寻求 DA/WB 利用率进入 50% 至 90% 区间的标定场景。

第二，Magazine/批次口径。Materials 表中 StripsPerMag、QtyPerMag 等字段含义须与封装行业规范及模型表达式逐项对照，避免批次因子物理意义偏差。

第三，MakeSpan 全局定义。Experiment 当前暂用 Mold_T_End，拟并行记录 Sink 整线 LastDepartureTime 并在论文中统一主口径。

第四，Source 层 EDD 尚未完全实现。拟修改订单源 Source 释放逻辑与各设备队列派工规则为 EDD，DueDate 升序，开展交期升序释放对照，并在较优因子附近情景对比 Penalty 改善幅度。

第五，潜在 OptQuest/元启发式扩展。当前以 Scenario Generator 网格扫描为主；待基准协议稳定后，可探索 OptQuest 或借鉴 Lin 和 Chen（2015）、Chen 等（2013）的 GA/PSO+OCBA 思路，作为后续拓展而非开题阶段必达项。""")
