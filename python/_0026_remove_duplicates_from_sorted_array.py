# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Easy

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_single_element(self):
        nums = [5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])

    def test_all_same(self):
        nums = [7, 7, 7, 7]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [7])

    def test_all_unique(self):
        nums = [1, 2, 3, 4, 5]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        nums = [-5, -3, -3, 0, 0, 0, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-5, -3, 0, 2])

    def test_mixed_negative_and_positive(self):
        nums = [-100, -100, -50, 0, 50, 50, 100]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-100, -50, 0, 50, 100])

    def test_two_elements_same(self):
        nums = [3, 3]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [3])

    def test_two_elements_different(self):
        nums = [3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [3, 4])

    def test_duplicates_at_ends(self):
        nums = [1, 1, 2, 3, 4, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])

    def test_constraint_boundaries(self):
        nums = [-100, -100, 100, 100]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [-100, 100])

    def test_large_array(self):
        nums = [i % 10 for i in range(1000)]
        nums.sort()
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 10)
        self.assertEqual(nums[:k], list(range(10)))

    def test_original_length_preserved(self):
        nums = [1, 1, 2]
        original_len = len(nums)
        self.solution.removeDuplicates(nums)
        self.assertEqual(len(nums), original_len)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers
