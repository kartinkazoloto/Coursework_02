import unittest
from src.aeroplanes import Aeroplane


class TestAeroplane(unittest.TestCase):
    def setUp(self):
        """Создаёт экземпляр Aeroplane для тестов"""
        self.aeroplane = Aeroplane(
            callsign="SWR438A",
            country="Switzerland",
            velocity=189.7,
            altitude=4267.2,
            on_ground=False
        )

    def test_initialization(self):
        """Проверка корректной инициализации"""
        self.assertEqual(self.aeroplane.callsign, "SWR438A")
        self.assertEqual(self.aeroplane.country, "Switzerland")
        self.assertEqual(self.aeroplane.velocity, 189.7)
        self.assertEqual(self.aeroplane.altitude, 4267.2)
        self.assertFalse(self.aeroplane.on_ground)

    def test_comparison_methods(self):
        """Проверка методов сравнения"""
        a1 = Aeroplane("A1", "RU", 100, 5000, False)
        a2 = Aeroplane("A2", "US", 150, 3000, False)

        self.assertTrue(a1 > a2)  # 5000 > 3000
        self.assertFalse(a1 < a2)

    def test_cast_to_object_list_valid_data(self):
        """Тест преобразования с валидными данными"""
        opensky_resp = {
            "states": [
                [None, "SWR438A ", "Switzerland", None, None, None, None, 4267.2, False, 189.7]
            ]
        }

        result = Aeroplane.cast_to_object_list(opensky_resp)

        expected = [{
            "callsign": "SWR438A ",
            "country": "Switzerland",
            "altitude": 4267.2,
            "velocity": 189.7,
            "on_ground": False
        }]

        self.assertEqual(result, expected)

    def test_cast_to_object_list_empty_data(self):
        """Тест с пустым списком данных"""
        with self.assertRaises(ValueError):
            Aeroplane.cast_to_object_list({})
