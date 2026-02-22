from src.aeroplanes import Aeroplane
from src.api_adapter import APIAdapter
from src.country import validate_country
from src.file_handler import JSONSaver
from src.sort_aeroplanes import (
    filter_aeroplanes,
    get_aeroplanes_by_altitude,
    get_top_aeroplanes,
    print_aeroplanes,
    sort_aeroplanes,
)


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    while True:
        country = str(input("Введите название страны: "))
        is_valid = validate_country(country)
        if is_valid:
            break

    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input("Введите названия стран для фильтрации по стране регистрации: ")

    altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000
    api = APIAdapter()
    aeroplanes = api.get_aeroplanes(country)

    aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print_aeroplanes(top_aeroplanes)
    json_saver = JSONSaver()
    json_saver.save(top_aeroplanes)


if __name__ == "__main__":
    user_interaction()
