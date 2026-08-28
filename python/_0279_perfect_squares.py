# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/
# Medium

class Solution:
    def numSquares(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n_equals_1(self):
        self.assertEqual(self.sol.numSquares(1), 1)

    def test_n_equals_2(self):
        self.assertEqual(self.sol.numSquares(2), 2)

    def test_n_equals_3(self):
        self.assertEqual(self.sol.numSquares(3), 3)

    def test_n_equals_4(self):
        self.assertEqual(self.sol.numSquares(4), 1)

    def test_n_equals_5(self):
        self.assertEqual(self.sol.numSquares(5), 2)

    def test_n_equals_7(self):
        self.assertEqual(self.sol.numSquares(7), 4)

    def test_n_equals_8(self):
        self.assertEqual(self.sol.numSquares(8), 2)

    def test_n_equals_12(self):
        self.assertEqual(self.sol.numSquares(12), 3)

    def test_n_equals_13(self):
        self.assertEqual(self.sol.numSquares(13), 2)

    def test_perfect_squares(self):
        for k in range(1, 101):
            self.assertEqual(self.sol.numSquares(k * k), 1)

    def test_sum_of_two_squares(self):
        self.assertEqual(self.sol.numSquares(25 + 36), 2)
        self.assertEqual(self.sol.numSquares(36 + 81), 2)
        self.assertEqual(self.sol.numSquares(9 + 100), 2)

    def test_four_required(self):
        self.assertEqual(self.sol.numSquares(15), 4)
        self.assertEqual(self.sol.numSquares(23), 4)
        self.assertEqual(self.sol.numSquares(31), 4)
        self.assertEqual(self.sol.numSquares(76), 3)
        self.assertEqual(self.sol.numSquares(9999), 4)

    def test_larger_values(self):
        self.assertEqual(self.sol.numSquares(100), 1)
        self.assertEqual(self.sol.numSquares(101), 2)
        self.assertEqual(self.sol.numSquares(999), 4)
        self.assertEqual(self.sol.numSquares(5000), 2)
        self.assertEqual(self.sol.numSquares(10000), 1)

    def test_brute_force_cross_check(self):
        def is_square(x):
            r = int(x**0.5)
            return r * r == x or (r + 1) * (r + 1) == x

        def expected(n):
            if is_square(n):
                return 1
            for a in range(1, int(n**0.5) + 1):
                if is_square(n - a * a):
                    return 2
            for a in range(1, int(n**0.5) + 1):
                for b in range(a, int((n - a * a) ** 0.5) + 1):
                    if is_square(n - a * a - b * b):
                        return 3
            return 4

        for n in range(1, 400):
            self.assertEqual(self.sol.numSquares(n), expected(n), f"mismatch at n={n}")


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack
