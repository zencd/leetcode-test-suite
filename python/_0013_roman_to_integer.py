# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Easy

class Solution:
    def romanToInt(self, s: str) -> int:
        raise Exception("Not solved yet")


import unittest


class TestRomanToInteger(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_additive(self):
        self.assertEqual(self.sol.romanToInt("III"), 3)
        self.assertEqual(self.sol.romanToInt("II"), 2)
        self.assertEqual(self.sol.romanToInt("I"), 1)
        self.assertEqual(self.sol.romanToInt("VII"), 7)
        self.assertEqual(self.sol.romanToInt("XII"), 12)
        self.assertEqual(self.sol.romanToInt("XXVII"), 27)

    def test_subtractive_pairs(self):
        self.assertEqual(self.sol.romanToInt("IV"), 4)
        self.assertEqual(self.sol.romanToInt("IX"), 9)
        self.assertEqual(self.sol.romanToInt("XL"), 40)
        self.assertEqual(self.sol.romanToInt("XC"), 90)
        self.assertEqual(self.sol.romanToInt("CD"), 400)
        self.assertEqual(self.sol.romanToInt("CM"), 900)

    def test_mixed(self):
        self.assertEqual(self.sol.romanToInt("LVIII"), 58)
        self.assertEqual(self.sol.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.sol.romanToInt("XXXVIII"), 38)
        self.assertEqual(self.sol.romanToInt("LXXXVIII"), 88)
        self.assertEqual(self.sol.romanToInt("CCCLXXXVIII"), 388)
        self.assertEqual(self.sol.romanToInt("CXLIV"), 144)

    def test_boundary_values(self):
        self.assertEqual(self.sol.romanToInt("M"), 1000)
        self.assertEqual(self.sol.romanToInt("MMM"), 3000)
        self.assertEqual(self.sol.romanToInt("MMMCMXCIX"), 3999)
        self.assertEqual(self.sol.romanToInt("MMMCMXCIV"), 3994)

    def test_single_symbols(self):
        self.assertEqual(self.sol.romanToInt("V"), 5)
        self.assertEqual(self.sol.romanToInt("X"), 10)
        self.assertEqual(self.sol.romanToInt("L"), 50)
        self.assertEqual(self.sol.romanToInt("C"), 100)
        self.assertEqual(self.sol.romanToInt("D"), 500)

    def test_repeat_symbols(self):
        self.assertEqual(self.sol.romanToInt("XXX"), 30)
        self.assertEqual(self.sol.romanToInt("LI"), 51)
        self.assertEqual(self.sol.romanToInt("CCCLXXX"), 380)
        self.assertEqual(self.sol.romanToInt("MMMDCCCLXXXVIII"), 3888)

    def test_subtraction_in_the_middle(self):
        self.assertEqual(self.sol.romanToInt("MMDXLIV"), 2544)
        self.assertEqual(self.sol.romanToInt("DCCLXXXIX"), 789)
        self.assertEqual(self.sol.romanToInt("CMXCIX"), 999)
        self.assertEqual(self.sol.romanToInt("MMXLIV"), 2044)


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Math, String
