import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()

# Andrew Rehfeldt SDEV220 Mr. Hamby's Class
# To me, the test results show that Python accepts certain inputs but may not read others. It shows me that Python did not properly import sum
# from my_sum, as well as that there is a "discovery error. I think this means that python cannot discover the test that I, the user am calling. "