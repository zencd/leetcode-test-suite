# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Easy

class Solution:
    def mySqrt(self, x: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero(self):
        self.assertEqual(self.solution.mySqrt(0), 0)

    def test_one(self):
        self.assertEqual(self.solution.mySqrt(1), 1)

    def test_two(self):
        self.assertEqual(self.solution.mySqrt(2), 1)

    def test_three(self):
        self.assertEqual(self.solution.mySqrt(3), 1)

    def test_four(self):
        self.assertEqual(self.solution.mySqrt(4), 2)

    def test_eight(self):
        self.assertEqual(self.solution.mySqrt(8), 2)

    def test_nine(self):
        self.assertEqual(self.solution.mySqrt(9), 3)

    def test_ten(self):
        self.assertEqual(self.solution.mySqrt(10), 3)

    def test_fifteen(self):
        self.assertEqual(self.solution.mySqrt(15), 3)

    def test_sixteen(self):
        self.assertEqual(self.solution.mySqrt(17), 4)

    def test_square_fifty(self):
        self.assertEqual(self.solution.mySqrt(25), 5)

    def test_square_hundred(self):
        self.assertEqual(self.solution.mySqrt(100), 10)

    def test_square_one_thousand(self):
        self.assertEqual(self.solution.mySqrt(1000000), 1000)

    def test_max_int(self):
        self.assertEqual(self.solution.mySqrt(2**31 - 1), 46340)

    def test_max_int_minus_one(self):
        self.assertEqual(self.solution.mySqrt(2**31 - 2), 46340)

    def test_boundary_between_squares(self):
        self.assertEqual(self.solution.mySqrt(46340 * 46340 + 1), 46340)
        self.assertEqual(self.solution.mySqrt(46341 * 46341 - 1), 46340)

    def test_exact_square_boundary(self):
        self.assertEqual(self.solution.mySqrt(46340 * 46340), 46340)

    def test_small_range(self):
        expected = [0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        for value, want in enumerate(expected):
            self.assertEqual(self.solution.mySqrt(value), want)

    def test_no_builtin_exponent_used(self):
        import inspect

        source = inspect.getsource(self.solution.mySqrt)
        self.assertNotIn("**", source)
        self.assertNotIn("pow", source)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Binary Search, Newton's Method
