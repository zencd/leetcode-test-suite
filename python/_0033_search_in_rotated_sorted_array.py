# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Medium

from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise Exception("Not solved yet")


class TestSearch(unittest.TestCase):
    def _check(self, nums, target, expected):
        self.assertEqual(Solution().search(nums, target), expected)

    def test_example1_target_zero(self):
        self._check([4, 5, 6, 7, 0, 1, 2], 0, 4)

    def test_example1_target_found_left(self):
        self._check([4, 5, 6, 7, 0, 1, 2], 4, 0)

    def test_example1_target_found_right(self):
        self._check([4, 5, 6, 7, 0, 1, 2], 2, 6)

    def test_example1_target_found_mid(self):
        self._check([4, 5, 6, 7, 0, 1, 2], 7, 3)

    def test_example2_target_missing(self):
        self._check([4, 5, 6, 7, 0, 1, 2], 3, -1)

    def test_example3_single_element_missing(self):
        self._check([1], 0, -1)

    def test_single_element_found(self):
        self._check([5], 5, 0)

    def test_two_elements_rotated_first(self):
        self._check([2, 1], 1, 1)

    def test_two_elements_rotated_second(self):
        self._check([1, 2], 2, 1)

    def test_two_elements_missing(self):
        self._check([2, 1], 3, -1)

    def test_unrotated_sorted(self):
        self._check([1, 2, 3, 4, 5], 4, 3)

    def test_unrotated_sorted_missing_low(self):
        self._check([1, 2, 3, 4, 5], 0, -1)

    def test_unrotated_sorted_missing_high(self):
        self._check([1, 2, 3, 4, 5], 6, -1)

    def test_rotated_at_one(self):
        self._check([2, 3, 4, 5, 1], 1, 4)

    def test_rotated_at_one_missing(self):
        self._check([2, 3, 4, 5, 1], 0, -1)

    def test_rotated_full(self):
        self._check([3, 4, 5, 1, 2], 5, 2)

    def test_negative_numbers(self):
        self._check([-1, -10, -5, 0, 3], -10, 1)

    def test_negative_missing(self):
        self._check([-1, -10, -5, 0, 3], -6, -1)

    def test_extreme_values(self):
        self._check([9999, 10000, -10000, -5, 0], -10000, 2)

    def test_target_at_boundaries(self):
        self._check([5, 6, 7, 8, 9, 1, 2, 3, 4], 9, 4)
        self._check([5, 6, 7, 8, 9, 1, 2, 3, 4], 1, 5)

    def test_larger_rotated(self):
        self._check(list(range(100, 200)) + list(range(0, 100)), 0, 100)
        self._check(list(range(100, 200)) + list(range(0, 100)), 199, 99)
        self._check(list(range(100, 200)) + list(range(0, 100)), 150, 50)
        self._check(list(range(100, 200)) + list(range(0, 100)), 50, 150)

    def test_5000_elements(self):
        nums = list(range(2500, 5000)) + list(range(0, 2500))
        self._check(nums, 0, 2500)
        self._check(nums, 4999, 2499)
        self._check(nums, 1250, 3750)
        self._check(nums, 2500, 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
