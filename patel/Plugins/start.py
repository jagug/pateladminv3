# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 Amano LLC


import telegram
from telegram.ext import CommandHandler, Updater

# Replace YOUR_TOKEN_HERE with your bot token
bot = telegram.Bot(token='YOUR_TOKEN_HERE')

# Define the /start command handler
def start(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=f"Hi {user.first_name}!")

# Create the dispatcher
dispatcher = Updater(token='YOUR_TOKEN_HERE', use_context=True).dispatcher

# Add the /start command handler to the bot
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()
