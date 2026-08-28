# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/
# Medium

import unittest

INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        raise Exception("Not solved yet")


class TestMyAtoi(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_numbers(self):
        self.assertEqual(self.sol.myAtoi("42"), 42)
        self.assertEqual(self.sol.myAtoi("00012"), 12)
        self.assertEqual(self.sol.myAtoi("0"), 0)
        self.assertEqual(self.sol.myAtoi("1"), 1)

    def test_signed_numbers(self):
        self.assertEqual(self.sol.myAtoi("+42"), 42)
        self.assertEqual(self.sol.myAtoi("-42"), -42)
        self.assertEqual(self.sol.myAtoi("-0"), 0)
        self.assertEqual(self.sol.myAtoi("+0"), 0)
        self.assertEqual(self.sol.myAtoi("-+1"), 0)
        self.assertEqual(self.sol.myAtoi("+-1"), 0)

    def test_leading_whitespace(self):
        self.assertEqual(self.sol.myAtoi("   42"), 42)
        self.assertEqual(self.sol.myAtoi(" -042"), -42)
        self.assertEqual(self.sol.myAtoi("      +123"), 123)
        self.assertEqual(self.sol.myAtoi("         7"), 7)

    def test_trailing_junk(self):
        self.assertEqual(self.sol.myAtoi("1337c0d3"), 1337)
        self.assertEqual(self.sol.myAtoi("4193 with words"), 4193)
        self.assertEqual(self.sol.myAtoi("2147483648000"), INT_MAX)
        self.assertEqual(self.sol.myAtoi("1 -1234"), 1)

    def test_no_digits(self):
        self.assertEqual(self.sol.myAtoi("words and 987"), 0)
        self.assertEqual(self.sol.myAtoi("  +"), 0)
        self.assertEqual(self.sol.myAtoi("  -"), 0)
        self.assertEqual(self.sol.myAtoi("+.878"), 0)
        self.assertEqual(self.sol.myAtoi("    ... 987"), 0)
        self.assertEqual(self.sol.myAtoi("abc"), 0)

    def test_empty_and_whitespace_only(self):
        self.assertEqual(self.sol.myAtoi(""), 0)
        self.assertEqual(self.sol.myAtoi("   "), 0)
        self.assertEqual(self.sol.myAtoi("    "), 0)

    def test_clamping(self):
        self.assertEqual(self.sol.myAtoi("2147483647"), INT_MAX)
        self.assertEqual(self.sol.myAtoi("-2147483648"), INT_MIN)
        self.assertEqual(self.sol.myAtoi("2147483648"), INT_MAX)
        self.assertEqual(self.sol.myAtoi("-2147483649"), INT_MIN)
        self.assertEqual(self.sol.myAtoi("91283472332"), INT_MAX)
        self.assertEqual(self.sol.myAtoi("-91283472332"), INT_MIN)

    def test_zero_sign(self):
        self.assertEqual(self.sol.myAtoi("00000"), 0)
        self.assertEqual(self.sol.myAtoi("  + 00 00"), 0)
        self.assertEqual(self.sol.myAtoi(" - 00 00"), 0)

    def test_decimal_point(self):
        self.assertEqual(self.sol.myAtoi("."), 0)
        self.assertEqual(self.sol.myAtoi(".1"), 0)
        self.assertEqual(self.sol.myAtoi("1.2"), 1)

    def test_large_leading_zeros(self):
        self.assertEqual(self.sol.myAtoi("00000000000000000000000001"), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: String
