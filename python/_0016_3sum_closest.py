# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/
# Medium

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        raise Exception("Not solved yet")


import unittest


class ThreeSumClosestTests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_example2(self):
        self.assertEqual(self.sol.threeSumClosest([0, 0, 0], 1), 0)

    def test_exact_match(self):
        self.assertEqual(self.sol.threeSumClosest([1, 2, 3], 6), 6)

    def test_exact_match_negative(self):
        self.assertEqual(self.sol.threeSumClosest([-3, -2, -1], -6), -6)

    def test_minimal_input(self):
        self.assertEqual(self.sol.threeSumClosest([-1, 2, 1], 1), 2)

    def test_exact_sum_zero(self):
        self.assertEqual(self.sol.threeSumClosest([3, 2, -3, 1, 0, 4, -1], 2), 2)

    def test_all_negative(self):
        self.assertEqual(self.sol.threeSumClosest([-5, -4, -3, -2, -1], 5), -6)

    def test_all_positive(self):
        self.assertEqual(self.sol.threeSumClosest([1, 2, 3, 4, 5], 1), 6)

    def test_duplicates(self):
        self.assertEqual(self.sol.threeSumClosest([2, 2, 2, 2, 2], 5), 6)

    def test_negative_target_closest_above(self):
        self.assertEqual(self.sol.threeSumClosest([-1, 2, 1, -4], -10), -4)

    def test_large_positive_target(self):
        self.assertEqual(self.sol.threeSumClosest([1, 2, 3], 10000), 6)

    def test_negative_target(self):
        self.assertEqual(self.sol.threeSumClosest([-1, 2, 1, -4], -5), -4)

    def test_mixed_positive_negative(self):
        self.assertEqual(self.sol.threeSumClosest([-4, -1, -1, 0, 1, 2, 3], 0), 0)

    def test_closest_is_less_than_target(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(self.sol.threeSumClosest(arr, 100), 3)

    def test_closest_is_greater_than_target(self):
        arr = [-1, -1, -1, -1, -1]
        self.assertEqual(self.sol.threeSumClosest(arr, -100), -3)

    def test_target_between_candidates(self):
        self.assertEqual(self.sol.threeSumClosest([-5, 1, 2], 10), -2)

    def test_large_array(self):
        nums = list(range(-250, 250))
        self.assertEqual(self.sol.threeSumClosest(nums, 0), 0)

    def test_constraint_bounds(self):
        nums = [-1000, -1000, 1000]
        self.assertEqual(self.sol.threeSumClosest(nums, 10000), -1000)

    def test_original_order_not_dependent(self):
        self.assertEqual(
            self.sol.threeSumClosest([-1, 2, 1, -4], 1),
            self.sol.threeSumClosest([2, -4, -1, 1], 1),
        )

    def test_closest_sum_not_exact(self):
        self.assertEqual(self.sol.threeSumClosest([8, -7, 3, 5, -2, 4, 1], 9), 9)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Sorting
