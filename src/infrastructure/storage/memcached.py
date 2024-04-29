from abc import ABC, abstractmethod
from typing import Optional

import memcache


class AbstractCacheRepository(ABC):
    @abstractmethod
    def set(self, key: str, value: str) -> None: ...

    @abstractmethod
    def get(self, key: str) -> Optional[str]: ...


class MemcachedRepository(AbstractCacheRepository):
    def __init__(self) -> None:
        self.client = memcache.Client(["url-shortener-memcached:11211"], debug=0)
        super().__init__()

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value, time=3600)  # Cache for 1 hour

    def get(self, key: str) -> Optional[str]:
        value = self.client.get(key)
        return value


class InMemoryCacheRepository(AbstractCacheRepository):

    mapping = {}

    def set(self, key, value):
        self.mapping[key] = value

    def get(self, key):
        return self.mapping.get("key", None)
