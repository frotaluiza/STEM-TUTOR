---
slug: happy-mountain
title: "Explore chat message flow (@explore subagent)"
date: 2026-06-15
agent: explore
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m34s
messages: 15
parts: 110
cost: 0.016544
tokens_input: 83384
tokens_output: 7315
tokens_reasoning: 1910
tokens_cache_read: 817024
tokens_cache_write: 0
created: "2026-06-15 19:22:35 UTC"
updated: "2026-06-15 19:24:10 UTC"
---

Sessão com **15 messages**, **110 parts**, agente **explore**, modelo **deepseek-v4-flash** | 💰 $0.0165 | 💾 cache read: 817.0K | ⏱️ 0h01m34s

## 👤 Usuário (2026-06-15 19:22:36 UTC)

Very thorough exploration. I need to understand how the DeepTutor chat receives and processes AI responses so I can add text-to-speech to speak the responses aloud.

Project: C:\Users\frota\Documents\Projetos\AI TUTOR\web

Find:

1. In `web/context/UnifiedChatContext.tsx` or similar context/state files - how are streaming responses received? Look for patterns like `onMessage`, `onToken`, `stream`, `appendMessage`, `addMessage` etc.

2. In the page file `web/app/(workspace)/chat/[...sessionId]/page.tsx` - how does `handleSend` work and how does the response get displayed? Look for `sendMessage`, `handleSend`, message state updates.

3. Find where the final AI message/text is added/committed after streaming finishes. This is where I'd hook in TTS.

4. Look for any existing text-to-speech or speech synthesis references in the codebase.

5. Check if there's a message interface/type definition for chat messages (look in `web/lib/` or `web/types/` for Message, ChatMessage, etc.)

6. Find how the WebSocket client works - `web/lib/unified-ws.ts` or similar - to understand the streaming response flow.

Return:
- The exact file path and line numbers where AI response text is committed/displayed
- The message type/interface used
- How the streaming response is processed (callbacks, events, etc.)
- Any existing speech/voice related code

## 🤖 Assistente (2026-06-15 19:22:36 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

The user wants a thorough exploration of the DeepTutor chat codebase to understand how AI responses are received and processed, so they can add text-to-speech functionality. Let me systematically search for all the relevant patterns and files.

Let me start by exploring the project structure and searching for the key patterns simultaneously.

</details>

### Resposta

I'll conduct a thorough exploration of the codebase. Let me start with multiple parallel searches to map out the architecture.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:22:41 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Good. I've found several key files. Let me also search for the message interfaces/types and the page file. Let me explore all the important files now.

</details>

### Resposta

Good. Found the key files. Let me now read them all in parallel, and search for additional patterns.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:22:45 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to read the chat page and the rest of the UnifiedChatContext file. Let me also look for components that display messages and use useChat or similar hooks.

</details>

### Resposta

Let me now read the chat page and the remaining parts of the context file, plus search for how the response is rendered.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:22:50 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to find the ChatMessages component to see how the assistant messages are rendered, and also look at the remaining parts of the chat page. Let me also check the components/chat directory structure and look for the ChatMessages component.

</details>

### Resposta

Let me now find the ChatMessages component and see how assistant messages are rendered, plus check the rest of the chat page.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:22:54 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the ChatMessages.tsx component to see how assistant messages are rendered, and more importantly, to see where the assistant message content gets displayed - that's where I'd hook in TTS.

</details>

### Resposta

Now let me read the ChatMessages component to see how assistant messages are displayed.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:22:57 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I need to find the `AssistantResponse` component, which is the actual component that renders the assistant's text content. That's where TTS would need to hook in. Also, I should check for any existing hooks related to speech.

</details>

### Resposta

Now let me read the `AssistantResponse` component - this is the key rendering component where TTS would hook in.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:02 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me read the AssistantResponse component and the useSmoothStreamText hook - these are the key files for understanding how content is displayed and where TTS would hook in.

</details>

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:05 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now let me check if there are any other speech-related references in the project, and also look for any existing TTS configuration or voice code in the settings or other areas.

</details>

### Resposta

