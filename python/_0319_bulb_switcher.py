# 319. Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/
# Medium

import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero(self):
        self.assertEqual(self.solution.bulbSwitch(0), 0)

    def test_one(self):
        self.assertEqual(self.solution.bulbSwitch(1), 1)

    def test_two(self):
        self.assertEqual(self.solution.bulbSwitch(2), 1)

    def test_three(self):
        self.assertEqual(self.solution.bulbSwitch(3), 1)

    def test_four(self):
        self.assertEqual(self.solution.bulbSwitch(4), 2)

    def test_five(self):
        self.assertEqual(self.solution.bulbSwitch(5), 2)

    def test_six(self):
        self.assertEqual(self.solution.bulbSwitch(6), 2)

    def test_seven(self):
        self.assertEqual(self.solution.bulbSwitch(7), 2)

    def test_eight(self):
        self.assertEqual(self.solution.bulbSwitch(8), 2)

    def test_nine(self):
        self.assertEqual(self.solution.bulbSwitch(9), 3)

    def test_teen(self):
        self.assertEqual(self.solution.bulbSwitch(16), 4)

    def test_twenty_five(self):
        self.assertEqual(self.solution.bulbSwitch(25), 5)

    def test_perfect_square_boundary(self):
        self.assertEqual(self.solution.bulbSwitch(10**8), 10**4)

    def test_minus_one_of_perfect_square(self):
        self.assertEqual(self.solution.bulbSwitch(10**8 - 1), 9999)

    def test_max_constraint(self):
        self.assertEqual(self.solution.bulbSwitch(10**9), 31622)

    def test_return_type_is_int(self):
        self.assertIsInstance(self.solution.bulbSwitch(3), int)

    def test_matches_brute_force(self):
        def brute_force(n):
            bulbs = [False] * (n + 1)
            for i in range(1, n + 1):
                for j in range(i, n + 1, i):
                    bulbs[j] = not bulbs[j]
            return sum(bulbs[1:])

        for n in range(0, 101):
            with self.subTest(n=n):
                self.assertEqual(self.solution.bulbSwitch(n), brute_force(n))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Brainteaser
