import telebot
import requests


response = requests.get('https://tv.yandex.ru')
print(response.text)