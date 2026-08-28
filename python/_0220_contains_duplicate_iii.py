# 220. Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/
# Hard

from typing import List
import unittest


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def contains(self, nums, indexDiff, valueDiff):
        return self.solution.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)

    def test_example_1(self):
        self.assertTrue(self.contains([1, 2, 3, 1], 3, 0))

    def test_example_2(self):
        self.assertFalse(self.contains([1, 5, 9, 1, 5, 9], 2, 3))

    def test_two_elements_equal(self):
        self.assertTrue(self.contains([1, 1], 1, 0))

    def test_two_elements_within_value_diff(self):
        self.assertTrue(self.contains([1, 2], 1, 1))

    def test_two_elements_outside_value_diff(self):
        self.assertFalse(self.contains([1, 2], 1, 0))

    def test_two_elements_negative(self):
        self.assertTrue(self.contains([-1, -1], 1, 0))

    def test_index_diff_too_small(self):
        self.assertFalse(self.contains([1, 10, 1], 1, 0))

    def test_index_diff_equal_distance(self):
        self.assertTrue(self.contains([1, 10, 1], 2, 0))

    def test_index_diff_full_length(self):
        self.assertTrue(self.contains([1, 100, 200, 1], 4, 0))

    def test_negative_values_close(self):
        self.assertTrue(self.contains([-10, -9, -8], 2, 1))

    def test_negative_values_far(self):
        self.assertFalse(self.contains([-100, -1, 100], 2, 1))

    def test_mixed_signs_boundary_bucket(self):
        self.assertTrue(self.contains([-1, 1, -1], 2, 2))

    def test_value_diff_zero_requires_exact_match(self):
        self.assertFalse(self.contains([1, 2, 3, 4, 5], 5, 0))

    def test_value_diff_zero_with_duplicate(self):
        self.assertTrue(self.contains([1, 2, 3, 2, 5], 3, 0))

    def test_large_numbers(self):
        self.assertTrue(self.contains([10**9, -(10**9), 10**9], 2, 2 * 10**9))

    def test_large_numbers_too_far(self):
        self.assertFalse(self.contains([10**9, -(10**9)], 1, 2 * 10**9 - 1))

    def test_repeated_value_in_window(self):
        self.assertTrue(self.contains([3, 1, 2, 1], 2, 0))

    def test_repeated_value_outside_window(self):
        self.assertFalse(self.contains([5, 1, 5, 2], 1, 0))

    def test_sliding_window_boundary(self):
        self.assertFalse(self.contains([1, 100, 50], 1, 10))

    def test_sliding_window_boundary_hit(self):
        self.assertTrue(self.contains([1, 100, 101], 1, 10))

    def test_all_same_elements(self):
        self.assertTrue(self.contains([7, 7, 7, 7], 2, 0))

    def test_decreasing_sequence(self):
        self.assertTrue(self.contains([5, 4, 3, 2, 1], 2, 1))

    def test_increasing_sequence(self):
        self.assertTrue(self.contains([1, 2, 3, 4, 5], 2, 1))

    def test_alternating_close_values(self):
        self.assertTrue(self.contains([10, 11, 10, 11], 1, 1))

    def test_long_array_pair_outside_window(self):
        self.assertFalse(self.contains([3, 1, 4, 1, 5], 1, 0))

    def test_long_array_pair_within_window(self):
        self.assertTrue(self.contains([3, 1, 4, 1, 5], 2, 0))

    def test_pair_crossing_bucket_boundary(self):
        self.assertTrue(self.contains([4, 10], 1, 6))

    def test_pair_just_outside_bucket_boundary(self):
        self.assertFalse(self.contains([4, 10], 1, 5))

    def test_single_window_pair_hit(self):
        self.assertTrue(self.contains([7, 18, 20], 2, 2))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
