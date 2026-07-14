---
title: "hidden-cabin"
slug: "hidden-cabin"
date: "2026-07-12"
origem: opencode
projeto_slug: ai-stem-tutor
---
---
slug: hidden-cabin
title: "Research comic/visual tools (@general subagent)"
date: 2026-06-17
agent: general
model: deepseek-v4-flash
project: "AI STEM Tutor"
branch: ""
duration: 0h01m02s
messages: 5
parts: 17
cost: 0.006614
tokens_input: 37119
tokens_output: 4106
tokens_reasoning: 228
tokens_cache_read: 72704
tokens_cache_write: 0
created: "2026-06-17 01:39:11 UTC"
updated: "2026-06-17 01:40:13 UTC"
---

SessÃ£o com **5 messages**, **17 parts**, agente **general**, modelo **deepseek-v4-flash** | ðŸ’° $0.0066 | ðŸ’¾ cache read: 72.7K | â±ï¸ 0h01m02s

## ðŸ‘¤ UsuÃ¡rio (2026-06-17 01:39:11 UTC)

Do a comprehensive web search on the following topics. Return ALL findings in a structured format.

## Topic 1: Text-to-Comic generation tools
Search for:
- Open source tools that convert text/stories into comic strips automatically (e.g., ComicGen, Text2Comic, Story-to-Comic)
- APIs or libraries for generating comic panels from text descriptions
- Research projects about automatic comic generation from educational content
- Any GitHub repos related to "text-to-comic", "comic-generation", "storyboard-generator"

## Topic 2: Comic-based learning in STEM/Engineering Education
Search for:
- Tools specifically for creating educational comics for STEM (Pixton, Storyboard That, MakeBeliefsComix, etc.)
- Papers or articles about "comic-based learning" in electrical engineering or physics
- "Educational comics" generators that are automated (not manual drag-and-drop)
- Any LMS or platform that integrates comic generation

## Topic 3: Stable Diffusion for comic generation
Search for:
- Stable Diffusion models fine-tuned for comic/manga style generation
- Workflows/tools that use SD to create multi-panel comics
- ComfyUI workflows for comic generation
- "Comicgen" or "ComicDiffusion" or similar SD models

Return everything you find organized by topic, with URLs and brief descriptions.

## ðŸ¤– Assistente (2026-06-17 01:39:11 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

The user wants a comprehensive web search on three topics related to comic generation. Let me search for all three topics in parallel using the Composio web search tool (via COMPOSIO_SEARCH_TOOLS for web search capability). Actually, let me use webfetch or the Composio tools for this.

Let me start by using COMPOSIO_SEARCH_TOOLS to find web search tools, and also do some direct searches.

Actually, I have a `webfetch` tool but no general web search tool directly. Let me check what tools Composio offers for web search.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:39:19 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Good, I have the Composio web search tools available. Let me now run multiple searches in parallel to cover all three topics comprehensively.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:39:33 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

I now have a comprehensive set of results. Let me also do a couple more targeted searches to fill in gaps, particularly for ComicDiffusion and specific SD models, as well as for the educational comics research papers.

Let me process what I have and also search for a few more specific topics.

</details>

*Novo passo iniciado*

## ðŸ¤– Assistente (2026-06-17 01:39:42 UTC) â€” RaciocÃ­nio

<details open>
<summary>ðŸ§  RaciocÃ­nio #1</summary>

Now I have comprehensive results across all three topics. Let me compile everything into a well-structured markdown response organized by topic.

</details>

### Resposta

---

# Comprehensive Web Search Results: Text-to-Comic Generation & Comic-Based Learning

## Topic 1: Text-to-Comic Generation Tools (Open Source & Research)

### GitHub Repositories â€” Full-Pipeline Tools

