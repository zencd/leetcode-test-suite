# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Easy

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestClimbStairs(unittest.TestCase):
    def test_n_1(self):
        self.assertEqual(Solution().climbStairs(1), 1)

    def test_n_2(self):
        self.assertEqual(Solution().climbStairs(2), 2)

    def test_n_3(self):
        self.assertEqual(Solution().climbStairs(3), 3)

    def test_n_4(self):
        self.assertEqual(Solution().climbStairs(4), 5)

    def test_n_5(self):
        self.assertEqual(Solution().climbStairs(5), 8)

    def test_n_10(self):
        self.assertEqual(Solution().climbStairs(10), 89)

    def test_n_20(self):
        self.assertEqual(Solution().climbStairs(20), 10946)

    def test_n_30(self):
        self.assertEqual(Solution().climbStairs(30), 1346269)

    def test_n_45(self):
        self.assertEqual(Solution().climbStairs(45), 1836311903)

    def test_matches_fibonacci(self):
        expected: List[int] = [1, 1]
        for _ in range(44):
            expected.append(expected[-1] + expected[-2])
        for n in range(1, 46):
            self.assertEqual(Solution().climbStairs(n), expected[n], f"n={n}")

    def test_multiple_instances(self):
        s1 = Solution()
        s2 = Solution()
        for n in range(1, 46):
            self.assertEqual(s1.climbStairs(n), s2.climbStairs(n))


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Memoization
