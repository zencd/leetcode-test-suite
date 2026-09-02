# 405. Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Easy

class Solution:
    def toHex(self, num: int) -> str:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero(self):
        self.assertEqual(self.solution.toHex(0), "0")

    def test_example_1(self):
        self.assertEqual(self.solution.toHex(26), "1a")

    def test_example_2(self):
        self.assertEqual(self.solution.toHex(-1), "ffffffff")

    def test_small_values(self):
        self.assertEqual(self.solution.toHex(1), "1")
        self.assertEqual(self.solution.toHex(9), "9")
        self.assertEqual(self.solution.toHex(10), "a")
        self.assertEqual(self.solution.toHex(15), "f")
        self.assertEqual(self.solution.toHex(16), "10")
        self.assertEqual(self.solution.toHex(255), "ff")
        self.assertEqual(self.solution.toHex(256), "100")

    def test_single_digit(self):
        for i, char in enumerate("0123456789abcdef"):
            self.assertEqual(self.solution.toHex(i), char)

    def test_max_int(self):
        self.assertEqual(self.solution.toHex(2**31 - 1), "7fffffff")

    def test_min_int(self):
        self.assertEqual(self.solution.toHex(-(2**31)), "80000000")

    def test_negative_values(self):
        self.assertEqual(self.solution.toHex(-2), "fffffffe")
        self.assertEqual(self.solution.toHex(-15), "fffffff1")
        self.assertEqual(self.solution.toHex(-16), "fffffff0")

    def test_no_leading_zeros(self):
        for value in range(0, 1000):
            expected = format(value, "x")
            self.assertEqual(self.solution.toHex(value), expected)

    def test_two_complement_matches_format(self):
        for value in list(range(-300, 300)):
            expected = format(value & 0xFFFFFFFF, "x")
            self.assertEqual(self.solution.toHex(value), expected)

    def test_lowercase_output(self):
        self.assertEqual(self.solution.toHex(255), self.solution.toHex(255).lower())
        self.assertNotIn("A", self.solution.toHex(-1))

    def test_all_bits_set(self):
        self.assertEqual(self.solution.toHex(-1), "f" * 8)

    def test_length_bounds(self):
        self.assertLessEqual(len(self.solution.toHex(16)), 8)
        self.assertEqual(len(self.solution.toHex(-1)), 8)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Bit Manipulation
