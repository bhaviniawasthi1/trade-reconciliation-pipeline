import csv

def read_settlements(file_path):

    settlements = {}

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            settlements[row["trade_id"]] = row

    return settlements