# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/
# Easy

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isPerfectSquare(16))
        self.assertFalse(self.sol.isPerfectSquare(14))

    def test_small_squares(self):
        for i in range(1, 27):
            self.assertTrue(self.sol.isPerfectSquare(i * i), f"{i * i}")
        for n in [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22]:
            self.assertFalse(self.sol.isPerfectSquare(n), f"{n}")

    def test_single_digit(self):
        expected = {
            1: True,
            2: False,
            3: False,
            4: True,
            5: False,
            6: False,
            7: False,
            8: False,
            9: True,
        }
        for num, ans in expected.items():
            self.assertEqual(self.sol.isPerfectSquare(num), ans, f"num={num}")

    def test_one(self):
        self.assertTrue(self.sol.isPerfectSquare(1))

    def test_large_square(self):
        n = 46340
        self.assertTrue(self.sol.isPerfectSquare(n * n))

    def test_max_constraint_range(self):
        self.assertTrue(self.sol.isPerfectSquare(46340 * 46340))
        self.assertFalse(self.sol.isPerfectSquare(46340 * 46340 + 1))
        self.assertFalse(self.sol.isPerfectSquare(2**31 - 1))

    def test_values_around_squares(self):
        for base in [1, 2, 10, 46340]:
            sq = base * base
            if sq - 1 >= 1:
                self.assertFalse(self.sol.isPerfectSquare(sq - 1), f"{sq - 1}")
            self.assertTrue(self.sol.isPerfectSquare(sq), f"{sq}")
            if sq + 1 <= 2**31 - 1:
                self.assertFalse(self.sol.isPerfectSquare(sq + 1), f"{sq + 1}")

    def test_no_sqrt_used(self):
        import inspect

        src = inspect.getsource(Solution.isPerfectSquare)
        self.assertNotIn("sqrt", src)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Binary Search
