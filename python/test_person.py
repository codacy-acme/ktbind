import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person()
    
    def test_set_name(self):
        # Test adding a single name
        id1 = self.person.set_name('Alice')
        self.assertEqual(id1, 0)
        self.assertEqual(self.person.get_name(0), 'Alice')
        
        # Test adding multiple names
        id2 = self.person.set_name('Bob')
        self.assertEqual(id2, 1)
        self.assertEqual(self.person.get_name(1), 'Bob')
        
        # Test adding empty name
        id3 = self.person.set_name('')
        self.assertEqual(id3, 2)
        self.assertEqual(self.person.get_name(2), '')

    def test_get_name(self):
        # Test getting existing name
        self.person.set_name('Alice')
        self.assertEqual(self.person.get_name(0), 'Alice')
        
        # Test getting non-existent user
        self.assertEqual(self.person.get_name(99), 'There is no such user')
        
        # Test getting name at boundary
        self.person.set_name('Bob')
        self.assertEqual(self.person.get_name(1), 'Bob')

    def test_tower_of_hanoi(self):
        # Test TowerOfHanoi with n=1
        # We'll use unittest.mock to capture the print output
        import io
        from unittest.mock import patch
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.person.TowerOfHanoi(1, 'A', 'C', 'B')
            self.assertEqual(fake_output.getvalue().strip(), 
                           'Move disk 1 from source A to destination C')
        
        # Test TowerOfHanoi with n=2
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            self.person.TowerOfHanoi(2, 'A', 'C', 'B')
            expected_output = '\n'.join([
                'Move disk 1 from source A to destination B',
                'Move disk 2 from source A to destination C',
                'Move disk 1 from source B to destination C'
            ])
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    def test_fibonacci_of(self):
        # Test base cases
        self.assertEqual(self.person.fibonacci_of(0), 0)
        self.assertEqual(self.person.fibonacci_of(1), 1)
        
        # Test recursive cases
        self.assertEqual(self.person.fibonacci_of(2), 1)
        self.assertEqual(self.person.fibonacci_of(3), 2)
        self.assertEqual(self.person.fibonacci_of(4), 3)
        self.assertEqual(self.person.fibonacci_of(5), 5)

if __name__ == '__main__':
    unittest.main()