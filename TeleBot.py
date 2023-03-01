import telebot

import config
import weatherapi

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def repit(message):
    response = weatherapi.get_weather(message.text)
    bot.send_message(message.chat.id, "\U00002744" + str(response['current']['temp_c']))

bot.polling(none_stop=True)
