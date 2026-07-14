---
title: "witty-lagoon"
slug: "witty-lagoon"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: witty-lagoon
title: "Explore DeepTutor web codebase (@explore subagent)"
date: 2026-06-16
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m23s
messages: 13
parts: 96
cost: 0.012586
tokens_input: 63217
tokens_output: 8485
tokens_reasoning: 467
tokens_cache_read: 439040
tokens_cache_write: 0
created: "2026-06-16 03:19:15 UTC"
updated: "2026-06-16 03:20:38 UTC"
---

SessÃ£o com **13 messages**, **96 parts**, agente **explore**, modelo **deepseek-v4-flash** | ðŸ’° $0.0126 | ðŸ’¾ cache read: 439.0K | â±ï¸ 0h01m23s

## ðŸ‘¤ UsuÃ¡rio (2026-06-16 03:19:15 UTC)

Explore the codebase at C:\Users\frota\Documents\Projetos\AI TUTOR\web to understand:

1. How `apiFetch` is implemented (find it and read it fully)
2. How `listSessions` is implemented
3. How the API base URL is configured (look for API_URL, NEXT_PUBLIC_API_URL, or similar)
4. The WorkspaceSidebar component and how it calls listSessions
5. Any .env files or configuration that sets the API URL
6. The server/backend setup - is there a backend server that needs to be running?

Return ALL relevant code snippets and file paths with line numbers. Be very thorough - read every file you find that's relevant.

## ðŸ¤– Assistente (2026-06-16 03:19:15 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to thoroughly explore a codebase at `C:\Users\frota\Documents\Projetos\AI TUTOR\web` to understand several aspects of the API setup. Let me start by exploring the directory structure and then dive into each specific question.

</details>

### Resposta

I'll start by exploring the directory structure and then dive into each specific area.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:20 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me now read the key files: `lib/api.ts`, `.env.local`, `next.config.js`, the file containing `listSessions`, and find the WorkspaceSidebar component. Let me also look at proxy.ts.

</details>

### Resposta

Now let me read the key files in parallel:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:24 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I need to read the key files:
1. `lib/session-api.ts` - contains `listSessions`
2. `components/sidebar/WorkspaceSidebar.tsx` - the component
3. `components/space/ChatHistorySection.tsx` - also uses listSessions
4. Possibly the backend setup

Let me also look at the project root for any server setup documentation.

</details>

### Resposta

Let me now read the key implementation files:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:28 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also look at the client-cache module since `listSessions` uses it, and let me also look for the backend server setup. Let me also check the project root directory structure for backend files.

</details>

### Resposta

Now let me look at the client cache module, the `SidebarShell` component, the project root for backend/server files, and the `data/user/settings` directory:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:33 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me now look at the backend server setup. The project root has `deeptutor/` directory (the Python backend), `deeptutor_cli/`, `deeptutor_web/`, and various Docker/deployment files. Let me look at how the backend server is started and configured.

</details>

### Resposta

Let me now explore the backend server setup:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:37 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me now read the backend server setup files to understand how the server starts and how the API routes are set up.

</details>

### Resposta

Let me read the server setup files:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:42 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also read the SQLite store's list_sessions implementation and the session store protocol to understand the backend flow. Let me also check the Docker compose files and the `data/` directory.

</details>

### Resposta

Let me read the backend SQLite store and session protocol files, plus the Docker setup:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:47 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also check the `lib/auth.ts` to understand authentication setup, and look at the `data/user/settings/system.json` if it exists.

</details>

### Resposta

Let me check for the system.json settings file and also look at how `useTextSource` and `useBinarySource` use `apiFetch` directly (without `apiUrl`):

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:52 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also read the system.json and auth.json files to see the actual current configuration values.

</details>

### Resposta

Let me read the actual settings files:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:55 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive understanding of the codebase. Let me also read the Dockerfile to understand the production deployment fully.

</details>

### Resposta

Let me get one final piece â€” the Dockerfile and the pyproject.toml for the CLI entry:

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:19:59 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also get the entry point scripts defined in pyproject.toml.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-16 03:20:03 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have all the information needed. Let me compile the comprehensive report.

</details>

### Resposta

Now I have a complete picture. Here is the full, thorough report.

---

## Comprehensive Codebase Analysis: DeepTutor Web Frontend API Integration

