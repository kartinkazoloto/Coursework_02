from src.api_adapter import APIAdapter
from src.file_handler import JSONSaver


class Aeroplane:
    __slots__ = ('_callsign', '_country', '_velocity', '_altitude', '_on_ground')

    def __init__(
        self,
        callsign: str,
        country: str,
        velocity: float,  # м/с
        altitude: float,   # метры
        on_ground: bool
    ):
        self._callsign = callsign
        self._country = country
        self._velocity = velocity
        self._altitude = altitude
        self._on_ground = on_ground


    @property
    def callsign(self) -> str:
        return self._callsign


    @property
    def country(self) -> str:
        return self._country


    @property
    def velocity(self) -> float:
        return self._velocity


    @property
    def altitude(self) -> float:
        return self._altitude


    @property
    def on_ground(self) -> bool:
        return self._on_ground


    def cast_to_object_list(self):
        """Преобразование набора данных в список объектов"""
        if not self:
            raise ValueError("получен пустой список")
        states_aeroplanes = self.get("states", [])
        aircrafts = []
        try:
            for state in states_aeroplanes:
                callsign = state[1]
                country = state[2]
                altitude = state[7]
                velocity = state[9]
                on_ground = state[8]
                aircrafts.append({
                    "callsign" : callsign,
                    "country" : country,
                    "altitude": altitude,
                    "velocity": velocity,
                    "on_ground": on_ground
                })
            return aircrafts
        except (ValueError, IndexError, TypeError) as e:
            print(f"Ошибка при обработке самолёта: {e}")


    def __le__(self, other) -> bool:
        """Метод сравнения Меньше или равно: <"""
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.altitude <= other.altitude


    def __ge__(self, other):
        """Метод сравнения Больше или равно"""
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.altitude >= other.altitude



# if __name__ == '__main__':
#     api = APIAdapter()
#     # country = input("Введите название страны: ")
#     input_country = "turkey"
#     aeroplanes = api.get_aeroplanes(input_country)
#     print("     Hello              _________")
#     print(aeroplanes)
#     aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
#     print("     Hello      2        _________\n  \n  \n")
#     print(aeroplanes)
#     aeroplane = Aeroplane("UAL1624", "United States", 268.79, 10203.18, False)
#     aeroplane1 = Aeroplane("UAL1620", "United States", 268.79, 10203.18, False)
#     json_saver = JSONSaver()
#     json_saver.add_aeroplane(aeroplane)
#     json_saver.add_aeroplane(aeroplane1)
#     json_saver.delete_aeroplane(aeroplane1)
#
#     # top_n = int(input("Введите количество самолетов для вывода в топ N: "))
#     top_n = 5
#     # filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
#     filter_words = "germany"
#     # altitude_range = input("Введите диапазон высот полета: ")  # Пример: 100000 - 150000
#     altitude_range = 100000 - 150000
#
#     # filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)
#     #
#     # ranged_aeroplanes = get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range)
#     #
#     # sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
#     # top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
#     # print_aeroplanes(top_aeroplanes)
