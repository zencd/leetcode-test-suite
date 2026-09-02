# 456. 132 Pattern
# https://leetcode.com/problems/132-pattern/
# Medium

from typing import List
import unittest


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_examples(self):
        self.assertEqual(self.s.find132pattern([1, 2, 3, 4]), False)
        self.assertEqual(self.s.find132pattern([3, 1, 4, 2]), True)
        self.assertEqual(self.s.find132pattern([-1, 3, 2, 0]), True)

    def test_too_short(self):
        self.assertEqual(self.s.find132pattern([]), False)
        self.assertEqual(self.s.find132pattern([1]), False)
        self.assertEqual(self.s.find132pattern([1, 2]), False)

    def test_negative_numbers(self):
        self.assertEqual(self.s.find132pattern([-2, 2, 3, 1]), True)
        self.assertEqual(self.s.find132pattern([-1, -2, -3]), False)
        self.assertEqual(self.s.find132pattern([-3, -1, -2]), True)

    def test_duplicates(self):
        self.assertEqual(self.s.find132pattern([1, 1, 1]), False)
        self.assertEqual(self.s.find132pattern([1, 2, 1, 2]), False)
        self.assertEqual(self.s.find132pattern([2, 1, 2, 1]), False)
        self.assertEqual(self.s.find132pattern([2, 2, 1, 2]), False)
        self.assertEqual(self.s.find132pattern([1, 3, 2, 2]), True)

    def test_all_equal(self):
        self.assertEqual(self.s.find132pattern([5, 5, 5, 5]), False)

    def test_sorted(self):
        self.assertEqual(self.s.find132pattern([1, 2, 3, 4, 5]), False)
        self.assertEqual(self.s.find132pattern([5, 4, 3, 2, 1]), False)

    def test_simple_true(self):
        self.assertEqual(self.s.find132pattern([1, 3, 2]), True)

    def test_large_values(self):
        self.assertEqual(self.s.find132pattern([-1000000000, 1000000000, 0]), True)
        self.assertEqual(self.s.find132pattern([1000000000, -1000000000, 1000000000]), False)

    def test_large_input(self):
        self.assertEqual(self.s.find132pattern(list(range(200000))), False)
        arr = list(range(100000)) + [200000] + list(range(99999, 0, -1))
        self.assertEqual(self.s.find132pattern(arr), True)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Stack, Monotonic Stack, Ordered Set
