from src.domain.url import Url
from src.domain.url_repository import UrlRepository
from src.infrastructure.shortener.shortener import URLShortener


class UrlShortenerUseCase:
    def __init__(self, url_repository: UrlRepository, shorter: URLShortener):
        self.repository = url_repository
        self.shorter = shorter

    async def execute(self, original_url: str) -> Url:
        exists = await self.repository.get_by_original_url(original_url)
        count = await self.repository.find_all()
        _count = len(count) + 1
        if exists:
            return exists
        short_url = self.shorter.shorten_url(_count)
        url = Url(id=_count, url=original_url, short_url=short_url)
        await self.repository.save(url)
        return url
