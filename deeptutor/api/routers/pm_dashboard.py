"""
pm_dashboard.py — Project Manager Dashboard API
===============================================
Endpoints for monitoring the watcher, sessions, projects, and pipeline health.
"""

import json
import os
import re
import subprocess
import uuid
from datetime import datetime, timezone
from pathlib import Path

import yaml

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from deeptutor.noteblocks.models import Note, Block, BlockType
from deeptutor.noteblocks.storage import NoteStorage

router = APIRouter(tags=["pm"])

PROJECT_DIR = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = PROJECT_DIR / "scripts" / "kb"
SESSOES_DIR = PROJECT_DIR / "kb" / "sessoes"
PROJETOS_DIR = PROJECT_DIR / "kb" / "projetos"
CLASSIFICATION_FILE = SESSOES_DIR / "classification.json"
WATCHER_STATE = SCRIPTS_DIR / ".watcher_state.json"
WATCHER_HEALTHY = SCRIPTS_DIR / ".watcher_healthy"
WATCHER_RUNNING = SCRIPTS_DIR / ".watcher_running"
WATCHER_LOG = SCRIPTS_DIR / "watcher.log"
STATE_JSON = PROJECT_DIR / "project-state" / "ai-stem-tutor.json"


def _read_json(path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, OSError):
        return None


PROJECT_KEYWORDS: dict[str, tuple[str, str]] = {
    "ai-stem-tutor": ("AI STEM Tutor — DeepTutor", [
        "ai tutor", "deeptutor", "deep tutor", "stem tutor", "ai-stem", "deep t",
        "noteblocks", "mind map", "mermaid", "project manager", "unified mind",
        "rode o front", "rode o back", "rodar front", "kb pipeline",
        "mastery path", "mastery", "knowledge base", "memphis", "bkt",
        "learning space", "space", "conceitual", "subagente",
    ]),
    "tcc": ("TCC — Ingrid (MD/Desalination)", [
        "tcc", "ingrid", "desalination", "md/", "membrana",
        "flux", "permeate", "vmd", "agmd", "reverse osmosis",
        "tese", "thesis", "disserta", "poli slides",
    ]),
    "notion-infra": ("Notion Infrastructure", [
        "notion", "workflows", "obsidian", "composio",
        "session agent", "escrever entrada", "@session",
    ]),
    "luc-repport": ("Luc-Repport", [
        "luc-repport", "luc rep", "luc appendix", "luc data",
    ]),
    "pinns": ("PINNs", [
        "pinns", "physics-informed", "pinn",
    ]),
    "plex": ("Plex / Media", [
        "plex", "media server",
    ]),
    "personal": ("Personal / PC", [
        "personal", "pc ", "windows", "desativar",
    ]),
}


def _classify_session(title: str, agent: str, directory: str) -> tuple[str, str]:
    """Classify a session into a project based on title, agent, and directory."""
    text = f"{title} {agent}".lower()
    dir_lower = directory.lower()

    for p_slug, (p_name, keywords) in PROJECT_KEYWORDS.items():
        for kw in keywords:
            if kw in text or kw in dir_lower:
                return (p_slug, p_name)

    # Agent-based fallbacks
    if agent == "session":
        return ("notion-infra", "Notion Infrastructure")

    return ("opencode-explore", "OpenCode Exploration")


