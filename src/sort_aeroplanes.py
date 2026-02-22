from tabulate import tabulate

from src.country import validate_country


def filter_aeroplanes(aeroplanes, filter_words):
    """Фильтрация списка по ключевым словам"""
    filter_words_lower = set(country.strip().lower() for country in filter_words.split(","))
    for country in filter_words_lower:
        if validate_country(country):
            continue
    filtered_dict = []

    for plane in aeroplanes:
        if plane["country"].lower() in filter_words_lower:
            filtered_dict.append(plane)
    return filtered_dict


def get_aeroplanes_by_altitude(aeroplanes, altitude_range):
    """Фильтрация списка по диапазону высот"""
    ranged_aeroplanes = []
    min_alt, max_alt = map(int, [x.strip() for x in altitude_range.split("-")])
    if min_alt > max_alt:
        max_alt, min_alt = map(int, [x.strip() for x in altitude_range.split("-")])
    for plane in aeroplanes:
        if plane["altitude"] is None:
            continue
        if plane.__le__(max_alt) and plane.__ge__(min_alt):
            ranged_aeroplanes.append(plane)

    return ranged_aeroplanes


def sort_aeroplanes(ranged_aeroplanes):
    """Сортировка списка по убыванию высоты"""
    aeroplanes = sorted(ranged_aeroplanes, key=lambda x: x["altitude"], reverse=True)
    return aeroplanes


def get_top_aeroplanes(aeroplanes, top_n):
    """Фильтрация списка по ТОП-N позициям"""
    top_5 = aeroplanes[:5]
    return top_5


def print_aeroplanes(top_aeroplanes):
    """Вывод итогового списка"""
    print(tabulate(top_aeroplanes, headers="keys", tablefmt="grid"))
