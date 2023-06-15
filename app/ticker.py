from classes import Ticker
from db import INSERT


class TickerInserter():
    
    def create(self, symbol: str, name: str, exchange: str) -> Ticker:
        return Ticker(
            symbol=symbol,
            name=name,
            exchange=exchange
        )

    def insert(self, ticker: Ticker) -> None:
        INSERT.ticker(ticker)

    def bulk_insert(self, tickers: list[Ticker]) -> None:
        INSERT.ticker_bulk(tickers)