from aiogram import Dispatcher, Bot
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('KEY'))
dp = Dispatcher(bot)
