# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Medium

import unittest
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        raise Exception("Not solved yet")


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_merge_left(self):
        self.assertEqual(
            self.solution.insert([[1, 3], [6, 9]], [2, 5]),
            [[1, 5], [6, 9]],
        )

    def test_merge_multiple(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        )

    def test_empty_intervals(self):
        self.assertEqual(self.solution.insert([], [5, 10]), [[5, 10]])

    def test_empty_interval_input_point(self):
        self.assertEqual(self.solution.insert([], [3, 3]), [[3, 3]])

    def test_insert_before_all(self):
        self.assertEqual(
            self.solution.insert([[5, 6], [7, 10]], [1, 3]),
            [[1, 3], [5, 6], [7, 10]],
        )

    def test_insert_after_all(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 4]], [10, 12]),
            [[1, 2], [3, 4], [10, 12]],
        )

    def test_insert_in_middle_no_overlap(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [10, 11]], [5, 6]),
            [[1, 2], [5, 6], [10, 11]],
        )

    def test_new_interval_covers_all(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 4], [5, 6]], [0, 10]),
            [[0, 10]],
        )

    def test_new_interval_inside_existing(self):
        self.assertEqual(
            self.solution.insert([[1, 10]], [4, 5]),
            [[1, 10]],
        )

    def test_new_interval_equals_existing(self):
        self.assertEqual(
            self.solution.insert([[1, 5], [8, 9]], [1, 5]),
            [[1, 5], [8, 9]],
        )

    def test_single_interval_overlap_right(self):
        self.assertEqual(
            self.solution.insert([[1, 3]], [3, 7]),
            [[1, 7]],
        )

    def test_single_interval_overlap_left(self):
        self.assertEqual(
            self.solution.insert([[5, 9]], [3, 6]),
            [[3, 9]],
        )

    def test_point_touching_between_intervals(self):
        self.assertEqual(
            self.solution.insert([[1, 4], [6, 8]], [4, 6]),
            [[1, 8]],
        )

    def test_adjacent_new_interval_both_sides(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [5, 6]], [2, 5]),
            [[1, 6]],
        )

    def test_new_interval_start_equals_first_start(self):
        self.assertEqual(
            self.solution.insert([[2, 3], [4, 5]], [2, 4]),
            [[2, 5]],
        )

    def test_new_interval_end_equals_last_end(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 8]], [5, 8]),
            [[1, 2], [3, 8]],
        )

    def test_point_interval_new(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [5, 6]], [3, 3]),
            [[1, 2], [3, 3], [5, 6]],
        )

    def test_point_interval_overlap(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [4, 5]], [2, 4]),
            [[1, 5]],
        )

    def test_point_existing_contains_point(self):
        self.assertEqual(
            self.solution.insert([[2, 4]], [3, 3]),
            [[2, 4]],
        )

    def test_zero_values(self):
        self.assertEqual(
            self.solution.insert([[0, 0], [5, 100000]], [0, 5]),
            [[0, 100000]],
        )

    def test_large_values(self):
        self.assertEqual(
            self.solution.insert([[100000, 100000]], [0, 99999]),
            [[0, 99999], [100000, 100000]],
        )

    def test_no_overlap_boundary(self):
        self.assertEqual(
            self.solution.insert([[1, 2]], [3, 4]),
            [[1, 2], [3, 4]],
        )

    def test_merge_into_several_middle(self):
        self.assertEqual(
            self.solution.insert([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], [2, 7]),
            [[1, 8], [9, 10]],
        )

    def test_input_not_mutated(self):
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        self.solution.insert(intervals, new_interval)
        self.assertEqual(intervals, [[1, 3], [6, 9]])
        self.assertEqual(new_interval, [2, 5])

    def test_result_sorted(self):
        result = self.solution.insert([[2, 3], [8, 10], [11, 12]], [0, 9])
        self.assertEqual(result, [[0, 10], [11, 12]])


if __name__ == "__main__":
    unittest.main()

# Tags: Array
