# 462. Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Medium

from typing import List
import unittest


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minMoves2([1, 2, 3]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.minMoves2([1, 10, 2, 9]), 16)

    def test_single_element(self):
        self.assertEqual(self.solution.minMoves2([5]), 0)

    def test_already_equal(self):
        self.assertEqual(self.solution.minMoves2([7, 7, 7, 7]), 0)

    def test_two_elements(self):
        self.assertEqual(self.solution.minMoves2([1, 3]), 2)

    def test_two_elements_large_gap(self):
        self.assertEqual(self.solution.minMoves2([0, 100]), 100)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.minMoves2([-1, -2, -3]), 2)

    def test_mixed_signs(self):
        self.assertEqual(self.solution.minMoves2([-1, 0, 1]), 2)

    def test_unsorted_input(self):
        self.assertEqual(self.solution.minMoves2([3, 1, 2]), 2)

    def test_odd_length_even_length(self):
        self.assertEqual(self.solution.minMoves2([1, 2, 3, 4]), 4)
        self.assertEqual(self.solution.minMoves2([1, 2, 3, 4, 5]), 6)

    def test_duplicated_elements(self):
        self.assertEqual(self.solution.minMoves2([2, 2, 3, 3]), 2)

    def test_extreme_values(self):
        self.assertEqual(self.solution.minMoves2([-(10**9), 10**9]), 2 * 10**9)

    def test_large_array_uniform(self):
        self.assertEqual(self.solution.minMoves2([42] * 100000), 0)

    def test_large_array_sequential(self):
        n = 100000
        nums = list(range(n))
        median = n // 2
        expected = sum(abs(x - median) for x in nums)
        self.assertEqual(self.solution.minMoves2(nums), expected)

    def test_does_not_mutate_input(self):
        nums = [3, 1, 2]
        expected = nums.copy()
        self.solution.minMoves2(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Sorting
