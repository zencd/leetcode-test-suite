# 198. House Robber
# https://leetcode.com/problems/house-robber/
# Medium

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_house(self):
        self.assertEqual(self.sol.rob([5]), 5)

    def test_single_house_zero(self):
        self.assertEqual(self.sol.rob([0]), 0)

    def test_two_houses(self):
        self.assertEqual(self.sol.rob([1, 2]), 2)

    def test_two_equal_houses(self):
        self.assertEqual(self.sol.rob([3, 3]), 3)

    def test_two_zero_houses(self):
        self.assertEqual(self.sol.rob([0, 0]), 0)

    def test_three_houses(self):
        self.assertEqual(self.sol.rob([2, 1, 3]), 5)

    def test_example_1(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)

    def test_example_2(self):
        self.assertEqual(self.sol.rob([2, 7, 9, 3, 1]), 12)

    def test_increasing(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 4, 5]), 9)

    def test_decreasing(self):
        self.assertEqual(self.sol.rob([5, 4, 3, 2, 1]), 9)

    def test_all_zeros(self):
        self.assertEqual(self.sol.rob([0, 0, 0]), 0)

    def test_all_max_values(self):
        self.assertEqual(self.sol.rob([400] * 100), 400 * 50)

    def test_alternating_pattern(self):
        self.assertEqual(self.sol.rob([400, 0, 400, 0, 400]), 1200)

    def test_even_length(self):
        self.assertEqual(self.sol.rob([1, 1, 1, 1]), 2)

    def test_odd_length(self):
        self.assertEqual(self.sol.rob([1, 1, 1, 1, 1]), 3)

    def test_first_house_best(self):
        self.assertEqual(self.sol.rob([10, 1, 1]), 11)

    def test_last_house_best(self):
        self.assertEqual(self.sol.rob([1, 1, 10]), 11)

    def test_middle_house_best(self):
        self.assertEqual(self.sol.rob([1, 10, 1]), 10)

    def test_large_input_100_houses(self):
        nums = [400] * 100
        self.assertEqual(self.sol.rob(nums), 20000)

    def test_mixed_values(self):
        self.assertEqual(self.sol.rob([3, 1, 4, 1, 5, 9, 2, 6, 5]), 22)

    def test_result_is_int(self):
        self.assertIsInstance(self.sol.rob([1, 2]), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