Let me also check for any audio-related code and look at the locales files for TTS references, plus the useChatAutoScroll hook which monitors content changes.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:10 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me now look for any settings pages that reference TTS, and also look at Partners feature which seems to have TTS-related configuration.

</details>

### Resposta

Let me search for TTS settings pages and the Partners feature which seems to have TTS config.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:15 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Let me also check the python backend for TTS references, and look more broadly at the web project for any partner/partner-related features that might have TTS. Also, let me look at the visualization viewer to see how "audio" is used there.

</details>

### Resposta

Let me check a few more references - TTS in the Python backend, and understand the VisualizationViewer audio reference.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:21 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Interesting! I found that the backend's config loader mentions a "narrator" agent for TTS. Let me check that file for more details. Also let me look at the SoulEditor component more closely to see if TTS is part of the partner system.

</details>

### Resposta

Let me check the backend TTS references and the SoulEditor for TTS configuration.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:25 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a comprehensive picture. Let me compile all findings into a clear report.

Summary of findings:

1. **Streaming response flow** (WebSocket → Context → UI):
   - `web/lib/unified-ws.ts`: `UnifiedWSClient` connects to `/api/v1/ws`, receives JSON events via `onmessage`, calls `onEvent(event)` callback (line 217)
   - `web/lib/stream.ts`: `StreamEvent` processing - `shouldAppendEventContent()` determines if a `content` event adds to the visible answer (line 15-27), `isNarrationMarker()` detects narration rounds (line 51-58), `recomputeAnswerContent()` rebuilds answer excluding narration (line 65-75)
   - `web/context/UnifiedChatContext.tsx`: The `UnifiedChatProvider` creates `UnifiedWSClient` with `handleRunnerEvent` callback (line 1140-1143). Events dispatched through reducer: STREAM_START (line 407), STREAM_EVENT (line 439), STREAM_END (line 504). The STREAM_EVENT handler appends content to the last assistant message (line 474-475). STREAM_END sets `isStreaming: false` (line 511).
   - The `handleRunnerEvent` function at line 1000 processes different event types: `session` (bind server session), `session_meta` (title), `done` (stream end), `error` (terminal errors).

2. **Message type/interface** (`MessageItem`):
   - Defined at line 145-155 of `UnifiedChatContext.tsx`:
     ```typescript
     export interface MessageItem {
       id?: number;
       role: "user" | "assistant" | "system";
       content: string;
       capability?: string;
       events?: StreamEvent[];
       attachments?: MessageAttachment[];
       requestSnapshot?: MessageRequestSnapshot;
       parentMessageId?: number | null;
     }
     ```
   - Also `ChatMessageItem` in `ChatMessages.tsx` line 72-81 (very similar, local mirror)
   - `StreamEvent` in `unified-ws.ts` line 33-43
   - `ChatMessage` (outgoing) in `unified-ws.ts` line 138-146

3. **Where AI response text is committed**:
   - In the reducer, STREAM_EVENT (line 439-503): content is appended incrementally
   - `content += action.event.content` (line 475) - for appendable events
   - Or `content = recomputeAnswerContent(events)` (line 473) - when narration markers arrive
   - The message is written into state at line 478-483
   - STREAM_END (line 504-524) just sets `isStreaming: false`, content is already in the message

4. **How the response gets displayed**:
   - `page.tsx` (`handleSend` at line 1294-1399) calls `sendMessage()` from context
   - `ChatMessageList` renders `AssistantMessage` for each assistant role (line 1144-1156)
   - `AssistantMessage` renders `AssistantResponse` component (line 464 for default chat mode)
   - `AssistantResponse` (common/AssistantResponse.tsx) uses `useSmoothStreamText` for smooth reveal, then splits into thinking segments and markdown segments, rendering through `MarkdownRenderer` (or `ModelThinkingCard` for `<think>` blocks)
   - `useSmoothStreamText` (hooks/useSmoothStreamText.ts) provides a typewriter effect using rAF

