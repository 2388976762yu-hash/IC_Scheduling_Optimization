# 项目文档中心

本目录为 **Git 主维护** 的文档区，服务于日常推进与硕士论文撰写。

## 文档地图

| 路径 | 用途 | 更新频率 |
|------|------|----------|
| [`status/CURRENT_STATUS.md`](status/CURRENT_STATUS.md) | **当前状态**：阶段、待办、阻塞项 | 每周 / 有重大进展时 |
| [`process/CHANGELOG.md`](process/CHANGELOG.md) | **变更日志**：按日期记录做了什么 | 每次提交前 |
| [`process/DECISIONS.md`](process/DECISIONS.md) | **决策记录**：为什么这样选 | 有重要决策时 |
| [`experiments/EXPERIMENT_LOG.md`](experiments/EXPERIMENT_LOG.md) | **实验总表**：所有 Experiment 索引 | 每次实验后 |
| [`experiments/records/`](experiments/records/) | **单次实验详情** | 每次实验一篇 |
| [`thesis/THESIS_NOTES.md`](thesis/THESIS_NOTES.md) | **论文素材**：可写入绪论/方法/实验的要点 | 随研究积累 |
| [`../开题报告/开题报告输出/00_INDEX.md`](../开题报告/开题报告输出/00_INDEX.md) | **开题报告输出**（正文真源、文献、脱敏） | 开题阶段 |

## 与其他目录的关系

| 外部材料 | 关系 |
|----------|------|
| `项目辅助材料/00_项目接手总说明.md` | 人类向总说明（较大，少改） |
| `项目辅助材料/AI_项目过程文档.md` | AI 跨会话上下文（与 status/CHANGELOG 同步摘要） |
| `项目辅助材料/会议纪要/` | 会议原始记录；**决议**摘录到 DECISIONS.md |
| `04_Output/*.csv` | 原始报告；**结论**写入 experiments/records/ |

## 推荐工作流

1. 跑完 Simio / Experiment → 在 `experiments/records/` 新建 `EXP-xxx.md`
2. 更新 `experiments/EXPERIMENT_LOG.md` 一行索引
3. 更新 `status/CURRENT_STATUS.md` 待办勾选
4. 在 `process/CHANGELOG.md` 追加日期条目
5. `git commit`

## 实验编号规则

`EXP-001`, `EXP-002`, … 按时间递增。文件名示例：

`experiments/records/EXP-001_experiment1_baseline.md`
