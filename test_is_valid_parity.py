from unittest import main
from unittest import TestCase
from hard import is_valid_parity
"""
    is_valid_parity("1111111111000011111000001010110101", "ODD") returns True
    is_valid_parity("111", "EVEN") returns False
    is_valid_parity("11111111100000000001010110101", "EVEN") returns False
    is_valid_parity("11", "ODD") returns False
    is_valid_parity("101", "ODD") returns False
    is_valid_parity("11111111111000011111000001010110101", "ODD") returns False
"""


class Test(TestCase):
    def test_101_EVEN(self):
        self.assertEqual(True, is_valid_parity("101", "EVEN"))

    def test_11_EVEN_(self):
        self.assertEqual(True, is_valid_parity("11", "EVEN"))

    def test_101_EVEN(self):
        self.assertEqual(True, is_valid_parity("101", "EVEN"))

    def test_long_EVEN(self):
        self.assertEqual(True, is_valid_parity(
            "111111111100000000001010110101", "EVEN"))

    def test_10_ODD(self):
        self.assertEqual(True, is_valid_parity("10", "ODD"))

    def test_111_ODD(self):
        self.assertEqual(True, is_valid_parity("111", "ODD"))


if __name__ == "__main__":
    main()
