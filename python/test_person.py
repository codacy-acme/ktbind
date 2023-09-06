import unittest
from person import Person

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_person(self):
        person = Person()
        person.set_name('yay')
        self.assertEqual(person.get_name(0), 'yay')

if __name__ == '__main__':
    unittest.main()