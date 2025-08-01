import csv
from datetime import datetime

def log_trade(action, symbol, price):
    with open("trades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), action, symbol, price])
