from abc import ABC, abstractmethod
from typing import Optional

import memcache


class CacheAbstract(ABC):
    @abstractmethod
    def set(self, key: str, value: str) -> None: ...

    @abstractmethod
    def get(self, key: str) -> Optional[str]: ...


class MemcachedRepository(CacheAbstract):
    def __init__(self) -> None:
        self.client = memcache.Client(["url-shortener-memcached:11211"], debug=0)
        super().__init__()

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value, time=3600)  # Cache for 1 hour

    def get(self, key: str) -> Optional[str]:
        value = self.client.get(key)
        return value
