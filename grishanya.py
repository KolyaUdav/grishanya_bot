from telegram.ext import Updater
from telegram.ext import CommandHandler

def start (bot, update):
    bot.message (chat_id=update.message.chat_id, text="ЗДАРОВА ПИЗДА У КАРОВЫ!!!");
    
updater = Updater (token='343422798:AAHZmAoi3WPoe4F4TQcBykrsK1ZZNTp5qmo');

start_handler = CommandHandler ('start', start);

updater.dispatcher.add_handler (start_handler);
updater.start_polling ();