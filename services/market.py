import requests

def get_market_data(ticker):

    try:
        r = requests.get(f"https://brapi.dev/api/quote/{ticker}").json()

        if not r.get("results"):
            return None

        s = r["results"][0]

        return {
            "price": s.get("regularMarketPrice"),
            "change": s.get("regularMarketChangePercent"),
            "high": s.get("regularMarketDayHigh"),
            "low": s.get("regularMarketDayLow"),
            "volume": s.get("regularMarketVolume")
        }

    except:
        return None
