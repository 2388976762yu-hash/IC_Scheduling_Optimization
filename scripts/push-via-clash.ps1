# Push to origin/main via Clash mixed port (default 7890)
param(
    [string]$Port = "7890",
    [string]$Remote = "origin",
    [string]$Branch = "main"
)

$proxy = "http://127.0.0.1:$Port"
$env:HTTP_PROXY = $proxy
$env:HTTPS_PROXY = $proxy

Write-Host "Using proxy $proxy"
git push -u $Remote $Branch
exit $LASTEXITCODE
