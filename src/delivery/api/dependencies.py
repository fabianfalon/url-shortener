from src.domain.url_repository import UrlRepository
from src.infrastructure.shortener.shortener import URLShortener, URLShortenerSHA2
from src.infrastructure.storage.memcached import AbstractCacheRepository, MemcachedRepository
from src.infrastructure.storage.mongo import MongoRepository
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.url_shortener import CreateShortUrlUseCase


def get_shortener() -> URLShortener:
    return URLShortenerSHA2()


def get_url_mongo_repository() -> UrlRepository:
    return MongoRepository()


def get_url_cache_repository() -> AbstractCacheRepository:
    return MemcachedRepository()


def get_url_shortener_use_case() -> CreateShortUrlUseCase:
    return CreateShortUrlUseCase(
        url_repository=get_url_mongo_repository(), shorter=get_shortener(), cache=get_url_cache_repository()
    )


def get_original_url_use_case() -> GetOriginalUrlUseCase:
    return GetOriginalUrlUseCase(url_repository=get_url_mongo_repository(), cache=get_url_cache_repository())
