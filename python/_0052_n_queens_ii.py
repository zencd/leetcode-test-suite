# 52. N-Queens II
# https://leetcode.com/problems/n-queens-ii/
# Hard

import unittest


class Solution:
    def totalNQueens(self, n: int) -> int:
        raise Exception("Not solved yet")


class TestTotalNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_1(self):
        self.assertEqual(self.solution.totalNQueens(1), 1)

    def test_n_2(self):
        self.assertEqual(self.solution.totalNQueens(2), 0)

    def test_n_3(self):
        self.assertEqual(self.solution.totalNQueens(3), 0)

    def test_n_4(self):
        self.assertEqual(self.solution.totalNQueens(4), 2)

    def test_n_5(self):
        self.assertEqual(self.solution.totalNQueens(5), 10)

    def test_n_6(self):
        self.assertEqual(self.solution.totalNQueens(6), 4)

    def test_n_7(self):
        self.assertEqual(self.solution.totalNQueens(7), 40)

    def test_n_8(self):
        self.assertEqual(self.solution.totalNQueens(8), 92)

    def test_n_9(self):
        self.assertEqual(self.solution.totalNQueens(9), 352)

    def test_symmetry_odd_even_consistency(self):
        self.assertEqual(self.solution.totalNQueens(4) % 2, 0)
        self.assertEqual(self.solution.totalNQueens(6) % 2, 0)

    def test_result_is_int(self):
        self.assertIsInstance(self.solution.totalNQueens(8), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Backtracking, Algorithm X