| Tool | URL | Description |
|---|---|---|
| **Prompt-to-Comic** | https://github.com/mettafore/prompt-to-comic | LangGraph + GPT-4o + DALLÂ·E; FastAPI backend; POST `/generate` with text, style, panel count params |
| **ComicForge** | https://github.com/snonux/comicforge | CLI-based; uses Gemini to generate story assets, panels, PDFs; manual prompt mode + style presets |
| **ComicGen** (jmilinovich) | https://github.com/jmilinovich/comicgen | Uses Google Gemini for multi-page comics with character consistency; CLI for projects, character sheets, PDF output |
| **MythGen** | https://github.com/elder-plinius/MythGen | Open-source Gradio-based iterative generator; lets you select panels/captions for sequential storyboards |
| **AI Comic Studio** | https://github.com/tosif121/ai-comic-studio | Web app; Gemini Flash + ElevenLabs for voice-narrated multi-panel comics in <1 minute |
| **Comic-Creator** | https://github.com/Khushal05220/Comic-Creator | Google Gemini-powered; consistent multi-panel comics |
| **ChooseFrame** | https://github.com/MasteraSnackin/ChooseFrame | Interactive generator using Claude + Runware SDXL |
| **ComicGenius Pro** | https://github.com/Srinivas26k/ComicGenius-Pro | Gemini 2.5 Flash based; character consistency, speech bubbles, voice narration |
| **Gio-Comic** | https://github.com/giolaq/gio-comic | Strands Agent framework + Gemini; panel-level control, text overlays, full-page composition |
| **Comicly** | https://github.com/Reghunaath/comicly | Next.js web platform; supervised workflow with manual review/regeneration before export |
| **AI Comic Generator** | https://github.com/liuestc/ai-comic-generator | "Director" + "Critic" multi-agent system; iteratively refines scripts before image generation |
| **AIComicBuilder** | https://github.com/LingyiChen-AI/AIComicBuilder | TypeScript-based; converts scripts into animated comics |
| **Comic-Crafter-AI** | https://github.com/GizzZmo/Comic-Crafter-AI | Another Gemini-powered comic generation tool |
| **OpusNana Comic Hank** | https://github.com/SouthBridgeAI/opusnana-comic-hank | Uses Gemini Nano Banana variant for comic generation |
| **Comicgan** (research) | https://github.com/YashPat22/16824_VLR_ComicGen | Research project (few-shot fine-tuning pipeline); txt2img.py + InferencePipeline_ControlNet |
| **LlamaGen** | https://github.com/LlamaGenAI/LlamaGen | REST API for generating comic artwork |
| **gramener/comicgen** | https://github.com/gramener/comicgen/ | Character generator with API for embedding components into websites (static assets, not AI) |

### Academic Papers on Text-to-Comic Generation

| Paper | Year | URL | Summary |
|---|---|---|---|
| **ComicGAN: Text-to-Comic GAN** | 2021 | https://arxiv.org/abs/2109.09120 | First dedicated GAN for text-to-comic generation (B. Proven-Bessel et al., 17 citations) |
| **Automatic comic generation with stylistic multi-page layouts** | 2021 | https://dl.acm.org/doi/abs/10.1145/3440053 | Multi-page layout + emotion-driven text balloons (28 citations) |
| **Comix-Gen AI: Text to Comics Generation** | 2025 | ResearchGate (linked above) | Deep learning models for automated comic creation |
| **AI Comic Strip Generator (NLP + Image Synthesis)** | 2025 | https://www.ijrtmr.com/archiver/archives/ai_comic_strip_generator_... | DALLÂ·E + Streamlit for live comic creation from text prompts |
| **Comic Generation Using AI â€“ A Review** | 2024 | Springer link | Comprehensive review of ML approaches for comic graphics from text |
| **AI-Driven Comic Generation** (thesis) | 2025 | OPUS Rhein-Waal | Transformer-based models for comic scriptwriting + generation |
| **Deep Learning pipeline for Comics Sequences** | 2025 | Springer | Capturing narrative with DL pipeline for comic sequences |
| **Generating coherent comic with ChatGPT + SD** | 2023 | https://ar5iv.labs.arxiv.org/html/2305.11067 | ChatGPT + Stable Diffusion pipeline for coherent multi-panel comics |
| **Comix â€” DL for Educational Comic Creation** | 2025 | https://ieeexplore.ieee.org/abstract/document/11156259/ | Emotion-driven balloon generation, keyframe extraction for educational comics |
| **Comic characters detection using DL** | 2017 | https://ieeexplore.ieee.org/abstract/document/8270235/ | Foundational work on DL for comic character detection (78 citations) |
| **DL text-to-image models for STEM comics** | 2023 | https://library.iated.org/view/RODRIGUEZRUIZ2023CRE | Using AI-Art/deep learning to make STEM disciplines accessible |

### News / Market Landscape
- **Pinecone Moment** â€” new AI app that creates 6-page comic stories (Bleeding Cool, Feb 2026)
- **AI-Generated Comic Book Market** â€” $4.6B market research report 2024-2034F (Yahoo Finance, Jan 2026)
- **Visualizing Research with Gemini 3.0** â€” turning papers into comics (Gonzo ML, Nov 2025)

