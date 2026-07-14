AREA_SUGGESTIONS: dict[str, dict] = {
    "eletrica": {
        "priority": ["open_library", "zona_eletrica", "newton_braga"],
        "optional": ["mundo_eletrica", "embarcados", "google_books", "perplexity_deep"],
        "explain": "Projetos de engenharia elétrica — foco em livros técnicos, exercícios resolvidos, circuitos e projetos práticos."
    },
    "eletronica": {
        "priority": ["newton_braga", "embarcados", "open_library"],
        "optional": ["perplexity_deep", "google_books"],
        "explain": "Projetos de eletrônica — circuitos, componentes, sistemas embarcados."
    },
    "ia": {
        "priority": ["perplexity_deep", "google_books"],
        "optional": ["embarcados", "open_library"],
        "explain": "Projetos de IA — papers, deep research, referências técnicas."
    },
    "academico": {
        "priority": ["open_library", "google_books", "perplexity_deep"],
        "optional": [],
        "explain": "Projetos acadêmicos — livros, papers, pesquisa aprofundada."
    },
    "musica": {
        "priority": [],
        "optional": [],
        "explain": "Projetos musicais — fontes específicas serão adicionadas futuramente."
    },
    "geral": {
        "priority": ["open_library", "google_books"],
        "optional": ["perplexity_deep"],
        "explain": "Projetos gerais — fontes universais."
    },
}


def suggest_for_area(area: str) -> list[str]:
    config = AREA_SUGGESTIONS.get(area, AREA_SUGGESTIONS["geral"])
    return config["priority"] + config["optional"]


def get_suggestion_info(area: str) -> dict:
    return AREA_SUGGESTIONS.get(area, AREA_SUGGESTIONS["geral"])
