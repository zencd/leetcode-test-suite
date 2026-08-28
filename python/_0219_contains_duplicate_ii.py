# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Easy

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_example2_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 0, 1, 1], 1))

    def test_example3_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_single_element_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1], 1))

    def test_two_equal_within_k_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 1], 1))

    def test_two_equal_beyond_k_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 0, 1, 2, 3], 1))

    def test_k_zero_always_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 1, 2, 2], 0))

    def test_all_duplicates_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([5, 5, 5, 5], 2))

    def test_negative_numbers_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([-1, -1], 1))

    def test_negative_numbers_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([-1, 2, -1], 1))

    def test_boundary_index_difference_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 3))

    def test_boundary_index_difference_plus_one_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 4, 1], 3))

    def test_k_larger_than_array_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3], 10))

    def test_k_larger_than_array_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1], 10))

    def test_large_numbers_same_value_true(self):
        big = 10**9
        small = -(10**9)
        self.assertTrue(self.sol.containsNearbyDuplicate([big, small, big], 2))

    def test_all_distinct_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 4, 5], 5))

    def test_duplicate_at_very_start_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([7, 7, 8, 9], 1))

    def test_mixed_duplicates_only_far_apart_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([9, 1, 4, 8, 10, 4, 1], 2))

    def test_window_slides_correctly_true(self):
        self.assertTrue(self.sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3, 1], 4))

    def test_window_slides_correctly_false(self):
        self.assertFalse(self.sol.containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7], 4))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Sliding Window
