from flask import Flask, request
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = '7432110325:AAH6NTVYz3QJUZaCD5IOqh8hoxQS4hZDJPM'
bot = telegram.Bot(token=BOT_TOKEN)


YOUR_URL = 'https://ai-final-z5c0.onrender.com'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook(f'{YOUR_URL}/webhook')
    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"


@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.message:
        text = update.message.text

        if text.lower() == 'exit':
            update.message.reply_text('Goodbye!')
        else:
            try:
                income = float(text)
                prediction = (income * 0.4851) + 147.4
                update.message.reply_text(f'Your predicted food expenditure is {prediction:.2f}')
            except ValueError:
                update.message.reply_text('Invalid input. Please enter a valid number.')
    return 'ok'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
