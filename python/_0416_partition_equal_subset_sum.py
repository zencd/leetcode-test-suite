# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# Medium

from typing import List
import unittest


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.canPartition([1, 5, 11, 5]))

    def test_example2(self):
        self.assertFalse(self.sol.canPartition([1, 2, 3, 5]))

    def test_single_element(self):
        self.assertFalse(self.sol.canPartition([1]))

    def test_single_large_element(self):
        self.assertFalse(self.sol.canPartition([100]))

    def test_two_equal_elements(self):
        self.assertTrue(self.sol.canPartition([5, 5]))

    def test_two_unequal_elements(self):
        self.assertFalse(self.sol.canPartition([3, 7]))

    def test_all_ones_even_count(self):
        self.assertTrue(self.sol.canPartition([1, 1, 1, 1]))

    def test_all_ones_odd_count(self):
        self.assertFalse(self.sol.canPartition([1, 1, 1]))

    def test_all_equal_even(self):
        self.assertTrue(self.sol.canPartition([3, 3, 3, 3]))

    def test_all_equal_odd(self):
        self.assertFalse(self.sol.canPartition([3, 3, 3]))

    def test_order_independence(self):
        self.assertEqual(
            self.sol.canPartition([1, 5, 11, 5]),
            self.sol.canPartition([11, 5, 1, 5]),
        )

    def test_true_small(self):
        self.assertTrue(self.sol.canPartition([1, 5, 6, 10]))

    def test_false_small(self):
        self.assertFalse(self.sol.canPartition([2, 2, 3, 5]))

    def test_false_three(self):
        self.assertFalse(self.sol.canPartition([1, 1, 4]))

    def test_true_three(self):
        self.assertTrue(self.sol.canPartition([1, 2, 3]))

    def test_max_values_partitionable(self):
        self.assertTrue(self.sol.canPartition([100] * 200))

    def test_max_values_not_partitionable(self):
        self.assertFalse(self.sol.canPartition([100] * 199))

    def test_mixed_large(self):
        nums = [199] + [1] * 199
        self.assertTrue(self.sol.canPartition(nums))

    def test_one_dominant_impossible(self):
        self.assertTrue(self.sol.canPartition([7, 3, 4, 2, 4]))

    def test_odd_total(self):
        self.assertFalse(self.sol.canPartition([1, 2, 4]))

    def test_duplicates(self):
        self.assertTrue(self.sol.canPartition([2, 2, 2, 2, 2, 2]))

    def test_no_subsum(self):
        self.assertFalse(self.sol.canPartition([1, 2, 5, 10, 11, 11]))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
