"""Unified mind map router — merges project state + mastery map data
into a single graph that can be rendered and edited from any page."""

from __future__ import annotations

import json
from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/mindmap", tags=["mindmap"])

PROJECT_DIR = Path(__file__).resolve().parents[3]
STATE_DIR = PROJECT_DIR / "project-state"


class MindMapNode(BaseModel):
    id: str
    type: str = "generic"
    label: str = ""
    subtitle: str = ""
    color: str = "#6b7280"
    status: str = ""
    mastery: float = 0.0


class MindMapEdge(BaseModel):
    id: str
    source: str
    target: str
    label: str = ""


class MindMapMeta(BaseModel):
    project: str = ""
    branch: str = ""
    last_commit: str = ""
    last_updated: str = ""
    path_id: str = ""


class MindMapResponse(BaseModel):
    nodes: list[MindMapNode] = []
    edges: list[MindMapEdge] = []
    meta: MindMapMeta = MindMapMeta()


@router.get("/{path_id:path}", response_model=MindMapResponse)
async def get_mind_map(path_id: str):
    state = _load_project_state()
    return _build_mind_map(state, path_id)


@router.post("/{path_id:path}")
async def save_mind_map(path_id: str, data: MindMapResponse):
    state_file = STATE_DIR / f"{_slug_from_path(path_id)}.json"
    payload = {
        "nodes": [n.model_dump() for n in data.nodes],
        "edges": [e.model_dump() for e in data.edges],
        "meta": data.meta.model_dump(),
        "path_id": path_id,
    }
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    return {"status": "saved", "file": str(state_file)}


def _slug_from_path(path_id: str) -> str:
    return path_id.strip("/").replace("/", "-").replace("\\", "-") or "default"


def _load_project_state() -> dict:
    state_file = STATE_DIR / "ai-stem-tutor.json"
    if state_file.exists():
        return json.loads(state_file.read_text(encoding="utf-8-sig"))
    return {}


def _build_mind_map(state: dict, path_id: str) -> MindMapResponse:
    nodes: list[MindMapNode] = []
    edges: list[MindMapEdge] = []
    edge_counter = [0]

    def eid() -> str:
        edge_counter[0] += 1
        return f"e-{edge_counter[0]}"

    project = state.get("project", path_id)
    branch = state.get("branch", "unknown")
    project_id = "root"

    nodes.append(MindMapNode(
        id=project_id, type="project", label=project,
        subtitle=f"branch: {branch}", color="#6366f1",
    ))

    # Branch
    branch_id = "branch"
    nodes.append(MindMapNode(
        id=branch_id, type="branch", label=branch,
        subtitle=state.get("last_commit", "")[:60],
        color="#8b5cf6",
    ))
    edges.append(MindMapEdge(id=eid(), source=project_id, target=branch_id, label="on"))

    # Commits
    commits = [ln.strip() for ln in state.get("git_log", "").split("\n") if ln.strip()][:5]
    for i, c in enumerate(commits):
        cid = f"commit-{i}"
        parts = c.split(None, 1)
        nodes.append(MindMapNode(
            id=cid, type="commit", label=(parts[1] if len(parts) > 1 else c)[:50],
            subtitle=parts[0][:8] if parts else "", color="#22c55e",
        ))
        edges.append(MindMapEdge(id=eid(), source=branch_id, target=cid, label="commit"))

    # Sessions
    for i, sess in enumerate(state.get("sessions", [])[:5]):
        sid = f"session-{i}"
        nodes.append(MindMapNode(
            id=sid, type="session", label=sess.get("title", "")[:50],
            subtitle=f"{sess.get('date', '?')} ({sess.get('id', '?')})",
            color="#3b82f6",
        ))
        edges.append(MindMapEdge(id=eid(), source=project_id, target=sid, label="session"))

        for j, dec in enumerate(sess.get("decisions", [])[:3]):
            did = f"decision-{i}-{j}"
            nodes.append(MindMapNode(
                id=did, type="decision", label=dec[:60], color="#f59e0b",
            ))
            edges.append(MindMapEdge(id=eid(), source=sid, target=did))

    # Global decisions
    for i, dec in enumerate(state.get("decisions", [])[:5]):
        did = f"d-{i}"
        nodes.append(MindMapNode(id=did, type="decision", label=dec[:60], color="#f59e0b"))
        edges.append(MindMapEdge(id=eid(), source=project_id, target=did, label="decision"))

    # Todos
    for i, todo in enumerate(state.get("todos", [])[:8]):
        tid = f"todo-{i}"
        nodes.append(MindMapNode(id=tid, type="todo", label=todo[:60], color="#ef4444"))
        edges.append(MindMapEdge(id=eid(), source=project_id, target=tid, label="next"))

    return MindMapResponse(
        nodes=nodes, edges=edges,
        meta=MindMapMeta(
            project=project, branch=branch,
            last_commit=state.get("last_commit", ""),
            last_updated=state.get("last_updated", ""),
            path_id=path_id,
        ),
    )
