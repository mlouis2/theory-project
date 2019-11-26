import NFAInterface
import unittest
import sys

class TestNFA(unittest.TestCase):

    def test_odd_zeroes(self):
        sys.argv = ['', './test_cases/OddZeroes.txt', '0']
        result = NFAInterface.main()
        self.assertTrue(result)

    def test_even_zeroes(self):
        sys.argv = ['', './test_cases/OddZeroes.txt', '00']
        result = NFAInterface.main()
        self.assertFalse(result)

    def test_empty_string_not_accepted(self):
        sys.argv = ['', './test_cases/OddZeroes.txt', '']
        result = NFAInterface.main()
        self.assertFalse(result)

    def test_empty_string_accepted(self):
        sys.argv = ['', './test_cases/NFAExample.txt', '']
        result = NFAInterface.main()
        self.assertTrue(result)

    def test_a_accepted(self):
        sys.argv = ['', './test_cases/NFAExample.txt', 'aaaa']
        result = NFAInterface.main()
        self.assertTrue(result)

    def test_b_not_accepted(self):
        sys.argv = ['', './test_cases/NFAExample.txt', 'b']
        result = NFAInterface.main()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
