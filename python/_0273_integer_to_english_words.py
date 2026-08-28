# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# Hard

class Solution:
    def numberToWords(self, num: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(self.sol.numberToWords(0), "Zero")

    def test_single_digits(self):
        self.assertEqual(self.sol.numberToWords(1), "One")
        self.assertEqual(self.sol.numberToWords(5), "Five")
        self.assertEqual(self.sol.numberToWords(9), "Nine")

    def test_teen_numbers(self):
        self.assertEqual(self.sol.numberToWords(10), "Ten")
        self.assertEqual(self.sol.numberToWords(11), "Eleven")
        self.assertEqual(self.sol.numberToWords(13), "Thirteen")
        self.assertEqual(self.sol.numberToWords(14), "Fourteen")
        self.assertEqual(self.sol.numberToWords(19), "Nineteen")

    def test_tens(self):
        self.assertEqual(self.sol.numberToWords(20), "Twenty")
        self.assertEqual(self.sol.numberToWords(30), "Thirty")
        self.assertEqual(self.sol.numberToWords(40), "Forty")
        self.assertEqual(self.sol.numberToWords(90), "Ninety")

    def test_two_digits(self):
        self.assertEqual(self.sol.numberToWords(21), "Twenty One")
        self.assertEqual(self.sol.numberToWords(99), "Ninety Nine")

    def test_hundreds(self):
        self.assertEqual(self.sol.numberToWords(100), "One Hundred")
        self.assertEqual(self.sol.numberToWords(110), "One Hundred Ten")
        self.assertEqual(self.sol.numberToWords(116), "One Hundred Sixteen")
        self.assertEqual(self.sol.numberToWords(305), "Three Hundred Five")

    def test_hundreds_full(self):
        self.assertEqual(self.sol.numberToWords(123), "One Hundred Twenty Three")
        self.assertEqual(self.sol.numberToWords(999), "Nine Hundred Ninety Nine")

    def test_thousands(self):
        self.assertEqual(self.sol.numberToWords(1000), "One Thousand")
        self.assertEqual(self.sol.numberToWords(1001), "One Thousand One")
        self.assertEqual(self.sol.numberToWords(1010), "One Thousand Ten")

    def test_example_two(self):
        self.assertEqual(
            self.sol.numberToWords(12345), "Twelve Thousand Three Hundred Forty Five"
        )

    def test_thousands_corner(self):
        self.assertEqual(self.sol.numberToWords(1000010), "One Million Ten")
        self.assertEqual(
            self.sol.numberToWords(999999),
            "Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine",
        )

    def test_millions(self):
        self.assertEqual(self.sol.numberToWords(1000000), "One Million")
        self.assertEqual(self.sol.numberToWords(1000100), "One Million One Hundred")

    def test_example_three(self):
        self.assertEqual(
            self.sol.numberToWords(1234567),
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        )

    def test_billions(self):
        self.assertEqual(self.sol.numberToWords(1000000000), "One Billion")

    def test_max_value(self):
        self.assertEqual(
            self.sol.numberToWords(2**31 - 1),
            "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven",
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Recursion
