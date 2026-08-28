# 391. Perfect Rectangle
# https://leetcode.com/problems/perfect-rectangle/
# Hard

from typing import List
from collections import Counter


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
            ),
            True,
        )

    def test_example2_gap(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
            ),
            False,
        )

    def test_example3_overlap(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
            ),
            False,
        )

    def test_single_rectangle(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 1, 1]]), True)

    def test_single_full_square(self):
        self.assertEqual(
            self.sol.isRectangleCover([[-100000, -100000, 100000, 100000]]), True
        )

    def test_empty_rectangles(self):
        self.assertEqual(self.sol.isRectangleCover([]), False)

    def test_degenerate_rectangle(self):
        self.assertEqual(self.sol.isRectangleCover([[1, 1, 1, 1]]), False)

    def test_degenerate_zero_width(self):
        self.assertEqual(self.sol.isRectangleCover([[1, 1, 1, 2]]), False)

    def test_two_side_by_side(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 1, 1], [1, 0, 2, 1]]), True)

    def test_two_stacked(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 1, 1], [0, 1, 1, 2]]), True)

    def test_two_overlapping(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 2, 2], [1, 1, 3, 3]]), False)

    def test_two_disjoint(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 1, 1], [2, 2, 3, 3]]), False)

    def test_four_quadrants(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[0, 0, 2, 2], [2, 0, 4, 2], [0, 2, 2, 4], [2, 2, 4, 4]]
            ),
            True,
        )

    def test_grid_2x3(self):
        rects = [[i, j, i + 1, j + 1] for i in range(2) for j in range(3)]
        self.assertEqual(self.sol.isRectangleCover(rects), True)

    def test_grid_with_missing_cell(self):
        rects = [
            [i, j, i + 1, j + 1] for i in range(2) for j in range(3) if (i, j) != (1, 1)
        ]
        self.assertEqual(self.sol.isRectangleCover(rects), False)

    def test_negative_coordinates(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[-2, -2, 0, 0], [0, -2, 2, 0], [-2, 0, 0, 2], [0, 0, 2, 2]]
            ),
            True,
        )

    def test_negative_coordinates_gap(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[-2, -2, 0, 0], [0, -2, 2, 0], [-2, 0, 0, 1], [0, 0, 2, 2]]
            ),
            False,
        )

    def test_rectangles_list_empty_list(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 1, 1], [0, 1, 1, 2]]), True)

    def test_t_shape_not_rectangle(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[0, 0, 1, 1], [1, 0, 2, 1], [0, 1, 3, 2], [3, 0, 4, 1], [3, 1, 4, 2]]
            ),
            False,
        )

    def test_large_valid_rectangle_grid(self):
        rects = [
            [i * 10, j * 10, i * 10 + 10, j * 10 + 10]
            for i in range(5)
            for j in range(7)
        ]
        self.assertEqual(self.sol.isRectangleCover(rects), True)

    def test_duplicate_rectangles(self):
        self.assertEqual(self.sol.isRectangleCover([[0, 0, 1, 1], [0, 0, 1, 1]]), False)

    def test_surrounding_gap_only_corner_check(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[0, 0, 3, 3], [0, 0, 4, 1], [3, 0, 4, 3], [1, 3, 4, 4]]
            ),
            False,
        )

    def test_overlap_inside_valid_boundary(self):
        self.assertEqual(
            self.sol.isRectangleCover(
                [[0, 0, 2, 2], [0, 0, 2, 2], [0, 2, 2, 3], [2, 0, 3, 2]]
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Hash Table, Math, Geometry, Sweep Line
