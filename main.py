from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7672621134:AAHVggFMvRnotTAqrPh2TTgCCd1cjeHkB3Q'
CHAT_ID = '1307856158'

def send_message_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'Markdown'
    }
    requests.post(url, data=payload)

@app.route('/telegram-webhook', methods=['POST'])
def telegram_webhook():
    data = request.json
    embeds = data.get("embeds", [])
    message = data.get("content", "")

    for embed in embeds:
        message += f"\n\n*{embed['title']}*\n_{embed['description']}_\n"
        for field in embed.get("fields", []):
            message += f"\n*{field['name']}*\n{field['value']}"

    send_message_to_telegram(message)
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
