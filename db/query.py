

class QUERY():

    @staticmethod
    def insert_ticker() -> str:
        return """
            INSERT INTO ticker
            (symbol, name, exchange)
            VALUES (%s, %s, %s)
        """

    @staticmethod
    def insert_tracking() -> str:
        return """
            INSERT INTO tracking
            (symbol, last_price, volume, marketcap, price_change_pct)
            VALUES (%s, %s, %s, %s, %s)
        """
    
    @staticmethod
    def get_tickers() -> str:
        return """
            SELECT symbol
            FROM ticker
        """

    @staticmethod
    def get_last_tracking_date() -> str:
        return """
            SELECT date
            FROM tracking
            ORDER BY date DESC
            LIMIT 1
        """
    
    @staticmethod
    def update_cik() -> str:
        return """
            UPDATE ticker
            SET cik = %s
            WHERE symbol = %s;
        """
