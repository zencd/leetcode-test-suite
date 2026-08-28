# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Medium

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestJump(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertEqual(self.sol.jump([0]), 0)

    def test_single_element_jumps(self):
        self.assertEqual(self.sol.jump([1]), 0)

    def test_example1(self):
        self.assertEqual(self.sol.jump([2, 3, 1, 1, 4]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.jump([2, 3, 0, 1, 4]), 2)

    def test_all_ones(self):
        self.assertEqual(self.sol.jump([1, 1, 1, 1, 1]), 4)

    def test_direct_jump(self):
        self.assertEqual(self.sol.jump([5, 0, 0, 0, 0, 0]), 1)

    def test_zeros_in_middle(self):
        self.assertEqual(self.sol.jump([1, 0, 1]), 2)

    def test_two_elements(self):
        self.assertEqual(self.sol.jump([1, 0]), 1)

    def test_reach_in_first_jump(self):
        self.assertEqual(self.sol.jump([3, 0, 0, 0]), 1)

    def test_large_jump_value(self):
        self.assertEqual(self.sol.jump([1000] + [0] * 999), 1)

    def test_staircase(self):
        self.assertEqual(self.sol.jump([1, 1, 1]), 2)

    def test_mixed(self):
        self.assertEqual(self.sol.jump([4, 1, 1, 3, 1, 1, 1]), 2)

    def test_zero_first_unreachable_excluded(self):
        self.assertEqual(self.sol.jump([1, 2, 2]), 2)

    def test_repeated_pattern(self):
        self.assertEqual(self.sol.jump([2, 1, 2, 1, 2]), 2)

    def test_alternating(self):
        self.assertEqual(self.sol.jump([3, 1, 3, 1, 3]), 2)

    def test_long_chain(self):
        nums = [1] * 100
        self.assertEqual(self.sol.jump(nums), 99)

    def test_optimal_greedy_chain(self):
        nums = [2, 2, 2, 2, 2]
        self.assertEqual(self.sol.jump(nums), 2)

    def test_no_jump_needed_single(self):
        nums = [42]
        self.assertEqual(self.sol.jump(nums), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Greedy
