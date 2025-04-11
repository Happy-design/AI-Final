from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7432110325:AAH6NTVYz3QJUZaCD5IOqh8hoxQS4hZDJPM"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to the food expenditure prediction. Please enter your income:')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.lower() == 'exit':
        await update.message.reply_text('Goodbye!')
    else:
        try:
            income = float(text)
            prediction = 100 + 0.722 * income 
            await update.message.reply_text(f'Your predicted food expenditure is {prediction:.2f}')
        except ValueError:
            await update.message.reply_text('Invalid input. Please enter a valid number.')

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
