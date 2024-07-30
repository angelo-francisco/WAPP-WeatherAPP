import sys, os

sys.path.insert(0, os.path.abspath(os.curdir))

from src.core.settings import API_LINK, API_KEY
from requests import get
import time


def get_weather(city: str) -> dict[str, float]:
    link = str(API_LINK).format(city=city, API_KEY=API_KEY)
    request = get(link)
    requestJSON = request.json()

    return requestJSON
