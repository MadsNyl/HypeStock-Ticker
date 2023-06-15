from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tracking():
    symbol: str
    last_price: float
    volume: str
    date: datetime = None
    marketcap: str = None
    price_change_pct: float = None
