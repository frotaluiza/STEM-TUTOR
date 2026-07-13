---
slug: clever-lagoon
title: "Explore web frontend viewers (@explore subagent)"
date: 2026-07-01
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m25s
messages: 14
parts: 96
cost: 0.015195
tokens_input: 78936
tokens_output: 7350
tokens_reasoning: 650
tokens_cache_read: 679936
tokens_cache_write: 0
created: "2026-07-01 20:34:37 UTC"
updated: "2026-07-01 20:36:02 UTC"
---

Sessão com **14 messages**, **96 parts**, agente **explore**, modelo **deepseek-v4-flash** | 💰 $0.0152 | 💾 cache read: 679.9K | ⏱️ 0h01m25s

## 👤 Usuário (2026-07-01 20:34:37 UTC)

Very thorough exploration: I need to understand how the DeepTutor Web frontend (Next.js) renders capability-specific output, especially how MathAnimatorViewer or any capability-specific viewers/components work.

Search in `C:\Users\frota\Documents\Projetos\AI TUTOR\web\` for:
1. How capability results are rendered (look for files mentioning "viewer", "capability", "render", "chat")
2. The component structure for rendering different capability outputs (check `web/app/`, `web/components/`, `web/src/` etc.)
3. How MathAnimatorViewer or similar capability viewers are structured
4. The WebSocket message handling (how capability results arrive and are dispatched to the right viewer)
5. Any existing iframe/embedded content support

Look for:
- Files containing "MathAnimatorViewer", "Viewer", "capability" 
- The chat message rendering pipeline
- Any plugin/viewer registration system

Return:
- The path to the main capability result renderer/viewer
- How new viewers/components are registered for specific capability types
- The component tree for rendering a chat message with capability-specific output
- Whether there's an iframe/sandbox mode for embedded third-party content
- An example of how math_animator results are rendered differently from chat results
- Any existing embedded game or interactive widget patterns

## 🤖 Assistente (2026-07-01 20:34:38 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants a thorough exploration of the DeepTutor Web frontend (Next.js) to understand how capability-specific output is rendered. Let me systematically search through the codebase.

Let me start with multiple parallel searches to understand the project structure.

</details>

### Resposta

I'll conduct a thorough exploration of the codebase. Let me start with several parallel searches to map out the structure.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:34:44 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me dig deeper into the key files identified. I need to look at:
1. The chat message rendering pipeline (ChatMessages.tsx)
2. The VisualizationViewer (which references MathAnimatorViewer)
3. The MathAnimatorViewer component itself
4. The WebSocket message handling (unified-ws.ts)
5. The message content types (message-content.ts)
6. The visualize-types.ts
7. The iframe-html.ts for embedded content

Let me read these files in parallel.

</details>

### Resposta

Good start. Let me now read the key files found in the search results.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:34:48 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a good picture of the main rendering pipeline. Let me also look at:
1. The visualize-types.ts to understand the VisualizeResult type
2. The iframe-html.ts to see the iframe support
3. The chat page that connects everything
4. The QuizViewer to understand another capability viewer
5. The ResearchOutlineEditor
6. The AssistantResponse component
7. The Mermaid component
8. Any existing embedded game/interactive widget patterns

Let me search for more files.

</details>

### Resposta

Excellent. Now let me read the remaining critical files - the visualize types, iframe support, chat page, and other viewers.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:34:54 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me continue reading the chat page and also look at the QuizViewer and the trailing parts of the chat page to understand how WebSocket events are dispatched. Let me also look for how the WebSocket events flow into the message rendering pipeline - specifically how messages with events arrive at the ChatMessages component.

</details>

### Resposta

Let me continue reading the chat page to understand the WebSocket event dispatching, and also the QuizViewer component.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:34:58 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look at the UnifiedChatContext to see how WS events are processed and how messages are built with events. Also need to look at the stream helper, and the AssistantResponse component.

</details>

### Resposta

Let me read more of the UnifiedChatContext to see the event dispatching logic, and also the stream helper and AssistantResponse.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:02 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look at the AssistantResponse component and also the CapabilityConfigCard to understand how config panels are loaded per capability. Also, let me search for any existing embedded game or interactive widget patterns.

</details>

### Resposta

Let me read the remaining key files - the AssistantResponse, CapabilityConfigCard, and search for game/interactive widget patterns.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:06 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look at the CapabilityConfigCard and the SessionViewerPanel for the iframe mode, and also search for any existing game/interactive patterns.

</details>

### Resposta

Let me check the CapabilityConfigCard and the SessionViewerPanel for their embedded content handling, and search for more game/interactive patterns.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:11 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look at the GeoGebra component to understand interactive widget patterns, and also search for how capability config panels are structured to understand how new capability viewers can be registered.

</details>

### Resposta

Let me look at the GeoGebra interactive component and the config panel structure for understanding the plugin/viewer registration pattern.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:16 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me look at the GeoGebra component to understand the interactive widget patterns, and also look at the quiz types to understand the full structure.

</details>

### Resposta

Let me read the GeoGebra component and the config panels to understand the full interactive widget and registration pattern.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:20 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the Geogebra.tsx component to understand the interactive widget pattern, and also look at the GeogebraTabContext to see how interactive tabs are opened.

</details>

### Resposta

Let me read the GeoGebra component and its context to understand the interactive widget pattern.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:24 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive understanding of the system. Let me also read the visualize folder for the SVG theme and look at the lib/playground-config to understand how capabilities are configured. Let me also look at the markdown rendering pipeline to understand if there's any more capability-related rendering.

</details>

### Resposta

Let me check the playground-config for capability configuration and the markdown renderer for any game/interactive patterns.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:29 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a very comprehensive picture. Let me compile the complete analysis. Let me also look at the full list of capabilities defined in the codebase to ensure complete coverage.

</details>

### Resposta

Let me do one final search to see the CAPABILITIES definition in the chat page and find any remaining capability-related patterns.

*Novo passo iniciado*

## 🤖 Assistente (2026-07-01 20:35:32 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a very thorough understanding of the entire system. Let me compile the comprehensive report.

</details>

### Resposta

Now I have a thorough understanding of the entire system. Here is the comprehensive report.

---

## DeepTutor Web Frontend — Capability Rendering Architecture

### 1. Main Capability Result Renderer/Viewer

**Primary file:**  
`C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\chat\home\ChatMessages.tsx`

This is the **central dispatcher** for all capability-specific output. The `AssistantMessage` component (lines 245-481) contains a multi-branch render tree that selects the appropriate viewer based on `msg.capability` and parsed result data:

```
AssistantMessage
  ├── (capability === "deep_research") && outlinePreview
  │     → AskUserOptions + ResearchOutlineEditor + AssistantResponse
  ├── (capability === "math_animator") && mathAnimatorResult
  │     → MathAnimatorViewer
  ├── (capability === "visualize") && visualizeResult
  │     → VisualizationViewer
  ├── (capability === "deep_question") && quizQuestions
  │     → AssistantResponse (preface) + QuizViewer
  ├── hasInlineAskUser (default chat with ask_user)
  │     → interleaved AssistantResponse + AskUserOptions
  └── default (plain chat)
        → AssistantResponse
