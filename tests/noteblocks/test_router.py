"""Testes dos endpoints REST do NoteBlocks — Render-first Verification.

Padrao:
  1. Renderizacao primeiro: verificar SE o endpoint responde (status code)
  2. Comportamento esperado: verificar o conteudo da resposta
  3. Cobertura de estados: sucesso, nao encontrado, criacao
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from deeptutor.api.main import app
from deeptutor.noteblocks.models import Block, BlockType, Note

client = TestClient(app)


def test_list_notes_empty() -> None:
    """Renderizacao: endpoint GET /api/v1/noteblocks/notes existe e retorna lista."""
    response = client.get("/api/v1/noteblocks/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_and_get_note() -> None:
    """Renderizacao: POST cria nota. Comportamento: GET retorna a nota criada."""
    note_data = {
        "id": "test-router-1",
        "title": "Nota de Teste",
        "blocks": [
            {"id": "b1", "type": "text", "content": "Hello"},
            {"id": "b2", "type": "ask", "content": "O que?"},
        ],
        "tags": ["test"],
    }
    create_resp = client.post("/api/v1/noteblocks/notes", json=note_data)
    assert create_resp.status_code == 201

    get_resp = client.get("/api/v1/noteblocks/notes/test-router-1")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["title"] == "Nota de Teste"
    assert len(data["blocks"]) == 2
    assert data["blocks"][0]["type"] == "text"


def test_get_note_not_found() -> None:
    """Cobertura de erro: GET de nota inexistente retorna 404."""
    response = client.get("/api/v1/noteblocks/notes/nao-existe")
    assert response.status_code == 404


def test_update_note() -> None:
    """Comportamento: PUT atualiza nota existente."""
    note = {
        "id": "test-update-1",
        "title": "Original",
        "blocks": [{"id": "b1", "type": "text", "content": "Original"}],
    }
    client.post("/api/v1/noteblocks/notes", json=note)

    updated = {
        "id": "test-update-1",
        "title": "Atualizada",
        "blocks": [{"id": "b1", "type": "text", "content": "Nova versao"}],
    }
    resp = client.put("/api/v1/noteblocks/notes/test-update-1", json=updated)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Atualizada"


def test_delete_note() -> None:
    """Comportamento: DELETE remove nota."""
    note = {
        "id": "test-delete-1",
        "title": "Para deletar",
        "blocks": [],
    }
    client.post("/api/v1/noteblocks/notes", json=note)
    del_resp = client.delete("/api/v1/noteblocks/notes/test-delete-1")
    assert del_resp.status_code == 204

    get_resp = client.get("/api/v1/noteblocks/notes/test-delete-1")
    assert get_resp.status_code == 404


def test_leveling_endpoint() -> None:
    """Renderizacao: endpoint de leveling existe e retorna pergunta."""
    resp = client.get("/api/v1/noteblocks/agent/leveling/start?topic=derivadas")
    assert resp.status_code == 200
    data = resp.json()
    assert "question" in data
    assert "options" in data
    assert len(data["options"]) >= 4
    assert data["options"][0]["id"] == "iniciante"


def test_leveling_answer() -> None:
    """Comportamento: registrar nivel do aluno."""
    note = {
        "id": "test-level-1",
        "title": "Leveling",
        "blocks": [{"id": "b1", "type": "text", "content": "test"}],
    }
    client.post("/api/v1/noteblocks/notes", json=note)
    resp = client.post(
        "/api/v1/noteblocks/agent/leveling/answer",
        json={"note_id": "test-level-1", "level": "intermediario", "topic": "derivadas"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["level"] == "intermediario"
    assert "prompt" in data


def test_bkt_record() -> None:
    """Renderizacao: BKT endpoint existe e registra resposta."""
    resp = client.post(
        "/api/v1/noteblocks/agent/bkt/record",
        json={"student_id": "test-student", "skill": "derivadas", "correct": True},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["skill"] == "derivadas"
    assert data["correct"] is True
    assert "mastery" in data


def test_bkt_status() -> None:
    """Comportamento: BKT status retorna mastery do aluno."""
    resp = client.post(
        "/api/v1/noteblocks/agent/bkt/status",
        json={"student_id": "test-student"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "mastery" in data
    assert "weak_skills" in data


def test_runner_start_recreational() -> None:
    """Renderizacao: Runner modo recreativo retorna frases sem vidas limitadas."""
    resp = client.post(
        "/api/v1/noteblocks/runner/start",
        json={"student_id": "test-runner", "skill": "derivadas", "mode": "recreational"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "phrases" in data
    assert len(data["phrases"]) > 0
    assert "color" in data["phrases"][0]
    assert "flag" in data["phrases"][0]
    assert data["lives"] == 999


def test_runner_start_test_mode() -> None:
    """Comportamento: Runner modo teste comeca com 3 vidas."""
    resp = client.post(
        "/api/v1/noteblocks/runner/start",
        json={"student_id": "test-runner-2", "skill": "derivadas", "mode": "test"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["lives"] == 3


def test_subtopic_test_start() -> None:
    """Renderizacao: Subtopic test endpoint existe."""
    resp = client.post(
        "/api/v1/noteblocks/subtopic-test/start",
        json={"student_id": "test-sub", "skill": "derivadas"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "theoretical" in data
    assert "practical" in data
    assert data["threshold"] == 0.9


def test_terminal_suggest() -> None:
    """Renderizacao: terminal-suggest endpoint existe e sugere comando."""
    resp = client.post(
        "/api/v1/noteblocks/agent/terminal-suggest",
        json={"prompt": "list files", "context": ""},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "suggested_command" in data
    assert "explanation" in data


def test_sync_to_notion_no_token() -> None:
    """Cobertura de erro: sync sem token retorna erro."""
    note = {
        "id": "test-sync-1",
        "title": "Sync Test",
        "blocks": [{"id": "b1", "type": "text", "content": "test"}],
    }
    client.post("/api/v1/noteblocks/notes", json=note)
    resp = client.post("/api/v1/noteblocks/agent/sync-to-notion/test-sync-1")
    assert resp.status_code == 200
    data = resp.json()
    assert "error" in data
