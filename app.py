from flask import Flask, request
from services.telegram import send_message
from services.market import get_stock_data
from services.formatter import format_response

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "").upper().strip()

    # 1. busca dados da ação
    stock = get_stock_data(text)

    # 2. se não existir
    if not stock:
        send_message(
            chat_id,
            f"❌ Não encontrei a ação {text} na B3.\nDigite outro ticker."
        )
        return "ok"

    # 3. formata resposta
    message = format_response(stock)

    # 4. envia Telegram
    send_message(chat_id, message)

    return "ok"


if __name__ == "__main__":
    app.run()
