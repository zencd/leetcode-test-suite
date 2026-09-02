# 447. Number of Boomerangs
# https://leetcode.com/problems/number-of-boomerangs/
# Medium

from typing import List
from collections import Counter


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]), 2)

    def test_example3_single_point(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[1, 1]]), 0)

    def test_two_points(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [0, 1]]), 0)

    def test_unit_square(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [0, 1], [1, 0], [1, 1]]), 8)

    def test_no_boomerangs(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [1, 2], [4, 7], [9, -3]]), 0)

    def test_symmetric_pair_at_center(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [1, 0], [-1, 0]]), 2)

    def test_vertical_symmetric(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [0, 1], [0, -1]]), 2)

    def test_three_equal_distances(self):
        pts = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]
        self.assertEqual(self.sol.numberOfBoomerangs(pts), 20)

    def test_negative_coordinates(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[-1, -1], [0, 0], [1, 1]]), 2)

    def test_large_coordinates(self):
        a = 10**4
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [a, 0], [-a, 0], [a, a]]), 4)

    def test_two_centers(self):
        pts = [[0, 0], [1, 0], [-1, 0], [10, 0], [9, 0], [11, 0]]
        self.assertEqual(self.sol.numberOfBoomerangs(pts), 4)

    def test_unordered_input_same_result(self):
        self.assertEqual(
            self.sol.numberOfBoomerangs([[2, 0], [0, 0], [1, 0]]),
            self.sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]),
        )

    def test_diamond(self):
        pts = [[0, 2], [2, 0], [0, -2], [-2, 0]]
        self.assertEqual(self.sol.numberOfBoomerangs(pts), 8)

    def test_lattice_cross(self):
        pts = [[0, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        self.assertEqual(self.sol.numberOfBoomerangs(pts), 20)

    def test_reference_check(self):
        self.assertEqual(self.sol.numberOfBoomerangs([[0, 0], [1, 1], [2, 2], [1, 2]]), 4)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Math
