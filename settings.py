import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

TICKER_DATA = [
    {
        "url": os.environ.get("AMEX_API"),
        "exchange": "amex"
    },
    {
        "url": os.environ.get("NASDAQ_API"),
        "exchange": "nasdaq"
    },
    {
        "url": os.environ.get("NYSE_API"),
        "exchange": "nyse"
    }
]

DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_DATABASE = os.environ.get("DB_DATABASE")

YAHOO_HISTORICAL_DATA_API = os.environ.get("YAHOO_HISTORICAL_DATA_API")