---
title: "neon-moon"
slug: "neon-moon"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: neon-moon
title: "Research Sci-Hub MCP (@explore subagent)"
date: 2026-07-12
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m05s
messages: 8
parts: 38
cost: 0.013109
tokens_input: 76691
tokens_output: 4935
tokens_reasoning: 642
tokens_cache_read: 289664
tokens_cache_write: 0
created: "2026-07-12 06:06:21 UTC"
updated: "2026-07-12 06:07:26 UTC"
---

SessÃ£o com **8 messages**, **38 parts**, agente **explore**, modelo **deepseek-v4-flash** | ðŸ’° $0.0131 | ðŸ’¾ cache read: 289.7K | â±ï¸ 0h01m05s

## ðŸ‘¤ UsuÃ¡rio (2026-07-12 06:06:21 UTC)

I need to research how to set up a Sci-Hub MCP (Model Context Protocol) server for use with OpenCode. Search the web and return:

1. What Sci-Hub MCP servers exist for OpenCode/Claude/Cline/etc
2. How to configure them in opencode.json/mcp.json
3. The npm package or Python package name and setup instructions
4. Any example configurations or documentation links
5. How to use it once configured (what tools it provides, how to fetch papers by DOI/URL)

Be very thorough - return all URLs, configuration snippets, and usage examples.

## ðŸ¤– Assistente (2026-07-12 06:06:21 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to research Sci-Hub MCP servers for use with OpenCode. Let me search the web thoroughly for this information.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 06:06:25 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Great, I found several Sci-Hub MCP servers. Let me now fetch the top repos for detailed information:

1. **JackKuo666/Sci-Hub-MCP-Server** - Python, 128 stars (most popular)
2. **CyberKrypton/Sci-Hub-MCP-Server** - Python, 2 stars
3. **Debvex/Sci-Hub-MCP-Server** - Python, 1 star
4. **Comet300/Sci-Hub-MCP-Server** - Python, 1 star
5. **pma1999/research_hub_mcp** - Rust, 2 stars
6. **ms7679-1/scholar-mcp** - Python, 3 stars
7. **yashimosh/biblio-mcp** - TypeScript
8. **lxidea/journal-data-api** - Python, 1 star
9. **rafgomindo/Ahara** - Python

Let me read the READMEs for the most popular ones.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 06:06:30 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also fetch the remaining repos to get the full picture.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 06:06:35 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also check the remaining repos and the Smithery badge link for JackKuo666's server, and also check for the opencode.json configuration pattern.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 06:06:40 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have all the information needed to compile a comprehensive answer. Let me check what opencode.json looks like for configuration. Let me also check if there's an existing opencode.json in the workspace.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 06:06:50 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me read the existing opencode.json to see its structure and understand how MCP servers are configured in it.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 06:06:53 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have all the information I need to compile a comprehensive answer. Let me organize all findings about Sci-Hub MCP servers.

