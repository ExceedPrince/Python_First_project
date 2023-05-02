def get_all_genres(list):
	all_genres = []

	for obj in list:
		all_genres.append(obj.get('Genre'))

	return set(all_genres)

def get_gamesales_by_genres(list):
	genres = sorted(tuple(get_all_genres(list)))
	all_genre_sales = []

	for genre in genres:
		all_genre_sales.append({genre: []})
	
	for obj in list:
		index = genres.index(obj.get('Genre'))
		all_genre_sales[index][obj.get('Genre')].append(obj)
	
	return tuple(all_genre_sales)

def sum_gamesales_by_territory(list, territory):
	sum = 0

	for obj in list:
		sum += obj[territory]
	
	return round(sum, 2)

def sum_genre_sales(tuple_list, sales_keys):
	only_sales = {}

	for genre, data in tuple_list:
		only_sales['Genre'] = genre

		for sale in sales_keys:
			only_sales[sale] = sum_gamesales_by_territory(data, sale)
	
	return only_sales

def create_genre_sales(list, sales_keys):
	new_list = []

	for obj in list:
		new_list.append(sum_genre_sales(obj.items(), sales_keys))

	return new_list