### 1. `apiFetch` Implementation

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\lib\api.ts` (lines 140-153)

```typescript
export async function apiFetch(
  input: RequestInfo | URL,
  init?: RequestInit,
): Promise<Response> {
  const res = await fetch(input, { credentials: "include", ...init });

  if (res.status === 401 && AUTH_ENABLED && typeof window !== "undefined") {
    const next = encodeURIComponent(window.location.pathname);
    window.location.href = `/login?next=${next}`;
    return new Promise(() => {});
  }

  return res;
}
```

**Key behaviors:**
- Wraps the standard `fetch()` API, always passing `credentials: "include"` to send cookies.
- When `NEXT_PUBLIC_AUTH_ENABLED=true` and a 401 is returned, it redirects to `/login` with a `?next=` parameter so the user returns to the page they were on after login.
- If auth is disabled (the default), 401 responses pass through without redirect.

The helper function `apiUrl()` (lines 102-111) is used in conjunction to construct the full URL:

```typescript
export function apiUrl(path: string): string {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  const base = resolveBase();
  const normalizedBase = base.endsWith("/") ? base.slice(0, -1) : base;
  return `${normalizedBase}${normalizedPath}`;
}
```

---

### 2. `listSessions` Implementation

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\lib\session-api.ts` (lines 131-157)

```typescript
export async function listSessions(
  limit = 50,
  offset = 0,
  options?: { force?: boolean },
): Promise<SessionSummary[]> {
  const qs = new URLSearchParams({
    limit: String(limit),
    offset: String(offset),
  });
  return withClientCache<SessionSummary[]>(
    `sessions:${limit}:${offset}`,
    async () => {
      const response = await apiFetch(
        apiUrl(`/api/v1/sessions?${qs.toString()}`),
        { cache: "no-store" },
      );
      const data = await expectJson<{ sessions: SessionSummary[] }>(response);
      return data.sessions ?? [];
    },
    { force: options?.force, ttlMs: 15_000 },
  );
}
```

**Key behaviors:**
- Calls `GET /api/v1/sessions?limit=N&offset=0` through `apiFetch`.
- Uses a client-side cache (`withClientCache`) with a 15-second TTL. When `force: true` is passed, the cache is bypassed.
- The `expectJson` helper (lines 119-129) handles errors and 401 redirects:

```typescript
async function expectJson<T>(response: Response): Promise<T> {
  if (response.status === 401 && typeof window !== "undefined") {
    const next = encodeURIComponent(window.location.pathname);
    window.location.href = `/login?next=${next}`;
    return new Promise(() => {});
  }
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json() as Promise<T>;
}
```

---

### 3. API Base URL Configuration

There are **multiple layers** of API URL configuration, with a fallback chain:

#### Layer 1: `next.config.js` (build-time resolution)

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\next.config.js` (lines 32-61)

```javascript
const SETTINGS_DIR = path.resolve(__dirname, "..", "data", "user", "settings");
const SYSTEM_SETTINGS = readJsonFile(path.join(SETTINGS_DIR, "system.json"));

const BACKEND_PORT = firstNonEmpty(
  process.env.BACKEND_PORT,
  SYSTEM_SETTINGS.backend_port,
  "8001",  // default
);

const NEXT_PUBLIC_API_BASE = firstNonEmpty(
  process.env.NEXT_PUBLIC_API_BASE_EXTERNAL,   // highest priority
  SYSTEM_SETTINGS.next_public_api_base_external,
  process.env.NEXT_PUBLIC_API_BASE,
  SYSTEM_SETTINGS.next_public_api_base,
  `http://localhost:${BACKEND_PORT}`,           // final fallback
);

process.env.NEXT_PUBLIC_API_BASE = NEXT_PUBLIC_API_BASE;
```

**Priority chain (highest to lowest):**
1. `process.env.NEXT_PUBLIC_API_BASE_EXTERNAL` â€” Docker/CI override
2. `system.json` â†’ `next_public_api_base_external` â€” user settings
3. `process.env.NEXT_PUBLIC_API_BASE` â€” env var from `.env.local` or shell
4. `system.json` â†’ `next_public_api_base` â€” user settings
5. `http://localhost:8001` â€” hardcoded default (port from `BACKEND_PORT`)

#### Layer 2: `.env.local` (development override)

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\.env.local` (2 lines)

```
NEXT_PUBLIC_API_BASE=http://localhost:8001
NEXT_PUBLIC_AUTH_ENABLED=false
```

#### Layer 3: `system.json` (runtime settings)

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\system.json`

