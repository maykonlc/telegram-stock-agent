from flask import Flask, request

from services.telegram import send_message
from services.validator import validate_ticker
from services.market import get_price_data
from services.fundamentals import get_fundamentals
from services.formatter import build_message

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    ticker = data["message"].get("text", "").upper().strip()

    # 1. valida ticker
    if not validate_ticker(ticker):
        send_message(chat_id, f"❌ Ticker {ticker} não encontrado na B3.")
        return "ok"

    # 2. dados de mercado
    market = get_price_data(ticker)

    # 3. fundamentos completos
    fundamentals = get_fundamentals(ticker)

    # 4. resposta final
    msg = build_message(ticker, market, fundamentals)

    send_message(chat_id, msg)

    return "ok"
