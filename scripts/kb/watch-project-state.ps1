<#
.SYNOPSIS
    Watcher de project-spaces. Monitora alterações em Projetos/,
    cria branches automáticas por sessão, commita e mergeia.

.DESCRIPTION
    - Inicia sessão: cria branch sessao/{slug} a partir de main
    - Monitora: project-state/, kb/, docs/, fontes/, tarefas/
    - Altereção: debounce 5s → git commit na branch da sessão
    - Final: git checkout main + merge sessao/{slug} + push

.PARAMETER ProjetosDir
    Caminho raiz do repositório Projetos/
.PARAMETER SessionSlug
    Slug da sessão atual (opcional, auto-detectado)
.PARAMETER WatchDirs
    Subdiretórios a monitorar (default: project-state, kb, docs, fontes, tarefas, arquitetura)
#>

param(
    [string]$ProjetosDir = (Get-Location).Path,
    [string]$SessionSlug = "",
    [string[]]$WatchDirs = @("project-state", "kb", "docs", "fontes", "tarefas", "arquitetura"),
    [int]$DebounceMs = 5000,
    [string]$LogFile = ""
)

if (-not $LogFile) {
    $LogFile = Join-Path $ProjetosDir "scripts\kb\watcher-project-state.log"
}

function Write-Log {
    param([string]$Msg)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp [WATCHER] $Msg" | Out-File -FilePath $LogFile -Encoding utf8 -Append
    Write-Host "$timestamp [WATCHER] $Msg" -ForegroundColor Cyan
}

function Get-CurrentBranch {
    return git -C $ProjetosDir rev-parse --abbrev-ref HEAD 2>$null
}

function Get-CurrentSessionSlug {
    # Tenta detectar slug da sessão pela branch atual
    $branch = Get-CurrentBranch
    if ($branch -match "^sessao/(.+)$") {
        return $matches[1]
    }
    return ""
}

function Start-SessionBranch {
    param([string]$Slug)
    $branch = Get-CurrentBranch
    if ($branch -eq "main" -or $branch -eq "master") {
        Write-Log "Criando branch sessao/$Slug a partir de $branch..."
        git -C $ProjetosDir checkout -b "sessao/$Slug" 2>&1 | Out-Null
        Write-Log "Branch sessao/$Slug criada."
    } elseif ($branch -ne "sessao/$Slug") {
        Write-Log "Já está na branch $branch. Criando sessao/$Slug a partir daqui..."
        git -C $ProjetosDir checkout -b "sessao/$Slug" 2>&1 | Out-Null
    } else {
        Write-Log "Já está na branch sessao/$Slug."
    }
    return "sessao/$Slug"
}

function End-SessionBranch {
    param([string]$Slug)
    $branch = Get-CurrentBranch
    $expected = "sessao/$Slug"
    if ($branch -ne $expected) {
        Write-Log "Não está na branch $expected (atual: $branch). Nada a mergear."
        return
    }
    Write-Log "Commit final em $branch..."
    git -C $ProjetosDir add -A 2>&1 | Out-Null
    git -C $ProjetosDir commit -m "sessao: $Slug — finalização" 2>&1 | Out-Null
    Write-Log "Checkout main..."
    git -C $ProjetosDir checkout main 2>&1 | Out-Null
    Write-Log "Mergeando $branch → main..."
    git -C $ProjetosDir merge $expected --no-edit 2>&1 | Out-Null
    if ($?) {
        Write-Log "Merge concluído. Pusheando..."
        git -C $ProjetosDir push origin main 2>&1 | Out-Null
        Write-Log "Push concluído."
        git -C $ProjetosDir branch -d $expected 2>&1 | Out-Null
        Write-Log "Branch $expected removida."
    } else {
        Write-Log "ERRO: Conflito no merge. Resolva manualmente."
    }
}

function Initialize-Watcher {
    Write-Log "=== WATCHER INICIANDO ==="
    Write-Log "ProjetosDir: $ProjetosDir"
    Write-Log "WatchDirs: $($WatchDirs -join ', ')"
    Write-Log "Debounce: ${DebounceMs}ms"

    # Verificar se é um repositório git
    if (-not (Test-Path (Join-Path $ProjetosDir ".git"))) {
        Write-Log "ERRO: $ProjetosDir não é um repositório git."
        exit 1
    }

    # Verificar branch inicial
    $branch = Get-CurrentBranch
    Write-Log "Branch atual: $branch"

    if ($SessionSlug) {
        Start-SessionBranch -Slug $SessionSlug
        Write-Log "Sessão vinculada à slug: $SessionSlug"
    }
}

function Watch-Directories {
    $watchers = @()
    foreach ($dir in $WatchDirs) {
        $fullPath = Join-Path $ProjetosDir $dir
        if (-not (Test-Path $fullPath)) {
            New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
            Write-Log "Criado diretório: $fullPath"
        }
        $watcher = New-Object System.IO.FileSystemWatcher
        $watcher.Path = $fullPath
        $watcher.IncludeSubdirectories = $true
        $watcher.EnableRaisingEvents = $true
        $watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor `
                                [System.IO.NotifyFilters]::FileName -bor `
                                [System.IO.NotifyFilters]::DirectoryName
        $watchers += $watcher
        Write-Log "Monitorando: $fullPath"
    }

    $timer = New-Object System.Timers.Timer
    $timer.Interval = $DebounceMs
    $timer.AutoReset = $false
    $script:changed = $false

    foreach ($watcher in $watchers) {
        Register-ObjectEvent $watcher "Changed" -Action {
            $script:changed = $true
            $timer.Stop()
            $timer.Start()
        } | Out-Null
        Register-ObjectEvent $watcher "Created" -Action {
            $script:changed = $true
            $timer.Stop()
            $timer.Start()
        } | Out-Null
        Register-ObjectEvent $watcher "Deleted" -Action {
            $script:changed = $true
            $timer.Stop()
            $timer.Start()
        } | Out-Null
        Register-ObjectEvent $watcher "Renamed" -Action {
            $script:changed = $true
            $timer.Stop()
            $timer.Start()
        } | Out-Null
    }

    Register-ObjectEvent $timer "Elapsed" -Action {
        if ($script:changed) {
            $script:changed = $false
            $branch = git -C $using:ProjetosDir rev-parse --abbrev-ref HEAD
            if ($branch -ne "main" -and $branch -notmatch "^sessao/") {
                Write-Log "Branch $branch não é de sessão. Commit direto."
            }
            git -C $using:ProjetosDir add -A 2>&1 | Out-Null
            $status = git -C $using:ProjetosDir status --porcelain
            if ($status) {
                $count = ($status -split "`n" | Measure-Object).Count
                git -C $using:ProjetosDir commit -m "auto: $count alteração(ões) em $branch" 2>&1 | Out-Null
                if ($?) {
                    $hash = git -C $using:ProjetosDir rev-parse --short HEAD
                    Write-Log "Commit $hash em $branch ($count arquivo(s))"
                }
            }
        }
    } | Out-Null

    Write-Log "Watcher ativo. Aguardando alterações..."
    Write-Log "Dica: Para finalizar sessão, execute: End-SessionBranch -Slug '<slug>'"
}

try {
    Initialize-Watcher
    Watch-Directories
    # Mantém o script rodando
    while ($true) {
        Start-Sleep -Seconds 10
    }
} catch {
    Write-Log "ERRO FATAL: $_"
    exit 1
}
