# 229. Majority Element II
# https://leetcode.com/problems/majority-element-ii/
# Medium

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.majorityElement([3, 2, 3]), [3])

    def test_example2(self):
        self.assertEqual(self.sol.majorityElement([1]), [1])

    def test_example3(self):
        self.assertEqual(sorted(self.sol.majorityElement([1, 2])), [1, 2])

    def test_single_element(self):
        self.assertEqual(self.sol.majorityElement([42]), [42])

    def test_all_same(self):
        self.assertEqual(self.sol.majorityElement([7, 7, 7, 7]), [7])

    def test_no_majority(self):
        self.assertEqual(self.sol.majorityElement([1, 2, 3]), [])

    def test_two_majorities(self):
        self.assertEqual(sorted(self.sol.majorityElement([2, 2, 1, 1])), [1, 2])

    def test_two_majorities_example(self):
        self.assertEqual(
            sorted(self.sol.majorityElement([1, 1, 1, 3, 3, 3, 2, 2, 2])), []
        )

    def test_two_majorities_actual(self):
        self.assertEqual(
            sorted(self.sol.majorityElement([1, 1, 1, 1, 3, 3, 3, 3, 2, 2, 2])), [1, 3]
        )

    def test_one_majority_mixed(self):
        self.assertEqual(self.sol.majorityElement([1, 1, 1, 2, 3, 4]), [1])

    def test_negative_numbers(self):
        self.assertEqual(self.sol.majorityElement([-1, -1, -2, -3]), [-1])

    def test_mixed_signs(self):
        self.assertEqual(self.sol.majorityElement([-5, -5, -5, 3, 3, 4, 4]), [-5])

    def test_duplicate_pair_boundary(self):
        self.assertEqual(self.sol.majorityElement([1, 2, 2]), [2])

    def test_all_distinct(self):
        self.assertEqual(self.sol.majorityElement([1, 2, 3, 4, 5]), [])

    def test_even_boundary_not_majority(self):
        self.assertEqual(
            self.sol.majorityElement([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), []
        )

    def test_large_values(self):
        self.assertEqual(
            sorted(self.sol.majorityElement([10**9, 10**9, 10**9, -(10**9), -(10**9)])),
            [-(10**9), 10**9],
        )

    def test_zero_values(self):
        self.assertEqual(self.sol.majorityElement([0, 0, 0, 1, 2, 3]), [0])

    def test_zero_with_negative(self):
        self.assertEqual(sorted(self.sol.majorityElement([0, 0, -1, -1])), [-1, 0])

    def test_large_input_single_dominant(self):
        nums = [1] * 100 + [2] * 40 + [3] * 40
        self.assertEqual(self.sol.majorityElement(nums), [1])

    def test_large_input_two_dominant(self):
        nums = [1] * 70 + [2] * 70 + [3] * 60
        self.assertEqual(sorted(self.sol.majorityElement(nums)), [1, 2])

    def test_input_not_mutated(self):
        nums = [3, 2, 3]
        self.sol.majorityElement(nums)
        self.assertEqual(nums, [3, 2, 3])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
