# 327. Count of Range Sum
# https://leetcode.com/problems/count-of-range-sum/
# Hard

from typing import List
from bisect import bisect_left, bisect_right
import unittest


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.countRangeSum([-2, 5, -1], -2, 2), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.countRangeSum([0], 0, 0), 1)

    def test_single_positive(self):
        self.assertEqual(self.sol.countRangeSum([1], 0, 2), 1)

    def test_single_negative(self):
        self.assertEqual(self.sol.countRangeSum([-1], -2, -1), 1)

    def test_single_below_range(self):
        self.assertEqual(self.sol.countRangeSum([5], 0, 2), 0)

    def test_single_above_range(self):
        self.assertEqual(self.sol.countRangeSum([-5], -2, 2), 0)

    def test_single_zero_outside_range(self):
        self.assertEqual(self.sol.countRangeSum([0], 1, 2), 0)

    def test_all_zeros(self):
        self.assertEqual(self.sol.countRangeSum([0, 0, 0], 0, 0), 6)

    def test_all_zeros_out_of_range(self):
        self.assertEqual(self.sol.countRangeSum([0, 0, 0], 1, 5), 0)

    def test_all_positives(self):
        self.assertEqual(self.sol.countRangeSum([1, 2, 3, 4], 3, 9), 7)

    def test_all_negatives(self):
        self.assertEqual(self.sol.countRangeSum([-1, -2, -3, -4], -9, -3), 7)

    def test_mixed_positive_negative(self):
        self.assertEqual(
            self.sol.countRangeSum([3, -4, 7, -2, -3, 1, -5, -2, -6, -7], -25, 2), 48
        )
        self.assertEqual(
            self.sol.countRangeSum([3, -4, 7, -2, -3, 1, -5, -2, -6, -7], -25, 20), 55
        )

    def test_empty_range_bounds(self):
        self.assertEqual(self.sol.countRangeSum([1], 2, 5), 0)

    def test_lower_upper_equal_single_value(self):
        self.assertEqual(self.sol.countRangeSum([1, -1, 1, -1], 0, 0), 4)

    def test_large_numbers(self):
        nums = [2**30, -(2**30), 2**30]
        self.assertEqual(self.sol.countRangeSum(nums, 2**30 - 1, 2**30 + 1), 3)

    def test_negative_lower_negative_upper(self):
        self.assertEqual(self.sol.countRangeSum([-1, -2, -3], -6, -3), 4)

    def test_boundary_exclusive_below(self):
        self.assertEqual(self.sol.countRangeSum([1, 2], 4, 5), 0)

    def test_boundary_inclusive_both_ends(self):
        self.assertEqual(self.sol.countRangeSum([1, 2, 3, 5], 1, 11), 10)
        self.assertEqual(self.sol.countRangeSum([1, 2, 3, 5], 2, 10), 8)
        self.assertEqual(self.sol.countRangeSum([1, 2, 3, 5], 3, 9), 6)

    def test_all_elements_fit_lower_upper(self):
        self.assertEqual(self.sol.countRangeSum([2, 4, 6], 2, 12), 6)

    def test_none_fit(self):
        self.assertEqual(self.sol.countRangeSum([2, 4, 6], 0, 1), 0)

    def test_duplicates(self):
        self.assertEqual(self.sol.countRangeSum([1, 1, 1, 1], 2, 2), 3)

    def test_alternating(self):
        self.assertEqual(self.sol.countRangeSum([1, -1, 1, -1, 1, -1], 1, 1), 6)

    def test_repeated_values_positive_and_negative(self):
        self.assertEqual(
            self.sol.countRangeSum([1, -1, 1, -1, 1, -1, 1, -1], -1, 1), 36
        )

    def test_long_run_same_sign(self):
        nums = [5] * 10
        self.assertEqual(self.sol.countRangeSum(nums, 30, 50), 15)

    def test_known_bruno_case(self):
        self.assertEqual(self.sol.countRangeSum([-2, 5, -1], -3, 4), 5)

    def test_bruteforce_cross_check(self):
        import random

        random.seed(42)
        for _ in range(200):
            n = random.randint(1, 30)
            nums = [random.randint(-20, 20) for _ in range(n)]
            lower = random.randint(-50, 50)
            upper = random.randint(lower, 50)
            expected = sum(
                1
                for i in range(n)
                for j in range(i, n)
                if lower <= sum(nums[i : j + 1]) <= upper
            )
            self.assertEqual(self.sol.countRangeSum(nums, lower, upper), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
