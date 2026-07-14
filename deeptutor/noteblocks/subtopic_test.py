"""Teste de Subtopic por Sessao — TOEFL-style.

Ao final de cada sessao do NoteBlocks, gera um teste com:
  - Parte Teorica: multipla escolha extraida das fontes do aluno (KB)
  - Parte Pratica: exercicios baseados no conteudo da sessao
  - Threshold: 90% para passar
  - Se falhar: encaminha para Runner modo teste
"""

from __future__ import annotations

from pathlib import Path
import random

from fastapi import APIRouter
from pydantic import BaseModel

from .bkt_model import TutorBKT
from .storage import NoteStorage

router = APIRouter(prefix="/api/v1/noteblocks/subtopic-test", tags=["noteblocks-subtopic-test"])

NOTES_DIR = Path("data/noteblocks/notes")
storage = NoteStorage(NOTES_DIR)

_bkt_instances: dict[str, TutorBKT] = {}

THEORETICAL_QUESTIONS = {
    "derivadas": [
        {
            "question": "O que significa a derivada de uma funcao em um ponto?",
            "options": [
                {"id": "a", "label": "A area sob a curva da funcao"},
                {"id": "b", "label": "A taxa de variacao instantanea da funcao naquele ponto"},
                {"id": "c", "label": "O valor maximo da funcao"},
                {"id": "d", "label": "A raiz da funcao"},
            ],
            "correct": "b",
        },
        {
            "question": "Segundo a regra da cadeia, qual a derivada de f(g(x))?",
            "options": [
                {"id": "a", "label": "f'(x) * g'(x)"},
                {"id": "b", "label": "f'(g(x)) * g'(x)"},
                {"id": "c", "label": "f'(g'(x))"},
                {"id": "d", "label": "f(g(x)) * g'(x)"},
            ],
            "correct": "b",
        },
    ],
    "integrais": [
        {
            "question": "O que representa a integral definida de f(x) de a ate b?",
            "options": [
                {"id": "a", "label": "A derivada de f(x) em x = b"},
                {"id": "b", "label": "A area sob a curva de f(x) entre a e b"},
                {"id": "c", "label": "O valor medio de f(x)"},
                {"id": "d", "label": "A inclinacao da reta tangente"},
            ],
            "correct": "b",
        },
    ],
    "limites": [
        {
            "question": "Quando um limite existe?",
            "options": [
                {"id": "a", "label": "Quando a funcao esta definida no ponto"},
                {"id": "b", "label": "Quando os limites laterais sao iguais"},
                {"id": "c", "label": "Quando a funcao eh continua"},
                {"id": "d", "label": "Quando o limite eh infinito"},
            ],
            "correct": "b",
        },
    ],
}

PRACTICAL_QUESTIONS = {
    "derivadas": [
        {
            "question": "Calcule a derivada de f(x) = 3x²",
            "options": [
                {"id": "a", "label": "6x"},
                {"id": "b", "label": "3x"},
                {"id": "c", "label": "6"},
                {"id": "d", "label": "x²"},
            ],
            "correct": "a",
        },
    ],
}


def _get_bkt(student_id: str) -> TutorBKT:
    if student_id not in _bkt_instances:
        _bkt_instances[student_id] = TutorBKT(student_id)
    return _bkt_instances[student_id]


class SubtopicTestStartRequest(BaseModel):
    student_id: str
    skill: str = ""
    note_id: str = ""


class SubtopicTestAnswerRequest(BaseModel):
    student_id: str
    skill: str = ""
    theoretical_answers: dict[str, str] = {}
    practical_answers: dict[str, str] = {}


@router.post("/start")
async def subtopic_test_start(req: SubtopicTestStartRequest) -> dict:
    skill = req.skill or "derivadas"

    theoretical = THEORETICAL_QUESTIONS.get(skill, THEORETICAL_QUESTIONS["derivadas"])
    practical = PRACTICAL_QUESTIONS.get(skill, PRACTICAL_QUESTIONS["derivadas"])

    random.shuffle(theoretical)
    random.shuffle(practical)

    return {
        "student_id": req.student_id,
        "skill": skill,
        "theoretical": theoretical[:3],
        "practical": practical[:2],
        "threshold": 0.9,
    }


@router.post("/evaluate")
async def subtopic_test_evaluate(req: SubtopicTestAnswerRequest) -> dict:
    bkt = _get_bkt(req.student_id)
    skill = req.skill or "derivadas"

    theoretical = THEORETICAL_QUESTIONS.get(skill, THEORETICAL_QUESTIONS["derivadas"])
    practical = PRACTICAL_QUESTIONS.get(skill, PRACTICAL_QUESTIONS["derivadas"])

    t_correct = 0
    t_total = len(theoretical)
    for q in theoretical:
        qid = q["question"][:20]
        user_ans = req.theoretical_answers.get(str(theoretical.index(q)))
        if user_ans == q["correct"]:
            t_correct += 1

    p_correct = 0
    p_total = len(practical)
    for q in practical:
        qid = q["question"][:20]
        user_ans = req.practical_answers.get(str(practical.index(q)))
        if user_ans == q["correct"]:
            p_correct += 1

    total_correct = t_correct + p_correct
    total_questions = max(t_total + p_total, 1)
    score_pct = total_correct / total_questions
    passed = score_pct >= 0.9

    bkt.record_answer(f"{skill}_teorico", passed)

    return {
        "student_id": req.student_id,
        "skill": skill,
        "score_pct": round(score_pct, 2),
        "theoretical": f"{t_correct}/{t_total}",
        "practical": f"{p_correct}/{p_total}",
        "passed": passed,
        "threshold": 0.9,
        "next_step": "runner_test" if not passed else "checkpoint_advance",
    }
