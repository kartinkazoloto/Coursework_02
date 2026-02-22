from src.sort_aeroplanes import (filter_aeroplanes, get_aeroplanes_by_altitude,
                                 sort_aeroplanes, get_top_aeroplanes, print_aeroplanes)

def test_filter_aeroplanes(aeroplanes, filtered_words):
    filtered_list = filter_aeroplanes(aeroplanes, filtered_words)
    assert len(filtered_list) == 9


def test_get_aeroplanes_by_altitude(aeroplanes):
    filtered_list = get_aeroplanes_by_altitude(aeroplanes, '13000 - 15000')
    assert len(filtered_list) == 4


def test_sort_aeroplanes(aeroplanes):
    filtered_list = sort_aeroplanes(aeroplanes)
    assert filtered_list[0] == {
            "callsign": "TLK822  ",
            "country": "Canada",
            "altitude": 13716,
            "velocity": 242.54,
            "on_ground": False
        }

def test_get_top_aeroplanes(aeroplanes):
    filtered_list = get_top_aeroplanes(aeroplanes, 1)
    assert filtered_list[0] == {
            "callsign": "ASP716  ",
            "country": "Canada",
            "altitude": 1371,
            "velocity": 179.36,
            "on_ground": False
        }