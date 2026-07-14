---
title: "witty-planet"
slug: "witty-planet"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: witty-planet
title: "Research DeepSeek embedding models (@general subagent)"
date: 2026-06-17
agent: general
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h00m30s
messages: 5
parts: 17
cost: 0.004979
tokens_input: 30632
tokens_output: 1216
tokens_reasoning: 606
tokens_cache_read: 64256
tokens_cache_write: 0
created: "2026-06-17 02:51:22 UTC"
updated: "2026-06-17 02:51:53 UTC"
---

SessÃ£o com **5 messages**, **17 parts**, agente **general**, modelo **deepseek-v4-flash** | ðŸ’° $0.0050 | ðŸ’¾ cache read: 64.3K | â±ï¸ 0h00m30s

## ðŸ‘¤ UsuÃ¡rio (2026-06-17 02:51:22 UTC)

Search the web for information about DeepSeek's embedding/RAG models. I need to know:

1. Does DeepSeek offer an embedding model API? (like "deepseek-embedding")
2. What is the API endpoint URL for DeepSeek embeddings?
3. What are the model names available?
4. What is the embedding dimension?
5. Is it compatible with OpenAI's embedding API format?
6. Any pricing information
7. Does it work with the same API key as their chat models?

Also check if DeepSeek has any specific RAG-related offerings or documentation about using their models for retrieval.

Search for: "deepseek embedding model", "deepseek-embedding", "deepseek RAG", "deepseek api embeddings"

## ðŸ¤– Assistente (2026-06-17 02:51:22 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants me to search the web for information about DeepSeek's embedding/RAG models. Let me search for this information using the web search tools available to me.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:51:27 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Good, I have the COMPOSIO_SEARCH_WEB tool available (no auth needed). Let me search the web for all these questions. I'll do multiple searches in parallel to get comprehensive results.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:51:37 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Let me also fetch the official DeepSeek API documentation to get authoritative answers. The search results are conflicting - some say DeepSeek does NOT offer an embeddings API, while others reference one. Let me check the official docs directly.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 02:51:43 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The official DeepSeek API documentation and the GitHub issue provide authoritative answers. Let me compile the information:

1. **Does DeepSeek offer an embedding model API?** â€” **No.** The official DeepSeek API docs only list chat completions (deepseek-v4-flash, deepseek-v4-pro). The GitHub issue (#802) requesting an embedding-aware API was closed as "not_planned". Multiple sources confirm DeepSeek does NOT provide a native embeddings API.

2. **API endpoint URL** â€” The base URL for the OpenAI-format API is `https://api.deepseek.com`, but there is NO `/v1/embeddings` endpoint. There's also an Anthropic format at `https://api.deepseek.com/anthropic`.

3. **Model names available** â€” Only chat/reasoning models: `deepseek-v4-flash` (also `deepseek-chat` and `deepseek-reasoner` - to be deprecated), `deepseek-v4-pro`. No embedding models.

4. **Embedding dimension** â€” N/A (no embedding API). Some third-party articles mention 1536 or 768 dimensions, but these are not official.

5. **OpenAI compatible format?** â€” The chat completion API is OpenAI-compatible (base_url: `https://api.deepseek.com`, uses OpenAI SDK), but there's no embedding endpoint.

6. **Pricing** â€” Only for chat models: 
   - deepseek-v4-flash: $0.0028/M tokens (cache hit), $0.14/M (cache miss) input, $0.28/M output
   - deepseek-v4-pro: $0.003625/M tokens (cache hit), $0.435/M (cache miss) input, $0.87/M output

7. **Same API key?** â€” Yes, the same API key works for all DeepSeek API services. But there's no embedding service.

8. **RAG-related offerings** â€” DeepSeek has no specific RAG offerings. For RAG with DeepSeek, you use DeepSeek's chat models for generation and a separate embedding model (from Sentence Transformers, BGE, GTE-Qwen2, etc.) for retrieval/vectorization. Various tutorials show this pattern.

Let me present this clearly.

</details>

### Resposta

Here are the findings from official DeepSeek docs and authoritative sources:

**1. Embedding model API â€” No.** DeepSeek does **not** offer a native embedding/vectorization API. A GitHub issue requesting it ([#802](https://github.com/deepseek-ai/DeepSeek-R1/issues/802)) was closed as `not_planned`.

**2. API endpoint â€”** `https://api.deepseek.com` (OpenAI-format chat). There is **no** `/v1/embeddings` endpoint.

**3. Available models (chat-only):**
- `deepseek-v4-flash` (also aliased as `deepseek-chat` / `deepseek-reasoner` â€” deprecated 2026/07/24)
- `deepseek-v4-pro`

**4. Embedding dimension â€”** N/A. No embedding API exists.

**5. OpenAI format compatibility â€”** The chat API uses OpenAI-compatible SDK (`base_url="https://api.deepseek.com"`), but this format does not extend to embeddings since no such endpoint exists.

**6. Pricing (chat models only, per 1M tokens):**
| Model | Input (cache hit) | Input (cache miss) | Output |
|---|---|---|---|
| v4-flash | $0.0028 | $0.14 | $0.28 |
| v4-pro | $0.003625 | $0.435 | $0.87 |

**7. Same API key â€”** Yes, a single API key works for all DeepSeek API services.

**8. RAG â€”** DeepSeek has no dedicated RAG infrastructure. The standard pattern is: use a **separate embedding model** (BGE, GTE-Qwen2, Sentence Transformers) for vectorization, store in a vector DB (FAISS, Chroma, OpenSearch), then use DeepSeek's chat models for generation with retrieved context.

*Novo passo iniciado*

---

*5 messages | 17 parts | ðŸ’° $0.0050 | â±ï¸ 0h00m30s*

