---
slug: lucky-mountain
title: "Explore DeepTutor test setup (@explore subagent)"
date: 2026-07-12
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h00m55s
messages: 9
parts: 55
cost: 0.007233
tokens_input: 34751
tokens_output: 6159
tokens_reasoning: 350
tokens_cache_read: 194688
tokens_cache_write: 0
created: "2026-07-12 02:27:26 UTC"
updated: "2026-07-12 02:28:22 UTC"
---

Sessão com **9 messages**, **55 parts**, agente **explore**, modelo **deepseek-v4-flash** | 💰 $0.0072 | 💾 cache read: 194.7K | ⏱️ 0h00m55s

## 👤 Usuário (2026-07-12 02:27:26 UTC)

I need to understand the DeepTutor project's testing and code quality setup in detail. Look at:

1. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\pyproject.toml` — find all tool configurations (pytest, ruff, mypy, coverage)
2. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\web\package.json` — find lint/test/typecheck scripts
3. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\__init__.py` — just first 10 lines
4. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\tests\` — list the test directory structure, see how existing tests are organized
5. Read one existing test file completely (preferably the simplest one) to understand the test style, fixtures, and patterns used
6. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\main.py` — the first 30 lines to understand how the FastAPI app is created
7. Read `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\routers\` — list the existing routers to understand the pattern

Return: 
- The full pytest config from pyproject.toml
- The ruff and mypy settings
- The npm test/lint/typecheck scripts
- The test directory structure
- An example test file (full content of one small test)
- How the FastAPI app is created (main.py)
- How existing routers are organized
- The full ruff lint command used

## 🤖 Assistente (2026-07-12 02:27:26 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants a comprehensive understanding of the DeepTutor project's testing and code quality setup. Let me gather all the requested information systematically.

</details>

### Resposta

I'll gather all the requested information in parallel.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:30 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to:
1. Find and read a simple test file to understand the test style
2. Check the conftest.py
3. Look at the test directory structure more deeply
4. Find the ruff lint command used (from AGENTS.md or scripts)

Let me look at a simple test file and the conftest.py, and also check for scripts that show the ruff command.

</details>

### Resposta

Now let me get the test structure details, a sample test file, the conftest, and search for the ruff lint command used.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:35 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now read a simple test file. Let me pick one that seems small - maybe `tests/test_matrix_requirements.py` or `tests/test_openrouter_provider.py`. Let me also look at one of the simpler tool tests, like `test_ask_user.py` or `test_web_fetch.py`.

Let me also check for the ruff command in the AGENTS.md or any other config files, and get the full glob of test files.

I need more data. Let me fetch the full glob and also read a small test file.

</details>

### Resposta

Let me now read a small test file and search for the ruff/mypy commands used.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:40 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also get the pre-commit config to see the full ruff/mypy commands, and check for any CI config files, and read the `main.py` more completely to see the FastAPI app creation pattern.

</details>

### Resposta

Let me get the pre-commit config for the exact ruff/mypy commands, and check for CI config.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:43 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me read a bit more of main.py to see the actual FastAPI app creation and lifespan.

</details>

### Resposta

Let me get the FastAPI app creation part from main.py and look for the `create_app` function.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:46 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me read the rest of main.py to see the actual FastAPI app creation.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me continue reading to see the router mounting pattern.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-07-12 02:27:50 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have all the information needed to provide a comprehensive answer. Let me also check what `requirements/dev.txt` looks like for the `--ruff-lint` command.

</details>

### Resposta

Now I have all the pieces. Here is the comprehensive report.

---

## DeepTutor Testing & Code Quality Setup -- Full Report

---

### 1. Full Pytest Configuration (`pyproject.toml`)

**Section (lines 408-422):**
```toml
[tool.pytest.ini_options]
testpaths = ["tests", "deeptutor/learning/tests"]
pythonpath = ["."]
markers = [
    "asyncio: mark async tests that require pytest-asyncio",
]
asyncio_default_fixture_loop_scope = "function"
addopts = [
    "--strict-markers",
    "--strict-config",
    "--disable-warnings",
    "--tb=short",
    "--import-mode=importlib",
]
```

**Key details:**
- **Test discovery:** searches `tests/` and `deeptutor/learning/tests/`
- **Python path:** `.` so imports work as `from deeptutor...`
- **asyncio:** fixtures default to function-scoped loop (`asyncio_default_fixture_loop_scope = "function"`)
- **Strict mode:** unknown markers and config errors are raised
- **Import mode:** `importlib` (the modern, safe approach -- no `sys.path` hacks)
- **Test output:** short tracebacks, no warnings

---

### 2. Ruff Settings (`pyproject.toml`)

**Section (lines 289-404):**
```toml
[tool.ruff]
target-version = "py311"
line-length = 100

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "F",   # pyflakes (unused imports, variables, etc.)
    "I",   # isort (import sorting)
]
extend-select = [
    "B006",  # Do not use mutable data structures for argument defaults
]
ignore = [
    "E501",  # Line too long (handled by formatter)
    "B008",  # Do not perform function calls in argument defaults
    # ... many deliberately relaxed rules ...
    "E722",  # bare except
    "E402",  # module-level import not at top
    "F841",  # unused variable
    "ERA001", # commented-out code
    # ... (full list above)
]

