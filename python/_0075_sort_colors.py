# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/
# Medium

import random
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def run_and_check(self, expected: List[int]) -> None:
        nums = list(expected)
        result = self.sol.sortColors(nums)
        self.assertIsNone(result)
        self.assertEqual(nums, sorted(expected))

    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self) -> None:
        self.run_and_check([2, 0, 2, 1, 1, 0])

    def test_example_2(self) -> None:
        self.run_and_check([2, 0, 1])

    def test_single_element_zero(self) -> None:
        self.run_and_check([0])

    def test_single_element_one(self) -> None:
        self.run_and_check([1])

    def test_single_element_two(self) -> None:
        self.run_and_check([2])

    def test_already_sorted(self) -> None:
        self.run_and_check([0, 0, 1, 1, 2, 2])

    def test_reverse_sorted(self) -> None:
        self.run_and_check([2, 2, 1, 1, 0, 0])

    def test_all_zeros(self) -> None:
        self.run_and_check([0, 0, 0, 0])

    def test_all_ones(self) -> None:
        self.run_and_check([1, 1, 1, 1])

    def test_all_twos(self) -> None:
        self.run_and_check([2, 2, 2, 2])

    def test_no_zeros(self) -> None:
        self.run_and_check([2, 1, 2, 1])

    def test_no_ones(self) -> None:
        self.run_and_check([2, 0, 2, 0])

    def test_no_twos(self) -> None:
        self.run_and_check([0, 1, 1, 0, 1])

    def test_two_elements(self) -> None:
        self.run_and_check([2, 0])

    def test_zeros_at_end(self) -> None:
        self.run_and_check([1, 2, 2, 0, 0])

    def test_alternating(self) -> None:
        self.run_and_check([0, 2, 0, 2, 0, 2, 0])

    def test_twos_in_middle(self) -> None:
        self.run_and_check([0, 1, 2, 1, 0])

    def test_long_run_of_ones(self) -> None:
        self.run_and_check([2, 1, 1, 1, 1, 1, 1, 1, 0])

    def test_max_size_random(self) -> None:
        expected = [random.choice([0, 1, 2]) for _ in range(300)]
        self.run_and_check(expected)

    def test_random_uniform_distribution(self) -> None:
        expected = [0] * 100 + [1] * 100 + [2] * 100
        random.shuffle(expected)
        self.run_and_check(expected)

    def test_preserves_input_list_object_in_place(self) -> None:
        nums = [2, 0, 2, 1, 1, 0]
        ident = id(nums)
        self.sol.sortColors(nums)
        self.assertEqual(ident, id(nums))
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_counts_preserved(self) -> None:
        original = [2, 0, 1, 1, 0, 2, 2, 0, 1]
        nums = original[:]
        before = {v: original.count(v) for v in (0, 1, 2)}
        self.sol.sortColors(nums)
        after = {v: nums.count(v) for v in (0, 1, 2)}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Sorting, Quicksort, Bubble Sort
