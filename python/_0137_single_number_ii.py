# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/
# Medium

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.singleNumber([2, 2, 3, 2]), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)

    def test_single_element(self):
        self.assertEqual(self.sol.singleNumber([7]), 7)

    def test_zero_single(self):
        self.assertEqual(self.sol.singleNumber([1, 1, 1, 0]), 0)

    def test_negative_single(self):
        self.assertEqual(self.sol.singleNumber([-1, -1, -1, 4]), 4)

    def test_negative_triplets_and_single_negative(self):
        self.assertEqual(self.sol.singleNumber([5, 5, 5, -3]), -3)

    def test_mixed_negatives(self):
        self.assertEqual(self.sol.singleNumber([2, 2, 2, -1, -1, -1, -7]), -7)

    def test_zeros_and_zero_single(self):
        self.assertEqual(self.sol.singleNumber([5, 5, 5, 1, 1, 1, 0]), 0)

    def test_min_int32(self):
        self.assertEqual(self.sol.singleNumber([1, 1, 1, -2147483648]), -2147483648)

    def test_max_int32(self):
        self.assertEqual(self.sol.singleNumber([1, 1, 1, 2147483647]), 2147483647)

    def test_both_extremes(self):
        nums = [-2147483648, -2147483648, -2147483648, 1, 1, 1, 2147483647]
        self.assertEqual(self.sol.singleNumber(nums), 2147483647)

    def test_many_triplets(self):
        self.assertEqual(self.sol.singleNumber([4, 4, 4, 5, 5, 5, 6, 6, 6, -2]), -2)

    def test_single_zero_among_triplets(self):
        self.assertEqual(self.sol.singleNumber([9, 9, 9, 0]), 0)

    def test_large_values(self):
        nums = [1000000007] * 3 + [-5]
        self.assertEqual(self.sol.singleNumber(nums), -5)

    def test_repeated_zero(self):
        self.assertEqual(self.sol.singleNumber([0, 0, 0, 5, 5, 5, 2]), 2)

    def test_order_independence(self):
        self.assertEqual(self.sol.singleNumber([3, 2, 2, 2]), 3)
        self.assertEqual(self.sol.singleNumber([2, 3, 2, 2]), 3)
        self.assertEqual(self.sol.singleNumber([2, 2, 3, 2]), 3)

    def test_negative_extreme_with_negatives(self):
        nums = [-2147483648] * 3 + [-1, -1, -1] + [42]
        self.assertEqual(self.sol.singleNumber(nums), 42)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Bit Manipulation
