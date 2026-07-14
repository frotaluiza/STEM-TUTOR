from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .bkt_model import TutorBKT
from .models import Note
from .notion_sync import sync_note_to_notion
from .storage import NoteStorage

router = APIRouter(prefix="/api/v1/noteblocks/agent", tags=["noteblocks-agent"])

NOTES_DIR = Path("data/noteblocks/notes")
storage = NoteStorage(NOTES_DIR)


class TerminalSuggestRequest(BaseModel):
    prompt: str
    context: str = ""


class TerminalSuggestResponse(BaseModel):
    suggested_command: str
    explanation: str


@router.post("/sync-to-notion/{note_id}")
async def sync_to_notion(note_id: str) -> dict:
    note = storage.load(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    result = await sync_note_to_notion(note_id)
    return result


@router.post("/terminal-suggest")
async def terminal_suggest(req: TerminalSuggestRequest) -> TerminalSuggestResponse:
    prompt_lower = req.prompt.lower()

    if "list" in prompt_lower or "ls" in prompt_lower or "files" in prompt_lower:
        cmd = "Get-ChildItem"
        explanation = "Lista arquivos no diretório atual"
    elif "dir" in prompt_lower or "folder" in prompt_lower or "pwd" in prompt_lower:
        cmd = "Get-Location"
        explanation = "Mostra o diretório atual"
    elif "git status" in prompt_lower or "status" in prompt_lower:
        cmd = "git status"
        explanation = "Mostra o estado do repositório git"
    elif "git log" in prompt_lower or "log" in prompt_lower:
        cmd = "git log --oneline -10"
        explanation = "Mostra os últimos 10 commits"
    elif "npm" in prompt_lower or "node" in prompt_lower or "dev" in prompt_lower:
        cmd = "npm run dev"
        explanation = "Roda o servidor de desenvolvimento"
    elif "test" in prompt_lower or "pytest" in prompt_lower:
        cmd = "cd AI TUTOR && python -m pytest tests/noteblocks/ -v"
        explanation = "Roda os testes do NoteBlocks"
    elif "ruff" in prompt_lower or "lint" in prompt_lower:
        cmd = "cd AI TUTOR && ruff check deeptutor/noteblocks/"
        explanation = "Roda o linter no NoteBlocks"
    elif "clear" in prompt_lower or "cls" in prompt_lower:
        cmd = "Clear-Host"
        explanation = "Limpa o terminal"
    else:
        cmd = req.prompt
        explanation = "Comando sugerido pelo agente"

    return TerminalSuggestResponse(suggested_command=cmd, explanation=explanation)


@router.post("/ask/{note_id}")
async def process_ask(note_id: str, block_id: str, instruction: str = "") -> dict:
    note = storage.load(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    block = next((b for b in note.blocks if b.id == block_id), None)
    if block is None:
        raise HTTPException(status_code=404, detail="Block not found")

    prompt = instruction or block.content
    full_context = _build_context(note)

    response = await _call_llm(full_context, prompt)

    for b in note.blocks:
        if b.id == block_id:
            b.content = response
            b.type = "output"

    storage.save(note)
    return {"block_id": block_id, "content": response}


@router.post("/assist-edit/{note_id}")
async def assist_edit(note_id: str, block_ids: list[str], instruction: str) -> dict:
    note = storage.load(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    selected = [b for b in note.blocks if b.id in block_ids]
    if not selected:
        raise HTTPException(status_code=404, detail="No valid blocks found")

    full_context = _build_context(note)
    selected_text = "\n\n".join(f"[Block {b.id}] {b.content}" for b in selected)

    results = await _call_llm_for_blocks(full_context, selected_text, instruction)

    updated = []
    for b in note.blocks:
        if b.id in results:
            b.content = results[b.id]
            updated.append(b.id)

    storage.save(note)
    return {"updated": updated, "blocks": {bid: results[bid] for bid in updated}}


def _build_context(note: Note) -> str:
    parts = [f"# {note.title}"]
    if note.level:
        parts.append(f"Nivel do aluno: {note.level} ({note.level_topic})")
    for b in note.blocks:
        parts.append(f"[{b.type}] {b.content}")
    return "\n\n".join(parts)


class AskWithOptionsRequest(BaseModel):
    note_id: str
    block_id: str
    instruction: str = ""


class AskWithOptionsResponse(BaseModel):
    question: str
    options: list[dict]
    allow_custom: bool


@router.post("/ask-with-options")
async def ask_with_options(req: AskWithOptionsRequest) -> AskWithOptionsResponse:
    note = storage.load(req.note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    block = next((b for b in note.blocks if b.id == req.block_id), None)
    if block is None:
        raise HTTPException(status_code=404, detail="Block not found")

    prompt = req.instruction or block.content
    prompt_lower = prompt.lower()

    options = [
        {"id": "a", "label": "Sim, entendi o conceito"},
        {"id": "b", "label": "Preciso de mais exemplos"},
        {"id": "c", "label": "Nao entendi, pode explicar de outra forma?"},
    ]
    allow_custom = True

    if "p-value" in prompt_lower or "significancia" in prompt_lower or "estatistic" in prompt_lower:
        options = [
            {"id": "a", "label": "Probabilidade de a hipotese nula ser verdadeira"},
            {
                "id": "b",
                "label": "Probabilidade de rejeitar a hipotese nula dado que ela eh verdadeira (Erro Tipo I)",
            },
            {"id": "c", "label": "Nivel de confianca do teste"},
            {"id": "d", "label": "Nao tenho certeza"},
        ]
    elif "derivada" in prompt_lower or "calculo" in prompt_lower or "integral" in prompt_lower:
        options = [
            {"id": "a", "label": "Taxa de variacao instantanea"},
            {"id": "b", "label": "Area sob a curva"},
            {"id": "c", "label": "Inclinacao da reta tangente"},
            {"id": "d", "label": "Nao sei"},
        ]
    elif "circuito" in prompt_lower or "resistencia" in prompt_lower or "ohm" in prompt_lower:
        options = [
            {"id": "a", "label": "V = R / I"},
            {"id": "b", "label": "V = I * R"},
            {"id": "c", "label": "V = I + R"},
            {"id": "d", "label": "Nao lembro"},
        ]

    return AskWithOptionsResponse(
        question=prompt,
        options=options,
        allow_custom=allow_custom,
    )


class AnswerRequest(BaseModel):
    note_id: str
    block_id: str
    answer: str
    selected_option: str = ""


@router.post("/answer")
async def process_answer(req: AnswerRequest) -> dict:
    note = storage.load(req.note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    for b in note.blocks:
        if b.id == req.block_id:
            b.content = f"Resposta: {req.answer}"
            b.type = "output"

    storage.save(note)
    return {
        "block_id": req.block_id,
        "answer": req.answer,
        "next": "follow-up",
    }


class LevelingStartResponse(BaseModel):
    question: str
    options: list[dict]


@router.get("/leveling/start")
async def leveling_start(topic: str = "") -> LevelingStartResponse:
    base_topic = topic.strip() or "este assunto"
    return LevelingStartResponse(
        question=f"Qual seu nivel em {base_topic}?",
        options=[
            {"id": "iniciante", "label": f"Iniciante - nunca vi {base_topic}"},
            {"id": "basico", "label": f"Basico - ja ouvi falar sobre {base_topic}"},
            {"id": "intermediario", "label": f"Intermediario - ja estudei {base_topic} antes"},
            {"id": "avancado", "label": f"Avançado - domino {base_topic}"},
        ],
    )


class LevelingAnswerRequest(BaseModel):
    note_id: str
    level: str
    topic: str = ""


@router.post("/leveling/answer")
async def leveling_answer(req: LevelingAnswerRequest) -> dict:
    note = storage.load(req.note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    note.level = req.level
    note.level_topic = req.topic
    storage.save(note)

    level_prompts = {
        "iniciante": "Vou explicar desde o comeco, com analogias simples e exemplos do dia a dia.",
        "basico": "Vou revisar os conceitos fundamentais e avancar gradualmente.",
        "intermediario": "Vou focar em aprofundamento e aplicacoes praticas.",
        "avancado": "Vou direto para problemas avancados e topicos complexos.",
    }
    prompt = level_prompts.get(req.level, "Vou ajustar o nivel conforme sua resposta.")

    return {
        "level": req.level,
        "prompt": prompt,
        "message": f"Nivel definido como {req.level}. {prompt}",
    }


async def _call_llm(context: str, prompt: str) -> str:
    return (
        f"[Agent response to: {prompt}]\n\n"
        f"Context analyzed. This is a placeholder response. "
        f"The full LLM integration will replace this."
    )


async def _call_llm_for_blocks(
    context: str, selected_text: str, instruction: str
) -> dict[str, str]:
    placeholder = f"[Edited based on: {instruction}]\n(LLM integration pending)"
    blocks: dict[str, str] = {}
    for line in selected_text.split("\n\n"):
        if line.startswith("[Block ") and "] " in line:
            bid = line.split("[Block ")[1].split("]")[0]
            blocks[bid] = placeholder
    return blocks


class BktRecordRequest(BaseModel):
    student_id: str
    skill: str
    correct: bool


class BktStatusRequest(BaseModel):
    student_id: str


_bkt_instances: dict[str, TutorBKT] = {}


def _get_bkt(student_id: str) -> TutorBKT:
    if student_id not in _bkt_instances:
        _bkt_instances[student_id] = TutorBKT(student_id)
    return _bkt_instances[student_id]


@router.post("/bkt/record")
async def bkt_record(req: BktRecordRequest) -> dict:
    bkt = _get_bkt(req.student_id)
    result = bkt.record_answer(req.skill, req.correct)
    return result


@router.post("/bkt/status")
async def bkt_status(req: BktStatusRequest) -> dict:
    bkt = _get_bkt(req.student_id)
    return {
        "student_id": req.student_id,
        "mastery": bkt.get_all_mastery(),
        "weak_skills": bkt.get_weak_skills(),
    }
