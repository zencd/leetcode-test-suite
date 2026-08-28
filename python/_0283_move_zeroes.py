# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Easy

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def move(self, nums):
        self.assertIsNone(self.solution.moveZeroes(nums))
        return nums

    def test_example1(self):
        nums = [0, 1, 0, 3, 12]
        self.assertEqual(self.move(nums), [1, 3, 12, 0, 0])

    def test_example2(self):
        nums = [0]
        self.assertEqual(self.move(nums), [0])

    def test_no_zeros(self):
        nums = [1, 2, 3]
        self.assertEqual(self.move(nums), [1, 2, 3])

    def test_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.move(nums), [0, 0, 0])

    def test_single_nonzero(self):
        nums = [7]
        self.assertEqual(self.move(nums), [7])

    def test_two_elements_zero_first(self):
        nums = [0, 5]
        self.assertEqual(self.move(nums), [5, 0])

    def test_two_elements_zero_last(self):
        nums = [5, 0]
        self.assertEqual(self.move(nums), [5, 0])

    def test_zero_at_front(self):
        nums = [0, 1, 2, 3]
        self.assertEqual(self.move(nums), [1, 2, 3, 0])

    def test_zero_at_back(self):
        nums = [1, 2, 3, 0]
        self.assertEqual(self.move(nums), [1, 2, 3, 0])

    def test_zeros_at_both_ends(self):
        nums = [0, 4, 5, 0]
        self.assertEqual(self.move(nums), [4, 5, 0, 0])

    def test_negative_values(self):
        nums = [-1, 0, -2, 0, -3]
        self.assertEqual(self.move(nums), [-1, -2, -3, 0, 0])

    def test_mixed_positive_negative_and_zero(self):
        nums = [-2147483648, 0, 2147483647, 0, 0, -5]
        self.assertEqual(self.move(nums), [-2147483648, 2147483647, -5, 0, 0, 0])

    def test_duplicate_nonzeros(self):
        nums = [3, 0, 3, 0, 3]
        self.assertEqual(self.move(nums), [3, 3, 3, 0, 0])

    def test_zero_between_all_elements(self):
        nums = [1, 0, 2, 0, 3, 0, 4, 0, 5]
        self.assertEqual(self.move(nums), [1, 2, 3, 4, 5, 0, 0, 0, 0])

    def test_consecutive_nonzero_middle(self):
        nums = [11, 12, 13, 0, 0, 14, 0, 15]
        self.assertEqual(self.move(nums), [11, 12, 13, 14, 15, 0, 0, 0])

    def test_returns_none(self):
        nums = [0, 1, 0, 3]
        result = self.solution.moveZeroes(nums)
        self.assertIsNone(result)

    def test_modifies_in_place(self):
        nums = [0, 1, 0, 3, 12]
        original_id = id(nums)
        self.solution.moveZeroes(nums)
        self.assertEqual(original_id, id(nums))
        self.assertEqual(len(nums), 5)

    def test_large_array(self):
        nums = [0, 2, 0, 4, 0, 6, 0, 8, 0, 10] * 1000
        expected = [2, 4, 6, 8, 10] * 1000 + [0] * 5000
        self.assertEqual(self.move(nums), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers
