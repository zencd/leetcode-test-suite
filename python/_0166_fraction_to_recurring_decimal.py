# 166. Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/
# Medium

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_fractions(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 2), "0.5")
        self.assertEqual(self.sol.fractionToDecimal(1, 4), "0.25")
        self.assertEqual(self.sol.fractionToDecimal(1, 8), "0.125")
        self.assertEqual(self.sol.fractionToDecimal(1, 5), "0.2")
        self.assertEqual(self.sol.fractionToDecimal(2, 4), "0.5")
        self.assertEqual(self.sol.fractionToDecimal(4, 2), "2")

    def test_whole_numbers(self):
        self.assertEqual(self.sol.fractionToDecimal(2, 1), "2")
        self.assertEqual(self.sol.fractionToDecimal(10, 1), "10")
        self.assertEqual(self.sol.fractionToDecimal(7, 7), "1")
        self.assertEqual(self.sol.fractionToDecimal(-1, 1), "-1")
        self.assertEqual(self.sol.fractionToDecimal(-7, 7), "-1")
        self.assertEqual(self.sol.fractionToDecimal(1, -1), "-1")
        self.assertEqual(self.sol.fractionToDecimal(-5, -2), "2.5")

    def test_repeating(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 3), "0.(3)")
        self.assertEqual(self.sol.fractionToDecimal(2, 3), "0.(6)")
        self.assertEqual(self.sol.fractionToDecimal(1, 6), "0.1(6)")
        self.assertEqual(self.sol.fractionToDecimal(4, 333), "0.(012)")
        self.assertEqual(self.sol.fractionToDecimal(28, 13), "2.(153846)")
        self.assertEqual(self.sol.fractionToDecimal(1, 9), "0.(1)")
        self.assertEqual(self.sol.fractionToDecimal(2, 9), "0.(2)")
        self.assertEqual(self.sol.fractionToDecimal(1, 7), "0.(142857)")
        self.assertEqual(self.sol.fractionToDecimal(3, 11), "0.(27)")
        self.assertEqual(self.sol.fractionToDecimal(1, 90), "0.0(1)")
        self.assertEqual(self.sol.fractionToDecimal(3, 14), "0.2(142857)")
        self.assertEqual(self.sol.fractionToDecimal(30, 90), "0.(3)")

    def test_negative(self):
        self.assertEqual(self.sol.fractionToDecimal(-1, 2), "-0.5")
        self.assertEqual(self.sol.fractionToDecimal(-1, 3), "-0.(3)")
        self.assertEqual(self.sol.fractionToDecimal(1, -3), "-0.(3)")
        self.assertEqual(self.sol.fractionToDecimal(-1, -3), "0.(3)")
        self.assertEqual(self.sol.fractionToDecimal(-50, 8), "-6.25")
        self.assertEqual(self.sol.fractionToDecimal(-2, 3), "-0.(6)")
        self.assertEqual(self.sol.fractionToDecimal(-2147483648, 1), "-2147483648")

    def test_zero_numerator(self):
        self.assertEqual(self.sol.fractionToDecimal(0, 1), "0")
        self.assertEqual(self.sol.fractionToDecimal(0, 123), "0")
        self.assertEqual(self.sol.fractionToDecimal(0, -7), "0")

    def test_large_values(self):
        self.assertEqual(self.sol.fractionToDecimal(2147483647, 1), "2147483647")
        self.assertEqual(self.sol.fractionToDecimal(2147483647, 2), "1073741823.5")
        self.assertEqual(self.sol.fractionToDecimal(2147483648, 3), "715827882.(6)")

    def test_mixed_finite_and_repeating(self):
        self.assertEqual(self.sol.fractionToDecimal(11, 2), "5.5")
        self.assertEqual(self.sol.fractionToDecimal(31, 2), "15.5")
        self.assertEqual(self.sol.fractionToDecimal(5, 6), "0.8(3)")
        self.assertEqual(self.sol.fractionToDecimal(1, 12), "0.08(3)")
        self.assertEqual(self.sol.fractionToDecimal(1, 40), "0.025")

    def test_single_digit_repeating_start(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 10), "0.1")
        self.assertEqual(self.sol.fractionToDecimal(1, 100), "0.01")


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Math, String
