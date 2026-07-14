<#
.SYNOPSIS
    Gera artefatos markdown obrigatórios (changelog + relatório) para a sessão atual.
    Deve ser executado ao final de cada sessão ou a cada commit significativo.

.PARAMETER SessionTitle
    Título descritivo da sessão
.PARAMETER SessionSlug
    Slug da sessão no opencode
.PARAMETER Branch
    Branch atual (default: git branch --show-current)
.PARAMETER ProjectSlug
    Slug do projeto (default: ai-stem-tutor)
.PARAMETER Changes
    Lista de alterações no formato "arquivo: descrição" (separadas por ;)
.PARAMETER Decisions
    Lista de decisões (separadas por ;)
.PARAMETER TestResults
    Resultados de testes no formato "framework|comando|resultado|duracao" (separadas por ;)
.PARAMETER Errors
    Descrição de erros encontrados (opcional)
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$SessionTitle,
    [Parameter(Mandatory = $true)]
    [string]$SessionSlug,
    [string]$Branch = $(git branch --show-current 2>$null),
    [string]$ProjectSlug = "ai-stem-tutor",
    [string]$Changes = "",
    [string]$Decisions = "",
    [string]$TestResults = "",
    [string]$Errors = ""
)

$Date = Get-Date -Format "yyyy-MM-dd"
$ProjectDir = Split-Path -Path (Split-Path -Path $PSScriptRoot -Parent) -Parent
$ArtefatosDir = Join-Path $ProjectDir "Projetos" $ProjectSlug "artefatos"
$RelatoriosDir = Join-Path $ProjectDir "Projetos" $ProjectSlug "relatorios"

New-Item -ItemType Directory -Path $ArtefatosDir -Force | Out-Null
New-Item -ItemType Directory -Path $RelatoriosDir -Force | Out-Null

$DateSlug = "$Date--$SessionSlug"

# --- Changelog ---
$changelog = @"
# Changelog — $SessionTitle
**Data:** $Date | **Branch:** $Branch | **Sessão:** $SessionSlug

## Alterações Realizadas

"@

if ($Changes) {
    $Changes.Split(';') | ForEach-Object {
        $changelog += "- $_`n"
    }
}

$changelog += @"

## Decisões

"@

if ($Decisions) {
    $Decisions.Split(';') | ForEach-Object {
        $changelog += "- $_`n"
    }
}

$changelogPath = Join-Path $ArtefatosDir "${DateSlug}--changelog.md"
$changelog | Out-File -FilePath $changelogPath -Encoding utf8
Write-Host "[Artefato] Changelog: $changelogPath"

# --- Relatório ---
$relatorio = @"
# Relatório — $SessionTitle
**Data:** $Date | **Branch:** $Branch

## Testes Executados

| Framework | Comando | Resultado | Duração |
|-----------|---------|-----------|---------|
"@

if ($TestResults) {
    $TestResults.Split(';') | ForEach-Object {
        $parts = $_ -split '\|'
        $relatorio += "| $($parts[0]) | $($parts[1]) | $($parts[2]) | $($parts[3]) |`n"
    }
}

$relatorio += @"

## Erros Encontrados
$Errors

## Observações
- Artefato gerado automaticamente por gerar-artefato.ps1
- Sessão: $SessionSlug ($SessionTitle)
"@

$relatorioPath = Join-Path $ArtefatosDir "${DateSlug}--relatorio.md"
$relatorio | Out-File -FilePath $relatorioPath -Encoding utf8
Write-Host "[Artefato] Relatório: $relatorioPath"

# --- Atualizar project-state.yaml ---
$YamlPath = Join-Path $ProjectDir "Projetos" $ProjectSlug "project-state.yaml"
if (Test-Path $YamlPath) {
    $yaml = Get-Content $YamlPath -Raw
    $yaml += "`n# Artefatos desta sessão`n"
    $yaml += "# - $DateSlug -- changelog`n"
    $yaml += "# - $DateSlug -- relatorio`n"
    $yaml | Out-File -FilePath $YamlPath -Encoding utf8
    Write-Host "[Artefato] project-state.yaml atualizado"
}

Write-Host "[Artefato] OK — artefatos gerados em $DateSlug"
