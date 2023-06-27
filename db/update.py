from db.setup import pool, db
from db.query import QUERY


class UPDATE():

    @staticmethod
    def cik(symbol: str, cik: int):
        """
        Updates ticker with matching cik.
        """
        try:
            pool.execute(
                QUERY.update_cik(),
                (
                    cik,
                    symbol
                )
            )
            
            db.commit()
        except Exception as e:
            print(f"Stock update error: {e}")