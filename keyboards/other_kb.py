from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json


with open("all_theatre.json") as file:
    all_theatre = json.load(file)

theatre = []
for item in all_theatre:
    theatre.append(item)

kb5 = KeyboardButton("назад")

keyboard_theatre = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_list = [KeyboardButton(text=theatre_name, callback_data='ok') for theatre_name in theatre]
keyboard_theatre.add(*buttons_list).add(kb5)
