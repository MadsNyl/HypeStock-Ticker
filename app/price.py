from util import http_get, is_same_date
from datetime import datetime
from errors import SameDateException
from db import INSERT, GET
from classes import Ticker, Tracking
from enums import TrackingJson, TickerJson


TICKER_SYMBOLS = GET.tickers()
last_tracking_date = GET.last_tracking_date()
if last_tracking_date:
    last_tracking_date = str(last_tracking_date[0])[:10]


def get_ticker_trackings(url: str, exchange: str) -> None:
    now_date = str(datetime.now())[:10]
    if is_same_date(now_date, last_tracking_date):
        raise SameDateException("The last tracking stored in DB is now.")
    
    json = http_get(url).json()

    for object in json:
        
        symbol = object[TickerJson.SYMBOL.value].strip()
        ticker = Ticker(
            symbol=symbol,
            name=object[TickerJson.NAME.value],
            exchange=exchange
        )

        last_price = object[TrackingJson.LAST_PRICE.value][1:]
        volume = object[TrackingJson.VOLUME.value]
        marketcap = object[TrackingJson.MARKETCAP.value]
        price_change_pct = object[TrackingJson.PRICE_CHANGE_PCT.value][:-1]

        tracking = Tracking(
            symbol=symbol,
            last_price=float(last_price) if len(last_price) else None,
            volume=volume,
            marketcap=marketcap[:-3],
            price_change_pct=float(price_change_pct) if price_change_pct else None
        )

        if symbol not in TICKER_SYMBOLS:
            INSERT.ticker(ticker)
        
        INSERT.tracking(tracking)
