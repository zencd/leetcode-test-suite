# 46. Permutations
# https://leetcode.com/problems/permutations/
# Medium

import itertools
import unittest
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        raise Exception("Not solved yet")


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_element(self):
        self.assertEqual(self.sol.permute([1]), [[1]])

    def test_two_elements(self):
        self.assertEqual(self.sol.permute([0, 1]), [[0, 1], [1, 0]])

    def test_three_elements(self):
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        self.assertEqual(
            sorted(map(tuple, self.sol.permute([1, 2, 3]))),
            sorted(map(tuple, expected)),
        )

    def test_result_is_set_equal(self):
        expected = {
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        }
        self.assertEqual({tuple(p) for p in self.sol.permute([1, 2, 3])}, expected)

    def test_negative_numbers(self):
        result = self.sol.permute([-1, 0])
        self.assertEqual(sorted(map(tuple, result)), [(-1, 0), (0, -1)])

    def test_all_negative(self):
        result = self.sol.permute([-3, -2, -1])
        self.assertEqual(len(result), 6)
        expected = set(itertools.permutations([-3, -2, -1]))
        self.assertEqual({tuple(p) for p in result}, expected)

    def test_zero_and_positive(self):
        result = self.sol.permute([0, 5])
        self.assertEqual(sorted(map(tuple, result)), [(0, 5), (5, 0)])

    def test_boundary_values(self):
        result = self.sol.permute([-10, 10])
        self.assertEqual(sorted(map(tuple, result)), [(-10, 10), (10, -10)])

    def test_three_elements_count(self):
        self.assertEqual(len(self.sol.permute([1, 2, 3])), 6)

    def test_four_elements_count(self):
        self.assertEqual(len(self.sol.permute([1, 2, 3, 4])), 24)

    def test_six_elements_count(self):
        self.assertEqual(len(self.sol.permute([1, 2, 3, 4, 5, 6])), 720)

    def test_each_permutation_is_permutation_of_input(self):
        nums = [1, 2, 3, 4]
        for p in self.sol.permute(nums):
            self.assertEqual(sorted(p), sorted(nums))

    def test_all_permutations_unique(self):
        nums = [1, 2, 3, 4]
        result = self.sol.permute(nums)
        tuples = [tuple(p) for p in result]
        self.assertEqual(len(tuples), len(set(tuples)))

    def test_completeness_four_elements(self):
        result = {tuple(p) for p in self.sol.permute([1, 2, 3, 4])}
        self.assertEqual(result, set(itertools.permutations([1, 2, 3, 4])))

    def test_does_not_mutate_input(self):
        nums = [1, 2, 3]
        copy = nums.copy()
        self.sol.permute(nums)
        self.assertEqual(nums, copy)

    def test_permutations_are_copies(self):
        result = self.sol.permute([1, 2, 3])
        self.assertIsNot(result[0], result[1])

    def test_six_elements_full_match(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = {tuple(p) for p in self.sol.permute(nums)}
        self.assertEqual(result, set(itertools.permutations(nums)))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Backtracking
