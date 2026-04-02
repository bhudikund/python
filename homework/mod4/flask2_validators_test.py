import unittest
from flask2_validators import app

class TestCode(unittest.TestCase):

    valid_data = {
        'email': 'test@gmail.com',
        'phone': '621233',
        'name': 'Name',
        'address': 'Street',
        'index': '123456',
        'comment': 'Tcomment'
    }
    invalid_data = {
        'email': 'invalid_email',
        'phone': '11111111111111111111',
        'name': '',
        'address': '',
        'index': '123456Invalid',
        'comment': 'Tcomment'
    }

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = '/registration'
        self.data = self.valid_data.copy()

    def test_valid_email(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        self.data['email'] = self.invalid_data['email']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('email' in response_text)

    def test_valid_phone(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        self.data['phone'] = self.invalid_data['phone']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('phone' in response_text)

    def test_valid_name(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_name(self):
        self.data['name'] = self.invalid_data['name']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('name' in response_text)

    def test_valid_address(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_address(self):
        self.data['address'] = self.invalid_data['address']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('address' in response_text)

    def test_valid_index(self):
        response = self.app.post(self.base_url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_index(self):
        self.data['index'] = self.invalid_data['index']
        response = self.app.post(self.base_url, data=self.data)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 400)
        self.assertTrue('index' in response_text)

if __name__ == '__main__':
    unittest.main()