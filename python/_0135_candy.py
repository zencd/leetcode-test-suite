# 135. Candy
# https://leetcode.com/problems/candy/
# Hard

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_child(self):
        self.assertEqual(self.solution.candy([1]), 1)

    def test_two_children_increasing(self):
        self.assertEqual(self.solution.candy([1, 2]), 3)

    def test_two_children_decreasing(self):
        self.assertEqual(self.solution.candy([2, 1]), 3)

    def test_two_children_equal(self):
        self.assertEqual(self.solution.candy([1, 1]), 2)

    def test_two_children_both_zero(self):
        self.assertEqual(self.solution.candy([0, 0]), 2)

    def test_example_1(self):
        self.assertEqual(self.solution.candy([1, 0, 2]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.candy([1, 2, 2]), 4)

    def test_all_equal(self):
        self.assertEqual(self.solution.candy([5, 5, 5, 5]), 4)

    def test_strictly_increasing(self):
        self.assertEqual(self.solution.candy([1, 2, 3, 4, 5]), 15)

    def test_strictly_decreasing(self):
        self.assertEqual(self.solution.candy([5, 4, 3, 2, 1]), 15)

    def test_v_shape(self):
        self.assertEqual(self.solution.candy([5, 4, 3, 2, 1, 2, 3, 4, 5]), 29)

    def test_v_shape_small(self):
        self.assertEqual(self.solution.candy([2, 1, 2]), 5)

    def test_peak(self):
        self.assertEqual(self.solution.candy([1, 2, 1]), 4)

    def test_multiple_peaks_and_valleys(self):
        self.assertEqual(self.solution.candy([1, 3, 2, 1, 2, 3, 1]), 13)

    def test_zero_ratings(self):
        self.assertEqual(self.solution.candy([0, 1, 0]), 4)

    def test_zero_rating_middle_with_neighbors_zero(self):
        self.assertEqual(self.solution.candy([0, 0, 0]), 3)

    def test_mixed_zero_and_positive(self):
        self.assertEqual(self.solution.candy([0, 1, 0, 1]), 6)

    def test_long_increasing_run(self):
        self.assertEqual(self.solution.candy([1, 2, 3, 4]), 10)

    def test_long_decreasing_run(self):
        self.assertEqual(self.solution.candy([4, 3, 2, 1]), 10)

    def test_wild_ratings(self):
        self.assertEqual(self.solution.candy([1, 0, 1, 0, 1, 0]), 9)

    def test_large_ratings_values(self):
        self.assertEqual(self.solution.candy([50000, 0, 50000]), 5)

    def test_random_case(self):
        self.assertEqual(self.solution.candy([1, 2, 2, 1, 2, 1, 2, 1]), 12)

    def test_ascending_then_ascending_flat(self):
        self.assertEqual(self.solution.candy([1, 2, 2, 2]), 5)

    def test_three_children_increasing(self):
        self.assertEqual(self.solution.candy([1, 2, 3]), 6)

    def test_three_children_decreasing(self):
        self.assertEqual(self.solution.candy([3, 2, 1]), 6)

    def test_alternating_peaks(self):
        self.assertEqual(self.solution.candy([1, 2, 1, 2, 1]), 7)

    def test_symmetric_v(self):
        self.assertEqual(self.solution.candy([3, 2, 1, 2, 3]), 11)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Greedy
