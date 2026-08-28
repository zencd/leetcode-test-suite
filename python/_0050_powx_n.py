# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Medium

import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.sol.myPow(2.0, 10), 1024.0)

    def test_example_2(self):
        self.assertAlmostEqual(self.sol.myPow(2.1, 3), 9.261)

    def test_example_3(self):
        self.assertAlmostEqual(self.sol.myPow(2.0, -2), 0.25)

    def test_zero_exponent(self):
        self.assertAlmostEqual(self.sol.myPow(3.5, 0), 1.0)

    def test_zero_exponent_negative_x(self):
        self.assertAlmostEqual(self.sol.myPow(-4.2, 0), 1.0)

    def test_exponent_one(self):
        self.assertAlmostEqual(self.sol.myPow(-5.7, 1), -5.7)

    def test_exponent_minus_one(self):
        self.assertAlmostEqual(self.sol.myPow(-5.7, -1), 1.0 / -5.7)

    def test_base_one(self):
        self.assertAlmostEqual(self.sol.myPow(1.0, 100), 1.0)
        self.assertAlmostEqual(self.sol.myPow(1.0, -100), 1.0)

    def test_base_minus_one_even(self):
        self.assertAlmostEqual(self.sol.myPow(-1.0, 8), 1.0)

    def test_base_minus_one_odd(self):
        self.assertAlmostEqual(self.sol.myPow(-1.0, 7), -1.0)

    def test_unit_base(self):
        self.assertAlmostEqual(self.sol.myPow(0.5, 4), 0.0625)

    def test_fractional_result_negative_exponent(self):
        self.assertAlmostEqual(self.sol.myPow(0.5, -3), 8.0)

    def test_large_negative_exponent(self):
        self.assertAlmostEqual(self.sol.myPow(2.0, -31), 1.0 / 2**31)

    def test_int_min_exponent(self):
        self.assertAlmostEqual(self.sol.myPow(2.0, -(2**31)), 0.0, places=30)

    def test_int_max_exponent_positive(self):
        value = self.sol.myPow(0.001, 2**31 - 1)
        self.assertAlmostEqual(value, 0.0, places=20)

    def test_positive_decimal_base(self):
        self.assertAlmostEqual(self.sol.myPow(1.234, 5), 1.234**5, places=9)

    def test_negative_base_negative_exponent(self):
        self.assertAlmostEqual(self.sol.myPow(-2.5, -3), 1.0 / (-(2.5**3)), places=9)

    def test_large_result(self):
        self.assertAlmostEqual(self.sol.myPow(99.0, 2), 9801.0)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Recursion
