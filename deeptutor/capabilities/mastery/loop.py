"""Mastery path loop-capability hooks — supports two tutor styles.

Tutor styles:
  - "deeptutor" (default): The original DeepTutor chat-loop tutor with its
    built-in didactic strategies (system.md).
  - "memphis": AutoTutor-inspired tutor with explicit EMT dialogue ladder,
    5-Step Tutoring Frame, face-saving, and misconception handling
    (system-memphis.md).
"""

from __future__ import annotations

from importlib import resources
from typing import Any

from deeptutor.capabilities.mastery.tools import MASTERY_TOOL_NAMES
from deeptutor.capabilities.protocol import PromptBlock
from deeptutor.core.context import UnifiedContext


class MasteryLoopCapability:
    """Turn-scoped integration for mastery-path tutoring.

    Reuses the full chat tool surface (rag / read_source / ask_user / … under
    the same user toggles as chat) and adds the mastery engine tools on top.

    The tutor style is selected via ``context.metadata.get("tutor_style")``:
    - ``"deeptutor"`` (default) — original prompt
    - ``"memphis"`` — AutoTutor EMT dialogue prompt
    """

    name = "mastery"
    owned_tools = MASTERY_TOOL_NAMES

    def is_active(self, context: UnifiedContext) -> bool:
        return bool(context.metadata.get("mastery_mode"))

    def _tutor_style(self, context: UnifiedContext) -> str:
        style = str(context.metadata.get("tutor_style") or "deeptutor").strip().lower()
        return "memphis" if style == "memphis" else "deeptutor"

    def system_block(
        self,
        context: UnifiedContext,
        *,
        language: str,
        prompts: dict[str, Any],
    ) -> PromptBlock | None:
        if not self.is_active(context):
            return None
        override = _prompt_text(prompts, ("mastery", "system"))
        style = self._tutor_style(context)
        content = override or _load_system_prompt(language, style=style)
        return PromptBlock("mastery_tutor", content)

    def augment_kwargs(
        self,
        tool_name: str,
        kwargs: dict[str, Any],
        context: UnifiedContext,
    ) -> dict[str, Any]:
        if self.is_active(context) and tool_name in MASTERY_TOOL_NAMES:
            updated = dict(kwargs)
            updated["_mastery_path_id"] = str(context.metadata.get("mastery_path_id") or "").strip()
            updated["_session_id"] = str(context.session_id or "").strip()
            updated["_turn_id"] = str(context.metadata.get("turn_id") or "").strip()
            updated["_tutor_style"] = self._tutor_style(context)
            return updated
        return kwargs

    def pre_loop_seed(self, context: UnifiedContext) -> str:
        _ = context
        return ""


def _prompt_text(prompts: dict[str, Any], path: tuple[str, ...]) -> str:
    value: Any = prompts
    for key in path:
        if not isinstance(value, dict):
            return ""
        value = value.get(key)
    return value if isinstance(value, str) and value else ""


def _load_system_prompt(language: str, *, style: str = "deeptutor") -> str:
    """Load the system prompt file for the given language and tutor style.

    Args:
        language: User language code (e.g. "en", "zh").
        style: Tutor style — ``"deeptutor"`` (default) or ``"memphis"``.

    Returns:
        The raw prompt text.
    """
    lang = "zh" if language.lower().startswith("zh") else "en"
    filename = "system-memphis.md" if style == "memphis" else "system.md"
    prompt = resources.files(__package__).joinpath("prompts", lang, filename)
    return prompt.read_text(encoding="utf-8").strip()


__all__ = ["MasteryLoopCapability"]
