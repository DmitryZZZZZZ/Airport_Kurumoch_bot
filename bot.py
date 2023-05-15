import telebot
from main import arrived, not_arrived
from telebot import types

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', ])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✈️ Все рейсы")
    btn2 = types.KeyboardButton("🚁 Только ожидаются")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Бот показывает рейсы аэропорта "Курумоч" на текущую дату', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "✈️ Все рейсы":
        bot.send_message(message.chat.id, arrived())
    elif message.text == "🚁 Только ожидаются":
        bot.send_message(message.chat.id, not_arrived())


bot.polling(none_stop=True)




