from bs4 import BeautifulSoup
import json
import requests


url = "https://afisha.relax.by/kino/minsk/"

headers = {
    'accept': '*/*',
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text

with open("index.html", 'w') as file:
    file.write(src)
with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_cinema_hrefs = soup.find_all(class_="schedule__place-link link")

all_cinema = {}
for item in all_cinema_hrefs:
    item_text = item.text.strip()
    item_href = item.get("href")

    all_cinema[item_text] = item_href
with open("all_cinema.json", "w") as file:
    json.dump(all_cinema, file, indent=4, ensure_ascii=False)







