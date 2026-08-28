# 365. Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/
# Medium

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.canMeasureWater(3, 5, 4))
        self.assertFalse(self.sol.canMeasureWater(2, 6, 5))
        self.assertTrue(self.sol.canMeasureWater(1, 2, 3))

    def test_zero_target(self):
        self.assertTrue(self.sol.canMeasureWater(1, 1, 0))
        self.assertTrue(self.sol.canMeasureWater(1000, 1, 0))
        self.assertTrue(self.sol.canMeasureWater(3, 5, 0))

    def test_target_exceeds_total_capacity(self):
        self.assertFalse(self.sol.canMeasureWater(1, 2, 4))
        self.assertFalse(self.sol.canMeasureWater(3, 5, 9))
        self.assertFalse(self.sol.canMeasureWater(1000, 1000, 2001))

    def test_target_equals_total_capacity(self):
        self.assertTrue(self.sol.canMeasureWater(3, 5, 8))
        self.assertTrue(self.sol.canMeasureWater(1, 1, 2))
        self.assertTrue(self.sol.canMeasureWater(1000, 1000, 2000))

    def test_target_in_single_jug(self):
        self.assertTrue(self.sol.canMeasureWater(3, 5, 3))
        self.assertTrue(self.sol.canMeasureWater(3, 5, 5))
        self.assertTrue(self.sol.canMeasureWater(1, 2, 1))
        self.assertTrue(self.sol.canMeasureWater(1, 2, 2))

    def test_target_one(self):
        self.assertFalse(self.sol.canMeasureWater(2, 4, 1))
        self.assertTrue(self.sol.canMeasureWater(3, 5, 1))
        self.assertTrue(self.sol.canMeasureWater(1, 1000, 1))

    def test_both_jugs_equal(self):
        self.assertTrue(self.sol.canMeasureWater(5, 5, 5))
        self.assertTrue(self.sol.canMeasureWater(5, 5, 10))
        self.assertFalse(self.sol.canMeasureWater(5, 5, 7))

    def test_gcd_divisibility(self):
        self.assertFalse(self.sol.canMeasureWater(6, 10, 5))
        self.assertTrue(self.sol.canMeasureWater(6, 10, 2))
        self.assertTrue(self.sol.canMeasureWater(6, 10, 8))
        self.assertTrue(self.sol.canMeasureWater(6, 10, 10))
        self.assertFalse(self.sol.canMeasureWater(4, 6, 3))
        self.assertTrue(self.sol.canMeasureWater(4, 6, 2))
        self.assertFalse(self.sol.canMeasureWater(4, 6, 5))

    def test_one_jug_capacity_one(self):
        self.assertTrue(self.sol.canMeasureWater(1, 1000, 345))
        self.assertTrue(self.sol.canMeasureWater(1, 1000, 1000))
        self.assertFalse(self.sol.canMeasureWater(1, 1000, 1002))

    def test_symmetry(self):
        for x, y, t in [(3, 5, 4), (2, 6, 5), (1, 2, 3), (7, 11, 6), (7, 11, 1)]:
            self.assertEqual(
                self.sol.canMeasureWater(x, y, t),
                self.sol.canMeasureWater(y, x, t),
                f"symmetry failed for {x},{y},{t}",
            )

    def test_boundary_values(self):
        self.assertTrue(self.sol.canMeasureWater(1, 1, 1))
        self.assertFalse(self.sol.canMeasureWater(1000, 1000, 500))
        self.assertFalse(self.sol.canMeasureWater(1000, 1000, 999))
        self.assertTrue(self.sol.canMeasureWater(1000, 999, 1))
        self.assertTrue(self.sol.canMeasureWater(2, 1000, 500))

    def test_measure_all_achievable_small_cases(self):
        from collections import deque

        def brute(x, y, target):
            if target == 0:
                return True
            if target > x + y:
                return False
            seen = {(0, 0)}
            q = deque([(0, 0)])
            while q:
                a, b = q.popleft()
                if a + b == target:
                    return True
                states = [
                    (x, b),
                    (a, y),
                    (0, b),
                    (a, 0),
                    (a - min(a, y - b), b + min(a, y - b)),
                    (a + min(b, x - a), b - min(b, x - a)),
                ]
                for s in states:
                    if s not in seen:
                        seen.add(s)
                        q.append(s)
            return False

        for x in range(1, 13):
            for y in range(1, 13):
                for t in range(0, x + y + 2):
                    self.assertEqual(
                        self.sol.canMeasureWater(x, y, t),
                        brute(x, y, t),
                        f"mismatch for x={x}, y={y}, target={t}",
                    )


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Depth-First Search, Breadth-First Search, Bézout's Lemma, Euclidean Algorithm, Greatest Common Divisor, Extended Euclidean Algorithm
