import mysql.connector
from app.config.settings import MYSQL_CONFIG


class MySQLRepository:

    def __init__(self):
        self.conn = mysql.connector.connect(**MYSQL_CONFIG)
        self.cursor = self.conn.cursor()

    def insert_trade(self, trade):

        query = """
        INSERT INTO trades (trade_id, symbol, quantity, price, side, trade_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            trade["trade_id"],
            trade["symbol"],
            trade["quantity"],
            trade["price"],
            trade["side"],
            trade["trade_date"]
        )

        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_exception(self, trade_id, reason):

        query = """
        INSERT INTO exceptions (trade_id, reason)
        VALUES (%s, %s)
        """

        values = (trade_id, reason)

        self.cursor.execute(query, values)
        self.conn.commit()