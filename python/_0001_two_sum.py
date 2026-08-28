# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Easy

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def check(self, nums, target, expected_set):
        result = self.sol.twoSum(nums, target)
        self.assertEqual(
            set(result), expected_set, "nums=%r target=%r" % (nums, target)
        )
        self.assertEqual(len(result), 2)

    def test_example_1(self):
        self.check([2, 7, 11, 15], 9, {0, 1})

    def test_example_2(self):
        self.check([3, 2, 4], 6, {1, 2})

    def test_example_3_duplicate_values(self):
        self.check([3, 3], 6, {0, 1})

    def test_two_elements(self):
        self.check([0, 4], 4, {0, 1})

    def test_negative_numbers(self):
        self.check([-3, 4, 3, 90], 0, {0, 2})

    def test_all_negative(self):
        self.check([-1, -2, -3, -4], -6, {1, 3})

    def test_with_zeros(self):
        self.check([0, 4, 5], 4, {0, 1})
        self.check([0, 3, 5], 3, {0, 1})

    def test_solution_at_end(self):
        self.check([1, 2, 3, 4, 5], 9, {3, 4})

    def test_solution_at_start(self):
        self.check([8, 1, 2, 3], 9, {0, 1})

    def test_large_values(self):
        self.check([10**9, 123, 5], 10**9 + 123, {0, 1})
        self.check([123456789, 987654321, 2], 1111111110, {0, 1})

    def test_duplicate_elements_different_positions(self):
        self.check([1, 3, 3, 4], 6, {1, 2})

    def test_same_element_not_reused(self):
        result = self.sol.twoSum([1, 5], 2)
        self.assertEqual(result, [])

    def test_returns_indices_not_values(self):
        nums = [50, 50, 10]
        result = self.sol.twoSum(nums, 100)
        self.assertEqual(sorted(result), [0, 1])
        for idx in result:
            self.assertGreaterEqual(idx, 0)
            self.assertLess(idx, len(nums))

    def test_result_indices_are_valid(self):
        nums = [10, 20, 30, 40]
        result = self.sol.twoSum(nums, 50)
        self.assertEqual(len(result), 2)
        self.assertNotEqual(result[0], result[1])
        self.assertEqual(nums[result[0]] + nums[result[1]], 50)

    def test_single_pair_among_many(self):
        nums = list(range(1, 10))
        self.check(nums, 17, {7, 8})

    def test_large_input_length(self):
        import random

        random.seed(42)
        n = 10**4
        nums = [random.randint(-(10**9), 10**9) for _ in range(n)]
        a, b = n // 2, n - 1
        target = nums[a] + nums[b]
        result = self.sol.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted([a, b]))

    def test_returns_list_type(self):
        result = self.sol.twoSum([1, 2, 3], 4)
        self.assertIsInstance(result, list)
        for idx in result:
            self.assertIsInstance(idx, int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table
