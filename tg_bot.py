import os
import random

import telebot
from dotenv import load_dotenv
from telebot import types


load_dotenv()
tg_bot_token = os.environ.get("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_bot_token)
score = 0


tasks_ru = ["Сколько всего тиов данных в Python?",
            "Какое улучшение исправит код?:file_ext = filename.split('.')[-1]",
            "Что делает метод append?",
            "Что такое список?",
            "Кортеж это изменяемый тип данных или нет?", 
            "Для чего нужна последовательность '\n'?",
            "Где правильно должны быть собраны import'ы по PEP8?",
            "Time-это встроенная библиотека?",
            "Как объявить функцию?",
            "С какого числа начинается индексация?",
            "Сколько элементов можно хранить в кортеже?",
            "Будет ли работать этот код?:\n class = 'Основы Python'\n print(class)",
            "Сколько библиотек можно импортировать в один проект?",
            "Как получить данные от пользователя?",
            "Какая библиотека отвечает за время?",
            "Какая функция выводит что-либо в консоль?",
            "Заполните пропуск в утверждении : Метод _______ умеет заменять одну часть строки на другую.",
            "С помощью кавычек вы можете создавать _______, \n пример:'Devman'",
            "Словарь – это объект, содержащий пары ключ-_______.",
            "Метод _______ умеет подставлять переменные в строку.",
            "_______ — это то, что вы передаёте функциям.",
            "Списки могут содержать объекты любого типа: числа, строки, словари, другие списки.",
            "Вы запустили код и получили KeyError. Какой метод словаря можно использовать, чтобы такой ошибки не случилось?",
            "Есть два вида аргументов: _______ и именованные.",
            "Функция sorted принимает на вход итерируемый объект и возвращает отсортированный список.",
            "Пароли, токены и прочую чувствительную информацию необходимо сохранять в ____-файл.",
            "Python лучше чем Java?)",
            "Для чего нужна конструкция try/except?",
            "Где правильно должны быть собраны функции по PEP8?",
            "Что делает метод .upper()?",

        ]   


answers_ru = ["3",
            "splitext из модуля os.path",
            "Добавляет элемент в список?",
            "Структура данных","Неизменяемый",
            "Перевод курсора на следующую строку",
            "В начале кода",
            "Да",
            "Через ключевое слово def",
            "C 0",
            "Неограниченное кол-во",
            "Да",
            "Неограниченное кол-во",
            "Метод input()",
            "time",
            "print()",
            ".replace()",
            "Строки",
            "Значение",
            ".format()",
            "Аргументы",
            "Да",
            ".get()",
            "Позиционные",
            "Да",
            ".env",
            "ДА",
            "Для обработки исключений",
            "После import'ов",
            "Возращает копию строки, в которой все буквы сконвертированы к большому регистру"
            ]
 
    
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn_1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_ru = types.KeyboardButton("🇷🇺 Русский")
        btn_en = types.KeyboardButton('🇬🇧 English')
        markup.add(btn_ru, btn_en)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    if message.text == '🇷🇺 Русский':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Легкий режим(5 Вопросов)")
        btn2 = types.KeyboardButton("Средний режим(15 Вопросов)")
        btn3 = types.KeyboardButton("Тяжелый режим(30 Вопросов)")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберите на какое кол-во вопросов вы собираетесь ответить:", reply_markup=markup)

    elif message.text == "Легкий режим(5 Вопросов)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        answers = []
        Button_1 = types.KeyboardButton("5")
        Button_2 = types.KeyboardButton(answers_ru[0])
        Button_3 = types.KeyboardButton("2")
        Button_4 = types.KeyboardButton("8")
        markup.add(Button_1, Button_2, Button_3, Button_4)
        bot.send_message(message.from_user.id, "1.{}:".format(tasks_ru[0]), reply_markup=markup)
        answers.append(Button_1,Button_2,Button_3,Button_4)

    if message.text == answers_ru[0]:
        score+=1

    elif message.text == answers:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Button_1 = types.KeyboardButton("5")
        Button_2 = types.KeyboardButton(answers_ru[1])
        Button_3 = types.KeyboardButton("2")
        Button_4 = types.KeyboardButton("8")
        markup.add(Button_1, Button_2, Button_3, Button_4)
        bot.send_message(message.from_user.id, "2.{}:", reply_markup=markup).format(tasks_ru[1])

    elif message.text == "Средний режим(15 Вопросов)":
        print("hello")
    elif message.text == "Тяжелый режим(30 Вопросов)":
        print("hello")

    elif message.text == 'en English':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Easy Mode (5 Questions)")
        btn2 = types.KeyboardButton("Medium Mode (15 Questions)")
        btn3 = types.KeyboardButton("Heavy Mode (30 Questions)")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберите на какое кол-во вопросов вы собираетесь ответить:", reply_markup=markup)
    

bot.polling(none_stop=True, interval=0)