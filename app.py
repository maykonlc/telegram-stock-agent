from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ["BOT_TOKEN"]

def enviar(chat_id, texto):

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": texto
        }
    )

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    chat_id = data["message"]["chat"]["id"]

    ticker = data["message"]["text"].upper()

    url = f"https://brapi.dev/api/quote/{ticker}"

    r = requests.get(url)

    if r.status_code != 200:

        enviar(
            chat_id,
            f"❌ Não encontrei {ticker}. Digite novamente."
        )

        return "ok"

    resultado = r.json()

    if not resultado.get("results"):

        enviar(
            chat_id,
            f"❌ Não encontrei {ticker}. Digite novamente."
        )

        return "ok"

    acao = resultado["results"][0]

    mensagem = f"""
📈 {acao['symbol']}

Empresa:
{acao.get('longName','N/D')}

Preço:
R$ {acao.get('regularMarketPrice','N/D')}
"""

    enviar(chat_id, mensagem)

    return "ok"

if __name__ == "__main__":
    app.run()
