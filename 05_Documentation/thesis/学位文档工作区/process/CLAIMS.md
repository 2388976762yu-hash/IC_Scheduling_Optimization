# 事实断言登记表

> 开题正文关键事实在此登记：**脱敏表述**（写入 `section_content.py`）、**内部真源**、**引用键**。  
> 写作策略见 [`WRITING_RULES.md`](WRITING_RULES.md) §4：正文用「脱敏表述」列中文实验名，**不用**内部 EXP 编号。

| ID | 脱敏表述（写入正文） | 内部真源 | 引用键 |
|----|---------------------|----------|--------|
| C-001 | 六工序封装后端：Taping→BG→DS→DA→WB→MOLD | MODEL_TRUTH §1；Excel MachineConfig | — |
| C-002 | 459 台 Server：Taping 8、BG 17、DS 31、DA 112、WB 284、MOLD 7 | MODEL_TRUTH §1；Excel MachineConfig | — |
| C-003 | 41 条订单、16 种物料，企业一周排产样本 | Simio_Import_Data Orders/Materials | — |
| C-004 | 批次链：Order→MLot→弹夹批次Magazine→SubLot | Architecture §6.1 | — |
| C-005 | Objective = 0.7×MakeSpan + 0.3×Penalty | DECISIONS D-004 | — |
| C-006 | 基准情景：MakeSpan=78.40, Penalty=0, Objective=54.88（因子均为 1.0） | EXP-001 | — |
| C-007 | 26 情景因子网格扫描：Objective 最优 50.61（MLot=1.0, SubLot=0.75） | EXP-002 | — |
| C-008 | 因子网格扫描：Penalty 最高 760 | EXP-002 | — |
| C-009 | 释放顺序表面对照：Objective 最优 52.38（0.75/0.5），Penalty 最高 700 | EXP-003 | — |
| C-010 | 加工时间 = CurrentQty / UPH | Architecture §2.2 | — |
| C-011 | DA/WB：转入转出搬运各3分钟；物料Group变化时换型Setup 10分钟 | Architecture §9.1 | — |
| C-012 | MakeSpan 暂用 Mold_T_End（待统一 Sink） | DECISIONS D-002, T-001 | — |
| C-013 | MLotFactor/SubLotFactor 为 Model Properties | DECISIONS D-003 | — |
| C-014 | 下一步：交期升序 EDD 释放 + 队列派工 | EXP-002/003 待优化项 | — |
| C-015 | 文件夹参考文献 3 篇唯一 PDF 均已纳入 | 项目辅助材料/参考文献 | lin2015, hoppe2025, luttmann2026 |
| C-016 | Panwalkar 综述年份为 1977（非 1993） | REFERENCE_VERIFICATION | panwalkar1977 |

## 实验名称映射（内部 → 正文）

| 内部真源 | 正文标准用语 |
|----------|--------------|
| EXP-001 | 因子均为 1.0 的基准情景 |
| EXP-002 | 26 情景批次因子全因子网格扫描 |
| EXP-003 | 仅调整订单表释放顺序的对照 |
| 拟开展 | 交期升序释放与 FIFO 的对照实验 |

## 脱敏映射示例

| 禁止写入正文 | 正文改用 |
|--------------|----------|
| 内部项目代号数据文件名 | 「企业脱敏 Simio 导入数据」 |
| 企业合作背景 | 「典型存储类半导体封装后端产线（已脱敏）」 |
