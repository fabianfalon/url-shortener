from src.domain.url import Url
from src.domain.url_repository import UrlRepository
from src.infrastructure.shortener.shortener import URLShortener
from src.infrastructure.storage.memcached import CacheAbstract


class UrlShortenerUseCase:
    def __init__(self, url_repository: UrlRepository, shorter: URLShortener, cache: CacheAbstract):
        self.repository = url_repository
        self.shorter = shorter
        self.cache = cache

    async def execute(self, original_url: str) -> str:
        cached_url = self.cache.get(original_url)
        if cached_url:
            return cached_url

        exists = await self.repository.get_by_original_url(original_url)
        if exists:
            self.cache.set(original_url, exists.short_url)
            return exists.short_url

        count = await self.repository.find_all()
        _count = len(count) + 1
        short_url = self.shorter.shorten_url(_count)
        url = Url(id=_count, url=original_url, short_url=short_url)
        await self.repository.save(url)
        self.cache.set(original_url, url.short_url)
        return url.short_url