# Per-file ignores
[tool.ruff.lint.per-file-ignores]
"**/test_*.py" = ["E501", "PLR2004", "F401"]
"**/__init__.py" = ["F401"]

[tool.ruff.lint.isort]
known-first-party = ["deeptutor", "deeptutor_cli", "scripts"]
force-sort-within-sections = true

[tool.ruff.lint.mccabe]
max-complexity = 10

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

**Philosophy:** The lint profile is intentionally **minimal** -- only `E`, `F`, `I` (plus `B006`) are selected. Many rules are explicitly ignored. The ruff **formatter** handles line length and style. Complexity is capped at 10.

---

### 3. Mypy Settings (`pyproject.toml`)

**Section (lines 427-450):**
```toml
[tool.mypy]
python_version = "3.11"
pretty = false
show_error_context = false
warn_return_any = false
warn_no_return = false
show_error_codes = true
ignore_missing_imports = true
follow_imports = "silent"
check_untyped_defs = false
disallow_untyped_defs = false
disallow_incomplete_defs = false
no_implicit_optional = false

[[tool.mypy.overrides]]
module = "tests.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "deeptutor.tools.*"
ignore_errors = true
```

**Philosophy:** **Very relaxed** -- mypy is in "gradual adoption" mode. Most strict checks are off. Tests and tools are entirely ignored. This is explicitly a work-in-progress.

---

### 4. Pre-commit Hooks (the actual commands run)

From `.pre-commit-config.yaml` (lines 42-50, 97-102):

| Hook | Command / Args |
|---|---|
| **ruff lint** | `ruff` with `--fix --quiet --exit-zero` |
| **ruff format** | `ruff-format --quiet` |
| **mypy** | `mypy --ignore-missing-imports --no-error-summary --no-strict-optional` (excludes `tests/`, `scripts/`, `deeptutor/agents/`, `deeptutor/services/rag/`, `deeptutor/api/routers/`) |
| **bandit** | `bandit -c pyproject.toml -q` (excludes `tests/`) |
| **prettier** (frontend) | `prettier --log-level warn` on `web/` files |
| **detect-secrets** | `detect-secrets --baseline .secrets.baseline` |

**The full ruff lint command is:**
```
ruff --fix --quiet --exit-zero
```
(When run without pre-commit, it would be `ruff check` with the settings from `pyproject.toml`.)

---

### 5. NPM Scripts (`web/package.json`)

```jsonc
{
  "scripts": {
    "dev":           "node --max-old-space-size=4096 ./node_modules/next/dist/bin/next dev",
    "dev:turbo":     "node --max-old-space-size=6144 ./node_modules/next/dist/bin/next dev --turbopack",
    "build":         "next build",
    "start":         "next start",
    "lint":          "eslint .",
    "test:node":     "node ./scripts/run-node-tests.mjs",
    "perf:check":    "node ./scripts/route_budgets.mjs",
    "build:perf":    "npm run build && npm run perf:check",
    "i18n:parity":   "node ./scripts/i18n_parity.mjs",
    "i18n:audit":    "node ./scripts/i18n_audit.mjs",
    "i18n:audit:strict": "node ./scripts/i18n_audit.mjs --strict",
    "i18n:check":    "npm run i18n:parity && npm run i18n:audit",
    "audit":         "playwright test --project=ui-audit",
    "audit:ui":      "playwright test --ui --project=ui-audit",
    "audit:report":  "playwright show-report"
  }
}
```

**Key observations:**
- **Lint:** `npm run lint` runs `eslint .`
- **Test:** `npm run test:node` runs a custom node script (`scripts/run-node-tests.mjs`) -- not Jest/Vitest
- **Typecheck:** There is **no explicit TypeScript type-check script** (no `tsc`). Type checking relies on the editor/IDE, presumably using the `tsconfig.json` via `tsc --noEmit` or Next.js's built-in type checking during `next build`.
- **Playwright:** used for UI audit/snapshot testing, not unit tests
- **Dev tooling:** Next.js 16, React 19, TypeScript 5, ESLint 9, Tailwind CSS 3

---

### 6. Test Directory Structure

