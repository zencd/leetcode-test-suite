# 415. Add Strings
# https://leetcode.com/problems/add-strings/
# Easy

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.addStrings("11", "123"), "134")

    def test_example_2(self):
        self.assertEqual(self.sol.addStrings("456", "77"), "533")

    def test_example_3(self):
        self.assertEqual(self.sol.addStrings("0", "0"), "0")

    def test_zeros_with_digit(self):
        self.assertEqual(self.sol.addStrings("0", "5"), "5")
        self.assertEqual(self.sol.addStrings("5", "0"), "5")

    def test_single_digits(self):
        self.assertEqual(self.sol.addStrings("1", "2"), "3")
        self.assertEqual(self.sol.addStrings("9", "1"), "10")
        self.assertEqual(self.sol.addStrings("5", "5"), "10")
        self.assertEqual(self.sol.addStrings("9", "9"), "18")

    def test_carry_propagation(self):
        self.assertEqual(self.sol.addStrings("999", "1"), "1000")
        self.assertEqual(self.sol.addStrings("5", "999"), "1004")
        self.assertEqual(self.sol.addStrings("99999", "1"), "100000")

    def test_different_lengths(self):
        self.assertEqual(self.sol.addStrings("1", "99"), "100")
        self.assertEqual(self.sol.addStrings("12345", "67"), "12412")
        self.assertEqual(self.sol.addStrings("12", "987654"), "987666")

    def test_large_numbers(self):
        num1 = "9" * 10000
        num2 = "1"
        self.assertEqual(self.sol.addStrings(num1, num2), "1" + "0" * 10000)

    def test_large_numbers_both(self):
        num1 = "99999999999999999999"
        num2 = "99999999999999999999"
        self.assertEqual(
            self.sol.addStrings(num1, num2),
            "199999999999999999998",
        )

    def test_no_carry(self):
        self.assertEqual(self.sol.addStrings("123", "456"), "579")

    def test_equal_length(self):
        self.assertEqual(self.sol.addStrings("78", "99"), "177")

    def test_mixed_carry(self):
        self.assertEqual(self.sol.addStrings("4999", "1"), "5000")
        self.assertEqual(self.sol.addStrings("909", "101"), "1010")


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Simulation
