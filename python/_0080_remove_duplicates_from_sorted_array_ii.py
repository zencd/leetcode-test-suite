# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Medium

import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


class TestRemoveDuplicates(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 1, 2, 2, 3])

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 7)
        self.assertEqual(nums[:k], [0, 0, 1, 1, 2, 3, 3])

    def test_empty(self):
        nums = []
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_single(self):
        nums = [5]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])

    def test_two_same(self):
        nums = [7, 7]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [7, 7])

    def test_two_different(self):
        nums = [1, 2]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_all_same(self):
        nums = [4, 4, 4, 4, 4]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [4, 4])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

    def test_all_allowed_twice(self):
        nums = [1, 1, 2, 2, 3, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 6)
        self.assertEqual(nums[:k], [1, 1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        nums = [-3, -3, -3, -2, -2, -2, -1]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-3, -3, -2, -2, -1])

    def test_mixed_negative_and_zero(self):
        nums = [-1, -1, 0, 0, 0, 1]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-1, -1, 0, 0, 1])

    def test_triple_run_in_middle(self):
        nums = [1, 2, 2, 2, 2, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 2, 3])

    def test_single_run_of_many(self):
        nums = [9] * 10 + [10] * 10
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [9, 9, 10, 10])

    def test_large_values(self):
        nums = [-10000, 10000, 10000, 10000]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [-10000, 10000, 10000])

    def test_three_run_at_end(self):
        nums = [1, 2, 3, 3, 3, 3, 3]
        k = Solution().removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 3])

    def test_in_place_mutation(self):
        nums = [1, 1, 1, 2, 2, 3]
        original = nums
        k = Solution().removeDuplicates(nums)
        self.assertIs(nums, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers
