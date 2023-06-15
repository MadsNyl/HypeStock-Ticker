from dataclasses import dataclass


@dataclass
class Ticker():
    symbol: str
    name: str
    exchange: str
