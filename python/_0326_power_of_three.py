# 326. Power of Three
# https://leetcode.com/problems/power-of-three/
# Easy

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isPowerOfThree(27))
        self.assertFalse(self.sol.isPowerOfThree(0))
        self.assertFalse(self.sol.isPowerOfThree(-1))

    def test_powers(self):
        n = 1
        for x in range(20):
            self.assertTrue(self.sol.isPowerOfThree(n), f"3^{x}")
            n *= 3

    def test_non_powers(self):
        for n in (
            2,
            3 + 1,
            4,
            5,
            6,
            7,
            8,
            9 + 1,
            10,
            11,
            12,
            14,
            15,
            16,
            25,
            26,
            28,
            29,
            30,
            80,
            81 + 1,
            100,
        ):
            self.assertFalse(self.sol.isPowerOfThree(n), f"{n}")

    def test_zero(self):
        self.assertFalse(self.sol.isPowerOfThree(0))

    def test_negatives(self):
        for n in (-1, -3, -9, -27, -100, -(2**31)):
            self.assertFalse(self.sol.isPowerOfThree(n))

    def test_boundary(self):
        self.assertFalse(self.sol.isPowerOfThree(2**31 - 1))
        self.assertTrue(self.sol.isPowerOfThree(3**19))
        self.assertFalse(self.sol.isPowerOfThree(3**19 + 1))
        self.assertFalse(self.sol.isPowerOfThree(-(2**31)))

    def test_divisors_of_max_power_not_powers(self):
        for n in (1162261467 // 2, 1162261467 // 7):
            self.assertFalse(self.sol.isPowerOfThree(n))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Recursion
