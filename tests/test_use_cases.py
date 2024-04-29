from expects import expect, equal

from src.delivery.api.dependencies import get_shortener
from src.infrastructure.storage.in_memory import InMemoryRepository
from src.infrastructure.storage.memcached import InMemoryCacheRepository
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.url_shortener import CreateShortUrlUseCase


class TestShortenerUrlUseCases:
    async def test_create_new_short_url(self):
        original_url = "https://probando.com"
        use_case = CreateShortUrlUseCase(
            url_repository=InMemoryRepository(),
            shorter=get_shortener(),
            cache=InMemoryCacheRepository(),
        )
        url = await use_case.execute(original_url=original_url)
        expect(url).to(equal("6b86b273"))

    async def test_get_short_url(self):
        short_url = "6b86b273"
        use_case = GetOriginalUrlUseCase(
            url_repository=InMemoryRepository(),
            cache=InMemoryCacheRepository(),
        )
        url = await use_case.execute(short_url=short_url)
        expect(url).to(equal("https://probando.com"))
