def get_all_platforms(list):
	all_platforms = []

	for obj in list:
		all_platforms.append(obj.get('Platform'))

	return set(all_platforms)
	
def get_gamesales_by_platforms(list):
	platforms = sorted(tuple(get_all_platforms(list)))
	all_platform_sales = []

	for platform in platforms:
		all_platform_sales.append({platform: []})
	
	for obj in list:
		index = platforms.index(obj.get('Platform'))
		all_platform_sales[index][obj.get('Platform')].append(obj)
	
	return tuple(all_platform_sales)

def sum_gamesales_by_territory(list, territory):
	sum = 0

	for obj in list:
		sum += obj[territory]
	
	return round(sum, 2)

def sum_platform_sales(tuple_list, sales_keys):
	only_sales = {}

	for platform, data in tuple_list:
		only_sales['Platform'] = platform

		for sale in sales_keys:
			only_sales[sale] = sum_gamesales_by_territory(data, sale)
	
	return only_sales

def create_platform_sales(list, sales_keys):
	new_list = []

	for obj in list:
		new_list.append(sum_platform_sales(obj.items(), sales_keys))

	return new_list



