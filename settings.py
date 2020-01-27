import os
from dotenv import load_dotenv

load_dotenv()

PIN=os.getenv('PIN')
GPIOD_HOST=os.getenv('GPIO_HOST')
TELEGRAM_API_TOKEN=os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_CHAT_ID=os.getenv('TELEGRAM_CHAT_ID')