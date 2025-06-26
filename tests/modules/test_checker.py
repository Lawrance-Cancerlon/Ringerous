import unittest
from shared.models.Ring import Ring
from modules.checker import check_all_properties

class TestRingProperties(unittest.TestCase):

    # Assert testing for set Z_n where 1 <= n <= 99
    def test_modulo_ring_properties(self):

        for n in range(1, 100):
            r = Ring(modulo = n)
            results = check_all_properties(r)

            self.assertTrue(results['Additive Associativity']['result'])
            self.assertTrue(results['Multiplicative Associativity']['result'])
            self.assertTrue(results['Additive Identity']['result'])
            self.assertTrue(results['Additive Inverse']['result'])
            self.assertTrue(results['Distributivity']['result'])
            self.assertEqual(results['Multiplicative Identity']['result'], True)

    # Assert testing for custom ring, given multiplication table and addition table
    def test_custom_ring_properties(self):
        elements = ['0', '1', '2']
        add_table = [
            ['0', '1', '2'],
            ['1', '2', '0'],
            ['2', '0', '1']
        ]
        mul_table = [
            ['0', '0', '0'],
            ['0', '1', '2'],
            ['0', '2', '1']
        ]
        r = Ring(elements=elements, add_table=add_table, mul_table=mul_table)
        results = check_all_properties(r)

        self.assertTrue(results['Additive Associativity']['result'])
        self.assertTrue(results['Multiplicative Associativity']['result'])
        self.assertTrue(results['Additive Identity']['result'])
        self.assertTrue(results['Additive Inverse']['result'])
        self.assertTrue(results['Distributivity']['result'])

        # This custom ring has '1' as multiplicative identity
        self.assertTrue(results['Multiplicative Identity']['result'])

if __name__ == '__main__':
    unittest.main()