```

**How capability is extracted from events (lines 284-325):**
- The `result` event (`event.type === "result"`) carries capability-specific metadata
- Each capability has a dedicated extractor function:
  - `extractMathAnimatorResult()` from `lib/math-animator-types.ts`
  - `extractVisualizeResult()` from `lib/visualize-types.ts`
  - `extractQuizQuestions()` from `lib/quiz-types.ts`
- These extractors guard on `msg.capability` before parsing

---

### 2. How New Viewers/Components Are Registered for Specific Capability Types

**There is NO plugin/viewer registration system.** Registration is done explicitly in three places:

#### a) Dynamic imports in `ChatMessages.tsx` (lines 56-70)
```typescript
const MathAnimatorViewer = dynamic(
  () => import("@/components/math-animator/MathAnimatorViewer"),
  { ssr: false },
);
const QuizViewer = dynamic(() => import("@/components/quiz/QuizViewer"), { ssr: false });
const ResearchOutlineEditor = dynamic(
  () => import("@/components/research/ResearchOutlineEditor"),
  { ssr: false },
);
const VisualizationViewer = dynamic(
  () => import("@/components/visualize/VisualizationViewer"),
  { ssr: false },
);
```

#### b) Capability definition in chat page (lines 198-258)
Each capability is defined as a `CapabilityDef` in `app/(workspace)/chat/[[...sessionId]]/page.tsx` with:
- `value` — the string identifier (e.g. `"visualize"`, `"deep_question"`)
- `label` — display name
- `allowedTools` and `defaultTools`

All capabilities listed:
| Value | Label | Has Viewer Component |
|---|---|---|
| `""` (empty) | Chat | `AssistantResponse` (no special viewer) |
| `deep_solve` | Solve | `AssistantResponse` (no special viewer) |
| `deep_question` | Quiz | `QuizViewer` |
| `deep_research` | Research | `ResearchOutlineEditor` |
| `visualize` | Visualize | `VisualizationViewer` |
| `mastery_path` | Mastery Path | `AssistantResponse` (no special viewer) |

#### c) Mode badge labels in `getModeBadgeLabel()` (lines 91-99)
Maps capability strings to human-readable labels. Also recognizes `math_animator` as a distinct capability here (though it's not in the CAPABILITIES dropdown).

#### d) Config panels for capabilities that need user config (lines 142-160)
```typescript
const CapabilityConfigCard = dynamic(
  () => import("@/components/chat/home/CapabilityConfigCard"),
  { ssr: false },
);
const QuizConfigPanel = dynamic(() => import("@/components/quiz/QuizConfigPanel"), { ssr: false });
const VisualizeConfigPanel = dynamic(
  () => import("@/components/visualize/VisualizeConfigPanel"),
  { ssr: false },
);
const ResearchConfigPanel = dynamic(
  () => import("@/components/research/ResearchConfigPanel"),
  { ssr: false },
);
```

**To add a new capability viewer, you would need to:**
1. Create the viewer component (e.g. `components/my-capability/MyViewer.tsx`)
2. Create the type extractor (e.g. `lib/my-capability-types.ts`)
3. Add a dynamic import in `ChatMessages.tsx`
4. Add a condition branch in the `AssistantMessage` render tree
5. Optionally add a capability definition to `CAPABILITIES` in the chat page
6. Optionally add a config panel

---

### 3. Component Tree for Rendering a Chat Message with Capability-Specific Output

```
ChatMessageList
  └── AssistantMessage (per assistant row)
        ├── AssistantActivity (trace/status header, always present)
        │
        ├── [capability decision tree — ONE of these branches renders]
        │
        ├── ResearchOutlineEditor (deep_research)
        │     └── outline sub_topics list + confirm/edit UI
        │
        ├── MathAnimatorViewer (math_animator)
        │     └── video <video> tags, image <img> grid, code <details>, metadata
        │
        ├── VisualizationViewer (visualize)
        │     ├── isManimResult → MathAnimatorViewer (delegation)
        │     ├── svg → SvgRenderer → SvgFigure (inline <svg> via DOMParser + sanitize)
        │     ├── chartjs → ChartJsRenderer (canvas + Chart.js)
        │     ├── mermaid → Mermaid
        │     ├── html → HtmlRenderer (<iframe sandbox="allow-scripts"> + srcdoc)
        │     └── comic → ComicRenderer (= HtmlRenderer)
        │     └── fullscreen portal (for non-html/comic types)
        │
        ├── QuizViewer (deep_question)
        │     └── question cards (choice/concept/fill-in-blank/short-answer/written/coding)
        │     └── answer state + submission + followup threads
        │
        ├── AssistantResponse (default / fallback)
        │     └── MarkdownRenderer (prose variant)
        │     └── ModelThinkingCard (for <think> segments)
        │
        └── AskUserOptions (pinned below, when applicable)
              └── option chips / free-text input (ask_user tool)
        
        └── GeneratedFileCards (exec/code_execution artifacts)
        └── Error cards (turn_terminal errors)
        └── Action buttons (Copy, Regenerate, Delete)
        └── CostFooter (token usage + cost)
