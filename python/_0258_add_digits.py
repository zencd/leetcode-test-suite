# 258. Add Digits
# https://leetcode.com/problems/add-digits/
# Easy

class Solution:
    def addDigits(self, num: int) -> int:
        raise Exception("Not solved yet")


import unittest


def brute_force(num: int) -> int:
    while num >= 10:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        num = total
    return num


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_zero(self):
        self.assertEqual(self.sol.addDigits(0), 0)

    def test_single_digits(self):
        for n in range(1, 10):
            self.assertEqual(self.sol.addDigits(n), n)

    def test_two_digits_requiring_second_step(self):
        self.assertEqual(self.sol.addDigits(38), 2)

    def test_two_digits_single_step(self):
        self.assertEqual(self.sol.addDigits(19), 1)
        self.assertEqual(self.sol.addDigits(27), 9)

    def test_nine_multiples(self):
        for n in (9, 18, 27, 99, 999, 9999, 99999):
            self.assertEqual(self.sol.addDigits(n), 9)

    def test_multi_digit(self):
        self.assertEqual(self.sol.addDigits(100), 1)
        self.assertEqual(self.sol.addDigits(123456), 3)
        self.assertEqual(self.sol.addDigits(123456789), 9)
        self.assertEqual(
            self.sol.addDigits(1234567890 % 2**31), brute_force(1234567890 % 2**31)
        )

    def test_max_constraint(self):
        self.assertEqual(self.sol.addDigits(2**31 - 1), 1)

    def test_matches_brute_force(self):
        for n in [
            0,
            1,
            2,
            5,
            9,
            10,
            11,
            12,
            19,
            20,
            29,
            37,
            38,
            39,
            40,
            98,
            99,
            100,
            101,
            109,
            110,
            199,
            200,
            299,
            989,
            990,
            1235,
            12348,
            4632,
            77777,
            100000,
            199999,
            999999,
            1234567,
            2147483647,
        ]:
            self.assertEqual(self.sol.addDigits(n), brute_force(n), f"num={n}")

    def test_property_range(self):
        for n in range(0, 2000):
            expected = 0 if n == 0 else 1 + (n - 1) % 9
            self.assertEqual(self.sol.addDigits(n), expected)

    def test_returns_int(self):
        self.assertIsInstance(self.sol.addDigits(38), int)


if __name__ == "__main__":
    unittest.main()

# Tags: Math, Simulation, Number Theory
