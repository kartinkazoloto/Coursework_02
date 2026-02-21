from tabulate import tabulate


def filter_aeroplanes(aeroplanes, filter_words):
    """Фильтрация списка по ключевым словам"""
    filter_words_lower = set(word.lower() for word in filter_words)
    return [
        plane for plane in aeroplanes
        if plane["country"].lower() in filter_words_lower
    ]


def get_aeroplanes_by_altitude(aeroplanes, altitude_range):
    """Фильтрация списка по диапазону высот"""
    pass


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
