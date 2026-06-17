import os
import requests

TOKEN = os.getenv("BOT_TOKEN")

def send_message(chat_id, text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text
        }
    )
