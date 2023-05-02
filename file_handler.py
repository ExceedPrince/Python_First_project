import os
import csv
import sys

path = os.path.join(os.path.dirname(__file__))

def get_dicts_from_csv(file_name):
	new_list = []

	try:
		file = open(path + "\\" + file_name, "r", encoding='utf-8')

		try:
			file_content = csv.DictReader(file)

			for record in file_content:
				new_list.append(record)

		finally:
			file.close()

	except OSError:
		sys.exit('Hiba a fájl kezelése közben!')

	else:
		return tuple(new_list)

def write_dicts_to_csv(file_name, sales_list):
	try:
		file = open(path + "\\" + file_name, "w", encoding='utf-8')

		try:
			all_keys = []
			for obj in sales_list:
				for key in obj.keys():
					if key not in all_keys:
						all_keys.append(key)

			writer = csv.DictWriter(file, all_keys)
			writer.writeheader()

			for obj in sales_list:
				writer.writerow(obj)

		finally:
			file.close()

	except OSError:
		sys.exit('Hiba a fájl létrehozása közben!')

	else:
		print("Fájl létrehozva!")