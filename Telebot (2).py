import telebot as tb
from telebot import types
import random as rd
import time
import datetime as dt
import logging
import sqlite3

# Сценарии
priv = ['Добрый день, товарищ', 'Приветствую вас', 'Здравтсуйте, друг мой', 'День добрый', 'Хэллоу']
net = ['Извините, отказано', 'Ответ системы - "Нет"', 'Товарищ, отказано']
da = ['Статус - "ДА', 'Естествено', 'TRUE (Da)']
bot_pohval = ['Лучший помощник', 'JARVIS только лучше', 'Супер мега пупер помощник', 'Танос среди помщников в мире']
fakt = [['Интересный факт: Первый человек в космоесу был из СССР', 'Факт про космос'],
        ['В начале у тебя 20 отчимов', 'Факт про дотеров']]

# Токен бота
token = '6282629918:AAGxRTkieARpHeQyliDtn4y0k2UHr8Wh4wE'
bot = tb.TeleBot(token)

# Уведомление о запуске
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# Факт
def fak(message):
    if 1 == rd.randint(0, 5):
        bot.send_message(message.chat.id, f'{fakt[rd.randint(0, 1)][1]}. Хотите узнать?')


# Подтверждение о готовности
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton('Да, готов')
    b2 = types.KeyboardButton('Нет')
    b4 = types.KeyboardButton('Почему такое название бота?')
    b3 = types.KeyboardButton('Сайт - для регистрации.')
    keyboard.add(b1, b2, b3, b4)
    bot.send_message(message.chat.id, f'{priv[rd.randint(0, 4)]}. Вы готовы к общению?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def keyboard_gotov(message):
    if message.text == 'Сайт - для регистрации.':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton('я тупой')
        b2 = types.KeyboardButton('Назад в ад')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Сайт Хабр", url='http://127.0.0.1:8080/')
        button2 = types.InlineKeyboardButton("Сайт Хабр правила", url='http://127.0.0.1:8080/rules')
        button3 = types.InlineKeyboardButton("Сайт Хабр регистрация", url='http://127.0.0.1:8080/Cams')
        markup.add(button1, button2, button3)
        keyboard.add(b1, b2)

        a = bot.send_message(message.chat.id,
                             f"Сэр {message.from_user.username} - Лучше всего перейти на сайт по кнопке")
        a1 = bot.send_photo(message.chat.id,
                            'https://www.meme-arsenal.com/memes/8813fd8b7aa8f1efd97c435c679fa3e1.jpg'.format(
                                message.from_user),
                            reply_markup=markup)
        a2 = bot.send_audio(message.chat.id,
                            'https://cs1-65v4.vkuseraudio.net/p4/e3d1633c928938.mp3?extra=UwZawvd-y72N_CZYKP_lO04smUYKNGu3zxoXpl2drPQrkQ_PQpmg1ZsnEiMuElrCudU3abDH4V95MNh3aCNhU067lyStRejERVIJIJRQYUCRtA1KIL6q8hOK1Gtp1shMJhCNrCtovzc-IAENvvhsoNAp&long_chunk=1',
                            reply_markup=keyboard)

    # Если тупой
    if message.text == 'я тупой':
        v = bot.send_message(message.chat.id,
                         f"Сэр {message.from_user.username} -=====")
        time.sleep(3)
        video = open('livsi.mp4', 'rb')
        bot.delete_message(message.chat.id, v.id)
        bot.send_video(message.chat.id, video)
    # Готов
    if message.text == 'Почему такое название бота?':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'А тебе это важно?', reply_markup=keyboard)
        time.sleep(1)
        bot.send_photo(message.chat.id,
                       'https://risovach.ru/upload/2014/06/mem/tvoe-vyrazhenie-lica_53549909_orig_.jpeg')
        start_message(message)
    # Помощник

    if message.text == 'Нет':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Всмысле не можешь.', reply_markup=keyboard)
        time.sleep(2)
        bot.send_photo(message.chat.id,
                       'https://risovach.ru/upload/2014/01/mem/kakoy-pacan_41226535_orig_.jpeg')
        b1 = types.KeyboardButton('Назад в ад')
        b3 = types.KeyboardButton('О боте')
        keyboard.add(b1, b3)
        bot.send_message(message.chat.id, f'Куда дальше',
                         reply_markup=keyboard)

    if message.text.lower() == 'о боте':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         f'{priv[rd.randint(0, 3)]} Если вы не поняли то я......{priv[rd.randint(0, 3)]}',
                         reply_markup=keyboard)
        bot.send_photo(message.chat.id,
                       'https://timeweb.com/ru/community/article/f9/f9126325726f89cede1e0ec2c3f8e501.jpg')
        markup = types.InlineKeyboardMarkup(row_width=1)
        button3 = types.InlineKeyboardButton(text='Понял', callback_data="reset")
        markup.add(button3)
        bot.send_message(message.chat.id, f'Я есть {bot_pohval[rd.randint(0, 3)]}', reply_markup=markup)
        # bot.send_message(message.chat.id, f'Я есть {bot_pohval[rd.randint(0, 3)]}', reply_markup=markup)

    if message.text == 'Назад в ад':
        start_message(message)

    if message.text == 'Да, готов':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 = types.KeyboardButton('Добавить')
        b2 = types.KeyboardButton('Изменить')
        b3 = types.KeyboardButton('Узнать')
        b4 = types.KeyboardButton('Назад в ад')
        keyboard.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, 'Выберети что хотите сделать', reply_markup=keyboard)

    if message.text == 'Узнать':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите логин и пароль')
        bot.register_next_step_handler(message, car_name)

    if message.text == 'Добавить':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите новый - логин и пароль')
        bot.register_next_step_handler(message, new_name)

    if message.text == 'Изменить':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Введите логи и пароль того пользватеоя которого хотите изменить')
        bot.register_next_step_handler(message, up_name)


