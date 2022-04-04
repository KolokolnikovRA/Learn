import time

import lxml
import requests
from bs4 import BeautifulSoup
import pyttsx3
from datetime import datetime
# _________________________________________________________________
# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quote = soup.find_all('span', class_='text')
# author = soup.find_all('small', class_='author')
# for i in range(len(quote)):
#     print(quote[i].text)
#     print('---',author[i].text)
# print(soup)

# _________________________________________________________________

# url = "https://scrapingclub.com/exercise/list_basic/?page=1"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# quote = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
# for i in quote:
#     name = i.find('h4', class_='card-title').text.strip()
#     prise = i.find('h5').text
#     print(f'{prise} за {name}')

# _________________________________________________________________
#
data1 = '19:33:02'
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

while current_time != data1:
    current_time = now.strftime("%H:%M:%S")
    if current_time == data1:
        break


url = "https://www.yandex.ru"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

quote = soup.find_all('div', class_="widget__content weather__content-outer")
sity = soup.find_all("span", class_="geolink__reg")
for i in sity:
    sityy = i.text
    siti = f"Сейчас мы находимся в {sityy}е"
for i in quote:
    temp = i.find("div", class_="weather__temp").text
    meteo = f"Сейчас в {sityy}е {temp}"

engine = pyttsx3.init()
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

engine.say(meteo)
engine.say(siti)
engine.runAndWait()