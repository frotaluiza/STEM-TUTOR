---
title: "hidden-river"
slug: "hidden-river"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: hidden-river
title: "Explore LLM service layer (@explore subagent)"
date: 2026-07-11
agent: explore
model: deepseek-v4-flash-free
project: "AI STEM Tutor"
branch: ""
duration: 0h01m14s
messages: 8
parts: 79
cost: 0
tokens_input: 127978
tokens_output: 6876
tokens_reasoning: 268
tokens_cache_read: 243456
tokens_cache_write: 0
created: "2026-07-11 21:17:52 UTC"
updated: "2026-07-11 21:19:07 UTC"
---

SessÃ£o com **8 messages**, **79 parts**, agente **explore**, modelo **deepseek-v4-flash-free** | ðŸ’¾ cache read: 243.5K | â±ï¸ 0h01m14s

## ðŸ‘¤ UsuÃ¡rio (2026-07-11 21:17:52 UTC)

Explore the DeepTutor codebase at C:\Users\frota\Documents\Projetos\AI TUTOR\ looking at the LLM integration layer. I need to understand:

1. Read C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\llm.py - how is the LLM service structured? Does it support multiple providers?
2. Read C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\__init__.py
3. Check deeptutor\services\ directory listing
4. Read C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\model_catalog.json - how models are configured
5. Check deeptutor\multi_user\ directory - what's the multi-user architecture?
6. Check if there's any usage tracking or rate limiting already
7. Look at deeptutor\config\ for how config is loaded

Return the COMPLETE content of llm.py and model_catalog.json. Also describe the multi-user system architecture and the config loading system.

## ðŸ¤– Assistente (2026-07-11 21:17:52 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to explore a DeepTutor codebase and understand the LLM integration layer. Let me start by reading the requested files and exploring the directory structure.

</details>

### Resposta

I'll start by reading all the requested files and exploring the directories in parallel.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-11 21:17:57 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The llm.py file wasn't found because it's actually a directory (llm/). Let me read the llm module as a directory and find the main files. Let me also read the multi_user and config files in detail.

</details>

### Resposta

The `llm.py` is actually a directory `llm/`. Let me explore its contents and read the key files.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-11 21:18:02 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the core LLM service files. I need to read the main files in the llm directory: __init__.py, client.py, factory.py, provider_factory.py, provider_registry.py, providers/, config.py, types.py, traffic_control.py, telemetry.py, etc.

</details>

### Resposta

Now let me read the core LLM service files in detail.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-11 21:18:08 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the remaining important files: the cloud_provider, local_provider, provider_core, providers directory, error_mapping, exceptions, capabilities, multimodal, and the multi_user files. Also the services/config directory for config loading.

</details>

### Resposta

Let me continue reading the provider implementations and the remaining important files.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-11 21:18:15 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the provider_core files and a few more multi_user files to understand the full architecture.

</details>

### Resposta

Let me now read the provider_core implementations and multi-user architecture files.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-11 21:18:22 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me read the services/config files to understand config loading, plus a few more multi-user files for completeness.

</details>

### Resposta

Let me read the config loading system and a few more architecture files.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-11 21:18:28 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive understanding of the DeepTutor codebase's LLM integration layer. Let me compile and present the findings.

</details>

### Resposta

Here is the complete analysis of the DeepTutor LLM integration layer.

---

## 1. LLM Service Structure (`deeptutor/services/llm/`)

The LLM service is a **modular package** (not a single file) located at:

```
deeptutor/services/llm/
```

It contains **24 entries** and is organized as follows:

### Core Architecture (3-Layer Design)

```
Agents (ChatAgent, SolveAgent, etc.)
        â”‚
   BaseAgent.call_llm() / stream_llm()
        â”‚
   LLM Factory (complete / stream)  â† factory.py
        â”‚
   â”Œâ”€â”€â”€â”€â”´â”€â”€â”€â”€â”
   â†“         â†“
Cloud       Local
Provider    Provider
```

### Key Modules

