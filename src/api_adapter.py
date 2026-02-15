from requests import get
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
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
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

        response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)
        print(response.status_code)
        data = response.json()
        print(data)
        #Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get('boundingbox')

        #Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = get(url=self.opensky_url, params=params)
        print(response.status_code)

        #Пример ответа от opensky-network можно посмотреть в задании курсовой.
        self.aeroplanes = response.json()
        # print(self.aeroplanes)
        return self.aeroplanes

if __name__ == '__main__':

    api = APIAdapter()
    aeroplanes = api.get_aeroplanes('Canada')
    print("     Hello              _________")
    print(aeroplanes)


