
class Aeroplane:
    __slots__ = ("_callsign", "_country", "_velocity", "_altitude", "_on_ground")

    def __init__(self, callsign: str, country: str, velocity: float, altitude: float, on_ground: bool):  # м/с  # метры
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
                aircrafts.append(
                    {
                        "callsign": callsign,
                        "country": country,
                        "altitude": altitude,
                        "velocity": velocity,
                        "on_ground": on_ground,
                    }
                )
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
