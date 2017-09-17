#import requests
#from bs4 import BeautifulSoup
#from multiprocessing import Pool
import pickle
#import Info
import random
#from link import give_list, give_list2
type_1 = 'аниме'
type_2 = 'биография'
type_3 = 'боевик'
type_4 = 'вестерн'
type_5 = 'военный'
type_6 = 'детектив'
type_7 = 'детский'
type_8 = 'для взрослых'
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
type_21 = 'новости'
type_22 = 'приключения'
type_23 = 'реальное ТВ'
type_24 = 'семейный'
type_25 = 'сериал'
type_26 = 'спорт'
type_27 = 'ток-шоу'
type_28 = 'триллер'
type_29 = 'ужасы'
type_30 = 'фантастика'
type_31 = 'фильм-нуар'
type_32 = 'фэнтези'
type_33 = 'церемония'

genre_list =[type_1,
type_2,
type_3,
type_4,
type_5 ,
type_6 ,
type_7 ,
type_8 ,
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
type_21 ,
type_22 ,
type_23 ,
type_24 ,
type_25 ,
type_26 ,
type_27 ,
type_28 ,
type_29 ,
type_30,
type_31,
type_32,
type_33]

fields = ['image', 'name', 'genre', 'rate', 'country', 'year', 'description']

# genre_types = {'аниме': [], 'биография':[], 'боевик':[], 'вестерн':[], 'военный': [], 'детектив': [], 'детский': [],
# 		 'для взрослых':[], 'документальный':[], 'драма':[], 'игра':[], 'история':[], 'комедия':[],
# 		 'концерт':[], 'короткометражка':[], 'криминал':[], 'мелодрама':[], 'музыка':[],
# 		 'мультфильм':[], 'мюзикл':[], 'новости':[],
# 		  'приключения':[], 'реальное ТВ':[], 'семейный':[], 'сериал':[], 'спорт':[], 'ток-шоу':[],
# 		  'триллер':[], 'ужасы':[], 'фантастика':[], 'фильм-нуар':[], 'фэнтези':[], 'церемония':[] }

# def get_html(url):
# 	response = requests.get(url)

# 	return response.text

# def get_info(html):
# 	soup = BeautifulSoup(html, 'html.parser')

# 	info_finder = soup.find('div', id = 'content_block')#.find_all('div', class_= 'name')#.find('div', class_='item_NO_HIGHLIGHT_')
# 	#print (info_finder)
# 	#print (links_finder)
# 	# links = []
# 	# tmp = info_finder[0].find('a').text.strip()
# 	# print (tmp)
# 	# for i in links_finder:
# 	# 	tmp = i.find('a').get('href')
# 	# 	link = 'https://www.kinopoisk.ru' + tmp
# 	# 	links.append(link)
# 	# return links



# 	#for i in info_finder:
# 	try:
# 		name = info_finder.find('h1', class_= 'moviename-big').text.strip()
# 		#print (name)
# 	except:
# 		name = ''
# 	try:	
# 		genre = []
# 		genre_html = info_finder.find('span', itemprop= 'genre').find_all('a')
# 		for i in genre_html:
# 			genre1 = i.text.strip()
# 			genre.append(genre1)

# 	except:
# 	 	genre = []
# 	try:
# 		info = info_finder.find_all('div', style="position: relative")#.find('a').text.strip()
# 	except:
# 		info = ''
# 	try:
# 		year= info[0].find('a').text.strip()
# 	except:
# 		year = ''
# 	try:
# 		country = info[1].find('a').text.strip()
# 	except:
# 		country = ''
# 	try:
# 		rate = info_finder.find('table', id = 'syn').find('span', class_ = 'rating_ball').text.strip()
# 	except:
# 		rate = ''
# 	try:
# 		description = info_finder.find('table', id = 'syn').find('div', class_ = 'brand_words film-synopsys').text.strip()
# 	except:
# 		description = ''

