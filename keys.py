# === Тексты сообщений =========================================================
import json
from pprint import pprint

import requests

textStart = "Я помогу вам узнать курсы валют относительно Российского Рубля\n\
Напомню вчерашний курс относительно Российского Рубля\n\
Покажу список доступных валют доступен\n\
Помогу провести конвертацию валют\n\
Нажмите /help для получения списка команд"

textHelp = "Для конвертации валют нужно ввести запрос формата:\n<имя валюты> \
\n<в какую валюту перевести> \
\n<количество переводимой валюты>\nПример запроса:\nEUR RUB 9"

listCommend = "Справка по командам /help\n\
Курсы валют относительно Российского Рубля /Kurs_k_RUB\n\
Вчерашний курс относительно RUB /YesterdayKurs\n\
Список доступных валют доступен /values\n "

textConvertionException = "Ошибка!!!\nError!!!"

# ====== Словарь полученный из нужного JSON ====================================
r1 = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
Base1 = json.loads(r1.content)
Base1 = Base1.get('Valute')
pprint(Base1)

r2 = requests.get(f'https://www.cbr-xml-daily.ru/latest.js')
Base2 = json.loads(r2.content)
Base2 = Base2.get('rates')
pprint(Base2)


# ==============================================================================

keys = {
    'RUB': 'RUB',
    'AUD': 'AUD',
    'AZN': 'AZN',
    'GBP': 'GBP',
    'AMD': 'AMD',
    'BYN': 'BYN',
    'BGN': 'BGN',
    'BRL': 'BRL',
    'HUF': 'HUF',
    'VND': 'VND',
    'HKD': 'HKD',
    'GEL': 'GEL',
    'DKK': 'DKK',
    'AED': 'AED',
    'USD': 'USD',
    'EUR': 'EUR',
    'EGP': 'EGP',
    'INR': 'INR',
    'IDR': 'IDR',
    'KZT': 'KZT',
    'CAD': 'CAD',
    'QAR': 'QAR',
    'KGS': 'KGS',
    'CNY': 'CNY',
    'MDL': 'MDL',
    'NZD': 'NZD',
    'NOK': 'NOK',
    'PLN': 'PLN',
    'RON': 'RON',
    'XDR': 'XDR',
    'SGD': 'SGD',
    'TJS': 'TJS',
    'THB': 'THB',
    'TRY': 'TRY',
    'TMT': 'TMT',
    'UZS': 'UZS',
    'UAH': 'UAH',
    'CZK': 'CZK',
    'SEK': 'SEK',
    'CHF': 'CHF',
    'RSD': 'RSD',
    'ZAR': 'ZAR',
    'KRW': 'KRW',
    'JPY': 'JPY',
}
