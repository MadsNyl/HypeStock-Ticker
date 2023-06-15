from db.setup import pool
from db.query import QUERY


class GET():

    @staticmethod
    def tickers() -> dict:
        """
            Returns all tickers as a dict.
        """
        try:
            pool.execute(
                QUERY.get_tickers()
            )

            return dict.fromkeys(
                list(
                    map(
                        lambda x: x[0],
                        pool.fetchall()
                    )
                )
            )
        
        except Exception as e:
            print(f"Fetching all tickers error: {e}") 
    
    @staticmethod
    def last_tracking_date():
        """
            Returns date of last tracking added.
        """ 
        try:
            pool.execute(
                QUERY.get_last_tracking_date()
            )

            return pool.fetchone()
        
        except Exception as e:
            print(f"Fetching tracking date error: {e}")