# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Medium

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_four_elements(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_with_zero(self):
        self.assertEqual(
            self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0]
        )

    def test_zero_at_start(self):
        self.assertEqual(self.solution.productExceptSelf([0, 2, 3]), [6, 0, 0])

    def test_zero_at_end(self):
        self.assertEqual(self.solution.productExceptSelf([2, 3, 0]), [0, 0, 6])

    def test_zero_in_middle(self):
        self.assertEqual(self.solution.productExceptSelf([2, 0, 3]), [0, 6, 0])

    def test_two_zeros(self):
        self.assertEqual(self.solution.productExceptSelf([0, 0, 3]), [0, 0, 0])

    def test_only_zeros(self):
        self.assertEqual(self.solution.productExceptSelf([0, 0]), [0, 0])

    def test_two_elements(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2]), [2, 1])

    def test_two_elements_negative(self):
        self.assertEqual(self.solution.productExceptSelf([-5, 3]), [3, -5])

    def test_negative_numbers(self):
        self.assertEqual(self.solution.productExceptSelf([-1, -2, -3]), [6, 3, 2])

    def test_all_negatives_even_count(self):
        self.assertEqual(
            self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6]
        )

    def test_mixed_positive_negative(self):
        self.assertEqual(
            self.solution.productExceptSelf([1, -2, 3, -4]), [24, -12, 8, -6]
        )

    def test_ones(self):
        self.assertEqual(self.solution.productExceptSelf([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_large_values(self):
        self.assertEqual(self.solution.productExceptSelf([10, 10, 10]), [100, 100, 100])

    def test_repeated_values(self):
        self.assertEqual(self.solution.productExceptSelf([2, 2, 2]), [4, 4, 4])

    def test_large_array_length(self):
        nums = [2] * 1000
        expected = [2**999] * 1000
        self.assertEqual(self.solution.productExceptSelf(nums), expected)

    def test_does_not_modify_input(self):
        nums = [1, 2, 3, 4]
        original = list(nums)
        self.solution.productExceptSelf(nums)
        self.assertEqual(nums, original)

    def test_returns_new_list(self):
        nums = [1, 2, 3]
        result = self.solution.productExceptSelf(nums)
        self.assertIsNot(result, nums)

    def test_two_same_elements(self):
        self.assertEqual(self.solution.productExceptSelf([7, 7]), [7, 7])

    def test_all_same_non_zero(self):
        self.assertEqual(
            self.solution.productExceptSelf([3, 3, 3, 3]), [27, 27, 27, 27]
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Prefix Sum
