from aiogram import types, Dispatcher
from aiogram.utils.markdown import hbold
from create_bot import dp, bot
from keyboards.client_kb import kb_client
from keyboards.client_kb import keyboard
from keyboards.other_kb import keyboard_theatre
from keyboards.party_kb import keyboard_clubs
from bs4 import BeautifulSoup
import requests
import json


headers = {
    'accept': '*/*',
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

with open("all_cinema.json") as file:
    all_cinema = json.load(file)

kino = []
for item in all_cinema:
    kino.append(item)

with open("all_theatre.json") as file:
    all_theatre = json.load(file)

theatre = []
for item in all_theatre:
    theatre.append(item)

with open("all_clubs.json") as file:
    all_clubs = json.load(file)

clubs = []
for item in all_clubs:
    clubs.append(item)


#@dp.message_handler(commands=['start', 'help'])
async def command_start(msg: types.Message):
    try:
        await bot.send_message(msg.from_user.id, 'Выберите категорию!!!', reply_markup=kb_client)
        await msg.delete()
    except:
        await msg.reply(msg.from_user.id, 'Общение с ботом через ЛС, напишите ему:\n https:/t.me/minskafisha_bot')


#@dp.message_handler(commands=['Кинотеатры'])
async def command_kino(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Выбери кинотеатр!!!", reply_markup=keyboard)


#@dp.message_handler(commands=['назад'])
async def command_back(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Выберите категорию", reply_markup=kb_client)


#@dp.message_handler(commands=['Театры'])
async def command_theatre(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Выбери театр!!!", reply_markup=keyboard_theatre)


#@dp.message_handler(commands=['Клубы'])
async def command_party(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Выбери клуб!!!", reply_markup=keyboard_clubs)


# @dp.message_handler()
async def command_cinema(msg: types.Message):

    if msg.text in kino:
        await bot.send_message(msg.from_user.id, "Идёт поиск...")
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
            link = item.find("a")
            dict[film] = cost

            await bot.send_message(msg.from_user.id, f'{hbold(film_date1)}\n' f'{hbold(dict.popitem())}\n' f'{link}')

    elif msg.text in theatre:
        await bot.send_message(msg.from_user.id, "Идёт поиск...")
        with open("all_theatre.json") as file:
            all_theatre = json.load(file)

        req = requests.get(url=all_theatre.get(msg.text), headers=headers)
        src = req.text
        dict = {}

        soup = BeautifulSoup(src, "lxml")

        film_date = soup.find(class_="schedule__list").find('h5').text.split()
        film_date1 = (film_date[0] + " " + film_date[1].strip(","))
        films_name = soup.find(class_="schedule__list").find_all(
            class_="schedule__item table_by_place rubric_place")

        for item in films_name:
            film = item.find(class_="schedule__event").text.strip().replace("\n", '').replace("     ", '')
            cost = item.find(class_="schedule__time").text.strip().replace("\n", '').replace("     ", '')
            link = item.find("a")
            dict[film] = cost

            await bot.send_message(msg.from_user.id, f'{hbold(film_date1)}\n' f'{hbold(dict.popitem())}\n' f'{link}')

    elif msg.text in clubs:
        await bot.send_message(msg.from_user.id, "Идёт поиск...")
        with open("all_clubs.json") as file:
            all_clubs = json.load(file)

        req = requests.get(url=all_clubs.get(msg.text), headers=headers)
        src = req.text
        dict = {}

        soup = BeautifulSoup(src, "lxml")

        film_date = soup.find(class_="schedule__list").find('h5').text.split()
        film_date1 = (film_date[0] + " " + film_date[1].strip(","))
        films_name = soup.find(class_="schedule__list").find_all(class_="schedule__item table_by_place rubric_place")

        for item in films_name:
            film = item.find(class_="schedule__event").text.strip().replace("\n", '').replace("     ", '')
            cost = item.find(class_="schedule__time").text.strip().replace("\n", '').replace("     ", '')
            link = item.find("a")
            dict[film] = cost

            await bot.send_message(msg.from_user.id, f'{hbold(film_date1)}\n' f'{hbold(dict.popitem())}\n' f'{link}')

    elif msg.text == "назад":
        await command_back(msg.from_user)

    else:
        await bot.send_message(msg.from_user.id, "Нет такой команды, сорри")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_kino, text=['Кинотеатры'])
    dp.register_message_handler(command_theatre, text=['Театры'])
    dp.register_message_handler(command_party, text=['Клубы'])
    dp.register_message_handler(command_back, text=["назад"])
    dp.register_message_handler(command_cinema)