```json
{
  "version": 1,
  "backend_port": 8001,
  "frontend_port": 3782,
  "next_public_api_base_external": "",
  "next_public_api_base": "",
  "cors_origin": "",
  "cors_origins": [],
  "disable_ssl_verify": false,
  "chat_attachment_dir": "",
  "sandbox_allow_subprocess": true
}
```

#### Layer 4: Runtime URL Resolution (`resolveBase()`)

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\lib\api.ts` (lines 73-95)

```typescript
export function resolveBase(): string {
  const base = assertApiBaseConfigured(API_BASE_URL);
  if (typeof window === "undefined") return base;
  try {
    const url = new URL(base);
    const clientHost = window.location.hostname;
    if (isLoopbackHost(url.hostname) && !isLoopbackHost(clientHost)) {
      url.hostname = clientHost;
      // ...warning logged...
      return url.toString().replace(/\/+$/, "");
    }
  } catch {
    // base is not a valid absolute URL â€“ return as-is
  }
  return base;
}
```

This handles the **LAN/remote machine scenario**: if the app was configured with `http://localhost:8001` but is being accessed from another machine (e.g., `192.168.1.100`), it rewrites the hostname to match `window.location.hostname` so API requests reach the actual server.

#### Layer 5: Docker/Production â€” Placeholder Substitution

In Docker builds, the `Dockerfile` (lines 42-46) creates `.env.local` with placeholders:

```dockerfile
RUN printf '%s\n' \
    'NEXT_PUBLIC_API_BASE=__NEXT_PUBLIC_API_BASE_PLACEHOLDER__' \
    'NEXT_PUBLIC_AUTH_ENABLED=__NEXT_PUBLIC_AUTH_ENABLED_PLACEHOLDER__' \
    > .env.local
```

At container runtime, the launcher (`runtime/launcher.py`, lines 497-521) substitutes these placeholders with the real values:

```python
def _patch_packaged_web_placeholders(web_dir, *, api_base, auth_enabled):
    replacements = {
        "__NEXT_PUBLIC_API_BASE_PLACEHOLDER__": api_base,
        "__NEXT_PUBLIC_AUTH_ENABLED_PLACEHOLDER__": auth_enabled,
    }
```

The `api.ts` code explicitly detects if the placeholder was never substituted (lines 19-21, 23-41), throwing a clear error:

```typescript
const API_BASE_PLACEHOLDER_TOKEN = "NEXT_PUBLIC_API_BASE_PLACEHOLDER";
export function isApiBasePlaceholder(value: string): boolean {
  return value.includes(API_BASE_PLACEHOLDER_TOKEN);
}
```

---

### 4. WorkspaceSidebar Component and Its Call to `listSessions`

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\app\(workspace)\layout.tsx` (lines 1-18)

The sidebar is used inside the workspace layout:

```tsx
<UnifiedChatProvider>
  <div className="flex h-screen overflow-hidden">
    <WorkspaceSidebar />
    <main className="flex-1 overflow-hidden bg-[var(--background)]">
      {children}
    </main>
  </div>
</UnifiedChatProvider>
```

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\sidebar\WorkspaceSidebar.tsx` (full file, 143 lines)

The call to `listSessions` happens inside a `refreshSessions` callback (lines 31-43):

```tsx
const refreshSessions = useCallback(async () => {
  if (!hasLoadedSessionsRef.current) {
    setLoadingSessions(true);
  }
  try {
    setSessions(await listSessions(50, 0, { force: true }));
    hasLoadedSessionsRef.current = true;
  } catch (error) {
    console.error("Failed to load sessions", error);
  } finally {
    setLoadingSessions(false);
  }
}, []);
```

It is triggered by a `useEffect` (lines 50-52):

```tsx
useEffect(() => {
  void refreshSessions();
}, [refreshSessions, sidebarRefreshToken]);
```

The `sidebarRefreshToken` comes from `useUnifiedChat()` context â€” it increments on `STREAM_END`, server-side session bind, or turn deletion, causing automatic re-fetch.

The data flows into `SidebarShell` (lines 125-142):

```tsx
return (
  <SidebarShell
    showSessions
    sessions={orderedSessions}
    activeSessionId={selectedSessionId}
    loadingSessions={loadingSessions}
    onNewChat={handleNewChat}
    onSelectSession={handleSelectSession}
    onRenameSession={handleRenameSession}
    onDeleteSession={handleDeleteSession}
    footerSlot={<><AdminLink /><LogoutButton /></>}
  />
);
```

