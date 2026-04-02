from freezegun import freeze_time
import unittest

from ci1_hello_world import app

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_hello_world(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)


    @freeze_time("2026-03-15")
    def test_sunday_greetings(self):
        greeting = 'Хорошего воскресенья'
        username = 'user'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(greeting in response_text)

    @freeze_time("2026-03-15")
    def test_username_greetings(self):
        greeting = 'Хорошего воскресенья'
        username = 'Хорошей среды'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(greeting in response_text)