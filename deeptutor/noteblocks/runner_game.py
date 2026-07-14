"""Runner do Conhecimento — Backend.

Gerencia:
- Frases para o runner (ordenadas por escada logica)
- Vidas e threshold 90%
- Barra de esperanca do professor
- Adaptacao pos-erro (frases mudam apos colisao)
- Re-teste sem ajuda (frases ja dominadas sem hint)
"""

from __future__ import annotations

from pathlib import Path
import random

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .bkt_model import TutorBKT
from .dialogue_engine import DialogueState
from .storage import NoteStorage

router = APIRouter(prefix="/api/v1/noteblocks/runner", tags=["noteblocks-runner"])

NOTES_DIR = Path("data/noteblocks/notes")
storage = NoteStorage(NOTES_DIR)

_bkt_instances: dict[str, TutorBKT] = {}
_runner_sessions: dict[str, dict] = {}


def _get_bkt(student_id: str) -> TutorBKT:
    if student_id not in _bkt_instances:
        _bkt_instances[student_id] = TutorBKT(student_id)
    return _bkt_instances[student_id]


SAMPLE_PHRASES = {
    "derivadas": [
        ("Derivada mede taxa de variacao instantanea", "important"),
        ("A notacao dy/dx foi introduzida por Leibniz", "source"),
        ("Se f'(x) > 0 a funcao eh crescente", "remember"),
        ("A derivada de x^n eh n * x^(n-1)", "weak"),
        ("Regra da cadeia: d/dx f(g(x)) = f'(g(x)) * g'(x)", "weak"),
        ("Derivada de sen(x) = cos(x)", "mastered"),
        ("Derivada de cos(x) = -sen(x)", "mastered"),
        ("A derivada representa a inclinacao da reta tangente", "important"),
    ],
    "integrais": [
        ("Integral definida calcula area sob a curva", "important"),
        ("Integral indefinida eh a antiderivada", "remember"),
        ("Teorema Fundamental do Calculo liga derivada e integral", "weak"),
        ("Integral de x^n dx = x^(n+1)/(n+1) + C", "weak"),
        ("Integral de 1/x dx = ln|x| + C", "source"),
    ],
    "limites": [
        ("Limite eh o valor que a funcao se aproxima", "important"),
        ("Se os limites laterais sao iguais o limite existe", "mastered"),
        ("Limite de 1/x quando x tende ao infinito eh 0", "remember"),
        ("Limites fundamentais: sen(x)/x = 1 quando x tende a 0", "weak"),
    ],
}

FLAG_COLORS = {
    "important": "blue",
    "remember": "orange",
    "weak": "red",
    "mastered": "green",
    "source": "gray",
}


class RunnerStartRequest(BaseModel):
    student_id: str
    skill: str = ""
    mode: str = "recreational"  # recreational | test


class RunnerAnswerRequest(BaseModel):
    session_id: str
    phrase_index: int
    correct: bool


@router.post("/start")
async def runner_start(req: RunnerStartRequest) -> dict:
    bkt = _get_bkt(req.student_id)

    phrases_pool = SAMPLE_PHRASES.get(req.skill, [])
    if not phrases_pool:
        for skill_phrases in SAMPLE_PHRASES.values():
            phrases_pool.extend(skill_phrases)

    weak_skills = bkt.get_weak_skills()
    weak_phrases: list[tuple[str, str]] = []
    for ws in weak_skills:
        weak_phrases.extend(SAMPLE_PHRASES.get(ws, []))

    weak_phrases = weak_phrases[:5] or phrases_pool[:5]

    random.shuffle(phrases_pool)
    random.shuffle(weak_phrases)

    final_phrases = phrases_pool[:8]
    for i, wp in enumerate(weak_phrases[:3]):
        final_phrases.insert(i, wp)

    session_id = f"run_{req.student_id}_{hash(str(final_phrases)) % 10000}"
    _runner_sessions[session_id] = {
        "student_id": req.student_id,
        "skill": req.skill,
        "mode": req.mode,
        "phrases": final_phrases,
        "current_index": 0,
        "lives": 3 if req.mode == "test" else 999,
        "correct_count": 0,
        "total_answered": 0,
        "hope_bar": 0.0,
        "professor_animation": "neutral",
        "dialogue_state": DialogueState(req.student_id, req.skill).get_context(),
    }

    session = _runner_sessions[session_id]
    phrase_list = [
        {"text": p[0], "color": FLAG_COLORS.get(p[1], "gray"), "flag": p[1]} for p in final_phrases
    ]
    return {
        "session_id": session_id,
        "phrases": phrase_list,
        "total_phrases": len(final_phrases),
        "lives": session["lives"],
        "mode": req.mode,
        "weak_skills": weak_skills,
    }


@router.post("/answer")
async def runner_answer(req: RunnerAnswerRequest) -> dict:
    session = _runner_sessions.get(req.session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Runner session not found")

    bkt = _get_bkt(session["student_id"])
    phrase = session["phrases"][req.phrase_index]
    skill = session.get("skill") or "general"

    result = bkt.record_answer(skill, req.correct)
    session["total_answered"] += 1

    phrase_obj = {"skill": skill, "phrase": phrase}

    if req.correct:
        session["correct_count"] += 1
        session["hope_bar"] = min(1.0, session["hope_bar"] + 0.12)
        session["professor_animation"] = "happy"
        session["dialogue_state"] = DialogueState(session["student_id"], skill).get_context()
    else:
        session["lives"] -= 1 if session["mode"] == "test" else 0
        session["hope_bar"] = max(0.0, session["hope_bar"] - 0.25)
        session["professor_animation"] = "sad"
        ds = DialogueState(session["student_id"], skill)
        ds.record_failure()
        session["dialogue_state"] = ds.get_context()

        idx = session["phrases"].index(phrase)
        if idx > 0:
            prereq = session["phrases"][idx - 1]
            session["phrases"].insert(idx + 1, prereq)

    game_over = session["lives"] <= 0 and session["mode"] == "test"
    if not game_over and session["total_answered"] >= len(session["phrases"]):
        game_over = True

    score_pct = session["correct_count"] / max(session["total_answered"], 1)
    passed = score_pct >= 0.9 and session["mode"] == "test"

    return {
        "session_id": req.session_id,
        "phrase_result": "correct" if req.correct else "wrong",
        "mastery": result.get("mastery", 0),
        "lives_remaining": session["lives"],
        "hope_bar": round(session["hope_bar"], 2),
        "professor_animation": session["professor_animation"],
        "score_pct": round(score_pct, 2),
        "game_over": game_over,
        "passed": passed,
        "total_answered": session["total_answered"],
        "total_phrases": len(session["phrases"]),
        "dialogue_move": session["dialogue_state"].get("current_move", "pump"),
        "phrases": session["phrases"] if not req.correct else [],
    }
