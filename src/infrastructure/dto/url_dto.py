from pydantic import BaseModel


class UrlPayloadIn(BaseModel):
    url: str


class UrlResponseOut(BaseModel):
    url: str
