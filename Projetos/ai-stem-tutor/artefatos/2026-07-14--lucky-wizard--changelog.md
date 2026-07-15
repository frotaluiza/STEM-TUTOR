# Changelog — Source Providers System + Branching Strategy
**Data:** 2026-07-14 | **Branch:** ps/mindmap-v2 | **Sessão:** lucky-wizard

## Alterações Realizadas (Artefatos)
- Definição da arquitetura do Source Providers System (módulo `deeptutor/services/sources/`)
- Definição da Branching Strategy: sessão → branch do project state → branch do repo
- Provedores de fonte personalizáveis por projeto com database SQLite
- Sugestões automáticas de fontes por área do projeto
- Integração bridge com Search Providers existentes do DeepTutor
- Mar da Elétrica como projeto com fontes sugeridas da área "eletrica"

## Decisões
1. **Branching Strategy**: Sessão ≡ branch do project state. Dentro dela, pode haver branch do repo. Project state registra associação.
2. **Source Providers System**: Módulo novo dentro do DeepTutor, não API separada.
3. **Mar da Elétrica**: Projeto no sistema de fontes. Mastery paths = futuro.

## Arquivos Modificados
- `C:\Users\frota\.local\share\opencode\docs\lucky-wizard.md` (criação — live doc da sessão)
- `C:\Users\frota\Documents\STEM-TUTOR\Projetos\ai-stem-tutor\artefatos\2026-07-14--lucky-wizard--changelog.md` (criação)
- `C:\Users\frota\Documents\STEM-TUTOR\project-state\ai-stem-tutor.md` (modificação)
- `C:\Users\frota\Documents\STEM-TUTOR\project-state\ai-stem-tutor.json` (modificação)