def new_name():
    print('---------')


def up_name(message):
    con = sqlite3.connect('regs.db')
    cur = con.cursor()
    # st = ("""UPDATE regs SET loginn = duration*2 WHERE genre =
    #                (SELECT id FROM genres WHERE title = 'фантастика')""").fetchall()
    # cur.execute(st)
    result = cur.execute("""SELECT login FROM regs""").fetchall()
    result1 = cur.execute("""SELECT password FROM regs""").fetchall()
    con.close()
    bot.send_message(message.chat.id, f"{result[0][0]} --- L {result1[0][0]} --- P")
    a, b = map(str, message.text.split())
    if a in result[0][0]:
        if b in result1[0][0]:
            bot.send_message(message.chat.id, f"ок")

        elif b not in result1[0][0]:
            bot.send_message(message.chat.id, f"- {net[rd.randint(0, 2)]}")
    elif a not in result[0][0]:
        bot.send_message(message.chat.id, f"- {net[rd.randint(0, 2)]}")

    a1, b1 = map(str, message.text.split())
    bot.send_message(message.chat.id, f"{a1} --- L {b1} --- P выбрали")


def car_name(message):
    con = sqlite3.connect('regs.db')
    cur = con.cursor()

    x = []
    x1 = []
    a, b = map(str, message.text.split())
    # st = f"""INSERT INTO regs(1)(login, password) VALUES({a}, {b})"""
    # cur.execute(st)
    bot.send_message(message.chat.id, f"{a} --- L {b} --- P")

    result = cur.execute("""SELECT login FROM regs""").fetchall()
    result1 = cur.execute("""SELECT password FROM regs""").fetchall()
    con.close()
    bot.send_message(message.chat.id, f"{result[0][0]} --- L {result1[0][0]} --- P")
    if a in result[0][0]:
        bot.send_message(message.chat.id, f"{a} - Логин есть)")
        if b in result1[0][0]:
            bot.send_message(message.chat.id, f"ок")
        else:
            bot.send_message(message.chat.id, f"{b} - неn пароль")


    else:
        bot.send_message(message.chat.id, f"{a} - неn такого логина")


@bot.message_handler(func=lambda call: True)
def message_handler(call):
    if call.message:
        if call.data == "reset":
            # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # bot.send_message(chat_id=call.message.chat.id, text='--------')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            start_message(call.message)
            # start_message()


bot.polling(non_stop=True)
