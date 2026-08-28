# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Medium

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        self.assertEqual(self.sol.kthSmallest(matrix, 8), 13)

    def test_example_2_single_element(self):
        self.assertEqual(self.sol.kthSmallest([[-5]], 1), -5)

    def test_k_equals_1(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        self.assertEqual(self.sol.kthSmallest(matrix, 1), 1)

    def test_k_equals_n_squared(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        self.assertEqual(self.sol.kthSmallest(matrix, 9), 15)

    def test_k_middle(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        self.assertEqual(self.sol.kthSmallest(matrix, 5), 11)

    def test_all_elements_equal(self):
        matrix = [[7, 7, 7], [7, 7, 7], [7, 7, 7]]
        self.assertEqual(self.sol.kthSmallest(matrix, 1), 7)
        self.assertEqual(self.sol.kthSmallest(matrix, 9), 7)

    def test_negative_numbers(self):
        matrix = [[-10, -5, -1], [-9, -3, 2], [-4, 0, 6]]
        self.assertEqual(self.sol.kthSmallest(matrix, 1), -10)
        self.assertEqual(self.sol.kthSmallest(matrix, 5), -3)
        self.assertEqual(self.sol.kthSmallest(matrix, 9), 6)

    def test_mixed_signs(self):
        matrix = [[-1, 0, 1], [2, 3, 4], [5, 6, 7]]
        self.assertEqual(self.sol.kthSmallest(matrix, 4), 2)
        self.assertEqual(self.sol.kthSmallest(matrix, 8), 6)

    def test_two_by_two(self):
        matrix = [[1, 3], [2, 4]]
        self.assertEqual(self.sol.kthSmallest(matrix, 1), 1)
        self.assertEqual(self.sol.kthSmallest(matrix, 2), 2)
        self.assertEqual(self.sol.kthSmallest(matrix, 3), 3)
        self.assertEqual(self.sol.kthSmallest(matrix, 4), 4)

    def test_duplicated_values_on_diagonal(self):
        matrix = [[1, 1, 1], [1, 2, 2], [1, 2, 3]]
        self.assertEqual(self.sol.kthSmallest(matrix, 5), 1)
        self.assertEqual(self.sol.kthSmallest(matrix, 6), 2)
        self.assertEqual(self.sol.kthSmallest(matrix, 7), 2)

    def test_large_values(self):
        big = 10**9
        matrix = [[-big, -big + 1], [big - 1, big]]
        self.assertEqual(self.sol.kthSmallest(matrix, 1), -big)
        self.assertEqual(self.sol.kthSmallest(matrix, 2), -big + 1)
        self.assertEqual(self.sol.kthSmallest(matrix, 3), big - 1)
        self.assertEqual(self.sol.kthSmallest(matrix, 4), big)

    def test_row_like_gradient(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        for k in range(1, 17):
            self.assertEqual(self.sol.kthSmallest(matrix, k), k)

    def test_matrix_is_not_mutated(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        original = [row[:] for row in matrix]
        self.sol.kthSmallest(matrix, 8)
        self.assertEqual(matrix, original)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Sorting, Heap (Priority Queue), Matrix
