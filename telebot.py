import telebot
from telebot import types


bot = telebot.TeleBot('7090418413:AAG4tAfm7BDZQeZ560VoMZg6-8HnHZ6y0Zo')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🚨')
    markup.row(btn1)
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, f'Привет, {message.from_user.first_name} :). Я могу угадать фильм по описанию. Чтобы начать, нажми на кнопочку')


@bot.message_handler()
def handle_text_doc(message):
    if message.text == '🚨':
        bot.send_message(message.chat.id, 'Теперь, пришли описание загаданного фильма')

#сохраняет сообщение пользователя в файл
def record_message(message):
    f = open('test.txt', 'w+')
    try:
        message_to_save = message.text
        f.write(message_to_save)
    finally:
        f.close()


bot.infinity_polling(none_stop=True)
