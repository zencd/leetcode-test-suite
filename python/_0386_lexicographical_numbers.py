# 386. Lexicographical Numbers
# https://leetcode.com/problems/lexicographical-numbers/
# Medium

import unittest
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        raise Exception("Not solved yet")


def expected(n: int) -> List[int]:
    return sorted(range(1, n + 1), key=str)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_13(self):
        self.assertEqual(
            self.sol.lexicalOrder(13),
            [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
        )

    def test_example_2(self):
        self.assertEqual(self.sol.lexicalOrder(2), [1, 2])

    def test_single(self):
        self.assertEqual(self.sol.lexicalOrder(1), [1])

    def test_ten(self):
        self.assertEqual(self.sol.lexicalOrder(10), [1, 10, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_pow10_boundaries(self):
        for n in (9, 10, 11, 100, 101, 111, 1000, 10000):
            with self.subTest(n=n):
                self.assertEqual(self.sol.lexicalOrder(n), expected(n))

    def test_nines(self):
        for n in (19, 99, 999, 9999):
            with self.subTest(n=n):
                self.assertEqual(self.sol.lexicalOrder(n), expected(n))

    def test_all_digits_nine_endings(self):
        for n in (29, 92, 992):
            with self.subTest(n=n):
                self.assertEqual(self.sol.lexicalOrder(n), expected(n))

    def test_mid_range_random(self):
        import random

        random.seed(386)
        for _ in range(25):
            n = random.randint(1, 50000)
            with self.subTest(n=n):
                self.assertEqual(self.sol.lexicalOrder(n), expected(n))

    def test_max_constraint(self):
        self.assertEqual(self.sol.lexicalOrder(50000), expected(50000))

    def test_full_range_small(self):
        for n in range(1, 51):
            with self.subTest(n=n):
                self.assertEqual(self.sol.lexicalOrder(n), expected(n))

    def test_output_length_and_elements(self):
        res = self.sol.lexicalOrder(13)
        self.assertEqual(len(res), 13)
        self.assertEqual(sorted(res), list(range(1, 14)))

    def test_lexicographic_property(self):
        for n in (13, 100, 1234):
            res = self.sol.lexicalOrder(n)
            self.assertEqual(res, sorted(res, key=str))


if __name__ == "__main__":
    unittest.main()

# Tags: Depth-First Search, Trie