Key findings:
1. JackKuo666/Sci-Hub-MCP-Server - Python, 128 stars (most popular)
2. CyberKrypton/Sci-Hub-MCP-Server - Python, 2 stars, no broken scihub package dependency
3. Debvex/Sci-Hub-MCP-Server - Python, pip install sci-hub-mcp-server, most robust (DNS-over-HTTPS, proxy support)
4. Comet300/Sci-Hub-MCP-Server - Python, 1 star
5. pma1999/research_hub_mcp - Rust, multi-provider
6. ms7679-1/scholar-mcp - Python, pip install scholar-mcp-server[all], multi-source search
7. yashimosh/biblio-mcp - TypeScript, npm, multi-source (Anna's Archive + Libgen + Sci-Hub + Z-Library)
8. lxidea/journal-data-api - Python
9. rafgomindo/Ahara - Python, RAG-focused

Now I need to understand how to configure it in opencode.json. Looking at the existing opencode.json, the MCP configs go under `mcp` key.

Let me compile the response.

</details>

### Resposta

Aqui esta o resultado completo da minha pesquisa sobre servidores MCP do Sci-Hub para OpenCode:

---

## 1. Quais servidores Sci-Hub MCP existem

Encontrei **9 repositorios** no GitHub. Os mais relevantes sao:

### A. JackKuo666/Sci-Hub-MCP-Server (RECOMENDADO - 128 estrelas)
- **Link:** https://github.com/JackKuo666/Sci-Hub-MCP-Server
- **Linguagem:** Python (100%)
- **Licenca:** MIT
- **Estrelas:** 128
- **Instalacao:** `git clone` + `pip install -r requirements.txt`
- **Disponivel no Smithery:** Sim (https://smithery.ai/server/@JackKuo666/sci-hub-mcp-server)

### B. Debvex/Sci-Hub-MCP-Server (MAIS ROBUSTO)
- **Link:** https://github.com/Debvex/Sci-Hub-MCP-Server
- **Linguagem:** Python
- **Licenca:** GPL-3.0
- **Instalacao via pip:** `pip install sci-hub-mcp-server`
- **Diferenciais:** DNS-over-HTTPS fallback, proxy support, permanent domain safeguard, CrossRef metadata enrichment
- **Python 3.11+ required**

### C. CyberKrypton/Sci-Hub-MCP-Server (ALTERNATIVA LEVE)
- **Link:** https://github.com/CyberKrypton/Sci-Hub-MCP-Server
- **Linguagem:** Python
- **Licenca:** MIT
- **Diferencial:** Nao depende do pacote `scihub` (quebrado), usa `requests` + `BeautifulSoup` diretamente com auto mirror failover

### D. Comet300/Sci-Hub-MCP-Server
- **Link:** https://github.com/Comet300/Sci-Hub-MCP-Server
- **Linguagem:** Python
- **Licenca:** MIT

### E. ms7679-1/scholar-mcp (MULTI-FONTE)
- **Link:** https://github.com/ms7679-1/scholar-mcp
- **Instalacao via pip:** `pip install scholar-mcp-server[all]`
- **Fontes:** Semantic Scholar, OpenAlex, Crossref, PubMed, arXiv, CORE, Europe PMC, DOAJ, dblp
- **Download via:** Unpaywall, Publisher OA, Sci-Hub, arXiv
- **Extra:** AI analysis, citation graph, code-based paper recommendation

### F. yashimosh/biblio-mcp (MULTI-BIBLIOTECA - NPX)
- **Link:** https://github.com/yashimosh/biblio-mcp
- **Linguagem:** TypeScript
- **Instalacao via npx:** `npx biblio-mcp`
- **Fontes:** Anna's Archive + Library Genesis + Sci-Hub + Z-Library
- **Node.js 18+ required**
- **NPM:** https://www.npmjs.com/package/biblio-mcp

### G. pma1999/research_hub_mcp (RUST - MAIS COMPLETO)
- **Link:** https://github.com/pma1999/research_hub_mcp
- **Linguagem:** Rust
- **Licenca:** GPL-3.0
- **14 provedores academicos:** CrossRef, Semantic Scholar, arXiv, PubMed Central, OpenReview, OpenAlex, CORE, Unpaywall, SSRN, bioRxiv, MDPI, ResearchGate, Sci-Hub
- **Instalacao:** `cargo install rust-research-mcp`
- **Extra:** Daemon mode, code pattern search, bibliography generation, smart categorization

---

## 2. Como configurar no opencode.json

Seu arquivo `opencode.json` atual fica em:
```
C:\Users\frota\OneDrive\Documentos\Projetos\Integracao workflows\opencode.json
```

O schema do OpenCode para MCP aceita a chave `"mcp"` no nivel raiz, onde cada servidor e definido como um objeto filho.

### Configuracao para JackKuo666/Sci-Hub-MCP-Server (Python - clone local):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "scihub": {
      "type": "stdio",
      "command": "C:\\Users\\frota\\miniconda3\\envs\\mcp_server\\python.exe",
      "args": [
        "C:\\Users\\frota\\Sci-Hub-MCP-Server\\sci_hub_server.py"
      ],
      "enabled": true
    }
  }
}
```

### Configuracao para Debvex/sci-hub-mcp-server (Python - pip install):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "scihub": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "sci_hub_mcp_server.sci_hub_server"],
      "enabled": true
    }
  }
}
```

### Configuracao para biblio-mcp (TypeScript - npx):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "biblio": {
      "type": "stdio",
      "command": "npx",
      "args": ["biblio-mcp"],
      "enabled": true
    }
  }
}
```

### Configuracao para scholar-mcp:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "scholar": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "scholar_mcp_server"],
      "enabled": true
    }
  }
}
```

