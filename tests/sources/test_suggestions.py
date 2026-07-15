from deeptutor.services.sources.suggestions import suggest_for_area, get_suggestion_info


class TestSuggestions:
    def test_suggest_for_area_eletrica(self):
        ids = suggest_for_area("eletrica")
        assert "open_library" in ids
        assert "zona_eletrica" in ids
        assert "newton_braga" in ids

    def test_suggest_for_area_unknown_falls_back_to_geral(self):
        ids = suggest_for_area("nonexistent")
        assert "open_library" in ids
        assert "google_books" in ids

    def test_suggest_for_area_musica_empty(self):
        ids = suggest_for_area("musica")
        assert ids == []

    def test_get_suggestion_info(self):
        info = get_suggestion_info("eletrica")
        assert "explain" in info
        assert "engenharia elétrica" in info["explain"]
