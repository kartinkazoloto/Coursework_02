import json
from abc import ABC, abstractmethod
from pathlib import Path



class DataFileHandler(ABC):
    """Класс работы с файлом"""

    @abstractmethod
    def add_aeroplane(self, **params):
        """Добавление инфо о самолете(ах) в файл"""
        pass


    @abstractmethod
    def delete_aeroplane(self, **params):
        """Удаление инфо о самолете(ах) из файла"""
        pass


    @abstractmethod
    def save(self, **params):
        """Сохранение информации в новый файл"""
        pass


class JSONSaver(DataFileHandler):
    """Создание JSON"""
    def __init__(self, json_file=None, aeroplanes=[]):
        self.__json_file = json_file
        self.__aeroplanes = aeroplanes


    def add_aeroplane(self, new_aeroplane):
        """Добавление информации"""
        new_aeroplane_dict = ({
                    "callsign" : new_aeroplane.callsign,
                    "country" : new_aeroplane.country,
                    "altitude": new_aeroplane.altitude,
                    "velocity": new_aeroplane.velocity,
                    "on_ground": new_aeroplane.on_ground
                })
        if not isinstance(new_aeroplane_dict, dict):
            raise TypeError

        if any(plane.get("callsign") == new_aeroplane_dict.get("callsign") for plane in self.__aeroplanes):
            print(f"Самолёт с callsign '{new_aeroplane_dict.get('callsign')}' уже существует, пропускаем")
            return
        self.__aeroplanes.append(new_aeroplane_dict)


    def delete_aeroplane(self, aeroplane_to_del):
        """Удаление инфо о самолете(ах) из файла"""
        aeroplane_to_del_dict = ({
            "callsign": aeroplane_to_del.callsign,
            "country": aeroplane_to_del.country,
            "altitude": aeroplane_to_del.altitude,
            "velocity": aeroplane_to_del.velocity,
            "on_ground": aeroplane_to_del.on_ground
        })
        if not isinstance(aeroplane_to_del_dict, dict):
            raise TypeError
        for i in self.__aeroplanes:
            if i.get("callsign") == aeroplane_to_del_dict.get("callsign"):
                del self


    def save(self):
        save_dir = Path(__file__).parent.parent / "data"
        file_name = f"data.json"
        path_file = save_dir / file_name
        with open(path_file, "w", encoding="utf-8") as f:
            json.dump(self.__json_file, f, ensure_ascii=False, indent=2)

