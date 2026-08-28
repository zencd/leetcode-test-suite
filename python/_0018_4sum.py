# 18. 4Sum
# https://leetcode.com/problems/4sum/
# Medium

from typing import List
import unittest


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        raise Exception("Not solved yet")


class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(
            sorted(self.sol.fourSum([1, 0, -1, 0, -2, 2], 0)),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        )

    def test_example_2(self):
        self.assertEqual(self.sol.fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])

    def test_no_solution(self):
        self.assertEqual(self.sol.fourSum([1, 2, 3, 4], 100), [])

    def test_single_quadruplet_only(self):
        self.assertEqual(self.sol.fourSum([1, 2, 3, 4], 10), [[1, 2, 3, 4]])

    def test_all_zeros(self):
        self.assertEqual(self.sol.fourSum([0] * 10, 0), [[0, 0, 0, 0]])

    def test_exactly_four_elements_match(self):
        self.assertEqual(self.sol.fourSum([2, -2, -1, 1], 0), [[-2, -1, 1, 2]])

    def test_exactly_four_elements_no_match(self):
        self.assertEqual(self.sol.fourSum([1, 1, 1, 1], 5), [])

    def test_more_than_four_elements_all_same(self):
        self.assertEqual(self.sol.fourSum([1] * 6, 4), [[1, 1, 1, 1]])

    def test_all_sevens(self):
        self.assertEqual(self.sol.fourSum([1] * 7, 4), [[1, 1, 1, 1]])

    def test_negative_numbers(self):
        result = sorted(self.sol.fourSum([-3, -2, -1, 0, 1, 2, 3], -4))
        self.assertEqual(result, [[-3, -2, -1, 2], [-3, -2, 0, 1]])

    def test_positive_and_negative_large(self):
        self.assertEqual(
            sorted(self.sol.fourSum([-10, -5, 0, 5, 10], 0)),
            [[-10, -5, 5, 10]],
        )

    def test_zero_target_with_negatives(self):
        result = sorted(self.sol.fourSum([0, 0, 0, 0, 1, -1], 0))
        self.assertEqual(result, [[-1, 0, 0, 1], [0, 0, 0, 0]])

    def test_single_element(self):
        self.assertEqual(self.sol.fourSum([1], 4), [])

    def test_two_elements(self):
        self.assertEqual(self.sol.fourSum([1, 2], 3), [])

    def test_three_elements(self):
        self.assertEqual(self.sol.fourSum([1, 2, 3], 6), [])

    def test_unsorted_input(self):
        self.assertEqual(
            sorted(self.sol.fourSum([2, -2, 1, 0, 0, -1, 1], 0)),
            [
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-2, 0, 1, 1],
                [-1, 0, 0, 1],
            ],
        )

    def test_result_is_sorted_and_unique(self):
        result = self.sol.fourSum([0] * 10, 0)
        self.assertEqual(result, [[0, 0, 0, 0]])

    def test_large_values(self):
        self.assertEqual(
            sorted(self.sol.fourSum([10**9, -(10**9), 5, -5], 0)),
            [[-(10**9), -5, 5, 10**9]],
        )

    def test_large_values_no_match(self):
        self.assertEqual(self.sol.fourSum([10**9] * 4, 1), [])

    def test_mixed_duplicates(self):
        result = sorted(self.sol.fourSum([1, 1, 1, 2, 3, 3], 6))
        self.assertIn([1, 1, 1, 3], result)
        self.assertEqual(result, sorted(self.sol.fourSum([1, 1, 1, 2, 3, 3], 6)))

    def test_negative_target(self):
        self.assertEqual(
            sorted(self.sol.fourSum([-1, -1, -1, -1, -2], -5)),
            [[-2, -1, -1, -1]],
        )

    def test_all_negative(self):
        self.assertEqual(
            sorted(self.sol.fourSum([-4, -3, -2, -1], -10)),
            [[-4, -3, -2, -1]],
        )

    def test_two_pairs(self):
        self.assertEqual(
            sorted(self.sol.fourSum([1, 1, 2, 2], 6)),
            [[1, 1, 2, 2]],
        )

    def test_target_smaller_than_min_sum(self):
        self.assertEqual(self.sol.fourSum([1, 2, 3, 4, 5], 0), [])

    def test_target_larger_than_max_sum(self):
        self.assertEqual(self.sol.fourSum([-1, -2, -3, -4], 100), [])

    def test_duplicates_of_two_values(self):
        self.assertEqual(self.sol.fourSum([1, 1, 2, 2, 1, 2], 6), [[1, 1, 2, 2]])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Sorting
