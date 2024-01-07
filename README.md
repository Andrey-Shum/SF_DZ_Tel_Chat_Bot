# Tel_Chat_Bot_SF home work for SkillFactory.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Русский (Russian)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Задание:
Написать Telegram-бота, в котором будет реализован следующий функционал:

1) Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
2) При написании бота необходимо использовать библиотеку pytelegrambotapi.
3) Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
4) При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
5) При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
6) Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.
7) Для парсинга полученных ответов использовать библиотеку JSON.
8) При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
9) Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
10) Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
- имя валюты, цену на которую надо узнать, — base;
- имя валюты, цену в которой надо узнать, — quote; 
- количество переводимой валюты — amount.
11) Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
12) Все классы спрятать в файле extensions.py.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
English (Английский)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Task
Write a Telegram bot that will implement the following functionality:

1) The bot returns the price for a certain amount of currency (euro, dollar or ruble).
2) When writing a bot, you need to use the pytelegrambotapi library.
3) A person should send a message to the bot in the form of <name of the currency whose price he wants to find out> <name of the currency in which to find out the price of the first currency> <quantity of the first currency>.
4) When entering the /start or /help command, the user is shown instructions for using the bot.
5) When entering the /values command, information about all available currencies should be displayed in a readable form.
6) To get the exchange rate, you need to use any convenient API and send requests to it using the Requests library.
7) To parse the received responses, use the JSON library.
8) If a user makes an error (for example, an incorrect or non-existent currency is entered or a number is entered incorrectly), call the ApiException exception that is actually written with the error explanation text.
9) The text of any error indicating the type of error should be sent to the user in messages.
10) To send API requests, describe a class with a static get_price() method that takes three arguments and returns the required amount in currency:
- the name of the currency to find out the price for — base;
- the name of the currency, the price in which you need to find out, — quote;
- the amount of currency to be transferred — amount.
11) The Telegram bot token is stored in a special config (you can use a .py file).
12) Hide all classes in a file extensions.py .
-----------------------------------------------------------------------------------------------------------------------------------------------------------
