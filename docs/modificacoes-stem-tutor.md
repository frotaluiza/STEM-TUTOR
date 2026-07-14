# Modificações STEM Tutor — DeepTutor Fork

## Sobre

Este documento registra todas as alterações feitas no fork `stem-tutor` do DeepTutor para desenvolvimento do AI STEM Tutor.

---

## Feature: Voice Input (Entrada por Voz)

### Feature: Modo Conversação por Voz (Voice Mode)

#### Descrição
Modo de conversa contínua onde o usuário fala, o sistema transcreve, envia automaticamente após pausa de 1.2s, e a resposta do tutor é lida em voz alta via TTS.

#### Arquivos Modificados
| Arquivo | Alteração |
|---|---|
| `web/components/chat/home/ChatComposer.tsx` | Adicionado `toggleVoiceMode` + `startMic` com auto-send por silêncio |
| `web/components/common/AssistantResponse.tsx` | Adicionado TTS via `speechSynthesis` quando streaming termina |
| `web/hooks/useTextToSpeech.ts` | Hook de TTS com seleção de voz, taxa, persistência em localStorage |
| `web/types/speech-recognition.d.ts` | Adicionado `SpeechSynthesis` types |

#### Como Funciona
1. Botão "Modo Voz" (ícone de balão de conversa) na toolbar ao lado do microfone
2. Quando ativado:
   - Reconhecimento de voz começa automaticamente
   - Ao falar, o texto aparece no input
   - Após 1.2s de silêncio, a mensagem é enviada automaticamente
   - Quando a resposta do tutor chega, é lida em voz alta via `SpeechSynthesis` (pt-BR)
3. Botão fica azul quando modo está ativo
4. TTS pode ser configurado: voz e taxa salvos em localStorage

#### Requisitos
- Navegador com suporte a Web Speech API (Chrome, Edge, Safari)
- `SpeechSynthesis` para leitura das respostas (vozes pt-BR disponíveis no sistema)

#### Controles
- `dt-voice-mode`: "1" ou "0" no localStorage
- `dt-tts-enabled`: "1" ou "0" no localStorage  
- `dt-tts-rate`: velocidade da fala (ex: "1.2")
- `dt-tts-voice-uri`: URI da voz selecionada

---

## Feature: TTS (Text-to-Speech nas Respostas)

### Descrição
Adiciona um botão de microfone na toolbar do chat que utiliza a Web Speech API do navegador para entrada por voz.

### Arquivos Modificados

| Arquivo | Alteração |
|---|---|
| `web/components/chat/home/ChatComposer.tsx` | Adicionado botão `Mic` na toolbar + hook `handleVoiceInput` com Web Speech API |
| `web/types/speech-recognition.d.ts` | Declaração de tipos TypeScript para Web Speech API (`SpeechRecognition`, `SpeechRecognitionEvent`, etc.) |

### Como Funciona
1. Botão de microfone posicionado na toolbar do chat (entre o seletor de modelo e o botão de envio)
2. Ao clicar: ativa o reconhecimento de voz via `webkitSpeechRecognition` / `SpeechRecognition`
3. Durante a gravação: botão fica vermelho com animação pulsante
4. Texto transcrito é inserido no textarea do chat
5. Suporta múltiplas frases (modo `continuous: true`)
6. Ao clicar novamente ou quando a fala termina: gravação é interrompida

### Requisitos
- Navegador com suporte a Web Speech API (Chrome, Edge, Safari)
- `lang: "en-US"` configurado (pode ser alterado para pt-BR)

### Próximos Passos Possíveis
- Adicionar seletor de idioma (en-US / pt-BR)
- Suporte a resultados intermediários (`interimResults: true`) para feedback em tempo real
- Fallback com indicação visual quando API não está disponível
- Comando de voz para enviar mensagem automaticamente

---

## Skills Instaladas do ClawHub

Skills educacionais instaladas do hub comunitário:

| Skill | Versão | Descrição |
|---|---|---|
| `tutor` | 1.0.0 | Personalized tutoring for any age and subject |
| `study-tutor` | 1.0.2 | Science-based learning assistant |
| `tutor-ai` | 1.0.0 | AI tutoring assistant |

---

## Configuração

### LLM Provider
- **Provider:** DeepSeek (API compatível com OpenAI)
- **Modelo:** `deepseek-chat`
- **Base URL:** `https://api.deepseek.com`
- **Contexto:** 65k tokens

### Ambiente
- **Python:** 3.12.12 (venv em `.venv`)
- **Node.js:** 24.15.0
- **Next.js:** 16.2.3 (Turbopack)
- **Branch:** `stem-tutor`

---

## Comandos Úteis

