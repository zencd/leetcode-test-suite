# 363. Max Sum of Rectangle No Larger Than K
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
# Hard

from bisect import bisect_left, insort
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        raise Exception("Not solved yet")


import unittest
import random


def brute_force(matrix: List[List[int]], k: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    best = float("-inf")
    for r1 in range(m):
        for r2 in range(r1, m):
            for c1 in range(n):
                for c2 in range(c1, n):
                    s = sum(
                        matrix[r][c]
                        for r in range(r1, r2 + 1)
                        for c in range(c1, c2 + 1)
                    )
                    if s <= k:
                        best = max(best, s)
    return best


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2), 2)

    def test_example2(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[2, 2, -1]], 3), 3)

    def test_single_cell_equal(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[5]], 5), 5)

    def test_single_cell_less(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[1]], 5), 1)

    def test_single_cell_negative(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[-3]], -3), -3)

    def test_single_cell_negative_k(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[-5]], -1), -5)

    def test_zero_k_zero_matrix(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[0, 0], [0, 0]], 0), 0)

    def test_single_row(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[1, 2, 3, 4]], 5), 5)

    def test_single_column(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[1], [2], [3], [4]], 5), 5)

    def test_all_negative_k_small(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[-1, -2], [-3, -4]], -1), -1)

    def test_all_negative_k_negative(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[-1, -2], [-3, -4]], -8), -10)

    def test_negative_and_positive_mixed(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[1, -1], [-1, 1]], 0), 0)

    def test_best_is_single_element(self):
        matrix = [[100, -100], [-100, 100]]
        self.assertEqual(self.sol.maxSumSubmatrix(matrix, 100), 100)

    def test_k_larger_than_total_sum(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(self.sol.maxSumSubmatrix(matrix, 1000), 10)

    def test_k_negative_full_negation(self):
        matrix = [[-1, -2], [-3, -4]]
        self.assertEqual(self.sol.maxSumSubmatrix(matrix, -10), -10)

    def test_1x1_zero(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[0]], 0), 0)

    def test_1x1_negative_value_positive_k(self):
        self.assertEqual(self.sol.maxSumSubmatrix([[-7]], 2), -7)

    def test_3x3_known(self):
        matrix = [[9, -8, 1], [5, 3, -2], [-1, 7, 0]]
        self.assertEqual(self.sol.maxSumSubmatrix(matrix, 8), 8)

    def test_random_vs_brute_force(self):
        random.seed(1)
        for trial in range(50):
            m = random.randint(1, 4)
            n = random.randint(1, 4)
            matrix = [[random.randint(-5, 5) for _ in range(n)] for _ in range(m)]
            k = random.randint(-10, 20)
            expected = brute_force(matrix, k)
            result = self.sol.maxSumSubmatrix(matrix, k)
            self.assertEqual(
                result,
                expected,
                f"matrix={matrix}, k={k}, got={result}, expected={expected}",
            )


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Binary Search, Matrix, Prefix Sum, Ordered Set
