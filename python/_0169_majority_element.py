# 169. Majority Element
# https://leetcode.com/problems/majority-element/
# Easy

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.majorityElement([3, 2, 3]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_single_element(self):
        self.assertEqual(self.solution.majorityElement([42]), 42)

    def test_all_same_elements(self):
        self.assertEqual(self.solution.majorityElement([7, 7, 7, 7]), 7)

    def test_two_elements_majority(self):
        self.assertEqual(self.solution.majorityElement([1, 2, 2]), 2)

    def test_negative_numbers(self):
        self.assertEqual(self.solution.majorityElement([-1, -1, -1, 0, 5]), -1)

    def test_mixed_negative_and_positive(self):
        self.assertEqual(self.solution.majorityElement([-5, 3, -5, 8, -5]), -5)

    def test_zero_majority(self):
        self.assertEqual(self.solution.majorityElement([1, 0, 0, 2, 0]), 0)

    def test_majority_at_start(self):
        self.assertEqual(self.solution.majorityElement([9, 9, 9, 1, 2]), 9)

    def test_majority_at_end(self):
        self.assertEqual(self.solution.majorityElement([1, 2, 9, 9, 9]), 9)

    def test_large_values(self):
        self.assertEqual(
            self.solution.majorityElement([10**9, -(10**9), 10**9, 0]), 10**9
        )

    def test_alternating_pattern(self):
        self.assertEqual(self.solution.majorityElement([5, 1, 5, 4, 5, 3, 5]), 5)

    def test_two_majority_candidates(self):
        self.assertEqual(self.solution.majorityElement([1, 1, 2, 1, 2]), 1)

    def test_even_length(self):
        self.assertEqual(self.solution.majorityElement([4, 4, 5, 5, 4, 4]), 4)

    def test_odd_length(self):
        self.assertEqual(self.solution.majorityElement([4, 5, 4, 5, 4]), 4)

    def test_minimum_majority_count(self):
        nums = [3] * 3 + [1, 2, 4]
        self.assertEqual(self.solution.majorityElement(nums), 3)

    def test_first_minority_isolation(self):
        self.assertEqual(self.solution.majorityElement([1, 2, 3, 3, 3, 3, 3]), 3)

    def test_many_small_numbers(self):
        nums = [1, 2, 3, 4, 2, 2, 2]
        self.assertEqual(self.solution.majorityElement(nums), 2)

    def test_duplicate_pairs(self):
        self.assertEqual(self.solution.majorityElement([1, 1, 2, 2, 3, 3, 3]), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Divide and Conquer, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