```

---

### 4. WebSocket Message Handling — Event to Viewer Pipeline

**Connection:** `lib/unified-ws.ts` — `UnifiedWSClient` class
- Connects to `/api/v1/ws`
- Receives `StreamEvent` objects with fields: `type`, `source`, `stage`, `content`, `metadata`, `turn_id`, `seq`, etc.
- Heartbeat (ping/pong every 30s), auto-reconnect with backoff (max 5 attempts)
- Supports `resume_from` for reconnection mid-stream

**Event types:** `stage_start`, `stage_end`, `thinking`, `observation`, `content`, `tool_call`, `tool_result`, `progress`, `sources`, `result`, `error`, `session`, `session_meta`, `done`

**Event processing:** `context/UnifiedChatContext.tsx`
- The `UnifiedWSClient` is instantiated with an `onEvent` callback in the context provider
- Each event is dispatched as `STREAM_EVENT` action to the reducer (line 439-502)
- The reducer accumulates events onto the last assistant message's `events[]` array
- `content` events are appended to `msg.content` (with narration filtering via `lib/stream.ts`)
- The `result` event signals the final output — its `metadata` contains capability-specific payload
- `STREAM_END` sets `isStreaming: false`

**To the viewer:** Each message carries `events: StreamEvent[]`. The `AssistantMessage` component finds the `result` event and passes its `metadata` to the capability-specific extractor, which returns typed data for the appropriate viewer component.

---

### 5. Iframe/Sandbox Mode for Embedded Third-Party Content

**Yes, there is a well-established sandboxed iframe pattern.**

#### a) VisualizationViewer HTML Renderer (`components/visualize/VisualizationViewer.tsx`, lines 110-185)
```typescript
<iframe
  ref={iframeRef}
  title={t("HTML visualization")}
  sandbox="allow-scripts"
  className="w-full rounded-lg border border-[var(--border)] bg-[var(--card)]"
  style={{ minHeight: 320, height }}
