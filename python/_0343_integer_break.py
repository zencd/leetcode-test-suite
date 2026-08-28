# 343. Integer Break
# https://leetcode.com/problems/integer-break/
# Medium

class Solution:
    def integerBreak(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n_2(self):
        self.assertEqual(self.sol.integerBreak(2), 1)

    def test_n_3(self):
        self.assertEqual(self.sol.integerBreak(3), 2)

    def test_n_4(self):
        self.assertEqual(self.sol.integerBreak(4), 4)

    def test_n_5(self):
        self.assertEqual(self.sol.integerBreak(5), 6)

    def test_n_6(self):
        self.assertEqual(self.sol.integerBreak(6), 9)

    def test_n_7(self):
        self.assertEqual(self.sol.integerBreak(7), 12)

    def test_n_8(self):
        self.assertEqual(self.sol.integerBreak(8), 18)

    def test_n_9(self):
        self.assertEqual(self.sol.integerBreak(9), 27)

    def test_n_10(self):
        self.assertEqual(self.sol.integerBreak(10), 36)

    def test_n_11(self):
        self.assertEqual(self.sol.integerBreak(11), 54)

    def test_n_12(self):
        self.assertEqual(self.sol.integerBreak(12), 81)

    def test_n_20(self):
        self.assertEqual(self.sol.integerBreak(20), 1458)

    def test_n_23(self):
        self.assertEqual(self.sol.integerBreak(23), 4374)

    def test_n_25(self):
        self.assertEqual(self.sol.integerBreak(25), 8748)

    def test_max_n_58(self):
        self.assertEqual(self.sol.integerBreak(58), 1549681956)

    def test_monotonic_increasing(self):
        prev = self.sol.integerBreak(2)
        for n in range(3, 59):
            cur = self.sol.integerBreak(n)
            self.assertGreater(cur, prev)
            prev = cur


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming
