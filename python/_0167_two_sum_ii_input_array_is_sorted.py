# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Medium

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_example2(self):
        self.assertEqual(self.sol.twoSum([2, 3, 4], 6), [1, 3])

    def test_example3(self):
        self.assertEqual(self.sol.twoSum([-1, 0], -1), [1, 2])

    def test_minimal_two_elements(self):
        self.assertEqual(self.sol.twoSum([1, 2], 3), [1, 2])

    def test_minimal_two_elements_negative(self):
        self.assertEqual(self.sol.twoSum([-5, 5], 0), [1, 2])

    def test_duplicates_in_array(self):
        self.assertEqual(self.sol.twoSum([0, 0, 3, 4], 0), [1, 2])

    def test_negative_target(self):
        self.assertEqual(self.sol.twoSum([-3, -1, 2, 6, 10, 15], -4), [1, 2])

    def test_all_negative_numbers(self):
        self.assertEqual(self.sol.twoSum([-10, -7, -3, 2, 6], -13), [1, 3])

    def test_positive_and_negative_mixed(self):
        self.assertEqual(self.sol.twoSum([-4, -1, 1, 3], 2), [2, 4])

    def test_target_zero(self):
        self.assertEqual(self.sol.twoSum([-3, 1, 2, 3], 0), [1, 4])

    def test_solution_at_end_of_array(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5], 9), [4, 5])

    def test_solution_at_beginning_of_array(self):
        self.assertEqual(self.sol.twoSum([1, 2, 3, 4, 5], 3), [1, 2])

    def test_zeros_in_array(self):
        self.assertEqual(self.sol.twoSum([0, 1, 2, 3], 3), [1, 4])

    def test_large_values_within_constraints(self):
        numbers = [-1000, 1000]
        self.assertEqual(self.sol.twoSum(numbers, 0), [1, 2])

    def test_repeated_identical_values(self):
        self.assertEqual(self.sol.twoSum([5, 5, 5, 5], 10), [1, 4])
        self.assertEqual(self.sol.twoSum([3, 3, 3, 4, 5], 7), [1, 4])

    def test_result_increasing_order(self):
        result = self.sol.twoSum([2, 7, 11, 15], 26)
        self.assertEqual(result, [3, 4])
        self.assertLess(result[0], result[1])

    def test_result_length(self):
        for nums, target in (
            ([2, 7, 11, 15], 9),
            ([2, 3, 4], 6),
            ([-1, 0], -1),
        ):
            result = self.sol.twoSum(nums, target)
            self.assertEqual(len(result), 2)

    def test_long_sorted_array(self):
        numbers = list(range(1, 15001))
        self.assertEqual(self.sol.twoSum(numbers, 29999), [14999, 15000])

    def test_solution_not_reusing_element(self):
        result = self.sol.twoSum([0, 0, 3, 4], 0)
        self.assertNotEqual(result[0], result[1])

    def test_single_use_of_each_index(self):
        numbers = [1, 1, 1, 1000, 1000, 1000]
        self.assertEqual(self.sol.twoSum(numbers, 2000), [4, 6])

    def test_bounds_of_constraints(self):
        self.assertEqual(self.sol.twoSum([-1000, 1000], 0), [1, 2])


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Binary Search
