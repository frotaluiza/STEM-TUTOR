from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class ProviderType(str, Enum):
    api = "api"
    scraper = "scraper"
    deep_search = "deep_search"
    database = "database"


class ProviderStatus(str, Enum):
    active = "active"
    deprecated = "deprecated"
    experimental = "experimental"


@dataclass
class SourceProvider:
    id: str
    name: str
    description: str
    type: ProviderType
    status: ProviderStatus = ProviderStatus.active
    requires_api_key: bool = False
    area_hints: list[str] = field(default_factory=list)
    icon_url: str = ""
    base_url: str = ""
    docs_url: str = ""


@dataclass
class ProjectSource:
    id: int = 0
    project_slug: str = ""
    provider_id: str = ""
    enabled: bool = True
    config: dict = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
