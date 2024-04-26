from src.domain.url import Url
from src.domain.url_repository import UrlRepository


class GetOriginalUrlUseCase:
    def __init__(self, url_repository: UrlRepository):
        self.repository = url_repository

    async def execute(self, short_url: str) -> Url:
        url = await self.repository.get_by_short_url(short_url)
        return url
