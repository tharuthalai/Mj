def sma_crossover(price_data):
    if len(price_data) < 20:
        return None
    short_sma = sum(price_data[-5:]) / 5
    long_sma = sum(price_data[-20:]) / 20
    return "BUY" if short_sma > long_sma else "SELL"

def rsi_reversal(price_data):
    if len(price_data) < 15:
        return None
    gains = []
    losses = []
    for i in range(-14, 0):
        delta = price_data[i] - price_data[i - 1]
        (gains if delta > 0 else losses).append(abs(delta))
    avg_gain = sum(gains) / 14 if gains else 0.001
    avg_loss = sum(losses) / 14 if losses else 0.001
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return "BUY" if rsi < 30 else "SELL" if rsi > 70 else None

def choose_strategy(balance):
    if balance <= 1000:
        return sma_crossover
    else:
        return rsi_reversal
