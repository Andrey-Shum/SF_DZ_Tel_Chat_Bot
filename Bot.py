# === IMPORT ===================================================================
import telebot
from config import TOKEN
from keys import Base1


# ==============================================================================

class Kurs:
    """
    Класс для получения списков на текущую дату и прошлую
    относительно Российского рубля.
    """

    def __init__(self, base):
        self.base = base

    def get_kurs_k_rub(self):  # Курс относительно RUB
        text = "Курс относительно RUB \n"
        res = []
        for Char_Code, valuetss in self.base.items():
            nominal = valuetss["Nominal"]
            name_v = valuetss['Name']
            valueta = valuetss['Value']
            res.append(
                f"=== {name_v}\nЗа {nominal} {Char_Code} : {valueta:.2f} RUB"
            )
        text += '\n'.join(res)
        return text

    def get_yesterday_kurs_k_rub(self):  # Вчерашний курс относительно RUB
        text = "Вчерашний курс относительно RUB \n"
        res = []
        for Char_Code, previouss in self.base.items():
            nominal = previouss["Nominal"]
            name_v = previouss['Name']
            previouss = previouss['Previous']
            res.append(
                f"=== {name_v}\nЗа {nominal} {Char_Code} : {previouss:.2f} RUB"
            )
        text += '\n'.join(res)
        return text


kurs_instance = Kurs(Base1)

text_kurs_k_rub = kurs_instance.get_kurs_k_rub()
text_yesterday_kurs_k_rub = kurs_instance.get_yesterday_kurs_k_rub()


# ------ Доступные валюты ------------------------------------------------------
class Values:
    def __init__(self, base):
        self.base = base

    def get_values(self):
        d_text = "Доступные валюты:\n"
        lst = ["RUB : Российский рубль"]  # Список для хранения значений
        for Code_Char, valuets in self.base.items():
            lst_vr = Code_Char + " : " + valuets["Name"]
            lst.append(lst_vr)
        d_text += "\n".join(lst)
        return d_text


text_values = Values(Base1)

d_text = text_values.get_values()
# === Переменные ===============================================================
values_instance = Values(Base1)
kurs_instance = Kurs(Base1)
# ==============================================================================
bot = telebot.TeleBot(TOKEN)
# ==============================================================================
