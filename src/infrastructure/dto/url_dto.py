from pydantic import BaseModel, AnyHttpUrl


class UrlPayloadIn(BaseModel):
    url: AnyHttpUrl


class UrlResponseOut(BaseModel):
    url: AnyHttpUrl
