from flask import Flask, request

from services.telegram import send_message
from services.normalizer import normalize_ticker
from services.validator import is_valid
from services.market import get_market_data
from services.fundamentals import get_fundamentals
from services.scorer import score_stock
from services.formatter import format_message

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    raw = data["message"].get("text", "")

    # 1. normaliza ticker
    ticker = normalize_ticker(raw)

    # 2. valida
    if not is_valid(ticker):
        send_message(chat_id, f"❌ Ticker {ticker} não encontrado na B3.")
        return "ok"

    # 3. dados de mercado
    market = get_market_data(ticker)

    # 4. fundamentos
    fund = get_fundamentals(ticker)

    # 5. score inteligente
    score = score_stock(market, fund)

    # 6. resposta final
    msg = format_message(ticker, market, fund, score)

    send_message(chat_id, msg)

    return "ok"
