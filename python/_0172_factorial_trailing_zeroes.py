# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/
# Medium

class Solution:
    def trailingZeroes(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(Solution().trailingZeroes(0), 0)

    def test_below_five(self):
        for n in range(1, 5):
            self.assertEqual(Solution().trailingZeroes(n), 0)

    def test_five(self):
        self.assertEqual(Solution().trailingZeroes(5), 1)

    def test_six(self):
        self.assertEqual(Solution().trailingZeroes(6), 1)

    def test_nine(self):
        self.assertEqual(Solution().trailingZeroes(9), 1)

    def test_ten(self):
        self.assertEqual(Solution().trailingZeroes(10), 2)

    def test_twenty_four(self):
        self.assertEqual(Solution().trailingZeroes(24), 4)

    def test_twenty_five(self):
        self.assertEqual(Solution().trailingZeroes(25), 6)

    def test_fifty(self):
        self.assertEqual(Solution().trailingZeroes(50), 12)

    def test_bigger_blocks(self):
        self.assertEqual(Solution().trailingZeroes(100), 24)
        self.assertEqual(Solution().trailingZeroes(125), 31)
        self.assertEqual(Solution().trailingZeroes(1000), 249)

    def test_max_constraint(self):
        self.assertEqual(Solution().trailingZeroes(10000), 2499)

    def test_monotonicity(self):
        results = [Solution().trailingZeroes(n) for n in range(200)]
        self.assertEqual(results, sorted(results))


if __name__ == "__main__":
    unittest.main()

# Tags: Math
