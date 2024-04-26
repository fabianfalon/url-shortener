from abc import ABC, abstractmethod
from datetime import datetime

from src.domain.value_objects.url_field import UrlField


class AggregateRoot(ABC):
    @abstractmethod
    def to_primitive(self): ...

    @abstractmethod
    def from_primitive(self, raw_data: dict): ...


class Url(AggregateRoot):
    id: int
    _url: UrlField
    short_url: str
    created_at: datetime
    updated_at: datetime

    def __init__(
            self, id: int, url: str, short_url: str, created_at: datetime = None, updated_at: datetime = None
    ) -> None:
        self.id = id
        self._url = UrlField(url)
        self.short_url = short_url
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    @property
    def url(self):
        return self._url.value

    def to_primitive(self):
        return {
            "id": self.id,
            "url": self.url,
            "short_url": self.short_url,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def from_primitive(raw_data: dict):
        return Url(
            id=raw_data["id"],
            url=raw_data["url"],
            short_url=raw_data["short_url"],
            created_at=raw_data["created_at"],
            updated_at=raw_data["updated_at"]
        )