`SidebarShell` (`C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\sidebar\SidebarShell.tsx`, lines 350-361) passes sessions to `SessionList`:

```tsx
{!recentsCollapsed && (
  <div className="min-h-0 flex-1 overflow-y-auto px-2 pb-2 pt-0.5">
    <SessionList
      sessions={sessions}
      activeSessionId={activeSessionId}
      loading={loadingSessions}
      onSelect={onSelectSession}
      onRename={onRenameSession}
      onDelete={onDeleteSession}
      compact
    />
  </div>
)}
```

---

### 5. `.env` Files and Configuration

Only one `.env` file exists:

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\.env.local`

```
NEXT_PUBLIC_API_BASE=http://localhost:8001
NEXT_PUBLIC_AUTH_ENABLED=false
```

The authoritative settings live in the **project root's `data/user/settings/`** directory:

| File | Path |
|------|------|
| `system.json` | `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\system.json` |
| `auth.json` | `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\auth.json` |
| `integrations.json` | `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\integrations.json` |
| `model_catalog.json` | `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\model_catalog.json` |
| `main.yaml` | `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\main.yaml` |
| `interface.json` | `C:\Users\frota\Documents\Projetos\AI TUTOR\data\user\settings\interface.json` |

The `next.config.js` reads `system.json` as the source of truth, with environment variables as overrides (see section 3 above).

---

### 6. Backend Server Setup

The backend is a **FastAPI server** running on **port 8001** (configurable). It is part of the same Python package as the frontend.

#### Server Entry Points

There are **two ways** to start the backend:

**A. `deeptutor serve` (standalone API server)**

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\run_server.py` (lines 30-73)

Starts uvicorn programmatically on the configured port:

```python
def main() -> None:
    project_root = get_runtime_home()
    os.chdir(str(project_root))
    backend_port = get_backend_port(project_root)  # defaults to 8001

    uvicorn.run(
        "deeptutor.api.main:app",
        host="0.0.0.0",
        port=backend_port,
        reload=True,
    )
```

**B. `deeptutor start` (backend + frontend together)**

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\runtime\launcher.py` (lines 722-911)

The launcher:
1. Reads settings from `data/user/settings/system.json`
2. Spawns the backend process: `python -m uvicorn deeptutor.api.main:app --host 0.0.0.0 --port 8001`
3. Spawns the frontend (either Next.js standalone from `deeptutor_web` package, or `npm run dev` from the source `web/` directory)
4. Waits for both to be ready, then prints the URL

**Key launcher logic** (lines 823-864):

```python
backend_cmd = [
    sys.executable, "-m", "uvicorn",
    "deeptutor.api.main:app",
    "--host", "0.0.0.0",
    "--port", str(backend_port),
    "--log-level", "info",
]
backend = _spawn(backend_cmd, cwd=runtime_home, env=common_env, name="backend")
```

#### C. `docker-compose.yml` (production)

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\docker-compose.yml`

Three services:
- `deeptutor` â€” the main app container (FastAPI + Next.js) on ports 8001/3782
- `pocketbase` â€” optional auth/database sidecar on port 8090
- `sandbox-runner` â€” isolated code execution sidecar on port 8900

#### FastAPI Application

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\main.py` (lines 212-408)

Creates the FastAPI app, mounts all routers including the sessions router at `/api/v1/sessions`:

```python
app = FastAPI(title="DeepTutor API", version="1.0.0", lifespan=lifespan)
# ...CORS middleware...
app.include_router(sessions.router, prefix="/api/v1/sessions", tags=["sessions"], dependencies=_auth)
```

All non-auth routes require `Depends(require_auth)` â€” but when `AUTH_ENABLED=false` (the default), `require_auth` is a no-op.

#### Sessions API Endpoint

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\api\routers\sessions.py` (lines 80-87)

```python
@router.get("")
async def list_sessions(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
):
    store = get_session_store()
    sessions = await store.list_sessions(limit=limit, offset=offset)
    return {"sessions": sessions}
```