def _get_classification() -> dict | None:
    """Get classification, with fallback to opencode DB query."""
    cached = _read_json(CLASSIFICATION_FILE)
    if cached:
        return cached

    # Build from opencode DB
    rows = _query_opencode("SELECT slug, title, agent, model, cost, directory, path, "
                           "datetime(time_created / 1000, 'unixepoch') as date_created "
                           "FROM session WHERE slug IS NOT NULL AND slug != '' "
                           "ORDER BY time_created DESC")
    if not rows:
        return None

    result = {}
    for r in rows:
        slug = r["slug"]
        if slug == "empty":
            continue

        proj_slug, proj_name = _classify_session(
            r["title"] or slug, r["agent"] or "", r["directory"] or ""
        )

        model_raw = r["model"]
        model_id = ""
        if model_raw:
            try:
                mo = json.loads(model_raw) if isinstance(model_raw, str) else model_raw
                model_id = mo.get("modelID", mo.get("id", ""))
            except Exception:
                model_id = str(model_raw)[:50]

        result[slug] = {
            "project_slug": proj_slug,
            "project_name": proj_name,
            "title": r["title"] or slug,
            "date": (r["date_created"] or "")[:10],
            "agent": r["agent"] or "",
            "model": model_id,
            "cost": round(r["cost"] or 0, 6),
        }

    return {"classification": result}


def _tail_file(path, n=50):
    if not path.exists():
        return []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        return lines[-n:]
    except OSError:
        return []


def _is_process_alive(pid=None):
    if pid:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False
    if WATCHER_RUNNING.exists():
        try:
            pid = int(WATCHER_RUNNING.read_text().strip())
            return _is_process_alive(pid)
        except (ValueError, OSError):
            pass
    return False


