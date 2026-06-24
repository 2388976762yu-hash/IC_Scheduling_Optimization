# -*- coding: utf-8 -*-
"""开题报告 SECTION1/2/3 正文（不含参考文献列表，列表由 fill_template 从 BIBLIOGRAPHY.yaml 生成）"""

SECTION1_BODY = r"""1. 论文选题的背景

1.1 产业环境与问题提出

半导体产业是国民经济与国家安全的重要支柱，其制造链条可概括为前道晶圆制造与后道封装测试两大环节。后道封装测试（Outsourced Semiconductor Assembly and Test，OSAT）承担晶圆切割、粘片、键合、塑封、研磨及贴带包装等工序，是连接芯片设计与终端应用的关键枢纽。全球半导体分工深化以来，OSAT企业普遍服务多家无晶圆设计客户，在按单生产（Make-to-Order，MTO）模式下同时处理多品种、小批量、短交期订单，排程决策直接影响制造周期、准交率、在制品（Work In Process，WIP）水平及设备利用率。Chien等（2011）指出，半导体制造建模需在产能约束、工艺路线柔性、随机扰动与信息不完全之间取得平衡；对于封装后端而言，上述矛盾往往体现为“物流驱动型”排程问题，而非单纯的前道工艺优化问题。

存储类半导体封装后端具有多品种混线、并行设备规模大、换型频繁、批次结构复杂等特点。典型产线可抽象为六工序串联流程：晶圆切割（D/S）→粘片（DA）→焊线（WB）→塑封（Mold）→键合/研磨（B/G）→贴带包装（Taping）。该结构在运筹学上属于混合流水车间（Hybrid Flow Shop，HFS）：各阶段按固定工艺顺序流转，阶段内部配置多台并行异构设备。DA与WB工序设备数量多、换型与搬运开销显著，常成为产能约束与调度热点；Mold等工序在特定负荷条件下亦可能形成瓶颈。与理想化流水车间不同，封装后端同时存在订单到达随机性、批次拆分与合并、跨工序Worker搬运、序列相关换型时间以及多级WIP等离散事件特征，使得纯解析优化模型难以完整刻画系统动态。Jain和Meeran（1999）对作业车间调度的长期回顾表明，真实生产环境中的资源异构、工序顺序与动态到达使NP-hard问题更加复杂；Stubbe和Rose（2011）的仿真研究亦说明，小批量与批处理设备替换会显著改变系统绩效。

1.2 业务特征与调度难点

从业务视角看，OSAT企业订单在ReleaseDate、DueDate、Material类型、OrderQty等方面高度异质。Lin和Chen（2015）在对真实封装组装设施的混合流水排程研究中指出，订单常被拆分为若干子作业并行加工后再合并，且同一订单的子作业在各阶段须使用相容的机台类型，以满足质量追溯与产品—机台资格约束。这一“拆分—并行—合并”行为显著增加了释放控制、批次规模与派工决策的耦合复杂度。Wu等（2023）在半导体制造机器调度综述中强调，后端组装与前道晶圆厂相比更突出物流、交期与流动时间（Flow Time）管理问题；短制造周期与稳健准交能力直接关联库存风险、销售损失与客户满意度。Lee和Lee（2008，2011）针对多芯片封装（MCP）组装线的研究亦表明，重入工序、异构并行机与换型时间对产能分配策略具有决定性影响，与本课题DA/WB结构高度相关。

在实际排程实践中，计划人员通常同时关注两类相互制约的目标：一是系统层面制造周期（MakeSpan）或流动时间最小化，反映产线吞吐效率；二是订单层面准交与延期惩罚最小化，反映交期承诺履行能力。Pinedo（2016）系统论述了制造周期、拖期与误期等经典目标函数；在多目标无法同时最优时，加权标量化是管理科学与工程领域常用的决策支持方式。本课题采用Objective=0.7×MakeSpan+0.3×Penalty，与项目组Experiment实现及决策记录（D-004）保持一致，其中Penalty在出现订单延期时取大罚值、全部准时则为零，以突出准交约束的硬边界特征。

1.3 本课题数据来源与研究场景

本课题依托导师科研项目，基于典型存储类半导体封装企业提供的已脱敏行业订单、物料与设备配置数据开展研究。数据经脱敏处理后保留订单数量、ReleaseDate/DueDate、Material类型、各工序单位产能（UPH）及机台规模等字段，不含可识别客户或合作方信息。基准场景包含41张订单，代表“一周”生产负荷；设备规模合计459台（D/S 31、DA 112、WB 284、Mold 7、B/G 17、Taping 8），加工时间按CurrentQty/UPH计算，DA/WB换型含搬运3分钟与设置10分钟（MaterialID/Group变化触发）。

在模型层面，采用Simio离散事件仿真（Discrete Event Simulation，DES）构建六工序一体化模型，刻画三级批次结构（制造批次MLot→杂志批次Magazine→子批次SubLot）、Worker搬运、换型及Source订单释放逻辑。Law（2015）与Banks等（2010）所阐述的DES建模—验证—实验设计流程，为本课题提供了方法规范。研究决策变量包括批次缩放因子MLotFactor、SubLotFactor（通过Model Properties接入Scenario Generator），以及基于最早交期规则（Earliest Due Date，EDD）的订单释放与派工策略。前期EXP-001至EXP-003实验表明：Experiment绩效链路可正确计算MakeSpan、Penalty与Objective；在SPAN基准数据下，26场景因子网格扫描得到Objective最优50.61（MLot=1.0，SubLot=0.75），部分因子组合Penalty高达760；仅调整Orders表DueDate行序不足以替代Source层EDD逻辑。上述结果为开题阶段的可行性提供了实证支撑。

2. 研究意义

2.1 理论意义

本研究将多目标排程理论、混合流水车间调度与批次拆分问题置于离散事件仿真框架下加以整合，具有以下理论价值。

第一，丰富封装后端排程建模范式。在统一Simio模型中同时刻画六工序流转、三级批次拆分/合并、Worker搬运与DA/WB换型，有助于弥补简化流水模型对OSAT场景刻画不足的问题，回应Chien等（2011）与Chen-Ritzo等（2011）关于“仿真需贴近工业逻辑方能支持运营决策”的论断。

第二，拓展仿真优化在后端组装的应用边界。以MakeSpan与延期惩罚构建加权多目标Response，并借助Scenario Generator开展二维因子网格实验，为“仿真评估+参数搜索”范式（Fowler等，2008；Lin和Chen，2015）提供可复现案例；与Chen等（2013）GA/PSO+OCBA、Chiu等（2023，2026）智能优化研究形成方法对照，明确DES Experiment在工业级复杂约束下的基准作用。

第三，揭示效率—准交权衡结构。通过对比FIFO、EDD等经典派工规则（Panwalkar和Iskander，1977）及批次因子敏感性，有助于识别MakeSpan与Penalty的Pareto权衡区间，补充Pinedo（2016）调度理论在含批次拆分与交期惩罚场景下的实证讨论。Framinan等（2004）与Ruiz等（2006）关于流水/混合流水制造周期启发式的研究，为本课题解析因子—规则交互效应提供了理论参照。

2.2 实践意义

在无需新增资本投入的前提下，通过仿真寻优识别批次因子与释放/派工策略的改进区间，可为封装后端产线计划人员提供可操作的排程参数建议。EXP-002显示，MLotFactor=1.0、SubLotFactor=0.75时Objective=50.61，优于EXP-001基准54.88；高因子组合（如1.25×1.25）则MakeSpan与Penalty双高，Objective可达291.18，提示盲目放大批次可能恶化准交绩效。研究结论可辅助降低延期风险、缩短制造周期并在负荷校准后改善DA/WB等关键工序利用率。

对于企业生产计划部门而言，本研究输出的并非一次性最优解，而是一组可解释的参数—绩效映射关系：在给定脱敏订单结构与设备规模下，何种批次缩放区间更可能同时控制MakeSpan与Penalty；在何种负荷水平下瓶颈由“喂料不足”转向“DA/WB约束”；EDD释放相对于FIFO究竟改善多少Penalty。此类“what-if”洞察正是Chen-Ritzo等（2011）所强调的仿真决策支持价值。对于学院管理科学与工程训练而言，课题贯穿数据治理、随机系统建模、实验设计与多目标决策，符合系统建模与仿真研究方向的人才培养目标。

此外，所构建的脱敏Simio模型与Experiment框架可复用于后续负荷敏感性分析、EDD派工对比及潜在OptQuest/metaheuristic扩展，为产学研协同提供可迁移的实验平台。Hoppe等（2025）与Luttmann和Xie（2026）等最新组合优化/强化学习研究虽提供了方法前沿，但与工业DES平台对接仍需可复现基准模型——本课题的积累可为此类对照研究提供基础场景。项目成果亦可以实验记录、对比图表形式支撑后续期刊论文或会议投稿，提升研究的延续性与学术产出潜力。

3. 国内外研究现状分析

3.1 半导体封装后端排程与派工规则

半导体制造调度研究长期以前道晶圆厂为主，但后端组装同样面临多品种、并行机台、换型与交期约束等难题。Wu等（2023）系统梳理了半导体制造机器调度问题及精确算法、启发式与仿真优化等求解方法，指出后端场景在订单拆分、异构并行机与交期管理方面具有鲜明特征。刘琼等（2022）从中文文献角度综述了半导体制造调度问题，为国内研究提供了系统入口。Chien等（2011）从全球产业链视角总结了半导体制造建模分析的主要挑战，强调脱敏真实数据与仿真验证对管理决策支持的重要性。

在封装组装线领域，Lee和Lee（2008，2011）针对MCP组装线研究了重入工序、异构并行机与换型下的产能分配与派工策略，是后端排程的代表性工作。Lin和Chen（2015）基于真实OSAT数据提出混合流水仿真优化方法，以遗传算法结合最优计算预算分配（OCBA）求解产线—机台类型指派，并开展需求、产品结构与批次大小情景分析，与本课题“真实数据+SO”路线高度契合。Chen等（2013）将粒子群优化（PSO）与OCBA用于后段组装动态并行机调度，验证了元启发式与仿真联动的有效性。赵子夜等（2025）针对封装测试柔性流水车间建立含拖期惩罚的多目标模型；轩华等（2020）研究考虑运输的柔性流水车间调度，为混合流水扩展提供参考。

从派工规则视角看，Panwalkar和Iskander（1977）的经典综述表明，EDD、SPT、CR等规则在不同目标下表现各异；在交期导向场景中，EDD常作为基准规则，但其效果依赖释放策略与队列形成机制。本课题前期实验显示，在Penalty触发情景下，Source释放顺序与Server Selection Rule尚未与EDD一致，导致部分因子组合出现高额延期惩罚，说明后端排程需同时优化“入流顺序”与“队列排序”。Lee和Lee（2011）的产能分配策略亦提示，仅优化局部队列不足以解决全局交期问题，需与订单释放、批次拆分协同。

近年来，智能优化方法加速向后端延伸。Chiu等（2023）研究半导体组装订单分配与灵活拆分规则的进化仿真优化；Chiu等（2026）将深度强化学习与仿真优化集成于后端组装调度。Yedidsion等（2021）与Zhou等（2020）在晶圆厂/智能制造场景下展示了深度强化学习对动态调度的潜力。Hoppe等（2025）提出结构化强化学习（SRL），通过嵌入组合优化层处理大规模组合动作空间；Luttmann和Xie（2026）的多动作自改进方法（MACSIM）在柔性流水/作业车间调度基准上展示了神经组合优化进展。上述研究丰富了方法谱系，但面向六工序一体化、含搬运换型与三级批次的Simio Experiment框架仍相对少见，且部分智能方法对数据规模与训练成本要求较高，尚难直接替代工业DES上的可解释参数扫描。

3.2 批次拆分、批处理与lot streaming

批次与子批次决策深刻影响WIP水平、流动时间与设备利用率。Potts和Van Wassenhove（1982）奠定了多阶段调度中lot streaming分解的理论基础；Uzsoy等（1992）给出同构子批的单机调度算法。Klemmt等（2011）比较混合整数规划与离散事件仿真，提出仿真与数学规划结合的时间窗分解方法，是半导体批处理调度的重要参考。Akçali等（2003）通过仿真评估批处理启发式对延期指标的影响；Mönch等（2001）研究不兼容产品族并行批处理机的启发式调度；Habenicht和Mönch（2002）将高级派工规则集成于晶圆厂批处理工具调度。Stubbe和Rose（2011）分析小批量与批处理设备替换的仿真绩效。王卓君等（2023）研究晶圆批处理设备的组批与指派。

在封装后端，批次结构更具层次性：制造批次（MLot）→杂志批次（Magazine）→子批次（SubLot）。Lin和Chen（2015）指出，Magazine是跨工序搬运与追溯的关键单元，拆分粒度直接影响作业在DA/WB等热点工序的并行度与等待时间。本课题通过MLotFactor、SubLotFactor对Separator逻辑进行缩放，在不改动底层BOM的前提下模拟“批次放大/缩小”政策，属于参数化敏感性分析而非重新设计Lot结构。EXP-002结果显示，SubLotFactor=0.75在MLot=1.0附近取得较优Objective，说明适度减小子批可能缩短流动时间；但当因子过大（1.25×1.25）时Penalty与MakeSpan同时恶化，体现批次规模与交期约束的非线性耦合。

现有文献多聚焦前道炉管批处理或一般lot streaming，对“三级批次+换型+搬运+多目标Penalty”的组合研究相对有限。本课题将在Klemmt等（2011）与Stubbe和Rose（2011）的仿真优化思路上，结合项目组Model3.0已实现的Combiner/Separator逻辑，形成可复现实验网格，填补封装后端批次参数扫描的实证空白。

3.3 离散事件仿真与仿真优化

Law（2015）、Banks等（2010）系统阐述了DES建模、验证、输出分析与实验设计方法论，是管理科学与工程领域开展仿真研究的经典教材。Chen-Ritzo等（2011）总结了半导体制造中仿真支持运营决策的工业实践经验，指出仿真模型需与MES/计划系统数据口径一致。Fowler等（2008）综述了基于仿真的调度研究进展，强调仿真优化在随机环境下的必要性。商业DES平台（如Simio）支持Experiment模块与Scenario Generator，便于对批次因子、释放规则等离散/连续决策变量进行网格扫描，并为后续接入OptQuest等仿真优化器预留接口。本课题采用Scenario Generator全因子扫描MLotFactor×SubLotFactor，对标项目组EXP-002/003实验协议，属于SO中的序贯敏感性分析策略。

仿真优化一般包括：（1）仿真模型作为性能评估oracle；（2）优化/search策略在决策空间上引导采样；（3）统计方法处理仿真噪声（如OCBA、Common Random Numbers等）。Lin和Chen（2015）与Chen等（2013）代表了元启发式+OCBA路线；本课题当前阶段以Scenario Generator穷举/网格为主，优势在于对工业参数的直接可解释性与较低实现门槛，符合开题到中期“先建立可复现基准”的研究节奏。Fowler等（2008）亦指出，在复杂系统中，先用仿真摸清参数敏感性再嵌入优化器，是常见且稳健的技术路线。

在模型验证方面，本项目Model3.0已实现41单100%完成流转，加工时间逻辑与Architecture文档一致，满足Law（2015）所强调的概念模型与运行模型一致性要求。后续将在负荷校准情景下进一步检查利用率与瓶颈位置是否合理，避免在“喂料不足”伪瓶颈下得出错误调度结论——这也是项目组第七次会议强调的现实问题。

3.4 多目标排程、制造周期与交期惩罚

制造周期最小化与准交/拖期最小化是生产排程的两类经典目标。Pinedo（2016）系统论述了相关目标函数及算法体系。Panwalkar和Iskander（1977）综述了包括EDD、SPT等在内的派工规则，EDD在交期约束场景下仍具基准价值。Framinan等（2004）研究流水车间制造周期与流动时间的启发式；Ruiz等（2006）给出混合流水鲁棒调度算法。赵子夜等（2025）在柔性流水车间中集成拖期惩罚，展示了多目标建模在国内封装测试研究中的应用。

在多目标处理策略上，常见方法包括Pareto前沿求解、分层优化与加权标量化。本课题采用Objective=0.7×MakeSpan+0.3×Penalty，属于加权标量化，便于在Simio Experiment中作为单一Primary Response排序Scenario，与项目组已跑通的EXP-001/002/003实现一致。Penalty采用“延期则大罚、全准时为零”的阈值式设计，强调准交硬约束，与部分文献中连续拖期积分目标不同；该设计更贴近计划部门对“是否延期”的离散管理口径，但需在论文中明确Penalty标度对权重解读的影响。

MakeSpan统计口径方面，DECISIONS D-002记录当前Experiment暂用Mold_T_End，而导师会议建议采用Sink整线LastDepartureTime。两种口径在数值上可能接近，但在订单后段（B/G、Taping）占用显著时将产生差异。Chen-Ritzo等（2011）强调KPI定义与仿真事件记录点必须一致；本课题将在后续实验中并行记录两种MakeSpan，并在论文中报告口径敏感性，避免结论对外部读者产生歧义。

3.5 文献述评与研究缺口

综合上述研究，可以得到以下缺口：（1）面向封装后端六工序一体化、含Worker搬运、DA/WB换型及三级批次结构的DES模型与脱敏真实订单数据相结合的实证研究仍不足；（2）在MakeSpan与延期惩罚双目标下，批次因子与EDD释放/派工策略的联合优化及对比验证有待系统化——EXP-003已表明仅调整Excel行序不足以实现交期驱动释放；（3）负荷校准、ReleaseDate/DueDate基准化与Penalty触发机制尚未在统一实验协议下充分揭示。本课题将在上述缺口上开展可复现的Simio Experiment研究，并为后续OptQuest或智能优化对照预留接口。

3.6 本课题与现有研究的定位

与Lin和Chen（2015）聚焦“产线—机台类型指派+GA+OCBA”相比，本课题将决策重点放在批次缩放因子与释放/派工规则，以Simio Experiment Scenario Generator为平台，强调加权多目标（MakeSpan+Penalty）在固定工艺路线下的参数敏感性，而非重新求解指派组合爆炸。与Chiu等（2023，2026）的智能优化路线相比，本课题优先保证工业级DES模型的可解释性与可复现性，使实验结论可直接对接计划员可操作的参数（MLotFactor/SubLotFactor、EDD规则）。与Klemmt等（2011）、Stubbe和Rose（2011）的批处理仿真研究相比，本课题突出封装后端三级批次结构及Worker/换型约束，而非前道炉管批处理。与Hoppe等（2025）、Luttmann和Xie（2026）等组合优化/神经方法相比，本课题提供基于真实脱敏订单的基准场景，可作为未来智能调度算法对照的“数字孪生”底座。

从研究方法论链条看，本课题遵循“数据基准化→DES建模→KPI/Experiment→因子与规则扫描→负荷校准→论文凝练”的递进逻辑，与Law（2015）所强调的仿真研究规范一致；在优化搜索层面，当前阶段以全因子网格为主（EXP-002/003），后续可逐步引入OptQuest或借鉴Chen等（2013）的PSO+OCBA进行连续/离散混合寻优。在绩效测度层面，将同步推进MakeSpan口径统一（Mold截面 vs Sink整线）与Penalty触发机制分析，避免KPI混用导致结论不可比（Chen-Ritzo等，2011）。

从数据与实验条件看，41张订单的一周基准、459台设备规模及DA/WB换型参数均来自项目组已验证的Model3.0与SPAN数据集，实验数字（EXP-001：Objective=54.88；EXP-002：Objective_min=50.61，Penalty_max=760；EXP-003：Objective_min=52.38，Penalty_max=700）已登记于CLAIMS与实验记录，保证开题报告与后续论文数字可追溯。第七次项目组会议（2026年5月23日）进一步明确了ReleaseDate/DueDate基准化、MakeSpan全局记录及EDD释放等实施优先级，与本开题方案一致。

综上，本课题在理论层面衔接HFSP调度、批次拆分与多目标仿真优化文献；在实践层面面向典型存储类封装后端脱敏场景；在方法层面以Simio DES+Experiment为主干，吸收派工规则与SO文献成果，形成具有可验证实验基础的管理科学与工程硕士研究方案。

4. 主要参考文献"""

