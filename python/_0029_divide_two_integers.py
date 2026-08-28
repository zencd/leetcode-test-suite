# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# Medium

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_cases(self):
        self.assertEqual(self.solution.divide(10, 3), 3)
        self.assertEqual(self.solution.divide(7, -3), -2)
        self.assertEqual(self.solution.divide(1, 1), 1)
        self.assertEqual(self.solution.divide(-1, 1), -1)
        self.assertEqual(self.solution.divide(1, -1), -1)
        self.assertEqual(self.solution.divide(-1, -1), 1)

    def test_exact_division(self):
        self.assertEqual(self.solution.divide(12, 4), 3)
        self.assertEqual(self.solution.divide(-12, 4), -3)
        self.assertEqual(self.solution.divide(12, -4), -3)
        self.assertEqual(self.solution.divide(-12, -4), 3)

    def test_truncation_toward_zero(self):
        self.assertEqual(self.solution.divide(43, 10), 4)
        self.assertEqual(self.solution.divide(-43, 10), -4)
        self.assertEqual(self.solution.divide(43, -10), -4)
        self.assertEqual(self.solution.divide(-43, -10), 4)

    def test_small_dividend(self):
        self.assertEqual(self.solution.divide(1, 2), 0)
        self.assertEqual(self.solution.divide(-1, 2), 0)
        self.assertEqual(self.solution.divide(2, 3), 0)
        self.assertEqual(self.solution.divide(-2, 3), 0)
        self.assertEqual(self.solution.divide(3, 2), 1)
        self.assertEqual(self.solution.divide(-3, 2), -1)

    def test_large_numbers(self):
        self.assertEqual(self.solution.divide(10**9, 3), 10**9 // 3)
        self.assertEqual(self.solution.divide(2**30, 2**29), 2)
        self.assertEqual(self.solution.divide(2**30 - 1, 2**15), (2**30 - 1) // 2**15)

    def test_overflow_clamp(self):
        self.assertEqual(self.solution.divide(-(2**31), -1), 2**31 - 1)

    def test_overflow_large_quotient(self):
        self.assertEqual(self.solution.divide(2**31 - 1, 1), 2**31 - 1)

    def test_boundary_dividend(self):
        self.assertEqual(self.solution.divide(-(2**31), 1), -(2**31))
        self.assertEqual(self.solution.divide(-(2**31), 2), -(2**30))
        self.assertEqual(self.solution.divide(2**31 - 1, 2), (2**31 - 1) // 2)

    def test_divisor_one(self):
        self.assertEqual(self.solution.divide(123, 1), 123)
        self.assertEqual(self.solution.divide(-123, 1), -123)
        self.assertEqual(self.solution.divide(123, -1), -123)
        self.assertEqual(self.solution.divide(-123, -1), 123)

    def expected_quotient(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)
        value = abs(dividend) // abs(divisor)
        if negative:
            value = -value
        if value > 2**31 - 1:
            return 2**31 - 1
        if value < -(2**31):
            return -(2**31)
        return value

    def test_randomized_against_reference(self):
        values = [
            (0, 7),
            (7, 5),
            (-2147483648, 2147483647),
            (2147483647, -2147483648),
            (2147483647, 2147483647),
            (-2147483648, -2147483648),
            (1000000007, 13),
            (-1000000007, 13),
            (123456789, 987654321),
            (-123456789, -987654321),
            (987654321, -123456789),
            (5, 5),
            (-5, 5),
            (5, -5),
            (2147483647, 3),
            (-2147483648, 3),
        ]
        for dividend, divisor in values:
            self.assertEqual(
                self.solution.divide(dividend, divisor),
                self.expected_quotient(dividend, divisor),
                f"dividend={dividend}, divisor={divisor}",
            )


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Bit Manipulation
