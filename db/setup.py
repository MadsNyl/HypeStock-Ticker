from mysql import connector
from settings import (
    DB_DATABASE,
    DB_HOST,
    DB_PASSWORD,
    DB_USERNAME
)


db = connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_DATABASE
)


pool = db.cursor(buffered=True)
