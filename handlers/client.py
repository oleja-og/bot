from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client
from parsers.parser import keyboard
from bs4 import BeautifulSoup
import requests
import json


headers = {
    'accept': '*/*',
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


#@dp.message_handler(commands=['start', 'help'])
async def command_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, 'Выберите категорию!!!', reply_markup=kb_client)
        await msg.delete()
    except:
        await msg.reply(msg.from_user.id, 'Общение с ботом через ЛС, напишите ему:\nhttps:/t.me/minskafisha_bot')


#@dp.message_handler(commands=['Кино'])
async def command_kino(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Выбери кинотеатр!!!", reply_markup=keyboard)


#@dp.message_handler()
async def command_cinema(msg: types.Message):
    with open("all_cinema.json") as file:
        all_cinema = json.load(file)

    req = requests.get(url=all_cinema.get(msg.text), headers=headers)
    src = req.text
    dict = {}

    soup = BeautifulSoup(src, "lxml")

    film_date = soup.find(class_="schedule__list").find('h5').text.split()
    film_date1 = (film_date[0] + " " + film_date[1].strip(","))
    films_name = soup.find(class_="schedule__list").find_all(class_="schedule__item table_by_place rubric_place")

    for item in films_name:
        film = item.find(class_="schedule__event").text.strip().replace("\n", '').replace("     ", '')
        cost = item.find(class_="schedule__time").text.strip().replace("\n", '').replace("     ", '')
        dict[film] = cost

        await bot.send_message(msg.from_user.id, f'{film_date1} {dict.popitem()}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_kino, commands=['Кино'])
    dp.register_message_handler(command_cinema)
