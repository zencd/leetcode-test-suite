# 204. Count Primes
# https://leetcode.com/problems/count-primes/
# Medium

class Solution:
    def countPrimes(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_zero(self):
        self.assertEqual(self.solution.countPrimes(0), 0)

    def test_n_one(self):
        self.assertEqual(self.solution.countPrimes(1), 0)

    def test_n_two(self):
        self.assertEqual(self.solution.countPrimes(2), 0)

    def test_n_three(self):
        self.assertEqual(self.solution.countPrimes(3), 1)

    def test_n_four(self):
        self.assertEqual(self.solution.countPrimes(4), 2)

    def test_n_five(self):
        self.assertEqual(self.solution.countPrimes(5), 2)

    def test_n_ten(self):
        self.assertEqual(self.solution.countPrimes(10), 4)

    def test_n_twelve(self):
        self.assertEqual(self.solution.countPrimes(12), 5)

    def test_n_twenty(self):
        self.assertEqual(self.solution.countPrimes(20), 8)

    def test_n_fifty(self):
        self.assertEqual(self.solution.countPrimes(50), 15)

    def test_n_hundred(self):
        self.assertEqual(self.solution.countPrimes(100), 25)

    def test_n_hundred_thousand(self):
        self.assertEqual(self.solution.countPrimes(100000), 9592)

    def test_n_one_million(self):
        self.assertEqual(self.solution.countPrimes(1000000), 78498)

    def test_large_prime_bound(self):
        self.assertEqual(self.solution.countPrimes(17), 6)

    def test_exact_prime_excluded(self):
        self.assertEqual(self.solution.countPrimes(7), 3)

    def test_constraint_upper_bound(self):
        self.assertEqual(self.solution.countPrimes(5000000), 348513)

    def test_returns_int(self):
        self.assertIsInstance(self.solution.countPrimes(10), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Enumeration, Number Theory, Primality Test, Sieve Theory, Prime Number Sieve
