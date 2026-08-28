# 375. Guess Number Higher or Lower II
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# Medium

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n_1(self):
        self.assertEqual(self.sol.getMoneyAmount(1), 0)

    def test_n_2(self):
        self.assertEqual(self.sol.getMoneyAmount(2), 1)

    def test_n_3(self):
        self.assertEqual(self.sol.getMoneyAmount(3), 2)

    def test_n_4(self):
        self.assertEqual(self.sol.getMoneyAmount(4), 4)

    def test_n_5(self):
        self.assertEqual(self.sol.getMoneyAmount(5), 6)

    def test_n_10(self):
        self.assertEqual(self.sol.getMoneyAmount(10), 16)

    def test_n_200(self):
        self.assertGreater(self.sol.getMoneyAmount(200), 0)

    def test_brute_force_cross_check(self):
        def brute(n):
            memo = {}

            def f(lo, hi):
                if lo >= hi:
                    return 0
                if (lo, hi) in memo:
                    return memo[(lo, hi)]
                best = float("inf")
                for mid in range(lo, hi):
                    best = min(best, mid + max(f(lo, mid - 1), f(mid + 1, hi)))
                memo[(lo, hi)] = best
                return best

            return f(1, n)

        for n in range(1, 13):
            self.assertEqual(self.sol.getMoneyAmount(n), brute(n), f"mismatch at n={n}")

    def test_monotonic_nondecreasing(self):
        prev = 0
        for n in range(1, 31):
            cur = self.sol.getMoneyAmount(n)
            self.assertGreaterEqual(cur, prev)
            prev = cur

    def test_type(self):
        self.assertIsInstance(self.sol.getMoneyAmount(10), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Minimax, Game Theory
