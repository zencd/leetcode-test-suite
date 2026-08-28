# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Medium

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(
            self.solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_example2_touching(self):
        self.assertEqual(
            self.solution.merge([[1, 4], [4, 5]]),
            [[1, 5]],
        )

    def test_example3_unsorted(self):
        self.assertEqual(
            self.solution.merge([[4, 7], [1, 4]]),
            [[1, 7]],
        )

    def test_single_interval(self):
        self.assertEqual(
            self.solution.merge([[1, 5]]),
            [[1, 5]],
        )

    def test_two_disjoint(self):
        self.assertEqual(
            self.solution.merge([[1, 2], [3, 4]]),
            [[1, 2], [3, 4]],
        )

    def test_two_overlapping(self):
        self.assertEqual(
            self.solution.merge([[1, 5], [3, 6]]),
            [[1, 6]],
        )

    def test_contained_interval(self):
        self.assertEqual(
            self.solution.merge([[1, 10], [2, 5]]),
            [[1, 10]],
        )

    def test_identical_intervals(self):
        self.assertEqual(
            self.solution.merge([[1, 4], [1, 4], [1, 4]]),
            [[1, 4]],
        )

    def test_point_interval(self):
        self.assertEqual(
            self.solution.merge([[0, 0], [1, 1]]),
            [[0, 0], [1, 1]],
        )

    def test_point_interval_touching(self):
        self.assertEqual(
            self.solution.merge([[0, 0], [0, 5]]),
            [[0, 5]],
        )

    def test_point_interval_inside(self):
        self.assertEqual(
            self.solution.merge([[1, 4], [2, 2]]),
            [[1, 4]],
        )

    def test_all_merged_to_one(self):
        self.assertEqual(
            self.solution.merge([[5, 8], [1, 7], [2, 9]]),
            [[1, 9]],
        )

    def test_none_overlap(self):
        self.assertEqual(
            self.solution.merge([[1, 2], [4, 6], [7, 9]]),
            [[1, 2], [4, 6], [7, 9]],
        )

    def test_reverse_ordered_input(self):
        self.assertEqual(
            self.solution.merge([[15, 18], [8, 10], [2, 6], [1, 3]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_duplicates_with_expansion(self):
        self.assertEqual(
            self.solution.merge([[1, 2], [1, 3], [3, 4]]),
            [[1, 4]],
        )

    def test_zero_values(self):
        self.assertEqual(
            self.solution.merge([[0, 0], [0, 10000]]),
            [[0, 10000]],
        )

    def test_max_value_range(self):
        self.assertEqual(
            self.solution.merge([[9999, 10000], [100, 10000]]),
            [[100, 10000]],
        )

    def test_result_order_matches_sort(self):
        result = self.solution.merge([[15, 18], [1, 3], [8, 10], [2, 6]])
        self.assertEqual(result, [[1, 6], [8, 10], [15, 18]])

    def test_many_small_disjoint_intervals(self):
        intervals = [[i, i] for i in range(10)]
        self.assertEqual(self.solution.merge(intervals), [[i, i] for i in range(10)])

    def test_many_consecutive_touching_intervals(self):
        intervals = [[i, i + 1] for i in range(10)]
        self.assertEqual(self.solution.merge(intervals), [[0, 10]])

    def test_larger_randomized_case(self):
        intervals = [[a, b] for a, b in zip(range(0, 100, 7), range(5, 110, 7))]
        ivs = sorted(intervals)
        exp = [list(ivs[0])]
        for s, e in ivs[1:]:
            if s <= exp[-1][1]:
                exp[-1][1] = max(exp[-1][1], e)
            else:
                exp.append([s, e])
        self.assertEqual(self.solution.merge(intervals), exp)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Sorting, Quicksort