```
tests/
├── conftest.py                         # Root fixtures (shared)
├── test_matrix_requirements.py         # Standalone (19 lines)
├── test_openrouter_provider.py         # Standalone (74 lines)
├── agents/
│   ├── __init__.py
│   ├── test_base_agent_binding.py
│   └── research/
│       ├── __init__.py
│       ├── test_rephrase_loop_host.py
│       ├── test_request_config.py
│       └── test_token_tracker_pricing.py
├── api/
│   ├── __init__.py
│   ├── test_auth_contextvar.py
│   ├── test_co_writer.py
│   ├── test_cors_settings.py
│   ├── test_imports.py
│   ├── test_knowledge_router.py
│   ├── test_knowledge_zip_upload.py
│   ├── test_main_notebook_router.py
│   ├── test_memory_resolver.py
│   ├── test_notebook_router.py
│   ├── test_partners_channel_schema.py
│   ├── test_partners_router.py
│   ├── test_plugins_api_partner.py
│   ├── test_question_router.py
│   ├── test_selective_access_log.py
│   ├── test_sessions_truncation.py
│   ├── test_settings_router.py
│   ├── test_skills_hub_router.py
│   ├── test_subagents_router.py
│   ├── test_system_router.py
│   ├── test_tools_router.py
│   ├── test_unified_ws_turn_runtime.py
│   └── test_voice_routes.py
├── book/
│   ├── test_context.py
│   ├── test_engine_controls.py
│   └── test_llm_writer.py
├── capabilities/
│   ├── __init__.py
│   ├── test_explore_context_capability.py
│   ├── test_obsidian_capability.py
│   ├── test_rag_consistency.py
│   ├── test_solve_capability.py
│   ├── test_status_i18n_consistency.py
│   └── test_subagent_capability.py
├── core/
├── knowledge/
├── logging/
│   ├── test_configure.py
│   ├── test_context.py
│   ├── test_loguru_bridge.py
│   ├── test_process_logs.py
│   └── test_task_log_stream.py
├── multi_user/
│   ├── conftest.py
│   ├── test_capability_access.py
│   ├── test_grants_and_settings.py
│   ├── test_identity_and_paths.py
│   ├── test_login_username_contract.py
│   ├── test_partner_access.py
│   ├── test_profile_avatar.py
│   ├── test_profile_router.py
│   ├── test_rag_tool_no_kb_fallback.py
│   ├── test_registration_invite_only.py
│   ├── test_resource_isolation.py
│   ├── test_settings_status_redaction.py
│   ├── test_skill_resolution_scoped.py
│   ├── test_tool_access.py
│   └── test_ui_language_scoping.py
├── runtime/
│   ├── __init__.py
│   ├── test_launcher.py
│   ├── test_orchestrator.py
│   ├── test_request_contracts_subagent.py
│   └── registry/
│       ├── test_deferred_tools.py
│       └── test_tool_registry_execute.py
├── scripts/
├── services/
├── tools/
│   ├── __init__.py
│   ├── test_ask_user.py
│   ├── test_file_tools.py
│   ├── test_github_query.py
│   ├── test_list_notebook.py
│   ├── test_mineru.py
│   ├── test_mineru_models.py
│   ├── test_question_extractor.py
│   ├── test_rag_tool.py
│   ├── test_web_fetch.py
│   ├── test_web_search.py
│   ├── test_write_note.py
│   └── test_youtube_playlist_search.py
└── utils/
    ├── __init__.py
    ├── test_archive_extractor.py
    ├── test_circuit_breaker.py
    ├── test_document_extractor.py
    ├── test_document_validator.py
    └── test_json_parser.py
```

---

### 7. Example Test File -- The Simplest One

**`tests/test_matrix_requirements.py`** (19 lines -- pure functions, no mocks):

```python
"""Tests for Matrix dependency split."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_matrix_default_requirements_do_not_install_e2e() -> None:
    text = (ROOT / "requirements" / "matrix.txt").read_text(encoding="utf-8")

    assert "matrix-nio[e2e]" not in text
    assert "matrix-nio>=0.25.2,<1.0.0" in text


def test_matrix_e2e_requirements_are_separate() -> None:
    text = (ROOT / "requirements" / "matrix-e2e.txt").read_text(encoding="utf-8")

    assert "-r matrix.txt" in text
    assert "matrix-nio[e2e]>=0.25.2,<1.0.0" in text
```

**Pattern observed:** Pure assertion-style tests with no fixtures, no classes, no mocks. Type hints used (`-> None`). Test file read patterns (simple file content checks).

---

### 8. Example Test File -- With Mocks & Fixtures

**`tests/test_openrouter_provider.py`** (74 lines -- `unittest.TestCase` style):

This uses **`unittest.TestCase`** with `MagicMock` and `patch.dict`. It tests the OpenRouter search provider by mocking the `openai` module and verifying:
- `WebSearchResponse` return type
- Citations extracted from both root and choice paths
- Provider name and content correctness

