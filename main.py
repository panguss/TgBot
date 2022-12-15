import hh
new_all = hh.all_n
new_avzp = round(hh.av_zp)
import telebot
from telebot import types
bot = telebot.TeleBot('5962050755:AAGOcxWWOQhEpiZXV_pNYFgtobjPXLAm6oU')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    amount = types.KeyboardButton('Количество предложенных вакансий')
    average = types.KeyboardButton('Cредняя зарплата')
    website = types.KeyboardButton('Посетить сайт')
    markup.add( amount, average, website)
    bot.send_message(message.chat.id, 'Привет! Выбери нужную команду:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Посетить сайт":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Посетить сайт", url='https://chelyabinsk.hh.ru/')
        markup.add(button1)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку,чтобы ознакомиться с вакансиями на платформе hh.ru))".format(message.from_user), reply_markup=markup)
    if message.text == "Количество предложенных вакансий":
        bot.send_message(message.chat.id,f'Количество предложенных вакансий: {new_all}')
    if message.text == "Cредняя зарплата":
        bot.send_message(message.chat.id,f'Cредняя зарплата: {new_avzp} руб.')


bot.polling(none_stop=True)
