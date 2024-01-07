# === IMPORT ===================================================================
import telebot

from Bot import bot, d_text, kurs_instance
from extensions import ConvertionException, ValutsConverter
from keys import textStart, listCommend, textHelp


# === Команды ===================================================++++===========

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.chat.username}")
    bot.send_message(message.chat.id, textStart)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id, f"{message.chat.username} Я всего лишь бот, чем я могу помочь..."
    )
    bot.send_message(message.chat.id, f"{listCommend}\n{textHelp}")


@bot.message_handler(commands=['values'])
def get_values(message):
    bot.send_message(message.chat.id, d_text)


@bot.message_handler(commands=["Kurs_k_RUB"])
def get_kurs_k_rub(message):
    bot.send_message(message.chat.id, kurs_instance.get_kurs_k_rub())


@bot.message_handler(commands=["YesterdayKurs"])
def get_yesterday_kurs_k_rub(message):
    bot.send_message(message.chat.id, kurs_instance.get_yesterday_kurs_k_rub())
# --- Обработка запроса пользователя -------------------------------------------
@bot.message_handler(content_types=['text'])
def convert_currency(message: telebot.types.Message):
    try:
        text = message.text.upper().split()
        if len(text) == 3 and text[2].isdigit():
            quote, base, amount = text
            total_base = ValutsConverter.convert(quote, base, amount)
            result_text = f"{amount} {quote} = {total_base} {base}"
            bot.send_message(message.chat.id, result_text)
        elif len(text) == 3:
            raise ConvertionException(
                f"Убедитесь, что количество указано корректно (число).\nПример запроса: EUR RUB 9"
            )
        else:
            raise ConvertionException(
                f"Запрос должен быть в формате: <имя валюты> <в какую валюту перевести> <количество переводимой валюты>.\nПример запроса: EUR RUB 9"
            )

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")


bot.polling(none_stop=True)  # чтобы бот не останавливался
# ==============================================================================
