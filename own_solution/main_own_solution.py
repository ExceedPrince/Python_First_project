import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from file_handler import get_dicts_from_csv, write_dicts_to_csv
from data_conversion import get_sales_keys, modify_sales_numbers
from type_sales import get_gamesales_by_types, create_type_sales

def wish_to_continue_question(was_wrong = False):
	local_answer = ""
	return_answer = ""

	while True:
		if was_wrong == True:
			local_answer = input("Érvénytelen adat! Újrapróbálja? (Y/N): ")
		else:
			local_answer = input("Szeretne másik '.csv' fájlt írni? (Y/N): ")

		if local_answer == "Y":
			return_answer = True
			break
		elif local_answer == "N":
			return_answer = False
			break
		else:
			print("Kérjük, válaszoljon 'Y' vagy 'N' karakterekkel!")
	
	return return_answer


def call_user_for_writing():
	wish = True
	options = ["Platform", "Year", "Genre", "Publisher"]

	while wish == True:
		answer = input("Válassza ki, milyen '.csv' listát szeretne íratni (Platform, Year, Genre, Publisher): ")
		
		if answer in options:
			video_game_sales = modify_sales_numbers(get_dicts_from_csv('vg_sales.csv'))

			summerized_platform_feed = create_type_sales(get_gamesales_by_types(video_game_sales, answer), get_sales_keys(video_game_sales), answer)
			print(write_dicts_to_csv(answer.lower() + '_sales.csv', summerized_platform_feed))

			wish = wish_to_continue_question()

		else:
			wish = wish_to_continue_question(True)

call_user_for_writing()