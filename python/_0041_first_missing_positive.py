# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/
# Hard

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.firstMissingPositive([1, 2, 0]), 3)

    def test_example2(self):
        self.assertEqual(self.sol.firstMissingPositive([3, 4, -1, 1]), 2)

    def test_example3(self):
        self.assertEqual(self.sol.firstMissingPositive([7, 8, 9, 11, 12]), 1)

    def test_single_one(self):
        self.assertEqual(self.sol.firstMissingPositive([1]), 2)

    def test_single_two(self):
        self.assertEqual(self.sol.firstMissingPositive([2]), 1)

    def test_single_negative(self):
        self.assertEqual(self.sol.firstMissingPositive([-5]), 1)

    def test_single_zero(self):
        self.assertEqual(self.sol.firstMissingPositive([0]), 1)

    def test_consecutive_from_one(self):
        self.assertEqual(self.sol.firstMissingPositive([1, 2, 3, 4, 5]), 6)

    def test_gaps(self):
        self.assertEqual(self.sol.firstMissingPositive([1, 3, 5, 7]), 2)

    def test_with_duplicates(self):
        self.assertEqual(self.sol.firstMissingPositive([1, 1, 1, 1]), 2)

    def test_all_zero(self):
        self.assertEqual(self.sol.firstMissingPositive([0, 0, 0]), 1)

    def test_all_negative(self):
        self.assertEqual(self.sol.firstMissingPositive([-1, -2, -3]), 1)

    def test_mixed_negative_and_positive(self):
        self.assertEqual(self.sol.firstMissingPositive([-1, -2, -3, 4, 5, 6]), 1)

    def test_mixed_missing_inside(self):
        self.assertEqual(self.sol.firstMissingPositive([-1, 2, 4, 3]), 1)

    def test_big_numbers(self):
        nums = [2147483647, -2147483648, 0]
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_big_numbers_present(self):
        nums = [1, 2, 3, 2147483647, 0]
        self.assertEqual(self.sol.firstMissingPositive(nums), 4)

    def test_duplicate_of_out_of_range(self):
        nums = [1, 2, 2, 2, 2]
        self.assertEqual(self.sol.firstMissingPositive(nums), 3)

    def test_large_positive_only(self):
        nums = [10**5] * 5
        self.assertEqual(self.sol.firstMissingPositive(nums), 1)

    def test_long_consecutive_then_gap(self):
        nums = list(range(1, 101)) + [200]
        self.assertEqual(self.sol.firstMissingPositive(nums), 101)

    def test_shuffled_full_range_plus_extra(self):
        nums = [50, 1, 100, 99, 1, 3, 4, 5, 2, 10]
        self.assertEqual(self.sol.firstMissingPositive(nums), 6)

    def test_reversed_range(self):
        nums = list(range(10, 0, -1))
        self.assertEqual(self.sol.firstMissingPositive(nums), 11)

    def test_input_mutation_allowed(self):
        nums = [1, 2, 3]
        self.sol.firstMissingPositive(nums)
        self.assertEqual(len(nums), 3)

    def test_two_elements_with_one_missing(self):
        self.assertEqual(self.sol.firstMissingPositive([2, 1]), 3)

    def test_two_elements_zero_and_two(self):
        self.assertEqual(self.sol.firstMissingPositive([2, 0]), 1)

    def test_many_duplicates_with_range(self):
        self.assertEqual(self.sol.firstMissingPositive([1, 2, 2, 3, 3, 3, 5, 6]), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table
