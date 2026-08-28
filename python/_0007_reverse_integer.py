# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Medium

class Solution:
    def reverse(self, x: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_positive(self):
        self.assertEqual(self.sol.reverse(123), 321)

    def test_basic_negative(self):
        self.assertEqual(self.sol.reverse(-123), -321)

    def test_trailing_zeroes(self):
        self.assertEqual(self.sol.reverse(120), 21)

    def test_negative_trailing_zeroes(self):
        self.assertEqual(self.sol.reverse(-120), -21)

    def test_zero(self):
        self.assertEqual(self.sol.reverse(0), 0)

    def test_single_digit(self):
        self.assertEqual(self.sol.reverse(7), 7)

    def test_negative_single_digit(self):
        self.assertEqual(self.sol.reverse(-7), -7)

    def test_powers_of_ten(self):
        self.assertEqual(self.sol.reverse(10), 1)
        self.assertEqual(self.sol.reverse(100), 1)
        self.assertEqual(self.sol.reverse(1000000), 1)
        self.assertEqual(self.sol.reverse(-1000), -1)

    def test_palindrome(self):
        self.assertEqual(self.sol.reverse(1221), 1221)
        self.assertEqual(self.sol.reverse(-1221), -1221)

    def test_all_nines(self):
        self.assertEqual(self.sol.reverse(999), 999)
        self.assertEqual(self.sol.reverse(-999), -999)

    def test_overflow_large(self):
        self.assertEqual(self.sol.reverse(1534236469), 0)

    def test_overflow_large_negative(self):
        self.assertEqual(self.sol.reverse(-1534236469), 0)

    def test_overflow_2147483647(self):
        self.assertEqual(self.sol.reverse(2147483647), 0)

    def test_overflow_negative_2147483648(self):
        self.assertEqual(self.sol.reverse(-2147483648), 0)

    def test_max_safe_positive(self):
        self.assertEqual(self.sol.reverse(1463847412), 2147483641)

    def test_min_safe_negative_boundary(self):
        self.assertEqual(self.sol.reverse(-1463847412), -2147483641)

    def test_overflow_8_digit_eight(self):
        self.assertEqual(self.sol.reverse(2147483648), 0)

    def test_max_input(self):
        self.assertEqual(self.sol.reverse(2147483647), 0)

    def test_min_input(self):
        self.assertEqual(self.sol.reverse(-2147483648), 0)

    def test_two_digits(self):
        self.assertEqual(self.sol.reverse(12), 21)
        self.assertEqual(self.sol.reverse(99), 99)
        self.assertEqual(self.sol.reverse(-99), -99)

    def test_mixed_digits(self):
        self.assertEqual(self.sol.reverse(1002), 2001)
        self.assertEqual(self.sol.reverse(-1002), -2001)

    def test_round_trip(self):
        for v in [1, -1, 123, -123, 1234, -1234, 12345, -12345, 1201]:
            self.assertEqual(self.sol.reverse(self.sol.reverse(v)), v)


if __name__ == "__main__":
    unittest.main()

# Tags: Math
