from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as http_status

from src.config import settings
from src.delivery.api.dependencies import get_original_url_use_case, get_url_shortener_use_case
from src.infrastructure.dto.url_dto import UrlPayloadIn, UrlResponseOut
from src.use_case.get_original_url import GetOriginalUrlUseCase
from src.use_case.create_short_url import CreateShortUrlUseCase

# Router Config
router = APIRouter(tags=["url shortener"])


@router.post(
    "/shortener",
    summary="Make a short url",
    status_code=http_status.HTTP_200_OK,
)
async def shortener(
    payload: UrlPayloadIn,
    use_case: CreateShortUrlUseCase = Depends(get_url_shortener_use_case),
) -> UrlResponseOut:
    original_url = payload.url.unicode_string()
    url = await use_case.execute(original_url)
    return UrlResponseOut(url=f"{settings.base_short_url}{url}")


@router.get(
    "/{short_url}",
    summary="redirect to original url",
    status_code=http_status.HTTP_302_FOUND,
)
async def get_original_url(
    short_url: str,
    use_case: GetOriginalUrlUseCase = Depends(get_original_url_use_case),
) -> UrlResponseOut:
    url = await use_case.execute(short_url)
    if not url:
        raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail="Url not found")
    return UrlResponseOut(url=url)