| Module | Purpose |
|---|---|
| `__init__.py` | Public API re-exports + lazy-loaded `cloud_provider`/`local_provider` |
| `factory.py` | **Main entry point** â€” `complete()` and `stream()` async functions with retry logic, provider resolution, image support |
| `client.py` | Legacy `LLMClient` class-based wrapper (deprecated; prefer `factory.complete`) |
| `config.py` | `LLMConfig` dataclass, singleton cache, `ContextVar` scoped config, env var setup |
| `provider_factory.py` | `get_runtime_provider()` â€” builds the correct provider runtime from config |
| `provider_registry.py` | Re-exports from `services/provider_registry.py` |
| `cloud_provider.py` | Direct aiohttp HTTP calls to OpenAI-compatible, Anthropic, and Cohere APIs |
| `local_provider.py` | Direct aiohttp HTTP calls to local servers (Ollama, LM Studio, vLLM, llama.cpp) |
| `provider_core/` | **SDK-based provider implementations** (OpenAI SDK, Anthropic SDK, etc.) |
| `providers/` | Legacy provider implementations (Anthropic, OpenAI, routing, base) |
| `capabilities.py` | Provider capability matrix (response_format, vision, streaming, tools per provider/model) |
| `error_mapping.py` | Maps provider-specific exceptions to unified `LLMError` hierarchy |
| `exceptions.py` | Exception hierarchy: `LLMError` -> `LLMConfigError`, `LLMAPIError`, `LLMRateLimitError`, etc. |
| `traffic_control.py` | `TrafficController` â€” concurrency semaphore + token-bucket rate limiter |
| `telemetry.py` | `track_llm_call` decorator for basic logging |
| `multimodal.py` | Image attachment handling (base64/URL, OpenAI/Anthropic format) |
| `executors.py` | SDK-based executors (`sdk_complete`, `sdk_stream`) using `openai.AsyncOpenAI` |
| `reasoning_params.py` | Reasoning effort parameter handling per provider |
| `registry.py` | Simple decorator-based provider registration system |
| `types.py` | `TutorResponse`, `TutorStreamChunk` data models |
| `utils.py` | URL sanitization, auth headers, thinking tag cleaning, chat URL building |
| `openai_http_client.py` | OpenAI HTTP client kwargs factory |
| `context_window.py` | Context window detection |
| `model_selection/` | Model selection service |

### Multiple Providers Support â€” **YES, extensively**

The system supports **three access patterns** for multiple providers:

**Pattern A â€” Provider Registry** (`services/provider_registry.py`):
A centralized `PROVIDERS` tuple of `ProviderSpec` dataclass entries. There are ~35 registered providers including:

- **Direct/Standard**: `openai`, `anthropic`, `deepseek`, `gemini`, `mistral`, `dashscope` (Qwen), `moonshot` (Kimi), `zhipu`, `stepfun`, `minimax`, `xiaomi_mimo`, `groq`, `together`, `qianfan`, `cohere`
- **Gateways** (route any model): `openrouter`, `aihubmix`, `siliconflow`, `volcengine`, `byteplus`, `nvidia_nim`
- **Local**: `ollama`, `vllm`, `lm_studio`, `llama_cpp`, `lemonade`, `ovms`
- **OAuth**: `github_copilot`, `openai_codex`
- **Custom/Direct**: `custom` (OpenAI-compatible), `custom_anthropic`, `azure_openai`

Provider detection uses API key prefixes, base URL keywords, model name keywords, and explicit binding hints. Providers fall into modes: `standard`, `gateway`, `local`, `oauth`, `direct`.

**Pattern B â€” Provider Core** (`provider_core/`):
Abstract base class `LLMProvider` with concrete implementations:
- `OpenAICompatProvider` â€” uses `openai.AsyncOpenAI` SDK for all OpenAI-compatible endpoints (OpenAI, DeepSeek, Gemini, Moonshot, gateways, local)
- `AnthropicProvider` â€” Anthropic SDK for Claude
- `AzureOpenAIProvider` â€” Azure-specific OpenAI
- `GitHubCopilotProvider` â€” GitHub Copilot
- `OpenAICodexProvider` â€” OpenAI Codex

Each handles message sanitization, tool calls, streaming, retry logic, and response parsing.

**Pattern C â€” Direct HTTP** (`cloud_provider.py` / `local_provider.py`):
Fallback/legacy HTTP-based providers using `aiohttp` for cases where SDKs are not available.

---

## 2. Complete `model_catalog.json`

```json
{
  "version": 1,
  "services": {
    "llm": {
      "active_profile_id": "deepseek",
      "active_model_id": "deepseek-chat",
      "profiles": [
        {
          "id": "deepseek",
          "provider": "openai",
          "base_url": "https://api.deepseek.com",
          "api_key": "sk-6c4b96cd265f40eb94b983049bf07add",
          "models": [
            {
              "id": "deepseek-chat",
              "name": "DeepSeek Chat",
              "context_length": 65536,
              "model": "deepseek-chat"
            }
          ],
          "name": "DeepSeek",
          "api_version": "",
          "binding": "openai",
          "extra_headers": {}
        }
      ]
    },
    "embedding": {
      "active_profile_id": "ollama",
      "active_model_id": "nomic-embed-text",
      "profiles": [
        {
          "id": "ollama",
          "binding": "ollama",
          "base_url": "http://localhost:11434/api/embed",
          "api_key": "sk-no-key-required",
          "models": [
            {
              "id": "nomic-embed-text",
              "name": "nomic-embed-text",
              "model": "nomic-embed-text",
              "dimension": 768,
              "supported_dimensions": ""
            }
          ],
          "name": "Ollama Local",
          "api_version": "",
          "extra_headers": {}
        }
      ]
    },
    "search": {
      "active_profile_id": null,
      "profiles": []
    }
  }
}
```

