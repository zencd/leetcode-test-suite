# 357. Count Numbers with Unique Digits
# https://leetcode.com/problems/count-numbers-with-unique-digits/
# Medium

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_n0(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(0), 1)

    def test_n1(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(1), 10)

    def test_n2(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(2), 91)

    def test_n3(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(3), 739)

    def test_n4(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(4), 5275)

    def test_n5(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(5), 32491)

    def test_n6(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(6), 168571)

    def test_n7(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(7), 712891)

    def test_n8(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(8), 2345851)

    def test_n_exceeds_max_digits(self):
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(9), 5611771)
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(10), 8877691)
        self.assertEqual(self.sol.countNumbersWithUniqueDigits(100), 8877691)

    def test_expected_values_bruteforce_small_n(self):
        for n in range(0, 4):
            expected = sum(len(set(str(x))) == len(str(x)) for x in range(10**n))
            self.assertEqual(self.sol.countNumbersWithUniqueDigits(n), expected)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Backtracking