---

## Topic 2: Comic-Based Learning in STEM/Engineering Education

### Platforms (Manual Drag-and-Drop)

| Platform | URL | Description |
|---|---|---|
| **Pixton** | https://www.pixton.com/ | Research-based; specific STEM packs for Math & Science; ESSA evidence packet; LMS integration via Microsoft AppSource |
| **Pixton Math** | https://www.pixton.com/math | Pre-made content packs aligned to curriculum |
| **Pixton Science** | https://www.pixton.com/science | Science-specific comic creation packs |
| **Storyboard That** | https://www.storyboardthat.com/comic-maker | Free comic maker; pre-made lesson plans for all subjects |

### Automated AI Educational Comic Generators (Not Manual)

| Tool | URL | Description |
|---|---|---|
| **Comistitch â€” AI Educational Comic** | https://comistitch.com/styles/ai-educational-comic/ | Generates STEM comics from plain text; supports labeled diagrams for physics/engineering |
| **Comic AI â€” STEM Creator** | https://comicai.com/create/stem | AI-powered; specific modes for physics, engineering, general STEM |
| **Comic AI â€” Physics** | https://comicai.com/create/physics | Specialized physics comic generation |
| **Comic AI â€” Engineering** | https://comicai.com/create/engineering | Specialized engineering comic generation |
| **StudyGlen** | https://studyglen.com/comics | AI comic generator; turns any topic or PDF into visual stories |
| **EduMate** (GitHub) | https://github.com/pushpenderindia/EduMate | Multi-agent workflow for converting complex curricula into visual formats |
| **Aether-AI** (GitHub) | https://github.com/karthik-2105/Aether-AI | Open-source AI for educational content visualization |
| **LearnByComics** | https://learnbycomics.com/ | Turn any topic into an engaging comic |
| **LifeToon** | https://www.lifetoon.me/ai-comics-for-education | Free AI educational comics maker |
| **Vizcept â€” Circuit Diagram Maker** | https://vizcept.com/tool/circuit-diagram-maker | AI schematic tool; converts text descriptions into IEEE-standard circuit diagrams |

### Research Papers on Comic-Based Learning in STEM

| Paper / Resource | URL | Summary |
|---|---|---|
| **Comic strips for electrical and electronic engineering** | https://www.academia.edu/11067800/ | Novel genre using comics for EEE; helps visualize abstract circuit behaviors |
| **Comics-Based Learning in Science (Literature Review)** | https://ejournal.upsi.edu.my/index.php/JPSMM/article/view/8998 | Systematic review of comics in science education |
| **Learning Using Comics + AI in Physics (Review)** | https://ejournal.upsi.edu.my/index.php/EJSMT/article/view/11044 | Reviews combining comics with AI for physics instruction |
| **Comics in Education (Registered Report)** | https://rr.peercommunityin.org/PCIRegisteredReports/articles/rec?articleId=575 | Large-scale effectiveness study registered at PCI |
| **Concept cartoon in problem-based learning (Systematic Review)** | https://jotse.org/index.php/jotse/article/download/542/370 | Concept cartoons in PBL; systematic literature review |
| **Teaching Programming with Comics: Concept-Language-Procedure Framework** | https://export.arxiv.org/pdf/2306.00464v1.pdf | Cheat sheet / framework for using comics in programming education |
| **Deep learning text-to-image models for STEM** | https://library.iated.org/view/RODRIGUEZRUIZ2023CRE | Using DL text-to-image (including comic style) to make STEM accessible to young generations |

### LMS Integration

| Platform | URL | Description |
|---|---|---|
| **Pixton on Microsoft AppSource** | https://appsource.microsoft.com/en-us/product/web-apps/pixtoncomicsinc1592511863166.pixton | Direct LMS integration; diagnostic, formative, and summative assessment support |
| **vComIQ** | https://uatvcomiq.educationyug.com/ | LMS platform with comic-based assessment tools |
| **Genyo + Animated Comics (Research)** | https://www.jisem-journal.com/index.php/journal/article/view/729 | Integration of animated comics with Genyo LMS for Philippine literature |
| **StudyGlen** | https://studyglen.com/comics | Exports comics for embedding in LMS environments |

---

## Topic 3: Stable Diffusion for Comic/Manga Generation

### Fine-Tuned Models

