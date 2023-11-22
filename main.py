'''requsets using example'''
from requests import get


class Proster:

    def __init__(self, url: str) -> None:
        self.url = url

    def make_request(self, timeout: float = 5.0) -> str:
        result = get(self.url, timeout=timeout)
        return result.text
