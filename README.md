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

**Push 走 Clash**：本机需经 Clash 访问 GitHub，详见 [`05_Documentation/process/GIT_AND_NETWORK.md`](05_Documentation/process/GIT_AND_NETWORK.md)（混合端口 **7890**）。

```powershell
# 推荐：一次性配置 git 代理
git config --global http.proxy  http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890

# 日常：改模型/跑实验后
git status
git add 05_Documentation/ 02_Simulation_Model/AUTO_Model2.0.spfx
git commit -m "描述本次改动"
git push origin main

# 或临时单次 push
.\scripts\push-via-clash.ps1
```

```bash
# 实验完成后：更新实验日志
# 编辑 05_Documentation/experiments/EXPERIMENT_LOG.md
```

## 远程仓库

已配置：

```
https://github.com/2388976762yu-hash/IC_Scheduling_Optimization.git  (main)
```

## 许可证

学术研究项目；Simio 模型文件为 Academic 版，勿用于商业用途。
