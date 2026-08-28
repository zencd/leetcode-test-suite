# 149. Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/
# Hard

import unittest
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_single_point(self):
        self.assertEqual(self.s.maxPoints([[1, 1]]), 1)

    def test_two_points(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [2, 2]]), 2)

    def test_three_collinear_example(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [2, 2], [3, 3]]), 3)

    def test_example_two(self):
        self.assertEqual(
            self.s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4
        )

    def test_vertical_line(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [1, 2], [1, 3], [2, 2]]), 3)

    def test_horizontal_line(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [2, 1], [3, 1], [2, 2]]), 3)

    def test_negative_coordinates(self):
        self.assertEqual(self.s.maxPoints([[-1, -1], [0, 0], [1, 1], [2, 2]]), 4)

    def test_fractional_slopes(self):
        self.assertEqual(self.s.maxPoints([[1, 1], [2, 3], [3, 5], [0, 0]]), 3)

    def test_no_three_collinear(self):
        self.assertEqual(self.s.maxPoints([[0, 0], [1, 2], [2, 1], [3, 3]]), 2)

    def test_zero_values(self):
        self.assertEqual(self.s.maxPoints([[0, 0], [0, 1], [0, 2], [1, 1]]), 3)

    def test_large_coordinates(self):
        pts = [[-10000, -10000], [0, 0], [10000, 10000], [5, 5]]
        self.assertEqual(self.s.maxPoints(pts), 4)

    def test_mixed_duplicate_like_lines(self):
        pts = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2]]
        self.assertEqual(self.s.maxPoints(pts), 4)

    def test_diagonal_negative_slope(self):
        self.assertEqual(self.s.maxPoints([[1, 3], [2, 2], [3, 1], [0, 0]]), 3)

    def test_all_points_same_line_5(self):
        pts = [[i, 2 * i + 1] for i in range(5)]
        self.assertEqual(self.s.maxPoints(pts), 5)

    def test_two_parallel_lines(self):
        pts = [[0, 0], [2, 0], [0, 2], [2, 2], [1, 1]]
        self.assertEqual(self.s.maxPoints(pts), 3)

    def test_l_shape(self):
        pts = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2]]
        self.assertEqual(self.s.maxPoints(pts), 3)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Math, Geometry, Euclidean Algorithm, Greatest Common Divisor
