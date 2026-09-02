# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Medium

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)

    def test_example3(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2)

    def test_single_balloon(self):
        self.assertEqual(self.solution.findMinArrowShots([[5, 10]]), 1)

    def test_single_point_span(self):
        self.assertEqual(self.solution.findMinArrowShots([[0, 1]]), 1)

    def test_two_identical_balloons(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 3], [1, 3]]), 1)

    def test_two_non_overlapping(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 2], [3, 4]]), 2)

    def test_touching_balloons(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 2], [2, 3]]), 1)

    def test_nested_balloons(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 10], [2, 8], [3, 6], [4, 5]]), 1)

    def test_negative_coordinates(self):
        self.assertEqual(self.solution.findMinArrowShots([[-10, -5], [-4, 0], [1, 5]]), 3)

    def test_negative_overlapping(self):
        self.assertEqual(self.solution.findMinArrowShots([[-5, -1], [-3, 2], [0, 6]]), 2)

    def test_empty_after_constraint_removed(self):
        self.assertEqual(self.solution.findMinArrowShots([]), 0)

    def test_duplicate_intervals_many(self):
        points = [[1, 5]] * 5
        self.assertEqual(self.solution.findMinArrowShots(points), 1)

    def test_chain_overlap(self):
        self.assertEqual(self.solution.findMinArrowShots([[1, 3], [2, 4], [3, 5], [4, 6]]), 2)

    def test_already_sorted_vs_unsorted_input(self):
        ordered = [[2, 8], [1, 6], [7, 12], [10, 16]]
        unordered = [[10, 16], [2, 8], [1, 6], [7, 12]]
        self.assertEqual(
            self.solution.findMinArrowShots(ordered),
            self.solution.findMinArrowShots(unordered),
        )

    def test_large_values_within_bounds(self):
        points = [[-(2**31), 2**31 - 1]]
        self.assertEqual(self.solution.findMinArrowShots(points), 1)

    def test_far_apart_extremes(self):
        points = [[-(2**31), -(2**31) + 1], [2**31 - 2, 2**31 - 1]]
        self.assertEqual(self.solution.findMinArrowShots(points), 2)

    def test_three_clusters(self):
        points = [[0, 1], [2, 3], [4, 5], [0, 1], [2, 3]]
        self.assertEqual(self.solution.findMinArrowShots(points), 3)

    def test_all_share_common_point(self):
        points = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]
        self.assertEqual(self.solution.findMinArrowShots(points), 1)

    def test_input_not_mutated_semantics(self):
        points = [[1, 6], [2, 8], [7, 12], [10, 16]]
        original = [list(p) for p in points]
        result = self.solution.findMinArrowShots(points)
        self.assertEqual(result, 2)
        self.assertEqual([list(p) for p in points], original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Greedy, Sorting
