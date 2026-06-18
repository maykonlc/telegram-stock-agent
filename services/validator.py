import requests

B3_CACHE = set()

def is_valid(ticker):

    # cache local primeiro
    if ticker in B3_CACHE:
        return True

    # API principal
    try:
        r = requests.get(f"https://brapi.dev/api/quote/{ticker}").json()

        if r.get("results"):
            B3_CACHE.add(ticker)
            return True

    except:
        pass

    # fallback leve (Yahoo-like proxy)
    try:
        r = requests.get(f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}.SA")
        if "quoteResponse" in r.json():
            return True
    except:
        pass

    return False