5. **Existing speech/voice related code**:
   - `types/speech-recognition.d.ts` - TypeScript declarations for Web Speech API (*speech recognition* only, not synthesis!)
   - Locales have TTS-related strings (`"TTS"`, `"TTS Configuration"`, `"TTS Model"`, etc.) - these are likely for the backend TTS configuration in the Partners system
   - Backend `loader.py` mentions "narrator" agent for TTS
   - `markdown-display.ts` includes "audio" as a known HTML element in its safelist
   - Visualization viewer references "audio" in a type
   - SoulEditor has a "how it speaks" placeholder but this is about personality text, not TTS
   - **No existing speech synthesis (speak aloud) code exists in the front-end**

6. **WebSocket client flow**:
   - `UnifiedWSClient` (unified-ws.ts): connects to `/api/v1/ws` (line 187), receives JSON events (line 207), calls `onEvent` handler (line 217)
   - Heartbeat at 30s intervals (line 259-275)
   - Auto-reconnect with exponential backoff (max 5 attempts) (line 286-300)
   - Resume state on reconnect (line 195-200)
   - `send()` method for outgoing messages (line 236-242)
   - Types: `StreamEvent` for incoming, `ChatMessage` union for outgoing

7. **Key line numbers for TTS hook-in**:
   - **WHERE to hook**: `AssistantResponse.tsx` - at line 33, `displayContent` is obtained via `useSmoothStreamText`. After this line, the content is available. The best hook point is after `isStreaming` becomes false (i.e., the message is complete) OR as content streams in.
   - **Alternative hook**: In `UnifiedChatContext.tsx` at the STREAM_END reducer case (line 504-524) - when `isStreaming` is set to false, the final content is available in the message list.
   - **Best approach**: Create a React hook like `useTextToSpeech` that monitors the last assistant message's content changes, and speaks when content changes while streaming OR when streaming completes. Hook into `AssistantResponseImpl` (line 33-37 in AssistantResponse.tsx).

Let me verify the useChatAutoScroll hook to see if there's a good pattern for monitoring content changes.

</details>

### Resposta

Now I have all the data I need. Let me verify one more thing — how the auto-scroll hook monitors content changes, since that pattern could guide TTS integration.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:40 UTC) — Raciocínio

<details open>
<summary>🧠 Raciocínio #1</summary>

Now I have a thorough understanding of the entire streaming flow. Let me compile the comprehensive report.

Key finding: The auto-scroll hook (`useChatAutoScroll`) uses `lastMessageContent` as a dependency (line 86), which means it re-runs its layout effect whenever the content of the last message changes. This is an excellent pattern to follow for TTS integration.

Let me also check if there are any existing TTS configuration settings pages to see if there's a settings UI for TTS that could be reused.

</details>

### Resposta

Let me do one final check for any existing TTS settings or configuration that might exist.

*Novo passo iniciado*

## 🤖 Assistente (2026-06-15 19:23:45 UTC)

Here is the complete, thorough analysis of the DeepTutor chat response flow, with all the locations you need for adding text-to-speech.

---

## 1. Message Type/Interface

**Primary type:** `MessageItem` (in `UnifiedChatContext.tsx`)
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\context\UnifiedChatContext.tsx`
- **Lines 145-155:**
```typescript
export interface MessageItem {
  id?: number;
  role: "user" | "assistant" | "system";
  content: string;           // <-- This is the AI response text
  capability?: string;
  events?: StreamEvent[];
  attachments?: MessageAttachment[];
  requestSnapshot?: MessageRequestSnapshot;
  parentMessageId?: number | null;
}
```

**Stream type:** `StreamEvent` (in `unified-ws.ts`)
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\lib\unified-ws.ts`
- **Lines 33-43:**
```typescript
export interface StreamEvent {
  type: StreamEventType;     // "stage_start" | "stage_end" | "thinking" | ... | "content" | "done" | ...
  source: string;
  stage: string;
  content: string;           // <-- The chunk of text for this event
  metadata: Record<string, unknown>;
  session_id?: string;
  turn_id?: string;
  seq?: number;
  timestamp: number;
}
```

