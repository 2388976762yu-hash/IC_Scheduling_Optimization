# 项目变更日志

按时间倒序记录（新的在上）。

---

## 2026-06-25

### Git push 走 Clash 文档化

- 新增 `process/GIT_AND_NETWORK.md`：Clash 7890、git proxy、Agent 说明
- 新增 `scripts/push-via-clash.ps1`
- 更新根 `README.md`、`05_Documentation/README.md` 工作流

---

## 2026-06-24

### 开题报告重大修订

- 扩展 `section_content.py`：第一节 ~5160 汉字 + 32 篇 GB/T7714 文献列表
- 纳入 `项目辅助材料/参考文献/` 3 篇唯一 PDF（Lin2015、Hoppe2025、Luttmann2026）
- 更正 Panwalkar 引用年份 1977；新增 REFERENCE_VERIFICATION.md
- 重新生成 `02_开题报告_提交版.doc` / `.docx`

---

## 2026-05-24

### 开题报告初稿完成

- 输出目录：`开题报告/开题报告输出/`
- 题目：**多目标优化的半导体后端制造生产排程研究**
- 正文 + Word 提交版 + BIBLIOGRAPHY.yaml（28 篇）+ 脱敏扫描通过
- 索引：THESIS_NOTES.md ↔ 00_INDEX.md

---

## 2026-05-30

### EXP-003：Orders DueDate 降序后因子网格复跑

- 模型：`AUTO_Model3.0-batchfactors.spfx`
- ~25 Scenario × 5 Replication，Ending 100h，运行 ~2412s
- Objective_min **52.38** (0.75/0.5)；Penalty_max **700**
- 相对 EXP-002：最优 Objective 略差，最差 Penalty 略好（760→700）
- 待做：DueDate **升序** + Source EDD（EXP-004）

### EXP-002：SPAN 数据批次因子网格（26 Scenario）

- 数据：`Simio_Import_Data-SPAN.xlsx`，41 单，Ending 100h
- 最优 Objective **50.6132**（MLot=1.0, SubLot=0.75）；最差 291.181（1.25/1.25）
- Penalty 最高 **760**
- **待优化**：Source 订单释放未按 DueTime 紧急度
- GitHub 远程连接并 push

---

## 2026-05-24

### Git 与文档体系

- 初始化 Git 仓库
- 新建 `05_Documentation/`：状态、过程、实验、论文文档结构
- 添加 `.gitignore`（忽略 Simio `.backup`、`old/` 模型等）

### Simio Experiment

- Properties 添加 `MLotFactor`、`SubLotFactor`（从 States 迁移）
- Experiment Controls 接通；Scenario Generator 可用
- Experiment1 跑通：MakeSpan≈78.4、Penalty=0、Objective≈54.88

### 模型指标

- 工序 T_Start/T_End、Penalty 记录实现
- MakeSpan 暂以 `Mold_T_End` 作为 Experiment Response

---

## 2026-05-23

### 第七次会议（导师）

- 主指标：Make Span + 延期罚函数
- Experiment 目标：0.7×MakeSpan + 0.3×Penalty
- ReleaseDate 统一基准日；41 单 = 一周工作量
- 批次大小（M Lot / Sub Lot）作为研究变量
- 每周六晚沟通

---

## 2026-05-24（早些时候）

### 文档与解析

- 更新 `00_项目接手总说明.md` 至 Model 2.0
- `parse_simio_spfx.py` 解压解析 AUTO_Model2.0.spfx
- 创建 `AI_项目过程文档.md`

---

## 更早

- Model 2.0 搭建：Worker、换型、41 单全完成
- V1/V2 仿真实验与 `v1v2_analysis.json`
- Model 1.0 归档至 `02_Simulation_Model/old/`
