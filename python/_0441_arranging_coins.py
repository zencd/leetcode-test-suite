# 441. Arranging Coins
# https://leetcode.com/problems/arranging-coins/
# Easy

class Solution:
    def arrangeCoins(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.arrangeCoins(5), 2)

    def test_example_2(self):
        self.assertEqual(self.sol.arrangeCoins(8), 3)

    def test_minimum(self):
        self.assertEqual(self.sol.arrangeCoins(1), 1)

    def test_exact_triangular(self):
        self.assertEqual(self.sol.arrangeCoins(3), 2)
        self.assertEqual(self.sol.arrangeCoins(6), 3)
        self.assertEqual(self.sol.arrangeCoins(10), 4)
        self.assertEqual(self.sol.arrangeCoins(55), 10)
        self.assertEqual(self.sol.arrangeCoins(5050), 100)

    def test_just_below_triangular(self):
        self.assertEqual(self.sol.arrangeCoins(2), 1)
        self.assertEqual(self.sol.arrangeCoins(5), 2)
        self.assertEqual(self.sol.arrangeCoins(9), 3)
        self.assertEqual(self.sol.arrangeCoins(54), 9)
        self.assertEqual(self.sol.arrangeCoins(5049), 99)

    def test_sequential_small_values(self):
        expected = {
            1: 1,
            2: 1,
            3: 2,
            4: 2,
            5: 2,
            6: 3,
            7: 3,
            8: 3,
            9: 3,
            10: 4,
            11: 4,
            15: 5,
            16: 5,
        }
        for n, exp in expected.items():
            self.assertEqual(self.sol.arrangeCoins(n), exp, f"failed for n={n}")

    def test_large_max_constraint(self):
        self.assertEqual(self.sol.arrangeCoins(2**31 - 1), 65535)

    def test_large_values(self):
        k = 32767
        n_exact = k * (k + 1) // 2
        self.assertEqual(self.sol.arrangeCoins(n_exact), k)
        self.assertEqual(self.sol.arrangeCoins(n_exact + 1), k)
        self.assertEqual(self.sol.arrangeCoins(n_exact - 1), k - 1)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Binary Search
