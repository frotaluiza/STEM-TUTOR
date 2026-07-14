---
title: "playful-rocket"
slug: "playful-rocket"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: playful-rocket
title: "Explore DeepTutor frontend nav (@explore subagent)"
date: 2026-07-12
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h00m55s
messages: 9
parts: 64
cost: 0.009634
tokens_input: 53203
tokens_output: 5529
tokens_reasoning: 534
tokens_cache_read: 174208
tokens_cache_write: 0
created: "2026-07-12 02:34:50 UTC"
updated: "2026-07-12 02:35:45 UTC"
---

SessÃ£o com **9 messages**, **64 parts**, agente **explore**, modelo **deepseek-v4-flash** | ðŸ’° $0.0096 | ðŸ’¾ cache read: 174.2K | â±ï¸ 0h00m55s

## ðŸ‘¤ UsuÃ¡rio (2026-07-12 02:34:50 UTC)

Explore the DeepTutor frontend navigation structure at C:\Users\frota\Documents\Projetos\AI TUTOR\web\

I need to understand:
1. Read web/app/layout.tsx â€” the root layout with navigation/sidebar
2. Read web/app/page.tsx â€” the main/home page (likely the chat)
3. Search for any Sidebar, Navbar, Navigation, or Menu components in web/components/ and web/features/
4. Look at how existing features (chat, knowledge, settings, etc.) are linked in the navigation
5. Check for any routing patterns (next/router or next/navigation)
6. Read one navigation component completely to understand the structure

