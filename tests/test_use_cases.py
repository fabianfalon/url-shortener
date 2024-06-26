from expects import expect, equal

from src.infrastructure.shortener.shortener import URLShortenerSHA2
from src.infrastructure.storage.in_memory import InMemoryRepository
from src.infrastructure.storage.memcached import InMemoryCacheRepository
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.create_short_url import CreateShortUrlUseCase
from tests.conftest import MOCK_ORIGINAL_URL, MOCK_SHORT_URL


class TestShortenerUrlUseCases:
    async def test_create_new_short_url(self):
        use_case = CreateShortUrlUseCase(
            url_repository=InMemoryRepository(),
            shorter=URLShortenerSHA2(),
            cache=InMemoryCacheRepository(),
        )
        url = await use_case.execute(original_url=MOCK_ORIGINAL_URL)
        expect(url).to(equal(MOCK_SHORT_URL))

    async def test_get_short_url(self):
        use_case = GetOriginalUrlUseCase(
            url_repository=InMemoryRepository(),
            cache=InMemoryCacheRepository(),
        )
        url = await use_case.execute(short_url=MOCK_SHORT_URL)
        expect(url).to(equal(MOCK_ORIGINAL_URL))
