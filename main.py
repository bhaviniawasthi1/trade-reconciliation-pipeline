from app.ingestion.csv_reader import read_trades_from_csv
from app.validation.trade_validator import TradeValidator

def main():

    trades = read_trades_from_csv("data/trades.csv")

    print("Validating trades...")

    for trade in trades:
        try:
            TradeValidator.validate(trade)
            print(f"Trade {trade['trade_id']} is valid.")

        except Exception as e:
            print(f"Trade {trade.get('trade_id')} failed validation: {e}")

if __name__ == "__main__":
    main()
