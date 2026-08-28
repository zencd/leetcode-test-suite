# 218. The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/
# Hard

from typing import List
import heapq
from collections import Counter


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        expected = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_example2(self):
        buildings = [[0, 2, 3], [2, 5, 3]]
        expected = [[0, 3], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_single_building(self):
        self.assertEqual(self.solution.getSkyline([[2, 9, 10]]), [[2, 10], [9, 0]])

    def test_one_building(self):
        buildings = [[3, 9, 8]]
        expected = [[3, 8], [9, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_identical_buildings(self):
        buildings = [[1, 2, 1], [1, 2, 1]]
        expected = [[1, 1], [2, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_two_buildings_different_height(self):
        buildings = [[0, 4, 3], [7, 9, 4]]
        expected = [[0, 3], [4, 0], [7, 4], [9, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_two_adjacent_buildings_same_height(self):
        buildings = [[0, 2, 3], [2, 5, 3]]
        expected = [[0, 3], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_two_overlapping_buildings_different_heights(self):
        buildings = [[0, 4, 3], [2, 5, 4]]
        expected = [[0, 3], [2, 4], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_two_buildings_different_height(self):
        buildings = [[0, 10, 10], [5, 15, 5]]
        expected = [[0, 10], [10, 5], [15, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_two_buildings_different_height2(self):
        buildings = [[0, 10, 1], [5, 15, 5]]
        expected = [[0, 1], [5, 5], [15, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_three_buildings(self):
        buildings = [[0, 10, 10], [5, 15, 20], [12, 20, 5]]
        expected = [[0, 10], [5, 20], [15, 5], [20, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_buildings_with_same_left_and_right(self):
        buildings = [[1, 2, 3], [1, 2, 3]]
        expected = [[1, 3], [2, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_buildings_with_same_right_different_height(self):
        buildings = [[0, 2, 3], [2, 5, 2]]
        expected = [[0, 3], [2, 2], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_buildings_different_heights_overlap(self):
        buildings = [[0, 10, 1], [3, 8, 2], [5, 6, 3]]
        expected = [[0, 1], [3, 2], [5, 3], [6, 2], [8, 1], [10, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_buildings_all_separated(self):
        buildings = [[0, 2, 5], [5, 6, 5], [8, 10, 5]]
        expected = [[0, 5], [2, 0], [5, 5], [6, 0], [8, 5], [10, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_nested_buildings(self):
        buildings = [[0, 100, 1], [10, 80, 5], [30, 50, 20]]
        expected = [[0, 1], [10, 5], [30, 20], [50, 5], [80, 1], [100, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_buildings_overlapping_with_same_start(self):
        buildings = [[2, 9, 10], [2, 12, 20], [2, 7, 5]]
        expected = [[2, 20], [12, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_larger_height_dominates(self):
        buildings = [[0, 5, 3], [1, 4, 10]]
        expected = [[0, 3], [1, 10], [4, 3], [5, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_large_heights(self):
        max_val = (1 << 31) - 1
        buildings = [[0, max_val, 1], [1, max_val - 1, max_val]]
        expected = [[0, 1], [1, max_val], [max_val - 1, 1], [max_val, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_many_buildings_same_height_row(self):
        buildings = [[i * 10, i * 10 + 10, 7] for i in range(5)]
        expected = [[0, 7], [50, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_zigzag_heights(self):
        buildings = [[0, 10, 2], [1, 11, 3], [2, 12, 2], [3, 13, 3]]
        expected = [[0, 2], [1, 3], [13, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_gap_between_buildings(self):
        buildings = [[0, 2, 5], [5, 7, 5]]
        expected = [[0, 5], [2, 0], [5, 5], [7, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_identical_duplicate_buildings(self):
        buildings = [[1, 2, 1], [1, 2, 1], [1, 2, 1]]
        expected = [[1, 1], [2, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_height_zero_not_allowed(self):
        buildings = [[0, 1, 1]]
        expected = [[0, 1], [1, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_single_building_min_height_max_span(self):
        max_val = (1 << 31) - 1
        buildings = [[0, max_val, 1]]
        expected = [[0, 1], [max_val, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_building_starts_at_zero(self):
        buildings = [[0, 5, 3], [5, 10, 2]]
        expected = [[0, 3], [5, 2], [10, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)

    def test_unsorted_similar_pattern(self):
        buildings = [[0, 2, 3], [1, 3, 4], [2, 4, 2]]
        expected = [[0, 3], [1, 4], [3, 2], [4, 0]]
        self.assertEqual(self.solution.getSkyline(buildings), expected)


import unittest

if __name__ == "__main__":
    unittest.main()

# Tags: Array, Divide and Conquer, Binary Indexed Tree, Segment Tree, Sweep Line, Sorting, Heap (Priority Queue), Ordered Set
