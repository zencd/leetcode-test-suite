# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Easy

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        raise Exception("Not solved yet")


import unittest


class TestMerge(unittest.TestCase):
    def test_example1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        Solution().merge(nums1, 3, [2, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example2(self):
        nums1 = [1]
        Solution().merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

    def test_example3(self):
        nums1 = [0]
        Solution().merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

    def test_all_elements_from_nums1(self):
        nums1 = [5, 8, 10, 0, 0, 0]
        Solution().merge(nums1, 3, [1, 2, 3], 3)
        self.assertEqual(nums1, [1, 2, 3, 5, 8, 10])

    def test_all_elements_from_nums2(self):
        nums1 = [0, 0, 0, 0, 0]
        Solution().merge(nums1, 0, [1, 2, 3, 4, 5], 5)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])

    def test_identical_elements(self):
        nums1 = [2, 2, 0, 0]
        Solution().merge(nums1, 2, [2, 2], 2)
        self.assertEqual(nums1, [2, 2, 2, 2])

    def test_single_single(self):
        nums1 = [0, 0]
        Solution().merge(nums1, 1, [7], 1)
        self.assertEqual(nums1, [0, 7])

    def test_single_single_reversed(self):
        nums1 = [0, 0]
        Solution().merge(nums1, 1, [-9], 1)
        self.assertEqual(nums1, [-9, 0])

    def test_negative_numbers(self):
        nums1 = [-5, -2, -1, 0, 0, 0, 0]
        Solution().merge(nums1, 3, [-10, -3, 0, 4], 4)
        self.assertEqual(nums1, [-10, -5, -3, -2, -1, 0, 4])

    def test_large_values(self):
        nums1 = [1000000000, 0, 0]
        Solution().merge(nums1, 1, [-1000000000, 1000000000], 2)
        self.assertEqual(nums1, [-1000000000, 1000000000, 1000000000])

    def test_duplicates_interleaved(self):
        nums1 = [1, 3, 3, 5, 0, 0, 0]
        Solution().merge(nums1, 4, [2, 3, 6], 3)
        self.assertEqual(nums1, [1, 2, 3, 3, 3, 5, 6])

    def test_already_sorted_order(self):
        nums1 = [1, 2, 0, 0, 0]
        Solution().merge(nums1, 2, [3, 4, 5], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])

    def test_max_size_sorted(self):
        m = 100
        n = 100
        nums1 = list(range(1, m + 1)) + [0] * n
        nums2 = list(range(m + 1, m + n + 1))
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, list(range(1, m + n + 1)))

    def test_max_size_reversed(self):
        m = 100
        n = 100
        nums1 = [0] * m + [0] * n
        nums1[:m] = list(range(-m, 0))
        nums2 = list(range(0, n))
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, list(range(-m, n)))

    def test_zero_length_nums2(self):
        nums1 = [4, 4, 6, 7]
        Solution().merge(nums1, 4, [], 0)
        self.assertEqual(nums1, [4, 4, 6, 7])

    def test_zero_length_nums1(self):
        nums1 = [0] * 6
        Solution().merge(nums1, 0, [1, 1, 2, 3, 5, 8], 6)
        self.assertEqual(nums1, [1, 1, 2, 3, 5, 8])

    def test_in_place_modification(self):
        nums1 = [1, 0]
        solution = Solution()
        ref = id(nums1)
        solution.merge(nums1, 1, [7], 1)
        self.assertEqual(id(nums1), ref)
        self.assertEqual(nums1, [1, 7])

    def test_no_return_value(self):
        nums1 = [1, 0, 0]
        result = Solution().merge(nums1, 1, [2], 1)
        self.assertIsNone(result)

    def test_all_zeros(self):
        nums1 = [0, 0, 0]
        nums2 = [0]
        Solution().merge(nums1, 2, nums2, 1)
        self.assertEqual(nums1, [0, 0, 0])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Sorting
