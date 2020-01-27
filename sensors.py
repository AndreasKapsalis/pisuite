from threading import Thread, Event
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DigitalInputDevice
from telegram_chat_bot import PiTelegramBot
import logging
import settings
from time import sleep
from datetime import datetime, timedelta

class SoundSensor(Thread):

    pin = settings.PIN
    logger = None
    do = None
    piBot = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        super(SoundSensor, self).__init__()
        self._stopper = Event()  
        self.logger.info("Starting sound sensor thread...")
        # In case you want to use Remote GPIO
        factory = PiGPIOFactory(host=settings.GPIOD_HOST)
        self.do = DigitalInputDevice(self.pin, pin_factory=factory)
        self.piBot = PiTelegramBot()

    def run(self):
        count = 0
        last_minute = timedelta(seconds=60)
        last_checked = datetime.now()
        while(True):
            if self.stopped():
                self.logger.info("Received stop signal. Stopping...")
                return
            
            if self.do.value == 1:
                count += 1
                self.logger.info("Sound detected")

            if count > 0 and (datetime.now() - last_minute > last_checked):
                self.piBot.send_sound_detected(count)
                last_checked = datetime.now()
                count = 0
                sleep(20)
            
            # Sleep time must be in msec to prevent any misses from the input device. Probably needs fine tuning though
            sleep(450/1000000.0)

    # function using _stop function 
    def stop(self): 
        self._stopper.set() 
        self.do = None
  
    def stopped(self): 
        return self._stopper.is_set()