| Model | URL | Description |
|---|---|---|
| **Comic-Diffusion v2** (ogkalu) | https://huggingface.co/ogkalu/Comic-Diffusion | SD 1.5 fine-tune; DreamBooth; 6 style tokens (charliebo, holliemengert, marioalberti, pepelarraz, andreasrocha, jamesdaly); Diffusers-compatible |
| **Comic-Diffusion v1** | Same HF repo | Trained solely on James Daly (token: `comicmay artsyle`) |
| **Comic-Diffusion ONNX** | https://huggingface.co/TheyCallMeHex/Comic-Diffusion-ONNX | ONNX export for faster inference |
| **Comic-Diffusion (Flax)** | https://huggingface.co/flax/Comic-Diffusion | JAX/Flax weights version |
| **Comic-Diffusion on Civitai** | https://civitai.com/models/13/comic-diffusion | Community hub page with examples & reviews |
| **comics_style_LoRA** | https://huggingface.co/ritwikraha/comics_style_LoRA | LoRA for adding comic style to any SD model |
| **DiffSensei** | https://github.com/jianzongwu/DiffSensei | Multi-modal model for high-resolution controllable manga panel generation (research) |

### ComfyUI Workflows & Nodes for Comic Generation

| Tool/Node | URL | Description |
|---|---|---|
| **comicgeneration** (KummethaYaswanth) | https://github.com/KummethaYaswanth/comicgeneration | End-to-end 6-panel comic workflow; Flux-Kontext model for character consistency; JSON story prompt â†’ auto grid |
| **ComfyUI_sloppy-comic** | https://comfyai.run/custom_node/ComfyUI_sloppy-comic | Custom node for generating comics; includes "Generate Comic" node documentation |
| **Comic_Type Node (StoryDiffusion)** | https://comfyai.run/documentation/Comic_Type | Pass scene prompts + images; layout styles + text overlays |
| **Sketch2Manga** | https://www.runcomfy.com/comfyui-nodes/sketch2manga | ComfyUI extension; applies screentone effects for traditional manga aesthetic |
| **comfyui_panels** | https://github.com/bmad4ever/comfyui_panels | Panel layout building, extraction, and border/outline nodes |
| **comfyui-panelforge** | https://github.com/lisaks/comfyui-panelforge | Panel layout node pack for ComfyUI |
| **ComfyUI-PromptLibrary** | https://github.com/Deaththegrim/ComfyUI-PromptLibrary | "Character Anchor" node for reusing character reference across panels |
| **FlexiComic** | https://github.com/cf-jx/flexicomic | Comic generation workflow for ComfyUI |
| **Manga Editor Desu** | https://github.com/new-sankaku/manga-editor-desu | Browser-based editor that connects to local ComfyUI; panel layout, text, batching |
| **Consistent Character Comic Tutorial** | https://comfyuiblog.com/create-a-consistent-character-comic-with-comfyui-automatically-write-embed-story-text/ | Blog guide: automatic consistent character comics with embedded story text |

### Key Research Papers on SD for Comics

| Paper | URL | Summary |
|---|---|---|
| **Generating coherent comic with ChatGPT and Stable Diffusion** | https://ar5iv.labs.arxiv.org/html/2305.11067 | Uses ChatGPT for script + SD for panels; presents a full pipeline for coherent multi-panel comics |
| **DiffSensei: High-resolution manga panel generation** | https://github.com/jianzongwu/DiffSensei | Multi-modal controllable generation for manga |

---

## Summary of Key Findings

1. **Best automated open-source tools** (LLM + image gen): **ComicForge** (CLI), **Prompt-to-Comic** (API), **MythGen** (Gradio UI), and **ComicGen** (character consistency focus) â€” all use Gemini or GPT-4o + DALLÂ·E / SD.

2. **Educational comic automation**: **Comistitch** and **Comic AI** lead in fully automated STEM comic generation from text. **Pixton** remains the most research-backed platform but is manual drag-and-drop. **Vizcept** is unique for circuit diagrams from text.

3. **SD for comics**: **Comic-Diffusion v2** (HuggingFace) is the primary fine-tuned model. For ComfyUI, the **comicgeneration** repo (Flux-Kontext) and **sloppy-comic** node are the most complete workflows. **DiffSensei** is the leading research model for controllable manga panels.

4. **Research gap**: Most academic work covers *detection/analysis* of existing comics or manual drag-and-drop tools. True end-to-end *generation* from educational text is nascent â€” only a few 2025 papers address automated educational comic creation (Comix 2025, EduMate 2025).

*Novo passo iniciado*

---

*5 messages | 17 parts | ðŸ’° $0.0066 | â±ï¸ 0h01m02s*

