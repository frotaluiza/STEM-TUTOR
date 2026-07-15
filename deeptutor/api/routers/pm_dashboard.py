"""
pm_dashboard.py — Project Manager Dashboard API
===============================================
Endpoints for monitoring the watcher, sessions, projects, and pipeline health.
"""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import uuid

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
import yaml

from deeptutor.noteblocks.models import Block, BlockType, Note
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
    """All projects with session counts, cost, and latest session date."""
    classification = _get_classification()
    if not classification:
        return {"projects": [], "total_sessions": 0, "total_cost": 0.0}

    by_project = {}
    for slug, info in classification.get("classification", {}).items():
        proj = info.get("project_name", "Unknown")
        if proj not in by_project:
            by_project[proj] = {
                "name": proj, "slug": info.get("project_slug", ""),
                "count": 0, "cost": 0.0, "last_date": "",
            }
        by_project[proj]["count"] += 1
        by_project[proj]["cost"] += info.get("cost", 0)
        date = info.get("date", "")
        if date and date > by_project[proj].get("last_date", ""):
            by_project[proj]["last_date"] = date

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


OPCODE_DOCS_DIR = Path.home() / ".local" / "share" / "opencode" / "docs"


def _resolve_session_file(slug: str) -> tuple[dict, Path, str]:
    """Resolve a session slug to its classification info, file path, and project slug.
    Falls back to opencode docs dir when KB file doesn't exist."""
    classification = _get_classification()
    if not classification:
        raise HTTPException(status_code=404, detail="No classification data")

    info = classification.get("classification", {}).get(slug)
    if not info:
        raise HTTPException(status_code=404, detail=f"Session '{slug}' not found")

    project_slug = info.get("project_slug", "")

    # Try KB dir first
    sessoes_dir = PROJETOS_DIR / project_slug / "sessoes"
    session_file = sessoes_dir / f"{slug}.md"
    if session_file.exists():
        return info, session_file, project_slug

    # Fallback to opencode docs dir
    session_file = OPCODE_DOCS_DIR / f"{slug}.md"
    if session_file.exists():
        return info, session_file, project_slug

    raise HTTPException(status_code=404, detail=f"Live doc not found for session '{slug}'")


@router.get("/api/v1/pm/sessions/{slug}/live-doc")
async def pm_session_live_doc(slug: str):
    """Serve clean markdown generated from opencode DB."""
    try:
        export = await pm_session_export(slug)
    except HTTPException:
        # Fallback to file with corruption fix
        _, session_file, _ = _resolve_session_file(slug)
        raw = session_file.read_bytes()
        # Remove E2 94 9C prefix before C3 bytes
        raw = raw.replace(b"\xe2\x94\x9c\xc3", b"\xc3")
        # Remove E2 94 9C prefix before C2 bytes (double corruption)
        raw = raw.replace(b"\xe2\x94\x9c\xc2", b"\xc2")
        # Remove remaining lone E2 94 9C
        raw = raw.replace(b"\xe2\x94\x9c", b"")
        content = raw.decode("utf-8", errors="replace")
        return Response(content=content, media_type="text/markdown")

    # Build clean markdown from export data
    lines = [f"# Sessão: {slug}", "", f"**Total de mensagens:** {export.get('total_messages', 0)}", ""]
    for msg in export.get("messages", []):
        role = msg.get("role", "")
        agent = msg.get("agent", "")
        ts = ""
        t = msg.get("time", {}) or {}
        if t.get("created"):
            from datetime import datetime
            ts = datetime.fromtimestamp(t["created"] / 1000).strftime(" (%d/%m %H:%M)")

        icon = "👤" if role == "user" else "🤖"
        lines.append(f"## {icon} {'Você' if role == 'user' else 'Assistente'}{ts}")
        lines.append("")

        for p in msg.get("parts", []):
            ptype = p.get("type", "")
            if ptype in ("step-start", "step-finish", "compaction"):
                continue
            if ptype == "reasoning":
                continue  # skip reasoning
            if ptype == "text":
                text = (p.get("text") or "").strip()
                if text:
                    # Escape markdown special chars? No, render as-is
                    lines.append(text)
                    lines.append("")
            elif ptype == "tool":
                tool_name = p.get("tool", "")
                state = p.get("state", {}) or {}
                status = state.get("status", "")
                inp = state.get("input", {}) or {}
                out = (state.get("output") or "")[:500]

                if tool_name in ("bash", "powershell"):
                    cmd = inp.get("command", "") if isinstance(inp, dict) else ""
                    if cmd:
                        lines.append(f"```bash\n{cmd}\n```")
                    if out:
                        lines.append(f"```\n{out}\n```")
                elif tool_name == "task":
                    desc = inp.get("description", "") if isinstance(inp, dict) else str(inp)
                    if desc:
                        lines.append(f"> 🧠 Subagente: {desc}")
                    if status == "error" and out:
                        lines.append(f"> ❌ Erro: {out[:200]}")
                lines.append("")

    content = "\n".join(lines)
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


