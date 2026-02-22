import unittest


from src.api_adapter import APIAdapter
from unittest.mock import patch, Mock


class TestAPIAdapter(unittest.TestCase):
    def setUp(self):
        """Создаёт экземпляр APIAdapter для тестов"""
        self.adapter = APIAdapter()

    @patch('src.api_adapter.requests.get')
    @patch('src.country.validate_country')
    def test_get_aero_valid_country(self, mock_validate, mock_get):
        # Мокируем валидацию страны
        mock_validate.return_value = (True, "✓ Найдено: Russia")

        # Мокируем ответ Nominatim
        mock_nominatim_response = Mock()
        mock_nominatim_response.raise_for_status.return_value = None
        mock_nominatim_response.json.return_value = [{
            "boundingbox": ["50.0", "60.0", "30.0", "40.0"]
        }]

        # Мокируем ответ OpenSky
        mock_opensky_response = Mock()
        mock_opensky_response.raise_for_status.return_value = None
        mock_opensky_response.json.return_value = {"states": [["test_data"]]}

        # Настраиваем side_effect для последовательных вызовов requests.get
        mock_get.side_effect = [mock_nominatim_response, mock_opensky_response]

        # Вызываем метод __get_aero напрямую
        result = self.adapter._APIAdapter__get_aero("Russia")

        # Проверяем, что результат не None и имеет ожидаемую структуру
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)


