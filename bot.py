# https://vak-sms.com/api/getCountNumber/?apiKey=f581ed49e50b4608946cee8e9c17e556&service=gl&country=kz&price
# https://vak-sms.com/api/getCountNumber/?apiKey=f581ed49e50b4608946cee8e9c17e556&service=gl&country=id&price
# https://vak-sms.com/api/getCountNumber/?apiKey=f581ed49e50b4608946cee8e9c17e556&service=gl&country=ru&price

import config
import telebot
import requests
import json
import time

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Поиск начался")
	google_last = 0
	while True:	
		t = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=f581ed49e50b4608946cee8e9c17e556&service=gl&country=kz&price").text
		google = t.split()[1][:-1]
		if google != google_last:
			bot.send_message(message.chat.id, "Есть " + str(google) +  " шт.")
			google_last = google
		else:
			google_last = google
		time.sleep(20)

bot.polling(none_stop=True)
