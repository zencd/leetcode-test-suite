# 352. Data Stream as Disjoint Intervals
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# Hard

from typing import List
from bisect import bisect_left


class SummaryRanges:
    def __init__(self):
        raise Exception("Not solved yet")

    def addNum(self, value: int) -> None:
        raise Exception("Not solved yet")

    def getIntervals(self) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_example_from_statement(self):
        sr = SummaryRanges()
        sr.addNum(1)
        self.assertEqual(sr.getIntervals(), [[1, 1]])
        sr.addNum(3)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3]])
        sr.addNum(7)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3], [7, 7]])
        sr.addNum(2)
        self.assertEqual(sr.getIntervals(), [[1, 3], [7, 7]])
        sr.addNum(6)
        self.assertEqual(sr.getIntervals(), [[1, 3], [6, 7]])

    def test_empty_stream(self):
        sr = SummaryRanges()
        self.assertEqual(sr.getIntervals(), [])

    def test_single_value(self):
        sr = SummaryRanges()
        sr.addNum(5)
        self.assertEqual(sr.getIntervals(), [[5, 5]])

    def test_zero(self):
        sr = SummaryRanges()
        sr.addNum(0)
        self.assertEqual(sr.getIntervals(), [[0, 0]])

    def test_duplicate_add(self):
        sr = SummaryRanges()
        sr.addNum(5)
        sr.addNum(5)
        sr.addNum(5)
        self.assertEqual(sr.getIntervals(), [[5, 5]])

    def test_duplicate_inside_interval(self):
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(2)
        sr.addNum(3)
        sr.addNum(2)
        self.assertEqual(sr.getIntervals(), [[1, 3]])

    def test_merge_two_intervals(self):
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(2)
        sr.addNum(4)
        sr.addNum(5)
        self.assertEqual(sr.getIntervals(), [[1, 2], [4, 5]])
        sr.addNum(3)
        self.assertEqual(sr.getIntervals(), [[1, 5]])

    def test_merge_three_intervals(self):
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(4)
        sr.addNum(7)
        sr.addNum(3)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 4], [7, 7]])
        sr.addNum(5)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 5], [7, 7]])
        sr.addNum(2)
        sr.addNum(6)
        self.assertEqual(sr.getIntervals(), [[1, 7]])

    def test_add_before_all(self):
        sr = SummaryRanges()
        sr.addNum(10)
        sr.addNum(11)
        sr.addNum(9)
        self.assertEqual(sr.getIntervals(), [[9, 11]])

    def test_add_after_all(self):
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(2)
        sr.addNum(3)
        self.assertEqual(sr.getIntervals(), [[1, 3]])

    def test_add_far_away(self):
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(10000)
        self.assertEqual(sr.getIntervals(), [[1, 1], [10000, 10000]])

    def test_sorted_output_disorderly_inserts(self):
        sr = SummaryRanges()
        for value in [9, 3, 7, 1, 5]:
            sr.addNum(value)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9]])

    def test_extending_both_sides(self):
        sr = SummaryRanges()
        sr.addNum(50)
        sr.addNum(49)
        sr.addNum(51)
        sr.addNum(48)
        self.assertEqual(sr.intervals, [[48, 51]])

    def test_max_value(self):
        sr = SummaryRanges()
        sr.addNum(10000)
        self.assertEqual(sr.getIntervals(), [[10000, 10000]])

    def test_large_stream(self):
        sr = SummaryRanges()
        for value in range(0, 500, 2):
            sr.addNum(value)
        self.assertEqual(sr.getIntervals(), [[i, i] for i in range(0, 500, 2)])
        for value in range(1, 500, 2):
            sr.addNum(value)
        self.assertEqual(sr.getIntervals(), [[0, 499]])

    def test_interval_not_mutated_by_returned_list(self):
        sr = SummaryRanges()
        sr.addNum(1)
        result = sr.getIntervals()
        result.append([99, 99])
        self.assertEqual(sr.getIntervals(), [[1, 1]])

    def test_interleaved_get_intervals(self):
        sr = SummaryRanges()
        self.assertEqual(sr.getIntervals(), [])
        sr.addNum(4)
        self.assertEqual(sr.getIntervals(), [[4, 4]])
        sr.addNum(1)
        self.assertEqual(sr.getIntervals(), [[1, 1], [4, 4]])
        self.assertEqual(sr.getIntervals(), [[1, 1], [4, 4]])
        sr.addNum(5)
        self.assertEqual(sr.getIntervals(), [[1, 1], [4, 5]])


if __name__ == "__main__":
    unittest.main()

# Tags: Hash Table, Binary Search, Union-Find, Design, Data Stream, Ordered Set
