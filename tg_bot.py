import os
import random

import telebot
from dotenv import load_dotenv


load_dotenv()
tg_bot_token = os.environ.get("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_bot_token)


questions  = {
    "Сколько всего типов данных в Python?": ["4", "5", "3", "7"],
    
    "Какое улучшение исправит код?:\nfile_ext = filename.split('.')[-1]": ["split(filename)[-1]", "split('.')[-1]", "split()[-1]", "splitext из модуля os.path"],

    "Что делает метод .append()?": ["Такого метода не сущетсвует", "Удаляет элемент из списка", "Разделяет список", "Добавляет элемент в список"],

    "Что такое список?": ["Переменная окружения", "Метод", "Библиотека", "Структура данных"], 

    "Кортеж это изменяемый тип данных или нет?": ["Наверное да", "Изменяемый", "Кортеж-это не тип данных", "Неизменяемый"],

    "Что такое лямбда-функция в Python?": ["Такой функции нет", "Функция без аргументов", "Функция без ключевого слова def", "Функция, которые не привязанная к имени"],

    "Где правильно должны быть собраны import'ы по PEP8?": ["После констант", "В конце кода", "между ф-циями", "В начале кода"],
    
    "Time-это встроенная библиотека?": ["Скорее да,чем нет", "Нет","Частично","Да"],
    
    "Как объявить функцию?": ["Через ключевое слово fun", "Через ключевое слово class", "Легко и просто", "Через ключевое слово def"],
    
    "С какого числа начинается индексация?": ["C 2", "С 1", "С -1", "C 0"],
    
    "Сколько элементов можно хранить в кортеже?": ["29", "10", "100", "Безгранное кол-во"],
    
    "Будет ли работать этот код?:\n class = 'Основы Python'\n print(class)": ["Без понятия", "Нет", "Выдаст ошибку", "Да"],
    
    "Сколько библиотек можно импортировать в один проект?": ["100", "10", "50", "Безгранное кол-во"],
    
    "Как получить данные от пользователя?": ["Функция int()", "Функция get()", "Через консоль", "Функция input()"],
    
    "Какая библиотека отвечает за время?": ["seconds", "Time", "hours", "time"],
    
    "Какая функция выводит что-либо в консоль?": ["output()", "input()", "split()", "print()"],
    
    "Заполните пропуск в утверждении : Метод _______ умеет заменять одну часть строки на другую.": [".choise()", ".reform()", ".retard()", ".replace()"],
    
    "С помощью кавычек вы можете создавать _______, \n пример:'Lleanin'": ["Классы", "Функции", "Методы", "Строки"],
    
    "Словарь – это объект, содержащий пары ключ-_______.": ["Смысл", "Замок", "Дверь", "Значение"],
    
    "Метод _______ умеет подставлять переменные в строку.": [".sample()", ".replace()", ".restaraut()", ".format()"],
    
    "_______ — это то, что вы передаёте функциям.": ["Списки", "Ключи", "Значения", "Аргументы"],
    
    "Списки могут содержать объекты любого типа: числа, строки, словари, другие списки.": ["Словари и числа", "Другие списки и строки", "Только строки", "Да"],
    
    "Вы запустили код и получили KeyError. Какой метод словаря можно использовать, чтобы такой ошибки не случилось?": ["given()", "give()", "file_get()", "get()"],
    
    "Есть два вида аргументов: _______ и именованные.": ["Исчисляемые", "Позированные", "Неисчисляемые", "Позиционные"],
    
    "Функция sorted принимает на вход итерируемый объект и возвращает отсортированный список.": ["Возвращает отсортированную строку", "Нет", "Возвращает отсортированный словарь", "Да"],
    
    "Пароли, токены и прочую чувствительную информацию необходимо сохранять в ____-файл.": ["main.py", ".gitignore", ".gitattributes", ".env"],
    
    "Python лучше чем Java?)": ["И то и то хорошо!", "Нет", "Да", "Мама я программист"],
    
    "Для чего нужна конструкция try/except?": ["Для перебора элементов в последовательности", "Для попыток", "Для выводов", "Для обработки исключений"],
    
    "Где правильно должны быть собраны функции по PEP8?": ["До обработки исключений", "После if 'name' == 'main':", "До констант", "После import'ов"],
    
    "Что делает метод .upper()?": ["Поднимает строку вверх", "Возращает копию строки, в которой все буквы в маленьком регистре", "Выбирает из списка элемент", "Возращает копию строки, в которой все буквы в большом регистре"]
}

modes = {
    "5 вопросов": 5 ,
    "15 вопросов": 15,
    "30 вопросов": 30
}

user_scores = {}


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("5 вопросов", "15 вопросов", "30 вопросов")
    bot.send_message(message.chat.id, "Привет! Выбери режим:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in modes.keys())
def handle_mode_choice(message):
    user_id = message.from_user.id
    user_scores[user_id] = 0
    num_questions = modes[message.text]
    quiz_questions = random.sample(list(questions .keys()), num_questions)
    ask_question(message, quiz_questions, 0)


def ask_question(message, quiz_question_names, current_question_counter):
    chat_id = message.chat.id
    current_question_name = quiz_question_names[current_question_counter]
    current_question_values = questions[current_question_name]
    correct_answer = current_question_values[::][-1]
    random.shuffle(current_question_values)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*current_question_values)

    bot.send_message(chat_id, f"{current_question_counter + 1}. {current_question_name}", reply_markup=markup)
    bot.register_next_step_handler(message, check_answer, quiz_question_names, current_question_counter, correct_answer)


def check_answer(message, quiz_questions, current_question, correct_answer):
    user_id = message.from_user.id
    user_answer = message.text.strip()

    if user_answer == correct_answer:
        user_scores[user_id] += 1

    if current_question + 1 < len(quiz_questions):
        ask_question(message, quiz_questions, current_question + 1)
    else:
        show_result(message, user_scores[user_id])


def show_result(message, score):
    bot.send_message(message.chat.id, f"Твой результат:\nПравильные ответы: {score}/{len(user_scores)}")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "Извини, я не понимаю. Выбери режим, чтобы начать викторину.")


bot.polling(none_stop=True, interval=0)
