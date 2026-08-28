# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Easy

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.containsDuplicate([1, 2, 3, 1]))

    def test_example2(self):
        self.assertFalse(self.sol.containsDuplicate([1, 2, 3, 4]))

    def test_example3(self):
        self.assertTrue(self.sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_all_same_elements(self):
        self.assertTrue(self.sol.containsDuplicate([5, 5, 5, 5]))

    def test_single_element(self):
        self.assertFalse(self.sol.containsDuplicate([42]))

    def test_two_elements_same(self):
        self.assertTrue(self.sol.containsDuplicate([7, 7]))

    def test_two_elements_distinct(self):
        self.assertFalse(self.sol.containsDuplicate([7, 8]))

    def test_negative_numbers_with_duplicate(self):
        self.assertTrue(self.sol.containsDuplicate([-1, -2, -1, 3]))

    def test_negative_numbers_distinct(self):
        self.assertFalse(self.sol.containsDuplicate([-10, -100, -1000]))

    def test_mixed_positive_negative_distinct(self):
        self.assertFalse(self.sol.containsDuplicate([-1, 0, 1]))

    def test_mixed_positive_negative_duplicate(self):
        self.assertTrue(self.sol.containsDuplicate([-1, 0, 1, -1]))

    def test_zero_value_duplicate(self):
        self.assertTrue(self.sol.containsDuplicate([0, 0]))

    def test_zero_value_single(self):
        self.assertFalse(self.sol.containsDuplicate([0]))

    def test_large_values_distinct(self):
        nums = [10**9, -(10**9), 999999999]
        self.assertFalse(self.sol.containsDuplicate(nums))

    def test_large_values_duplicate(self):
        nums = [10**9, 5, 10**9]
        self.assertTrue(self.sol.containsDuplicate(nums))

    def test_duplicate_at_ends(self):
        self.assertTrue(self.sol.containsDuplicate([9, 1, 2, 3, 9]))

    def test_duplicate_adjacent(self):
        self.assertTrue(self.sol.containsDuplicate([1, 2, 2, 3]))

    def test_long_array_all_distinct(self):
        nums = list(range(1000))
        self.assertFalse(self.sol.containsDuplicate(nums))

    def test_long_array_one_duplicate(self):
        nums = list(range(1000)) + [500]
        self.assertTrue(self.sol.containsDuplicate(nums))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Sorting
