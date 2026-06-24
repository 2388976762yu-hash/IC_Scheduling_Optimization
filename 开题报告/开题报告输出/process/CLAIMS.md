# 事实断言登记表

> 开题正文中的每个关键事实须在此登记：**脱敏表述**、**内部真源**、**引用键**。

| ID | 脱敏表述（写入正文） | 内部真源 | 引用键 |
|----|---------------------|----------|--------|
| C-001 | 六工序封装后端：D/S→DA→WB→Mold→B/G→Taping | Architecture §1.2 | — |
| C-002 | 459 台加工设备，DA/WB 为关键资源 | Architecture §2.1 | — |
| C-003 | 41 张订单代表一周基准负荷 | DECISIONS D-007; 会议纪要 | — |
| C-004 | 三级批次：MLot→Magazine→SubLot | Architecture §6 | — |
| C-005 | Objective = 0.7×MakeSpan + 0.3×Penalty | DECISIONS D-004 | — |
| C-006 | EXP-001：MakeSpan=78.40, Penalty=0, Objective=54.88 | EXP-001 | — |
| C-007 | EXP-002：26 场景，Objective_min=50.61 (1.0/0.75) | EXP-002 | — |
| C-008 | EXP-002：Penalty_max=760 | EXP-002 | — |
| C-009 | EXP-003：Objective_min=52.38 (0.75/0.5), Pen_max=700 | EXP-003 | — |
| C-010 | 加工时间 = CurrentQty / UPH | Architecture §2.2 | — |
| C-011 | DA/WB 换型：Transfer 3min + Setup 10min | 00_项目接手总说明 §3 | — |
| C-012 | MakeSpan 暂用 Mold_T_End（待统一 Sink） | DECISIONS D-002, T-001 | — |
| C-013 | MLotFactor/SubLotFactor 为 Model Properties | DECISIONS D-003 | — |
| C-014 | 下一步：EDD 释放 + 队列派工 | EXP-002/003 待优化项 | — |
| C-015 | 文件夹参考文献 3 篇唯一 PDF 均已纳入 | 项目辅助材料/参考文献 | lin2015, hoppe2025, luttmann2026 |
| C-016 | Panwalkar 综述年份为 1977（非 1993） | REFERENCE_VERIFICATION | panwalkar1977 |

## 脱敏映射示例

| 禁止写入正文 | 正文改用 |
|--------------|----------|
| 内部项目代号数据文件名 | 「行业脱敏 SPAN 基准数据集」 |
| 企业合作背景 | 「典型存储类半导体封装后端产线（已脱敏）」 |
