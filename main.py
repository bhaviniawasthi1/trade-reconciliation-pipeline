from app.ingestion.csv_reader import read_trades_from_csv
from app.ingestion.settlement_reader import read_settlements
from app.validation.trade_validator import TradeValidator
from app.normalization.trade_normalizer import TradeNormalizer
from app.persistence.mysql_repo import MySQLRepository
from app.reconciliation.recon_engine import ReconciliationEngine
from app.pnl.pnl_engine import PnLEngine


def main():

    trades = read_trades_from_csv("data/trades.csv")
    settlements = read_settlements("data/settlements.csv")

    db = MySQLRepository()
    recon = ReconciliationEngine()

    print("Processing trades...")

    for trade in trades:

        try:
            TradeValidator.validate(trade)

            normalized_trade = TradeNormalizer.normalize(trade)

            db.insert_trade(normalized_trade)

            trade_id = normalized_trade["trade_id"]

            if trade_id in settlements:

                mismatches = recon.reconcile(
                    normalized_trade,
                    settlements[trade_id]
                )

                for reason in mismatches:
                    db.insert_exception(trade_id, reason)

            print(f"Trade {trade_id} processed")

        except Exception as e:
            print(f"Trade {trade.get('trade_id')} failed: {e}")

    # P&L computation
    pnl_engine = PnLEngine()

    db_trades = db.fetch_trades()

    pnl = pnl_engine.calculate_pnl(db_trades)

    print("\nDaily P&L:", pnl)


if __name__ == "__main__":
    main()