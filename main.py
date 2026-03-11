from app.ingestion.csv_reader import read_trades_from_csv
from app.validation.trade_validator import TradeValidator
from app.normalization.trade_normalizer import TradeNormalizer


def main():

    trades = read_trades_from_csv("data/trades.csv")

    print("Validating and normalizing trades...")

    normalized_trades = []

    for trade in trades:

        try:
            # validation
            TradeValidator.validate(trade)

            # normalization
            normalized_trade = TradeNormalizer.normalize(trade)

            normalized_trades.append(normalized_trade)

            print(f"Trade {trade['trade_id']} processed successfully.")

        except Exception as e:

            print(f"Trade {trade.get('trade_id')} failed: {e}")

    print("\nNormalized Trades:")
    print(normalized_trades)


if __name__ == "__main__":
    main()