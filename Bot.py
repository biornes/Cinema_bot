import requests
import misk
#from yobit import get_btc
from info_links import enter
from time import sleep
from telebot import types
#from bs4 import BeautifulSoup
#import random
#import os
import telebot
#type_1 = 'аниме'
type_2 = 'биография'
type_3 = 'боевик'
type_4 = 'вестерн'
type_5 = 'военный'
type_6 = 'детектив'
type_7 = 'детский'
#type_8 = 'для взрослых'
type_9 = 'документальный'
type_10 = 'драма'
type_11 = 'игра'
type_12 = 'история'
type_13 = 'комедия'
type_14 = 'концерт'
type_15 = 'короткометражка'
type_16 = 'криминал'
type_17 = 'мелодрама'
type_18 = 'музыка'
type_19 = 'мультфильм'
type_20 = 'мюзикл'
#type_21 = 'новости'
type_22 = 'приключения'
#type_23 = 'реальное ТВ'
type_24 = 'семейный'
type_25 = 'сериал'
type_26 = 'спорт'
#type_27 = 'ток-шоу'
type_28 = 'триллер'
type_29 = 'ужасы'
type_30 = 'фантастика'
type_31 = 'фильм-нуар'
type_32 = 'фэнтези'
#type_33 = 'церемония'

genre_list =[#type_1,
type_2,
type_3,
type_4,
type_5 ,
type_6 ,
type_7 ,
#type_8 ,
type_9 ,
type_10,
type_11 ,
type_12 ,
type_13 ,
type_14,
type_15,
type_16 ,
type_17,
type_18,
type_19 ,
type_20 ,
#type_21 ,
type_22 ,
#type_23 ,
type_24 ,
type_25 ,
type_26 ,
#type_27 ,
type_28 ,
type_29 ,
type_30,
type_31,
type_32
#type_33
]

fields = ['Название', 'Жанр', 'Рейтинг', 'Страна', 'Год', 'Описание']
token = misk.token
URL= 'https://api.telegram.org/bot' + token+ '/'
global last_update_id
last_update_id = 0
tb = telebot.TeleBot(token)


def get_updates():
	url = URL+ 'getupdates'
	r = requests.get(url)
	return r.json()

def get_message():
	
		data = get_updates()


		last_object = data['result'][-1]
		current_update_id = last_object['update_id']
		global last_update_id
		if last_update_id != current_update_id:
			last_update_id = current_update_id
			chat_id = data['result'][-1]['message']['chat']['id']
			try:
				message_text= data['result'][-1]['message']['text']
			except:
				message_text = ''

			message={'chat_id': chat_id,
						'text': message_text}

			return message
		return None

# def send_message(chat_id, text):
# 	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
# 	requests.get(url)

def main():


	keyboard = types.InlineKeyboardMarkup()

	url_1  = 'https://www.kinopoisk.ru/'

	while (True):



	
		response = ''
		answer = get_message()
		if answer != None:
			chat_id = answer['chat_id']
			try:
				text = answer['text']
			except:
				te
			if text == '/start':
				tb.send_message (chat_id, 'Здравствуйте! Я выведу вам фильм снятый начиная с 1990 года.\nЧтобы начать пользоваться ботом достаточно ввести жанр желаемого фильма.\nНапример, "драма"\nЧтобы получить список всех доступных жанров, введите "/genre"')
			elif text == '/genre':
				for i in genre_list:
					response+=i + ', '
				response = response[0:-2]
				tb.send_message (chat_id, response)
			elif text:
				try:
				#send_photo(chat_id, enter(text))
				# folder = os.path.abspath('images')
				# way = folder +'/1.jpg'
					text = text.lower()
					film = enter(text)
					url_1 = film['trailer']
					url_button = types.InlineKeyboardButton(text = 'Трейлер', url=url_1 )
					keyboard.add(url_button)

					#print (film)
					for i in fields:
						if i == 'Жанр':
							response += i + ": "
							#print (genre_types[k][0])
							for j in film[i]:
								response += j + ', '
							response =response[0:-2]
							#[len(response)-2:len(response)-1: 1]
							response+= '\n'
						elif i == "Poster's way":
							continue
						else:
					#print (genre_types[msg][num]['name'])
							#try:
								response +=i+': ' +str(film[i])+'\n'
							#except:
								#send_message(chat_id, 'Введите распозноваемую команду')
					
					
					tb.send_message(chat_id, response, reply_markup=keyboard)
					keyboard = types.InlineKeyboardMarkup()
				except:
					tb.send_message(chat_id, 'Введите распозноваемую команду')
				

				#image = open(film["file_name"], 'rb') 
				#tb.send_photo(chat_id, image)
			else: 
				continue
		#tb.polling()
		sleep(2)

if __name__ == '__main__':
	main()