/>
```
- Uses `srcdoc` attribute with `prepareIframeHtml()` for the content
- `sandbox="allow-scripts"` — **no `allow-same-origin`**, so the iframe runs in a null origin
- PostMessage bridge for: `dt:visualize-prompt` (send prompt to composer), `dt:visualize-height` (auto-resize)
- "Open in new tab" button creates a Blob URL

#### b) Iframe HTML preparation (`lib/iframe-html.ts`)
Three-layer pipeline: `prepareIframeHtml()` = `injectBridge(sanitizeIframeHtml(injectKaTeX(html)))`
1. **injectKaTeX** — auto-injects KaTeX CSS + JS for math rendering if not present
2. **sanitizeIframeHtml** — strips `javascript:` URLs and `target="_top"` / `target="_parent"`
3. **injectBridge** — injects a `sendPrompt()` function and `ResizeObserver` height reporter via postMessage

#### c) SessionViewerPanel iframe (`components/chat/home/SessionViewerPanel.tsx`, lines 978-998)
```typescript
<iframe
  key={url}
  src={url}
  title={host}
  onLoad={() => setLoaded(true)}
  className="h-full w-full border-0"
  sandbox="allow-scripts allow-same-origin allow-forms allow-popups"
  referrerPolicy="no-referrer"
/>
```
- More permissive sandbox (same-origin + forms + popups) — for browsing external URLs
- Has loading indicator and timeout detection
- Warning message when sites refuse embedding (X-Frame-Options / CSP frame-ancestors)

---

### 6. Math Animator Results vs. Chat Results — Rendering Comparison

#### Chat result (default)
- Rendered via `AssistantResponse` → `MarkdownRenderer` with `variant="prose"`
- Handles `content` string with markdown, code blocks, LaTeX, thinking segments
- Content is accumulated from streaming `content` events

#### Math Animator result
**Type definition** (`lib/math-animator-types.ts`):
```typescript
interface MathAnimatorResult {
  response: string;
  output_mode: "video" | "image";
  code: { language: string; content: string };
  artifacts: MathAnimatorArtifact[];  // { type, url, filename, label }
  timings: Record<string, number>;
  render: { quality?, retry_attempts?, visual_review?, ... };
  summary?: { summary_text?, user_request?, key_points? };
}
```

**Extraction** (`extractMathAnimatorResult`):
- Only returns a result when artifacts or render metadata are present
- A plain `response` field alone (common across capabilities) is ignored
- Guards against generic payloads (lines 76-84)

**Rendering** (`MathAnimatorViewer.tsx`):
- **Video section**: `<video controls>` tags for video artifacts
- **Image section**: Grid of clickable `<img>` thumbnails with fullscreen overlay via portal
- **Code section**: Collapsible `<details>` showing the Manim Python code
- **Visual review warning**: Amber alert when visual_review.passed === false
- **Metadata chips**: Quality, retry count, timing info
- No markdown rendering — content is purely artifact-driven

**Key difference**: Chat results render textual markdown; math_animator results render media artifacts (video/image) with code metadata, using the `response` text only as secondary info.

---

### 7. Existing Embedded Game or Interactive Widget Patterns

There are **no embedded games** in the frontend, but there are two clear interactive widget patterns:

#### a) GeoGebra Interactive Geometry (`components/Geogebra.tsx`)
- Loads GeoGebra's `deployggb.js` from CDN (shared single-loader pattern)
- Injects a `<div>` container and instantiates a `GGBApplet`
- Commands parsed from `ggbscript` text (one command per line, `#` comments)
- PostMessage-free: pure in-page DOM
- Invoked from markdown via `GeogebraOpenCTA` → opens in side viewer panel tab
- Context: `GeogebraTabContext` bridges CTA clicks to the viewer panel

