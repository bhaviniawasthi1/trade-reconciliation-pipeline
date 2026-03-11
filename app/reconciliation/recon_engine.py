class ReconciliationEngine:

    def reconcile(self, trade, settlement):

        mismatches = []

        if int(settlement["quantity"]) != trade["quantity"]:
            mismatches.append("Quantity mismatch")

        if float(settlement["price"]) != trade["price"]:
            mismatches.append("Price mismatch")

        return mismatches