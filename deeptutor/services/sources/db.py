import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

from deeptutor.services.sources.models import ProjectSource, SourceProvider, ProviderStatus


_DB_PATH: Optional[str] = None


def _get_db() -> sqlite3.Connection:
    global _DB_PATH
    if _DB_PATH is None:
        _DB_PATH = str(Path(__file__).resolve().parents[4] / "data" / "sources.db")
    conn = sqlite3.connect(_DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db() -> None:
    conn = _get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS source_providers (
            id              TEXT PRIMARY KEY,
            name            TEXT NOT NULL,
            description     TEXT DEFAULT '',
            type            TEXT NOT NULL CHECK(type IN ('api','scraper','deep_search','database')),
            status          TEXT DEFAULT 'active' CHECK(status IN ('active','deprecated','experimental')),
            requires_api_key INTEGER DEFAULT 0,
            area_hints      TEXT DEFAULT '[]',
            icon_url        TEXT DEFAULT '',
            base_url        TEXT DEFAULT '',
            docs_url        TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS project_sources (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            project_slug    TEXT NOT NULL,
            provider_id     TEXT NOT NULL,
            enabled         INTEGER DEFAULT 1,
            config          TEXT DEFAULT '{}',
            created_at      TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (provider_id) REFERENCES source_providers(id),
            UNIQUE(project_slug, provider_id)
        );
    """)
    conn.commit()
    conn.close()


def seed_default_providers() -> None:
    providers = [
        ("open_library", "Open Library", "Catálogo aberto de livros", "api", "active", 0,
         '["engenharia","academico","eletrica"]', "", "https://openlibrary.org", "https://openlibrary.org/developers/api"),
        ("zona_eletrica", "Zona da Elétrica", "Portal BR de engenharia elétrica", "scraper", "active", 0,
         '["engenharia","eletrica"]', "", "https://zonadaeletrica.com.br", ""),
        ("newton_braga", "Inst. Newton C. Braga", "Eletrônica + projetos práticos", "scraper", "active", 0,
         '["engenharia","eletrica","eletronica"]', "", "https://newtoncbraga.com.br", ""),
        ("mundo_eletrica", "Mundo da Elétrica", "Elétrica residencial/industrial", "scraper", "active", 0,
         '["engenharia","eletrica"]', "", "https://mundodaeletrica.com.br", ""),
        ("embarcados", "Embarcados", "Sistemas embarcados e IoT", "scraper", "active", 0,
         '["engenharia","eletronica","iot"]', "", "https://embarcados.com.br", ""),
        ("google_books", "Google Books", "Google Books API", "api", "active", 1,
         '["academico","geral"]', "", "https://books.google.com", "https://developers.google.com/books"),
        ("perplexity_deep", "Perplexity DeepSearch", "AI-powered deep research", "deep_search", "active", 1,
         '["academico","geral","engenharia"]', "", "https://perplexity.ai", ""),
    ]
    conn = _get_db()
    for p in providers:
        conn.execute("""
            INSERT OR IGNORE INTO source_providers
            (id, name, description, type, status, requires_api_key, area_hints, icon_url, base_url, docs_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, p)
    conn.commit()
    conn.close()


def list_providers(area: Optional[str] = None) -> list[SourceProvider]:
    conn = _get_db()
    if area:
        rows = conn.execute(
            "SELECT * FROM source_providers WHERE area_hints LIKE ? ORDER BY name",
            (f"%{area}%",)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM source_providers ORDER BY name").fetchall()
    conn.close()
    return [_row_to_provider(r) for r in rows]


def get_provider(provider_id: str) -> Optional[SourceProvider]:
    conn = _get_db()
    row = conn.execute("SELECT * FROM source_providers WHERE id = ?", (provider_id,)).fetchone()
    conn.close()
    return _row_to_provider(row) if row else None


def _row_to_provider(row: sqlite3.Row) -> SourceProvider:
    return SourceProvider(
        id=row["id"], name=row["name"], description=row["description"],
        type=row["type"], status=ProviderStatus(row["status"]),
        requires_api_key=bool(row["requires_api_key"]),
        area_hints=json.loads(row["area_hints"]) if row["area_hints"] else [],
        icon_url=row["icon_url"] or "", base_url=row["base_url"] or "",
        docs_url=row["docs_url"] or "",
    )


def list_project_sources(project_slug: str, enabled_only: bool = True) -> list[ProjectSource]:
    conn = _get_db()
    query = "SELECT * FROM project_sources WHERE project_slug = ?"
    params: list = [project_slug]
    if enabled_only:
        query += " AND enabled = 1"
    query += " ORDER BY provider_id"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [_row_to_project_source(r) for r in rows]


def add_project_source(project_slug: str, provider_id: str, config: Optional[dict] = None) -> ProjectSource:
    conn = _get_db()
    config_json = json.dumps(config or {})
    conn.execute(
        "INSERT OR IGNORE INTO project_sources (project_slug, provider_id, config) VALUES (?, ?, ?)",
        (project_slug, provider_id, config_json),
    )
    conn.commit()
    row = conn.execute(
        "SELECT * FROM project_sources WHERE project_slug = ? AND provider_id = ?",
        (project_slug, provider_id),
    ).fetchone()
    conn.close()
    return _row_to_project_source(row)


def remove_project_source(project_slug: str, provider_id: str) -> None:
    conn = _get_db()
    conn.execute(
        "DELETE FROM project_sources WHERE project_slug = ? AND provider_id = ?",
        (project_slug, provider_id),
    )
    conn.commit()
    conn.close()


def toggle_project_source(project_slug: str, provider_id: str, enabled: bool) -> None:
    conn = _get_db()
    conn.execute(
        "UPDATE project_sources SET enabled = ? WHERE project_slug = ? AND provider_id = ?",
        (int(enabled), project_slug, provider_id),
    )
    conn.commit()
    conn.close()


def _row_to_project_source(row: sqlite3.Row) -> ProjectSource:
    return ProjectSource(
        id=row["id"], project_slug=row["project_slug"],
        provider_id=row["provider_id"], enabled=bool(row["enabled"]),
        config=json.loads(row["config"]) if row["config"] else {},
        created_at=datetime.fromisoformat(row["created_at"]) if row["created_at"] else datetime.now(),
    )
