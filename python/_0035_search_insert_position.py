# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Easy

import unittest
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        raise Exception("Not solved yet")


class TestSearchInsert(unittest.TestCase):
    def test_found_middle(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 5), 2)

    def test_found_first(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 1), 0)

    def test_found_last(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 6), 3)

    def test_insert_between(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 2), 1)

    def test_insert_before_first(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 0), 0)

    def test_insert_after_last(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 7), 4)

    def test_single_element_found(self):
        self.assertEqual(Solution().searchInsert([10], 10), 0)

    def test_single_element_insert_before(self):
        self.assertEqual(Solution().searchInsert([10], 5), 0)

    def test_single_element_insert_after(self):
        self.assertEqual(Solution().searchInsert([10], 15), 1)

    def test_two_elements(self):
        self.assertEqual(Solution().searchInsert([1, 2], 0), 0)
        self.assertEqual(Solution().searchInsert([1, 2], 1), 0)
        self.assertEqual(Solution().searchInsert([1, 2], 3), 2)

    def test_negative_values(self):
        self.assertEqual(Solution().searchInsert([-10, -5, 0, 5, 10], -5), 1)
        self.assertEqual(Solution().searchInsert([-10, -5, 0, 5, 10], -7), 1)
        self.assertEqual(Solution().searchInsert([-10, -5, 0, 5, 10], -20), 0)
        self.assertEqual(Solution().searchInsert([-10, -5, 0, 5, 10], 0), 2)
        self.assertEqual(Solution().searchInsert([-10, -5, 0, 5, 10], 15), 5)

    def test_consecutive_values(self):
        self.assertEqual(Solution().searchInsert([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(Solution().searchInsert([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(Solution().searchInsert([1, 2, 3, 4, 5], 6), 5)

    def test_large_array(self):
        nums = list(range(0, 20000, 2))
        self.assertEqual(Solution().searchInsert(nums, 200), 100)
        self.assertEqual(Solution().searchInsert(nums, 1), 1)
        self.assertEqual(Solution().searchInsert(nums, 19999), 10000)

    def test_alternation_found_and_missing(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(Solution().searchInsert(nums, 1), 0)
        self.assertEqual(Solution().searchInsert(nums, 2), 1)
        self.assertEqual(Solution().searchInsert(nums, 3), 1)
        self.assertEqual(Solution().searchInsert(nums, 4), 2)
        self.assertEqual(Solution().searchInsert(nums, 5), 2)
        self.assertEqual(Solution().searchInsert(nums, 6), 3)
        self.assertEqual(Solution().searchInsert(nums, 7), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
