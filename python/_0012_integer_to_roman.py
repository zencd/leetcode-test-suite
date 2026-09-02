# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
# Medium

class Solution:
    def intToRoman(self, num: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestIntToRoman(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_examples(self):
        self.assertEqual(self.sol.intToRoman(3749), "MMMDCCXLIX")
        self.assertEqual(self.sol.intToRoman(58), "LVIII")
        self.assertEqual(self.sol.intToRoman(1994), "MCMXCIV")

    def test_min_and_max(self):
        self.assertEqual(self.sol.intToRoman(1), "I")
        self.assertEqual(self.sol.intToRoman(3999), "MMMCMXCIX")

    def test_powers_of_ten(self):
        self.assertEqual(self.sol.intToRoman(10), "X")
        self.assertEqual(self.sol.intToRoman(100), "C")
        self.assertEqual(self.sol.intToRoman(1000), "M")

    def test_five_multiples(self):
        self.assertEqual(self.sol.intToRoman(5), "V")
        self.assertEqual(self.sol.intToRoman(50), "L")
        self.assertEqual(self.sol.intToRoman(500), "D")

    def test_subtractive_forms(self):
        self.assertEqual(self.sol.intToRoman(4), "IV")
        self.assertEqual(self.sol.intToRoman(9), "IX")
        self.assertEqual(self.sol.intToRoman(40), "XL")
        self.assertEqual(self.sol.intToRoman(90), "XC")
        self.assertEqual(self.sol.intToRoman(400), "CD")
        self.assertEqual(self.sol.intToRoman(900), "CM")

    def test_triples(self):
        self.assertEqual(self.sol.intToRoman(3), "III")
        self.assertEqual(self.sol.intToRoman(30), "XXX")
        self.assertEqual(self.sol.intToRoman(300), "CCC")
        self.assertEqual(self.sol.intToRoman(3000), "MMM")

    def test_mixed(self):
        self.assertEqual(self.sol.intToRoman(39), "XXXIX")
        self.assertEqual(self.sol.intToRoman(49), "XLIX")
        self.assertEqual(self.sol.intToRoman(44), "XLIV")
        self.assertEqual(self.sol.intToRoman(88), "LXXXVIII")
        self.assertEqual(self.sol.intToRoman(499), "CDXCIX")
        self.assertEqual(self.sol.intToRoman(949), "CMXLIX")
        self.assertEqual(self.sol.intToRoman(1234), "MCCXXXIV")
        self.assertEqual(self.sol.intToRoman(399), "CCCXCIX")
        self.assertEqual(self.sol.intToRoman(649), "DCXLIX")
        self.assertEqual(self.sol.intToRoman(1576), "MDLXXVI")

    def test_types_and_brands(self):
        self.assertIsInstance(self.sol.intToRoman(2026), str)

    def test_exhaustive_small_range_against_inverse(self):
        def romanToInt(s: str) -> int:
            table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
            total = 0
            prev = 0
            for ch in reversed(s):
                v = table[ch]
                if v < prev:
                    total -= v
                else:
                    total += v
                    prev = v
            return total

        for n in range(1, 2000):
            self.assertEqual(romanToInt(self.sol.intToRoman(n)), n, n)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)

# Tags: Hash Table, Math, String
