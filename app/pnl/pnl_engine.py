class PnLEngine:

    def calculate_pnl(self, trades):

        pnl = 0

        for trade in trades:

            value = trade["quantity"] * trade["price"]

            if trade["side"] == "BUY":
                pnl -= value
            else:
                pnl += value

        return pnl