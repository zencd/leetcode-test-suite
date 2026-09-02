# 475. Heaters
# https://leetcode.com/problems/heaters/
# Medium

from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.findRadius([1, 2, 3], [2]), 1)

    def test_example_2(self):
        self.assertEqual(self.sol.findRadius([1, 2, 3, 4], [1, 4]), 1)

    def test_example_3(self):
        self.assertEqual(self.sol.findRadius([1, 5], [2]), 3)

    def test_single_house_single_heater_same_position(self):
        self.assertEqual(self.sol.findRadius([7], [7]), 0)

    def test_single_house_single_heater_different(self):
        self.assertEqual(self.sol.findRadius([3], [10]), 7)

    def test_heater_between_houses(self):
        self.assertEqual(self.sol.findRadius([1, 3], [2]), 1)

    def test_houses_unsorted_input(self):
        self.assertEqual(self.sol.findRadius([3, 1, 2], [2]), 1)

    def test_heaters_unsorted_input(self):
        self.assertEqual(self.sol.findRadius([1, 2, 3, 4], [4, 1]), 1)

    def test_all_houses_covered_by_zero_radius(self):
        self.assertEqual(self.sol.findRadius([1, 2, 3], [1, 2, 3]), 0)

    def test_heaters_outside_house_range(self):
        self.assertEqual(self.sol.findRadius([10, 20], [1, 100]), 19)

    def test_house_exactly_between_two_heaters(self):
        self.assertEqual(self.sol.findRadius([5], [1, 9]), 4)

    def test_duplicate_house_positions(self):
        self.assertEqual(self.sol.findRadius([5, 5, 5], [5]), 0)

    def test_duplicate_heater_positions(self):
        self.assertEqual(self.sol.findRadius([5, 8], [1, 1, 1]), 7)

    def test_many_heaters_few_houses(self):
        self.assertEqual(self.sol.findRadius([10, 20], [1, 5, 9, 12, 18, 21, 30]), 1)

    def test_many_houses_few_heaters(self):
        self.assertEqual(self.sol.findRadius([1, 2, 3, 4, 5, 6, 7], [7]), 6)

    def test_large_positions(self):
        self.assertEqual(self.sol.findRadius([1, 10**9], [5 * 10**8]), 5 * 10**8)

    def test_house_at_both_ends(self):
        self.assertEqual(self.sol.findRadius([1, 100], [50]), 50)

    def test_heaters_surrounding_single_house(self):
        self.assertEqual(self.sol.findRadius([10], [1, 9, 11, 19]), 1)

    def test_minimum_radius_dominated_by_farthest_house(self):
        self.assertEqual(self.sol.findRadius([1, 2, 10], [2]), 8)

    def test_house_left_of_nearest_heater_to_the_right(self):
        self.assertEqual(self.sol.findRadius([1], [2, 3, 4]), 1)

    def test_all_houses_left_of_all_heaters(self):
        self.assertEqual(self.sol.findRadius([1, 2, 3], [10, 20]), 9)

    def test_all_houses_right_of_all_heaters(self):
        self.assertEqual(self.sol.findRadius([10, 20, 30], [1, 2]), 28)

    def test_interleaved(self):
        self.assertEqual(self.sol.findRadius([1, 3, 5, 7, 9], [2, 4, 6, 8]), 1)

    def test_zero_radius_single_overlapping(self):
        self.assertEqual(self.sol.findRadius([42], [41, 42, 43]), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Two Pointers, Binary Search, Sorting
