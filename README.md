# IC 后端制造排程优化仿真项目

SanDisk 半导体后端制造场景的 Simio 离散事件仿真与排程优化研究。

## 当前状态

- **主模型**：`02_Simulation_Model/AUTO_Model2.0.spfx`
- **文档入口**：[`05_Documentation/README.md`](05_Documentation/README.md)
- **接手说明**：[`项目辅助材料/00_项目接手总说明.md`](项目辅助材料/00_项目接手总说明.md)

## 目录结构

| 目录 | 说明 |
|------|------|
| `01_Data/` | Simio 导入数据、调优 Excel |
| `02_Simulation_Model/` | `.spfx` 模型、架构文档、解析结果 |
| `03_Algorithm/` | Python 脚本（spfx 解析、数据预处理） |
| `04_Output/` | 仿真报告 CSV、分析 JSON |
| `05_Documentation/` | **过程 / 状态 / 实验 / 论文** 文档（Git 主维护） |
| `项目辅助材料/` | 会议纪要、原始业务资料、AI 上下文 |

## Git 使用建议

```bash
# 日常：改模型/跑实验后
git status
git add 05_Documentation/ 02_Simulation_Model/AUTO_Model2.0.spfx
git commit -m "描述本次改动"

# 实验完成后：更新实验日志
# 编辑 05_Documentation/experiments/EXPERIMENT_LOG.md
```

## 远程仓库（自行创建后）

```bash
git remote add origin <你的仓库 URL>
git branch -M main
git push -u origin main
```

## 许可证

学术研究项目；Simio 模型文件为 Academic 版，勿用于商业用途。
