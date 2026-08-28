# 120. Triangle
# https://leetcode.com/problems/triangle/
# Medium

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(
            self.sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11
        )

    def test_example2_single_negative(self):
        self.assertEqual(self.sol.minimumTotal([[-10]]), -10)

    def test_single_element_positive(self):
        self.assertEqual(self.sol.minimumTotal([[5]]), 5)

    def test_single_element_zero(self):
        self.assertEqual(self.sol.minimumTotal([[0]]), 0)

    def test_two_rows(self):
        self.assertEqual(self.sol.minimumTotal([[1], [2, 3]]), 3)

    def test_negative_values(self):
        triangle = [[-1], [2, 3], [1, -1, -3]]
        self.assertEqual(self.sol.minimumTotal(triangle), -1)

    def test_all_negative(self):
        triangle = [[-5], [-2, -3], [-1, -4, -2]]
        self.assertEqual(self.sol.minimumTotal(triangle), -12)

    def test_zeroes(self):
        triangle = [[0], [0, 0], [0, 0, 0]]
        self.assertEqual(self.sol.minimumTotal(triangle), 0)

    def test_mixed(self):
        triangle = [[-1], [2, 5], [1, -3, 4]]
        self.assertEqual(self.sol.minimumTotal(triangle), -2)

    def test_path_down_the_left_edge(self):
        triangle = [[1], [1, 100], [1, 100, 100], [1, 100, 100, 100]]
        self.assertEqual(self.sol.minimumTotal(triangle), 4)

    def test_path_down_the_right_edge(self):
        triangle = [[1], [100, 1], [100, 100, 1], [100, 100, 100, 1]]
        self.assertEqual(self.sol.minimumTotal(triangle), 4)

    def test_middle_path_best(self):
        triangle = [[10], [1, 100], [50, 2, 60]]
        self.assertEqual(self.sol.minimumTotal(triangle), 13)

    def test_large_values(self):
        triangle = [[10000], [10000, 10000], [10000, 10000, 10000]]
        self.assertEqual(self.sol.minimumTotal(triangle), 30000)

    def test_wide_triangle(self):
        n = 50
        triangle = [[-4 * r + 2 * j for j in range(r + 1)] for r in range(n)]
        self.assertEqual(self.sol.minimumTotal(triangle), -4 * n * (n - 1) // 2)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
