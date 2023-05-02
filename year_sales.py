def get_all_years(list):
	all_years = []

	for obj in list:
		all_years.append(obj.get('Year'))

	return set(all_years)

def get_gamesales_by_years(list):
	years = sorted(tuple(get_all_years(list)))
	all_year_sales = []

	for year in years:
		all_year_sales.append({year: []})
	
	for obj in list:
		index = years.index(obj.get('Year'))
		all_year_sales[index][obj.get('Year')].append(obj)
	
	return tuple(all_year_sales)

def sum_gamesales_by_territory(list, territory):
	sum = 0

	for obj in list:
		sum += obj[territory]
	
	return round(sum, 2)

def sum_year_sales(tuple_list, sales_keys):
	only_sales = {}

	for year, data in tuple_list:
		only_sales['Year'] = year

		for sale in sales_keys:
			only_sales[sale] = sum_gamesales_by_territory(data, sale)
	
	return only_sales

def create_year_sales(list, sales_keys):
	new_list = []

	for obj in list:
		new_list.append(sum_year_sales(obj.items(), sales_keys))

	return new_list