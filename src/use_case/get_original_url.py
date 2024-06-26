from typing import Optional

from src.domain.url_repository import UrlRepository
from src.infrastructure.storage.memcached import AbstractCacheRepository


class GetOriginalUrlUseCase:
    def __init__(self, url_repository: UrlRepository, cache: AbstractCacheRepository):
        self.repository = url_repository
        self.cache = cache

    async def execute(self, short_url: str) -> Optional[str]:
        cached_url = self.cache.get(short_url)
        if cached_url:
            return cached_url
        url = await self.repository.get_by_short_url(short_url)
        if not url:
            return None
        self.cache.set(short_url, url.url)
        return url.url
