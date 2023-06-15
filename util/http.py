import requests
from requests import Response


def http_get(url: str, **kwargs) -> Response:
    return requests.get(url, **kwargs)
