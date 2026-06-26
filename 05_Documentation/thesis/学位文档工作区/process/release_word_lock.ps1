# 开题报告 doc 解锁：结束占用 Word/WPS，清除只读属性
# 用法：
#   .\release_word_lock.ps1              # 仅结束 WINWORD
#   .\release_word_lock.ps1 -CloseWps    # 同时结束标题含「开题报告」的 WPS 窗口

param(
    [switch]$CloseWps
)

$doc = Join-Path $PSScriptRoot "..\02_开题报告_提交版.doc"
$template = Join-Path $PSScriptRoot "..\..\2120253828-喻炫琪-研究生开题报告.doc"

$procs = Get-Process -Name WINWORD -ErrorAction SilentlyContinue
if ($procs) {
    $procs | Stop-Process -Force
    Write-Host "已结束 WINWORD 进程: $($procs.Id -join ', ')"
} else {
    Write-Host "未发现 WINWORD 进程。"
}

if ($CloseWps) {
    $wps = Get-Process wps -ErrorAction SilentlyContinue |
        Where-Object { $_.MainWindowTitle -match '开题报告' }
    if ($wps) {
        $wps | Stop-Process -Force
        Write-Host "已结束 WPS 开题报告窗口: $($wps.Id -join ', ')"
    } else {
        Write-Host "未发现标题含「开题报告」的 WPS 窗口（若仍锁文件，请手动关标签页）。"
    }
}

foreach ($path in @($doc, $template)) {
    if (Test-Path $path) {
        attrib -R $path
        Write-Host "已清除只读属性: $path"
    }
}

Write-Host ""
Write-Host "工作前检查: python ensure_doc_closed.py"
Write-Host "自动解锁并重检: python ensure_doc_closed.py --close"
Write-Host "若 WPS 仍显示[只读]，请关闭该文档标签后重新打开。"
