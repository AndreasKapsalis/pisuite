from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from threading import Thread
from time import sleep
from picamera import PiCamera
import logging, io, settings
from sensors import SoundSensor

TOKEN = settings.TELEGRAM_API_TOKEN

class PiTelegramBotCommandHandler():

    updater = None
    logger = logging.getLogger(__name__)
    sound_sensor = None
    camera = None


    def __init__(self):
        self.updater = Updater(TOKEN, use_context=True)
        dp = self.updater.dispatcher
        self.camera = PiCamera()
        self.camera.resolution = (1920, 1080)
        self.logger.info("Starting the main command bot...")
        dp.add_handler(CommandHandler("start_sound_sensor", self.start_sound_sensor))
        dp.add_handler(CommandHandler("stop_sound_sensor", self.stop_sound_sensor))
        dp.add_handler(CommandHandler("photo", self.photo))
        dp.add_error_handler(self.error)
        self.updater.start_polling()
        self.updater.idle()
        
    def error(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)

    def start_sound_sensor(self, update, context):
        if self.sound_sensor is None:
            self.sound_sensor = SoundSensor()
            self.sound_sensor.start()
            update.message.bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text="Starting sound sensor...")
        else:
            update.message.reply_text("Sound sensor is already running")

    def stop_sound_sensor(self, update, context):
        if self.sound_sensor is not None:
            self.logger.info("Stopping sound sensor...")
            update.message.bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text="Stopping sound sensor...")
            self.sound_sensor.stop()
            self.sound_sensor = None
        else:
            update.message.reply_text("There is not sound sensor thread running. You can start a sound sensor thread with the \"start_sound_monitor\" command")

    def photo(self, update, context):
        pic_stream = io.BytesIO()
        self.camera.capture(pic_stream, 'png')
        pic_stream.seek(0)
        update.message.bot.send_photo(chat_id=settings.TELEGRAM_CHAT_ID, photo=pic_stream)
