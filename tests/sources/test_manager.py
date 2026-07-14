import pytest
from deeptutor.services.sources.manager import SourceManager
from deeptutor.services.sources import db


class TestSourceManager:
    @pytest.fixture(autouse=True)
    def setup(self, tmp_path):
        db._DB_PATH = str(tmp_path / "test_manager.db")
        db.init_db()
        db.seed_default_providers()
        self.manager = SourceManager()

    def test_list_providers(self):
        providers = self.manager.list_providers()
        assert len(providers) >= 7

    def test_project_sources_flow(self):
        self.manager.add_source("proj-a", "open_library")
        self.manager.add_source("proj-a", "zona_eletrica")
        sources = self.manager.list_project_sources("proj-a")
        assert len(sources) == 2

        self.manager.toggle_source("proj-a", "open_library", False)
        enabled = self.manager.list_project_sources("proj-a", enabled_only=True)
        assert len(enabled) == 1
        assert enabled[0].provider_id == "zona_eletrica"

        self.manager.remove_source("proj-a", "zona_eletrica")
        remaining = self.manager.list_project_sources("proj-a")
        assert len(remaining) == 0

    def test_suggest_sources(self):
        suggestions = self.manager.suggest_sources("eletrica")
        ids = [p.id for p in suggestions]
        assert "open_library" in ids
        assert "zona_eletrica" in ids

    def test_apply_suggestions(self):
        applied = self.manager.apply_suggestions("proj-b", "eletrica")
        assert len(applied) > 0
        sources = self.manager.list_project_sources("proj-b")
        assert len(sources) == len(applied)

    def test_get_active_providers(self):
        self.manager.add_source("proj-c", "open_library")
        self.manager.add_source("proj-c", "newton_braga")
        self.manager.toggle_source("proj-c", "newton_braga", False)
        active = self.manager.get_active_providers("proj-c")
        assert "open_library" in active
        assert "newton_braga" not in active
