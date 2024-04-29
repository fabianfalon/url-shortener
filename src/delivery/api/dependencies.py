from src.domain.url_repository import UrlRepository
from src.infrastructure.shortener.shortener import URLShortener, URLShortenerSHA2
from src.infrastructure.storage.in_memory import InMemoryRepository
from src.infrastructure.storage.memcached import CacheAbstract, MemcachedRepository
from src.infrastructure.storage.mongo import MongoRepository
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.url_shortener import UrlShortenerUseCase


def get_url_repository() -> UrlRepository:
    return InMemoryRepository()


def get_shortener() -> URLShortener:
    return URLShortenerSHA2()


def get_url_mongo_repository() -> UrlRepository:
    return MongoRepository()


def get_url_cache_repository() -> CacheAbstract:
    return MemcachedRepository()


def get_url_shortener_use_case() -> UrlShortenerUseCase:
    return UrlShortenerUseCase(
        url_repository=get_url_mongo_repository(), shorter=get_shortener(), cache=get_url_cache_repository()
    )


def get_original_url_use_case() -> GetOriginalUrlUseCase:
    return GetOriginalUrlUseCase(url_repository=get_url_mongo_repository(), cache=get_url_cache_repository())
