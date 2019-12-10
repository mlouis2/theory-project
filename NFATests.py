import NFAInterface
import unittest
import sys

class TestNFA(unittest.TestCase):

    def test_odd_zeroes(self):
        with open('./test_cases/OddZeroes.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', '0']
            result = NFAInterface.main()
            self.assertTrue(result)

    def test_even_zeroes(self):
        with open('./test_cases/OddZeroes.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', '00']
            result = NFAInterface.main()
            self.assertFalse(result)

    def test_empty_string_not_accepted(self):
        with open('./test_cases/OddZeroes.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', '']
            result = NFAInterface.main()
            self.assertFalse(result)

    def test_empty_string_accepted(self):
        with open('./test_cases/NFAExample.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', '']
            result = NFAInterface.main()
            self.assertTrue(result)

    def test_a_accepted(self):
        with open('./test_cases/NFAExample.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', 'aaaa']
            result = NFAInterface.main()
            self.assertTrue(result)

    def test_b_not_accepted(self):
        with open('./test_cases/NFAExample.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', 'b']
            result = NFAInterface.main()
            self.assertFalse(result)

    def test_lambda(self):
        with open('./test_cases/NFAExample.txt','r') as f:
            sys.stdin = f
            sys.argv = ['', 'a']
            result = NFAInterface.main()
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
