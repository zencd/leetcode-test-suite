# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# Medium

class Solution:
    def getSum(self, a: int, b: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.getSum(1, 2), 3)
        self.assertEqual(self.solution.getSum(2, 3), 5)

    def test_zeros(self):
        self.assertEqual(self.solution.getSum(0, 0), 0)
        self.assertEqual(self.solution.getSum(0, 5), 5)
        self.assertEqual(self.solution.getSum(5, 0), 5)
        self.assertEqual(self.solution.getSum(0, -5), -5)
        self.assertEqual(self.solution.getSum(-5, 0), -5)

    def test_positive_positive(self):
        self.assertEqual(self.solution.getSum(1, 1), 2)
        self.assertEqual(self.solution.getSum(10, 20), 30)
        self.assertEqual(self.solution.getSum(100, 900), 1000)
        self.assertEqual(self.solution.getSum(512, 256), 768)

    def test_positive_negative(self):
        self.assertEqual(self.solution.getSum(5, -3), 2)
        self.assertEqual(self.solution.getSum(3, -5), -2)
        self.assertEqual(self.solution.getSum(1000, -1000), 0)
        self.assertEqual(self.solution.getSum(7, -7), 0)
        self.assertEqual(self.solution.getSum(1, -1), 0)

    def test_negative_positive(self):
        self.assertEqual(self.solution.getSum(-5, 3), -2)
        self.assertEqual(self.solution.getSum(-3, 5), 2)
        self.assertEqual(self.solution.getSum(-1000, 1000), 0)
        self.assertEqual(self.solution.getSum(-7, 7), 0)

    def test_negative_negative(self):
        self.assertEqual(self.solution.getSum(-1, -2), -3)
        self.assertEqual(self.solution.getSum(-2, -3), -5)
        self.assertEqual(self.solution.getSum(-1000, -1000), -2000)
        self.assertEqual(self.solution.getSum(-100, -900), -1000)

    def test_boundaries(self):
        self.assertEqual(self.solution.getSum(1000, 1000), 2000)
        self.assertEqual(self.solution.getSum(-1000, -1000), -2000)
        self.assertEqual(self.solution.getSum(1000, -1000), 0)
        self.assertEqual(self.solution.getSum(-1000, 1000), 0)

    def test_carry_propagation(self):
        self.assertEqual(self.solution.getSum(3, 1), 4)
        self.assertEqual(self.solution.getSum(6, 1), 7)
        self.assertEqual(self.solution.getSum(7, 1), 8)
        self.assertEqual(self.solution.getSum(15, 1), 16)
        self.assertEqual(self.solution.getSum(255, 1), 256)
        self.assertEqual(self.solution.getSum(1048575, 1), 1048576)

    def test_large_negative_result(self):
        self.assertEqual(self.solution.getSum(-1000, -999), -1999)
        self.assertEqual(self.solution.getSum(-1, -1000), -1001)

    def test_symmetry(self):
        self.assertEqual(self.solution.getSum(123, 456), self.solution.getSum(456, 123))
        self.assertEqual(
            self.solution.getSum(-123, 456), self.solution.getSum(456, -123)
        )
        self.assertEqual(
            self.solution.getSum(-123, -456), self.solution.getSum(-456, -123)
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Bit Manipulation
