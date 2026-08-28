# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Medium

import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        raise Exception("Not solved yet")


class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertTrue(self.s.canJump([2, 3, 1, 1, 4]))

    def test_example2(self):
        self.assertFalse(self.s.canJump([3, 2, 1, 0, 4]))

    def test_single_element_zero(self):
        self.assertTrue(self.s.canJump([0]))

    def test_single_element_positive(self):
        self.assertTrue(self.s.canJump([5]))

    def test_two_elements_reachable(self):
        self.assertTrue(self.s.canJump([1, 1]))

    def test_two_elements_zero_first(self):
        self.assertFalse(self.s.canJump([0, 1]))

    def test_zero_skipped_over(self):
        self.assertTrue(self.s.canJump([3, 0, 0, 1]))

    def test_short_fall(self):
        self.assertFalse(self.s.canJump([1, 0, 0, 1]))

    def test_all_zeros_length_two(self):
        self.assertFalse(self.s.canJump([0, 0]))

    def test_all_zeros_length_three(self):
        self.assertFalse(self.s.canJump([0, 0, 0]))

    def test_zero_blocks_middle(self):
        self.assertFalse(self.s.canJump([2, 1, 0, 2]))

    def test_zero_within_reach(self):
        self.assertTrue(self.s.canJump([2, 0, 1]))

    def test_zero_at_last(self):
        self.assertTrue(self.s.canJump([3, 0, 2, 1, 0]))

    def test_big_jump(self):
        self.assertTrue(self.s.canJump([100000, 0, 0, 0]))

    def test_staircase_reachable(self):
        self.assertTrue(self.s.canJump([1, 1, 1, 1, 1]))

    def test_staircase_blocked(self):
        self.assertFalse(self.s.canJump([1, 1, 0, 1, 1]))

    def test_exact_reach(self):
        self.assertTrue(self.s.canJump([2, 1, 1]))

    def test_fall_one_short(self):
        self.assertFalse(self.s.canJump([2, 0, 0, 2]))

    def test_alternating(self):
        self.assertTrue(self.s.canJump([5, 0, 5, 0, 5]))

    def test_alternating_blocked(self):
        self.assertFalse(self.s.canJump([1, 0, 1, 0, 1]))

    def test_zero_head_blocks(self):
        self.assertFalse(self.s.canJump([0, 2, 3]))

    def test_multi_zero_run_skipped(self):
        self.assertTrue(self.s.canJump([4, 0, 0, 0, 2]))

    def test_multi_zero_run_blocks(self):
        self.assertFalse(self.s.canJump([3, 0, 0, 0, 2]))

    def test_long_all_ones(self):
        self.assertTrue(self.s.canJump([1] * 10000))

    def test_long_blocked(self):
        nums = [1] * 10000
        nums[5000] = 0
        self.assertFalse(self.s.canJump(nums))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Greedy