**Note:** This is the **old-style** approach. Newer tests use **pytest-style** fixtures (see `conftest.py` below).

---

### 9. Shared Fixtures (`tests/conftest.py` -- full content, 142 lines)

The root `conftest.py` provides:

| Fixture | Description |
|---|---|
| `_guard_legacy_multi_user_migration` (autouse) | Prevents tests from touching real `multi-user/` data |
| `stream_bus` | Fresh `StreamBus` instance |
| `minimal_context` | `UnifiedContext` with just `session_id`, `user_message`, `language` |
| `rich_context` | Full context with attachments, tools, KB, metadata, conversation history |
| `tmp_db_path` | `Path` to a temp file (uses pytest `tmp_path`) |
| `sqlite_store` | `SQLiteSessionStore` backed by the temp file |
| `stub_capability` | A `_StubCapability` (custom class inheriting `BaseCapability`) that emits one content event |
| `fake_llm_config` | `MagicMock` mimicking `LLMConfig` with common defaults |

**Pattern:** pytest-style fixtures with explicit type hints, `from __future__ import annotations`, lazy imports inside fixtures, and composition (e.g., `sqlite_store` depends on `tmp_db_path`).

---

### 10. How the FastAPI App Is Created (`deeptutor/api/main.py`)

**App creation (lines 219-228):**
```python
app = FastAPI(
    title="DeepTutor API",
    version="1.0.0",
    lifespan=lifespan,
    redirect_slashes=False,
)
```

**Key architecture:**
- **Lifespan handler** (`@asynccontextmanager` async def) manages startup/shutdown:
  - Startup: validates tool consistency, initializes LLM client, starts EventBus, auto-starts partner channels, starts cron service, pings PocketBase, runs v1 memory migration
  - Shutdown: stops cron, partners, EventBus
- **CORS middleware** is dynamically configured based on auth settings (permissive vs explicit)
- **Static files** mounted at `/api/outputs` with a custom `SafeOutputStaticFiles` class that whitelists paths
- **Selective access log middleware** -- only non-200 responses are logged
- **Router registration** follows a consistent pattern:
  - `auth.router` is mounted **without** auth dependency (public login/logout/register)
  - All other routers use `Depends(require_auth)` (no-op when auth is disabled)
  - Partner routers use `Depends(require_admin)` (admin-gated)
  - WebSocket routers (`unified_ws`, `quiz_judge`) handle auth **inside the handler**, not via FastAPI dependencies

---

### 11. How Existing Routers Are Organized

**File listing** (32 modules in `deeptutor/api/routers/`):

```
routers/
├── __init__.py
├── _partners_channel_schema.py
├── agent_config.py
├── attachments.py
├── auth.py
├── book.py
├── capabilities_settings.py
├── chat.py
├── co_writer.py
├── dashboard.py
├── imports.py
├── knowledge.py
├── mastery_path.py
├── mcp_settings.py
├── memory.py
├── notebook.py
├── partners.py
├── personas.py
├── plugins_api.py
├── project_state.py
├── question.py
├── question_notebook.py
├── quiz_judge.py
├── sessions.py
├── settings.py
├── skills.py
├── subagents.py
├── system.py
├── tools.py
├── unified_ws.py
└── voice.py
```

**Router mounting pattern** (each follows the same structure):
```python
app.include_router(chat.router, prefix="/api/v1", tags=["chat"], dependencies=_auth)
app.include_router(knowledge.router, prefix="/api/v1/knowledge", tags=["knowledge"], dependencies=_auth)
app.include_router(system.router, prefix="/api/v1/system", tags=["system"], dependencies=_auth)
# ...
app.include_router(unified_ws.router, prefix="/api/v1", tags=["unified-ws"])  # no auth dep
```

**Pattern:** Each router module exports a `router` (APIRouter), is imported and mounted with a distinct `prefix="/api/v1/<resource>"`, a matching `tags` group, and typically the shared `_auth` dependency. The two WebSocket routers (`unified_ws`, `quiz_judge`) skip the auth dependency because FastAPI dependencies don't work cleanly with WebSocket handshake rejection.

---

### 12. Summary of the Full Ruff Lint Command

From the pre-commit config:
```
ruff --fix --quiet --exit-zero
```

This is equivalent to `ruff check --fix --quiet --exit-zero` (the `check` subcommand is the default). It uses all settings from `pyproject.toml`:
- Only selects `E`, `F`, `I` rules + `B006`
- Line length 100, target Python 3.11
- Auto-fixes what it can, with `--exit-zero` so it always passes (soft fail in CI)
- Isort configured with first-party packages: `deeptutor`, `deeptutor_cli`, `scripts`

*Novo passo iniciado*

---

*9 messages | 55 parts | 💰 $0.0072 | ⏱️ 0h00m55s*
