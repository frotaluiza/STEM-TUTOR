<#
.SYNOPSIS
    Configura git worktrees para trabalhar em múltiplas branches
    do STEM-TUTOR simultaneamente, cada uma com sua própria API.

.DESCRIPTION
    Cria uma pasta STEM-TUTOR-{branch} para cada branch listada
    e inicia a API em portas sequenciais.

    Uso padrão: mantém a branch atual na pasta original (porta 8080)
    e cria worktrees para as demais (porta 8081, 8082, ...).

.PARAMETER Branches
    Lista de branches para criar worktrees (ex: "main", "feature/x")
    Se vazio, cria apenas para main.

.PARAMETER StartAPIs
    Se true, inicia a API em cada worktree automaticamente.

.EXAMPLE
    .\scripts\kb\worktree-setup.ps1 -Branches "main"
    .\scripts\kb\worktree-setup.ps1 -Branches "main,feature/x" -StartAPIs

.NOTES
    Branch atual (ps/mindmap-v2) fica na pasta original na porta 8080.
    Cada worktree adicional ganha uma porta incremental (8081, 8082...).
#>

param(
    [string[]]$Branches = @("main"),
    [switch]$StartAPIs = $false
)

$RepoDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$BaseName = Split-Path $RepoDir -Leaf  # STEM-TUTOR
$ParentDir = Split-Path $RepoDir -Parent

$currentBranch = git -C $RepoDir rev-parse --abbrev-ref HEAD
Write-Host "[WORKTREE] Branch atual: $currentBranch (porta 8080)" -ForegroundColor Cyan

$port = 8081
foreach ($branch in $Branches) {
    $targetDir = Join-Path $ParentDir "${BaseName}-${branch}"
    if ($branch -eq $currentBranch) {
        Write-Host "[WORKTREE] Pulando $branch (já é a branch atual)" -ForegroundColor Yellow
        continue
    }
    if (Test-Path $targetDir) {
        Write-Host "[WORKTREE] $targetDir já existe" -ForegroundColor Yellow
    } else {
        Write-Host "[WORKTREE] Criando $targetDir → $branch ..." -ForegroundColor Cyan
        git -C $RepoDir worktree add $targetDir $branch 2>&1 | Out-Null
        Write-Host "[WORKTREE] Criada: $targetDir (branch: $branch)" -ForegroundColor Green
    }

    if ($StartAPIs) {
        Write-Host "[WORKTREE] Iniciando API em :$port para $branch ..." -ForegroundColor Cyan
        Start-Process -FilePath "python" -WindowStyle Hidden -WorkingDirectory $targetDir -ArgumentList @(
            "-m", "uvicorn", "scripts.api.main:app", "--host", "127.0.0.1", "--port", $port.ToString(), "--log-level", "warning"
        ) -PassThru | Out-Null
        Write-Host "[WORKTREE] API $branch → http://127.0.0.1:$port" -ForegroundColor Green
        $port++
    }
}

Write-Host "`n[WORKTREE] Resumo:" -ForegroundColor Magenta
Write-Host "  Pasta original: $RepoDir ($currentBranch → :8080)" -ForegroundColor White
foreach ($branch in $Branches) {
    if ($branch -ne $currentBranch) {
        $p = Join-Path $ParentDir "${BaseName}-${branch}"
        Write-Host "  Worktree: $p ($branch)" -ForegroundColor White
    }
}
