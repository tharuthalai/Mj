import time
from kite_paper import get_price
from selector import choose_strategy
from risk_manager import should_exit
from notifier import notify
from trade_logger import log_trade

balance = 1000
symbol = "RELIANCE.NS"
price_data = []
position = None

notify("📈 MJ’s Replit Bot Started!")

def run_bot():
    global price_data, position, balance
    price = get_price(symbol)
    if price is None:
        time.sleep(10)
        return

    price_data.append(price)
    if len(price_data) > 50:
        price_data.pop(0)

    strategy = choose_strategy(balance)
    signal = strategy(price_data)

    if not position and signal == "BUY":
        position = {"entry": price}
        notify(f"✅ Bought at {price}")
        log_trade("BUY", symbol, price)

    elif position and should_exit(price, position["entry"]):
        pnl = price - position["entry"]
        balance += pnl
        notify(f"❌ Exited at {price} | PnL: {pnl:.2f}")
        log_trade("SELL", symbol, price)
        position = None

if __name__ == "__main__":
    while True:
        run_bot()
        time.sleep(300)