**Local rendering type:** `ChatMessageItem` (in `ChatMessages.tsx`)
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\chat\home\ChatMessages.tsx`
- **Lines 72-81** — mirrors `MessageItem`; used internally by the message list.

---

## 2. How Streaming Responses are Received (WebSocket → Context)

### A. WebSocket Client
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\lib\unified-ws.ts`
- `UnifiedWSClient` connects to `/api/v1/ws` (line 187)
- **Incoming events parsed at line 207:** `const event: StreamEvent = JSON.parse(ev.data);`
- **Callback at line 217:** `this.onEvent(event);` — delivers every incoming event to the handler
- Heartbeat: 30s interval (line 261), dead-connection detection at 45s (line 264)
- Auto-reconnect: exponential backoff, max 5 attempts (lines 286-300)
- Resume: reconnection sends `resume_from` with the last `turn_id` and `seq` (lines 195-200)

### B. Context Provider — Event Handler
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\context\UnifiedChatContext.tsx`
- **`UnifiedWSClient` created at lines 1140-1143** with `handleRunnerEvent` as the callback
- **`handleRunnerEvent` function at lines 1000-1126:**
  - Dispatches `STREAM_EVENT` for most event types (line 1085)
  - Handles `session` events (bind server session, line 1004)
  - Handles `session_meta` (title update, line 1024)
  - Handles `done` event → dispatches `STREAM_END` (line 1044-1083), sets `isStreaming: false`
  - Handles terminal errors with `turn_terminal` flag (line 1086-1123)

### C. Reducer — Where Content is Accumulated
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\context\UnifiedChatContext.tsx`

**`STREAM_START` (lines 407-438):** Creates an empty assistant placeholder message with `content: ""` and `events: []`.

**`STREAM_EVENT` (lines 439-503):** This is where AI response text is **incrementally committed**:
- Line 468-476: The critical content accumulation logic:
  ```typescript
  let content = last?.content || "";
  if (isNarrationMarker(action.event)) {
    content = recomputeAnswerContent(events);   // Rebuilds from scratch
  } else if (shouldAppendEventContent(action.event)) {
    content += action.event.content;            // Appends the new chunk
  }
  ```
- Lines 478-483: The message with accumulated content is written into state:
  ```typescript
  msgs[msgs.length - 1] = {
    ...(last || { role: "assistant", content: "" }),
    content,       // <-- updated with latest accumulated text
    events,
    capability,
  };
  ```

**`STREAM_END` (lines 504-524):** Sets `isStreaming: false` (line 511). Content is already in the message; this just marks the turn complete.

---

## 3. How `handleSend` Works (Page → Context)

- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\app\(workspace)\chat\[[...sessionId]]\page.tsx`
- **`handleSend` at lines 1294-1399:**
  1. Validates input (not empty when no attachments/references) (lines 1296-1306)
  2. Builds capability-specific config (Quiz/Visualize/Research) (lines 1316-1337)
  3. Calls `sendMessage()` from `UnifiedChatContext` at line 1355-1365
  4. Resets attachments and reference selections (lines 1366-1372)

- **`sendMessage` in Context (lines 1347-1533):**
  1. Creates a draft session key if none exists (lines 1367-1371)
  2. Optionally dispatches `ADD_USER_MSG` (line 1469-1477)
  3. Dispatches `STREAM_START` (line 1479) — creates empty assistant bubble
  4. Sends `start_turn` message over WebSocket via `sendThroughRunner` (line 1484-1530)

---

## 4. Where the Final AI Text is Displayed (Context → UI)

### A. ChatMessageList renders each assistant message
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\chat\home\ChatMessages.tsx`
- **Lines 1144-1156:** Each assistant message renders `<AssistantMessage msg={msg} isStreaming={...} />`
- **AssistantMessage component (lines 245-481):**
  - Lines 406-409: Renders `<AssistantResponse content={msg.content} isStreaming={isStreaming} />` for research body
  - Lines 427-431: Same for quiz content
  - **Line 464: The most important line for TTS — default chat mode:**
    ```tsx
    <AssistantResponse content={msg.content} isStreaming={isStreaming} />
    ```
  - Lines 446-451: For inline ask_user segments (text before/after user questions)

### B. AssistantResponse renders the markdown
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\common\AssistantResponse.tsx`
- **Line 33:** `const displayContent = useSmoothStreamText(content, isStreaming);`
- **Line 34-37:** Parses displayContent into thinking segments and markdown segments
- **Lines 64-88:** Renders segments through `ModelThinkingCard` or `MarkdownRenderer`

### C. useSmoothStreamText — Typewriter effect
- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\hooks\useSmoothStreamText.ts`
- While `isStreaming === true`: reveals characters gradually via rAF (lines 100-116)
- When `isStreaming` flips `false`: snaps to full content immediately (lines 74-85)
- Return value `shown` (line 140) is the partially-revealed text