### Configuracao para CyberKrypton/Sci-Hub-MCP-Server (Windows):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "scihub": {
      "type": "stdio",
      "command": "C:\\Users\\frota\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
      "args": [
        "C:\\Users\\frota\\Sci-Hub-MCP-Server\\sci_hub_server.py"
      ],
      "enabled": true
    }
  }
}
```

---

## 3. Nome do pacote e instrucoes de instalacao

### Opcao 1: Debvex/sci-hub-mcp-server (RECOMENDADO - pip install)
```powershell
pip install sci-hub-mcp-server
python -m sci_hub_mcp_server.sci_hub_server
```
**Requisitos:** Python 3.11+

### Opcao 2: JackKuo666/Sci-Hub-MCP-Server (git clone)
```powershell
git clone https://github.com/JackKuo666/Sci-Hub-MCP-Server.git
cd Sci-Hub-MCP-Server
pip install -r requirements.txt
python sci_hub_server.py
```
**Requisitos:** Python 3.10+, FastMCP, requests, bs4, scihub

### Opcao 3: yashimosh/biblio-mcp (npx - mais versatil)
```powershell
npx biblio-mcp
```
Ou build local:
```powershell
git clone https://github.com/yashimosh/biblio-mcp.git
cd biblio-mcp
npm install
npm run build
```
**Requisitos:** Node.js 18+

### Opcao 4: ms7679-1/scholar-mcp (pip install - multi-source)
```powershell
pip install scholar-mcp-server[all]
scholar-mcp-install --all
```
**Requisitos:** Python 3.10+

### Opcao 5: CyberKrypton/Sci-Hub-MCP-Server (git clone - sem dependencia quebrada)
```powershell
git clone https://github.com/CyberKrypton/Sci-Hub-MCP-Server.git
cd Sci-Hub-MCP-Server
pip install -r requirements.txt
python sci_hub_server.py
```

### Opcao 6: pma1999/research_hub_mcp (Rust - mais completo)
```powershell
cargo install rust-research-mcp
```
Ou build:
```powershell
git clone https://github.com/pma1999/research_hub_mcp.git
cd research_hub_mcp
cargo build --release
```
**Requisitos:** Rust 1.70+

---

## 4. Ferramentas MCP que cada servidor expoe

### JackKuo666 / CyberKrypton / Comet300 (mesmo conjunto de tools):

| Tool | Descricao | Parametros |
|---|---|---|
| `search_scihub_by_doi` | Busca paper por DOI | `doi: str` |
| `search_scihub_by_title` | Busca paper por titulo | `title: str` |
| `search_scihub_by_keyword` | Busca papers por palavra-chave | `keyword: str`, `num_results: int` (default 10) |
| `download_scihub_pdf` | Download do PDF | `pdf_url: str`, `output_path: str` |
| `get_paper_metadata` | Metadados do paper | `doi: str` |

### Debvex/sci-hub-mcp-server (mesmo conjunto, mas com CrossRef enrichment):

As mesmas 5 ferramentas acima, porem com metadados enriquecidos (title, author, year populados via CrossRef).

**Variaveis de ambiente uteis:**
- `SCIHUB_HTTPS_PROXY` - Proxy HTTPS (prioridade maxima)
- `SCIHUB_HTTP_PROXY` - Proxy HTTP
- `PYTHONUTF8=1` - No Windows para evitar erros de encoding

### scholar-mcp (ms7679-1):

| Tool | Descricao |
|---|---|
| `paper_search` | Busca em 9 fontes simultaneamente |
| `paper_download` | Download multi-source (Unpaywall, OA, Sci-Hub, arXiv) |
| `paper_batch_download` | Download em lote por lista de DOIs |
| `paper_ai_analyze` | Analise de texto completo via IA |
| `paper_recommend` | Recomendacao baseada em codigo do workspace |
| `paper_citation_graph` | Visualizacao de citacoes (Mermaid) |
| `paper_health` | Verifica disponibilidade das fontes |

**Variaveis de ambiente:**
- `AI_API_KEY` - Para analise de IA
- `AI_API_BASE` - URL base da API (default: `https://api.deepseek.com`)
- `AI_MODEL` - Modelo (default: `deepseek-chat`)
- `UNPAYWALL_EMAIL` - Email para Unpaywall API

### biblio-mcp (yashimosh):

| Tool | Descricao |
|---|---|
| `search_books` | Busca livros em Anna's Archive + Libgen + Z-Library |
| `book_details` | Metadados completos de um livro por MD5 |
| `get_download_links` | URLs de download para um MD5 |
| `download_book` | Download do arquivo por MD5 |
| `search_papers` | Busca papers academicos via Libgen scimag |
| `get_paper` | Resolve PDF via Sci-Hub por DOI/URL/title |

**Variaveis de ambiente:**
- `BIBLIO_ANNA_MIRRORS` - Mirrors do Anna's Archive
- `BIBLIO_LIBGEN_MIRRORS` - Mirrors do Libgen
- `BIBLIO_SCIHUB_MIRRORS` - Mirrors do Sci-Hub (default: `.ren, .mksa.top, .hkvisa.net, .se, .st, .ru`)
- `BIBLIO_ZLIB_MIRRORS` - Mirrors do Z-Library
- `BIBLIO_TIMEOUT_MS` - Timeout por request (default: 20000)

