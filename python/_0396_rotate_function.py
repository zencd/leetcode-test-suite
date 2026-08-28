# 396. Rotate Function
# https://leetcode.com/problems/rotate-function/
# Medium

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxRotateFunction([4, 3, 2, 6]), 26)

    def test_example2_single_element(self):
        self.assertEqual(self.sol.maxRotateFunction([100]), 0)

    def test_negative_single_element(self):
        self.assertEqual(self.sol.maxRotateFunction([-100]), 0)

    def test_two_elements(self):
        self.assertEqual(self.sol.maxRotateFunction([1, 2]), 2)
        self.assertEqual(self.sol.maxRotateFunction([2, 1]), 2)

    def test_negative_numbers(self):
        self.assertEqual(self.sol.maxRotateFunction([-1, -2, -3]), -5)

    def test_mixed_signs(self):
        self.assertEqual(self.sol.maxRotateFunction([1, -2, 3]), 5)

    def test_uniform_elements(self):
        self.assertEqual(self.sol.maxRotateFunction([5, 5, 5, 5]), 30)
        self.assertEqual(self.sol.maxRotateFunction([0, 0, 0]), 0)

    def test_zeros(self):
        self.assertEqual(self.sol.maxRotateFunction([0]), 0)
        self.assertEqual(self.sol.maxRotateFunction([0, 0, 0, 0, 0]), 0)

    def test_two_equal_elements(self):
        self.assertEqual(self.sol.maxRotateFunction([7, 7]), 7)

    def test_brute_force_reference(self):
        def reference(nums):
            n = len(nums)
            best = None
            total = sum(nums)
            best = sum(i * x for i, x in enumerate(nums))
            for k in range(1, n):
                rotated = nums[-k:] + nums[:-k]
                val = sum(i * x for i, x in enumerate(rotated))
                best = max(best, val)
            return best

        cases = [
            [4, 3, 2, 6],
            [100],
            [-100],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [-1, -2, -3, -4, -5],
            [100, -100, 100, -100],
            [1, 1, 1, 2, 2],
            [-3, 0, 2, -1, 5, -2, 100],
            [100, 100, -100, -100, 99],
        ]
        for case in cases:
            with self.subTest(nums=case):
                self.assertEqual(self.sol.maxRotateFunction(case), reference(case))

    def test_all_negatives(self):
        self.assertEqual(self.sol.maxRotateFunction([-1, -2, -3, -4]), -12)

    def test_negative_where_rotation_wins(self):
        self.assertEqual(self.sol.maxRotateFunction([-1, -4, -3, -2]), -10)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Dynamic Programming
