import unittest
import postfix


class Test_Postfix(unittest.TestCase):

    def setUp(self):
        self._postfix = postfix.Postfix()

    def test_in_2_post(self):
        self.assertEqual(''.join(self._postfix.in_2_post('a*b')), 'a*b#')
        self.assertEqual(''.join(self._postfix.in_2_post('ab*')), 'ab*#')
        self.assertEqual(''.join(self._postfix.in_2_post('(ab)*')), 'ab#*')
        self.assertEqual(''.join(self._postfix.in_2_post('(ab)*c')), 'ab#*c#')
        self.assertEqual(''.join(self._postfix.in_2_post('(ab)*(cd)*')), 'ab#*cd#*#')

if __name__ == "__main__":
    unittest.main()