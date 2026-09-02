# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/
# Medium

from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]),
            2,
        )

    def test_example2(self):
        self.assertEqual(
            self.s.fourSumCount([0], [0], [0], [0]),
            1,
        )

    def test_single_no_match(self):
        self.assertEqual(
            self.s.fourSumCount([1], [1], [1], [1]),
            0,
        )

    def test_single_negative_match(self):
        self.assertEqual(
            self.s.fourSumCount([-1], [1], [1], [-1]),
            1,
        )

    def test_all_zeros_two_each(self):
        self.assertEqual(
            self.s.fourSumCount([0, 0], [0, 0], [0, 0], [0, 0]),
            16,
        )

    def test_duplicates_counts_each_tuple(self):
        self.assertEqual(
            self.s.fourSumCount([1, 1], [-1, -1], [0], [0]),
            4,
        )

    def test_multiple_matches_large(self):
        self.assertEqual(
            self.s.fourSumCount([1, 2, 3], [-1, -2, -3], [0, 0, 0], [0, 0, 0]),
            27,
        )

    def test_big_values_cancel(self):
        v = 2**28
        self.assertEqual(
            self.s.fourSumCount([v], [-v], [v], [-v]),
            1,
        )

    def test_big_values_no_match(self):
        v = 2**28
        self.assertEqual(
            self.s.fourSumCount([v], [v], [v], [v]),
            0,
        )

    def test_negative_only_no_match(self):
        self.assertEqual(
            self.s.fourSumCount([-2, -3], [-4, -5], [-6, -7], [-8, -9]),
            0,
        )

    def test_mixed_signs_partial(self):
        nums1 = [1, 2]
        nums2 = [-3, 4]
        nums3 = [0, 1]
        nums4 = [2, -1]
        expected = 0
        for a in nums1:
            for b in nums2:
                for c in nums3:
                    for d in nums4:
                        if a + b + c + d == 0:
                            expected += 1
        self.assertEqual(self.s.fourSumCount(nums1, nums2, nums3, nums4), expected)
        self.assertGreaterEqual(expected, 1)

    def test_large_n_performance(self):
        arr = [0] * 200
        expected = 200**4
        self.assertEqual(self.s.fourSumCount(arr, arr, arr, arr), expected)

    def test_large_n_no_match(self):
        arr = [1] * 200
        self.assertEqual(self.s.fourSumCount(arr, arr, arr, arr), 0)

    def test_symmetric_arrays(self):
        arr = list(range(-5, 6))
        expected = 0
        for a in arr:
            for b in arr:
                for c in arr:
                    for d in arr:
                        if a + b + c + d == 0:
                            expected += 1
        self.assertEqual(self.s.fourSumCount(arr, arr, arr, arr), expected)

    def test_brute_force_cross_check_random(self):
        import random

        random.seed(42)
        for _ in range(20):
            n = random.randint(1, 6)
            nums1 = [random.randint(-10, 10) for _ in range(n)]
            nums2 = [random.randint(-10, 10) for _ in range(n)]
            nums3 = [random.randint(-10, 10) for _ in range(n)]
            nums4 = [random.randint(-10, 10) for _ in range(n)]
            expected = 0
            for a in nums1:
                for b in nums2:
                    for c in nums3:
                        for d in nums4:
                            if a + b + c + d == 0:
                                expected += 1
            self.assertEqual(self.s.fourSumCount(nums1, nums2, nums3, nums4), expected)

    def test_returns_int_type(self):
        result = self.s.fourSumCount([0], [0], [0], [0])
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table
