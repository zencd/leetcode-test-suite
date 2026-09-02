# 497. Random Point in Non-overlapping Rectangles
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Medium

import bisect
import random
import unittest
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        raise Exception("Not solved yet")

    def pick(self) -> List[int]:
        raise Exception("Not solved yet")


from contextlib import contextmanager


@contextmanager
def mock_randint(values):
    orig = random.randint
    it = iter(values)
    random.randint = lambda lo, hi: next(it)
    try:
        yield
    finally:
        random.randint = orig


class TestSolution(unittest.TestCase):
    def test_example_points_within_rects(self):
        sol = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
        for _ in range(200):
            p = sol.pick()
            self.assertTrue((-2 <= p[0] <= 1 and -2 <= p[1] <= 1) or (2 <= p[0] <= 4 and 2 <= p[1] <= 6))

    def test_single_point_rect(self):
        sol = Solution([[5, 7, 5, 7]])
        for _ in range(10):
            self.assertEqual(sol.pick(), [5, 7])

    def test_all_points_covered_small_rect(self):
        sol = Solution([[0, 0, 1, 1]])
        seen = set()
        for _ in range(5000):
            seen.add(tuple(sol.pick()))
        self.assertEqual(seen, {(0, 0), (0, 1), (1, 0), (1, 1)})

    def test_negative_coordinates(self):
        sol = Solution([[-10, -5, -3, 2]])
        for _ in range(200):
            p = sol.pick()
            self.assertTrue(-10 <= p[0] <= -3 and -5 <= p[1] <= 2)

    def test_rect_order_independence(self):
        for seq in ([[0, 0, 0, 0], [1, 1, 1, 1]], [[1, 1, 1, 1], [0, 0, 0, 0]]):
            sol = Solution(seq)
            points = {tuple(sol.pick()) for _ in range(100)}
            self.assertLessEqual(points, {(0, 0), (1, 1)})

    def test_deterministic_with_mocked_random(self):
        sol = Solution([[0, 0, 1, 1], [5, 5, 5, 5]])
        with mock_randint([1, 0, 0]):
            self.assertEqual(sol.pick(), [0, 0])
        with mock_randint([4, 1, 1]):
            self.assertEqual(sol.pick(), [1, 1])
        with mock_randint([5, 5, 5]):
            self.assertEqual(sol.pick(), [5, 5])

    def test_large_coordinates(self):
        lo = -(10**9)
        sol = Solution([[lo, lo, lo + 1, lo + 1]])
        p = sol.pick()
        self.assertTrue(lo <= p[0] <= lo + 1 and lo <= p[1] <= lo + 1)

    def test_max_size_rects(self):
        sol = Solution([[0, 0, 2000, 2000]])
        for _ in range(50):
            p = sol.pick()
            self.assertTrue(0 <= p[0] <= 2000 and 0 <= p[1] <= 2000)

    def test_return_type(self):
        sol = Solution([[-3, -1, 3, 1]])
        p = sol.pick()
        self.assertIsInstance(p, list)
        self.assertEqual(len(p), 2)
        self.assertIsInstance(p[0], int)
        self.assertIsInstance(p[1], int)

    def test_weighted_uniformity_across_rects(self):
        sol = Solution([[0, 0, 1, 1], [5, 5, 5, 5]])
        n0 = n1 = 0
        for _ in range(100000):
            p = sol.pick()
            if p == [5, 5]:
                n1 += 1
            else:
                n0 += 1
        ratio = n0 / n1
        self.assertTrue(3.0 < ratio < 5.0, f"ratio {ratio} not ~4")

    def test_multi_rect_point_validation(self):
        sol = Solution([[-5, -3, -1, 2], [3, 0, 4, 5]])
        for _ in range(500):
            p = sol.pick()
            self.assertTrue((-5 <= p[0] <= -1 and -3 <= p[1] <= 2) or (3 <= p[0] <= 4 and 0 <= p[1] <= 5))

    def test_single_rect_uniformity(self):
        import collections

        sol = Solution([[0, 0, 1, 1]])
        counts = collections.Counter()
        for _ in range(40000):
            counts[tuple(sol.pick())] += 1
        self.assertEqual(len(counts), 4)
        lo, hi = min(counts.values()), max(counts.values())
        self.assertTrue(lo > 6000 and hi < 14000)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Binary Search, Reservoir Sampling, Prefix Sum, Ordered Set, Randomized
