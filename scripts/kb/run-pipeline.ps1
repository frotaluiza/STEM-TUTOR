<#
.SYNOPSIS
    Post-session pipeline: extract live docs from opencode.db + update project state.
.DESCRIPTION
    Processes all AI STEM Tutor sessions (or a single one with -Slug).
    Designed to be called automatically after each opencode session.
.PARAMETER Slug
    Optional: process only a specific session slug.
.PARAMETER SkipExtract
    If set, skips the SQLite extraction step (useful when live doc already exists).
.EXAMPLE
    .\scripts\kb\run-pipeline.ps1
    .\scripts\kb\run-pipeline.ps1 -Slug witty-wizard
    .\scripts\kb\run-pipeline.ps1 -SkipExtract
#>

param(
    [string]$Slug = '',
    [switch]$SkipExtract
)

$AITutorDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$ExtractScript = Join-Path $AITutorDir "scripts\kb\extract-live-docs.py"
$UpdateScript = Join-Path $AITutorDir "scripts\kb\update-project-state.py"

Write-Host "[KB Pipeline] Starting post-session pipeline..." -ForegroundColor Cyan
Write-Host ""

if (-not $SkipExtract) {
    Write-Host "[KB Pipeline] Step 1: Extract live docs from opencode.db" -ForegroundColor Cyan
    if ($Slug) {
        python $ExtractScript --slug $Slug
    } else {
        python $ExtractScript
    }
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[KB Pipeline] ERROR: Extraction failed!" -ForegroundColor Red
        exit 1
    }
    Write-Host ""
} else {
    Write-Host "[KB Pipeline] Skipping extraction (--SkipExtract)" -ForegroundColor Yellow
}

Write-Host "[KB Pipeline] Step 2: Update project state" -ForegroundColor Cyan
python $UpdateScript
if ($LASTEXITCODE -ne 0) {
    Write-Host "[KB Pipeline] ERROR: Project state update failed!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[KB Pipeline] Done! Project state updated." -ForegroundColor Green