@router.post("/api/v1/pm/sessions/{slug}/fork")
async def pm_session_fork(slug: str):
    """Fork a session — opens it in a new opencode TUI window."""
    sessions = _query_opencode(
        "SELECT id, slug, title, directory FROM session WHERE slug = ?",
        (slug,)
    )
    if not sessions:
        raise HTTPException(status_code=404, detail=f"Session '{slug}' not found in opencode DB")

    sess = sessions[0]
    session_id = sess["id"]
    directory = sess["directory"] or str(Path.home())

    # Build the fork command
    cmd = f'opencode --fork --session {session_id}'

    try:
        import subprocess
        subprocess.Popen(
            ["powershell", "-NoExit", "-Command", cmd],
            cwd=directory,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        return {
            "forked": True,
            "session_id": session_id,
            "slug": slug,
            "title": sess["title"],
            "command": cmd,
        }
    except Exception as e:
        return {
            "forked": False,
            "session_id": session_id,
            "slug": slug,
            "command": cmd,
            "error": str(e),
            "manual": f"Execute no terminal: {cmd}",
        }


KB_DIRS = [
    PROJECT_DIR / "data" / "knowledge_bases",
    Path.home() / ".local" / "share" / "opencode" / "docs",
    PROJECT_DIR / "data" / "noteblocks" / "notes",
]


@router.get("/api/v1/pm/space/{slug}")
async def pm_project_space(slug: str, branch: str | None = None):
    """Unified project space data: state + sessions + KBs + notes + learning + videos."""
    # 0. Load project state by branch
    ps_data = None
    if branch and branch != "main":
        ps_file = PROJECT_DIR / "project-state" / "branches" / f"{branch.replace('/', '-')}.json"
        if ps_file.exists():
            ps_data = json.loads(ps_file.read_text(encoding="utf-8-sig"))
    else:
        ps_file = PROJECT_DIR / "project-state" / "ai-stem-tutor.json"
        if ps_file.exists():
            ps_data = json.loads(ps_file.read_text(encoding="utf-8-sig"))

    resolved_branch = (ps_data or {}).get("branch", "main")

    # 1. Project detail (sessions, decisions, branch, commits)
    detail = await pm_project_detail(slug)

    # 2. Knowledge bases from data dir
    kbs = []
    kb_data_dir = PROJECT_DIR / "data" / "knowledge_bases"
    if kb_data_dir.exists():
        for kb_dir in kb_data_dir.iterdir():
            if kb_dir.is_dir():
                doc_count = len(list(kb_dir.glob("*.md"))) + len(list(kb_dir.glob("*.pdf")))
                kbs.append({
                    "name": kb_dir.name,
                    "documents": doc_count,
                    "path": str(kb_dir),
                })

    # 3. NoteBlocks notes
    notes = []
    noteblocks_dir = PROJECT_DIR / "data" / "noteblocks" / "notes"
    if noteblocks_dir.exists():
        for f in noteblocks_dir.glob("*.md"):
            try:
                content = f.read_text(encoding="utf-8")
                parts = content.split("---\n", 2)
                note_data = yaml.safe_load(parts[1]) if len(parts) >= 3 and parts[0].strip() == "" else {}
                if note_data.get("project") == slug or note_data.get("session"):
                    notes.append({
                        "id": f.stem,
                        "title": note_data.get("title", f.stem),
                        "project": note_data.get("project"),
                        "session": note_data.get("session"),
                        "tags": note_data.get("tags", []),
                        "blocks": len(note_data.get("_blocks", [])),
                        "size": f.stat().st_size,
                        "type": "noteblocks",
                    })
            except Exception:
                pass

    # 4. Videos from KB videos directory
    videos = []
    videos_dir = PROJECT_DIR / "kb" / "videos"
    if videos_dir.exists():
        for f in videos_dir.glob("*.md"):
            try:
                content = f.read_text(encoding="utf-8")
                fm = yaml.safe_load(content.split("---\n", 2)[1]) if "---\n" in content else {}
                if fm.get("link"):
                    videos.append({
                        "title": fm.get("title", f.stem),
                        "url": fm["link"],
                        "channel": fm.get("channel", ""),
                        "tags": fm.get("tags", []),
                        "duracao": fm.get("duracao", ""),
                    })
            except Exception:
                pass

    # Also check youtube video DB from session search results
    try:
        share_videos = _query_opencode(
            "SELECT DISTINCT slug, title FROM session "
            "WHERE (LOWER(title) LIKE '%youtube%' OR LOWER(title) LIKE '%wolfram%' "
            "OR LOWER(title) LIKE '%video%') AND title NOT LIKE 'New session%' LIMIT 10"
        )
        for v in share_videos:
            videos.append({
                "title": (v.get("title") or "")[:80],
                "url": f"/session-viewer/{v.get('slug', '')}",
                "source": "opencode_session",
            })
    except Exception:
        pass

    # 5. Active sessions from opencode DB
    active_sessions = []
    closed_sessions = []
    try:
        all_sessions = _query_opencode(
            "SELECT slug, title, agent, model, cost, datetime(time_created / 1000, 'unixepoch') as date_created, "
            "tokens_input, tokens_output "
            "FROM session ORDER BY time_created DESC LIMIT 50"
        )
        for s in all_sessions:
            entry = {
                "slug": s.get("slug"),
                "title": s.get("title", "")[:80],
                "agent": s.get("agent", ""),
                "messages": (s.get("tokens_input") or 0) // 1000 + 1,
                "custo": round(s.get("cost") or 0, 4),
                "date": (s.get("date_created") or "")[:10],
                "branch": resolved_branch if s.get("slug") in [x.get("slug") for x in (ps_data or {}).get("sessoes_ativas", [])] else "main",
            }
            # Simple heuristic: sessions with "concluído" or older than 3 days in title are "closed"
            title_lower = (s.get("title") or "").lower()
            if any(w in title_lower for w in ["encerrada", "concluído", "concluido", "archive"]) or False:
                closed_sessions.append(entry)
            else:
                active_sessions.append(entry)
    except Exception:
        pass

    # 4b. Learning modules (placeholder)
    learning = {}

    # 5. Session stats
    session_stats = {
        "ativas": len(active_sessions),
        "encerradas": len(closed_sessions),
        "total": len(active_sessions) + len(closed_sessions),
    }
    nodes = []
    edges = []

    # Root project node
    nodes.append({
        "id": f"project-{slug}", "label": slug, "type": "project", "color": "#6366f1"
    })

    ei = 0  # edge index for unique IDs

    branch = detail.get("branch")
    if branch:
        nodes.append({
            "id": f"branch-{slug}", "label": str(branch)[:30], "type": "branch", "color": "#8b5cf6"
        })
        edges.append({"id": f"e-{ei}", "source": f"project-{slug}", "target": f"branch-{slug}", "label": "branch"})
        ei += 1

    for i, s in enumerate(detail.get("recent_sessions", [])[:10]):
        sid = s.get("slug", f"session-{i}")
        nodes.append({
            "id": sid, "label": (s.get("title") or sid)[:40],
            "type": "session", "color": "#3b82f6",
            "subtitle": s.get("date", ""),
        })
        edges.append({"id": f"e-{ei}", "source": f"project-{slug}", "target": sid, "label": "session"})
        ei += 1

        for j, dec in enumerate(detail.get("decisions", [])[:3]):
            did = f"decision-{i}-{j}"
            nodes.append({
                "id": did, "label": (dec.get("text") if isinstance(dec, dict) else str(dec))[:50],
                "type": "decision", "color": "#f59e0b",
            })
            edges.append({"id": f"e-{ei}", "source": sid, "target": did, "label": "decision"})
            ei += 1

    for kb in kbs[:8]:
        kb_id = f"kb-{kb['name']}"
        nodes.append({
            "id": kb_id, "label": kb["name"][:30],
            "type": "kb", "color": "#14b8a6",
            "subtitle": f"{kb.get('documents', 0)} documentos",
        })
        edges.append({"id": f"e-{ei}", "source": f"project-{slug}", "target": kb_id, "label": "kb"})
        ei += 1

    for n in notes[:8]:
        note_id = f"note-{n['id']}"
        nodes.append({
            "id": note_id, "label": (n.get("title") or n["id"])[:30],
            "type": "note", "color": "#f97316",
            "subtitle": f"{(n.get('blocks') or [])} blocks" if n.get("blocks") else "",
        })
        edges.append({"id": f"e-{ei}", "source": f"project-{slug}", "target": note_id, "label": "note"})
        ei += 1

    for mod_name in list(learning.keys())[:5]:
        mod_id = f"module-{mod_name}"
        nodes.append({
            "id": mod_id, "label": mod_name[:30],
            "type": "module", "color": "#a855f7",
        })
        edges.append({"id": f"e-{ei}", "source": f"project-{slug}", "target": mod_id, "label": "learning"})
        ei += 1

    return {
        "project": slug,
        "branch": resolved_branch,
        "nodes": nodes,
        "edges": edges,
        "features": (ps_data or {}).get("features", []),
        "repositorio_codigo": (ps_data or {}).get("repositorio_codigo", ""),
        "kbs": kbs[:20],
        "notes": notes[:20],
        "videos": videos[:20],
        "sessoes": {
            "ativas": active_sessions[:20],
            "encerradas": closed_sessions[:20],
        },
        "decisions": detail.get("decisions", [])[:20],
        "todos": (ps_data or {}).get("todos", [])[:10],
        "meta": {
            "sessions": detail.get("total_sessions", 0),
            "total_cost": detail.get("total_cost", 0),
            "branch": resolved_branch,
            "kbs": len(kbs),
            "notes": len(notes),
            "videos": len(videos),
            "modules": len(learning),
            "session_stats": session_stats,
            "features_count": len((ps_data or {}).get("features", [])),
        },
    }


TAREFAS_DIR = PROJECT_DIR / "project-state"


def _tarefas_file(branch: str = "main") -> Path:
    """Path to the tarefas JSON file for a given branch."""
    f = TAREFAS_DIR / "branches" if branch != "main" else TAREFAS_DIR
    f = f / f"tarefas-{branch.replace('/', '-')}.json"
    f.parent.mkdir(parents=True, exist_ok=True)
    return f


def _load_tarefas(branch: str = "main") -> list:
    p = _tarefas_file(branch)
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, OSError):
        return []


