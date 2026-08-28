# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Hard

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def f(self, a, b):
        return self.s.findMedianSortedArrays(a, b)

    def test_examples(self):
        self.assertAlmostEqual(self.f([1, 3], [2]), 2.0)
        self.assertAlmostEqual(self.f([1, 2], [3, 4]), 2.5)

    def test_single_elements(self):
        self.assertAlmostEqual(self.f([1], [2]), 1.5)
        self.assertAlmostEqual(self.f([2], [1]), 1.5)
        self.assertAlmostEqual(self.f([5], []), 5.0)
        self.assertAlmostEqual(self.f([], [5]), 5.0)
        self.assertAlmostEqual(self.f([7], [7]), 7.0)
        self.assertAlmostEqual(self.f([], [1, 3]), 2.0)
        self.assertAlmostEqual(self.f([1, 3], []), 2.0)

    def test_identical_arrays(self):
        self.assertAlmostEqual(self.f([1, 2, 3], [1, 2, 3]), 2.0)
        self.assertAlmostEqual(self.f([1, 1, 1, 1], [1, 1, 1]), 1.0)

    def test_disjoint_ranges(self):
        self.assertAlmostEqual(self.f([1, 2], [5, 6]), 3.5)
        self.assertAlmostEqual(self.f([5, 6], [1, 2]), 3.5)
        self.assertAlmostEqual(self.f([1], [1000000]), 500000.5)

    def test_duplicates_and_negatives(self):
        self.assertAlmostEqual(self.f([-1, -1, -1], [-2]), -1.0)
        self.assertAlmostEqual(self.f([-5, -4], [-1, 0, 2]), -1.0)
        self.assertAlmostEqual(self.f([-1000000, -1000000], [1000000]), -1000000.0)

    def test_odd_and_even_totals(self):
        self.assertAlmostEqual(self.f([1, 3, 5], [2, 4, 6, 7]), 4.0)
        self.assertAlmostEqual(self.f([1, 4, 7], [2, 3]), 3.0)
        self.assertAlmostEqual(self.f([1, 2, 3, 4, 5], [6, 7, 8]), 4.5)

    def test_order_independent(self):
        for a, b in (
            ([1, 3], [2]),
            ([1, 2], [3, 4]),
            ([], [9, 9]),
            ([1], []),
            ([1, 2, 3], [4, 5, 6, 7]),
            ([6, 7], [1, 2, 3, 4, 5, 6, 8]),
        ):
            self.assertAlmostEqual(self.f(a, b), self.f(b, a))

    def test_large_arrays(self):
        import random

        random.seed(42)
        a = sorted(random.randint(-(10**6), 10**6) for _ in range(1000))
        b = sorted(random.randint(-(10**6), 10**6) for _ in range(1000))
        expected = sorted(a + b)
        total = len(expected)
        if total % 2 == 1:
            want = float(expected[total // 2])
        else:
            want = (expected[total // 2 - 1] + expected[total // 2]) / 2.0
        self.assertAlmostEqual(self.f(a, b), want)

    def test_return_type_is_float(self):
        self.assertIsInstance(self.f([1], [2]), float)
        self.assertIsInstance(self.f([1], []), float)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Divide and Conquer