#### Session Store â€” SQLite (default)

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\session\sqlite_store.py` (lines 1125-1204)

The default session store is SQLite (PocketBase is optional). The query lists sessions sorted by `updated_at DESC`, with a subquery for the latest turn status and last message content:

```python
def _list_sessions_sync(self, limit=50, offset=0):
    with self._connect() as conn:
        rows = conn.execute("""
            SELECT s.id, s.title, s.created_at, s.updated_at,
                   s.compressed_summary, s.summary_up_to_msg_id,
                   s.preferences_json,
                   COUNT(m.id) AS message_count,
                   (SELECT t.status FROM turns t WHERE t.session_id = s.id
                    ORDER BY t.updated_at DESC LIMIT 1) AS status,
                   (SELECT t.id FROM turns t
                    WHERE t.session_id = s.id AND t.status = 'running'
                    ORDER BY t.updated_at DESC LIMIT 1) AS active_turn_id,
                   (SELECT m2.content FROM messages m2
                    WHERE m2.session_id = s.id AND TRIM(COALESCE(m2.content,'')) != ''
                    ORDER BY m2.id DESC LIMIT 1) AS last_message
            FROM sessions s
            LEFT JOIN messages m ON m.session_id = s.id
            GROUP BY s.id
            ORDER BY s.updated_at DESC
            LIMIT ? OFFSET ?
        """, (limit, offset)).fetchall()
```

#### Session Store Protocol

**File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\deeptutor\services\session\protocol.py` (lines 70-74)

```python
async def list_sessions(
    self,
    limit: int = 50,
    offset: int = 0,
) -> list[dict[str, Any]]: ...
```

---

### Complete Request Flow Summary

```
Browser
  â”‚
  â”œâ”€â”€ WorkspaceSidebar.tsx line 36:
  â”‚     listSessions(50, 0, { force: true })
  â”‚
  â”œâ”€â”€ session-api.ts line 131:
  â”‚     withClientCache(key="sessions:50:0", loader, {force, ttlMs:15000})
  â”‚       â”‚
  â”‚       â”œâ”€â”€ api.ts line 73:  resolveBase() â†’ "http://localhost:8001"
  â”‚       â”œâ”€â”€ api.ts line 102: apiUrl("/api/v1/sessions?limit=50&offset=0")
  â”‚       â”‚                     â†’ "http://localhost:8001/api/v1/sessions?limit=50&offset=0"
  â”‚       â””â”€â”€ api.ts line 140: apiFetch(url, { cache: "no-store" })
  â”‚             â”‚
  â”‚             â””â”€â”€ fetch("http://localhost:8001/api/v1/sessions?limit=50&offset=0",
  â”‚                        { credentials: "include", cache: "no-store" })
  â”‚
  â”œâ”€â”€ FastAPI (backend, deeptutor/api/main.py):
  â”‚     â””â”€â”€ sessions.router (prefix="/api/v1/sessions")
  â”‚           â””â”€â”€ GET "" â†’ list_sessions (sessions.py:81)
  â”‚                 â””â”€â”€ store.list_sessions(limit=50, offset=0)
  â”‚                       â””â”€â”€ SQLiteSessionStore (sqlite_store.py:1199)
  â”‚                             â””â”€â”€ SELECT ... FROM sessions ... ORDER BY updated_at DESC LIMIT 50
  â”‚
  â””â”€â”€ Response: { sessions: SessionSummary[] }
```

### Key Takeaways

1. **The backend must be running** at the configured API URL (default `http://localhost:8001`). Without the FastAPI server, all API calls will fail.

2. **Configuration sources** (in priority order): env var `NEXT_PUBLIC_API_BASE_EXTERNAL` â†’ `system.json:next_public_api_base_external` â†’ env var `NEXT_PUBLIC_API_BASE` â†’ `system.json:next_public_api_base` â†’ hardcoded `http://localhost:8001`.

3. **Current config** resolves to: `NEXT_PUBLIC_API_BASE=http://localhost:8001` from `.env.local`, with `NEXT_PUBLIC_AUTH_ENABLED=false` in `auth.json`.

4. **The client-side cache** in `withClientCache` holds session list data for 15 seconds, with `force: true` bypassing it.

5. **Three ways to run the backend:**
   - `deeptutor serve` â€” starts only the FastAPI backend
   - `deeptutor start` â€” starts both backend and frontend
   - `docker-compose up` â€” full containerized deployment with PocketBase and sandbox

*Novo passo iniciado*

---

*13 messages | 96 parts | ðŸ’° $0.0126 | â±ï¸ 0h01m23s*

