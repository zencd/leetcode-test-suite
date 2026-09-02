# 413. Arithmetic Slices
# https://leetcode.com/problems/arithmetic-slices/
# Medium

from typing import List
import unittest


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 4]), 3)

    def test_example_2(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1]), 0)

    def test_two_elements(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2]), 0)

    def test_minimal_slice(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3]), 1)

    def test_all_equal(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([7, 7, 7, 7]), 3)

    def test_zero_difference_long(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([0, 0, 0, 0, 0]), 6)

    def test_negative_difference(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([3, -1, -5, -9]), 3)

    def test_not_arithmetic(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 4, 8]), 0)

    def test_multiple_runs(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 10, 11, 12, 13]), 4)

    def test_single_run_inside(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 5, 10, 20, 30]), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([-2, -1, 0, 1, 2]), 6)

    def test_mixed_values(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([5, 3, 1, -1]), 3)

    def test_break_after_long_run(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([2, 4, 6, 8, 10, 11]), 6)

    def test_only_last_slice(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([10, 20, 30, 40]), 3)

    def test_no_slice_with_4_elements_but_splitting(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 3, 5, 6]), 1)

    def test_large_values_within_bounds(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([-1000, -500, 0, 500, 1000]), 3 + 2 + 1)

    def test_interleaved_non_arithmetic(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 4, 1, 2, 3, 4]), 6)

    def test_repeated_pattern(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 2, 3, 2, 3, 4]), 2)

    def test_two_element_arithmetic_pair_not_sliced(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([1, 1]), 0)

    def test_constraint_bounds_values(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([-1000, 0, 1000]), 1)

    def test_constraint_breaking(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([-1000, 0, 0]), 0)

    def test_single_long_arithmetic_run_formula(self):
        n = 10
        self.assertEqual(self.s.numberOfArithmeticSlices(list(range(n))), (n - 1) * (n - 2) // 2)

    def test_empty_not_allowed_but_two(self):
        self.assertEqual(self.s.numberOfArithmeticSlices([4, 5]), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming, Sliding Window
