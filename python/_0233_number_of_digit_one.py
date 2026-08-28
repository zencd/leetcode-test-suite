# 233. Number of Digit One
# https://leetcode.com/problems/number-of-digit-one/
# Hard

class Solution:
    def countDigitOne(self, n: int) -> int:
        raise Exception("Not solved yet")


def brute(n: int) -> int:
    return sum(str(i).count("1") for i in range(n + 1))


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(self.sol.countDigitOne(0), 0)

    def test_one(self):
        self.assertEqual(self.sol.countDigitOne(1), 1)

    def test_below_ten(self):
        self.assertEqual(self.sol.countDigitOne(9), 1)

    def test_double_digits(self):
        self.assertEqual(self.sol.countDigitOne(10), 2)

    def test_eleven(self):
        self.assertEqual(self.sol.countDigitOne(11), 4)

    def test_thirteen(self):
        self.assertEqual(self.sol.countDigitOne(13), 6)

    def test_twenty(self):
        self.assertEqual(self.sol.countDigitOne(20), 12)

    def test_ninety_nine(self):
        self.assertEqual(self.sol.countDigitOne(99), 20)

    def test_one_hundred(self):
        self.assertEqual(self.sol.countDigitOne(100), 21)

    def test_one_hundred_one(self):
        self.assertEqual(self.sol.countDigitOne(101), 23)

    def test_one_hundred_ninety_nine(self):
        self.assertEqual(self.sol.countDigitOne(199), 140)

    def test_two_hundred(self):
        self.assertEqual(self.sol.countDigitOne(200), 140)

    def test_ninety_nine_thousand_nine_hundred_ninety_nine(self):
        self.assertEqual(self.sol.countDigitOne(99999), 50000)

    def test_one_million(self):
        self.assertEqual(self.sol.countDigitOne(1000000), 600001)

    def test_max_constraint(self):
        self.assertEqual(self.sol.countDigitOne(10**9), 900000001)

    def test_power_of_ten_values(self):
        for k in range(1, 10):
            self.assertEqual(self.sol.countDigitOne(10**k), k * 10 ** (k - 1) + 1)

    def test_brute_force_cross_check(self):
        for n in (
            1,
            5,
            8,
            12,
            15,
            21,
            49,
            50,
            90,
            105,
            111,
            119,
            199,
            222,
            499,
            500,
            1000,
            1234,
            2468,
            9999,
            10246,
        ):
            self.assertEqual(
                self.sol.countDigitOne(n), brute(n), msg=f"mismatch at n={n}"
            )

    def test_single_digit_sweep(self):
        self.assertEqual(
            [self.sol.countDigitOne(i) for i in range(11)],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
        )


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Dynamic Programming, Recursion
