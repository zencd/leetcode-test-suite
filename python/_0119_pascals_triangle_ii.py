# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/
# Easy

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_row_0(self):
        self.assertEqual(self.sol.getRow(0), [1])

    def test_row_1(self):
        self.assertEqual(self.sol.getRow(1), [1, 1])

    def test_row_2(self):
        self.assertEqual(self.sol.getRow(2), [1, 2, 1])

    def test_row_3(self):
        self.assertEqual(self.sol.getRow(3), [1, 3, 3, 1])

    def test_row_4(self):
        self.assertEqual(self.sol.getRow(4), [1, 4, 6, 4, 1])

    def test_row_5(self):
        self.assertEqual(self.sol.getRow(5), [1, 5, 10, 10, 5, 1])

    def test_row_6(self):
        self.assertEqual(self.sol.getRow(6), [1, 6, 15, 20, 15, 6, 1])

    def test_row_length(self):
        row = self.sol.getRow(10)
        self.assertEqual(len(row), 11)

    def test_endpoints_are_one(self):
        for n in (2, 5, 10, 20, 30):
            row = self.sol.getRow(n)
            self.assertEqual(row[0], 1)
            self.assertEqual(row[-1], 1)

    def test_symmetry(self):
        for n in (0, 1, 4, 7, 13):
            row = self.sol.getRow(n)
            self.assertEqual(row, row[::-1])

    def test_pascal_recurrence(self):
        prev = self.sol.getRow(1)
        for n in range(2, 15):
            cur = self.sol.getRow(n)
            expected = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
            self.assertEqual(cur, expected)
            prev = cur

    def test_known_values(self):
        self.assertEqual(self.sol.getRow(8), [1, 8, 28, 56, 70, 56, 28, 8, 1])
        self.assertEqual(self.sol.getRow(9), [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])

    def test_max_row_33_length(self):
        self.assertEqual(len(self.sol.getRow(33)), 34)

    def test_max_row_33_endpoints(self):
        row = self.sol.getRow(33)
        self.assertEqual(row[0], 1)
        self.assertEqual(row[-1], 1)
        self.assertEqual(row[1], 33)
        self.assertEqual(row[2], 528)

    def test_max_row_33_symmetry(self):
        row = self.sol.getRow(33)
        self.assertEqual(row, row[::-1])

    def test_does_not_mutate_input_or_share_state(self):
        r1 = self.sol.getRow(5)
        r2 = self.sol.getRow(5)
        self.assertIsNot(r1, r2)

    def test_return_type(self):
        self.assertIsInstance(self.sol.getRow(3), list)
        self.assertTrue(all(isinstance(x, int) for x in self.sol.getRow(10)))


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Dynamic Programming
