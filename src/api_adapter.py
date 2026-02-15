from asyncio import exceptions

import requests
from abc import ABC, abstractmethod


class ApiService(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_aeroplanes(self, **params) -> None:
        pass


class APIAdapter(ApiService):

    def __init__(self) -> None:
        self.__openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.__opensky_url = 'https://opensky-network.org/api/states/all?'
        self.__aeroplanes = None

    def __get_aeroplanes(self, country: str) -> None:
        #Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        headers_nominatim = {
            'User-Agent': 'test-app',
        }

        #Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }
        try:
            response = requests.get(url=self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except requests.exceptions.HTTPError:
            print("HTTP Error")
        #Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get('boundingbox')

        #Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }
        try:

            response = requests.get(url=self.__opensky_url, params=params)
            # print(response.status_code)
            response.raise_for_status()
            #Пример ответа от opensky-network можно посмотреть в задании курсовой.
            self.__aeroplanes = response.json()
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except requests.exceptions.HTTPError:
            print("HTTP Error")
            # print(self.aeroplanes)
        return self.__aeroplanes


    @property
    def get_aeroplanes(self) -> None:
        return self.__get_aeroplanes



if __name__ == '__main__':

    api = APIAdapter()
    aeroplanes = api.get_aeroplanes('Canada')
    print("     Hello              _________")
    print(aeroplanes)


