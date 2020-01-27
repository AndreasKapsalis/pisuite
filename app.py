from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DigitalInputDevice
from time import sleep
import logging
from datetime import datetime
from telegram_command_bot import PiTelegramBotCommandHandler

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

_ = PiTelegramBotCommandHandler()