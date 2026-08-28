# 372. Super Pow
# https://leetcode.com/problems/super-pow/
# Medium

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.superPow(2, [3]), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.superPow(2, [1, 0]), 1024)

    def test_example_3(self):
        self.assertEqual(self.solution.superPow(1, [4, 3, 3, 8, 5, 2]), 1)

    def test_a_is_one(self):
        self.assertEqual(self.solution.superPow(1, [9, 9, 9]), 1)

    def test_single_digit_exponents(self):
        for digit in range(10):
            self.assertEqual(self.solution.superPow(2, [digit]), pow(2, digit, 1337))

    def test_exponent_ten(self):
        self.assertEqual(self.solution.superPow(2, [1, 0]), 1024)

    def test_exponent_one_hundred(self):
        self.assertEqual(self.solution.superPow(2, [1, 0, 0]), pow(2, 100, 1337))

    def test_large_a(self):
        a = 2**31 - 1
        self.assertEqual(self.solution.superPow(a, [1]), a % 1337)

    def test_large_a_and_b(self):
        a = 2**31 - 1
        expected = pow(a, 123456, 1337)
        self.assertEqual(self.solution.superPow(a, [1, 2, 3, 4, 5, 6]), expected)

    def test_a_multiple_of_mod(self):
        self.assertEqual(self.solution.superPow(1337, [5]), 0)

    def test_a_multiple_of_seven(self):
        expected = pow(7, 49, 1337)
        self.assertEqual(self.solution.superPow(7, [4, 9]), expected)

    def test_two_digit_digits(self):
        expected = pow(3, 99, 1337)
        self.assertEqual(self.solution.superPow(3, [9, 9]), expected)

    def test_long_exponent_of_ones(self):
        b = [1] * 2000
        expected = pow(2, int("1" * 2000), 1337)
        self.assertEqual(self.solution.superPow(2, b), expected)

    def test_zeros_in_middle(self):
        expected = pow(5, 505, 1337)
        self.assertEqual(self.solution.superPow(5, [5, 0, 5]), expected)

    def test_exponent_81129(self):
        self.assertEqual(
            self.solution.superPow(4, [8, 1, 1, 2, 9]), pow(4, 81129, 1337)
        )

    def test_result_is_non_negative(self):
        self.assertGreaterEqual(self.solution.superPow(2, [9, 9, 9, 9]), 0)
        self.assertLess(self.solution.superPow(2, [9, 9, 9, 9]), 1337)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Divide and Conquer, Euler's Totient Function, Euler's Theorem
