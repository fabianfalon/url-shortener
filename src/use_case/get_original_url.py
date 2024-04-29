from src.domain.url_repository import UrlRepository
from src.infrastructure.storage.memcached import CacheAbstract


class GetOriginalUrlUseCase:
    def __init__(self, url_repository: UrlRepository, cache: CacheAbstract):
        self.repository = url_repository
        self.cache = cache

    async def execute(self, short_url: str) -> str:
        value = self.cache.get(short_url)
        if value:
            return value
        url = await self.repository.get_by_short_url(short_url)
        self.cache.set(short_url, url.url)
        return url.url
