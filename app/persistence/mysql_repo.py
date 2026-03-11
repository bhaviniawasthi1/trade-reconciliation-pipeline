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


    def fetch_trades(self):

        query = "SELECT trade_id, symbol, quantity, price, side, trade_date FROM trades"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        trades = []

        for row in rows:
            trades.append({
                "trade_id": row[0],
                "symbol": row[1],
                "quantity": row[2],
                "price": float(row[3]),
                "side": row[4],
                "trade_date": row[5]
            })

        return trades