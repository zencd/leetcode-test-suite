# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Medium

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.findDuplicate([3, 1, 3, 4, 2]), 3)

    def test_example3(self):
        self.assertEqual(self.sol.findDuplicate([3, 3, 3, 3, 3]), 3)

    def test_minimal_array(self):
        self.assertEqual(self.sol.findDuplicate([1, 1]), 1)

    def test_duplicate_at_start(self):
        self.assertEqual(self.sol.findDuplicate([2, 2, 3, 4, 1]), 2)

    def test_duplicate_at_end(self):
        self.assertEqual(self.sol.findDuplicate([1, 2, 3, 4, 4]), 4)

    def test_consecutive_duplicates(self):
        self.assertEqual(self.sol.findDuplicate([1, 1, 2, 3, 4]), 1)

    def test_duplicate_repeated_many_times(self):
        self.assertEqual(self.sol.findDuplicate([4, 1, 4, 2, 4, 3, 4]), 4)

    def test_all_same_except_one_value(self):
        self.assertEqual(self.sol.findDuplicate([5, 5, 5, 5, 5, 5]), 5)

    def test_identity_with_one_swap(self):
        self.assertEqual(self.sol.findDuplicate([1, 3, 3, 4, 5, 2]), 3)

    def test_reversed_identity_with_duplicate(self):
        self.assertEqual(self.sol.findDuplicate([5, 4, 3, 2, 1, 5]), 5)

    def test_duplicate_is_n(self):
        self.assertEqual(self.sol.findDuplicate([1, 2, 3, 4, 6, 6, 6]), 6)

    def test_duplicate_is_lowest_value(self):
        self.assertEqual(self.sol.findDuplicate([1, 2, 1, 3, 4, 5]), 1)

    def test_large_array(self):
        n = 1000
        nums = list(range(1, n + 1))
        nums[-1] = 999
        self.assertEqual(self.sol.findDuplicate(nums), 999)

    def test_original_array_not_modified(self):
        nums = [1, 3, 4, 2, 2]
        expected = nums.copy()
        self.sol.findDuplicate(nums)
        self.assertEqual(nums, expected)

    def test_returns_int(self):
        result = self.sol.findDuplicate([1, 3, 4, 2, 2])
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Binary Search, Bit Manipulation, Pigeonhole Principle, Floyd's Cycle Finding Algorithm