### research_hub_mcp (pma1999 - Rust):

| Tool | Descricao |
|---|---|
| `search_papers` | Busca em 14 provedores com roteamento inteligente |
| `download_paper` | Download com fallback multi-provedor |
| `extract_metadata` | Extrai metadados de PDFs |
| `search_code` | Busca por padroes de codigo em papers |
| `generate_bibliography` | Gera citacoes em varios formatos |
| `categorize_papers` | Categorizacao automatica de papers |

---

## 5. Como usar uma vez configurado

Apos configurar o MCP server no `opencode.json`, o OpenCode automaticamente disponibiliza as ferramentas para o LLM durante as sessoes. Voce pode simplesmente pedir em linguagem natural:

### Exemplos de uso:

**Buscar paper por DOI:**
> "Search Sci-Hub for the paper with DOI 10.1038/nature09492"
> "Find the paper with DOI 10.1109/TSMC.2016.2597800"

**Buscar paper por titulo:**
> "Find the paper titled 'Attention Is All You Need' on Sci-Hub"
> "Search for 'Choosing Assessment Instruments for Posttraumatic Stress Disorder Screening'"

**Buscar por palavra-chave:**
> "Search Sci-Hub for recent papers about reinforcement learning"
> "Find papers about CRISPR therapy on Sci-Hub"

**Download de PDF:**
> "Download the PDF for this paper to my_paper.pdf"
> "Download the paper to C:\Users\frota\Downloads\paper.pdf"

**Obter metadados:**
> "Show me the metadata for DOI 10.1038/nature09492"

**Com biblio-mcp (livros + papers):**
> "Find me Dune by Frank Herbert as an EPUB"
> "Search for papers about quantum computing"

### Fluxo tipico de trabalho:

1. **Buscar** um paper por DOI ou titulo
2. **Obter metadados** (autores, ano, titulo completo)
3. **Download** do PDF para uma pasta local
4. **Ler/analisar** o PDF (com outras ferramentas)
5. **Extrair** citacoes ou referencias

---

## 6. Links e documentacao

| Recurso | URL |
|---|---|
| JackKuo666/Sci-Hub-MCP-Server | https://github.com/JackKuo666/Sci-Hub-MCP-Server |
| Debvex/sci-hub-mcp-server (PyPI) | https://pypi.org/project/sci-hub-mcp-server/ |
| CyberKrypton/Sci-Hub-MCP-Server | https://github.com/CyberKrypton/Sci-Hub-MCP-Server |
| Comet300/Sci-Hub-MCP-Server | https://github.com/Comet300/Sci-Hub-MCP-Server |
| scholar-mcp (PyPI) | https://pypi.org/project/scholar-mcp-server/ |
| biblio-mcp (npm) | https://www.npmjs.com/package/biblio-mcp |
| pma1999/research_hub_mcp | https://github.com/pma1999/research_hub_mcp |
| journal-data-api (lxidea) | https://github.com/lxidea/journal-data-api |
| Ahara (rafgomindo) | https://github.com/rafgomindo/Ahara |
| Smithery - JackKuo666 | https://smithery.ai/server/@JackKuo666/sci-hub-mcp-server |
| Model Context Protocol | https://modelcontextprotocol.io |

---

## 7. Recomendacao para seu setup

Considerando seu ambiente Windows e o uso com OpenCode, minha recomendacao em ordem de prioridade:

1. **Debvex/sci-hub-mcp-server** (`pip install sci-hub-mcp-server`) - Mais robusto contra bloqueios de DNS, tem proxy support, e e o unico publicando no PyPI ativamente. A configuracao e a mais limpa.

2. **JackKuo666/Sci-Hub-MCP-Server** - Mais popular (128 estrelas), mas depende do pacote `scihub` que pode estar desatualizado.

3. **biblio-mcp** (`npx biblio-mcp`) - Se voce tambem quiser acesso a livros (Libgen, Anna's Archive, Z-Library), este e o mais versatil.

Para instalar agora, eu sugiro:
```powershell
pip install sci-hub-mcp-server
```

E adicionar ao seu `opencode.json`:
```json
{
  "mcp": {
    "scihub": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "sci_hub_mcp_server.sci_hub_server"],
      "enabled": true
    }
  }
}
```

Isso expora as 5 ferramentas MCP (`search_scihub_by_doi`, `search_scihub_by_title`, `search_scihub_by_keyword`, `download_scihub_pdf`, `get_paper_metadata`) para uso durante as sessoes do OpenCode.

*Novo passo iniciado*

---

*8 messages | 38 parts | ðŸ’° $0.0131 | â±ï¸ 0h01m05s*

