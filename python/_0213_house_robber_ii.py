# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Medium

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertEqual(self.sol.rob([5]), 5)

    def test_single_zero(self):
        self.assertEqual(self.sol.rob([0]), 0)

    def test_two_elements(self):
        self.assertEqual(self.sol.rob([1, 2]), 2)

    def test_two_elements_first_larger(self):
        self.assertEqual(self.sol.rob([100, 1]), 100)

    def test_two_equal(self):
        self.assertEqual(self.sol.rob([7, 7]), 7)

    def test_example_1(self):
        self.assertEqual(self.sol.rob([2, 3, 2]), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)

    def test_example_3(self):
        self.assertEqual(self.sol.rob([1, 2, 3]), 3)

    def test_three_all_equal(self):
        self.assertEqual(self.sol.rob([5, 5, 5]), 5)

    def test_wraparound_disables_both_ends(self):
        self.assertEqual(self.sol.rob([10, 1, 1]), 10)

    def test_wraparound_disables_last(self):
        self.assertEqual(self.sol.rob([1, 1, 10]), 10)

    def test_mixed_wraparound(self):
        self.assertEqual(self.sol.rob([8, 1, 1, 9]), 10)

    def test_all_zeros(self):
        self.assertEqual(self.sol.rob([0, 0, 0, 0]), 0)

    def test_single_zero_among_positives(self):
        self.assertEqual(self.sol.rob([0, 1, 1]), 1)

    def test_alternating_rob_all(self):
        self.assertEqual(self.sol.rob([1, 0, 1, 0, 1]), 2)

    def test_increasing(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 4, 5]), 8)

    def test_decreasing(self):
        self.assertEqual(self.sol.rob([5, 4, 3, 2, 1]), 8)

    def test_longer_sequence(self):
        self.assertEqual(self.sol.rob([2, 7, 9, 3, 1]), 11)

    def test_large_values(self):
        self.assertEqual(self.sol.rob([1000, 1, 1000, 1, 1000]), 2000)

    def test_max_length(self):
        nums = [1000] * 100
        expected = 50 * 1000
        self.assertEqual(self.sol.rob(nums), expected)

    def test_does_not_mutate_input(self):
        nums = [1, 2, 3, 1]
        copy = nums[:]
        self.sol.rob(nums)
        self.assertEqual(nums, copy)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
