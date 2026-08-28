# 154. Find Minimum in Rotated Sorted Array II
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Hard

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findMin([1, 3, 5]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.findMin([2, 2, 2, 0, 1]), 0)

    def test_task_example_rotated_4_times(self):
        self.assertEqual(self.sol.findMin([4, 5, 6, 7, 0, 1, 4]), 0)

    def test_single_element(self):
        self.assertEqual(self.sol.findMin([1]), 1)
        self.assertEqual(self.sol.findMin([-5]), -5)

    def test_two_elements_unrotated(self):
        self.assertEqual(self.sol.findMin([1, 2]), 1)

    def test_two_elements_rotated(self):
        self.assertEqual(self.sol.findMin([2, 1]), 1)

    def test_unsorted_full_sorted_array(self):
        self.assertEqual(self.sol.findMin([0, 1, 2, 3, 4, 5, 6, 7]), 0)

    def test_minimum_at_end(self):
        self.assertEqual(self.sol.findMin([5, 6, 7, 1, 2, 3, 4]), 1)

    def test_minimum_at_middle(self):
        self.assertEqual(self.sol.findMin([3, 4, 5, 6, 1, 2]), 1)

    def test_minimum_right_after_start(self):
        self.assertEqual(self.sol.findMin([2, 1, 3, 4, 5]), 1)

    def test_all_duplicate_min(self):
        self.assertEqual(self.sol.findMin([2, 2, 2, 2, 2]), 2)

    def test_all_duplicate_negative_min(self):
        self.assertEqual(self.sol.findMin([-7, -7, -7]), -7)

    def test_duplicates_on_both_sides(self):
        self.assertEqual(self.sol.findMin([3, 3, 3, 1, 2, 3, 3]), 1)

    def test_duplicates_with_negative_values(self):
        self.assertEqual(self.sol.findMin([-1, -1, 0, -1, -1]), -1)

    def test_negative_values_rotated(self):
        self.assertEqual(self.sol.findMin([5, 7, -2, 0, 3]), -2)

    def test_sorted_negative_values(self):
        self.assertEqual(self.sol.findMin([-5, -3, -1, 0, 2, 4]), -5)

    def test_extreme_constraint_values(self):
        self.assertEqual(self.sol.findMin([-5000, -5000, 5000]), -5000)
        self.assertEqual(self.sol.findMin([4999, 5000, -5000, -4999, -4999]), -5000)

    def test_two_duplicates(self):
        self.assertEqual(self.sol.findMin([2, 2]), 2)

    def test_minimum_not_unique(self):
        self.assertEqual(self.sol.findMin([1, 3, 3, 3, 3]), 1)
        self.assertEqual(self.sol.findMin([0, 0, 1, 2]), 0)

    def test_large_array_rotated(self):
        nums = list(range(10, 110)) + list(range(0, 10))
        self.assertEqual(self.sol.findMin(nums), 0)

    def test_large_array_rotated_with_duplicates(self):
        nums = [7] * 40 + [3] + [4, 5, 6] * 10
        self.assertEqual(self.sol.findMin(nums), 3)

    def test_worst_case_many_duplicates(self):
        self.assertEqual(self.sol.findMin([6, *([7] * 100), 8, 9, 1, 2, 3, 4, 5]), 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search
