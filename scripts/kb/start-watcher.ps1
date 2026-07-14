<#
.SYNOPSIS
    Starts the continuous opencode DB watcher in background.
.DESCRIPTION
    Launches watch-opencode-db.py as a hidden PowerShell process.
    Polls SQLite every 30s, detects session changes, runs pipeline.
    Creates a watchdog file that can be checked for health.
.PARAMETER Interval
    Polling interval in seconds (default: 30)
.PARAMETER Settle
    Seconds of stability before processing a session (default: 120)
.PARAMETER Log
    Log file path (default: scripts/kb/watcher.log)
.EXAMPLE
    .\scripts\kb\start-watcher.ps1
    .\scripts\kb\start-watcher.ps1 -Interval 15 -Settle 60
#>

param(
    [int]$Interval = 30,
    [int]$Settle = 120
)

$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$WatcherScript = Join-Path $AITutorDir "scripts\kb\watch-opencode-db.py"

# Check if already running
$existing = Get-Process -Name "python*" -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -like "*watch-opencode-db*"
}

if ($existing) {
    Write-Host "[Watcher] Already running (PID: $($existing.Id))" -ForegroundColor Yellow
    exit 0
}

# Start in background
$logFile = Join-Path $AITutorDir "scripts\kb\watcher.log"
$args = "-u", $WatcherScript, "--interval", $Interval, "--settle", $Settle, "--watchdog"

try {
    $process = Start-Process -FilePath "python" -ArgumentList $args -WindowStyle Hidden -PassThru -NoNewWindow -RedirectStandardOutput "$logFile.tmp"
    Write-Host "[Watcher] Started (PID: $($process.Id))" -ForegroundColor Green
    Write-Host "[Watcher] Polling every ${Interval}s, settle ${Settle}s" -ForegroundColor Cyan
    Write-Host "[Watcher] Log: $logFile" -ForegroundColor Gray
} catch {
    Write-Host "[Watcher] Failed to start: $_" -ForegroundColor Red
    exit 1
}

# Create a status marker
$statusFile = Join-Path $AITutorDir "scripts\kb\.watcher_running"
$process.Id | Out-File -FilePath $statusFile -Encoding utf8