SECTION2 = r"""1. 研究目标、研究内容和拟解决的关键问题

1.1 研究目标

本研究旨在面向典型存储类半导体封装后端产线，构建可运行的Simio离散事件仿真模型，并在加权多目标框架下开展批次因子与释放/派工策略的仿真优化与情景对比。具体目标包括：（1）建立涵盖六工序、三级批次、搬运与换型逻辑的DES模型，实现与行业脱敏订单及设备数据的可重复绑定；（2）以MakeSpan最小化与延期惩罚最小化为核心，构建Objective=0.7×MakeSpan+0.3×Penalty的Experiment绩效体系，通过Scenario Generator对MLotFactor、SubLotFactor及EDD等策略进行网格扫描与对比；（3）识别效率—准交权衡下的较优参数区间及瓶颈工序，为学位论文提供可验证的实验结论与管理启示。

1.2 研究内容

（1）数据基准化与流程建模。基于行业脱敏订单数据，完成ReleaseDate/DueDate基准化（41张订单代表一周负荷；DueDate=ReleaseDate+交期间隔），建立Materials、Orders、MachineConfig等数据绑定；在Simio中实现六工序主流程及MLot→Magazine→SubLot三级批次结构，加工时间按CurrentQty/UPH计算，DA/WB换型含搬运3分钟与设置10分钟。

（2）绩效指标与Experiment框架。定义MakeSpan、Penalty及加权Objective三个Response；将MLotFactor、SubLotFactor设为Model Properties并接入Scenario Generator，开展二维因子网格实验；明确MakeSpan统计口径（当前采用Mold工序截面时刻Mold_T_End，并与Sink整线LastDepartureTime口径对照验证）。

（3）交期驱动释放与派工策略。在Source及首队列引入EDD规则（按DueDate或DueDate−ReleaseDate升序释放与派工），对比先进先出（FIFO）等基线；开展EXP-004及后续对比实验，评估Penalty与Objective改善幅度。

（4）负荷校准与敏感性分析。通过订单复制、压缩ReleaseDate窗口或调整有效设备规模等方式，将DA/WB利用率提升至可反映瓶颈特征的水平（目标区间约50%—90%），在此基础上重复因子网格与派工对比，分析结论稳健性。

1.3 拟解决的关键问题

（1）批次因子如何影响WIP、MakeSpan与Penalty？不同MLotFactor/SubLotFactor组合是否呈现可解释的权衡规律？（2）订单释放顺序与队列派工规则如何影响准交绩效？Source层EDD与Excel行序调整的效果边界何在？（3）在负荷校准条件下，如何识别DA/WB/Mold等瓶颈工序并解释Experiment最优情景的运作机制？

2. 拟采取的研究思路与方法、技术路线、实验方案及可行性分析

2.1 研究思路与技术路线

研究分四阶段推进：①订单数据ReleaseDate/DueDate基准化与SPAN数据集固化；②完善Simio六工序模型（Model3.0）及Experiment绩效体系；③开展批次因子网格、EDD策略及负荷校准实验；④汇总结果、撰写学位论文。

技术路线如下：行业脱敏数据准备→Simio DES建模（六工序+批次+搬运+换型）→定义MakeSpan/Penalty/Objective→Scenario Generator因子扫描→EDD释放/派工优化→负荷敏感性实验→结论与论文定稿。

2.2 研究方法

（1）离散事件仿真法。采用Simio构建封装后端系统模型，通过多次重复运行（Replications）估计响应均值，遵循Law（2015）所述建模—验证—实验设计流程。

（2）仿真优化与全因子实验设计。以MLotFactor、SubLotFactor为可控因子，利用Scenario Generator构造网格场景；Primary Response设为Objective，对比各情景MakeSpan、Penalty及综合目标，方法上对标Lin和Chen（2015）、Chen等（2013）的SO框架；后续可探索OptQuest/metaheuristic接入。

（3）派工与释放规则对比法。以Panwalkar和Iskander（1977）所述EDD为交期驱动基准，与FIFO对比，并结合第七次项目组会议（2026年5月23日）决议，在Source与Server Selection Rule层协同实现。

（4）情景分析与敏感性分析。参照Stubbe和Rose（2011）、Lee和Lee（2011）的做法，在不同负荷水平、因子水平下比较系统绩效，解释Penalty触发条件与瓶颈迁移现象。

2.3 实验方案

基准实验（EXP-001）验证Objective计算链路；SPAN数据下26场景因子全网格（EXP-002）识别较优因子区间；调整订单释放顺序的复跑（EXP-003）检验Source逻辑必要性；计划中的EXP-004实现DueDate升序EDD释放并与EXP-002最优因子附近情景对比。Ending Time设为100—144小时量级，以全部41单完成为准；Warm-up期按基准化方案处理1/9之前历史为预热窗口。

2.4 可行性分析

项目组已完成AUTO_Model2.0/3.0，涵盖六工序Server流程、三级批次、Worker搬运及DA/WB换型；459台设备配置与41单100%完成流转已验证。Experiment体系已定义MakeSpan、Penalty、Objective，MLotFactor与SubLotFactor已接入Model Properties。EXP-001验证Objective计算正确（MakeSpan=78.40，Objective=54.88）；EXP-002在26个场景下Objective最优值为50.61（MLotFactor=1.0，SubLotFactor=0.75），Penalty最高760；EXP-003表明仅调整订单表顺序不足以替代Source层EDD。导师科研项目提供数据与领域指导，Simio平台与脱敏数据条件齐备，研究方案可行。

3. 研究的特色与创新点

（1）在单一Simio模型中集成六工序、Worker搬运、DA/WB换型及三级批次结构，贴近OSAT后端实际逻辑，克服简化流水模型对封装场景刻画不足的问题。

（2）将批次因子与Experiment Scenario Generator联动，形成可复现的二维参数网格与加权多目标响应体系，为MakeSpan—Penalty权衡提供量化实验证据。

（3）在统一DES框架下联合考察批次缩放与EDD释放/派工策略，对接项目组已积累的EXP-001—003结果，并为后续负荷校准与OptQuest扩展预留方法接口。

4. 研究工作计划

2026年6—8月：完成ReleaseDate/DueDate基准化，统一MakeSpan口径，开展负荷校准实验；2026年9—12月：实现Source与队列EDD，完成EXP-004及派工对比；2027年1—3月：扩展因子水平与稳健性分析，整理实验图表；2027年4—5月：撰写、修改学位论文并准备答辩。

5. 预期研究成果

（1）硕士学位论文1篇，题目为《多目标优化的半导体后端制造生产排程研究》；（2）可运行的Simio封装后端仿真模型及脱敏实验数据集；（3）批次因子与释放/派工策略的对比实验结论，含MakeSpan、Penalty、Objective定量结果及瓶颈分析；（4）可复用的Experiment配置与实验记录，支撑后续期刊论文或项目报告撰写。"""

