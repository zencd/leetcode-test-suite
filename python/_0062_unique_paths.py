# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# Medium

from math import comb
from typing import List
import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        raise Exception("Not solved yet")


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)

    def test_example2(self):
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)

    def test_single_cell(self):
        self.assertEqual(self.solution.uniquePaths(1, 1), 1)

    def test_single_row(self):
        self.assertEqual(self.solution.uniquePaths(1, 5), 1)

    def test_single_column(self):
        self.assertEqual(self.solution.uniquePaths(5, 1), 1)

    def test_two_rows_two_columns(self):
        self.assertEqual(self.solution.uniquePaths(2, 2), 2)

    def test_two_by_three(self):
        self.assertEqual(self.solution.uniquePaths(2, 3), 3)

    def test_three_by_three(self):
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)

    def test_four_by_four(self):
        self.assertEqual(self.solution.uniquePaths(4, 4), 20)

    def test_five_by_five(self):
        self.assertEqual(self.solution.uniquePaths(5, 5), 70)

    def test_symmetry(self):
        cases = [(1, 50), (2, 99), (3, 100), (7, 3), (10, 40), (60, 40)]
        for m, n in cases:
            self.assertEqual(
                self.solution.uniquePaths(m, n),
                self.solution.uniquePaths(n, m),
                f"m={m}, n={n}",
            )

    def test_one_row_many_columns(self):
        self.assertEqual(self.solution.uniquePaths(1, 100), 1)

    def test_one_column_many_rows(self):
        self.assertEqual(self.solution.uniquePaths(100, 1), 1)

    def test_large(self):
        self.assertEqual(
            self.solution.uniquePaths(100, 100),
            22750883079422934966181954039568885395604168260154104734000,
        )

    def test_known_values_table(self):
        cases: List[tuple] = [
            (1, 1, 1),
            (1, 2, 1),
            (2, 1, 1),
            (1, 3, 1),
            (3, 1, 1),
            (2, 2, 2),
            (2, 4, 4),
            (4, 2, 4),
            (3, 3, 6),
            (2, 8, 8),
            (8, 2, 8),
            (3, 4, 10),
            (4, 3, 10),
            (4, 5, 35),
            (6, 6, 252),
            (2, 100, 100),
            (100, 2, 100),
        ]
        for m, n, expected in cases:
            self.assertEqual(self.solution.uniquePaths(m, n), expected, f"m={m}, n={n}")

    def test_matches_dp(self):
        for m in range(1, 21):
            for n in range(1, 21):
                dp = [[1] * n for _ in range(m)]
                for i in range(1, m):
                    for j in range(1, n):
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                self.assertEqual(
                    self.solution.uniquePaths(m, n),
                    dp[m - 1][n - 1],
                    f"m={m}, n={n}",
                )

    def test_multiple_instances(self):
        s1 = Solution()
        s2 = Solution()
        for m, n in [(3, 7), (3, 2), (1, 1), (5, 1), (10, 10), (42, 7)]:
            self.assertEqual(s1.uniquePaths(m, n), s2.uniquePaths(m, n))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Combinatorics
