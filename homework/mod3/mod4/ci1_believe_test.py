import datetime, unittest

from ci1_believe import Person

class TestPerson(unittest.TestCase):
    name = 'Alex'
    birth_year = 1999
    address = '8 marta'
    person = Person(name, birth_year, address)

    def test_get_age(self):
        current_year = datetime.datetime.now().year
        expected_age = current_year - self.birth_year
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), self.name)

    def test_set_name(self):
        new_name = 'Victor'
        self.person.set_name(new_name)
        self.assertEqual(self.person.get_name(), new_name)

    def test_set_address(self):
        new_address = 'Mira 32'
        self.person.set_address(new_address)
        self.assertEqual(self.person.address, new_address)

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), self.address)

    def test_is_homeless(self):
        homeless = Person(self.name, self.birth_year)
        self.assertFalse(self.person.is_homeless())
        self.assertTrue(homeless.is_homeless())