import requests

def validate_ticker(ticker):

    url = f"https://brapi.dev/api/quote/{ticker}"
    r = requests.get(url).json()

    return "results" in r and len(r["results"]) > 0
