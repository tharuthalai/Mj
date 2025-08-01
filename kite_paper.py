import requests

def get_price(symbol):
    try:
        res = requests.get(
            f'https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}',
            timeout=5
        )
        return res.json()['quoteResponse']['result'][0]['regularMarketPrice']
    except Exception:
        return None
