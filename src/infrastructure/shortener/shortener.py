import hashlib
import string
from abc import ABC, abstractmethod

BASE62_CHARS = string.digits + string.ascii_letters


class URLShortener(ABC):
    @abstractmethod
    def shorten_url(self, auto_increment_id): ...


class URLShortenerBase62(URLShortener):
    def shorten_url(self, auto_increment_id):
        short_url = self.convert_to_base62(auto_increment_id)
        return short_url

    @staticmethod
    def convert_to_base62(number):
        if number == 0:
            return "0"

        base62 = ""
        while number:
            number, remainder = divmod(number, 62)
            base62 = BASE62_CHARS[remainder] + base62
        return base62


class URLShortenerSHA2(URLShortener):
    def shorten_url(self, auto_increment_id):
        short_url = self.convert_to_sha2(auto_increment_id)
        return short_url

    @staticmethod
    def convert_to_sha2(cadena):
        sha2_hash = hashlib.sha256()
        sha2_hash.update(str(cadena).encode("utf-8"))
        hash_hexadecimal = sha2_hash.hexdigest()
        return hash_hexadecimal[0:8]
