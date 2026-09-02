# 410. Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/
# Hard

from typing import List
import unittest


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.splitArray([7, 2, 5, 10, 8], 2), 18)

    def test_example2(self):
        self.assertEqual(self.sol.splitArray([1, 2, 3, 4, 5], 2), 9)

    def test_single_element(self):
        self.assertEqual(self.sol.splitArray([5], 1), 5)

    def test_k_equals_n(self):
        self.assertEqual(self.sol.splitArray([3, 1, 4, 1, 5], 5), 5)

    def test_k_equals_1(self):
        self.assertEqual(self.sol.splitArray([3, 1, 4, 1, 5], 1), 14)

    def test_all_ones(self):
        self.assertEqual(self.sol.splitArray([1, 1, 1, 1, 1], 2), 3)

    def test_all_zeros(self):
        self.assertEqual(self.sol.splitArray([0, 0, 0, 0], 2), 0)

    def test_zero_and_one_elements(self):
        self.assertEqual(self.sol.splitArray([0, 0, 1, 0], 2), 1)

    def test_single_largest_element(self):
        self.assertEqual(self.sol.splitArray([10, 1, 1, 1, 1], 3), 10)

    def test_two_elements(self):
        self.assertEqual(self.sol.splitArray([1, 1], 2), 1)
        self.assertEqual(self.sol.splitArray([5, 2], 1), 7)

    def test_descending(self):
        self.assertEqual(self.sol.splitArray([5, 4, 3, 2, 1], 2), 9)

    def test_uniform_small(self):
        self.assertEqual(self.sol.splitArray([2, 2, 2, 2], 2), 4)

    def test_large_values(self):
        nums = [10**6] * 10
        self.assertEqual(self.sol.splitArray(nums, 3), 4 * 10**6)

    def test_long_array_k_50(self):
        nums = [1] * 1000
        self.assertEqual(self.sol.splitArray(nums, 50), 20)

    def test_known_value_from_split_points(self):
        self.assertEqual(self.sol.splitArray([1, 1, 1], 3), 1)
        self.assertEqual(self.sol.splitArray([1, 1, 1], 1), 3)
        self.assertEqual(self.sol.splitArray([8, 8, 8], 2), 16)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum
