from file_handler import get_dicts_from_csv, write_dicts_to_csv
from data_conversion import get_sales_keys, modify_sales_numbers
from platform_sales import get_gamesales_by_platforms, create_platform_sales
from year_sales import get_gamesales_by_years, create_year_sales
from genre_sales import get_gamesales_by_genres, create_genre_sales

video_game_sales = modify_sales_numbers(get_dicts_from_csv('vg_sales.csv'))

summerized_platform_feed = create_platform_sales(get_gamesales_by_platforms(video_game_sales), get_sales_keys(video_game_sales))
print(write_dicts_to_csv('platform_sales.csv', summerized_platform_feed))

summerized_year_feed = create_year_sales(get_gamesales_by_years(video_game_sales), get_sales_keys(video_game_sales))
print(write_dicts_to_csv('year_sales.csv', summerized_year_feed))

summerized_genre_feed = create_genre_sales(get_gamesales_by_genres(video_game_sales), get_sales_keys(video_game_sales))
print(write_dicts_to_csv('genre_sales.csv', summerized_genre_feed))