from app import get_ticker_trackings
from settings import TICKER_DATA


if __name__ == "__main__":
    for data in TICKER_DATA:
        get_ticker_trackings(
            data["url"],
            data["exchange"]
        )