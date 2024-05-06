from fastapi import Depends

from src.domain.url_repository import UrlRepository
from src.infrastructure.shortener.shortener import URLShortener, URLShortenerSHA2
from src.infrastructure.storage.memcached import AbstractCacheRepository, MemcachedRepository
from src.infrastructure.storage.mongo import MongoRepository
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.create_short_url import CreateShortUrlUseCase


async def get_shortener() -> URLShortener:
    return URLShortenerSHA2()


async def get_url_mongo_repository() -> UrlRepository:
    return MongoRepository()


async def get_url_cache_repository() -> AbstractCacheRepository:
    return MemcachedRepository()


async def get_url_shortener_use_case(
    url_repository: UrlRepository = Depends(get_url_mongo_repository),
    shorter: URLShortener = Depends(get_shortener),
    cache: AbstractCacheRepository = Depends(get_url_cache_repository),
) -> CreateShortUrlUseCase:
    return CreateShortUrlUseCase(url_repository=url_repository, shorter=shorter, cache=cache)


async def get_original_url_use_case(
    url_repository: UrlRepository = Depends(get_url_mongo_repository),
    cache: AbstractCacheRepository = Depends(get_url_cache_repository),
) -> GetOriginalUrlUseCase:
    return GetOriginalUrlUseCase(url_repository=url_repository, cache=cache)
