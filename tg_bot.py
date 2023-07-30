import os
import random

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()
tg_bot_token = os.environ.get("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_bot_token)

questions  = {
    "Сколько всего типов данных в Python?": ["1", "2", "3", "4"],
    
    "Какое улучшение исправит код?:\nfile_ext = filename.split('.')[-1]": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],

    "Что делает метод append?": ["Добавляет элемент в список", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],

    "Что такое список?": ["Структура данных", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"], 

    "Кортеж это изменяемый тип данных или нет?": ["Неизменяемый", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],

    "Для чего нужна последовательность '\n'?": ["Перевод курсора на следующую строку", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],

    "Где правильно должны быть собраны import'ы по PEP8?": ["В начале кода", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Time-это встроенная библиотека?": ["Да", "Нет","Частично","Скорее да,чем нет"],
    
    "Как объявить функцию?": ["Через ключевое слово def", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "С какого числа начинается индексация?": ["C 0", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Сколько элементов можно хранить в кортеже?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Будет ли работать этот код?:\n class = 'Основы Python'\n print(class)": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Сколько библиотек можно импортировать в один проект?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Как получить данные от пользователя?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Какая библиотека отвечает за время?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Какая функция выводит что-либо в консоль?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Заполните пропуск в утверждении : Метод _______ умеет заменять одну часть строки на другую.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "С помощью кавычек вы можете создавать _______, \n пример:'Lleanin'": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Словарь – это объект, содержащий пары ключ-_______.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Метод _______ умеет подставлять переменные в строку.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "_______ — это то, что вы передаёте функциям.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Списки могут содержать объекты любого типа: числа, строки, словари, другие списки.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Вы запустили код и получили KeyError. Какой метод словаря можно использовать, чтобы такой ошибки не случилось?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Есть два вида аргументов: _______ и именованные.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Функция sorted принимает на вход итерируемый объект и возвращает отсортированный список.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Пароли, токены и прочую чувствительную информацию необходимо сохранять в ____-файл.": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Python лучше чем Java?)": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Для чего нужна конструкция try/except?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Где правильно должны быть собраны функции по PEP8?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"],
    
    "Что делает метод .upper()?": ["splitext из модуля os.path", "split('.')[-1]", "split()[-1]", "split(filename)[-1]"]
}


modes = {
    "5": 5,
    "15": 15,
    "30": 30,
}


user_scores = {}


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("5 вопросов", "15 вопросов", "30 вопросов")
    bot.send_message(message.chat.id, "Привет! Выбери режим:", reply_markup=markup)


# Обработчик выбора режима и запуск викторины
@bot.message_handler(func=lambda message: message.text in modes.keys())
def handle_mode_choice(message):
    user_id = message.from_user.id
    user_scores[user_id] = 0  # Обнуляем счет пользователя
    num_questions = modes[message.text]
    quiz_questions = random.sample(list(questions .keys()), num_questions)
    ask_question(message, quiz_questions, 0)


# Функция задает вопрос и предлагает варианты ответов
def ask_question(message, quiz_questions, current_question):
    chat_id = message.chat.id
    question = quiz_questions[current_question]
    answers = questions[question][:-1]
    correct_answer = questions[question][-1]

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*answers)

    bot.send_message(chat_id, f"{current_question + 1}. {question}", reply_markup=markup)
    bot.register_next_step_handler(message, check_answer, quiz_questions, current_question, correct_answer)

# Функция проверяет ответ пользователя и переходит к следующему вопросу или выводит результат
def check_answer(message, quiz_questions, current_question, correct_answer):
    user_id = message.from_user.id
    user_answer = message.text.strip()

    if user_answer == correct_answer:
        user_scores[user_id] += 1

    if current_question + 1 < len(quiz_questions):
        ask_question(message, quiz_questions, current_question + 1)
    else:
        show_result(message, user_scores[user_id])

# Функция выводит результат участника
def show_result(message, score):
    bot.send_message(message.chat.id, f"Твой результат:\nПравильные ответы: {score}/{len(user_scores)}")

# Обработка всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, "Извини, я не понимаю. Выбери режим, чтобы начать викторину.")


bot.polling(none_stop=True, interval=0)
