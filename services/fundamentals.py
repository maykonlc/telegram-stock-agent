import requests
from bs4 import BeautifulSoup

def get_fundamentals(ticker):

    try:
        url = f"https://www.fundamentus.com.br/detalhes.php?papel={ticker}"
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")

        def find(label):
            try:
                return soup.find(text=label).find_next().text.strip()
            except:
                return "N/D"

        return {
            "pl": find("P/L"),
            "pvp": find("P/VP"),
            "roe": find("ROE"),
            "roic": find("ROIC"),
            "dy": find("Div Yield"),
            "ebitda": find("EV/EBITDA"),
            "margem_liquida": find("Marg. Líquida"),
            "divida_liquida": find("Dív. Líquida"),
        }

    except:
        return None
