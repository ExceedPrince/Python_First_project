from file_handler import get_dicts_from_csv, write_dicts_to_csv
from data_conversion import get_sales_keys, modify_sales_numbers
from platform_sales import get_all_platforms, get_gamesales_by_platforms, sum_gamesales_by_territory, sum_platform_sales, create_platform_sales

from year_sales import get_all_years, get_gamesales_by_years, sum_year_sales, create_year_sales


""" test_video_game_sales = get_dicts_from_csv('vg_sales.csv')
print(test_video_game_sales)
print(write_dicts_to_csv('test_sales.csv', test_video_game_sales)) """

""" test_video_game_sales = get_dicts_from_csv('vg_sales.csv')
print(get_sales_keys(test_video_game_sales))
print(modify_sales_numbers(test_video_game_sales)) """

""" test_video_game_sales = get_dicts_from_csv('vg_sales.csv')[:3]
print(get_all_platforms(test_video_game_sales))
print(get_gamesales_by_platforms(test_video_game_sales)) """

""" test_video_game_sales = modify_sales_numbers(get_dicts_from_csv('vg_sales.csv')[:3])
print(sum_gamesales_by_territory(test_video_game_sales, 'Global_Sales'))
print(sum_platform_sales(get_gamesales_by_platforms(test_video_game_sales)[0].items(), get_sales_keys(test_video_game_sales))) """

""" test_video_game_sales = modify_sales_numbers(get_dicts_from_csv('vg_sales.csv')[:3])
print(create_platform_sales(get_gamesales_by_platforms(test_video_game_sales), get_sales_keys(test_video_game_sales))) """

""" test_video_game_sales = get_dicts_from_csv('vg_sales.csv')[:3]
print(get_all_years(test_video_game_sales))
print(get_gamesales_by_years(test_video_game_sales)) """

""" test_video_game_sales = modify_sales_numbers(get_dicts_from_csv('vg_sales.csv')[:3])
print(create_year_sales(get_gamesales_by_years(test_video_game_sales), get_sales_keys(test_video_game_sales))) """