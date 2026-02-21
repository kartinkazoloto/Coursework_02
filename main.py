from src.aeroplanes import Aeroplane
from src.sort_aeroplanes import (filter_aeroplanes,
                            get_aeroplanes_by_altitude, sort_aeroplanes,
                            get_top_aeroplanes, print_aeroplanes)
from src.api_adapter import APIAdapter
from src.file_handler import JSONSaver

# # Создание экземпляра класса для работы с API сайтов с самолетами
# api = ApiService()
#
# # Получение информации о самолетах с opensky-network.org
# aeroplanes = api.get_aeroplanes("Spain")
#
# # Преобразование набора данных в список объектов
# aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
#
# # Пример работы конструктора класса с одним самолетом
# aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18, False)
#
# # Сохранение информации в файл
# json_saver = JSONSaver()
# json_saver.add_aeroplane(aeroplane)
# json_saver.delete_aeroplane(aeroplane)

# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
    altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print_aeroplanes(top_aeroplanes)


if __name__ == "__main__":
    # user_interaction()
    api = APIAdapter()
    # country = input("Введите название страны: ")
    input_country = "turkey"
    aeroplanes = api.get_aeroplanes(input_country)
    print("     Hello              _________")
    print(aeroplanes)
    aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
    print("     Hello      2        _________\n ")
    print(aeroplanes)
    print(len(aeroplanes))
    aeroplane = Aeroplane("PGT694  ", "United States", 268.79, 10203.18, False)
    print(type(aeroplane))
    json_saver = JSONSaver()
    print(aeroplane.callsign)
    json_saver.add_aeroplane(aeroplane)
    print(len(aeroplanes))
    json_saver.delete_aeroplane(aeroplane)
    print(len(aeroplanes))

    # top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    top_n = 5
    # filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
    filter_words = "Turkey"
    # altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000
    altitude_range = 100000 - 150000

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)
    print(filtered_aeroplanes)
    # ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)
    #
    # sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    # top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    # print_aeroplanes(top_aeroplanes)