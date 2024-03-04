import telebot
from time import sleep
from telebot import types
bot = telebot.TeleBot('your bot token')
from translate import Translator
translator = Translator(from_lang='en', to_lang='ru')
import randfacts

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('СЛУЧАЙНЫЙ ФАКТ')
    markup.row(btn1)
    bot.send_message(message.chat.id,f'Привет {message.from_user.first_name} :)\nЯ умею генерировать случайные факты\nНажми кнопку СЛУЧАЙНЫЙ ФАКТ если хочешь узнать что то новое)', reply_markup=markup)
@bot.message_handler(content_types = ['text'])
def send_fact(message):
    if message.text == 'СЛУЧАЙНЫЙ ФАКТ':
        bot.send_message(message.chat.id,translator.translate(randfacts.get_fact(False)))


while True:
    try:
        if __name__ == "__main__":
            bot.polling(none_stop=True, timeout=123)
    except Exception as _ex:
        print(_ex)
        sleep(5)