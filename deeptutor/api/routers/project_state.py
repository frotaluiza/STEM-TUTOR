import json
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

router = APIRouter(tags=["project"])

PROJECT_DIR = Path(__file__).resolve().parents[3]  # AI TUTOR/
STATE_DIR = PROJECT_DIR / "project-state"
CLASSIFICATION_FILE = PROJECT_DIR / "kb" / "sessoes" / "classification.json"


def _resolve_state_file(slug: str | None) -> Path | None:
    """Resolve project state file by slug. Falls back to ai-stem-tutor if no slug given."""
    target = slug or "ai-stem-tutor"
    path = STATE_DIR / f"{target}.json"
    if path.exists():
        return path
    return None


def _read_json(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (json.JSONDecodeError, OSError):
        return None


class GraphNode(BaseModel):
    id: str
    label: str
    type: str = "generic"
    subtitle: str = ""
    color: str = "#6b7280"


class GraphEdge(BaseModel):
    source: str
    target: str
    label: str = ""


class ProjectMindMap(BaseModel):
    nodes: list[GraphNode] = []
    edges: list[GraphEdge] = []
    project: str = ""
    branch: str = ""
    last_commit: str = ""
    last_updated: str = ""


class FocusPanel(BaseModel):
    project: str = ""
    branch: str = ""
    last_commit: str = ""
    last_session: str = ""
    next_steps: list[str] = []
    pending_tasks: list[dict] = []
    drift_warning: str = ""


@router.get("/focus", response_model=FocusPanel)
async def get_focus_panel(slug: str | None = Query(None, description="Project slug")):
    state_file = _resolve_state_file(slug)
    if not state_file:
        return FocusPanel()

    raw = _read_json(state_file)
    if not raw:
        return FocusPanel()

    sessions = raw.get("sessions", [])
    last_session = sessions[-1]["title"] if sessions else ""

    return FocusPanel(
        project=raw.get("project", ""),
        branch=raw.get("branch", ""),
        last_commit=raw.get("last_commit", ""),
        last_session=last_session,
        next_steps=raw.get("todos", [])[:5],
        pending_tasks=[],
    )


@router.get("/state", response_model=ProjectMindMap)
async def get_project_state(slug: str | None = Query(None, description="Project slug")):
    state_file = _resolve_state_file(slug)
    if not state_file:
        raise HTTPException(status_code=404, detail="No project state found")

    raw = _read_json(state_file)
    if not raw:
        raise HTTPException(status_code=404, detail="No project state found")

    return _build_mind_map(raw)


@router.get("/state/raw")
async def get_project_state_raw(slug: str | None = Query(None, description="Project slug")):
    state_file = _resolve_state_file(slug)
    if not state_file:
        raise HTTPException(status_code=404, detail="No project state found")

    raw = _read_json(state_file)
    if not raw:
        raise HTTPException(status_code=404, detail="No project state found")
    return raw


def _build_mind_map(data: dict) -> ProjectMindMap:
    nodes: list[GraphNode] = []
    edges: list[GraphEdge] = []

    # Root node — the project itself
    project_id = "project-root"
    nodes.append(
        GraphNode(
            id=project_id,
            label=data.get("project", "Project"),
            type="project",
            subtitle=f"branch: {data.get('branch', '?')}",
            color="#6366f1",
        )
    )

    # Branch node
    branch = data.get("branch", "unknown")
    branch_id = "branch-current"
    nodes.append(
        GraphNode(
            id=branch_id,
            label=branch,
            type="branch",
            subtitle=data.get("last_commit", "")[:60],
            color="#8b5cf6",
        )
    )
    edges.append(GraphEdge(source=project_id, target=branch_id, label="on"))

    # Git log — last 5 commits as nodes
    git_log = data.get("git_log", "")
    commits = [ln.strip() for ln in git_log.split("\n") if ln.strip()][:5]
    for i, commit in enumerate(commits):
        cid = f"commit-{i}"
        hash_part = commit.split()[0][:8]
        msg_part = commit[len(hash_part) + 1:][:50]
        nodes.append(
            GraphNode(
                id=cid,
                label=msg_part,
                type="commit",
                subtitle=hash_part,
                color="#22c55e",
            )
        )
        edges.append(GraphEdge(source=branch_id, target=cid, label="commit"))

    # Sessions
    sessions = data.get("sessions", [])[:5]
    for i, sess in enumerate(sessions):
        sid = f"session-{i}"
        nodes.append(
            GraphNode(
                id=sid,
                label=sess.get("title", "Session")[:50],
                type="session",
                subtitle=f"{sess.get('date', '?')} ({sess.get('id', '?')})",
                color="#3b82f6",
            )
        )
        edges.append(GraphEdge(source=project_id, target=sid, label="session"))

        # Decisions within this session
        for j, dec in enumerate(sess.get("decisions", [])):
            did = f"decision-{i}-{j}"
            nodes.append(
                GraphNode(
                    id=did,
                    label=dec[:60],
                    type="decision",
                    color="#f59e0b",
                )
            )
            edges.append(GraphEdge(source=sid, target=did))

        # Files modified in this session
        for j, fname in enumerate(sess.get("files", [])):
            fid = f"file-{i}-{j}"
            nodes.append(
                GraphNode(
                    id=fid,
                    label=Path(fname).name,
                    type="file",
                    subtitle=fname[:40],
                    color="#10b981",
                )
            )
            edges.append(GraphEdge(source=sid, target=fid))

    # Global decisions (accumulated)
    decisions = data.get("decisions", [])
    for i, dec in enumerate(decisions):
        did = f"decision-global-{i}"
        nodes.append(
            GraphNode(
                id=did,
                label=dec[:60],
                type="decision",
                color="#f59e0b",
            )
        )
        edges.append(GraphEdge(source=project_id, target=did, label="decision"))

    # Todos / next steps
    todos = data.get("todos", [])
    for i, todo in enumerate(todos[:10]):
        tid = f"todo-{i}"
        nodes.append(
            GraphNode(
                id=tid,
                label=todo[:60],
                type="todo",
                color="#ef4444",
            )
        )
        edges.append(GraphEdge(source=project_id, target=tid, label="next"))

    # Issues
    issues = data.get("issues", [])
    for i, issue in enumerate(issues):
        iid = f"issue-{i}"
        nodes.append(
            GraphNode(
                id=iid,
                label=issue[:60],
                type="issue",
                color="#dc2626",
            )
        )
        edges.append(GraphEdge(source=project_id, target=iid, label="issue"))

    return ProjectMindMap(
        nodes=nodes,
        edges=edges,
        project=data.get("project", ""),
        branch=data.get("branch", ""),
        last_commit=data.get("last_commit", ""),
        last_updated=data.get("last_updated", ""),
    )