---

## 5. The Stream Processing Helpers

- **File:** `C:\Users\frota\Documents\Projetos\AI TUTOR\web\lib\stream.ts`
- **`shouldAppendEventContent(event)` (lines 15-27):** Determines if a `content` event should be appended to the visible answer (only `content` type events with `call_kind === "llm_final_response"` or `"agent_loop_round"`, or events without a `call_id`)
- **`isNarrationMarker(event)` (lines 51-58):** Detects when a round was "narration" (preamble to a tool call)
- **`recomputeAnswerContent(events)` (lines 65-75):** Rebuilds answer text excluding narration rounds

---

## 6. Existing Speech/Voice Related Code

**Minimal. No front-end speech synthesis exists.** What does exist:

| Location | What |
|---|---|
| `C:\Users\frota\Documents\Projetos\AI TUTOR\web\types\speech-recognition.d.ts` | TypeScript declarations for **Speech Recognition API** (not synthesis) — lines 1-43 |
| `locales/en/app.json:151,174,424,640,651` | Translation strings: `"TTS"`, `"TTS Configuration"`, `"TTS Model"`, `"Script only (TTS not configured)"` — likely for backend Partners system |
| `locales/zh/app.json` | Same strings in Chinese |
| `deeptutor/services/config/loader.py:212` | Backend mentions `"narrator": Narrator agent (independent, for TTS)` |
| `lib/markdown-display.ts:105` | `"audio"` in the HTML element safelist |
| `components/visualize/VisualizationViewer.tsx:209` | `"audio"` in a type union for render formats |

**There is no `speechSynthesis`, `SpeechSynthesisUtterance`, or any Web Speech API synthesis call anywhere in the front-end.**

---

## 7. Best Hook Points for TTS

Based on the architecture, here are the precise locations to add text-to-speech:

### Primary Hook Point (Component Level — Recommended)
**`C:\Users\frota\Documents\Projetos\AI TUTOR\web\components\common\AssistantResponse.tsx`** — **Line 33**

After `useSmoothStreamText` returns the stable `displayContent`, you can create a custom hook `useTextToSpeech` that:
- Watches `displayContent` changing while `isStreaming === true` (reading partial text) OR
- Reads the final content when `isStreaming` transitions from `true` to `false` (reading full response)

This is the cleanest approach because `AssistantResponse` is the single rendering component for all assistant text.

### Alternative Hook Point (Context Level)
**`C:\Users\frota\Documents\Projetos\AI TUTOR\web\context\UnifiedChatContext.tsx`** — **STREAM_END reducer (lines 504-524)**

When `isStreaming` is set to `false`, you can extract the final assistant message from state and pass it to a TTS system. However, this is more complex because you'd need to coordinate with the React component lifecycle.

### The Pattern to Follow
The `useChatAutoScroll` hook at `C:\Users\frota\Documents\Projetos\AI TUTOR\web\hooks\useChatAutoScroll.ts` demonstrates the ideal pattern:
- It receives `lastMessageContent` and `isStreaming` as dependencies (lines 55-56, 86)
- It reacts to content changes and streaming state — **exactly what TTS needs**

A `useTextToSpeech` hook following this pattern would:
1. Accept `content` and `isStreaming` as parameters
2. On content change while streaming: optionally speak partial text
3. On streaming finished: speak the final full text
4. Use `speechSynthesis` API (`SpeechSynthesisUtterance`)

### For live streaming read-aloud, the flow is:
```
WebSocket event → UnifiedChatContext.STREAM_EVENT (content appended at line 475)
  → state.messages updated → AssistantMessage re-renders
    → AssistantResponse re-renders with new content
      → useSmoothStreamText reveals text → displayContent changes
        → **[HERE: TTS hook speaks the new text]**
```

*Novo passo iniciado*

---

*15 messages | 110 parts | 💰 $0.0165 | ⏱️ 0h01m34s*
