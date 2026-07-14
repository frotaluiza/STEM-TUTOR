"""Dialogue Move Engine — Memphis-style Hint -> Pump -> Prompt -> Summary sequence.

Each move type corresponds to a level of scaffolding:
  Level 1 - PUMP:    Most open. "Tell me more about X"
  Level 2 - HINT:    Partial context. "Think about the relationship between..."
  Level 3 - PROMPT:  Specific gap. "What is the value of X when Y=0?"
  Level 4 - ASSERT:  Correction. "Actually, the answer is..."
  Level 5 - SUMMARY: Closure. "Recapping: ..."
"""

from __future__ import annotations

from enum import Enum


class DialogueMove(str, Enum):
    PUMP = "pump"
    HINT = "hint"
    PROMPT = "prompt"
    ASSERT = "assertion"
    SUMMARY = "summary"


MOVE_ORDER = [DialogueMove.PUMP, DialogueMove.HINT, DialogueMove.PROMPT]


class DialogueState:
    def __init__(self, student_id: str, skill: str) -> None:
        self.student_id = student_id
        self.skill = skill
        self.current_move_idx: int = 0
        self.expectation_text: str = ""
        self.consecutive_failures: int = 0
        self.mastered: bool = False

    @property
    def current_move(self) -> DialogueMove | None:
        if self.current_move_idx < len(MOVE_ORDER):
            return MOVE_ORDER[self.current_move_idx]
        return None

    def advance(self) -> None:
        if self.current_move_idx < len(MOVE_ORDER):
            self.current_move_idx += 1

    def reset_to_pump(self) -> None:
        self.current_move_idx = 0
        self.consecutive_failures = 0

    def record_failure(self) -> None:
        self.consecutive_failures += 1
        if self.consecutive_failures >= 3:
            self.reset_to_pump()

    def record_success(self) -> None:
        self.consecutive_failures = 0
        if self.current_move_idx < len(MOVE_ORDER):
            self.advance()
        else:
            self.mastered = True

    def generate_move_text(self, expectation: str) -> str:
        move = self.current_move
        if move is None:
            return f"Summary: {expectation}"

        prompts = {
            DialogueMove.PUMP: f"Me fale mais sobre: {expectation}",
            DialogueMove.HINT: f"Pense: {expectation} (dica: relacione com o que ja vimos)",
            DialogueMove.PROMPT: f"Complete: {expectation}",
            DialogueMove.ASSERT: f"Na verdade: {expectation}",
            DialogueMove.SUMMARY: f"Recapitulando: {expectation}",
        }
        return prompts.get(move, expectation)

    def get_context(self) -> dict:
        return {
            "skill": self.skill,
            "current_move": self.current_move.value if self.current_move else "summary",
            "consecutive_failures": self.consecutive_failures,
            "mastered": self.mastered,
        }
