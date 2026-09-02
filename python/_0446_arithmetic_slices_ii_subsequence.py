# 446. Arithmetic Slices II - Subsequence
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Hard

from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest
from itertools import combinations


def brute_force(nums):
    count = 0
    for k in range(3, len(nums) + 1):
        for idx in combinations(range(len(nums)), k):
            s = [nums[i] for i in idx]
            if all(s[j + 1] - s[j] == s[1] - s[0] for j in range(len(s) - 1)):
                count += 1
    return count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([2, 4, 6, 8, 10]), 7)

    def test_example2(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([7, 7, 7, 7, 7]), 16)

    def test_no_arithmetic_subsequence(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 1, 2, 5, 7]), 0)

    def test_length_1(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1]), 0)

    def test_length_2(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2]), 0)

    def test_length_3_constant(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([3, 3, 3]), 1)

    def test_length_3_arithmetic(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3]), 1)

    def test_length_3_not_arithmetic(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 5]), 0)

    def test_minimal_example(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 4]), 3)

    def test_negative_numbers(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([3, -1, -5, -9]), 3)

    def test_mixed_signs(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, -3, 1]), 0)

    def test_negative_difference_even(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([5, 3, 1]), 1)

    def test_duplicated_non_constant(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 1, 2]), 0)

    def test_all_six_sevens(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([7] * 6), 42)

    def test_larger_full_arithmetic(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]), 12)

    def test_out_of_order_elements(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 3, 2, 4, 5]), 2)

    def test_negative_even_sized(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([-1, 1, 3, 5, 7]), 7)

    def test_large_values(self):
        nums = [-(2**31), 0, 2**31 - 1]
        self.assertEqual(self.s.numberOfArithmeticSlices(nums), 0)

    def test_pairs_counting(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 5]), 2)

    def test_alternating_differences(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 3, 2, 4, 3]), 1)

    def test_cross_check_brute_force(self):
        cases = [
            [],
            [42],
            [1, 1],
            [1, 1, 1],
            [2, 2, 2, 2],
            [1, 1, 2, 2, 3, 3],
            [1, 3, 2, 4, 3, 1],
            [5, 3, 1, 3, 5],
            [-2, -1, 0, 1, 2, 3, 4],
            [1, 2, 3, 2, 4, 3],
            [7, 7, 7, 7, 7, 7, 7],
            [100, -100, 100, -100],
            [4, 4, 4, 5, 5, 5],
        ]
        for c in cases:
            with self.subTest(nums=c):
                self.assertEqual(self.s.numberOfArithmeticSlices(c), brute_force(c))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
