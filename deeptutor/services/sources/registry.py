from typing import Optional, Type

from deeptutor.services.sources.providers.base import BaseSourceProvider


_registry: dict[str, Type[BaseSourceProvider]] = {}


def register_provider_class(provider_id: str):
    def decorator(cls: Type[BaseSourceProvider]) -> Type[BaseSourceProvider]:
        _registry[provider_id] = cls
        return cls
    return decorator


def get_provider_class(provider_id: str) -> Optional[Type[BaseSourceProvider]]:
    return _registry.get(provider_id)


def list_provider_classes() -> list[str]:
    return list(_registry.keys())
