# -*- coding: utf-8 -*-
"""中期报告 / 中期考核表正文真源。

中期报告为学院提交件：三节标题不含模板指引语；不设「提纲」字样；
各节下用 1.1 / 1.2 分条，章节之间不插空段（由 fill 脚本写入 Word）。
"""

from __future__ import annotations


def _compact(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if line.strip())


THESIS_TITLE_CN = "多目标优化的半导体后端制造生产排程研究"
THESIS_TITLE_EN = (
    "Multi-Objective Optimization of Production Scheduling in "
    "Semiconductor Backend Manufacturing"
)
KEYWORDS_CN = "半导体封装后端；生产排程；离散事件仿真；多目标优化；Simio"
KEYWORDS_EN = (
    "semiconductor backend packaging; production scheduling; "
    "discrete-event simulation; multi-objective optimization; Simio"
)

# 考核表 Table2 勾选项（在模板原有括号行上打 √，不整格覆盖）
FORM_TOPIC_NATURE = "应用研究"
FORM_ADVISOR_RELATION = "与导师研究课题无关"
FORM_ABSTRACT_HEADER = "一、中期报告摘要"

# 正式三节标题（不含括号内填写说明）
MIDTERM_H1 = "一、学位论文进展情况及已取得阶段性成果"
MIDTERM_H2 = "二、存在的问题与下一步工作计划"
MIDTERM_H3 = "三、已取得研究成果"

MIDTERM_ABSTRACT = _compact(
    """本研究面向典型存储类半导体封装后端产线调度优化问题，以企业脱敏 Simio 导入数据为基准，建立涵盖编带、分拣、装片、键合、塑封、烘烤及切筋六工序的离散事件仿真模型，完整纳入订单释放、Order—MLot—Magazine—SubLot 多级批次链、Worker 搬运输送及 DA/WB 工序换型 Setup 等关键约束。研究采用 MakeSpan 与准交惩罚 Penalty 双指标，构建加权 Objective=0.7×MakeSpan+0.3×Penalty 评价函数，并通过 Experiment 接入 MLotFactor、SubLotFactor 情景生成器开展系统参数扫描。已完成基准情景验证与 26 组批次因子全因子网格实验，基准 MakeSpan 为 78.40，网格扫描 Objective 最优 50.61；另有释放顺序对照实验表明，释放逻辑须与 Source 层交期驱动释放机制协同设计。当前正推进负荷校准、MakeSpan 统计口径统一、Source 层 EDD 释放与队列派工规则对比及与 FIFO 基线对照，为后续学位论文系统实验与正式论文撰写奠定基础。"""
)

MIDTERM_SECTION1 = _compact(
    """1.1 研究进展概况
自开题以来，本研究按「数据基准化—离散事件仿真建模—Experiment 实验—批次因子与释放/派工规则扫描—负荷校准—论文凝练」的技术路线推进，研究内容与开题报告保持一致，围绕典型存储类半导体封装后端产线的 MakeSpan 与准交绩效开展仿真优化研究。
1.2 仿真模型与实验框架
已建立涵盖 D/S→DA→WB→Mold→B/G→Taping 六工序的 Simio 模型，并与企业脱敏 Simio 导入数据绑定：Orders 表 41 条订单、Materials 表 16 种物料、MachineConfig 合计 459 台设备。加工时间按 CurrentQty/UPH 计算；DA/WB 每批转入与转出搬运各 3 分钟，Assigned_DA_Group 变化时触发 10 分钟换型 Setup。订单 Order 经 Separator 链形成 MLot→Magazine（弹夹批次）→SubLot 结构，并纳入 Worker 搬运逻辑。Experiment 已定义 MakeSpan、Penalty 与 Objective=0.7×MakeSpan+0.3×Penalty 三个 Response；MLotFactor、SubLotFactor 作为 Model Properties 接入 Scenario Generator。
1.3 阶段性仿真实验结果
（1）基准情景（因子均为 1.0）：MakeSpan=78.40，Penalty=0，Objective=54.88，41 单均可完整流转，绩效计算链路验证通过。
（2）26 情景 MLotFactor×SubLotFactor 全因子网格扫描：Objective 最优 50.61（MLotFactor=1.0，SubLotFactor=0.75）；部分因子组合 Penalty 高达 760，表明批次缩放与准交约束存在显著非线性耦合。
（3）释放顺序对照实验（仅调整 Orders 表 DueDate 行序、不改 Source 释放逻辑）：Objective 最优 52.38，Penalty 最高 700，表明释放顺序须与 Source 层交期驱动逻辑协同，表序调整不能替代 EDD 释放。
此外，已完成半导体后端排程、批次拆分、DES 与仿真优化、多目标调度等方向的文献研读，开题报告已撰写完成并整理参考文献 32 篇。"""
)

MIDTERM_SECTION2 = _compact(
    """2.1 存在的主要问题
（1）负荷水平偏低：原始场景各工序平均利用率约 13%，喂料不足导致瓶颈判断失真，需在负荷校准后再比较调度策略优劣。
（2）MakeSpan 统计口径待统一：Experiment 当前暂用 Mold 工序截面 Mold_T_End，须并行记录 Sink 整线 LastDepartureTime 并在论文中确定主口径。
（3）交期驱动释放与派工待完善：Source 层 EDD 释放及各设备队列 EDD 派工尚未完全实现，DueDate 升序释放与 FIFO 基线对比实验尚待完成。
（4）批次参数口径待核对：Materials 表 StripsPerMag、QtyPerMag 等字段含义须与封装行业规范逐项对照，确保批次因子物理意义准确。
2.2 下一步工作计划
2026 年 6—8 月：完成 ReleaseDate/DueDate 基准化、MakeSpan 口径统一与负荷校准实验；2026 年 9—12 月：实现 Source 与队列 EDD，完成交期升序释放与 FIFO 对比及较优因子附近稳健性分析；2027 年 1—3 月：整理实验图表、扩展因子水平；2027 年 4—5 月：撰写并修改学位论文。
2.3 论文选题说明
论文选题与开题一致，为《多目标优化的半导体后端制造生产排程研究》，中期阶段不作选题调整。若负荷校准后瓶颈结构发生变化，将在不改变题目前提下补充实验情景说明。"""
)

MIDTERM_SECTION3 = _compact(
    """3.1 已完成的工作成果
（1）完成开题报告及学院表格提交版；
（2）交付可运行的 Simio 六工序封装后端仿真模型（含 Order—MLot—Magazine—SubLot 批次链、Worker 搬运与 DA/WB 换型 Setup）；
（3）形成基准情景、26 情景因子网格及释放顺序对照等实验记录与数据摘要；
（4）整理 32 篇参考文献元数据及引用核实记录。
3.2 发表论文与知识产权
截至目前，尚无正式发表学术论文、授权专利或已录用会议论文。后续将在完成 EDD 与负荷校准等系统实验后，将主要结论凝练为硕士学位论文；视研究进展，再考虑管理科学与工程相关期刊投稿。"""
)


def midterm_report_paragraphs() -> list[str]:
    """Ordered paragraphs for Word body (first item replaces P50 header line)."""
    return [
        MIDTERM_H1,
        *MIDTERM_SECTION1.split("\n"),
        MIDTERM_H2,
        *MIDTERM_SECTION2.split("\n"),
        MIDTERM_H3,
        *MIDTERM_SECTION3.split("\n"),
    ]