#### b) Interactive SVG nodes (`components/visualize/VisualizationViewer.tsx`, lines 318-335)
```typescript
const onSvgClick = (e: MouseEvent<HTMLDivElement>) => {
  const node = (e.target as Element).closest?.("[data-prompt]");
  const prompt = node?.getAttribute("data-prompt")?.trim();
  if (prompt) {
    window.dispatchEvent(
      new CustomEvent("dt:visualize-prompt", { detail: prompt }),
    );
  }
};
```
- SVG nodes with `data-prompt` attributes are clickable
- Clicking dispatches a custom event that the chat page listens for
- Prefills the composer with a follow-up question (not auto-send)
- Theme-aware SVG via `svg-theme.css` (light/dark mode CSS variables)

#### c) Visualize HTML iframe bridge (`lib/iframe-html.ts`)
- `window.sendPrompt(text)` injected into the iframe → postMessage → window.dispatchEvent → prefills composer
- ResizeObserver for auto-height (avoids scroll clipping)

---

### Summary of Key Files

| File | Purpose |
|---|---|
| `components/chat/home/ChatMessages.tsx` | **Main capability dispatcher** — branches by capability + parsed result to select viewer |
| `components/math-animator/MathAnimatorViewer.tsx` | Math animator output renderer (video/image/code) |
| `components/visualize/VisualizationViewer.tsx` | Visualize output renderer (SVG/Chart.js/Mermaid/HTML/Comic → delegates manim to MathAnimatorViewer) |
| `components/quiz/QuizViewer.tsx` | Quiz question cards renderer |
| `components/research/ResearchOutlineEditor.tsx` | Research outline editor |
| `components/common/AssistantResponse.tsx` | Default markdown/text renderer (with thinking segments) |
| `components/Mermaid.tsx` | Mermaid diagram renderer |
| `components/Geogebra.tsx` | Interactive GeoGebra widget |
| `components/chat/home/CapabilityConfigCard.tsx` | Config card wrapper for capability settings forms |
| `components/visualize/visualize/VisualizeConfigPanel.tsx` | Visualize config form |
| `components/quiz/QuizConfigPanel.tsx` | Quiz config form |
| `components/research/ResearchConfigPanel.tsx` | Research config form |
| `lib/unified-ws.ts` | WebSocket client (connect, heartbeat, reconnect, resume) |
| `lib/stream.ts` | Event content accumulation + narration filtering |
| `lib/math-animator-types.ts` | MathAnimatorResult type + extractor |
| `lib/visualize-types.ts` | VisualizeResult type + extractor (delegates to math-animator-types for manim path) |
| `lib/iframe-html.ts` | HTML iframe preparation (KaTeX inject, sanitize, postMessage bridge) |
| `lib/quiz-types.ts` | QuizQuestion type + extractors |
| `lib/playground-config.ts` | Capability playground configuration persistence |
| `context/UnifiedChatContext.tsx` | State management + WebSocket event → message pipeline |
| `context/GeogebraTabContext.tsx` | GeoGebra tab opening bridge |
| `components/chat/home/SessionViewerPanel.tsx` | Side viewer panel (attachment previews, web embeds, GeoGebra tabs) |
| `components/visualize/svg-theme.css` | SVG color ramp classes for light/dark/glass/snow themes |

*Novo passo iniciado*

---

*14 messages | 96 parts | 💰 $0.0152 | ⏱️ 0h01m25s*
