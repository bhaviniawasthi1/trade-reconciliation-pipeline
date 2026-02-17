from datetime import datetime

class TradeValidator:

    @staticmethod
    def validate(trade):

        required_fields = [
            "trade_id",
            "symbol",
            "quantity",
            "price",
            "side",
            "trade_date"
        ]

        # 1️⃣ Check missing fields
        for field in required_fields:
            if field not in trade:
                raise ValueError(f"Missing field: {field}")

        # 2️⃣ Check side valid
        if trade["side"] not in ["BUY", "SELL"]:
            raise ValueError("Invalid side. Must be BUY or SELL.")

        # 3️⃣ Quantity positive
        if int(trade["quantity"]) <= 0:
            raise ValueError("Quantity must be positive.")

        # 4️⃣ Date format check
        try:
            datetime.strptime(trade["trade_date"], "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        return True
