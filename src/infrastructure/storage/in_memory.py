from typing import List, Optional

from src.domain.url import Url
from src.domain.url_repository import UrlRepository


class InMemoryRepository(UrlRepository):
    def delete(self, course_id: str) -> None:
        print("mock delete")

    _urls: List[Url] = []

    async def save(self, url: Url) -> None:
        url.id = len(self._urls) + 1
        self._urls.append(url)

    async def find_one(self, url_id: str) -> Optional[Url]:
        return next(filter(lambda x: (x.id == url_id), self._urls), None)

    async def find_all(self) -> List[Url]:
        return self._urls

    async def get_by_original_url(self, url) -> Optional[Url]:
        return next(filter(lambda x: (x.url == url), self._urls), None)

    async def get_by_short_url(self, url) -> Optional[Url]:
        return next(filter(lambda x: (x.short_url == url), self._urls), None)

    def clear(self):
        self._urls = []
