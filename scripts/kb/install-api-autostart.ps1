<#
.SYNOPSIS
    Instala a API REST dos project-states como tarefa do Windows
    para iniciar automaticamente no login do usuário.

.DESCRIPTION
    Cria uma tarefa no Task Scheduler que:
    - Inicia a API automaticamente no login
    - Roda em background (sem janela)
    - Reinicia se falhar
    - Porta 8080 por padrão

.PARAMETER Port
    Porta da API (default: 8080)
.PARAMETER Remove
    Remove a tarefa de auto-início
#>

param(
    [int]$Port = 8080,
    [switch]$Remove = $false
)

$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$TaskName = "ProjectOrchestratorAPI"
$ScriptPath = Join-Path $AITutorDir "scripts\kb\start-api.ps1"

if ($Remove) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
    Write-Host "[AUTOSTART] Tarefa '$TaskName' removida." -ForegroundColor Yellow
    exit 0
}

$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument @"
-NoProfile -WindowStyle Hidden -File "$ScriptPath" -Port $Port -Background
"@

$Trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME

$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 1)

$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -RunLevel Limited

try {
    Register-ScheduledTask -TaskName $TaskName `
        -Action $Action `
        -Trigger $Trigger `
        -Settings $Settings `
        -Principal $Principal `
        -Force

    Write-Host "[AUTOSTART] Tarefa '$TaskName' instalada!" -ForegroundColor Green
    Write-Host "[AUTOSTART] A API iniciará automaticamente no próximo login." -ForegroundColor Cyan
    Write-Host "[AUTOSTART] Para iniciar agora sem esperar o login:" -ForegroundColor Gray
    Write-Host "  .\scripts\kb\start-api.ps1 -Background" -ForegroundColor White
} catch {
    Write-Host "[AUTOSTART] Erro ao instalar: $_" -ForegroundColor Red
    Write-Host "Tente executar como Administrador ou use o modo manual:" -ForegroundColor Yellow
    Write-Host "  .\scripts\kb\start-api.ps1 -Background" -ForegroundColor White
}
