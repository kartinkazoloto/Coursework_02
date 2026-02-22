import pytest


@pytest.fixture
def openstreetmap_resp() -> list:
    # Пример ответа от nominatim.openstreetmap
    return [
        {
            "place_id": 346277167,
            "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
            "osm_type": "relation",
            "osm_id": 1428125,
            "lat": "61.0666922",
            "lon": "-107.9917070",
            "class": "boundary",
            "type": "administrative",
            "place_rank": 4,
            "importance": 0.9082390417046676,
            "addresstype": "country",
            "name": "Canada",
            "display_name": "Canada",
            "boundingbox": ["41.6765597", "83.3362128", "-141.0027500", "-52.3237664"],
        }
    ]


@pytest.fixture
def opensky_resp() -> dict:
    # Пример ответа от opensky-network
    return {
        "time": 1766142246,  # UNIX - время сервера OpenSky(секунды)
        "states": [
            [
                "4b1812",  # ICAO24 — уникальный идентификатор борта
                "SWR438A ",  # Callsign — позывной рейса
                "Switzerland",  # Страна регистрации ВС
                1766166618,  # time_position — время последнего обновления позиции
                1766166618,  # last_contact — время последнего контакта
                -0.0168,  # longitude — долгота(°)
                51.0888,  # latitude — широта(°)
                4267.2,  # baro_altitude — барометрическая  высота(м)
                False,  # on_ground — находится ли самолёт на земле
                189.7,  # velocity — горизонтальная скорость(м / с)
                129.39,  # true_track — курс(градусы)
                14.63,  # vertical_rate — вертикальная  скорость(м / с)
                "null",  # sensors — ID сенсоров(null=неизвестно)
                4282.44,  # geo_altitude — геометрическая высота(м)
                "2061",  # squawk — код ответчика(транспондера)
                False,  # spi — специальный сигнал(emergency / priority)
                0,  # position_source — источник  позиции
            ],
            ...,
        ],
    }

@pytest.fixture
def filtered_words():
    return "Canada"

@pytest.fixture
def aeroplanes():
    return [
        {
            "callsign": "ASP716  ",
            "country": "Canada",
            "altitude": 1371,
            "velocity": 179.36,
            "on_ground": False
        },
        {
            "callsign": "TLK822  ",
            "country": "Canada",
            "altitude": 13716,
            "velocity": 242.54,
            "on_ground": False
        },
        {
            "callsign": "ASP642  ",
            "country": "Canada",
            "altitude": 13106.4,
            "velocity": 190.25,
            "on_ground": False
        },
        {
            "callsign": "TLK833  ",
            "country": "Canada",
            "altitude": 13106.4,
            "velocity": 226.12,
            "on_ground": False
        },
        {
            "callsign": "CFLMK   ",
            "country": "Canada",
            "altitude": 13106.4,
            "velocity": 238.73,
            "on_ground": False
        },
        {
            "callsign": "ASP875  ",
            "country": "Canada",
            "altitude": 12496.8,
            "velocity": 218.48,
            "on_ground": False
        },
        {
            "callsign": "",
            "country": "Canada",
            "altitude": 12496.8,
            "velocity": 242.61,
            "on_ground": False
        },
        {
            "callsign": "BOE729  ",
            "country": "Canada",
            "altitude": 12466.32,
            "velocity": 248.14,
            "on_ground": False
        },
        {
            "callsign": "NOJ90   ",
            "country": "Canada",
            "altitude": 12214.86,
            "velocity": 224.6,
            "on_ground": False
        },
        {
            "callsign": "CGKGN   ",
            "country": "Spain",
            "altitude": 12192,
            "velocity": 215.63,
            "on_ground": False
        }
    ]
