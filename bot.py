# https://5sim.net/v1/guest/products/ghana/virtual2
# https://5sim.net/v1/guest/products/russia/any

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
		t = requests.get("https://5sim.net/v1/guest/products/ghana/virtual2").text
		t = json.loads(t.replace("'",'"'))
		google = t["google"]['Qty']
		if google != google_last:
			bot.send_message(message.chat.id, "Есть " + str(google) +  " шт.")
			google_last = google
		else:
			google_last = google
		time.sleep(10)

bot.polling(none_stop=True)