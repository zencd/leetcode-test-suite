# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Medium

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        raise Exception("Not solved yet")


import unittest


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.multiply("2", "3"), "6")
        self.assertEqual(self.solution.multiply("123", "456"), "56088")

    def test_zero(self):
        self.assertEqual(self.solution.multiply("0", "0"), "0")
        self.assertEqual(self.solution.multiply("0", "12345"), "0")
        self.assertEqual(self.solution.multiply("98765", "0"), "0")

    def test_single_digits(self):
        self.assertEqual(self.solution.multiply("1", "1"), "1")
        self.assertEqual(self.solution.multiply("9", "9"), "81")
        self.assertEqual(self.solution.multiply("5", "2"), "10")

    def test_multiplying_by_one(self):
        self.assertEqual(self.solution.multiply("1", "999"), "999")
        self.assertEqual(self.solution.multiply("100", "1"), "100")

    def test_trailing_zeros(self):
        self.assertEqual(self.solution.multiply("10", "10"), "100")
        self.assertEqual(self.solution.multiply("12", "10"), "120")
        self.assertEqual(self.solution.multiply("1000", "1000"), "1000000")

    def test_carry_propagation(self):
        self.assertEqual(self.solution.multiply("999", "999"), "998001")
        self.assertEqual(self.solution.multiply("5", "5"), "25")
        self.assertEqual(self.solution.multiply("99", "99"), "9801")

    def test_long_numbers(self):
        self.assertEqual(
            self.solution.multiply("123456789", "987654321"),
            str(int("123456789") * int("987654321")),
        )
        big1 = "9" * 100
        big2 = "9" * 100
        expected = str(int(big1) * int(big2))
        self.assertEqual(self.solution.multiply(big1, big2), expected)

    def test_max_length_inputs(self):
        num1 = "9" * 200
        num2 = "9" * 200
        self.assertEqual(
            self.solution.multiply(num1, num2),
            str(int(num1) * int(num2)),
        )

    def test_asymmetry(self):
        self.assertEqual(
            self.solution.multiply("123", "456"),
            self.solution.multiply("456", "123"),
        )

    def test_inner_zeros(self):
        self.assertEqual(self.solution.multiply("101", "101"), "10201")
        self.assertEqual(self.solution.multiply("1001", "1001"), "1002001")


if __name__ == "__main__":
    unittest.main()

# Tags: Math, String, Simulation
