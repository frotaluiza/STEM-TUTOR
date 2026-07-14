<#
.SYNOPSIS
    Inicializa o ambiente de trabalho. Verifica git, Notion API,
    dependências, e prepara o repositório Projetos/ para alterações.

.DESCRIPTION
    - Verifica se git está instalado
    - Verifica se o repositório Projetos/ existe e está clonado
    - Verifica branch atual e sugere criar branch de sessão
    - Verifica NOTION_API_KEY (se aplicável)
    - Verifica dependências Python
    - Inicia watcher de project-state (opcional)

.PARAMETER CheckNotion
    Se true, verifica se NOTION_API_KEY está configurada
.PARAMETER StartWatcher
    Se true, inicia o watch-project-state.ps1 em background
.PARAMETER SessionSlug
    Slug da sessão para criar branch automática
#>

param(
    [switch]$CheckNotion = $false,
    [switch]$StartWatcher = $false,
    [string]$SessionSlug = ""
)

$ErrorActionPreference = "Stop"
$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$ProjetosDir = Join-Path $AITutorDir "Projetos"

function Write-Status {
    param([string]$Label, [string]$Status, [string]$Color)
    Write-Host "[$Label] $Status" -ForegroundColor $Color
}

function Test-GitSetup {
    Write-Status "GIT" "Verificando..." "Cyan"
    try {
        $version = git --version
        Write-Status "GIT" "OK ($version)" "Green"
        return $true
    } catch {
        Write-Status "GIT" "FALHA — git não encontrado" "Red"
        return $false
    }
}

function Test-RepoSetup {
    Write-Status "REPO" "Verificando $ProjetosDir..." "Cyan"
    if (-not (Test-Path $ProjetosDir)) {
        Write-Status "REPO" "FALHA — $ProjetosDir não existe" "Red"
        return $false
    }
    if (-not (Test-Path (Join-Path $ProjetosDir ".git"))) {
        Write-Status "REPO" "AVISO — Projetos/ não é um repositório git" "Yellow"
        return $false
    }
    $branch = git -C $ProjetosDir rev-parse --abbrev-ref HEAD
    Write-Status "REPO" "OK — branch: $branch" "Green"

    if ($SessionSlug) {
        $expected = "sessao/$SessionSlug"
        if ($branch -eq "main" -or $branch -eq "master") {
            Write-Status "BRANCH" "Criando $expected..." "Cyan"
            git -C $ProjetosDir checkout -b $expected 2>&1 | Out-Null
            Write-Status "BRANCH" "OK — criada $expected" "Green"
        } elseif ($branch -eq $expected) {
            Write-Status "BRANCH" "OK — já está em $expected" "Green"
        } else {
            Write-Status "BRANCH" "AVISO — em $branch, esperado $expected" "Yellow"
        }
    }

    return $true
}

function Test-PythonSetup {
    Write-Status "PYTHON" "Verificando..." "Cyan"
    try {
        $version = python --version 2>&1
        Write-Status "PYTHON" "OK ($version)" "Green"
        return $true
    } catch {
        Write-Status "PYTHON" "FALHA — python não encontrado" "Red"
        return $false
    }
}

function Test-NotionKey {
    if (-not $CheckNotion) { return }
    Write-Status "NOTION" "Verificando API key..." "Cyan"

    # Checar em variável de ambiente primeiro
    $key = $env:NOTION_API_KEY
    if (-not $key) {
        # Checar em .env
        $envFile = Join-Path $AITutorDir ".env"
        if (Test-Path $envFile) {
            $envContent = Get-Content $envFile | Select-String "NOTION_API_KEY"
            if ($envContent) {
                $key = "configurada em .env"
            }
        }
    }
    if ($key) {
        Write-Status "NOTION" "OK — chave encontrada" "Green"
    } else {
        Write-Status "NOTION" "AVISO — NOTION_API_KEY não configurada" "Yellow"
    }
}

function Start-ProjectWatcher {
    if (-not $StartWatcher) { return }
    $watcherScript = Join-Path $AITutorDir "scripts\kb\watch-project-state.ps1"
    if (-not (Test-Path $watcherScript)) {
        Write-Status "WATCHER" "Script não encontrado: $watcherScript" "Red"
        return
    }
    $args = @(
        "-ProjetosDir", $ProjetosDir
    )
    if ($SessionSlug) {
        $args += "-SessionSlug", $SessionSlug
    }
    try {
        $process = Start-Process -FilePath "powershell" -ArgumentList @(
            "-NoProfile", "-WindowStyle Hidden", "-File", $watcherScript
        ) -PassThru -WindowStyle Hidden
        Write-Status "WATCHER" "OK — iniciado (PID: $($process.Id))" "Green"
    } catch {
        Write-Status "WATCHER" "FALHA — $_" "Red"
    }
}

# --- Main ---
Write-Host ""
Write-Host "╔════════════════════════════════════════╗" -ForegroundColor Magenta
Write-Host "║   PROJECT ORCHESTRATOR — ENVIRONMENT   ║" -ForegroundColor Magenta
Write-Host "╚════════════════════════════════════════╝" -ForegroundColor Magenta
Write-Host ""

$gitOk = Test-GitSetup
$repoOk = Test-RepoSetup
$pythonOk = Test-PythonSetup
Test-NotionKey
Start-ProjectWatcher

Write-Host ""
Write-Host "═══ RESUMO ═══" -ForegroundColor Magenta
Write-Host "  Git:      $(if ($gitOk) { '✓' } else { '✗' })" -ForegroundColor $(if ($gitOk) { 'Green' } else { 'Red' })
Write-Host "  Repo:     $(if ($repoOk) { '✓' } else { '✗' })" -ForegroundColor $(if ($repoOk) { 'Green' } else { 'Red' })
Write-Host "  Python:   $(if ($pythonOk) { '✓' } else { '✗' })" -ForegroundColor $(if ($pythonOk) { 'Green' } else { 'Red' })
if ($SessionSlug) {
    Write-Host "  Branch:   sessao/$SessionSlug" -ForegroundColor Cyan
}
Write-Host ""

if ($gitOk -and $repoOk -and $pythonOk) {
    Write-Host "✓ Ambiente pronto para alterações." -ForegroundColor Green
} else {
    Write-Host "⚠ Ambiente com pendências. Corrija antes de prosseguir." -ForegroundColor Yellow
}
