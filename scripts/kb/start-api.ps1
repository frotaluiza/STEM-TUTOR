<#
.SYNOPSIS
    Inicia a API REST dos project-states.
    Por padrão roda em http://localhost:8080
    Acessível pelo DeepTutor e PM.

.PARAMETER Port
    Porta da API (default: 8080)
.PARAMETER BindHost
    Host de bind (default: 127.0.0.1)
.PARAMETER Background
    Se true, inicia em background (sem janela)
#>

param(
    [int]$Port = 8080,
    [string]$BindHost = "127.0.0.1",
    [switch]$Background = $false
)

$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$ApiModule = "scripts.api.main:app"
$LogFile = Join-Path $AITutorDir "scripts\api\api-server.log"

# Verifica se já está rodando
$existing = Get-Process -Name "python*" -ErrorAction SilentlyContinue | Where-Object {
    $_.CommandLine -like "*$ApiModule*"
}
if ($existing) {
    Write-Host "[API] Já está rodando (PID: $($existing.Id)) em http://localhost:$Port" -ForegroundColor Yellow
    exit 0
}

$cmd = "python -m uvicorn $ApiModule --host $BindHost --port $Port --reload --log-level warning"

if ($Background) {
    Write-Host "[API] Iniciando em background..." -ForegroundColor Cyan
    $process = Start-Process -FilePath "python" -WindowStyle Hidden -WorkingDirectory $AITutorDir -ArgumentList @(
        "-m", "uvicorn", $ApiModule, "--host", $BindHost, "--port", $Port.ToString(), "--log-level", "warning"
    ) -PassThru -RedirectStandardOutput $LogFile
    Start-Sleep -Seconds 2
    Write-Host "[API] Rodando em http://localhost:$Port (PID: $($process.Id))" -ForegroundColor Green
    $process.Id | Out-File -FilePath (Join-Path $AITutorDir "scripts\api\.api_pid") -Encoding utf8
} else {
    Write-Host "[API] Iniciando em http://localhost:$Port" -ForegroundColor Cyan
    Write-Host "[API] Pressione Ctrl+C para parar" -ForegroundColor Gray
    Invoke-Expression $cmd
}
