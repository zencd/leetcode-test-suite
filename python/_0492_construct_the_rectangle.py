# 492. Construct the Rectangle
# https://leetcode.com/problems/construct-the-rectangle/
# Easy

from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_area_1(self):
        self.assertEqual(self.sol.constructRectangle(1), [1, 1])

    def test_area_2(self):
        self.assertEqual(self.sol.constructRectangle(2), [2, 1])

    def test_area_3(self):
        self.assertEqual(self.sol.constructRectangle(3), [3, 1])

    def test_area_4(self):
        self.assertEqual(self.sol.constructRectangle(4), [2, 2])

    def test_area_12(self):
        self.assertEqual(self.sol.constructRectangle(12), [4, 3])

    def test_area_37(self):
        self.assertEqual(self.sol.constructRectangle(37), [37, 1])

    def test_area_100(self):
        self.assertEqual(self.sol.constructRectangle(100), [10, 10])

    def test_area_122122(self):
        self.assertEqual(self.sol.constructRectangle(122122), [427, 286])

    def test_prime_large(self):
        self.assertEqual(self.sol.constructRectangle(9999991), [9999991, 1])

    def test_max_area(self):
        self.assertEqual(self.sol.constructRectangle(10**7), [3200, 3125])

    def test_perfect_square_prime_product(self):
        n = 997 * 991
        self.assertEqual(self.sol.constructRectangle(n), [997, 991])

    def test_area_10000(self):
        self.assertEqual(self.sol.constructRectangle(10000), [100, 100])

    def test_area_81(self):
        self.assertEqual(self.sol.constructRectangle(81), [9, 9])

    def test_area_800(self):
        self.assertEqual(self.sol.constructRectangle(800), [32, 25])

    def test_properties(self):
        for area in range(1, 200):
            l, w = self.sol.constructRectangle(area)
            self.assertEqual(l * w, area, f"area {area}")
            self.assertGreaterEqual(l, w, f"area {area}")


if __name__ == "__main__":
    unittest.main()

# Tags: Math
