import unittest
import ci1_finances as ms

class TestMoneyStorage(unittest.TestCase):
    def setUp(self):
        ms.app.config['TESTING'] = True
        ms.app.config['DEBUG'] = False
        ms.storage = {2026: {3: 70, 11: 500, 12: 2000}}
        self.app = ms.app.test_client()

    def test_adding_for_new_date(self):
        self.app.get('/add/20261130/2000')
        self.assertEqual(ms.storage[2026][11], 2500)

    def test_adding_for_exist_date(self):
        self.app.get('/add/20231120/3000')
        self.assertEqual(ms.storage[2023][11], 3000)

    def test_uncorrected_date_format_catch_exception_message(self):
        response = self.app.get('/add/2023-11-20/3000')
        self.assertEqual(response.status_code, 500)

    def test_calculate_data_for_correct_year(self):
        response = self.app.get('/calculate/2025')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'За период 2025 не было совершено трат')

    def test_calculate_data_for_correct_year_and_month(self):
        response = self.app.get('/calculate/2026/12')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'За период 12/2026 траты составили 2000')

    def test_calculate_data_for_unexist_date(self):
        ms.storage = {}
        response = self.app.get('/calculate/2025')
        response_text = response.data.decode()
        self.assertEqual(response_text, 'За период 2025 не было совершено трат')