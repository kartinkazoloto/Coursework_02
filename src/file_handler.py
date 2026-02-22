import json
from abc import ABC, abstractmethod
from pathlib import Path
import os


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
    save_dir = Path(__file__).parent.parent / "data"
    filename = f"data.json"
    path_file = save_dir / filename

    def __init__(self, filename: str = filename):
        self.__filename = filename

    @property
    def filename(self) -> str:
        """Геттер для имени файла."""
        return self.__filename

    def load(self):
        if not os.path.exists(self.__filename):
            return []

        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла {self.__filename}: {e}")
            return []


    def save(self, data):

        try:
            with open(self.path_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Данные успешно сохранены в {self.__filename}")
        except IOError as e:
            print(f"Ошибка при записи в файл {self.__filename}: {e}")


    def add_aeroplane(self, new_aeroplane):
        """Добавление информации о самолете(ах) в файл"""
        new_aeroplane_dict = ({
                    "callsign" : new_aeroplane.callsign,
                    "country" : new_aeroplane.country,
                    "altitude": new_aeroplane.altitude,
                    "velocity": new_aeroplane.velocity,
                    "on_ground": new_aeroplane.on_ground
                })
        current_dict = self.load()
        if not isinstance(new_aeroplane_dict, dict):
            raise TypeError
        if any(plane.get("callsign") == new_aeroplane_dict.get("callsign") for plane in current_dict):
            print(f"Самолёт с callsign '{new_aeroplane_dict.get('callsign')}' уже существует, пропускаем")
            return
        current_dict.append(new_aeroplane_dict)
        self.save(current_dict)


    def delete_aeroplane(self, aeroplane_to_del):
        """Удаление инфо о самолете(ах) из файла"""
        aeroplane_to_del_dict = ({
            "callsign": aeroplane_to_del.callsign,
            "country": aeroplane_to_del.country,
            "altitude": aeroplane_to_del.altitude,
            "velocity": aeroplane_to_del.velocity,
            "on_ground": aeroplane_to_del.on_ground
        })

        current_data = self.load()
        initial_count = len(current_data)

        # Фильтруем данные — оставляем только те, у которых callsign не совпадает
        filtered_data = [plane for plane in current_data
                         if plane.get("callsign") != aeroplane_to_del_dict.get("callsign")]

        # Если количество не изменилось — запись не найдена
        if len(filtered_data) == initial_count:
            print(f"Самолёт с callsign '{aeroplane_to_del_dict.get('callsign')}' не найден")
            return False

        # Сохраняем отфильтрованные данные
        self.save(filtered_data)
        print(f"Удален самолёт с callsign '{aeroplane_to_del_dict.get('callsign')}'")
        return True
