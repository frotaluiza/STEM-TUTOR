from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

try:
    from pyBKT.models import Model as BKTModel

    _HAS_PYBKT = True
except ImportError:
    _HAS_PYBKT = False

BKT_STATE_DIR = Path("data/noteblocks/bkt")
BKT_STATE_DIR.mkdir(parents=True, exist_ok=True)


class TutorBKT:
    def __init__(self, student_id: str) -> None:
        self.student_id = student_id
        self._state_path = BKT_STATE_DIR / f"{student_id}.json"
        self._model = BKTModel(seed=42, num_fits=1) if _HAS_PYBKT else None
        self._skills: dict[str, dict[str, float]] = {}
        self._load()

    def _load(self) -> None:
        if self._state_path.exists():
            raw = self._state_path.read_text(encoding="utf-8")
            data = json.loads(raw)
            self._skills = data.get("skills", {})

    def _save(self) -> None:
        self._state_path.write_text(
            json.dumps({"student_id": self.student_id, "skills": self._skills}, indent=2),
            encoding="utf-8",
        )

    def record_answer(self, skill: str, correct: bool) -> dict[str, Any]:
        if skill not in self._skills:
            self._skills[skill] = {
                "prior": 0.3,
                "learns": 0.2,
                "guesses": 0.15,
                "slips": 0.1,
                "responses": [],
                "mastery": 0.3,
            }

        skill_data = self._skills[skill]
        skill_data["responses"].append(1 if correct else 0)

        df = pd.DataFrame(
            {
                "user_id": [self.student_id] * len(skill_data["responses"]),
                "skill_name": [skill] * len(skill_data["responses"]),
                "correct": skill_data["responses"],
            }
        )

        if _HAS_PYBKT and self._model is not None:
            try:
                self._model.fit(data=df, skills=skill)
                params = self._model.params()
                if skill in params:
                    p = params[skill]
                    skill_data["prior"] = float(p.get("prior", skill_data["prior"]))
                    skill_data["learns"] = float(p.get("learns", [skill_data["learns"]])[0])
                    skill_data["guesses"] = float(p.get("guesses", [skill_data["guesses"]])[0])
                    skill_data["slips"] = float(p.get("slips", [skill_data["slips"]])[0])

                preds = self._model.predict(data=df)
                if not preds.empty:
                    latest = preds.iloc[-1]
                    skill_data["mastery"] = float(
                        latest.get(
                            "correct_predictions", latest.get("state", skill_data["mastery"])
                        )
                    )
            except Exception:
                skill_data["mastery"] = self._fallback_mastery(skill_data)
        else:
            skill_data["mastery"] = self._fallback_mastery(skill_data)

        self._save()
        return {
            "skill": skill,
            "correct": correct,
            "mastery": round(skill_data["mastery"], 3),
            "total_attempts": len(skill_data["responses"]),
        }

    def _fallback_mastery(self, skill_data: dict) -> float:
        n_correct = sum(skill_data["responses"])
        n_total = len(skill_data["responses"])
        return n_correct / max(n_total, 1)

    def get_mastery(self, skill: str) -> float:
        if skill in self._skills:
            return self._skills[skill]["mastery"]
        return 0.3

    def get_all_mastery(self) -> dict[str, float]:
        return {s: d["mastery"] for s, d in self._skills.items()}

    def get_weak_skills(self, threshold: float = 0.6) -> list[str]:
        return [s for s, m in self.get_all_mastery().items() if m < threshold]
