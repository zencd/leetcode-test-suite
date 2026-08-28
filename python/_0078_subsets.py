# 78. Subsets
# https://leetcode.com/problems/subsets/
# Medium

from typing import List
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        raise Exception("Not solved yet")


class TestSubsets(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(Solution().subsets([0]), [[], [0]])

    def test_three_elements(self):
        got = Solution().subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(
            sorted(map(tuple, sorted(got))), sorted(map(tuple, sorted(expected)))
        )

    def test_two_elements(self):
        self.assertEqual(Solution().subsets([1, 2]), [[], [1], [2], [1, 2]])

    def test_negative_numbers(self):
        got = Solution().subsets([-5, 3])
        expected = [[], [-5], [3], [-5, 3]]
        self.assertEqual(
            sorted(map(tuple, sorted(got))), sorted(map(tuple, sorted(expected)))
        )

    def test_max_range_values(self):
        got = Solution().subsets([-10, 10])
        expected = [[], [-10], [10], [-10, 10]]
        self.assertEqual(
            sorted(map(tuple, sorted(got))), sorted(map(tuple, sorted(expected)))
        )

    def test_count_is_power_of_two(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(len(Solution().subsets(nums)), 2 ** len(nums))

    def test_subsets_lengths(self):
        nums = [1, 2, 3]
        got = Solution().subsets(nums)
        lengths = sorted(len(s) for s in got)
        self.assertEqual(lengths, [0, 1, 1, 1, 2, 2, 2, 3])

    def test_tenth_element_max_size_input(self):
        nums = list(range(10))
        got = Solution().subsets(nums)
        self.assertEqual(len(got), 1024)
        self.assertIn(list(nums), got)

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4]
        got = Solution().subsets(nums)
        tuples = sorted(map(tuple, map(sorted, got)))
        self.assertEqual(len(tuples), len(set(tuples)))

    def test_contains_empty_and_full(self):
        nums = [7, -2, 9]
        got = Solution().subsets(nums)
        self.assertIn([], got)
        self.assertIn([7, -2, 9], got)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking, Bit Manipulation