def _save_tarefas(tarefas: list, branch: str = "main"):
    _tarefas_file(branch).write_text(
        json.dumps(tarefas, indent=2, ensure_ascii=False), encoding="utf-8"
    )


@router.get("/api/v1/pm/tarefas")
async def pm_list_tarefas(branch: str = "main", session_slug: str | None = None):
    """List tasks, optionally filtered by branch or session."""
    tarefas = _load_tarefas(branch)
    if session_slug:
        tarefas = [t for t in tarefas if t.get("session_slug") == session_slug]
    return {"tarefas": tarefas, "count": len(tarefas), "branch": branch}


@router.post("/api/v1/pm/tarefas", status_code=201)
async def pm_create_tarefa(body: dict):
    """Create a new task."""
    tarefas = _load_tarefas(body.get("branch", "main"))
    task = {
        "id": uuid.uuid4().hex[:12],
        "text": body.get("text", ""),
        "feito": False,
        "session_slug": body.get("session_slug", ""),
        "prioridade": body.get("prioridade", "media"),
        "tags": body.get("tags", []),
        "created": datetime.now(timezone.utc).isoformat(),
        "updated": datetime.now(timezone.utc).isoformat(),
    }
    if not task["text"]:
        raise HTTPException(status_code=400, detail="text is required")
    tarefas.insert(0, task)
    _save_tarefas(tarefas, body.get("branch", "main"))
    return task


