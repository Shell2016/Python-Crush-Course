import unittest
from city_functions import format_name


class FormatnameTestCase(unittest.TestCase):
    """Тесты для city_functions.py"""

    def test_city_country(self):
        formatted_name = format_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_name = format_name('santiago', 'chile', population=5000000)
        self.assertEqual(
            formatted_name, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
