# 65. Valid Number
# https://leetcode.com/problems/valid-number/
# Hard

import unittest


class Solution:
    def isNumber(self, s: str) -> bool:
        raise Exception("Not solved yet")


class TestIsNumber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_valid_basic(self):
        self.assertTrue(self.sol.isNumber("0"))
        self.assertTrue(self.sol.isNumber("2"))
        self.assertTrue(self.sol.isNumber("0089"))
        self.assertTrue(self.sol.isNumber("-0.1"))
        self.assertTrue(self.sol.isNumber("+3.14"))
        self.assertTrue(self.sol.isNumber("4."))
        self.assertTrue(self.sol.isNumber("-.9"))
        self.assertTrue(self.sol.isNumber(".9"))
        self.assertTrue(self.sol.isNumber("9"))
        self.assertTrue(self.sol.isNumber("+9"))
        self.assertTrue(self.sol.isNumber("-9"))

    def test_valid_exponent(self):
        self.assertTrue(self.sol.isNumber("2e10"))
        self.assertTrue(self.sol.isNumber("-90E3"))
        self.assertTrue(self.sol.isNumber("3e+7"))
        self.assertTrue(self.sol.isNumber("+6e-1"))
        self.assertTrue(self.sol.isNumber("53.5e93"))
        self.assertTrue(self.sol.isNumber("-123.456e789"))
        self.assertTrue(self.sol.isNumber("1e1"))
        self.assertTrue(self.sol.isNumber("1E1"))
        self.assertTrue(self.sol.isNumber("0e0"))
        self.assertTrue(self.sol.isNumber(".1e1"))
        self.assertTrue(self.sol.isNumber("1.e1"))

    def test_invalid_examples(self):
        self.assertFalse(self.sol.isNumber("abc"))
        self.assertFalse(self.sol.isNumber("1a"))
        self.assertFalse(self.sol.isNumber("1e"))
        self.assertFalse(self.sol.isNumber("e3"))
        self.assertFalse(self.sol.isNumber("99e2.5"))
        self.assertFalse(self.sol.isNumber("--6"))
        self.assertFalse(self.sol.isNumber("-+3"))
        self.assertFalse(self.sol.isNumber("95a54e53"))

    def test_invalid_signs(self):
        self.assertFalse(self.sol.isNumber("+"))
        self.assertFalse(self.sol.isNumber("-"))
        self.assertFalse(self.sol.isNumber("+-1"))
        self.assertFalse(self.sol.isNumber("++1"))
        self.assertFalse(self.sol.isNumber("1+"))
        self.assertFalse(self.sol.isNumber("1-2"))
        self.assertFalse(self.sol.isNumber("1+2"))
        self.assertFalse(self.sol.isNumber("+-"))
        self.assertFalse(self.sol.isNumber("e+"))
        self.assertFalse(self.sol.isNumber("e-"))
        self.assertFalse(self.sol.isNumber("1e+e"))
        self.assertFalse(self.sol.isNumber("1e+-1"))

    def test_invalid_dot(self):
        self.assertFalse(self.sol.isNumber("."))
        self.assertFalse(self.sol.isNumber(".."))
        self.assertFalse(self.sol.isNumber("1.2.3"))
        self.assertFalse(self.sol.isNumber("46..34"))
        self.assertFalse(self.sol.isNumber(".e1"))
        self.assertFalse(self.sol.isNumber("1e6.77e"))
        self.assertFalse(self.sol.isNumber("1.2.3e4"))

    def test_invalid_e(self):
        self.assertFalse(self.sol.isNumber("e"))
        self.assertFalse(self.sol.isNumber("E"))
        self.assertFalse(self.sol.isNumber("e1"))
        self.assertFalse(self.sol.isNumber("E1"))
        self.assertFalse(self.sol.isNumber("ee1"))
        self.assertFalse(self.sol.isNumber("1ee1"))
        self.assertFalse(self.sol.isNumber("1e"))
        self.assertFalse(self.sol.isNumber("1e2e3"))
        self.assertFalse(self.sol.isNumber("e.1"))
        self.assertFalse(self.sol.isNumber("1e+"))
        self.assertFalse(self.sol.isNumber("1e-"))
        self.assertFalse(self.sol.isNumber("2e+2a"))
        self.assertFalse(self.sol.isNumber("2e2.2"))

    def test_invalid_letters(self):
        self.assertFalse(self.sol.isNumber("a"))
        self.assertFalse(self.sol.isNumber("helloworld"))
        self.assertFalse(self.sol.isNumber("2a"))
        self.assertFalse(self.sol.isNumber("a2"))
        self.assertFalse(self.sol.isNumber("2e2c"))
        self.assertFalse(self.sol.isNumber("c1"))

    def test_long(self):
        self.assertTrue(self.sol.isNumber("99999999999999999999"))
        self.assertTrue(self.sol.isNumber("999999999999999999999999"))
        self.assertFalse(self.sol.isNumber("1111111111111111111a"))

    def test_leet_examples(self):
        self.assertFalse(self.sol.isNumber("e"))
        self.assertFalse(self.sol.isNumber("."))
        self.assertTrue(self.sol.isNumber("0"))


if __name__ == "__main__":
    unittest.main()

# Tags: String
