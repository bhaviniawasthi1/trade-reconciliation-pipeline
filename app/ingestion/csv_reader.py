import csv

def read_trades_from_csv(file_path):
    trades = []

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            trades.append(row)

    return trades