def _find_watcher_pid():
    try:
        result = subprocess.run(
            ["powershell", "-Command",
             "Get-Process python* | Where-Object { $_.CommandLine -like '*watch-opencode*' } | Select-Object -ExpandProperty Id"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0 and result.stdout.strip():
            return int(result.stdout.strip().split('\n')[0])
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.get("/api/v1/pm/status")
async def pm_status():
    """Watcher status, health pulse, uptime."""
    pid = _find_watcher_pid()
    running = pid is not None

    last_pulse = None
    if WATCHER_HEALTHY.exists():
        try:
            last_pulse = WATCHER_HEALTHY.read_text().strip()
        except OSError:
            pass

    watcher_state = _read_json(WATCHER_STATE)
    processed_count = len(watcher_state.get("processed_sessions", [])) if watcher_state else 0
    tracked_count = len(watcher_state.get("last_updated_map", {})) if watcher_state else 0

    return {
        "running": running,
        "pid": pid,
        "last_healthy_pulse": last_pulse,
        "last_pulse_seconds_ago": (
            round((datetime.now() - datetime.fromisoformat(last_pulse)).total_seconds())
            if last_pulse else None
        ),
        "sessions_processed": processed_count,
        "sessions_tracked": tracked_count,
        "watcher_state_file": str(WATCHER_STATE),
    }


@router.get("/api/v1/pm/logs")
async def pm_logs(tail: int = 50):
    """Recent watcher log lines."""
    return {"lines": _tail_file(WATCHER_LOG, tail)}


@router.get("/api/v1/pm/projects")
async def pm_projects():
    """All projects with session counts and cost."""
    classification = _get_classification()
    if not classification:
        return {"projects": [], "total_sessions": 0, "total_cost": 0.0}

    by_project = {}
    for slug, info in classification.get("classification", {}).items():
        proj = info.get("project_name", "Unknown")
        if proj not in by_project:
            by_project[proj] = {"name": proj, "slug": info.get("project_slug", ""), "count": 0, "cost": 0.0}
        by_project[proj]["count"] += 1
        by_project[proj]["cost"] += info.get("cost", 0)

    projects = sorted(by_project.values(), key=lambda p: -p["count"])
    total_cost = sum(p["cost"] for p in projects)
    total_sessions = sum(p["count"] for p in projects)

    return {"projects": projects, "total_sessions": total_sessions, "total_cost": round(total_cost, 2)}


@router.get("/api/v1/pm/sessions/recent")
async def pm_sessions_recent(limit: int = 20):
    """Most recent sessions across all projects."""
    classification = _get_classification()
    if not classification:
        return {"sessions": []}

    all_sessions = []
    for slug, info in classification.get("classification", {}).items():
        if info.get("project_slug") in ("empty", "unclassified"):
            continue
        all_sessions.append({
            "slug": slug,
            "title": info.get("title", slug),
            "project": info.get("project_name", ""),
            "project_slug": info.get("project_slug", ""),
            "date": info.get("date", ""),
            "agent": info.get("agent", ""),
            "cost": info.get("cost", 0),
        })

    all_sessions.sort(key=lambda s: s.get("date", ""), reverse=True)
    return {"sessions": all_sessions[:limit]}


@router.get("/api/v1/pm/health")
async def pm_health():
    """Overall health check."""
    watcher_status = await pm_status()
    healthy = watcher_status["running"]

    log_lines = _tail_file(WATCHER_LOG, 3)
    last_log = log_lines[-1] if log_lines else ""

    return {
        "healthy": healthy,
        "watcher_running": watcher_status["running"],
        "last_log": last_log,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/api/v1/pm/stats")
async def pm_stats():
    """Aggregate statistics."""
    classification = _get_classification()
    state = _read_json(STATE_JSON)

    total_sessions = len(classification.get("classification", {})) if classification else 0
    total_cost = sum(
        s.get("cost", 0) for s in classification.get("classification", {}).values()
    ) if classification else 0

    stem_sessions = len(state.get("sessions", [])) if state else 0
    stem_cost = state.get("total_cost", 0) if state else 0

    return {
        "total_sessions": total_sessions,
        "total_cost": round(total_cost, 2),
        "total_live_docs": len(list(SESSOES_DIR.glob("*.md"))) if SESSOES_DIR.exists() else 0,
        "total_projects": len(list(PROJETOS_DIR.iterdir())) if PROJETOS_DIR.exists() else 0,
        "stem_tutor_sessions": stem_sessions,
        "stem_tutor_cost": round(stem_cost, 2),
    }


# ---------------------------------------------------------------------------
# Multi-project detail endpoints
# ---------------------------------------------------------------------------


@router.get("/api/v1/pm/projects/{slug}")
async def pm_project_detail(slug: str):
    """Detailed report for a specific project by slug."""
    classification = _get_classification()
    state_file = PROJECT_DIR / "project-state" / f"{slug}.json"
    state = _read_json(state_file)

    # Aggregate from classification
    sessions_list = []
    total_cost = 0.0
    date_min = None
    date_max = None

    if classification:
        for sess_slug, info in classification.get("classification", {}).items():
            if info.get("project_slug") != slug:
                continue
            cost = info.get("cost", 0)
            total_cost += cost
            date_str = info.get("date", "")
            if date_str:
                if not date_min or date_str < date_min:
                    date_min = date_str
                if not date_max or date_str > date_max:
                    date_max = date_str
            sessions_list.append({
                "slug": sess_slug,
                "title": info.get("title", sess_slug),
                "project": info.get("project_name", ""),
                "date": date_str,
                "agent": info.get("agent", ""),
                "cost": round(cost, 4),
            })

    sessions_list.sort(key=lambda s: s.get("date", ""), reverse=True)

    # Session dir info
    project_sessoes_dir = PROJETOS_DIR / slug / "sessoes"
    session_files = []
    if project_sessoes_dir.exists():
        session_files = sorted(
            [f.stem for f in project_sessoes_dir.glob("*.md")],
            reverse=True,
        )

    # Build decisions with session links
    decisions_list: list[dict] = []
    seen = set()

    # Per-session decisions
    for sess in (state or {}).get("sessions", []):
        sess_slug = sess.get("id", "")
        for d in sess.get("decisions", []):
            key = d[:80]  # dedup by first 80 chars
            if key not in seen:
                seen.add(key)
                decisions_list.append({"text": d, "session_slug": sess_slug})

    # Global decisions (no session link)
    for d in (state or {}).get("decisions", []):
        key = d[:80]
        if key not in seen:
            seen.add(key)
            decisions_list.append({"text": d, "session_slug": None})

    return {
        "slug": slug,
        "name": sessions_list[0]["project"] if sessions_list else slug,
        "total_sessions": len(sessions_list),
        "total_cost": round(total_cost, 2),
        "date_range": {"min": date_min, "max": date_max},
        "branch": (state or {}).get("branch"),
        "last_commit": (state or {}).get("last_commit"),
        "last_updated": (state or {}).get("last_updated"),
        "decisions": decisions_list[:30],
        "todos": (state or {}).get("todos", [])[:10],
        "recent_sessions": sessions_list[:20],
        "session_files_available": len(session_files),
    }


@router.get("/api/v1/pm/projects/{slug}/sessions")
async def pm_project_sessions(slug: str, limit: int = 50, offset: int = 0):
    """Paginated sessions for a specific project."""
    classification = _get_classification()
    if not classification:
        return {"sessions": [], "total": 0, "offset": offset, "limit": limit}

    all_sessions = []
    for sess_slug, info in classification.get("classification", {}).items():
        if info.get("project_slug") != slug:
            continue
        all_sessions.append({
            "slug": sess_slug,
            "title": info.get("title", sess_slug),
            "project": info.get("project_name", ""),
            "date": info.get("date", ""),
            "agent": info.get("agent", ""),
            "model": info.get("model", ""),
            "cost": info.get("cost", 0),
        })

    all_sessions.sort(key=lambda s: s.get("date", ""), reverse=True)
    total = len(all_sessions)
    page = all_sessions[offset:offset + limit]

    return {
        "sessions": page,
        "total": total,
        "offset": offset,
        "limit": limit,
    }


def _resolve_session_file(slug: str) -> tuple[dict, Path, str]:
    """Resolve a session slug to its classification info, file path, and project slug."""
    classification = _get_classification()
    if not classification:
        raise HTTPException(status_code=404, detail="No classification data")

    info = classification.get("classification", {}).get(slug)
    if not info:
        raise HTTPException(status_code=404, detail=f"Session '{slug}' not found")

    project_slug = info.get("project_slug", "")
    sessoes_dir = PROJETOS_DIR / project_slug / "sessoes"
    session_file = sessoes_dir / f"{slug}.md"

    if not session_file.exists():
        raise HTTPException(status_code=404, detail=f"Live doc not found for session '{slug}'")

    return info, session_file, project_slug


@router.get("/api/v1/pm/sessions/{slug}/live-doc")
async def pm_session_live_doc(slug: str):
    """Serve a session live doc as raw markdown content."""
    _, session_file, _ = _resolve_session_file(slug)
    content = session_file.read_text(encoding="utf-8")
    return Response(content=content, media_type="text/markdown")


@router.get("/api/v1/pm/sessions/{slug}/export")
async def pm_session_export(slug: str):
    """Return structured session data for the SessionViewer."""
    sessions = _query_opencode(
        "SELECT id, slug, title, agent, model, cost FROM session WHERE slug = ?",
        (slug,)
    )
    if not sessions:
        raise HTTPException(status_code=404, detail=f"Session '{slug}' not found")

    sess = sessions[0]
    session_id = sess["id"]

    # Fetch all messages
    messages = _query_opencode(
        "SELECT id, data FROM message WHERE session_id = ? ORDER BY time_created ASC",
        (session_id,)
    )

    result_messages = []
    for msg_row in messages:
        msg_data = json.loads(msg_row["data"])
        role = msg_data.get("role", "")
        if role not in ("user", "assistant"):
            continue

        # Fetch parts
        parts_raw = _query_opencode(
            "SELECT data FROM part WHERE message_id = ? ORDER BY time_created",
            (msg_row["id"],)
        )
        parts = []
        for p in parts_raw:
            pd = json.loads(p["data"])
            ptype = pd.get("type", "")
            if ptype in ("step-start", "step-finish", "compaction"):
                continue
            parts.append(pd)

        model_id = ""
        model_info = msg_data.get("model", {})
        if isinstance(model_info, dict):
            model_id = model_info.get("modelID", "") or model_info.get("id", "")

        cost = msg_data.get("cost", 0)
        tokens = msg_data.get("tokens", {})

        # Detect internal-only messages (tool calls without substantial text)
        is_internal = False
        if role == "assistant":
            has_substantive_text = False
            has_visible_tool = False
            for p in parts:
                pt = p.get("type", "")
                if pt == "text":
                    txt = (p.get("text") or "").strip()
                    if len(txt) > 80 and not txt.startswith("<task"):
                        has_substantive_text = True
                elif pt == "tool":
                    tool_name = p.get("tool", "")
                    if tool_name in ("bash", "powershell", "task", "composio"):
                        has_visible_tool = True
            is_internal = not has_substantive_text and has_visible_tool

        result_messages.append({
            "role": role,
            "id": msg_row["id"],
            "agent": msg_data.get("agent", ""),
            "modelID": model_id,
            "cost": cost,
            "tokens": tokens,
            "time": {"created": msg_data.get("time", {}).get("created", 0)},
            "parts": parts,
            "is_internal": is_internal,
        })

    return {
        "slug": slug,
        "title": sess["title"],
        "agent": sess["agent"],
        "messages": result_messages,
        "total_messages": len(result_messages),
    }


OPCODE_DB = Path.home() / ".local" / "share" / "opencode" / "opencode.db"


def _flatten(text: str, max_len: int = 500) -> str:
    """Flatten multi-line text into a single line for safe storage."""
    return re.sub(r'\r?\n', ' ↵ ', text.strip())[:max_len]


def _query_opencode(sql: str, params: tuple = ()) -> list:
    """Query the opencode SQLite database and return rows as dicts."""
    if not OPCODE_DB.exists():
        raise HTTPException(status_code=500, detail=f"OpenCode DB not found at {OPCODE_DB}")
    import sqlite3
    conn = sqlite3.connect(str(OPCODE_DB))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@router.post("/api/v1/pm/sessions/{slug}/to-note")
async def pm_session_to_note(slug: str):
    """Convert a session from opencode DB into a structured NoteBlocks note."""

    # Look up session ID from slug
    sessions = _query_opencode(
        "SELECT id, slug, title, agent, model, cost FROM session WHERE slug = ?",
        (slug,)
    )
    if not sessions:
        raise HTTPException(status_code=404, detail=f"Session '{slug}' not found in opencode DB")

    sess = sessions[0]
    session_id = sess["id"]

    # Fetch all messages ordered by creation time
    messages = _query_opencode(
        "SELECT id, data FROM message WHERE session_id = ? ORDER BY time_created ASC",
        (session_id,)
    )

    blocks: list[Block] = []
    max_blocks = 150
    msg_num = 0

    for msg_row in messages:
        if len(blocks) >= max_blocks:
            break
        msg_data = json.loads(msg_row["data"])
        role = msg_data.get("role", "")

        # Fetch parts for this message
        parts = _query_opencode(
            "SELECT id, data FROM part WHERE message_id = ? ORDER BY time_created",
            (msg_row["id"],)
        )

        if role == "user":
            msg_num += 1
            # Collect all text from user message parts
            user_texts = []
            for p in parts:
                pd = json.loads(p["data"])
                if pd.get("type") == "text":
                    user_texts.append(pd.get("text", ""))
            if user_texts:
                blocks.append(Block(
                    type=BlockType.HEADING,
                    content=f"👤 Você (#{msg_num})",
                    origin="human",
                    collapsed=False,
                ))
                for text in user_texts:
                    line = _flatten(text)
                    if line:
                        blocks.append(Block(
                            type=BlockType.TEXT,
                            content=line,
                            origin="human",
                            collapsed=False,
                        ))

        elif role == "assistant":
            msg_num += 1
            has_response = False
            assistant_texts = []
            tool_blocks = []
            saw_tool = False

            for p in parts:
                pd = json.loads(p["data"])
                ptype = pd.get("type", "")

                if ptype == "text":
                    text = pd.get("text", "").strip()
                    if text:
                        # Only use text parts that appear before the first tool call
                        # (text after tools is subagent output, not assistant speech)
                        if not saw_tool:
                            assistant_texts.append(text)
                            has_response = True

                elif ptype == "tool":
                    saw_tool = True
                    tool_name = pd.get("tool", "")
                    state = pd.get("state", {})
                    status = state.get("status", "")
                    inp = state.get("input", {})
                    out = state.get("output", "")

                    if tool_name in ("bash",):
                        cmd = inp.get("command", "") if isinstance(inp, dict) else ""
                        if cmd:
                            tool_blocks.append(("command", cmd))
                            has_response = True
                        if out:
                            o = out[:1500]
                            tool_blocks.append(("output", o))

                    elif tool_name == "task":
                        has_response = True
                        desc = inp.get("description", "") if isinstance(inp, dict) else str(inp)
                        tool_blocks.append(("subagent", desc))

                    elif status == "error":
                        err = str(state.get("output", ""))[:300]
                        tool_blocks.append(("error", err))

            if has_response or tool_blocks:
                heading = f"🤖 Assistente (#{msg_num})"
                blocks.append(Block(
                    type=BlockType.HEADING,
                    content=heading,
                    origin="opencode",
                    collapsed=False,
                ))

                # Add assistant text (before tool calls) - single-line blocks
                for text in assistant_texts:
                    line = _flatten(text)
                    if line:
                        blocks.append(Block(
                            type=BlockType.TEXT,
                            content=line,
                            origin="opencode",
                            collapsed=True,
                        ))

                # Add tool blocks (single-line only for clean storage round-trip)
                for tb_type, tb_content in tool_blocks:
                    safe = _flatten(tb_content)
                    if tb_type == "command":
                        blocks.append(Block(
                            type=BlockType.TEXT,
                            content=f"$ {safe}",
                            origin="opencode",
                            collapsed=True,
                        ))
                    elif tb_type == "output":
                        blocks.append(Block(
                            type=BlockType.TEXT,
                            content=f"📋 {_flatten(tb_content, 200)}",
                            origin="opencode",
                            collapsed=True,
                        ))
                    elif tb_type == "error":
                        blocks.append(Block(
                            type=BlockType.TEXT,
                            content=f"[Error] {safe}",
                            origin="opencode",
                            collapsed=True,
                        ))
                    elif tb_type == "subagent":
                        blocks.append(Block(
                            type=BlockType.TEXT,
                            content=f"🧠 {safe}",
                            origin="opencode",
                            collapsed=True,
                        ))

    # If no blocks from DB, fall back to raw markdown
    if not blocks:
        _, session_file, project_slug = _resolve_session_file(slug)
        raw = session_file.read_text(encoding="utf-8")
        fm_parts = raw.split("---\n", 2)
        frontmatter = {}
        if len(fm_parts) >= 3 and fm_parts[0].strip() == "":
            frontmatter = yaml.safe_load(fm_parts[1]) or {}
        blocks.append(Block(
            type=BlockType.TEXT,
            content="(Live doc não disponível no opencode DB — use o botão MD para ver o raw)",
            origin="human",
            collapsed=False,
        ))
    else:
        frontmatter = {}

    # Determine project slug from classification if available
    try:
        _, _, project_slug = _resolve_session_file(slug)
    except HTTPException:
        project_slug = ""

    note_id = uuid.uuid4().hex[:12]
    title = sess["title"]
    note = Note(
        id=note_id,
        title=f"Sessão: {title}",
        blocks=blocks,
        tags=["session", slug],
        project=project_slug or slug,
        session=slug,
    )

    notes_dir = Path("data/noteblocks/notes")
    storage = NoteStorage(notes_dir)
    storage.save(note)

    return {
        "note_id": note_id,
        "title": note.title,
        "blocks": len(note.blocks),
        "source": "opencode_db",
        "messages": len(messages),
    }
