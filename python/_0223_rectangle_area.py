# 223. Rectangle Area
# https://leetcode.com/problems/rectangle-area/
# Medium

import unittest


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2), 45)

    def test_example2_identical(self):
        self.assertEqual(self.solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2), 16)

    def test_no_overlap_horizontal(self):
        self.assertEqual(self.solution.computeArea(0, 0, 2, 2, 3, 0, 5, 2), 8)

    def test_no_overlap_vertical(self):
        self.assertEqual(self.solution.computeArea(0, 0, 2, 2, 0, 3, 2, 5), 8)

    def test_touching_edges_zero_overlap(self):
        self.assertEqual(self.solution.computeArea(0, 0, 2, 2, 2, 0, 4, 2), 8)

    def test_complete_containment(self):
        self.assertEqual(self.solution.computeArea(0, 0, 10, 10, 2, 2, 8, 8), 100)

    def test_partial_overlap(self):
        self.assertEqual(self.solution.computeArea(0, 0, 4, 4, 2, 2, 6, 6), 28)

    def test_negative_coordinates(self):
        self.assertEqual(self.solution.computeArea(-10, -10, 0, 0, 0, 0, 10, 10), 200)

    def test_point_rectangles(self):
        self.assertEqual(self.solution.computeArea(0, 0, 0, 0, 0, 0, 0, 0), 0)

    def test_zero_area_rectangle(self):
        self.assertEqual(self.solution.computeArea(1, 1, 1, 5, 0, 0, 3, 3), 9)

    def test_max_constraints(self):
        self.assertEqual(
            self.solution.computeArea(
                -(10**4), -(10**4), 10**4, 10**4, -(10**4), -(10**4), 10**4, 10**4
            ),
            400000000,
        )

    def test_one_rectangle_degenerate_line_overlap(self):
        self.assertEqual(self.solution.computeArea(0, 0, 5, 0, 1, 0, 4, 2), 6)

    def test_corner_touch(self):
        self.assertEqual(self.solution.computeArea(0, 0, 1, 1, 1, 1, 2, 2), 2)

    def test_offset_identical_size(self):
        self.assertEqual(self.solution.computeArea(0, 0, 1, 1, 5, 5, 6, 6), 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Geometry
