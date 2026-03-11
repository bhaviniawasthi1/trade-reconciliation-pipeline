class TradeNormalizer:

    @staticmethod
    def normalize(trade):

        normalized_trade = {
            "trade_id": trade["trade_id"],
            "symbol": trade["symbol"].upper(),
            "quantity": int(trade["quantity"]),
            "price": float(trade["price"]),
            "side": trade["side"].upper(),
            "trade_date": trade["trade_date"]
        }

        return normalized_trade