```powershell
# Ativar ambiente
.\.venv\Scripts\Activate.ps1

# Iniciar DeepTutor (backend + frontend)
deeptutor start

# Rodar apenas backend
python -m uvicorn deeptutor.api.main:app --host 0.0.0.0 --port 8001

# Rodar apenas frontend (dev)
cd web; npm run dev -- --port 3782

# Instalar skill do ClawHub
deeptutor skill install clawhub:<skill-name>

# TypeScript type check
cd web; npx tsc --noEmit
```

---

## Feature: Crop Tool + Notebook Editor (Junho 2026)

### Branch
`feature/crop-tool-inline` → mergeado em `stem-tutor`

### Descrição
Sistema de recorte de figuras diretamente do PDF, com editor markdown vivo integrado ao chat LLM.

### Componentes Novos

#### Backend

| Endpoint | Função |
|---|---|
| `POST /api/v1/knowledge/{kb}/crop` | Corta uma região do PDF e retorna PNG (não salva) |
| `POST /api/v1/knowledge/{kb}/crop-save` | Corta, salva em `raw/figures/`, retorna URL pública |
| `POST /api/v1/notebook/chat` | Chat completion simples pro Notebook Editor (usa DeepSeek via `deeptutor.services.llm.complete`) |

**Arquivo:** `deeptutor/api/routers/knowledge.py` (crop endpoints)
**Arquivo:** `deeptutor/api/routers/notebook.py` (chat endpoint)

#### Frontend

| Componente | Local | Função |
|---|---|---|
| `CropModal` | `web/components/knowledge/CropModal.tsx` | Modal com imagem da página, drag pra selecionar região, navegação ◀▶ entre páginas |
| `CropPlaceholder` | `web/components/knowledge/CropPlaceholder.tsx` | Placeholder clicável q abre CropModal |
| `MarkdownWithCrops` | `web/components/knowledge/MarkdownWithCrops.tsx` | Wrapper do MarkdownRenderer com toolbar de crop por página |
| `NotebookEditor` | `web/components/knowledge/NotebookEditor.tsx` | Split-pane: editor markdown (textarea + preview) + chat assistente |

#### Arquivos Modificados

| Arquivo | Alteração |
|---|---|
| `web/components/knowledge/KbFilePreview.tsx` | Adicionado `kbName` prop, render condicional de `MarkdownWithCrops` |
| `web/components/knowledge/KbFilesTab.tsx` | Passa `kb.name` pro `KbFilePreview` |
| `web/next.config.js` | Removeu rewrite rule de `/api/v1` (não estava em uso) |
| `deeptutor/api/routers/knowledge.py` | +fitz import, +crop, +crop-save endpoints |
| `deeptutor/api/routers/notebook.py` | +`/chat` endpoint, +`complete` import |

### Fluxo Crop

1. Abre `.md` no Knowledge Center → toolbar "Pages" no final
2. Clica `+N` → CropModal abre com a página
3. Arrasta pra selecionar região → "Crop" → salva em `raw/figures/`
4. Miniatura aparece na toolbar, persiste em `localStorage`

### Fluxo Notebook Editor

1. Dentro do `.md`, clica "Open in Notebook"
2. Split-pane: textarea (edit) + MarkdownRenderer (preview) + Chat
3. Chat entende tags:
   - `<crop page="N" label="..." />` → vira botão de crop inline
   - `<doc>...</doc>` → substitui documento inteiro
   - `<edit>...</edit>` → substitui seleção atual
4. Seleciona texto no editor → aparece badge âmbar → chat recebe o texto selecionado no prompt
5. "Save" → salva no sistema Notebook do DeepTutor

### Script de Ingestão

| Script | Função |
|---|---|
| `scripts/ingest_textbook.py` | Pipeline completo: extrai texto + renderiza páginas a 72 DPI + divide em capítulos/seções/exercícios + registra KB |

```
data/modules/sadiku/
├── textbook.md              (livro completo)
├── chapters/ch01..ch18.md   (18 capítulos)
├── sections/                (339 sub-seções)
├── exercises/               (20 listas de exercícios)
├── figures/pgNNNN.png       (1022 páginas renderizadas)
└── meta.json
```

### Ferramenta Auxiliar

`http://localhost:3782/crop-tool.html` — crop tool standalone (abre qualquer página, corta, copia pra área de transferência)

### Função de Crop no Assistente

Quando o usuário pede uma figura no Notebook Editor, o sistema prompt instrui o LLM a responder com:
```
<crop page="36" label="Figure 1.1 - A simple electric circuit" />
```
O frontend detecta a tag e mostra um botão "✂️ Crop Figure 1.1". Ao clicar, abre o CropModal na página indicada.

---
