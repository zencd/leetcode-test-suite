# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/
# Easy

from typing import List
import unittest


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.summaryRanges([0, 1, 2, 4, 5, 7]),
            ["0->2", "4->5", "7"],
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]),
            ["0", "2->4", "6", "8->9"],
        )

    def test_empty_list(self):
        self.assertEqual(self.solution.summaryRanges([]), [])

    def test_single_element(self):
        self.assertEqual(self.solution.summaryRanges([42]), ["42"])

    def test_single_element_negative(self):
        self.assertEqual(self.solution.summaryRanges([-1]), ["-1"])

    def test_two_consecutive(self):
        self.assertEqual(self.solution.summaryRanges([1, 2]), ["1->2"])

    def test_two_non_consecutive(self):
        self.assertEqual(self.solution.summaryRanges([1, 3]), ["1", "3"])

    def test_all_consecutive(self):
        self.assertEqual(self.solution.summaryRanges([1, 2, 3, 4, 5]), ["1->5"])

    def test_all_isolated(self):
        self.assertEqual(
            self.solution.summaryRanges([1, 3, 5, 7, 9]),
            ["1", "3", "5", "7", "9"],
        )

    def test_negative_numbers(self):
        self.assertEqual(
            self.solution.summaryRanges([-3, -2, 0, 1, 2, 5]),
            ["-3->-2", "0->2", "5"],
        )

    def test_crossing_zero(self):
        self.assertEqual(
            self.solution.summaryRanges([-2, -1, 0, 1, 3]),
            ["-2->1", "3"],
        )

    def test_extreme_int_values(self):
        self.assertEqual(
            self.solution.summaryRanges([-2147483648, -2147483647, 2147483647]),
            ["-2147483648->-2147483647", "2147483647"],
        )

    def test_max_boundary_values_together(self):
        self.assertEqual(
            self.solution.summaryRanges([2147483645, 2147483646, 2147483647]),
            ["2147483645->2147483647"],
        )

    def test_max_range_length_20(self):
        nums = list(range(10, 30))
        self.assertEqual(self.solution.summaryRanges(nums), ["10->29"])

    def test_does_not_modify_input(self):
        nums = [0, 1, 2, 4, 5, 7]
        original = list(nums)
        self.solution.summaryRanges(nums)
        self.assertEqual(nums, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array
