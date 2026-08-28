# 77. Combinations
# https://leetcode.com/problems/combinations/
# Medium

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        raise Exception("Not solved yet")


import unittest


class TestCombine(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            sorted(self.s.combine(4, 2)),
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
        )

    def test_example2(self):
        self.assertEqual(self.s.combine(1, 1), [[1]])

    def test_k_equals_n(self):
        self.assertEqual(self.s.combine(3, 3), [[1, 2, 3]])

    def test_k_equals_1(self):
        self.assertEqual(self.s.combine(5, 1), [[1], [2], [3], [4], [5]])

    def test_n_equals_1(self):
        self.assertEqual(self.s.combine(1, 1), [[1]])

    def test_returns_lists_not_tuple(self):
        for combo in self.s.combine(5, 2):
            self.assertIsInstance(combo, list)
            for x in combo:
                self.assertIsInstance(x, int)

    def test_combination_length(self):
        res = self.s.combine(6, 4)
        self.assertEqual(len(res), 15)

    def test_no_duplicates(self):
        res = self.s.combine(4, 2)
        self.assertEqual(len(res), len({tuple(c) for c in res}))

    def test_within_range(self):
        for c in self.s.combine(10, 3):
            for x in c:
                self.assertTrue(1 <= x <= 10)

    def test_increasing_within_combo(self):
        for c in self.s.combine(8, 3):
            self.assertEqual(c, sorted(c))

    def test_all_combinations_present(self):
        from math import comb

        self.assertEqual(len(self.s.combine(7, 3)), comb(7, 3))

    def test_max_constraints(self):
        res = self.s.combine(20, 10)
        self.assertEqual(len(res), 184756)
        self.assertEqual(len(res[0]), 10)

    def test_result_not_aliased(self):
        res = self.s.combine(4, 2)
        res[0][0] = 99
        self.assertNotEqual(self.s.combine(4, 2)[0][0], 99)


if __name__ == "__main__":
    unittest.main()

# Tags: Backtracking
