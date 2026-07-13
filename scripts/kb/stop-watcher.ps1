<#
.SYNOPSIS
    Stops the opencode DB watcher.
.DESCRIPTION
    Kills the watch-opencode-db.py process.
#>

$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent

$processes = Get-Process -Name "python*" -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -like "*watch-opencode-db*"
}

if (-not $processes) {
    Write-Host "[Watcher] Not running" -ForegroundColor Yellow
    # Clean up stale status file
    $statusFile = Join-Path $AITutorDir "scripts\kb\.watcher_running"
    if (Test-Path $statusFile) { Remove-Item $statusFile }
    exit 0
}

foreach ($p in $processes) {
    Write-Host "[Watcher] Stopping PID $($p.Id)..." -ForegroundColor Yellow
    Stop-Process -Id $p.Id -Force
    Write-Host "[Watcher] Stopped" -ForegroundColor Green
}

# Clean up
$statusFile = Join-Path $AITutorDir "scripts\kb\.watcher_running"
if (Test-Path $statusFile) { Remove-Item $statusFile }
