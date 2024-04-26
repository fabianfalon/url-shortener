import os
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

import motor.motor_asyncio

from src.domain.url import Url
from src.domain.url_repository import UrlRepository

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017")


class AbstractMongoRepository(ABC):
    def __init__(self) -> None:
        self.mongo_url = MONGO_URL
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
        self.database = self.client["url-shortener-mongodb"]

    def save(self, aggregate_root: object) -> None:
        self.database.get_collection(self.collection_name()).insert_one(aggregate_root.to_primitive())

    @abstractmethod
    def collection_name(self): ...


class MongoRepository(AbstractMongoRepository, UrlRepository):
    def __init__(self) -> None:
        super().__init__()

    def collection_name(self):
        return "url-shortener"

    def find_one(self, url_id: str) -> Optional[Url]:
        url = self.database.get_collection(self.collection_name()).find_one({"id": url_id})
        return self._create_url(url)

    def find_all(self) -> List[Url]:
        urls = self.database.get_collection(self.collection_name()).find()
        return [self._create_url(url) for url in urls]

    def get_by_original_url(self, original_url: str) -> Url:
        url = self.database.get_collection(self.collection_name()).find_one({"url": original_url})
        return self._create_url(url)

    def get_by_short_url(self, short_url: str) -> Url:
        url = self.database.get_collection(self.collection_name()).find_one({"short_url": short_url})
        return self._create_url(url)

    @staticmethod
    def _create_uel(raw_data: Dict) -> Url:
        return Url.from_primitive(raw_data)

    def delete(self):
        pass
