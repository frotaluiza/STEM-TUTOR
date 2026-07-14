import pytest
from deeptutor.services.sources import db


class TestSourceDB:
    @pytest.fixture(autouse=True)
    def setup_db(self, tmp_path):
        db._DB_PATH = str(tmp_path / "test_sources.db")
        db.init_db()
        db.seed_default_providers()

    def test_list_providers_default(self):
        providers = db.list_providers()
        assert len(providers) >= 7
        ids = [p.id for p in providers]
        assert "open_library" in ids
        assert "zona_eletrica" in ids
        assert "newton_braga" in ids

    def test_list_providers_by_area(self):
        eletrica = db.list_providers("eletrica")
        assert all("eletrica" in p.area_hints for p in eletrica)
        assert any(p.id == "zona_eletrica" for p in eletrica)

    def test_get_provider(self):
        p = db.get_provider("open_library")
        assert p is not None
        assert p.name == "Open Library"
        assert p.type == "api"

    def test_get_provider_not_found(self):
        assert db.get_provider("nonexistent") is None

    def test_project_sources_crud(self):
        db.add_project_source("test-project", "open_library")
        sources = db.list_project_sources("test-project")
        assert len(sources) == 1
        assert sources[0].provider_id == "open_library"

        db.add_project_source("test-project", "zona_eletrica")
        sources = db.list_project_sources("test-project")
        assert len(sources) == 2

        db.remove_project_source("test-project", "open_library")
        sources = db.list_project_sources("test-project")
        assert len(sources) == 1
        assert sources[0].provider_id == "zona_eletrica"

    def test_toggle_source(self):
        db.add_project_source("test-project", "open_library")
        db.toggle_project_source("test-project", "open_library", False)

        all_sources = db.list_project_sources("test-project", enabled_only=False)
        assert len(all_sources) == 1
        assert all_sources[0].enabled is False

        enabled = db.list_project_sources("test-project", enabled_only=True)
        assert len(enabled) == 0
