# beeline
# lycamobile
# megafon
# mts
# rostelecom
# tele2

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
		t = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&price").text
		time.sleep(60)
		google = t.split()[1][:-1]
		if google != google_last:
			google_beeline = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&operator=beeline&price").text
			time.sleep(60)
			google_lycamobile = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&operator=lycamobile&price").text
			time.sleep(60)
			google_megafon = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&operator=megafon&price").text
			time.sleep(60)
			google_mts = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&operator=mts&price").text
			time.sleep(60)
			google_rostelecom = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&operator=rostelecom&price").text
			time.sleep(60)
			google_tele2 = requests.get("https://vak-sms.com/api/getCountNumber/?apiKey=489f298673794679af08f0165f1acfa9&service=gl&country=ru&operator=tele2&price").text
			
			google_beeline = google_beeline.split()[1][:-1]
			google_lycamobile = google_lycamobile.split()[1][:-1]
			google_megafon = google_megafon.split()[1][:-1]
			google_mts = google_mts.split()[1][:-1]
			google_rostelecom = google_rostelecom.split()[1][:-1]
			google_tele2 = google_tele2.split()[1][:-1]

			bot.send_message(message.chat.id, "Всего: " + str(google) + " шт.\nbeeline: " + str(google_beeline) + " шт.\nlycamobile: " + str(google_lycamobile) + " шт.\nmegafon: " + str(google_megafon) + " шт.\nmts: " + str(google_mts) + " шт.\nrostelecom: " + str(google_rostelecom) + " шт.\ntele2: " + str(google_tele2) + " шт.")
			google_last = google
		else:
			google_last = google
		

bot.polling(none_stop=True)
