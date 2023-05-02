def get_all_types(list, type):
	all_types = []

	for obj in list:
		all_types.append(obj.get(type))

	return set(all_types)
	
def get_gamesales_by_types(list, given_type):
	types = sorted(tuple(get_all_types(list, given_type)))
	all_type_sales = []

	for type in types:
		all_type_sales.append({type: []})
	
	for obj in list:
		index = types.index(obj.get(given_type))
		all_type_sales[index][obj.get(given_type)].append(obj)
	
	return tuple(all_type_sales)

def sum_gamesales_by_territory(list, territory):
	sum = 0

	for obj in list:
		sum += obj[territory]
	
	return round(sum, 2)

def sum_type_sales(tuple_list, sales_keys, type):
	only_sales = {}

	for platform, data in tuple_list:
		only_sales[type] = platform

		for sale in sales_keys:
			only_sales[sale] = sum_gamesales_by_territory(data, sale)
	
	return only_sales

def create_type_sales(list, sales_keys, type):
	new_list = []

	for obj in list:
		new_list.append(sum_type_sales(obj.items(), sales_keys, type))

	return new_list



