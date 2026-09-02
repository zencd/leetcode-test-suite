# 220. Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/
# Hard

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))

    def test_example_2(self):
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))

    def test_adjacent_equal_values(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 1], 1, 0))

    def test_adjacent_diff_within_bound(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 2], 1, 1))

    def test_adjacent_diff_exceeding_bound(self):
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 3], 1, 1))

    def test_no_pair_with_small_index_diff(self):
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 4, 1], 1, 0))

    def test_pair_found_with_larger_index_diff(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 4, 1], 2, 0))

    def test_negative_numbers(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([-1, -1], 1, 0))

    def test_negative_and_positive(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([-5, -2, -5], 1, 3))

    def test_large_values_within_diff(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([10**9, 10**9 - 1], 1, 1))

    def test_large_values_exceeding_diff(self):
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([10**9, -(10**9)], 1, 10**9 - 1))

    def test_index_diff_equals_length(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 2, 3, 4], 4, 3))

    def test_value_diff_zero_requires_exact_match(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 2], 2, 1))
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 2], 2, 0))

    def test_all_distinct(self):
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 2, 3, 4, 5], 5, 0))

    def test_multiple_repeats(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 1, 1, 1], 1, 0))

    def test_repeats_out_of_window(self):
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 2, 3, 4, 1], 2, 0))

    def test_repeats_within_window(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 2, 3, 4, 1], 4, 0))

    def test_two_elements_boundary(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 2], 1, 1))
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 2], 1, 0))

    def test_mixed_signs_around_zero(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([-1, 1], 1, 2))
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([-2, 2], 1, 3))

    def test_cross_sign_close_pair(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([50, -26, 20, -25, 15, -45], 1, 84))
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([-26, 50], 1, 84))
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([-26, 50], 1, 75))

    def test_long_array_with_far_duplicates(self):
        nums = list(range(1, 100))
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate(nums, 1, 0))

    def test_long_array_with_near_duplicates(self):
        nums = [i for i in range(1, 50)] + [i for i in range(60, 110)]
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate(nums, 5, 5))

    def test_all_same_large(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([7] * 5, 2, 0))

    def test_interleaved_values(self):
        self.assertTrue(self.sol.containsNearbyAlmostDuplicate([1, 3, 5, 2, 4], 3, 1))
        self.assertFalse(self.sol.containsNearbyAlmostDuplicate([1, 3, 5, 7, 9], 2, 1))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
