# === IMPORT ===================================================================
import json

import requests
import telebot

from Bot import bot
from keys import textConvertionException, Base2, keys


# === Exception ================================================================
class ConvertionException(Exception):
    def convert(message: telebot.types.Message):
        bot.send_message(message.chat.id, f"{textConvertionException}")


class ValutsConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(
                f"Зачем сравнивать одно и тоже? {quote} = {base}"
            )
        try:
            quote_ticker = keys[quote.upper()]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base.upper()]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(
                f"Не удалось обработать количество {amount}, должно быть число"
            )

        r3 = requests.get(f'https://api.exchangerate-api.com/v4/latest/{quote}')
        total_base = round(
            float(amount) * json.loads(r3.content)['rates'][base], 2
        )
        return total_base

# ==============================================================================
