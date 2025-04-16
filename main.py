import requests
import threading
import time
from flask import Flask

app = Flask(__name__)

def run_request():
    url1 = "https://apis-3kns.onrender.com/?product_id=3"
    url2 = "https://imgbot-3y9h.onrender.com"
    main_app_url_provider = "https://raw.githubusercontent.com/Pryanxhufr/app_url/refs/heads/main/main.txt"

    while True:
        try:
            response1 = requests.get(url1)
            print("URL1:", response1.status_code)

            response2 = requests.get(url2)
            print("URL2:", response2.status_code)

            response3 = requests.get(url1)
            if response3.ok:
                main_response = requests.get(response3.text)
                print("Main Response:", main_response.status_code)
        except:
            pass
        time.sleep(35)

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
