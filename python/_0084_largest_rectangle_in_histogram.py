# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Hard

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)

    def test_example2(self):
        self.assertEqual(self.sol.largestRectangleArea([2, 4]), 4)

    def test_single_bar(self):
        self.assertEqual(self.sol.largestRectangleArea([7]), 7)

    def test_single_zero(self):
        self.assertEqual(self.sol.largestRectangleArea([0]), 0)

    def test_two_equal_bars(self):
        self.assertEqual(self.sol.largestRectangleArea([3, 3]), 6)

    def test_all_equal(self):
        self.assertEqual(self.sol.largestRectangleArea([2, 2, 2, 2]), 8)

    def test_increasing(self):
        self.assertEqual(self.sol.largestRectangleArea([1, 2, 3, 4]), 6)

    def test_decreasing(self):
        self.assertEqual(self.sol.largestRectangleArea([4, 3, 2, 1]), 6)

    def test_valley(self):
        self.assertEqual(self.sol.largestRectangleArea([1, 0, 1]), 1)

    def test_peak(self):
        self.assertEqual(self.sol.largestRectangleArea([1, 3, 1]), 3)

    def test_zeros_inside(self):
        self.assertEqual(self.sol.largestRectangleArea([5, 0, 4]), 5)

    def test_all_zeros(self):
        self.assertEqual(self.sol.largestRectangleArea([0, 0, 0]), 0)

    def test_zigzag(self):
        self.assertEqual(self.sol.largestRectangleArea([2, 1, 2, 1, 2]), 5)

    def test_known_case_12(self):
        self.assertEqual(self.sol.largestRectangleArea([4, 2, 0, 3, 2, 5]), 6)

    def test_single_max_in_middle(self):
        self.assertEqual(self.sol.largestRectangleArea([1, 1, 100000, 1, 1]), 100000)

    def test_max_height_values(self):
        self.assertEqual(self.sol.largestRectangleArea([9999, 10000, 9999]), 29997)

    def test_large_uniform(self):
        self.assertEqual(self.sol.largestRectangleArea([5] * 1000), 5000)

    def test_large_range(self):
        heights = list(range(1, 201))
        n = len(heights)
        self.assertEqual(
            self.sol.largestRectangleArea(heights),
            max(heights[i] * (n - i) for i in range(n)),
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Stack, Monotonic Stack, Range Minimum/Maximum Query
