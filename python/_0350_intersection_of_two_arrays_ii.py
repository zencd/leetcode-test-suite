# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Easy

from collections import Counter
from typing import List
import unittest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def _assert_same_multiset(self, expected, actual):
        self.assertEqual(sorted(expected), sorted(actual))

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self._assert_same_multiset(
            [2, 2], self.solution.intersect([1, 2, 2, 1], [2, 2])
        )

    def test_example_2(self):
        self._assert_same_multiset(
            [4, 9], self.solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])
        )

    def test_no_common_elements(self):
        self.assertEqual([], self.solution.intersect([1, 2, 3], [4, 5, 6]))

    def test_single_elements(self):
        self.assertEqual([1], self.solution.intersect([1], [1]))
        self.assertEqual([], self.solution.intersect([1], [2]))

    def test_all_identical(self):
        self.assertEqual([7, 7, 7], self.solution.intersect([7, 7, 7], [7, 7, 7]))

    def test_duplicates_counted_in_both(self):
        actual = self.solution.intersect([2, 2, 2, 3, 3], [2, 3, 3, 3])
        self._assert_same_multiset([2, 3, 3], actual)

    def test_smaller_array_first_and_second(self):
        self._assert_same_multiset(
            [1, 1], self.solution.intersect([1, 1, 9], [1, 1, 1])
        )
        self._assert_same_multiset(
            [1, 1], self.solution.intersect([1, 1, 1], [1, 1, 9])
        )

    def test_subset(self):
        actual = self.solution.intersect([1, 2, 3, 4], [2])
        self._assert_same_multiset([2], actual)
        actual = self.solution.intersect([2], [1, 2, 3, 4])
        self._assert_same_multiset([2], actual)

    def test_zero_values(self):
        self._assert_same_multiset([0, 0], self.solution.intersect([0, 0], [0, 0, 0]))

    def test_only_zeros(self):
        self.assertEqual([0], self.solution.intersect([0], [0]))
        self.assertEqual([], self.solution.intersect([0], [1]))

    def test_max_constraint_values(self):
        self.assertEqual([1000], self.solution.intersect([1000], [1000]))
        self._assert_same_multiset(
            [0, 1000], self.solution.intersect([0, 1000], [1000, 0])
        )

    def test_large_arrays(self):
        nums1 = list(range(1000))
        nums2 = list(range(500, 1500))
        self._assert_same_multiset(
            list(range(500, 1000)), self.solution.intersect(nums1, nums2)
        )

    def test_identical_large_arrays(self):
        nums = [1, 2, 3] * 333
        self._assert_same_multiset(
            nums, self.solution.intersect(nums, list(reversed(nums)))
        )

    def test_does_not_mutate_inputs(self):
        nums1 = [1, 2, 2]
        nums2 = [2, 2, 3]
        copy1 = list(nums1)
        copy2 = list(nums2)
        self.solution.intersect(nums1, nums2)
        self.assertEqual(copy1, nums1)
        self.assertEqual(copy2, nums2)

    def test_result_length_bounded_by_smaller(self):
        result = self.solution.intersect([1, 1, 1, 1], [1, 1])
        self.assertEqual(2, len(result))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Two Pointers, Binary Search, Sorting
