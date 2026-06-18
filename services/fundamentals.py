import requests
from bs4 import BeautifulSoup

def get_fundamentals(ticker):

    try:
        url = f"https://www.fundamentus.com.br/detalhes.php?papel={ticker}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "lxml")

        def get(label):
            try:
                return soup.find(text=label).find_next().text.strip()
            except:
                return "N/D"

        return {
            "pl": get("P/L"),
            "pvp": get("P/VP"),
            "roe": get("ROE"),
            "roic": get("ROIC"),
            "dy": get("Div Yield"),
            "ev_ebitda": get("EV/EBITDA"),
            "margem": get("Marg. Líquida")
        }

    except:
        return None
