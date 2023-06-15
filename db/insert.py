from db.setup import pool, db
from db.query import QUERY
from classes import Ticker, Tracking


class INSERT():

    @staticmethod
    def ticker(ticker: Ticker):
        """
            Inserts a ticker.
        """
        try:
            pool.execute(
                QUERY.insert_ticker(),
                (
                    ticker.symbol,
                    ticker.name,
                    ticker.exchange
                )
            )
            
            db.commit()
        except Exception as e:
            print(f"Stock insertion error: {e}")
    
    @staticmethod
    def ticker_bulk(tickers: list[Ticker]):
        """
            Inserts a bulk of tickers.
        """
        try:
            pool.executemany(
                QUERY.insert_ticker(),
                tickers
            )
        except Exception as e:
            print(f"Bulk insertion of tickers error: {e}")

    @staticmethod
    def tracking(tracking: Tracking):
        """
            Inserts a tracking.
        """
        try:
            pool.execute(
                QUERY.insert_tracking(),
                (
                    tracking.symbol,
                    tracking.last_price,
                    tracking.volume,
                    tracking.marketcap,
                    tracking.price_change_pct
                )
            )
        except Exception as e:
            print(f"Insertion of tracking error: {e}")

