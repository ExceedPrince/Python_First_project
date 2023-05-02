def get_sales_keys(list):
	sales_keys = []
	for obj in list:
		for elem in obj:
			if elem not in sales_keys and "sales" in elem.lower():
				sales_keys.append(elem)
	return sales_keys

def modify_sales_numbers(list):
	sales_keys = get_sales_keys(list)
	
	for obj in list:
		for row in obj:
			if row in sales_keys:
				obj[row] = float(obj[row])

	return list
