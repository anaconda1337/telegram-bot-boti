# Telegram Bot
- A simple telegram bot that can send messages to a channel or group

## Prerequisites
- Python 3.10 or higher
- [Telegram Bot Token](https://core.telegram.org/bots#6-botfather)
- [Virtual Environment](https://docs.python.org/3/library/venv.html)
- Docker (optional)

## Installation
- Create a virtual environment
```bash
virtualenv venv
```
- Activate the virtual environment
```bash
source venv/bin/activate
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Create .env file in the `/app` directory and add the following (replace `<your-telegram-bot-token>` with your telegram bot token)
How to get a telegram bot token: https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot#create-bot
```bash
TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
```
- Run the bot
```bash
python main.py
```

## Usage
- Go to your telegram bot and send a message to it
- Available commands:
1. `/hello` - sends a hello message
2. `/clock` - sends the current time
3. `/timer {seconds}` - sets a timer for the specified seconds