SECTION3 = r"""1. 与本项目有关的研究工作积累和已取得的研究工作成绩

（1）仿真模型建设。已完成AUTO_Model2.0及Model3.0-batchfactors版本，涵盖六工序Server流程（D/S→DA→WB→Mold→B/G→Taping）、三级批次拆分与合并（Separator_MLot/Separator_Mag/Separator_SubLot及Combiner_Sub）、Worker搬运及DA/WB换型逻辑。设备规模：D/S 31台、DA 112台、WB 284台、Mold 7台、B/G 17台、Taping 8台，合计459台。各Server加工时间按OrderEntity.CurrentQty/Materials.UPH计算，DA/WB换型含Transfer 3分钟与Setup 10分钟（MaterialID/Group变化触发）。

（2）Experiment与数据体系。已定义MakeSpan（当前为Mold_T_End）、Penalty与Objective=0.7×MakeSpan+0.3×Penalty三个Response；MLotFactor、SubLotFactor已定义为Model Properties并接入Scenario Generator。行业脱敏SPAN基准数据集（41张订单）已用于EXP-002/003网格实验。

（3）初步实验结果。EXP-001（基准，MLot=SubLot=1.0）：MakeSpan=78.40，Penalty=0，Objective=54.88。EXP-002（26场景因子网格）：Objective最优50.61（MLot=1.0，SubLot=0.75），Penalty最高760。EXP-003（Orders按DueDate降序后复跑）：Objective最优52.38（0.75/0.5），Penalty最高700，表明释放顺序须与Source逻辑协同而非仅调整表格行序。上述实验记录、架构说明与决策文档（DECISIONS D-001—D-008）已纳入项目版本管理。

（4）文献与开题准备。已系统研读项目参考文献文件夹及半导体排程、仿真优化、多目标调度等领域文献，完成开题报告撰写与模板填表脚本，建立BIBLIOGRAPHY.yaml文献真源与脱敏 CLAIMS 登记表。

2. 已具备的实验、资料等条件，尚缺少的实验、资料条件和拟解决的途径

2.1 已具备条件

Simio软件及Model3.0源文件；行业脱敏订单、物料与设备配置数据（含SPAN基准集）；模型架构文档（AUTO_Model2.0_Architecture_Document.md）；Experiment初步结果（EXP-001—003）；导师科研项目指导与每周进度沟通机制（项目组第七次会议，2026年5月23日）。

2.2 尚缺条件与解决途径

（1）设备利用率偏低。当前原始场景各工序平均利用率约13%，距反映瓶颈的负荷水平差距较大。拟通过复制订单并压缩ReleaseDate窗口、参考V1/V2扩容实验（×5/×6）或调整有效DA/WB台数等方式开展负荷敏感性实验，寻求DA/WB利用率进入50%—90%区间的标定场景。

（2）Magazine/批次口径。Quantity per magazine等字段含义需与导师及行业规范对照确认，避免批次因子物理意义与模型表达式不一致。

（3）MakeSpan全局定义。当前Experiment暂用Mold_T_End，与导师提出的“从0时刻至最后一单离开Sink”整线MakeSpan（LastDepartureTime）尚待统一；拟在Sink增加状态记录并与Mold截面口径对比，在论文中明确统计口径。

（4）Source层EDD尚未完全实现。EXP-003表明仅调整Excel行序不足；下一阶段修改Source_Orders释放逻辑与各Server Selection Rule为EDD（DueDate升序），开展EXP-004并与EXP-002最优因子附近情景对比Penalty改善幅度。

（5）潜在OptQuest/元启发式扩展。当前以Scenario Generator网格扫描为主；待基准协议稳定后，可探索OptQuest或借鉴Lin和Chen（2015）、Chen等（2013）的GA/PSO+OCBA思路进行连续参数寻优，作为后续拓展而非开题阶段必达项。"""
