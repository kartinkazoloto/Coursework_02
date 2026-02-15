from api_adapter import APIAdapter



class Aeroplane:
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


    def __lt__(self, other):
        """Метод сравнения меньше"""
        return self.altitude < other.altitude


    def __gt__(self, other):
        """Метод сравнения Больше"""
        return self.altitude > other.altitude


    def __len__(self):
        return len(f'Количество самолетов на земле {self.on_ground}')


    def cast_to_object_list(self):
        """Преобразование набора данных в список объектов"""
        if not aeroplanes:
            raise ValueError("получен пустой список")
        states_aeroplanes = aeroplanes.get("states", [])
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
                # print(aircrafts)
            return aircrafts
        except (ValueError, IndexError, TypeError) as e:
            print(f"Ошибка при обработке самолёта: {e}")





if __name__ == '__main__':
    api = APIAdapter()
    aeroplanes = api.get_aeroplanes('Canada')
    print("     Hello              _________")
    print(aeroplanes)
    aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
    print("     Hello      2        _________\n  \n  \n")
    print(aeroplanes)

