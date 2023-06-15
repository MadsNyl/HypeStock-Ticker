from app import TickerInserter
from util import http_get
from settings import TICKER_DATA
from enums import TickerJson


def insert_ticker(data: dict) -> None:
    inserter = TickerInserter()

    res = http_get(data["url"])
    json = res.json()

    for object in json:
        ticker = inserter.create(
            symbol=object[TickerJson.SYMBOL.value].strip(),
            name=object[TickerJson.NAME.value],
            exchange=data[TickerJson.EXCHANGE.value]
        )
        inserter.insert(ticker)


def main() -> None:
    for data in TICKER_DATA:
        insert_ticker(data)


if __name__ == "__main__":
    main()