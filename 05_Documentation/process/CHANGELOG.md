# 项目变更日志

按时间倒序记录（新的在上）。

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
