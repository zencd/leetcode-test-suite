# 400. Nth Digit
# https://leetcode.com/problems/nth-digit/
# Medium

class Solution:
    def findNthDigit(self, n: int) -> int:
        raise Exception("Not solved yet")


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def nth_digit_brute(self, n: int) -> int:
        seq = []
        i = 1
        while len(seq) < n:
            seq.extend(str(i))
            i += 1
        return int(seq[n - 1])

    def test_single_digits(self):
        for n in range(1, 10):
            self.assertEqual(self.sol.findNthDigit(n), n, f"n={n}")

    def test_example_1(self):
        self.assertEqual(self.sol.findNthDigit(3), 3)

    def test_example_2(self):
        self.assertEqual(self.sol.findNthDigit(11), 0)

    def test_two_digit_boundary(self):
        self.assertEqual(self.sol.findNthDigit(10), 1)
        self.assertEqual(self.sol.findNthDigit(12), 1)
        self.assertEqual(self.sol.findNthDigit(13), 1)
        self.assertEqual(self.sol.findNthDigit(19), 4)
        self.assertEqual(self.sol.findNthDigit(20), 1)
        self.assertEqual(self.sol.findNthDigit(21), 5)

    def test_three_digit_boundary(self):
        self.assertEqual(self.sol.findNthDigit(109), 9)
        self.assertEqual(self.sol.findNthDigit(110), 6)
        self.assertEqual(self.sol.findNthDigit(111), 0)
        self.assertEqual(self.sol.findNthDigit(112), 6)
        self.assertEqual(self.sol.findNthDigit(118), 6)
        self.assertEqual(self.sol.findNthDigit(119), 4)

    def test_four_digit_boundary(self):
        end_3digit = 9 + 90 * 2 + 900 * 3
        self.assertEqual(self.sol.findNthDigit(end_3digit), 9)
        self.assertEqual(self.sol.findNthDigit(end_3digit + 1), 1)
        self.assertEqual(self.sol.findNthDigit(end_3digit + 2), 0)
        self.assertEqual(self.sol.findNthDigit(end_3digit + 3), 0)
        self.assertEqual(self.sol.findNthDigit(end_3digit + 4), 0)

    def test_range_1_500(self):
        for n in range(1, 501):
            self.assertEqual(
                self.sol.findNthDigit(n), self.nth_digit_brute(n), f"n={n}"
            )

    def test_random_spot_checks(self):
        import random

        random.seed(42)
        for _ in range(30):
            n = random.randint(1, 20000)
            self.assertEqual(
                self.sol.findNthDigit(n), self.nth_digit_brute(n), f"n={n}"
            )

    def test_large_values(self):
        self.assertIsInstance(self.sol.findNthDigit(10**6), int)
        self.assertIsInstance(self.sol.findNthDigit(2**31 - 1), int)
        self.assertLessEqual(self.sol.findNthDigit(2**31 - 1), 9)
        self.assertGreaterEqual(self.sol.findNthDigit(2**31 - 1), 0)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Binary Search
