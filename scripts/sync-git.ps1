<#
.SYNOPSIS
    Sincroniza o repositório local com o remote personal (frotaluiza/STEM-TUTOR).
    Puxa mudanças do remote e empurra commits locais.
    Pode ser chamado pelo PM Dashboard ou manualmente.

.PARAMETER Branch
    Branch para sync (default: main)
.PARAMETER Remote
    Remote para sync (default: personal)
.PARAMETER AutoMerge
    Se true, faz merge automático das mudanças do remote (cuidado com conflitos)
#>

param(
    [string]$Branch = "main",
    [string]$Remote = "personal",
    [switch]$AutoMerge = $false
)

$ProjectDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent

Write-Host "[Git Sync] Sincronizando $Remote/$Branch em $ProjectDir"

# 1. Stash changes locais não commitados
$hasChanges = & "C:\Program Files\Git\bin\git.exe" status --porcelain 2>$null
$stashed = $false
if ($hasChanges) {
    Write-Host "[Git Sync] Mudanças locais detectadas — executando stash..."
    & "C:\Program Files\Git\bin\git.exe" stash push -m "auto-stash before sync" 2>$null
    $stashed = $true
}

# 2. Mudar para a branch
& "C:\Program Files\Git\bin\git.exe" checkout $Branch 2>$null

# 3. Fetch do remote
Write-Host "[Git Sync] Fetch de $Remote/$Branch..."
& "C:\Program Files\Git\bin\git.exe" fetch $Remote $Branch 2>&1 | Out-Null

# 4. Pull (rebase para evitar merge commits desnecessários)
Write-Host "[Git Sync] Pull de $Remote/$Branch..."
if ($AutoMerge) {
    & "C:\Program Files\Git\bin\git.exe" pull $Remote $Branch --no-edit 2>&1
} else {
    & "C:\Program Files\Git\bin\git.exe" pull $Remote $Branch --ff-only 2>&1
}

if ($LASTEXITCODE -ne 0 -and -not $AutoMerge) {
    Write-Host "[Git Sync] ⚠ Fast-forward não possível. Use -AutoMerge para fazer merge." -ForegroundColor Yellow
}

# 5. Push commits locais
Write-Host "[Git Sync] Push para $Remote/$Branch..."
& "C:\Program Files\Git\bin\git.exe" push $Remote $Branch 2>&1

# 6. Restaurar stash
if ($stashed) {
    Write-Host "[Git Sync] Restaurando stash..."
    & "C:\Program Files\Git\bin\git.exe" stash pop 2>$null
}

Write-Host "[Git Sync] ✔ Sincronizado com $Remote/$Branch"
