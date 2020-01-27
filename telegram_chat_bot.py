from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from threading import Thread
import logging, io, settings

TOKEN = settings.TELEGRAM_API_TOKEN

class PiTelegramBot():

    bot = Bot(token=TOKEN)
    updater = None
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.logger.info("Starting chat bot")        

    def send_sound_detected(self, count):
        self.bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text="Sound module captured sound {} times in the last minute...".format(count))
        self.bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text="Send the /photo command to the bot to see what is going on")