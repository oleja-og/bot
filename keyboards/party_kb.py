from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json


with open("all_clubs.json") as file:
    all_clubs = json.load(file)

clubs = []
for item in all_clubs:
    clubs.append(item)

kb5 = KeyboardButton("назад")

keyboard_clubs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_list = [KeyboardButton(text=clubs_name, callback_data='ok') for clubs_name in clubs]
keyboard_clubs.add(*buttons_list).add(kb5)
