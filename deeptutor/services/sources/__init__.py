from deeptutor.services.sources.db import init_db, seed_default_providers


def init_sources_db() -> None:
    init_db()
    seed_default_providers()