Note: The `model_catalog.json` supports multiple **services** (llm, embedding, search, tts, stt, imagegen, videogen), each with multiple **profiles** (provider configurations) and multiple **models** per profile. Profiles carry `binding`, `base_url`, `api_key`, `api_version`, `extra_headers`. Models carry `model`, `name`, `context_length`, `dimension` (embedding), voice settings (tts), etc.

The config loading system (`services/config/model_catalog.py`) auto-normalizes the catalog, filling in defaults for any missing fields, and saving back if changes were made.

---

## 3. Config Loading System

The configuration loading is a **multi-layered system** in `deeptutor/services/config/`:

### Layer 1 â€” `runtime_settings.py` (`RuntimeSettingsService`)
- **JSON-backed** settings under `data/user/settings/`
- Supports multiple config files: `system.json`, `auth.json`, `integrations.json`, `document_parsing.json`, `pageindex.json`, `llamaindex.json`, `graphrag.json`, `lightrag.json`
- Each has **defaults**, **normalization**, and **process environment overrides**
- Process env vars (e.g., `BACKEND_PORT`, `AUTH_ENABLED`, `POCKETBASE_URL`) apply at deployment time

### Layer 2 â€” `loader.py`
- YAML-based configuration loading (`main.yaml`, `agents.yaml`)
- `load_config_with_main()` loads a YAML file and injects runtime paths
- `get_agent_params()` reads per-capability agent temperature/max_tokens from `agents.yaml`
- `get_chat_params()` reads chat capability parameters with deep-merged defaults

### Layer 3 â€” `provider_runtime.py`
- Resolves active LLM/embedding/search/TTS/STT/imagegen/videogen configs from `model_catalog.json`
- `resolve_llm_runtime_config()` reads active profile + model, performs provider auto-detection (gateway detection via key prefix / base URL keywords, model-based matching), and returns `ResolvedLLMConfig` dataclass
- Used by `services/llm/config.py` â†’ `get_llm_config()`

### Layer 4 â€” Pydantic Settings (`config/settings.py`)
- `Settings` class (Pydantic `BaseSettings`) for LLM retry configuration
- Environment variable prefix: `LLM_`, with nested delimiter `__` (e.g., `LLM_RETRY__MAX_RETRIES=5`)
- Falls back to defaults (max_retries=8, base_delay=5.0, exponential_backoff=True)

### Layer 5 â€” `config/defaults.py`
- Hardcoded defaults for llm model/provider and paths

### Config Loading Flow:
1. `get_llm_config()` (cached singleton + ContextVar scoped override)
2. â†’ `resolve_llm_runtime_config()` (reads `model_catalog.json` via `ModelCatalogService`)
3. â†’ `ModelCatalogService.load()` (reads/creates/normalizes JSON)
4. â†’ Provider auto-detection via `provider_registry.py`
5. â†’ Returns `LLMConfig` dataclass with all resolved fields

---

## 4. Multi-User Architecture (`deeptutor/multi_user/`)

The multi-user system is **optional** and **deliberately isolated** from single-user code. It enters through thin adapters only when auth is enabled.

### Directory Structure (14 files)

