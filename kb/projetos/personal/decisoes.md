# Decisões e Timeline — Personal / PC

**4 sessões** | **$0.63 custo total**
**30 decisões extraídas**
**3 ferramentas/tecnologias referenciadas**

## Decisões por Categoria

### Arquitetura (1)

- **Erro Bonjour** resolvido (serviço desabilitado)

### Ferramentas / Stack (3)

- `opencode serve` - headless server (just the API/server)
- Dá para criar um plugin que集成a Whisper + hotkey e injeta o texto direto no input do opencode via API/simulação de teclado
- **Haystack** (deepset) - Good for building search-augmented pipelines

### Dados / KB (2)

- **Dragon Naturally Speaking** for Windows dictation
- **LlamaIndex** - Excellent for RAG workflows, data ingestion from various sources

### Interface / UX (4)

- **Acessar pastas do PC pelo celular**: abra um gerenciador de arquivos (ou app Tailscale) e digite `\\100.x.x.x\Compartilhamento` (o IP aparece no app)
- **Alias**: `PC-LUIZA` (qualquer nome)
- **Obsidian** itself - The user mentions Obsidian nodes, so using Obsidian as a frontend could work
- **Neo4j** + visualization - For the graph database backend

### Outros (20)

- **Acessar o PC inteiro**: instale um app de desktop remoto (ex: Microsoft Remote Desktop) — o Tailscale faz a conexão segura
- **66.3 GB → 103.1 GB livres** (+36.8 GB)
- **15+ programas** removidos da inicialização
- **Tailscale** instalado e configurado (PC + iPhone na mesma rede)
- **Servidor web** rodando em `http://100.117.222.86:3000`
- **SSH** instalado e rodando
- **Whisper** (OpenAI's speech-to-text) running locally
- **Voice In** browser extensions (but opencode is terminal-based)
- **PowerToys Voice Access** / **Windows 11 Voice Access**
- **Speech-to-text via PowerShell/AutoHotkey** scripts
- **Windows Terminal + PowerShell dictation**: There are ways to pipe speech-to-text into PowerShell/terminal
- **AutoHotkey + Whisper**: Record audio, transcribe, paste into terminal
- **Clipboard-based approach**: Use a speech-to-text tool that writes to clipboard, then paste (Ctrl+V) into opencode
- **OBS Studio + plugin**: Overkill
- Projeto (title): "Implementando Oliver"
  *+5 mais...*


## Timeline de Sessões

| Data | Título | Agente | Custo | Resumo |
|------|--------|--------|-------|--------|
| 2026-06-27 | [NotebookLM é opensource?](sessoes/shiny-planet.md) | build | $0.35 |  |
| 2026-06-26 | [Cancelar aba de monitoramento](sessoes/quick-cabin.md) | build | $0.01 |  |
| 2026-06-25 | [Diagnóstico de lentidão e erro Bonjour](sessoes/playful-cactus.md) | build | $0.23 |  |
| 2026-06-15 | [Associar comando de voz para conversa contínua](sessoes/quiet-cactus.md) | build | $0.04 |  |