Return: 
- The navigation structure (what items exist, how they're rendered)
- The routing pattern used (App Router pages, dynamic routes)
- Where new menu items should be added
- How the layout.tsx handles different pages

## ðŸ¤– Assistente (2026-07-12 02:34:50 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to explore the DeepTutor frontend navigation structure. Let me start by reading the root layout and main page, and searching for navigation components.

</details>

### Resposta

I'll explore the DeepTutor frontend systematically. Let me start with multiple parallel reads and searches.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:34:54 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The main `page.tsx` doesn't exist at the root, and there are no page.tsx or layout.tsx files in subdirectories. Let me search more broadly for the app directory structure, navigation components, and page files.

</details>

### Resposta

Interesting â€” no `page.tsx` at root and no standard routes yet. Let me broaden the search.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:34:59 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Great findings! Now I can see:

1. The app uses Next.js App Router with route groups: `(admin)`, `(auth)`, `(utility)`, `(workspace)`
2. There's a `WorkspaceSidebar` at `@/components/sidebar/WorkspaceSidebar` (used in `(workspace)/layout.tsx`)
3. There's a `UtilitySidebar` at `@/components/sidebar/UtilitySidebar` (used in `(utility)/layout.tsx`)
4. The main page is `(workspace)/page.tsx` (since no root page.tsx, the workspace route group likely serves as the main interface)
5. There's a catch-all route `(workspace)/home/[[...sessionId]]/page.tsx` - this is the chat page
6. Navigation components live in `components/sidebar/`

Let me now read the key files:
- The workspace layout
- The two sidebar components
- The utility layout
- The main (workspace) page

</details>

### Resposta

Excellent! Now I can see the route groups and sidebar components. Let me read all the key files.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:35:05 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The glob patterns for sidebar components and pages didn't find anything (likely because these are TypeScript files with paths that have special characters). Let me try different patterns.

</details>

### Resposta

The glob may have issues with parenthesis in paths. Let me try direct reads and more specific patterns.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:35:09 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a clear picture of the entire routing structure. Let me now read the two sidebar components to understand the full navigation structure.

</details>

### Resposta

Now let me read the two sidebar components in full.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:35:11 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now let me also read the capability-routes file to understand the Capability type and how gating works, and also look at what other important navigation-related files exist.

</details>

### Resposta

Now let me check the capability routes (gating), the admin/auth layout, and one more sidebar-related file.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:35:16 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have a comprehensive view of the navigation structure. Let me also check if there's a `layout.tsx` inside `(workspace)\home\[[...sessionId]]` directory, and check for any `layout.tsx` files in the deeper route groups.

Actually, I have everything I need. Let me compile a comprehensive answer.

Let me also quickly check if there's a `(workspace)\playground\page.tsx` and the `CapabilityGate.tsx` to understand the gating mechanism at the page level.

</details>

### Resposta

Let me check one more file for the gating mechanism and the playground page.

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-07-12 02:35:19 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

I now have a comprehensive understanding of the DeepTutor frontend navigation structure. Let me compile the full report.

</details>

### Resposta

I now have a complete picture. Here is the full analysis.

---

## DeepTutor Frontend Navigation Structure

### 1. Route Groups (Next.js App Router)

The entire app uses **Next.js App Router** with **Route Groups** (parenthesized folders). There are **four route groups**, each with its own layout:

| Route Group Directory | Layout | Sidebar | Purpose |
|---|---|---|---|
| `(workspace)/` | `WorkspaceLayout` | `WorkspaceSidebar` | Main authenticated workspace (chat, partners, co-writer, book, playground) |
| `(utility)/` | `UtilityLayout` | `UtilitySidebar` | System consoles (memory, knowledge, settings, space, agents, notebook, profile) |
| `(auth)/` | `AuthLayout` | None (centered) | Login / Register |
| `(admin)/` | `AdminLayout` | None (full-width) | Admin user management |

**Key finding:** The root `layout.tsx` (`web/app/layout.tsx`) is a **thin shell** â€” it only provides fonts, theme script, `AppShellProvider`, `I18nClientBridge`, and `ToastViewport`. It does **not** render a sidebar directly; the sidebars are rendered by the route-group layouts.

The `layout.tsx` flow:
```
RootLayout (app/layout.tsx)
  â””â”€â”€ AppShellProvider â”€â”€ manages sidebar collapsed state
      â””â”€â”€ I18nClientBridge
          â””â”€â”€ Route Group Layout (workspace | utility | auth | admin)
              â””â”€â”€ Sidebar (WorkspaceSidebar | UtilitySidebar | none | none)
                  â””â”€â”€ main > CapabilityGate > page content
```

---

### 2. Navigation Items (from `SidebarShell.tsx`)

The sidebar is implemented by the reusable `SidebarShell` component. Both `WorkspaceSidebar` and `UtilitySidebar` render a `SidebarShell`, sharing the same nav structure. The nav entries are defined as arrays in `SidebarShell.tsx`:

#### PRIMARY_NAV (top section â€” workspace features)

| # | href | Label | Icon | Gated (`requires`) | Notes |
|---|---|---|---|---|---|
| 1 | `/home` | Home | `House` | `llm` | Main chat page. Clicking resets to a new session |
| 2 | `/partners` | Partners | `HeartHandshake` | `llm` | IM-connected companions |
| 3 | `/agents` | My Agents | `Bot` | (none) | Manage local Claude Code / Codex connections |
| 4 | `/co-writer` | Co-Writer | `PenLine` | `llm` | Long-form writing assistant |
| 5 | `/book` | Book | `Library` | `llm` | Interactive book reader |
| 6 | `/space` | Learning Space | `LayoutGrid` | (none) | Dashboard for skills, personas, notebooks, etc. |

#### SECONDARY_NAV (bottom section â€” system consoles)

| # | href | Label | Icon | Gated | Notes |
|---|---|---|---|---|---|
| 1 | `/memory` | Memory | `Brain` | (none) | Long-term memory console |
| 2 | `/knowledge` | Knowledge Center | `BookOpen` | (none) | KB and retrieval engine management |
| 3 | `/settings` | Settings | `Settings` | (none) | Full settings hub with many sub-pages |

**External links** (always present):
- Docs (`BookText` icon) â†’ `https://deeptutor.info/`
- GitHub (`Github` icon) â†’ `https://github.com/HKUDS/DeepTutor`

---

### 3. Complete Route Map (all `page.tsx` files)

#### Workspace routes (`(workspace)/`)

| Route | Page | Notes |
|---|---|---|
| `/` | `page.tsx` | **Redirects** to `/home` (with backward compat for `?session=` query params) |
| `/home` | `home/[[...sessionId]]/page.tsx` | **Catch-all** â€” the main chat page. `sessionId` is optional. |
| `/home/{sessionId}` | same page | Loads a specific chat session |
| `/partners` | `partners/page.tsx` | Partner list |
| `/partners/new` | `partners/new/page.tsx` | Create new partner |
| `/partners/{partnerId}` | `partners/[partnerId]/page.tsx` | Partner detail/chat |
| `/co-writer` | `co-writer/page.tsx` | Co-Writer landing |
| `/co-writer/{docId}` | `co-writer/[docId]/page.tsx` | Specific document |
| `/book` | `book/page.tsx` | Book reader (with `BookSidebar` component) |
| `/playground` | `playground/page.tsx` | Capability/tool testing playground |

#### Utility routes (`(utility)/`)

| Route | Page | Notes |
|---|---|---|
| `/agents` | `agents/page.tsx` | My Agents page |
| `/knowledge` | `knowledge/page.tsx` | Knowledge Center |
| `/memory` | `memory/page.tsx` | Memory hub |
| `/memory/graph` | `memory/graph/page.tsx` | Memory graph visualization |
| `/memory/l1` | `memory/l1/page.tsx` | L1 memory workbench |
| `/memory/l2` | `memory/l2/page.tsx` | L2 memory |
| `/memory/l2/{surface}` | `memory/l2/[surface]/page.tsx` | Dynamic route per surface |
| `/memory/l3` | `memory/l3/page.tsx` | L3 memory |
| `/memory/l3/{slot}` | `memory/l3/[slot]/page.tsx` | Dynamic route per slot |
| `/memory/resolve` | `memory/resolve/page.tsx` | Memory resolve tool |
| `/notebook` | `notebook/page.tsx` | Notebooks |
| `/profile` | `profile/page.tsx` | User profile |
| `/settings` | `settings/page.tsx` | Settings hub |
| `/settings/agents` | `settings/agents/page.tsx` | Agent settings |
| `/settings/agents/claude-code` | `settings/agents/claude-code/page.tsx` | Claude Code config |
| `/settings/agents/codex` | `settings/agents/codex/page.tsx` | Codex config |
| `/settings/appearance` | `settings/appearance/page.tsx` | Theme/appearance |
| `/settings/capabilities` | `settings/capabilities/page.tsx` | Capability settings |
| `/settings/chat` | `settings/chat/page.tsx` | Chat settings |
| `/settings/document-parsing` | `settings/document-parsing/page.tsx` | Document parsing |
| `/settings/embedding` | `settings/embedding/page.tsx` | Embedding config |
| `/settings/image` | `settings/image/page.tsx` | Image generation |
| `/settings/llm` | `settings/llm/page.tsx` | LLM configuration |
| `/settings/mcp` | `settings/mcp/page.tsx` | MCP settings |
| `/settings/memory` | `settings/memory/page.tsx` | Memory settings |
| `/settings/mineru` | `settings/mineru/page.tsx` | MinerU engine |
| `/settings/models` | `settings/models/page.tsx` | Model management |
| `/settings/network` | `settings/network/page.tsx` | Network/proxy |
| `/settings/search` | `settings/search/page.tsx` | Search settings |
| `/settings/status` | `settings/status/page.tsx` | System status |
| `/settings/stt` | `settings/stt/page.tsx` | Speech-to-text |
| `/settings/tools` | `settings/tools/page.tsx` | Tool toggles |
| `/settings/tts` | `settings/tts/page.tsx` | Text-to-speech |
| `/settings/video` | `settings/video/page.tsx` | Video settings |
| `/space` | `space/page.tsx` | Learning Space dashboard |
| `/space/chat-history` | `space/chat-history/page.tsx` | Chat history |
| `/space/learning` | `space/learning/page.tsx` | Mastery Path |
| `/space/notebooks` | `space/notebooks/page.tsx` | Notebooks in space |
| `/space/personas` | `space/personas/page.tsx` | Personas |
| `/space/project` | `space/project/page.tsx` | Project mind map |
| `/space/questions` | `space/questions/page.tsx` | Question bank |
| `/space/skills` | `space/skills/page.tsx` | Skills |

#### Auth routes (`(auth)/`)

| Route | Notes |
|---|---|
| `/login` | Login page |
| `/register` | Registration page |

#### Admin routes (`(admin)/`)

| Route | Notes |
|---|---|
| `/admin/users` | User management |

---

### 4. Routing Pattern

- **Library:** `next/navigation` (`useRouter`, `usePathname`, `useParams`, `useSearchParams`, `notFound`) â€” used throughout
- **Navigation elements:** `<Link>` from `next/link` for declarative links
- **Active detection:** `pathname.startsWith(item.href)` â€” prefix matching (e.g. `/home` matches `/home/abc123`)
- **Dynamic routes:**
  - `[[...sessionId]]` â€” **catch-all optional segment** for `/home/{sessionId}`
  - `[docId]` â€” dynamic param for co-writer documents
  - `[partnerId]` â€” dynamic param for partner detail
  - `[surface]`, `[slot]` â€” dynamic params for memory levels

---

### 5. Capability Gating System

Routes requiring an LLM are gated at **two levels**:

1. **Sidebar level** (`SidebarShell.tsx`, line 151-152):
   ```typescript
   const navLocked = (item: NavEntry) => item.requires ? !has(item.requires) : false;
   ```
   Locked items render as disabled (grayed out, cursor-not-allowed) with a `Lock` icon overlay and a tooltip.

2. **Page level** (`CapabilityGate.tsx`, used in both `WorkspaceLayout` and `UtilityLayout`):
   ```typescript
   const capability = capabilityForPath(pathname);
   // renders <RequireCapability capability={capability}>{children}</RequireCapability>
   ```

The gating rules are centralized in `web/lib/capability-routes.ts`:
```typescript
export const ROUTE_CAPABILITIES = [
  { prefix: "/home", capability: "llm" },
  { prefix: "/partners", capability: "llm" },
  { prefix: "/co-writer", capability: "llm" },
  { prefix: "/book", capability: "llm" },
  { prefix: "/space/learning", capability: "llm" },
  { prefix: "/playground", capability: "llm" },
];
```

---

### 6. Sidebar Collapse/Expand

Managed via `AppShellContext`:
- **State:** `sidebarCollapsed` (boolean), stored in `localStorage` under key `deeptutor.sidebarCollapsed`
- **Event:** `deeptutor:sidebar-collapsed` â€” dispatched to sync across tabs
- **Visual:** Collapsed = 60px wide (icons only); Expanded = 220px wide (icons + labels)
- **Session history ("Recents"):** Only shown in expanded state below the primary nav. Has its own collapsible toggle (`ChevronDown`) with localStorage persistence.

---

### 7. Where to Add New Menu Items

**Adding a primary/secondary nav item:**
Edit `web/components/sidebar/SidebarShell.tsx` and add an entry to either:
- `PRIMARY_NAV` array (lines 43-88) â€” for workspace features
- `SECONDARY_NAV` array (lines 90-110) â€” for system consoles

Each entry requires:
```typescript
{
  href: "/your-route",
  label: "Your Label",         // i18n key
  icon: YourLucideIcon,
  tooltipKey: "Your tooltip",  // optional
  requires: "llm",             // optional â€” omit if not gated
}
```

**Adding a sub-page of an existing feature:**
Simply create a new `page.tsx` in the appropriate route group directory. No sidebar changes needed â€” `pathname.startsWith()` auto-highlights the parent nav item.

**Important:** If the new route needs LLM gating, also add it to `ROUTE_CAPABILITIES` in `web/lib/capability-routes.ts`.

---

### 8. File Paths Summary

| File | Purpose |
|---|---|
| `web/app/layout.tsx` | Root layout (fonts, theme, AppShellProvider) |
| `web/app/(workspace)/layout.tsx` | Workspace layout (WorkspaceSidebar + CapabilityGate) |
| `web/app/(utility)/layout.tsx` | Utility layout (UtilitySidebar + CapabilityGate) |
| `web/app/(auth)/layout.tsx` | Auth layout (centered content, no sidebar) |
| `web/app/(admin)/layout.tsx` | Admin layout (full width, no sidebar) |
| `web/app/(workspace)/page.tsx` | Root redirect â†’ `/home` |
| `web/app/(workspace)/home/[[...sessionId]]/page.tsx` | Main chat page (catch-all) |
| `web/components/sidebar/SidebarShell.tsx` | **Central nav component** â€” defines PRIMARY_NAV + SECONDARY_NAV, renders collapsed/expanded sidebar |
| `web/components/sidebar/WorkspaceSidebar.tsx` | Wraps SidebarShell with workspace session logic |
| `web/components/sidebar/UtilitySidebar.tsx` | Wraps SidebarShell with utility session logic |
| `web/components/sidebar/SidebarShell.tsx` lines 43-88 | `PRIMARY_NAV` array |
| `web/components/sidebar/SidebarShell.tsx` lines 90-110 | `SECONDARY_NAV` array |
| `web/lib/capability-routes.ts` | `ROUTE_CAPABILITIES` â€” feature gating source of truth |
| `web/components/access/CapabilityGate.tsx` | Route-level gate wrapper |
| `web/components/access/CapabilityAccessContext.tsx` | Capability access provider (probes backend) |
| `web/context/AppShellContext.tsx` | Sidebar collapse state + cross-tab sync |

*Novo passo iniciado*

---

*9 messages | 64 parts | ðŸ’° $0.0096 | â±ï¸ 0h00m55s*

