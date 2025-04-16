import requests
import threading
import time
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = "6725481041:AAFU_9qn9Vwd96hxEj9j2FfNfBz8jVY0Ugc"
USER_ID = "5122281931"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": USER_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload, timeout=5)
    except:
        pass

def run_request():
    url1 = "https://apis-3kns.onrender.com/?product_id=3"
    url2 = "https://imgbot-3y9h.onrender.com"
    main_app_url_provider = "https://raw.githubusercontent.com/Pryanxhufr/test/refs/heads/main/main.txt"

    while True:
        try:
            response1 = requests.get(url1)
            print(response1.text)

            response2 = requests.get(url2)
            print(response2.text)

            response3 = requests.get(main_app_url_provider)
            print("response 3:", response3.text)

            url_to_fetch = response3.text.strip()

            if "https" in url_to_fetch:
                print("ok")
                main_response = requests.get(url_to_fetch)
                print(main_response.text)
                print(main_response)

                msg = (
                    "🚀 <b>Everything's live — the server is running perfectly!</b>\n\n"
                    f"<b>Response 1:</b> {response1.status_code}\n"
                    f"<b>Response 2:</b> {response2.status_code}\n"
                    f"<b>Response 3:</b> {response3.status_code}\n"
                    f"<b>Response 3 Text:</b>\n<code>{response3.text.strip()}</code>\n"
                    f"<b>Response 4:</b> {main_response.status_code}"
                )
                send_telegram_message(msg)
        except:
            pass

        time.sleep(40)

@app.route('/')
def hello_world():
    return 'Alive'

def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    request_thread = threading.Thread(target=run_request)

    flask_thread.start()
    request_thread.start()
