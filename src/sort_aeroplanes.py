from tabulate import tabulate

from src.country import validate_country


def filter_aeroplanes(aeroplanes: list, filter_words: str) -> list:
    """Фильтрация списка по ключевым словам"""
    filter_words_lower = set(country.strip().lower() for country in filter_words.split(","))
    for country in filter_words_lower:
        if validate_country(country):
            continue
    filtered_list: list = []

    for plane in aeroplanes:
        if plane["country"].lower() in filter_words_lower:
            filtered_list.append(plane)
    return filtered_list


def get_aeroplanes_by_altitude(aeroplanes: list, altitude_range: str) -> list:
    """Фильтрация списка по диапазону высот"""
    ranged_aeroplanes: list = []
    min_alt, max_alt = map(float, [x.strip() for x in altitude_range.split("-")])
    if min_alt > max_alt:
        raise ValueError(f"Минимальное значение {min_alt} не может быть больше максимального {max_alt}")

    for plane in aeroplanes:
        alt: float = plane["altitude"]
        if alt is None:
            continue
        if min_alt <= alt <= max_alt:
            ranged_aeroplanes.append(plane)

    return ranged_aeroplanes


def sort_aeroplanes(ranged_aeroplanes: list) -> list:
    """Сортировка списка по убыванию высоты"""
    aeroplanes = sorted(ranged_aeroplanes, key=lambda x: x["altitude"], reverse=True)
    return aeroplanes


def get_top_aeroplanes(aeroplanes: list, top_n: int) -> list:
    """Фильтрация списка по ТОП-N позициям"""
    top: list = aeroplanes[:top_n]
    return top


def print_aeroplanes(top_aeroplanes: list):
    """Вывод итогового списка"""
    print(tabulate(top_aeroplanes, headers="keys", tablefmt="grid"))
