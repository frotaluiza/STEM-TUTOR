<#
.SYNOPSIS
    Installs the watcher as a Windows Task Scheduler task that starts at user login.
.DESCRIPTION
    Creates a task "KB Watcher - AI STEM Tutor" that runs watch-opencode-db.py
    in the background whenever the user logs in.
.PARAMETER Uninstall
    Remove the scheduled task.
#>

param([switch]$Uninstall)

$TaskName = "KB Watcher - AI STEM Tutor"
$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$PythonExe = (Get-Command python).Source
$WatcherScript = Join-Path $AITutorDir "scripts\kb\watch-opencode-db.py"
$LogFile = Join-Path $AITutorDir "scripts\kb\watcher.log"

if ($Uninstall) {
    Write-Host "[Task] Removing scheduled task '$TaskName'..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "[Task] Removed" -ForegroundColor Green
    exit 0
}

# Build the action
$Action = New-ScheduledTaskAction -Execute $PythonExe -Argument "-u `"$WatcherScript`" --interval 30 --settle 120 --watchdog" -WorkingDirectory $AITutorDir

# Trigger at logon
$Trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME

# Run whether user is logged on or not, with lowest priority
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -Priority 7

# Run as current user
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType S4U -RunLevel Limited

try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal -Force
    Write-Host "[Task] Created '$TaskName'" -ForegroundColor Green
    Write-Host "[Task] Python: $PythonExe" -ForegroundColor Gray
    Write-Host "[Task] Script: $WatcherScript" -ForegroundColor Gray
    Write-Host "[Task] Triggers: At logon of $env:USERNAME" -ForegroundColor Gray
    Write-Host ""
    Write-Host "[Task] To start now:" -ForegroundColor Cyan
    Write-Host "  Start-ScheduledTask -TaskName '$TaskName'" -ForegroundColor White
    Write-Host "[Task] To remove:" -ForegroundColor Cyan
    Write-Host "  .\scripts\kb\install-watcher-task.ps1 -Uninstall" -ForegroundColor White
} catch {
    Write-Host "[Task] Failed: $_" -ForegroundColor Red
    exit 1
}
