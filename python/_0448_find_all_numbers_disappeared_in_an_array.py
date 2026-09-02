# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Easy

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])

    def test_example2(self):
        self.assertEqual(self.sol.findDisappearedNumbers([1, 1]), [2])

    def test_single_element_present(self):
        self.assertEqual(self.sol.findDisappearedNumbers([1]), [])

    def test_single_element_value_outside(self):
        self.assertEqual(self.sol.findDisappearedNumbers([1]), [])

    def test_all_same(self):
        self.assertEqual(self.sol.findDisappearedNumbers([4, 4, 4, 4]), [1, 2, 3])

    def test_no_missing(self):
        self.assertEqual(self.sol.findDisappearedNumbers([1, 2, 3, 4]), [])

    def test_all_missing_except_first(self):
        self.assertEqual(self.sol.findDisappearedNumbers([1, 1, 1, 1]), [2, 3, 4])

    def test_largest_value(self):
        self.assertEqual(self.sol.findDisappearedNumbers([2, 2, 3, 4, 5]), [1])

    def test_only_largest_present(self):
        self.assertEqual(self.sol.findDisappearedNumbers([5, 5, 5, 5, 5]), [1, 2, 3, 4])

    def test_two_elements(self):
        self.assertEqual(self.sol.findDisappearedNumbers([2, 2]), [1])
        self.assertEqual(self.sol.findDisappearedNumbers([1, 1]), [2])
        self.assertEqual(self.sol.findDisappearedNumbers([1, 2]), [])

    def test_unordered(self):
        self.assertEqual(self.sol.findDisappearedNumbers([3, 1, 5, 4, 2]), [])

    def test_result_ordering(self):
        self.assertEqual(self.sol.findDisappearedNumbers([3, 3, 3, 3]), [1, 2, 4])

    def test_interleaved_missing(self):
        self.assertEqual(self.sol.findDisappearedNumbers([2, 1, 4, 4]), [3])

    def test_larger_case(self):
        nums = [1] * 5 + [1] * 5
        self.assertEqual(self.sol.findDisappearedNumbers(nums), [2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_large_boundary(self):
        n = 100000
        nums = list(range(1, n + 1))
        self.assertEqual(self.sol.findDisappearedNumbers(nums), [])
        nums = [1] * n
        expected = list(range(2, n + 1))
        self.assertEqual(self.sol.findDisappearedNumbers(nums), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table
