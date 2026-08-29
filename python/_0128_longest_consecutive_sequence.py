# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Medium

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_example2(self):
        self.assertEqual(
            self.solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9
        )

    def test_example3(self):
        self.assertEqual(self.solution.longestConsecutive([1, 0, 1, 2]), 3)

    def test_empty(self):
        self.assertEqual(self.solution.longestConsecutive([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.longestConsecutive([42]), 1)

    def test_all_duplicates(self):
        self.assertEqual(self.solution.longestConsecutive([7, 7, 7, 7]), 1)

    def test_two_elements_consecutive(self):
        self.assertEqual(self.solution.longestConsecutive([1, 2]), 2)

    def test_two_elements_non_consecutive(self):
        self.assertEqual(self.solution.longestConsecutive([1, 3]), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.longestConsecutive([-1, 0, 1, 2, -2]), 5)

    def test_all_negative_numbers(self):
        self.assertEqual(self.solution.longestConsecutive([-5, -3, -4, -2]), 4)

    def test_large_values(self):
        self.assertEqual(
            self.solution.longestConsecutive([2147483647, -2147483648, 0]), 1
        )

    def test_already_sorted(self):
        self.assertEqual(self.solution.longestConsecutive([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted(self):
        self.assertEqual(self.solution.longestConsecutive([5, 4, 3, 2, 1]), 5)

    def test_gaps(self):
        self.assertEqual(self.solution.longestConsecutive([1, 3, 5, 7, 9]), 1)

    def test_mixed_sequences(self):
        self.assertEqual(self.solution.longestConsecutive([1, 2, 10, 11, 12, 20]), 3)

    def test_zero_in_sequence(self):
        self.assertEqual(self.solution.longestConsecutive([-1, 0, 1]), 3)

    def test_many_duplicates(self):
        self.assertEqual(
            self.solution.longestConsecutive([1, 1, 1, 2, 2, 2, 3, 3, 3]), 3
        )

    def test_single_negative(self):
        self.assertEqual(self.solution.longestConsecutive([-1000000000]), 1)

    def test_two_same(self):
        self.assertEqual(self.solution.longestConsecutive([0, 0]), 1)

    def test_long_sequence(self):
        self.assertEqual(self.solution.longestConsecutive(list(range(1000))), 1000)

    def test_unordered_long_sequence(self):
        import random

        random.seed(0)
        nums = list(range(1000))
        random.shuffle(nums)
        self.assertEqual(self.solution.longestConsecutive(nums), 1000)

    def test_duplicates_in_long_sequence(self):
        nums = list(range(500)) * 2
        self.assertEqual(self.solution.longestConsecutive(nums), 500)

    def test_cross_zero_boundary(self):
        self.assertEqual(self.solution.longestConsecutive([-2, -1, 0, 1]), 4)

    def test_isolated_elements(self):
        self.assertEqual(self.solution.longestConsecutive([10, 20, 30, 40]), 1)

    def test_large_numbers_close(self):
        self.assertEqual(self.solution.longestConsecutive([999999999, 1000000000]), 2)

    def test_large_numbers_sequence(self):
        self.assertEqual(
            self.solution.longestConsecutive([1000000000, 999999999, 999999998]), 3
        )

    def test_mixed_pos_neg_isolated(self):
        self.assertEqual(self.solution.longestConsecutive([-5, -3, 5, 3]), 1)

    def test_duplicates_and_gaps(self):
        self.assertEqual(self.solution.longestConsecutive([2, 2, 6, 4, 8, 10]), 1)

    def test_extra_1(self):
        self.assertEqual(self.solution.longestConsecutive([4, 2, 2, -4, 0, -2, 4, -3, -4, -4, -5, 1, 4, -9, 5, 0, 6, -8, -1, -3, 6, 5, -8, -1, -5, -1, 2, -9, 1]), 8)

    def test_merge_then_duplicate(self):
        self.assertEqual(self.solution.longestConsecutive([-4, -2, -1, 1, 0, -3, 0, 2]), 7)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Union-Find
