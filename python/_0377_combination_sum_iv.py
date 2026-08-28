# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/
# Medium

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.combinationSum4([1, 2, 3], 4), 7)

    def test_example2(self):
        self.assertEqual(self.sol.combinationSum4([9], 3), 0)

    def test_target_1(self):
        self.assertEqual(self.sol.combinationSum4([1], 1), 1)

    def test_single_elem_target(self):
        self.assertEqual(self.sol.combinationSum4([2], 2), 1)

    def test_single_elem_repeat(self):
        self.assertEqual(self.sol.combinationSum4([2], 6), 1)

    def test_single_elem_odd(self):
        self.assertEqual(self.sol.combinationSum4([2], 7), 0)

    def test_two_nums_order_matters(self):
        self.assertEqual(self.sol.combinationSum4([1, 2], 3), 3)

    def test_two_nums_target_4(self):
        self.assertEqual(self.sol.combinationSum4([1, 2], 4), 5)

    def test_order_independence_of_input(self):
        self.assertEqual(
            self.sol.combinationSum4([1, 2, 3], 4),
            self.sol.combinationSum4([3, 2, 1], 4),
        )

    def test_large_num_greater_than_target(self):
        self.assertEqual(self.sol.combinationSum4([1000], 1), 0)

    def test_all_nums_greater_than_target(self):
        self.assertEqual(self.sol.combinationSum4([5, 6, 7], 4), 0)

    def test_known_small_values(self):
        self.assertEqual(self.sol.combinationSum4([1, 2, 3], 1), 1)
        self.assertEqual(self.sol.combinationSum4([1, 2, 3], 2), 2)
        self.assertEqual(self.sol.combinationSum4([1, 2, 3], 3), 4)

    def test_fibonacci_like(self):
        self.assertEqual(self.sol.combinationSum4([1, 2], 10), 89)

    def test_many_ones(self):
        self.assertEqual(self.sol.combinationSum4([1], 20), 1)

    def test_with_zero_target_not_expected_but_guard(self):
        self.assertEqual(self.sol.combinationSum4([1, 2, 3], 0), 1)

    def test_max_constraints_small(self):
        nums = list(range(1, 201))
        self.assertEqual(self.sol.combinationSum4(nums, 1000) > 0, True)

    def test_deterministic_repeated_calls(self):
        a = self.sol.combinationSum4([1, 2, 3, 4], 20)
        b = self.sol.combinationSum4([4, 3, 2, 1], 20)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
