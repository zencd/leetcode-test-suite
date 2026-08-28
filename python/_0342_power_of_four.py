# 342. Power of Four
# https://leetcode.com/problems/power-of-four/
# Easy

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isPowerOfFour(16))
        self.assertFalse(self.sol.isPowerOfFour(5))
        self.assertTrue(self.sol.isPowerOfFour(1))

    def test_powers_of_four_true(self):
        x = 0
        while 4**x <= 2**31 - 1:
            self.assertTrue(self.sol.isPowerOfFour(4**x), msg=4**x)
            x += 1

    def test_negative_and_zero(self):
        self.assertFalse(self.sol.isPowerOfFour(0))
        self.assertFalse(self.sol.isPowerOfFour(-1))
        self.assertFalse(self.sol.isPowerOfFour(-16))
        self.assertFalse(self.sol.isPowerOfFour(-4))
        self.assertFalse(self.sol.isPowerOfFour(-(2**31)))

    def test_powers_of_two_but_not_four(self):
        for n in (2, 8, 32, 128, 512):
            self.assertFalse(self.sol.isPowerOfFour(n), msg=n)

    def test_powers_of_three(self):
        for n in (3, 9, 27, 81):
            self.assertFalse(self.sol.isPowerOfFour(n), msg=n)

    def test_other_values(self):
        for n in (4, 40, 63, 64, 255, 256, 1000, 4096, 65535, 65536):
            expected = n in {
                i
                for i in (
                    1,
                    4,
                    16,
                    64,
                    256,
                    1024,
                    4096,
                    16384,
                    65536,
                    262144,
                    1048576,
                    4194304,
                    16777216,
                    67108864,
                )
            }
            self.assertEqual(self.sol.isPowerOfFour(n), expected, msg=n)

    def test_boundary(self):
        self.assertFalse(self.sol.isPowerOfFour(2**31 - 1))
        self.assertFalse(self.sol.isPowerOfFour(-(2**31)))
        self.assertTrue(self.sol.isPowerOfFour(4**15))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Bit Manipulation, Recursion
