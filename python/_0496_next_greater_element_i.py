# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/
# Easy

from typing import List
import unittest


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]),
            [-1, 3, -1],
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.nextGreaterElement([2, 4], [1, 2, 3, 4]),
            [3, -1],
        )

    def test_single_element_with_greater(self):
        self.assertEqual(
            self.solution.nextGreaterElement([1], [1, 2]),
            [2],
        )

    def test_single_element_no_greater(self):
        self.assertEqual(
            self.solution.nextGreaterElement([1], [2, 1]),
            [-1],
        )

    def test_all_no_greater(self):
        self.assertEqual(
            self.solution.nextGreaterElement([3, 2, 1], [3, 2, 1]),
            [-1, -1, -1],
        )

    def test_all_have_greater(self):
        self.assertEqual(
            self.solution.nextGreaterElement([1, 2, 3], [1, 2, 3, 4]),
            [2, 3, 4],
        )

    def test_first_element_of_nums1(self):
        self.assertEqual(
            self.solution.nextGreaterElement([1], [1, 5, 2]),
            [5],
        )

    def test_last_element_of_nums2(self):
        self.assertEqual(
            self.solution.nextGreaterElement([9], [1, 2, 9]),
            [-1],
        )

    def test_first_greater_not_final(self):
        self.assertEqual(
            self.solution.nextGreaterElement([1], [1, 3, 2]),
            [3],
        )

    def test_query_order_preserved(self):
        self.assertEqual(
            self.solution.nextGreaterElement([2, 4, 1], [1, 3, 4, 2]),
            [-1, -1, 3],
        )

    def test_nums1_equals_nums2(self):
        self.assertEqual(
            self.solution.nextGreaterElement([1, 2, 3], [1, 2, 3]),
            [2, 3, -1],
        )

    def test_max_constraints(self):
        nums2 = list(range(1000))
        nums1 = list(reversed(range(1000)))
        expected = [n + 1 if n < 999 else -1 for n in nums1]
        self.assertEqual(
            self.solution.nextGreaterElement(nums1, nums2),
            expected,
        )

    def test_result_length_matches_nums1(self):
        nums1 = [5, 1, 4, 2]
        nums2 = [3, 1, 4, 1, 5, 9, 2, 6]
        result = self.solution.nextGreaterElement(nums1, nums2)
        self.assertEqual(len(result), len(nums1))

    def test_zero_value(self):
        self.assertEqual(
            self.solution.nextGreaterElement([0], [0, 7, 3]),
            [7],
        )

    def test_max_value_no_greater(self):
        self.assertEqual(
            self.solution.nextGreaterElement([10000], [1, 2, 10000]),
            [-1],
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Stack, Monotonic Stack
