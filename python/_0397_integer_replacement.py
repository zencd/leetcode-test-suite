# 397. Integer Replacement
# https://leetcode.com/problems/integer-replacement/
# Medium

class Solution:
    def integerReplacement(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_equals_one(self):
        self.assertEqual(self.solution.integerReplacement(1), 0)

    def test_examples(self):
        self.assertEqual(self.solution.integerReplacement(8), 3)
        self.assertEqual(self.solution.integerReplacement(7), 4)
        self.assertEqual(self.solution.integerReplacement(4), 2)

    def test_specific_cases(self):
        self.assertEqual(self.solution.integerReplacement(2), 1)
        self.assertEqual(self.solution.integerReplacement(3), 2)
        self.assertEqual(self.solution.integerReplacement(5), 3)
        self.assertEqual(self.solution.integerReplacement(6), 3)
        self.assertEqual(self.solution.integerReplacement(9), 4)
        self.assertEqual(self.solution.integerReplacement(15), 5)
        self.assertEqual(self.solution.integerReplacement(21), 6)
        self.assertEqual(self.solution.integerReplacement(23), 6)
        self.assertEqual(self.solution.integerReplacement(25), 6)
        self.assertEqual(self.solution.integerReplacement(47), 7)
        self.assertEqual(self.solution.integerReplacement(1023), 11)
        self.assertEqual(self.solution.integerReplacement(1025), 11)

    def test_powers_of_two(self):
        for i in range(1, 31):
            self.assertEqual(self.solution.integerReplacement(2**i), i)

    def test_ones_mask(self):
        for i in list(range(3, 28)):
            self.assertEqual(self.solution.integerReplacement(2**i - 1), i + 1)

    def test_max_constraint(self):
        self.assertEqual(self.solution.integerReplacement(2**31 - 1), 32)

    def test_monotonicity_checks(self):
        self.assertEqual(self.solution.integerReplacement(2**10 + 1), 11)
        self.assertEqual(self.solution.integerReplacement(2**10 - 1), 11)

    def test_matches_dp(self):
        def dp(n):
            memo = {1: 0}

            def go(x):
                if x in memo:
                    return memo[x]
                if x % 2 == 0:
                    r = go(x // 2) + 1
                else:
                    r = min(go(x - 1), go(x + 1)) + 1
                memo[x] = r
                return r

            return go(n)

        for n in range(1, 500):
            self.assertEqual(self.solution.integerReplacement(n), dp(n))


if __name__ == "__main__":
    unittest.main()

# Tags: Dynamic Programming, Greedy, Bit Manipulation, Memoization
