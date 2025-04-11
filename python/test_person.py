import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person()
    
    def test_set_name_returns_correct_id(self):
        # Test adding first user
        id1 = self.person.set_name('Alice')
        self.assertEqual(id1, 0)
        
        # Test adding second user
        id2 = self.person.set_name('Bob')
        self.assertEqual(id2, 1)
    
    def test_get_name_returns_correct_name(self):
        # Test getting existing user
        self.person.set_name('Alice')
        self.assertEqual(self.person.get_name(0), 'Alice')
        
        # Test multiple users
        self.person.set_name('Bob')
        self.assertEqual(self.person.get_name(1), 'Bob')
    
    def test_get_name_invalid_id(self):
        # Test getting non-existent user
        self.assertEqual(self.person.get_name(99), 'There is no such user')
        
        # Test getting user with negative id
        self.assertEqual(self.person.get_name(-1), 'There is no such user')
    
    def test_name_list_persistence(self):
        # Test that names are correctly stored in the list
        names = ['Alice', 'Bob', 'Charlie']
        ids = []
        
        for name in names:
            ids.append(self.person.set_name(name))
        
        # Verify all names are stored and retrievable
        for i, name in enumerate(names):
            self.assertEqual(self.person.get_name(i), name)

if __name__ == '__main__':
    unittest.main()