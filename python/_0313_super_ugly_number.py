# 313. Super Ugly Number
# https://leetcode.com/problems/super-ugly-number/
# Medium

from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example_1(self):
        self.assertEqual(self.s.nthSuperUglyNumber(12, [2, 7, 13, 19]), 32)

    def test_example_2_first_number(self):
        self.assertEqual(self.s.nthSuperUglyNumber(1, [2, 3, 5]), 1)

    def test_first_number_always_one(self):
        self.assertEqual(self.s.nthSuperUglyNumber(1, [2]), 1)
        self.assertEqual(self.s.nthSuperUglyNumber(1, [997]), 1)

    def test_single_prime_two(self):
        seq = [1, 2, 4, 8, 16, 32, 64]
        for i in range(1, len(seq) + 1):
            self.assertEqual(self.s.nthSuperUglyNumber(i, [2]), seq[i - 1])

    def test_single_prime_three(self):
        seq = [1, 3, 9, 27, 81]
        for i in range(1, len(seq) + 1):
            self.assertEqual(self.s.nthSuperUglyNumber(i, [3]), seq[i - 1])

    def test_single_prime_larger(self):
        seq = [1, 7, 49, 343, 2401, 16807]
        for i in range(1, len(seq) + 1):
            self.assertEqual(self.s.nthSuperUglyNumber(i, [7]), seq[i - 1])

    def test_two_primes(self):
        seq = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18]
        for i in range(1, len(seq) + 1):
            self.assertEqual(self.s.nthSuperUglyNumber(i, [2, 3]), seq[i - 1])

    def test_classic_ugly_2_3_5(self):
        seq = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
        for i in range(1, len(seq) + 1):
            self.assertEqual(self.s.nthSuperUglyNumber(i, [2, 3, 5]), seq[i - 1])

    def test_primes_2_5(self):
        seq = [1, 2, 4, 5, 8, 10, 16, 20, 25]
        for i in range(1, len(seq) + 1):
            self.assertEqual(self.s.nthSuperUglyNumber(i, [2, 5]), seq[i - 1])

    def test_larger_n_32bit_bound(self):
        self.assertEqual(self.s.nthSuperUglyNumber(1690, [2, 3, 5]), 2123366400)

    def test_primes_large_value(self):
        self.assertEqual(self.s.nthSuperUglyNumber(1, [997]), 1)
        self.assertEqual(self.s.nthSuperUglyNumber(2, [997]), 997)
        self.assertEqual(self.s.nthSuperUglyNumber(3, [997]), 997 * 997)

    def test_n_equals_two_single_prime(self):
        self.assertEqual(self.s.nthSuperUglyNumber(2, [11]), 11)


if __name__ == "__main__":
    unittest.main()

# Tags: Array, Math, Dynamic Programming
