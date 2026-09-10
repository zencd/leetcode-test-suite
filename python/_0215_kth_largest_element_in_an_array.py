# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Medium

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_example2(self):
        self.assertEqual(self.solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_single_element(self):
        self.assertEqual(self.solution.findKthLargest([7], 1), 7)

    def test_k_equals_one_returns_max(self):
        self.assertEqual(self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 1), 6)

    def test_k_equals_n_returns_min(self):
        self.assertEqual(self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 6), 1)

    def test_all_elements_equal(self):
        self.assertEqual(self.solution.findKthLargest([4, 4, 4, 4, 4], 3), 4)

    def test_all_elements_equal_k_boundary(self):
        self.assertEqual(self.solution.findKthLargest([9, 9, 9], 1), 9)
        self.assertEqual(self.solution.findKthLargest([9, 9, 9], 3), 9)

    def test_duplicates_with_kth_not_distinct(self):
        self.assertEqual(self.solution.findKthLargest([2, 2, 2, 2, 2], 2), 2)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.findKthLargest([-3, -1, -2, -4, -5], 3), -3)

    def test_mixed_negative_and_positive(self):
        self.assertEqual(self.solution.findKthLargest([-5, 3, 0, -2, 7], 2), 3)

    def test_sorted_ascending(self):
        self.assertEqual(self.solution.findKthLargest([1, 2, 3, 4, 5], 3), 3)

    def test_sorted_descending(self):
        self.assertEqual(self.solution.findKthLargest([5, 4, 3, 2, 1], 3), 3)

    def test_two_elements_k1(self):
        self.assertEqual(self.solution.findKthLargest([1, 2], 1), 2)

    def test_two_elements_k2(self):
        self.assertEqual(self.solution.findKthLargest([2, 1], 2), 1)

    def test_two_elements_equal(self):
        self.assertEqual(self.solution.findKthLargest([5, 5], 2), 5)

    def test_extreme_values(self):
        nums = [-10000, 10000, -10000, 10000]
        self.assertEqual(self.solution.findKthLargest(nums, 1), 10000)
        self.assertEqual(self.solution.findKthLargest(nums, 2), 10000)
        self.assertEqual(self.solution.findKthLargest(nums, 3), -10000)
        self.assertEqual(self.solution.findKthLargest(nums, 4), -10000)

    def test_larger_array_known_order_statistics(self):
        nums = list(range(20)) + [100, -50]
        self.assertEqual(self.solution.findKthLargest(nums, 1), 100)
        self.assertEqual(self.solution.findKthLargest(nums, 2), 19)
        self.assertEqual(self.solution.findKthLargest(nums, 21), 0)
        self.assertEqual(self.solution.findKthLargest(nums, 22), -50)
        self.assertEqual(self.solution.findKthLargest(nums, 11), 10)

    def test_duplicate_heavy_array(self):
        nums = [1, 1, 2, 2, 2, 3, 3, 3, 3]
        self.assertEqual(self.solution.findKthLargest(nums, 1), 3)
        self.assertEqual(self.solution.findKthLargest(nums, 5), 2)
        self.assertEqual(self.solution.findKthLargest(nums, 9), 1)

    def test_original_list_not_required_ordered(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = self.solution.findKthLargest(nums, 4)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
