import unittest
from shared.models.Ring import Ring
from shared.exceptions.ValidationException import ValidationException

class TestRing(unittest.TestCase):
    def test_modulo_addition(self):
        r = Ring(modulo=5)
        self.assertEqual(r.add(2, 3), 0)
        self.assertEqual(r.add(1, 4), 0)
        self.assertEqual(r.add(3, 3), 1)

    def test_modulo_multiplication(self):
        r = Ring(modulo=5)
        self.assertEqual(r.mul(2, 3), 1)
        self.assertEqual(r.mul(4, 2), 3)
        self.assertEqual(r.mul(3, 3), 4)

    def test_custom_addition(self):
        elements = ['a', 'b', 'c']
        add_table = [
            ['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']
        ]
        mul_table = [
            ['a', 'a', 'a'],
            ['a', 'b', 'c'],
            ['a', 'c', 'b']
        ]
        r = Ring(elements=elements, add_table=add_table, mul_table=mul_table)
        self.assertEqual(r.add('a', 'b'), 'b')
        self.assertEqual(r.add('b', 'c'), 'a')
        self.assertEqual(r.add('c', 'a'), 'c')

    def test_custom_multiplication(self):
        elements = ['a', 'b', 'c']
        add_table = [
            ['a', 'b', 'c'],
            ['b', 'c', 'a'],
            ['c', 'a', 'b']
        ]
        mul_table = [
            ['a', 'a', 'a'],
            ['a', 'b', 'c'],
            ['a', 'c', 'b']
        ]
        r = Ring(elements=elements, add_table=add_table, mul_table=mul_table)
        self.assertEqual(r.mul('a', 'b'), 'a')
        self.assertEqual(r.mul('b', 'b'), 'b')
        self.assertEqual(r.mul('b', 'c'), 'c')
        self.assertEqual(r.mul('c', 'c'), 'b')


    # Assert test that module Ring should arise exceptionn if modulo is not a natural number
    def test_n_is_not_natural(self):
        self.assertRaises(ValidationException, Ring, modulo = 0)

    # Assert test for table that are not N x N for N is the number of elements in set
    def test_different_matrix_size(self):
        elements = ['0', '1']
        addition = [
            ['0', '1']
        ]
        multiplication = [
            ['1', '1'], ['1', '0']
        ]
        self.assertRaises(ValidationException, Ring, elements = elements, add_table = addition, mul_table = multiplication)

if __name__ == '__main__':
    unittest.main()