# 		#number = i
# 	all_info = {"name": name,
# 					"year": year,
# 					"rate": rate, 
# 					"country": country,
# 					"genre": genre,
# 					"description": description
# 					#'number': number
# 					}
	#return all_info
	# for k in all_info['genre']:
	# 	#print (i)
# 	for i in genre_list:
# 		#print (all_info['genre'])
# 		for j in all_info['genre']:
# 			if i == j:
# 				genre_types[i].append(all_info)
# 				# print (genre_types[i])
# 		#print (genre_types)

# def sort(url):
# 	all_info = get_info(get_html(url))
# 	for i in genre_list:
# 		#print (all_info['genre'])
# 		for j in all_info['genre']:
# 			if i == j:
# 				genre_types[i].append(all_info)


# # def random(msg):
# # 	for i in genre_list:
# # 		if msg == i:
# # 			answer = random.choice(genre_types[genre_list[i]])
# # 			return answer


# def parsing_all(url):
# 	#print (url)
# 	html = get_html(url)
# 	get_info(html)



#def data_file(url):
# 	html = get_html(url)
# 	data = get_info(html)
#def image():


def enter(msg):
	response = ''
	#print (genre_list)
	#num = 0
	# links = give_list()
	# links2 = give_list2()
	# links3 = [links, links2]
	#print (links[0])
	#link = links[0]
	# for i in range(0, 78):
	# 	for j in range(0, 50):
	# 		url = give_link(i, j)
			#print (url)
			# sort(get_info(get_html(url)))
			#type (info)
	# for i in links3:
	# 	with Pool(20) as p:
	# 		p.map(parsing_all, i)

	
	# with open('dump.dat', 'wb') as dump_out:
	# 	pickle.dump(genre_types, dump_out)
	with open('dump_with_trailer.dat', 'rb') as dump_in:
		genre_types= pickle.load(dump_in)
	try:
		num = random.randint(0, len(genre_types[msg]))
	except:
		return ''
	#print (random.randint(0, len(genre_types['для взрослых'])))
	#print (len(genre_types['аниме']))
			#print (genre_types.values())
	#print (genre_types['биография'])#[0])#['name'])
	return genre_types[msg][num]
	# for i in fields:
	# 	if i == 'genre':
	# 			response += i + ": "
	# 			#print (genre_types[k][0])
	# 			for j in genre_types[msg][num][i]:
	# 				response += j + ', '
	# 			response+= '\n'

	# 	else:
	# 			#print (genre_types[msg][num]['name'])
	# 			try:
	# 				response +=i+': ' +str(genre_types[msg][num][i])+'\n'
	# 			except:
	# 				return 'Введите распозноваемую команду'
	# return (genre_types[msg][0]['name'])
	# for k in genre_list:
	# 	for i in fields:
	# 		if i == 'genre':
	# 			response += i + ": "
	# 			#print (genre_types[k][0])
	# 			for j in genre_types[k][0][i]:
	# 				response += j + ', '
	# 			response+= '\n'
			#else:
				#print (genre_types[k][0]['name'])
				#response +=i+': ' +str(genre_types[k][0][i])+'\n'
	#return response

	# for i in range(1, 81):
	# 	if i == 1:
	# 		url = 'https://www.kinopoisk.ru/top/navigator/m_act%5Brating%5D/1:/m_act%5Bis_film%5D/on/m_act%5Bis_mult%5D/on/order/rating/page/1/#results'
					
	# 	else:
	# 		url = 'https://www.kinopoisk.ru/top/navigator/m_act%5Brating%5D/1:/m_act%5Bis_film%5D/on/m_act%5Bis_mult%5D/on/order/rating/page/' +str(i) +'/#results'
	# 	all_links = get_info(get_html(url))


		# for i in all_links:
		# 	print (i)
	#print ('done')

if __name__ == '__main__':
	enter(msg)


# film[]


# for i in 