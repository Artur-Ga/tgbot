import telebot
import webbrowser

bot = telebot.TeleBot('6275171896:AAGVi51lKjlE9DQZ3Xr5C4ssdRfCIVFOpLw')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com/')  #

@bot.message_handler(commands=['contact', 'info'])
def contact(message):
    webbrowser.open('https://www.youtube.com/')  #

@bot.message_handler(commands=['new', 'news'])
def news(message):
    webbrowser.open('https://www.youtube.com/')  #


@bot.message_handler(commands=['start', 'hello', 'привет'])  # тригер на слова с /...
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['инфо'])
def main(message):
    bot.send_message(message.chat.id, f'Привет!{message.from_user.first_name} {message.from_user.last_name}')  # f строки и обращение через мес к фром юзер к ферст и ласт

@bot.message_handler()
def info(message):
    if message.text.lower() == 'пока':
        bot.send_message(message.chat.id, f'поки поки!')
    if message.text.lower() == 'я илья':
        bot.send_message(message.chat.id, f'Здравствуйте! Мой господин!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)