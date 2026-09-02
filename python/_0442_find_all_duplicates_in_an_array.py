# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Medium

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def set_up(self):
        self.sol = Solution()

    def test_example1(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])

    def test_example2(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1, 1, 2]), [1])

    def test_example3(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1]), [])

    def test_two_elements_first_is_duplicate(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1, 1]), [1])

    def test_all_duplicates(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1, 1, 2, 2]), [1, 2])

    def test_two_elements_one_duplicate(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([2, 2]), [2])

    def test_last_element_duplicate(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1, 2, 3, 4, 5, 5]), [5])

    def test_no_duplicates(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1, 2, 3, 4]), [])

    def test_duplicates_in_different_order(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([2, 2]), [2])
        self.assertEqual(self.sol.findDuplicates([3, 1, 2, 3]), [3])

    def test_duplicates_preserve_appearance_order(self):
        self.set_up()
        nums = [3, 3, 2, 1, 1, 2, 4, 4]
        self.assertEqual(self.sol.findDuplicates(nums), [3, 1, 2, 4])

    def test_repeated_pattern(self):
        self.set_up()
        self.assertEqual(self.sol.findDuplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_large_input(self):
        self.set_up()
        n = 100000
        nums = list(range(1, n // 2 + 1)) * 2
        expected = list(range(1, n // 2 + 1))
        self.assertEqual(self.sol.findDuplicates(nums), expected)

    def test_input_not_modified_for_uniqueness_check(self):
        self.set_up()
        nums = [2, 1, 2]
        self.assertEqual(self.sol.findDuplicates(nums), [2])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Sorting
