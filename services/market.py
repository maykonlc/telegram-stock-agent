import requests

def get_price_data(ticker):

    url = f"https://brapi.dev/api/quote/{ticker}"

    r = requests.get(url).json()

    if "results" not in r:
        return None

    s = r["results"][0]

    return {
        "price": s.get("regularMarketPrice"),
        "change": s.get("regularMarketChangePercent"),
        "high": s.get("regularMarketDayHigh"),
        "low": s.get("regularMarketDayLow"),
        "volume": s.get("regularMarketVolume")
    }
