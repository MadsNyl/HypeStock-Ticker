from enum import Enum


class TrackingIndex(Enum):
    DATE = 0
    LAST_PRICE = 4
    VOLUME = 6


class TrackingJson(Enum):
    SYMBOL = "symbol"
    LAST_PRICE = "lastsale"
    VOLUME = "volume"
    MARKETCAP = "marketCap"
    INDUSTRY = "industry"
    SECTOR = "sector"
    COUNTRY = "country"
    IPO_YEAR = "ipoyear"
    PRICE_CHANGE_PCT = "pctchange"
