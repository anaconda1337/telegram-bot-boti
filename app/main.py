import os
from time import sleep
from datetime import datetime

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


load_dotenv()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello as sum Boti, {update.effective_user.first_name}')


async def clock(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Current time, {datetime.now().strftime("%H:%M:%S")}')


async def timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    time_range = update.message.text.split(' ')
    for i in range(int(time_range[1])):
        await update.message.reply_text(f'{i}')
        sleep(1)
    await update.message.reply_text(f'End of timer')


def start_bot() -> None:
    app = ApplicationBuilder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()

    # Register handlers here
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("clock", clock))
    app.add_handler(CommandHandler("timer", timer))

    app.run_polling()


if __name__ == '__main__':
    start_bot()
