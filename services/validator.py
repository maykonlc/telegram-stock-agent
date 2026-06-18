import requests

def validate_ticker(ticker):

    url = f"https://brapi.dev/api/quote/{ticker}"
    r = requests.get(url).json()

    if "results" not in r:
        return False

    if not r["results"]:
        return False

    # proteção extra
    if r["results"][0].get("symbol") is None:
        return False

    return True
