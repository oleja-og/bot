from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('KEY'), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
