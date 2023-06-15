from os import remove
from io import TextIOWrapper
from classes import Tracking
from datetime import datetime
from util import http_get, is_empty_file_line, is_null
from settings import YAHOO_HISTORICAL_DATA_API
from enums import TrackingIndex


class Tracker():
    
    def download_csv(self, symbol: str, start: datetime, end: datetime) -> str:
        file_symbol = symbol.replace("/", "-")
        file = f"csv/{file_symbol}.csv"

        headers = {
            "User-Agent": "user-agent"
        }

        period = f"?period1={start}&period2={end}interval=1d&events=history&includeAdjustedClose=true"
        url = f"{YAHOO_HISTORICAL_DATA_API}{file_symbol}{period}"

        res = http_get(url=url, headers=headers)
        open(file, "wb").write(res.content)
        return 
    
    def get_data(self, file_path: str, symbol: str) -> list[Tracking]:
        trackings: list[Tracking] = []

        with open(file_path, "r") as file:
            trackings = self._parse_csv(file, symbol)
        
        return trackings

    def delete_csv(self, file_path: str) -> None:
        remove(file_path)

    def _parse_csv(self, file: TextIOWrapper, symbol: str) -> list[Tracking]:
        trackings: list[Tracking] = []

        for line in file:
            tracking = self._create_tracking(line, symbol)

            if not tracking:
                continue

            trackings.append(tracking)
        
        return trackings
    
    def _create_tracking(self, line: str, symbol: str) -> Tracking:
        data = line.strip().split(",")

        if is_empty_file_line(data, 1):
            return None
        
        last_price = data[TrackingIndex.LAST_PRICE.value]
        volume = data[TrackingIndex.VOLUME.value]
        date = data[TrackingIndex.DATE.value]

        return Tracking(
            symbol=symbol,
            last_price=float(last_price) if not is_null(last_price) else None,
            volume=volume if not is_null(volume) else None,
            date=date
        )