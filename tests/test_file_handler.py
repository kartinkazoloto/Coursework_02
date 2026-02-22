import unittest
from unittest.mock import patch, mock_open
from src.file_handler import JSONSaver
from src.aeroplanes import Aeroplane


class TestJSONSaver(unittest.TestCase):
    def setUp(self):
        """Создаёт экземпляр Aeroplane для тестов"""
        self.handler = JSONSaver()

    @patch('src.file_handler.os.path.exists')
    def test_load_file_not_exists(self, mock_exists):
        mock_exists.return_value = False

        result = self.handler.load()

        self.assertEqual(result, [])

    def test_save(self):
        with patch('builtins.open', mock_open()) as mock_open_func:
            with patch('src.file_handler.os.path.exists') as mock_exists:
                mock_exists.return_value = True
                test_data = [{"callsign": "TEST123", "country": "Russia"}]

                result = self.handler.save(data=test_data)

                self.assertEqual(result, test_data)
                mock_open_func.assert_called_once_with(
                    self.handler.path_file, "w", encoding="utf-8"
                )

    @patch('src.file_handler.JSONSaver.load')
    @patch('src.file_handler.JSONSaver.save')
    def test_add_aeroplane_success(self, mock_save, mock_load):
        # Подготавливаем тестовые данные
        mock_load.return_value = []
        mock_save.return_value = [{"callsign": "SWR438A", "country": "Switzerland"}]

        test_aeroplane = Aeroplane(
            callsign="SWR438A",
            country="Switzerland",
            velocity=189.7,
            altitude=4267.2,
            on_ground=False
        )

        result = self.handler.add_aeroplane(new_aeroplane=test_aeroplane)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["callsign"], "SWR438A")

    @patch('src.file_handler.JSONSaver.load')
    @patch('src.file_handler.JSONSaver.save')
    def test_add_aeroplane_duplicate(self, mock_save, mock_load):
        existing_data = [{"callsign": "SWR438A", "country": "Switzerland"}]
        mock_load.return_value = existing_data
        mock_save.return_value = existing_data  # save возвращает те же данные

        test_aeroplane = Aeroplane(
            callsign="SWR438A",
            country="Switzerland",
            velocity=189.7,
            altitude=4267.2,
            on_ground=False
        )

        with patch('builtins.print') as mock_print:
            result = self.handler.add_aeroplane

    @patch('src.file_handler.JSONSaver.load')
    @patch('src.file_handler.JSONSaver.save')
    def test_delete_aeroplane_success(self, mock_save, mock_load):
        initial_data = [
            {"callsign": "SWR438A", "country": "Switzerland"},
            {"callsign": "DEL123", "country": "Germany"}
        ]
        mock_load.return_value = initial_data
        mock_save.return_value = [{"callsign": "DEL123", "country": "Germany"}]

        aeroplane_to_delete = Aeroplane(
            callsign="SWR438A",
            country="Switzerland",
            velocity=189.7,
            altitude=4267.2,
            on_ground=False
        )

        with patch('builtins.print') as mock_print:
            result = self.handler.delete_aeroplane(aeroplane_to_del=aeroplane_to_delete)
            mock_print.assert_called_with("Удален самолёт с callsign 'SWR438A'")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["callsign"], "DEL123")
