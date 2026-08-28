# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Medium

import unittest
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.searchRange([5, 7, 7, 8, 8, 10], 8),
            [3, 4],
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.searchRange([5, 7, 7, 8, 8, 10], 6),
            [-1, -1],
        )

    def test_example_3(self):
        self.assertEqual(self.solution.searchRange([], 0), [-1, -1])

    def test_single_element_present(self):
        self.assertEqual(self.solution.searchRange([1], 1), [0, 0])

    def test_single_element_absent(self):
        self.assertEqual(self.solution.searchRange([1], 2), [-1, -1])

    def test_all_same_present(self):
        self.assertEqual(self.solution.searchRange([7, 7, 7, 7], 7), [0, 3])

    def test_all_same_absent(self):
        self.assertEqual(self.solution.searchRange([7, 7, 7, 7], 5), [-1, -1])

    def test_target_first(self):
        self.assertEqual(self.solution.searchRange([1, 2, 3, 4], 1), [0, 0])

    def test_target_last(self):
        self.assertEqual(self.solution.searchRange([1, 2, 3, 4], 4), [3, 3])

    def test_target_in_middle(self):
        self.assertEqual(self.solution.searchRange([1, 2, 3, 4], 2), [1, 1])

    def test_target_consecutive_all(self):
        self.assertEqual(self.solution.searchRange([1, 2, 2, 2, 3], 2), [1, 3])

    def test_target_below_min(self):
        self.assertEqual(self.solution.searchRange([5, 7, 8, 10], 1), [-1, -1])

    def test_target_above_max(self):
        self.assertEqual(self.solution.searchRange([5, 7, 8, 10], 100), [-1, -1])

    def test_negative_numbers_present(self):
        self.assertEqual(
            self.solution.searchRange([-10, -5, -5, -5, 0, 3], -5),
            [1, 3],
        )

    def test_negative_numbers_absent(self):
        self.assertEqual(
            self.solution.searchRange([-10, -5, -3, 0, 3], -6),
            [-1, -1],
        )

    def test_two_elements_present(self):
        self.assertEqual(self.solution.searchRange([1, 2], 2), [1, 1])

    def test_two_elements_absent(self):
        self.assertEqual(self.solution.searchRange([1, 2], 3), [-1, -1])

    def test_two_elements_both_present(self):
        self.assertEqual(self.solution.searchRange([4, 4], 4), [0, 1])

    def test_large_values(self):
        nums = [-(10**9), -(10**9), 0, 10**9, 10**9]
        self.assertEqual(self.solution.searchRange(nums, 10**9), [3, 4])
        self.assertEqual(self.solution.searchRange(nums, -(10**9)), [0, 1])

    def test_large_array_present(self):
        nums = [1] * 50 + [2] * 50
        self.assertEqual(self.solution.searchRange(nums, 1), [0, 49])
        self.assertEqual(self.solution.searchRange(nums, 2), [50, 99])

    def test_large_array_absent(self):
        nums = list(range(100))
        self.assertEqual(self.solution.searchRange(nums, 50), [50, 50])
        self.assertEqual(self.solution.searchRange(nums, -1), [-1, -1])
        self.assertEqual(self.solution.searchRange(nums, 100), [-1, -1])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
