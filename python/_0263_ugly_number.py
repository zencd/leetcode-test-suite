# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/
# Easy

class Solution:
    def isUgly(self, n: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isUgly(6))
        self.assertTrue(self.sol.isUgly(1))
        self.assertFalse(self.sol.isUgly(14))

    def test_ugly_numbers(self):
        for n in (
            2,
            3,
            4,
            5,
            8,
            9,
            10,
            12,
            15,
            16,
            18,
            20,
            24,
            25,
            27,
            30,
            32,
            36,
            40,
            45,
            48,
            50,
            60,
            75,
            100,
            125,
            243,
            2**30,
            5**10,
        ):
            self.assertTrue(self.sol.isUgly(n), f"{n} should be ugly")

    def test_non_ugly_positive_numbers(self):
        for n in (
            7,
            11,
            13,
            14,
            17,
            19,
            21,
            22,
            23,
            26,
            28,
            33,
            34,
            35,
            37,
            39,
            42,
            44,
            46,
            47,
            49,
            91,
            98,
            105,
            7**4,
            2**31 - 1,
        ):
            self.assertFalse(self.sol.isUgly(n), f"{n} should not be ugly")

    def test_zero(self):
        self.assertFalse(self.sol.isUgly(0))

    def test_negative_numbers(self):
        for n in (-1, -2, -6, -14, -100, -(2**31)):
            self.assertFalse(self.sol.isUgly(n), f"{n} should not be ugly")


if __name__ == "__main__":
    unittest.main()

# Tags: Math
