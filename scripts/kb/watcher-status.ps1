<#
.SYNOPSIS
    Check if the watcher is running and show its status.
#>

$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$statusFile = Join-Path $AITutorDir "scripts\kb\.watcher_running"
$watchdogFile = Join-Path $AITutorDir "scripts\kb\.watcher_healthy"
$logFile = Join-Path $AITutorDir "scripts\kb\watcher.log"

$processes = Get-Process -Name "python*" -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -like "*watch-opencode-db*"
}

if ($processes) {
    Write-Host "[Watcher] RUNNING" -ForegroundColor Green
    foreach ($p in $processes) {
        Write-Host "  PID: $($p.Id)" -ForegroundColor Cyan
        Write-Host "  Started: $($p.StartTime)" -ForegroundColor Gray
        Write-Host "  CPU: $($p.CPU)s" -ForegroundColor Gray
        Write-Host "  Memory: $([math]::Round($p.WorkingSet64 / 1MB, 1)) MB" -ForegroundColor Gray
    }
} else {
    Write-Host "[Watcher] NOT RUNNING" -ForegroundColor Red
}

if (Test-Path $watchdogFile) {
    $lastPulse = Get-Content $watchdogFile -Raw
    $since = [datetime]::Now - [datetime]::Parse($lastPulse)
    $color = if ($since.TotalMinutes -gt 5) { "Red" } else { "Green" }
    Write-Host "  Last healthy pulse: $lastPulse ($([math]::Round($since.TotalMinutes, 1)) min ago)" -ForegroundColor $color
}

if (Test-Path $logFile) {
    $lines = Get-Content $logFile -Tail 3
    Write-Host "  Last log lines:" -ForegroundColor Gray
    foreach ($line in $lines) {
        Write-Host "    $line" -ForegroundColor Gray
    }
}
