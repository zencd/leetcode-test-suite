# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Medium

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.minSubArrayLen(4, [1, 4, 4]), 1)

    def test_example3(self):
        self.assertEqual(self.solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)

    def test_single_element_equal_target(self):
        self.assertEqual(self.solution.minSubArrayLen(5, [5]), 1)

    def test_single_element_less_than_target(self):
        self.assertEqual(self.solution.minSubArrayLen(6, [5]), 0)

    def test_single_element_greater_than_target(self):
        self.assertEqual(self.solution.minSubArrayLen(3, [10]), 1)

    def test_first_element_satisfies_target(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [7, 1, 1, 1]), 1)

    def test_last_element_satisfies_target(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [1, 1, 1, 7]), 1)

    def test_all_elements_needed(self):
        self.assertEqual(self.solution.minSubArrayLen(15, [1, 2, 3, 4, 5]), 5)

    def test_no_subarray_possible(self):
        self.assertEqual(self.solution.minSubArrayLen(100, [1, 2, 3]), 0)

    def test_target_greatly_exceeds_sum(self):
        self.assertEqual(self.solution.minSubArrayLen(10**9, [1, 1, 1]), 0)

    def test_target_one(self):
        self.assertEqual(self.solution.minSubArrayLen(1, [10000, 10000, 10000]), 1)

    def test_subarray_at_start(self):
        self.assertEqual(self.solution.minSubArrayLen(6, [3, 3, 2, 2, 2]), 2)

    def test_subarray_in_middle(self):
        self.assertEqual(self.solution.minSubArrayLen(8, [1, 1, 4, 4, 1, 1]), 2)

    def test_subarray_at_end(self):
        self.assertEqual(self.solution.minSubArrayLen(6, [1, 1, 1, 2, 4]), 2)

    def test_two_elements_suffice(self):
        self.assertEqual(self.solution.minSubArrayLen(5, [2, 2, 1, 1]), 3)

    def test_large_values(self):
        self.assertEqual(self.solution.minSubArrayLen(19998, [9999, 9999, 1, 1]), 2)

    def test_maximum_constraint_values(self):
        self.assertEqual(self.solution.minSubArrayLen(10000, [10000]), 1)

    def test_duplicated_elements(self):
        self.assertEqual(self.solution.minSubArrayLen(30, [5, 5, 5, 5, 5, 5]), 6)

    def test_alternating_large_small(self):
        self.assertEqual(self.solution.minSubArrayLen(10, [9, 1, 9, 1, 9]), 2)

    def test_all_ones_needs_all(self):
        self.assertEqual(self.solution.minSubArrayLen(10, [1] * 10), 10)

    def test_all_ones_not_enough(self):
        self.assertEqual(self.solution.minSubArrayLen(11, [1] * 10), 0)

    def test_large_array_random_sum(self):
        nums = [i % 10000 + 1 for i in range(100000)]
        self.assertEqual(self.solution.minSubArrayLen(1, nums), 1)

    def test_large_array_impossible(self):
        nums = [1] * 100000
        self.assertEqual(self.solution.minSubArrayLen(100001, nums), 0)

    def test_result_len_two_not_one(self):
        self.assertEqual(self.solution.minSubArrayLen(7, [3, 4, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Sliding Window, Prefix Sum
