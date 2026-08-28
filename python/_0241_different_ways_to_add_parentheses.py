# 241. Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/
# Medium

from typing import List
import unittest


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(sorted(self.sol.diffWaysToCompute("2-1-1")), sorted([0, 2]))

    def test_example_2(self):
        self.assertEqual(
            sorted(self.sol.diffWaysToCompute("2*3-4*5")),
            sorted([-34, -14, -10, -10, 10]),
        )

    def test_single_digit(self):
        self.assertEqual(self.sol.diffWaysToCompute("7"), [7])

    def test_single_number_two_digits(self):
        self.assertEqual(self.sol.diffWaysToCompute("42"), [42])

    def test_plus_single(self):
        self.assertEqual(self.sol.diffWaysToCompute("1+2"), [3])

    def test_minus_single(self):
        self.assertEqual(self.sol.diffWaysToCompute("3-1"), [2])

    def test_mult_single(self):
        self.assertEqual(self.sol.diffWaysToCompute("2*3"), [6])

    def test_two_digit_multiplication(self):
        self.assertEqual(self.sol.diffWaysToCompute("12*3"), [36])

    def test_all_plus(self):
        self.assertEqual(self.sol.diffWaysToCompute("1+2+3"), [6, 6])

    def test_all_minus(self):
        self.assertEqual(sorted(self.sol.diffWaysToCompute("1-2-3")), [-4, 2])

    def test_all_mult(self):
        self.assertEqual(self.sol.diffWaysToCompute("2*3*4"), [24, 24])

    def test_mixed_operators(self):
        self.assertEqual(self.sol.diffWaysToCompute("1-2*3"), [-5, -3])

    def test_zero_value(self):
        self.assertEqual(self.sol.diffWaysToCompute("0*5"), [0])

    def test_zero_in_sum(self):
        self.assertEqual(self.sol.diffWaysToCompute("0+0"), [0])

    def test_max_digit(self):
        self.assertEqual(self.sol.diffWaysToCompute("99*99"), [9801])

    def test_negative_result(self):
        self.assertEqual(self.sol.diffWaysToCompute("0-98"), [-98])

    def test_multiple_results(self):
        self.assertEqual(
            sorted(self.sol.diffWaysToCompute("2+3*4-5")), sorted([-5, -1, 9, 9, 15])
        )

    def test_max_length_expression(self):
        expression = "1+2+3+4+5+6+7-8"
        self.assertGreaterEqual(len(expression), 1)
        self.assertLessEqual(len(expression), 20)
        results = self.sol.diffWaysToCompute(expression)
        self.assertLessEqual(len(results), 10**4)
        self.assertTrue(all(r == 20 for r in results))

    def test_duplicates_in_output(self):
        results = self.sol.diffWaysToCompute("2*3-4*5")
        self.assertIn(results.count(-10), [2])

    def test_result_range_32bit(self):
        results = self.sol.diffWaysToCompute("99+99-99")
        for r in results:
            self.assertGreaterEqual(r, -(2**31))
            self.assertLessEqual(r, 2**31 - 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Dynamic Programming, Recursion, Memoization, Bracket Sequences