@router.patch("/api/v1/pm/tarefas/{task_id}")
async def pm_update_tarefa(task_id: str, body: dict):
    """Toggle task status or update fields."""
    branch = body.get("branch", "main")
    tarefas = _load_tarefas(branch)
    for t in tarefas:
        if t["id"] == task_id:
            if "feito" in body:
                t["feito"] = body["feito"]
            if "text" in body:
                t["text"] = body["text"]
            if "prioridade" in body:
                t["prioridade"] = body["prioridade"]
            t["updated"] = datetime.now(timezone.utc).isoformat()
            _save_tarefas(tarefas, branch)
            return t
    raise HTTPException(status_code=404, detail="Task not found")




@router.get("/api/v1/pm/conflicts")
async def pm_conflicts(source: str = "main", target: str | None = None):
    """Simulate a merge to detect conflicts between two branches."""
    if not target:
        target = _run_git(["branch", "--show-current"]) or "main"

    # Fetch latest from remote
    _run_git(["fetch", "--prune", "personal"])
    _run_git(["fetch", "--prune", "origin"])

    def _resolve_ref(name: str) -> str:
        """Resolve a branch name to a full ref that git can use."""
        # Try local first
        local = _run_git(["rev-parse", "--verify", name])
        if local:
            return name
        # Try with origin/ prefix
        origin_ref = _run_git(["rev-parse", "--verify", f"origin/{name}"])
        if origin_ref:
            return f"origin/{name}"
        # Try personal/ prefix
        personal_ref = _run_git(["rev-parse", "--verify", f"personal/{name}"])
        if personal_ref:
            return f"personal/{name}"
        return name  # fallback, will fail

    source_ref = _resolve_ref(source)
    target_ref = _resolve_ref(target)

    # Use git merge-tree to simulate merge
    merge_base = _run_git(["merge-base", source_ref, target_ref])
    if not merge_base:
        return {"error": f"Não foi possível encontrar base comum entre {source} e {target}", "conflicts": []}

    tree_result = _run_git_binary(["merge-tree", merge_base, source_ref, target_ref])
    if not tree_result:
        return {"error": "merge-tree falhou", "conflicts": []}

    # Parse merge-tree output for conflicts
    lines = tree_result.split("\n")
    conflicts = []
    current_file = ""
    in_conflict = False

    # Parse merge-tree output for real conflicts
    import re
    conflict_pattern = re.compile(r"^CONFLICT\s+\(content\):\s+Merge conflict in (.+)$")

    for line in lines:
        m = conflict_pattern.match(line)
        if m:
            fname = m.group(1).strip()
            conflicts.append({
                "file": fname,
                "type": "content",
                "description": line.strip(),
            })
            current_file = fname
            continue

        if line.startswith("CHANGED:"):
            parts = line.split()
            if len(parts) >= 2:
                fname = parts[-1]
                conflicts.append({
                    "file": fname,
                    "type": "auto-merge",
                    "description": "Será mergeado automaticamente",
                })

    # Get ahead/behind info
    ahead = _run_git(["rev-list", "--count", f"{target_ref}..{source_ref}"]) or "0"
    behind = _run_git(["rev-list", "--count", f"{source_ref}..{target_ref}"]) or "0"

    # Diff stats
    diff_stat = _run_git(["diff", "--stat", f"{target_ref}...{source_ref}"])
    files_changed = 0
    insertions = 0
    deletions = 0
    for line in (diff_stat or "").split("\n"):
        if "file" in line and "changed" in line:
            import re
            m = re.search(r"(\d+) file", line)
            if m: files_changed = int(m.group(1))
            m = re.search(r"(\d+) insertion", line)
            if m: insertions = int(m.group(1))
            m = re.search(r"(\d+) deletion", line)
            if m: deletions = int(m.group(1))

    # Commits to be merged
    log = _run_git(["log", "--oneline", f"{target_ref}...{source_ref}"])
    commits = [l.strip() for l in (log or "").split("\n") if l.strip()][:20]

    has_conflicts = any(c["type"] == "content" for c in conflicts)

    return {
        "source": source,
        "source_ref": source_ref,
        "target": target,
        "target_ref": target_ref,
        "has_conflicts": has_conflicts,
        "conflicts": conflicts[:20],
        "conflict_count": len([c for c in conflicts if c["type"] == "content"]),
        "auto_merge_count": len([c for c in conflicts if c["type"] == "auto-merge"]),
        "ahead": int(ahead),
        "behind": int(behind),
        "files_changed": files_changed,
        "insertions": insertions,
        "deletions": deletions,
        "commits": commits,
        "merge_base": merge_base[:12],
    }
