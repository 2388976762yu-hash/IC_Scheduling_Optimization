# Git 与网络（Clash 代理）

> **最后更新**：2026-06-25  
> 本机访问 GitHub **需走 Clash**；直连常出现 `Could not resolve host` / `443 连不上` / `Connection reset`。

## 本机 Clash 端口

| 项 | 值 |
|----|-----|
| 客户端 | Clash for Windows |
| 混合端口 | **7890**（`127.0.0.1:7890`） |
| 使用前 | 确认 Clash 已启动且 **System Proxy / 系统代理** 已开（可选，见下） |

端口若改过，以 Clash 面板 **Port / 混合端口** 为准。

## 推荐：Git 固定走 Clash（一次性配置）

在 PowerShell 中执行（端口非 7890 请替换）：

```powershell
git config --global http.proxy  http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

验证：

```powershell
git config --get https.proxy
git ls-remote origin HEAD
```

取消代理：

```powershell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 临时：单次 push 走 Clash

不改 git config 时：

```powershell
$env:HTTP_PROXY  = "http://127.0.0.1:7890"
$env:HTTPS_PROXY = "http://127.0.0.1:7890"
git push origin main
```

或使用项目脚本：

```powershell
.\scripts\push-via-clash.ps1
```

## Cursor / AI Agent 说明

- Agent 在终端里跑 `git push` 时**不会自动走 Clash**，除非已设置 `git config` 代理或上述环境变量。
- 此前 push 失败多为 **Agent  shell 未配代理**；配置 `--global http(s).proxy` 后 Agent 与本地终端行为一致。

## 故障排查

| 现象 | 处理 |
|------|------|
| `Could not resolve host: github.com` | 开 Clash；设代理后重试 |
| `Failed to connect ... port 443` | 同上；检查 7890 是否在监听 |
| `Connection was reset` | 换节点 / 重开 Clash 后再 push |
| push 成功但很慢 | 正常；可换 GitHub 友好节点 |

检查端口：

```powershell
netstat -ano | findstr 7890
Get-Process Clash* -ErrorAction SilentlyContinue
```

## 远程仓库

```
origin  https://github.com/2388976762yu-hash/IC_Scheduling_Optimization.git
branch  main
```
