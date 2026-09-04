# 478. Generate Random Point in a Circle
# https://leetcode.com/problems/generate-random-point-in-a-circle/
# Medium

import math
import random
import unittest
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        raise Exception("Not solved yet")

    def randPoint(self) -> List[float]:
        raise Exception("Not solved yet")


class TestSolution(unittest.TestCase):
    def test_stores_parameters(self):
        s = Solution(1.5, -2.0, 3.25)
        self.assertEqual(s.radius, 1.5)
        self.assertEqual(s.x_center, -2.0)
        self.assertEqual(s.y_center, 3.25)

    def test_returns_list_of_two_floats(self):
        s = Solution(1.0, 0.0, 0.0)
        p = s.randPoint()
        self.assertIsInstance(p, list)
        self.assertEqual(len(p), 2)
        self.assertIsInstance(p[0], float)
        self.assertIsInstance(p[1], float)

    def test_all_points_inside_circle(self):
        random.seed(42)
        R, cx, cy = 5.0, 1.5, -2.5
        s = Solution(R, cx, cy)
        for _ in range(20000):
            x, y = s.randPoint()
            d = math.hypot(x - cx, y - cy)
            self.assertLessEqual(d, R + 1e-9)

    def test_reaches_near_boundary(self):
        random.seed(1)
        R = 10.0
        s = Solution(R, 0.0, 0.0)
        maxd = 0.0
        for _ in range(300000):
            x, y = s.randPoint()
            maxd = max(maxd, math.hypot(x, y))
        self.assertGreater(maxd, 0.999 * R)

    def test_quadrant_distribution(self):
        random.seed(7)
        R = 2.0
        s = Solution(R, 0.0, 0.0)
        counts = [0, 0, 0, 0]
        n = 40000
        for _ in range(n):
            x, y = s.randPoint()
            if x >= 0 and y >= 0:
                counts[0] += 1
            elif x < 0 and y >= 0:
                counts[1] += 1
            elif x < 0 and y < 0:
                counts[2] += 1
            else:
                counts[3] += 1
        expected = n / 4.0
        for c in counts:
            self.assertAlmostEqual(c, expected, delta=n * 0.12)

    def test_mean_near_center(self):
        random.seed(99)
        cx, cy = 100.0, -50.0
        s = Solution(3.0, cx, cy)
        n = 50000
        sx = sy = 0.0
        for _ in range(n):
            x, y = s.randPoint()
            sx += x
            sy += y
        self.assertAlmostEqual(sx / n, cx, places=1)
        self.assertAlmostEqual(sy / n, cy, places=1)

    def test_variance(self):
        random.seed(123)
        R = 4.0
        s = Solution(R, 0.0, 0.0)
        n = 60000
        sumx = sumy = sumx2 = sumy2 = 0.0
        for _ in range(n):
            x, y = s.randPoint()
            sumx += x
            sumy += y
            sumx2 += x * x
            sumy2 += y * y
        mx = sumx / n
        my = sumy / n
        vx = sumx2 / n - mx * mx
        vy = sumy2 / n - my * my
        expected = R * R / 4.0
        self.assertAlmostEqual(vx, expected, delta=expected * 0.2)
        self.assertAlmostEqual(vy, expected, delta=expected * 0.2)

    def test_large_radius(self):
        random.seed(5)
        R = 1e8
        s = Solution(R, 0.0, 0.0)
        for _ in range(2000):
            x, y = s.randPoint()
            self.assertLessEqual(math.hypot(x, y), R * (1 + 1e-6))

    def test_small_radius(self):
        random.seed(6)
        R = 1e-6
        cx = cy = 5.0
        s = Solution(R, cx, cy)
        for _ in range(2000):
            x, y = s.randPoint()
            self.assertLessEqual(math.hypot(x - cx, y - cy), R * (1 + 1e-6))

    def test_extreme_coordinates(self):
        cx = cy = 1e7
        R = 1e8
        s = Solution(R, cx, cy)
        for _ in range(1000):
            x, y = s.randPoint()
            self.assertLessEqual(math.hypot(x - cx, y - cy), R * (1 + 1e-6))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Geometry, Rejection Sampling, Randomized