@router.delete("/api/v1/pm/tarefas/{task_id}")
async def pm_delete_tarefa(task_id: str, branch: str = "main"):
    """Delete a task."""
    tarefas = _load_tarefas(branch)
    tarefas = [t for t in tarefas if t["id"] != task_id]
    _save_tarefas(tarefas, branch)
    return {"deleted": True, "task_id": task_id}


# ---------------------------------------------------------------------------
# Branches + Sync Status
# ---------------------------------------------------------------------------


def _run_git_binary(args: list[str]) -> str:
    """Run git and return stdout as utf-8, ignoring decode errors."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True, timeout=15,
            cwd=PROJECT_DIR,
        )
        return result.stdout.decode("utf-8", errors="replace").strip()
    except Exception:
        return ""


def _run_git(args: list[str]) -> str:
    """Run a git command in the project directory and return stdout."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True, text=True, timeout=15,
            cwd=PROJECT_DIR,
        )
        return result.stdout.strip()
    except Exception:
        return ""


@router.get("/api/v1/pm/branches")
async def pm_list_branches(slug: str = "ai-stem-tutor"):
    """List all branches (local + remote) with their project state files."""
    _run_git(["fetch", "--prune", "personal"])
    _run_git(["fetch", "--prune", "origin"])
    local_raw = _run_git(["branch", "--list"]).split("\n")
    branches = []
    seen = set()
    for b in local_raw:
        name = b.replace("*", "").strip()
        if name and name not in seen:
            seen.add(name)
            branches.append({"name": name, "current": "*" in b})
    remote_raw = _run_git(["branch", "-r"]).split("\n")
    for b in remote_raw:
        name = b.strip().replace("personal/", "").replace("origin/", "")
        if name and name not in seen and "HEAD" not in name:
            seen.add(name)
            branches.append({"name": name, "current": False, "remote": True})

    # Project state files in branches dir
    ps_files = []
    ps_dir = PROJECT_DIR / "project-state" / "branches"
    if ps_dir.exists():
        for f in sorted(ps_dir.glob("*.json")):
            ps_files.append(f.stem.replace("-", "/", 1).replace("--", "/"))

    return {
        "branches": branches,
        "project_state_files": ps_files,
        "current": _run_git(["branch", "--show-current"]),
    }


