# 373. Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Medium

from typing import List
import heapq
import unittest


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        raise Exception("Not solved yet")


def _reference(nums1, nums2, k):
    pairs = sorted(
        ((a, b) for a in nums1 for b in nums2), key=lambda p: (p[0] + p[1], p[0], p[1])
    )
    return [[a, b] for a, b in pairs[:k]]


def _same_multiset(actual, expected):
    key = lambda pairs: sorted((a + b, a, b) for a, b in pairs)
    return key(actual) == key(expected)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3),
            [[1, 2], [1, 4], [1, 6]],
        )

    def test_example2(self):
        self.assertEqual(
            self.sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2),
            [[1, 1], [1, 1]],
        )

    def test_k_larger_than_available_pairs(self):
        nums1, nums2 = [1, 2], [3, 4]
        res = self.sol.kSmallestPairs(nums1, nums2, 100)
        self.assertEqual(len(res), 4)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 4)))

    def test_k_equals_total_pairs(self):
        nums1, nums2 = [1, 7, 11], [2, 4, 6]
        res = self.sol.kSmallestPairs(nums1, nums2, 9)
        self.assertEqual(len(res), 9)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 9)))

    def test_single_elements(self):
        self.assertEqual(self.sol.kSmallestPairs([5], [-3], 1), [[5, -3]])

    def test_negative_numbers(self):
        nums1, nums2 = [-5, -2, 3], [-10, 0, 10]
        res = self.sol.kSmallestPairs(nums1, nums2, 4)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 4)))

    def test_all_negative_numbers(self):
        nums1, nums2 = [-9, -8], [-7, -6, -5]
        res = self.sol.kSmallestPairs(nums1, nums2, 5)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 5)))

    def test_duplicates_in_both_arrays(self):
        nums1, nums2 = [1, 1, 1], [2, 2, 2]
        res = self.sol.kSmallestPairs(nums1, nums2, 6)
        self.assertEqual(len(res), 6)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 6)))

    def test_k_one(self):
        self.assertEqual(
            self.sol.kSmallestPairs([1, 2, 3], [4, 5, 6], 1),
            [[1, 4]],
        )

    def test_k_smaller_than_first_row(self):
        nums1, nums2 = [1, 2, 3, 4], [10, 20]
        res = self.sol.kSmallestPairs(nums1, nums2, 3)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 3)))

    def test_zero_values(self):
        nums1, nums2 = [0, 0], [0, 1]
        res = self.sol.kSmallestPairs(nums1, nums2, 3)
        self.assertEqual(res, [[0, 0], [0, 0], [0, 1]])

    def test_large_values(self):
        nums1, nums2 = [10**9, 2 * 10**9], [10**9, 3 * 10**9]
        res = self.sol.kSmallestPairs(nums1, nums2, 3)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 3)))

    def test_first_array_longer(self):
        nums1, nums2 = list(range(1, 12)), [5, 6]
        res = self.sol.kSmallestPairs(nums1, nums2, 7)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 7)))

    def test_second_array_longer(self):
        nums1, nums2 = [1, 2], list(range(1, 12))
        res = self.sol.kSmallestPairs(nums1, nums2, 5)
        self.assertTrue(_same_multiset(res, _reference(nums1, nums2, 5)))

    def test_randomized_cross_check(self):
        import random

        random.seed(42)
        for _ in range(25):
            n1 = random.randint(1, 8)
            n2 = random.randint(1, 8)
            nums1 = sorted(random.randint(-20, 20) for _ in range(n1))
            nums2 = sorted(random.randint(-20, 20) for _ in range(n2))
            k = random.randint(1, min(30, n1 * n2))
            res = self.sol.kSmallestPairs(nums1, nums2, k)
            self.assertEqual(len(res), k)
            self.assertTrue(_same_multiset(res, _reference(nums1, nums2, k)))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Heap (Priority Queue)
