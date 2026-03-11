from app.ingestion.csv_reader import read_trades_from_csv
from app.validation.trade_validator import TradeValidator
from app.normalization.trade_normalizer import TradeNormalizer
from app.persistence.mysql_repo import MySQLRepository


def main():

    trades = read_trades_from_csv("data/trades.csv")

    db = MySQLRepository()

    print("Processing trades...")

    for trade in trades:

        try:
            TradeValidator.validate(trade)

            normalized_trade = TradeNormalizer.normalize(trade)

            db.insert_trade(normalized_trade)

            print(f"Trade {trade['trade_id']} inserted into database.")

        except Exception as e:

            print(f"Trade {trade.get('trade_id')} failed: {e}")


if __name__ == "__main__":
    main()