@router.get("/api/v1/pm/sync-status")
async def pm_sync_status(branch: str | None = None):
    """Git sync status: ahead/behind/uncommitted for project and repo."""
    if not branch:
        branch = _run_git(["branch", "--show-current"])
    if not branch:
        return {"status": "no-branch", "branch": ""}

    remote = "personal"

    # Check if remote exists for this branch
    has_remote = False
    remote_ref = _run_git(["ls-remote", "--exit-code", remote, branch])
    has_remote = bool(remote_ref) or _run_git(["rev-parse", f"{remote}/{branch}"]) != ""

    # Count ahead/behind
    ahead = _run_git(["rev-list", "--count", f"{remote}/{branch}..HEAD"]) if has_remote else "0"
    behind = _run_git(["rev-list", "--count", f"HEAD..{remote}/{branch}"]) if has_remote else "0"

    # Uncommitted changes
    uncommitted_raw = _run_git(["status", "--porcelain"])
    uncommitted = len([l for l in uncommitted_raw.split("\n") if l.strip()]) if uncommitted_raw else 0

    # Last commits
    last_commit = _run_git(["log", "-1", "--oneline"])
    last_remote = _run_git(["log", "-1", "--oneline", f"{remote}/{branch}"]) if has_remote else ""

    # Determine status label
    try:
        a = int(ahead)
        b = int(behind)
    except ValueError:
        a = b = 0

    if not has_remote:
        status = "no-remote"
    elif uncommitted > 0:
        status = "uncommitted"
    elif a > 0 and b > 0:
        status = "diverged"
    elif a > 0:
        status = "ahead"
    elif b > 0:
        status = "behind"
    else:
        status = "synced"

    # Repo info
    repo_slug = _run_git(["remote", "get-url", remote]).replace("https://github.com/", "").replace(".git", "")

    return {
        "branch": branch,
        "remote": remote,
        "status": status,
        "ahead": a,
        "behind": b,
        "uncommitted": uncommitted,
        "has_remote": has_remote,
        "last_commit": last_commit,
        "last_remote_commit": last_remote,
        "repositorio": {
            "slug": repo_slug or "",
            "ahead": a,
            "behind": b,
            "uncommitted": uncommitted,
            "last_commit": last_commit,
            "has_remote": has_remote,
            "status": status,
        },
    }
