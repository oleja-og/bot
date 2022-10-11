from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types
import json


with open("all_cinema.json") as file:
    all_cinema = json.load(file)

kino = []
for item in all_cinema:
    kino.append(item)


start_button = ['Кинотеатры', 'Театры', 'Клубы']
kb_client = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(*start_button)


kb5 = KeyboardButton("назад")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_list = [KeyboardButton(text=cinema_name, callback_data='ok') for cinema_name in kino]
keyboard.add(*button_list).add(kb5)







