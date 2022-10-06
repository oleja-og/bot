from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




kb1 = KeyboardButton("/Кино")
kb2 = KeyboardButton("/Спектакли")
kb3 = KeyboardButton("/Вечеринки")
kb4 = KeyboardButton("???")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(kb1, kb2, kb3).add(kb4)




