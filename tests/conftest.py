import pytest

from src.infrastructure.storage.in_memory import InMemoryRepository
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.url_shortener import CreateShortUrlUseCase
from src.delivery.api.dependencies import get_shortener
from src.infrastructure.storage.memcached import InMemoryCacheRepository


@pytest.fixture()
def mock_create_short_url_use_case(mocker):
    use_case = CreateShortUrlUseCase(
        url_repository=InMemoryRepository(), shorter=get_shortener(), cache=InMemoryCacheRepository()
    )
    mocker.patch("src.delivery.api.dependencies.get_url_shortener_use_case", return_value=use_case)
    return use_case


@pytest.fixture
def mock_get_original_url_use_case(mocker):
    use_case = GetOriginalUrlUseCase(url_repository=InMemoryRepository(), cache=InMemoryCacheRepository())
    mocker.patch("src.delivery.api.dependencies.get_original_url_use_case", return_value=use_case)
    return use_case
