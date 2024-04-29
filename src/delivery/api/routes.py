from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as http_status

from src.delivery.api.dependencies import (
    get_original_url_use_case,
    get_url_cache_repository,
    get_url_shortener_use_case,
)
from src.infrastructure.dto.url_dto import UrlPayloadIn, UrlResponseOut

# Router Config
router = APIRouter(tags=["url shortener"])


@router.post(
    "/shortener",
    summary="Make a short url",
    status_code=http_status.HTTP_200_OK,
)
async def shortener(
    payload: UrlPayloadIn,
    use_case=Depends(get_url_shortener_use_case),
    cache=Depends(get_url_cache_repository)
) -> UrlResponseOut:
    base_url = "http://localhost:8000/"
    original_url = payload.url
    value = cache.get(original_url)
    if value:
        return UrlResponseOut(url=f"{base_url}{value}")
    url = await use_case.execute(original_url)
    cache.set(original_url, url.short_url)
    return UrlResponseOut(url=f"{base_url}{url.short_url}")


@router.get(
    "/{short_url}",
    summary="redirect to original url",
    status_code=http_status.HTTP_302_FOUND,
)
async def get_original_url(
    short_url: str,
    use_case=Depends(get_original_url_use_case),
    cache=Depends(get_url_cache_repository)
) -> UrlResponseOut:
    value = cache.get(short_url)
    if value:
        return UrlResponseOut(url=value)
    url = await use_case.execute(short_url)
    if not url:
        raise HTTPException(status_code=404, detail="Url not found")
    cache.set(short_url, url.url)
    return UrlResponseOut(url=url.url)