| File | Purpose |
|---|---|
| `__init__.py` | Exports `CurrentUser`, `UserRecord`, `UserScope` |
| `models.py` | Data models: `CurrentUser` (id, username, role, scope), `UserRecord`, `UserScope` (kind, user_id, root), `KnowledgeResource` |
| `identity.py` | User store: CRUD for users in `data/system/auth/users.json`, password hashing, avatar management, role management, auth secret generation |
| `context.py` | Request-local `ContextVar` for `CurrentUser` with `set_current_user()` / `get_current_user()` |
| `paths.py` | File system layout: `data/user` (admin), `data/users/<uid>` (per-user), `data/system/` (grants, auth, audit), `data/partners/<id>` (partners). Legacy migration from sibling `multi-user/` directory |
| `grants.py` | Per-user resource grants (version 2): `models.llm`, `knowledge_bases`, `skills`, `partners`, `enabled_tools`, `mcp_tools`, `exec_enabled`. Stored as `data/system/grants/<user_id>.json`. Validates that grants don't contain secrets/paths |
| `model_access.py` | Model grant enforcement: `redacted_model_access()` filters catalog to only admin-granted models, `allowed_llm_options()` returns selectable models, `has_capability_access()` gates capability usage, `apply_allowed_llm_selection()` enforces model choice at runtime |
| `router.py` | FastAPI admin endpoints: `/admin/resources` (catalog, KBs, skills, partners, tools), `/users/{id}/grants` (GET/PUT), `/admin/skills/install`, `/users` (list) |
| `knowledge_access.py` | Per-user KB access based on grants |
| `skill_access.py` | Per-user skill access based on grants |
| `tool_access.py` | Per-user tool access control (enabled_tools, mcp_tools, exec_enabled) |
| `partner_access.py` | Per-user partner (companion bot) assignment |
| `audit.py` | Admin action logging |
| `grants.py` | Grant persistence and normalization |

### Access Control Model

- **Admin users** have full access to everything in the `data/user/` workspace
- **Non-admin users** only see resources explicitly granted by an admin via `grants.json`
- The grant system controls:
  - Which LLM **profile+model combinations** a user can select
  - Which **knowledge bases** a user can search
  - Which **skills** (agent capabilities) a user can invoke
  - Which **partners** (companion bots) a user can interact with
  - **Tool whitelists** (built-in tools and MCP tools)
  - **Code execution** policy override
- Both JSON/SQLite file backend and PocketBase are supported (PocketBase mode is documented as single-user-only currently)

### User Roles
- `admin` â€” full access to admin workspace (`data/user/`)
- `user` â€” restricted to granted resources from `data/users/<uid>/`

### Identity Store
- Default: `data/system/auth/users.json` (JSON file with thread-safe writes)
- Auth secret: `data/system/auth/auth_secret`
- Avatar images: `data/system/auth/avatars/<user_id>.{png,jpg,webp}`
- Environment variable fallback: `AUTH_USERNAME` + `AUTH_PASSWORD_HASH`
- First user registered automatically becomes admin

---

## 5. Rate Limiting and Usage Tracking

### Rate Limiting â€” `traffic_control.py`

The `TrafficController` class provides:
- **Concurrency gate**: `asyncio.Semaphore` with configurable `max_concurrency` (default: 20)
- **Token-bucket rate limiter**: configurable `requests_per_minute` (default: 600)
- **Acquisition timeout**: `acquisition_timeout` (default: 30s) before raising `asyncio.TimeoutError`
- Implemented as an async context manager (`async with TrafficController(...)`)
- Rate limit tokens are refilled per-second based on RPM/60

This is per-provider and is wired into the `LLMConfig` dataclass via `traffic_controller` and `max_concurrency`/`requests_per_minute` fields.

### Usage Tracking â€” `telemetry.py`

Currently a **minimal logging decorator** (`track_llm_call`) that logs:
- Provider name and function name before call
- Success/failure after call

There is no dedicated cost tracking or token usage persistence system in the LLM layer itself. Token usage is captured in responses (`usage.prompt_tokens`, `usage.completion_tokens`, `usage.total_tokens`) through the `LLMResponse.usage` field and `TutorResponse.usage` model, but there is no centralized usage aggregation or billing system visible in this layer. Cost summary is handled at the capability level via `UsageTracker` in `capabilities/_shared.py` (not in the LLM service layer).

---

## 6. Retry System

The retry system is comprehensive and multi-layered:

1. **Pydantic Settings**: `LLMRetryConfig` with `max_retries=8`, `base_delay=5.0`, `exponential_backoff=True`
2. **`LLMProvider._call_with_retry()`** in `provider_core/base.py`: Configurable retry delays, transient error detection (429, 5xx, timeouts, connection errors), image fallback (Stage-2: strips images and retries text-only for non-vision models)
3. **Response Format Auto-fallback**: When a provider rejects `response_format` with HTTP 400, it's stripped and retried once. Runtime-discovered incompatibilities are cached to skip `response_format` on future calls
4. **`_create_with_format_fallback()`** in `executors.py`: same logic for SDK-based calls
5. **Streaming fallback**: If streaming fails, falls back to non-streaming completion
6. **Provider-specific error classification** via `error_mapping.py` maps SDK errors to unified `LLMError` subclasses (rate limits, auth errors, context window errors, etc.)

*Novo passo iniciado*

---

*8 messages | 79 parts | ðŸ’° $0.0000 | â±ï¸ 0h01m14s*

